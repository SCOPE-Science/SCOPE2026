# PowerSGD warm-start has an exact rank-two error law
## Finding

Let
\[
M\in\mathbb R^{n\times m}
\]
have rank two, with singular values
\[
\sigma_1\ge\sigma_2>0.
\]
Write
\[
\kappa=\frac{\sigma_1}{\sigma_2}.
\]

Consider source-form rank-one PowerSGD compression on the **same fixed matrix** at every step. Initialize
\[
q_0
\]
with independent standard Gaussian entries. For
\[
t\ge1,
\]
perform
\[
p_t
=
\frac{Mq_{t-1}}{\|Mq_{t-1}\|_2},
\qquad
q_t=M^\top p_t,
\]
and reconstruct
\[
C_t
=
p_tq_t^\top
=
p_tp_t^\top M.
\]

Then the expected squared Frobenius residual has the exact closed form
\[
\boxed{
\mathbb E\|M-C_t\|_F^2
=
\sigma_2^2
\left[
1+
\frac{\kappa^2-1}
{\kappa^{2t-1}+1}
\right].
}
\]

The best rank-one approximation has squared Frobenius residual
\[
\sigma_2^2.
\]
Therefore the exact expected multiplicative suboptimality of the \(t\)-th PowerSGD compression is
\[
\boxed{
R_t(\kappa)
=
1+
\frac{\kappa^2-1}
{\kappa^{2t-1}+1}.
}
\]

At the random start,
\[
\boxed{
R_1(\kappa)=\kappa,
}
\]
so
\[
\boxed{
\mathbb E\|M-C_1\|_F^2
=
\sigma_1\sigma_2.
}
\]

After only one warm-start reuse,
\[
\boxed{
R_2(\kappa)
=
1+
\frac{\kappa^2-1}{\kappa^3+1}
=
\frac{\kappa^2}{\kappa^2-\kappa+1}.
}
\]
For a large singular-value gap,
\[
R_2(\kappa)
=
1+\frac1\kappa+O(\kappa^{-2}).
\]

More generally, for every fixed
\[
t\ge2,
\]
\[
R_t(\kappa)-1
=
\frac{\kappa^2-1}{\kappa^{2t-1}+1}
=
O(\kappa^{3-2t}).
\]
Thus every additional reuse removes two powers of the singular-value ratio from the large-gap excess-error scale.

This gives an exact finite-step explanation of the source paper's empirical observation that warm-starting is crucial. On the minimal nontrivial rank-two model, a fresh random start can be a factor
\[
\kappa
\]
worse than the best rank-one error, while a single reuse is already asymptotically optimal as the spectral gap grows.

## Assumptions and scope

The matrix is fixed across compression steps. This isolates the warm-start mechanism from changing stochastic gradients.

The target rank is one and the true matrix rank is two.

The initial right factor is an isotropic standard Gaussian vector, exactly as in the source initialization.

The statement concerns compression error only. It does not claim an end-to-end convergence rate for error-feedback SGD.

The source PowerSGD implementation uses the previous right factor as the next initialization. Since only its direction matters in rank one, normalization of that factor is immaterial.

The case
\[
\kappa=1
\]
is included by continuity. Then every rank-one left subspace loses the same squared Frobenius energy
\[
\sigma_2^2,
\]
and the formula gives
\[
R_t(1)=1.
\]

## Proof

Because the Gaussian initialization is rotationally invariant, apply the singular-value decomposition and work in the two-dimensional right singular subspace. It is enough to take
\[
M
=
\begin{pmatrix}
\sigma_1&0\\
0&\sigma_2
\end{pmatrix},
\qquad
q_0
=
\begin{pmatrix}
z_1\\
z_2
\end{pmatrix},
\]
where
\[
z_1,z_2
\]
are independent standard Gaussians.

The scale of
\[
q_t
\]
does not matter for the next orthogonalization. From
\[
q_t=M^\top p_t
\]
and
\[
p_t\parallel Mq_{t-1},
\]
we obtain inductively
\[
q_{t-1}
\parallel
(M^\top M)^{t-1}q_0.
\]
Hence
\[
p_t
\parallel
\begin{pmatrix}
\sigma_1^{2t-1}z_1\\
\sigma_2^{2t-1}z_2
\end{pmatrix}.
\]

Since
\[
C_t=p_tp_t^\top M
\]
is the orthogonal projection of the columns of \(M\) onto the line spanned by \(p_t\),
\[
\|M-C_t\|_F^2
=
\|M\|_F^2-\|M^\top p_t\|_2^2.
\]
Substitution gives the pointwise identity
\[
\|M-C_t\|_F^2
=
\sigma_1^2\sigma_2^2
\frac{
\sigma_1^{4t-4}z_1^2
+
\sigma_2^{4t-4}z_2^2
}{
\sigma_1^{4t-2}z_1^2
+
\sigma_2^{4t-2}z_2^2
}.
\]

The radial part of the two-dimensional Gaussian cancels. Its direction is uniform, so write
\[
z_1=r\cos\theta,
\qquad
z_2=r\sin\theta,
\]
with uniform
\[
\theta.
\]
After dividing by
\[
\sigma_2^2
\]
and setting
\[
\kappa=\sigma_1/\sigma_2,
\]
the residual ratio becomes
\[
\kappa^2
\frac{
\kappa^{4t-4}\cos^2\theta+\sin^2\theta
}{
\kappa^{4t-2}\cos^2\theta+\sin^2\theta
}.
\]

Put
\[
a=\kappa^{4t-2}.
\]
The standard circle integral is
\[
\mathbb E_\theta
\frac1{a\cos^2\theta+\sin^2\theta}
=
\frac1{\sqrt a}.
\]
Let
\[
J_c
=
\mathbb E_\theta
\frac{\cos^2\theta}
{a\cos^2\theta+\sin^2\theta},
\qquad
J_s
=
\mathbb E_\theta
\frac{\sin^2\theta}
{a\cos^2\theta+\sin^2\theta}.
\]
The identities
\[
J_c+J_s=\frac1{\sqrt a}
\]
and
\[
aJ_c+J_s=1
\]
give
\[
J_c
=
\frac{1-a^{-1/2}}{a-1},
\qquad
J_s
=
\frac{a^{1/2}-1}{a-1}.
\]

Therefore
\[
R_t(\kappa)
=
\kappa^2
\left(
\kappa^{4t-4}J_c+J_s
\right).
\]
Substituting
\[
a^{1/2}=\kappa^{2t-1}
\]
and simplifying yields
\[
R_t(\kappa)
=
1+
\frac{\kappa^2-1}
{\kappa^{2t-1}+1}.
\]

At
\[
t=1,
\]
\[
R_1
=
1+\frac{\kappa^2-1}{\kappa+1}
=
\kappa.
\]
At
\[
t=2,
\]
\[
R_2
=
1+\frac{\kappa^2-1}{\kappa^3+1}
=
\frac{\kappa^2}{\kappa^2-\kappa+1}.
\]
The remaining asymptotics follow immediately.

## Verification

The accompanying `verify.py` reconstructs rank-one PowerSGD directly from the source matrix multiplications.

For several singular-value ratios it compares direct pointwise compression errors against the derived closed form for arbitrary Gaussian directions and multiple warm-start depths.

It then numerically integrates over the Gaussian direction angle and checks the exact expectation
\[
1+
\frac{\kappa^2-1}
{\kappa^{2t-1}+1}.
\]

It separately verifies the random-start identity
\[
\mathbb E\|M-C_1\|_F^2
=
\sigma_1\sigma_2
\]
and the one-reuse factor.

The numerical integration is only a transcription check. The expectation is evaluated analytically in the proof.

## Relationship to prior work

Vogels, Karimireddy, and Jaggi introduce PowerSGD as a low-rank gradient compressor based on subspace iteration. Their Algorithm 1 initializes the right factor with independent standard Gaussian entries, computes one left and one right matrix multiplication, and reuses the resulting factor at the next optimization step.

The paper explicitly identifies warm-start as a key feature. It reports that a single warm-started subspace-iteration step can match the empirical performance of a much more expensive best rank-\(r\) approximation. For a fixed matrix, its appendix gives the usual asymptotic subspace-iteration statement: with a singular-value gap and nonzero initial support, repeated iteration converges to the leading singular subspace.

That asymptotic convergence is prior and is not claimed here.

Classical randomized low-rank approximation theory gives general expected-error and tail bounds for Gaussian range finding and power schemes. The accepted result is narrower but exact: in the rank-one, rank-two, no-oversampling case matching PowerSGD initialization, it evaluates the complete finite-step Gaussian expectation and exposes the explicit warm-start factor
\[
1+
\frac{\kappa^2-1}
{\kappa^{2t-1}+1}.
\]

Focused searches for PowerSGD together with exact finite-step rank-two expected Frobenius error, Gaussian initialization, and warm-start singular-value laws did not identify an implication-equivalent published formula.

## Limitations

The matrix is stationary. Real stochastic gradients change between optimization steps, which is precisely why the source paper describes warm-start as an approximation to stochastic subspace tracking.

The result is rank one on a rank-two matrix. Higher target rank and larger spectra need not admit the same one-line expectation.

The theorem concerns squared Frobenius compression error, not spectral error or an optimizer-level convergence bound.

The large-gap conclusion should not be read as saying random initialization is poor in absolute terms: when
\[
\kappa
\]
is large, the first compression still removes most of the dominant energy. The exact statement is that its **residual relative to the best rank-one residual** is a factor
\[
\kappa.
\]

## References

1. Thijs Vogels, Sai Praneeth Karimireddy, and Martin Jaggi, “PowerSGD: Practical Low-Rank Gradient Compression for Distributed Optimization,” arXiv:1905.13727v1, first submitted 2019-05-31; NeurIPS 2019.
2. Nathan Halko, Per-Gunnar Martinsson, and Joel A. Tropp, “Finding Structure with Randomness: Probabilistic Algorithms for Constructing Approximate Matrix Decompositions,” SIAM Review 53(2), 2011, DOI:10.1137/090771806.
