# Reversal and sign symmetry force a half-variance maximum–endpoint law

## Finding

Let
\[
X=(X_1,\ldots,X_n)
\]
be a square-integrable real random vector. Assume only the two finite-horizon symmetries
\[
(X_1,\ldots,X_n)
\overset d=
(X_n,\ldots,X_1)
\tag{1}
\]
and
\[
(X_1,\ldots,X_n)
\overset d=
(-X_1,\ldots,-X_n).
\tag{2}
\]

Define
\[
S_0=0,
\qquad
S_k=\sum_{i=1}^kX_i,
\qquad
S=S_n,
\]
and
\[
M=\max_{0\le k\le n}S_k,
\qquad
m=\min_{0\le k\le n}S_k.
\]

For every odd measurable function \(g\) such that
\[
\mathbb E|Mg(S)|+\mathbb E|Sg(S)|<\infty,
\]
one has the exact identity
\[
\boxed{
\mathbb E[M g(S)]
=
\frac12\mathbb E[Sg(S)].
}
\tag{3}
\]

Since sign symmetry gives
\[
\mathbb E g(S)=0,
\]
equation (3) is equivalently
\[
\boxed{
\operatorname{Cov}(M,g(S))
=
\frac12\mathbb E[Sg(S)].
}
\tag{4}
\]

The terminal drawdown and the full path range satisfy the companion identities
\[
\boxed{
\operatorname{Cov}(M-S,g(S))
=
-\frac12\mathbb E[Sg(S)]
}
\tag{5}
\]
and
\[
\boxed{
\operatorname{Cov}(M-m,g(S))
=
0.
}
\tag{6}
\]

Taking
\[
g(x)=x
\]
gives the particularly simple half-variance law
\[
\boxed{
\operatorname{Cov}(M,S)
=
\frac12\operatorname{Var}(S).
}
\tag{7}
\]

Thus any square-integrable finite path with reversal-invariant increments and global sign symmetry has exactly half of its endpoint variance encoded in the maximum–endpoint covariance. Independence and exchangeability are not required.

For iid symmetric increments with
\[
\operatorname{Var}(X_1)=\sigma^2,
\]
equation (7) becomes
\[
\boxed{
\operatorname{Cov}(M,S)
=
\frac{n\sigma^2}{2}.
}
\tag{8}
\]

More generally, whenever the indicated moments exist,
\[
\boxed{
\mathbb E[M S^{2r+1}]
=
\frac12\mathbb E[S^{2r+2}],
\qquad
r=0,1,2,\ldots .
}
\tag{9}
\]

If the increments are iid and symmetric with
\[
0<\sigma^2<\infty
\]
and
\[
\mathbb E|X_1|^{2+\delta}<\infty
\]
for some \(\delta>0\), then the invariance principle and maximal-moment uniform integrability give
\[
\frac{\operatorname{Var}(M)}{n\sigma^2}
\longrightarrow
1-\frac2\pi.
\]
Combining this with (8),
\[
\boxed{
\operatorname{Corr}(M,S)
\longrightarrow
\frac{1}{2\sqrt{1-2/\pi}}
\approx0.829448.
}
\tag{10}
\]

## Assumptions and scope

The exact finite-horizon identity requires only reversal invariance and global sign symmetry of the increment vector.

The increments may be dependent and need not be exchangeable. For example, a mixture of sign-and-reversal orbits of deterministic increment vectors satisfies the hypotheses and can fail every nontrivial permutation symmetry beyond reversal.

Equation (10) uses stronger iid assumptions only for the asymptotic variance of the maximum. The finite identities (3)--(9) do not use independence, stationarity, a Markov property, or a lattice assumption.

The maximum includes time zero. This convention guarantees
\[
M\ge0,
\qquad
m\le0.
\]

## Proof

Let
\[
\mathcal R(X_1,\ldots,X_n)
=
(X_n,\ldots,X_1)
\]
be reversal.

For the reversed path, the partial sums are
\[
S_k^{\mathcal R}
=
S-S_{n-k}.
\]
Therefore its maximum is
\[
M^{\mathcal R}
=
S-m.
\tag{11}
\]
The terminal value remains \(S\).

By reversal invariance,
\[
(M,S)
\overset d=
(S-m,S).
\]
Hence
\[
\mathbb E[M g(S)]
=
\mathbb E[(S-m)g(S)].
\tag{12}
\]

Now apply global sign change. Under
\[
X\mapsto-X,
\]
the endpoint becomes \(-S\), while
\[
M\mapsto -m.
\]
Since \(g\) is odd,
\[
(-m)g(-S)=m g(S).
\]
Thus sign symmetry gives
\[
\mathbb E[M g(S)]
=
\mathbb E[m g(S)].
\tag{13}
\]

Substitute (13) into (12):
\[
\mathbb E[M g(S)]
=
\mathbb E[Sg(S)]
-
\mathbb E[M g(S)].
\]
Therefore
\[
2\mathbb E[M g(S)]
=
\mathbb E[Sg(S)],
\]
which proves (3).

Sign symmetry of \(S\) gives
\[
\mathbb E g(S)=0,
\]
so (4) follows.

For the drawdown,
\[
\mathbb E[(M-S)g(S)]
=
\mathbb E[M g(S)]
-
\mathbb E[Sg(S)]
=
-\frac12\mathbb E[Sg(S)],
\]
which proves (5).

Equation (13) gives
\[
\mathbb E[(M-m)g(S)]=0.
\]
The path range
\[
M-m
\]
is invariant under global sign change, while \(g(S)\) changes sign, so both expectations factor consistently and (6) follows.

Setting
\[
g(x)=x
\]
in (3), sign symmetry gives
\[
\mathbb ES=0,
\]
hence
\[
\mathbb E[MS]
=
\frac12\mathbb ES^2
=
\frac12\operatorname{Var}(S),
\]
which proves (7).

For iid symmetric increments,
\[
\operatorname{Var}(S)=n\sigma^2,
\]
giving (8). Equation (9) is (3) with
\[
g(x)=x^{2r+1}.
\]

For the asymptotic statement, Donsker's invariance principle gives
\[
\left(
\frac{S_{\lfloor nt\rfloor}}{\sigma\sqrt n}
\right)_{0\le t\le1}
\Longrightarrow
(B_t)_{0\le t\le1}.
\]
Hence
\[
\frac{M}{\sigma\sqrt n}
\Longrightarrow
\sup_{0\le t\le1}B_t.
\]
The Brownian maximum has the same distribution as
\[
|Z|,
\qquad
Z\sim N(0,1),
\]
so its variance is
\[
1-\frac2\pi.
\]

The finite \((2+\delta)\)-moment assumption and a standard maximal-moment inequality give uniform integrability of the squared normalized maxima. Therefore second moments converge and
\[
\frac{\operatorname{Var}(M)}{n\sigma^2}
\longrightarrow
1-\frac2\pi.
\]
Equation (10) now follows from (8).

## Verification

The accompanying checker uses exact rational arithmetic.

It first constructs several dependent increment laws as mixtures of finite orbits under only reversal and global sign change. These examples are deliberately nonexchangeable. For several odd functions, it verifies (3), (5), and (6) exactly.

It then exhaustively enumerates iid symmetric two-point and three-point increments for a range of sample sizes and verifies the half-variance covariance (8).

Finally, it computes the simple symmetric-walk joint law of \((M,S)\) by dynamic programming up to large \(n\) and confirms convergence of the exact finite-\(n\) correlation toward the constant in (10).

Finite replay is supplementary. The universal theorem is the two-symmetry argument in the proof.

## Relationship to prior work

Spitzer's identity classically gives the joint transform of a random-walk maximum and terminal drawdown for iid increments. Thus the iid specialization of (7) lies inside a much stronger classical joint-distribution theory.

Heinrich gives an elementary formulation of Spitzer's identity and explicitly investigates weaker exchangeability assumptions. The public full text is especially relevant because its posted correction states that the proposed cyclic-exchangeability proof actually needs independence. The present result does not attempt to extend Spitzer's full transform. It isolates one mixed-moment identity that survives under the substantially weaker pair of reversal and sign symmetries.

Anis and Gharib study moments, especially the variance, of maxima of partial sums under exchangeability. Their result concerns the marginal maximum rather than a maximum–endpoint mixed moment.

Blanchet and Glynn develop precise diffusion approximations for random-walk maxima and provide an archive-era primary \(60G50\) source for the random-walk maximum setting. Their work concerns all-time maxima and ladder-height expansions rather than the finite-horizon symmetry identity here.

Targeted searches for maximum–endpoint covariance, half-variance identities, odd-transform mixed moments, and reversal-invariant increment formulations did not locate (3)--(7).

## Limitations

The claim is not that the iid half-variance identity is outside classical Spitzer theory; the new scope is the weak symmetry class and the odd-transform family.

Reversal invariance alone is insufficient, as is sign symmetry alone. Both are used essentially in the proof.

The asymptotic correlation statement needs additional moment control beyond the exact finite identity.

A more abstract path-space formulation under involutive symmetries is possible, but is not claimed here.

## References

1. L. Heinrich, “An elementary proof of Spitzer's identity,” *Statistics* 16 (1985), 249–252, DOI 10.1080/02331888508801852.
2. A. A. Anis and M. Gharib, “On the variance of the maximum of partial sums of \(n\)-exchangeable random variables with applications,” *Journal of Applied Probability* 17 (1980), 432–439, DOI 10.2307/3213032.
3. J. Blanchet and P. W. Glynn, “Complete Corrected Diffusion Approximations for the Maximum of a Random Walk,” manuscript dated 2005-12-20; arXiv:math/0607121; *Annals of Applied Probability* 16 (2006), 951–983.
