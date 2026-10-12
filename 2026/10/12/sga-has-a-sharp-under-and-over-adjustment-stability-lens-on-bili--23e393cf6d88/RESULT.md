# SGA has a sharp under- and over-adjustment stability lens on bilinear games
## Finding

Symplectic Gradient Adjustment (SGA) augments a game's simultaneous gradient by a term derived from the antisymmetric part of the game Jacobian. In a bilinear zero-sum game that antisymmetric component is the entire Jacobian, so the discrete iteration can be solved exactly.

Consider
\[
\ell_1(x,y)=x^\top C y,
\qquad
\ell_2(x,y)=-x^\top C y,
\]
where
\[
C\in\mathbb R^{d\times d}
\]
is nonsingular and has singular values
\[
\mu\le \sigma_j\le L,
\qquad
0<\mu\le L.
\]
Let
\[
z=
\begin{bmatrix}
x\\
y
\end{bmatrix},
\qquad
J=
\begin{bmatrix}
0&C\\
-C^\top&0
\end{bmatrix}.
\]
The simultaneous game gradient is
\[
F(z)=Jz,
\]
and
\[
J^\top=-J.
\]

With positive symplectic-adjustment strength
\[
\tau>0,
\]
the source SGA field is
\[
\Gamma_\tau(z)
=
F(z)+\tau J^\top F(z)
=
(I-\tau J)Jz.
\]
Apply an explicit step with
\[
\eta>0:
\qquad
z^+=z-\eta\Gamma_\tau(z).
\]

On the invariant two-dimensional plane associated with a singular value
\[
\sigma,
\]
write the skew action as
\[
J=\sigma R,
\qquad
R^2=-I.
\]
Then
\[
z^+
=
\left[
(1-\eta\tau\sigma^2)I-\eta\sigma R
\right]z.
\]
Its exact squared Euclidean contraction factor is
\[
\boxed{
r_\sigma^2
=
(1-\eta\tau\sigma^2)^2+\eta^2\sigma^2.
}
\]

Consequently the SGA iteration converges linearly to the unique Nash equilibrium from every initial point if and only if
\[
\boxed{
0<\eta<
\frac{2\tau}{1+\tau^2L^2}.
}
\]
At equality the top singular mode has
\[
r_L=1,
\]
so a nonzero initialization in that mode does not converge. Above the threshold,
\[
r_L>1,
\]
and that mode expands geometrically. The boundary is therefore sharp.

A dimensionless form exposes a second phenomenon. Put
\[
s=\eta L,
\qquad
u=\tau L.
\]
The exact stability condition is
\[
\boxed{
s(1+u^2)<2u.
}
\]
For fixed
\[
u>0,
\]
the largest stable normalized step is
\[
\frac{2u}{1+u^2},
\]
whose maximum over all adjustment strengths is
\[
1,
\]
attained at
\[
u=1.
\]
Thus no positive SGA adjustment stabilizes an explicit step with
\[
s\ge1.
\]

Conversely, for a fixed normalized step
\[
0<s<1,
\]
the complete stable adjustment interval is
\[
\boxed{
\frac{1-\sqrt{1-s^2}}{s}
<
u
<
\frac{1+\sqrt{1-s^2}}{s}.
}
\]
The two endpoints multiply to one. Hence fixed-step SGA has a genuine *stability lens*: too little adjustment leaves too much rotation, while too much adjustment makes the added radial term too stiff for the same explicit step.

A later general quadratic-game analysis proves linear convergence under the sufficient step restriction
\[
\eta
<
\frac{\tau\mu^2}
{(1+\tau^2L^2)L^2}
\]
on this pure-skew specialization. The exact ceiling above is larger by the sharp ratio
\[
\boxed{
2\left(\frac{L}{\mu}\right)^2.
}
\]
Thus the sufficient general bound can be quadratically conservative in the singular-value condition number even on the most elementary full-rank bilinear family.

## Assumptions and scope

The theorem concerns a square, full-rank bilinear zero-sum game, so the Nash equilibrium
\[
z=0
\]
is unique.

The adjustment strength
\[
\tau
\]
is positive and fixed. The explicit outer step
\[
\eta
\]
is also fixed.

The source algorithm can choose the sign of its adjustment using an alignment test. On a pure Hamiltonian bilinear game the positive adjustment is the convergent orientation and is the case studied here.

The result is an exact deterministic linear stability classification. It does not claim that the same threshold holds for nonlinear games, stochastic gradients, approximate Jacobians, or low-rank SGA variants.

## Proof

Take a singular value decomposition
\[
C=U\Sigma V^\top.
\]
Under the orthogonal change of variables
\[
x=U\hat x,
\qquad
y=V\hat y,
\]
the matrix
\[
J
\]
splits into independent two-dimensional skew blocks
\[
J_\sigma
=
\sigma
\begin{bmatrix}
0&1\\
-1&0
\end{bmatrix}
=
\sigma R.
\]

Because
\[
J^\top=-J,
\]
the defining SGA field is
\[
F+\tau J^\top F
=
Jz-\tau J^2z.
\]
On a singular block,
\[
J_\sigma^2=-\sigma^2I,
\]
so
\[
\Gamma_{\tau,\sigma}
=
(\sigma R+\tau\sigma^2I)z.
\]
The explicit iteration matrix on that block is therefore
\[
M_\sigma
=
(1-\eta\tau\sigma^2)I-\eta\sigma R.
\]

Since
\[
R^\top=-R
\]
and
\[
R^\top R=I,
\]
one obtains
\[
M_\sigma^\top M_\sigma
=
\left[
(1-\eta\tau\sigma^2)^2+\eta^2\sigma^2
\right]I.
\]
This proves the exact modal factor.

For
\[
\eta>0,
\]
the strict inequality
\[
r_\sigma^2<1
\]
is equivalent to
\[
-2\eta\tau\sigma^2
+
\eta^2\tau^2\sigma^4
+
\eta^2\sigma^2
<0,
\]
and, after division by
\[
\eta\sigma^2>0,
\]
to
\[
\eta(1+\tau^2\sigma^2)<2\tau.
\]
Thus mode
\[
\sigma
\]
is strictly contractive exactly when
\[
\eta<
\frac{2\tau}{1+\tau^2\sigma^2}.
\]
The right-hand side decreases with
\[
\sigma,
\]
so simultaneous contraction of every singular mode is equivalent to the displayed threshold at
\[
\sigma=L.
\]

Because the entire iteration is an orthogonal direct sum of these scaled rotations, strict contraction of every block is equivalent to linear convergence from every initial point.

At equality the
\[
L
\]
block has Euclidean factor one. Above equality it has factor greater than one. These top-mode initializations prove necessity and sharpness.

For the dimensionless form, substitute
\[
s=\eta L,
\qquad
u=\tau L.
\]
The top-mode condition becomes
\[
s(1+u^2)<2u.
\]
For fixed
\[
u,
\]
the ceiling
\[
2u/(1+u^2)
\]
is maximized at
\[
u=1
\]
with value one. For fixed
\[
0<s<1,
\]
the quadratic inequality
\[
su^2-2u+s<0
\]
holds exactly between its roots
\[
u_\pm
=
\frac{1\pm\sqrt{1-s^2}}{s}.
\]
Their product is one.

Finally, on this pure-skew family the later general quadratic-game sufficient bound reduces to
\[
\eta_{\rm suff}
=
\frac{\tau\mu^2}
{(1+\tau^2L^2)L^2}.
\]
Dividing the exact ceiling by this quantity gives
\[
\frac{
2\tau/(1+\tau^2L^2)
}{
\tau\mu^2/[(1+\tau^2L^2)L^2]
}
=
2\left(\frac{L}{\mu}\right)^2.
\]

## Verification

The accompanying `verify.py` reconstructs the bilinear game matrix and the source SGA adjustment.

It checks the singular-mode formula against full matrices built from random orthogonal singular-vector bases, verifies contraction below the exact threshold, unit norm at the boundary, expansion above it, tests the reciprocal adjustment-window roots, and verifies the exact ratio to the later sufficient quadratic-game bound.

The numerical checks are transcription guards. The if-and-only-if theorem is proved algebraically above.

## Relationship to prior work

Balduzzi and coauthors introduced SGA from the symmetric/antisymmetric decomposition of differentiable games. Their minimal zero-sum example identifies the original simultaneous gradient as rotational and the antisymmetric correction as radial, and their algorithm outputs the adjusted field
\[
F+\tau A^\top F.
\]
Their experiments emphasize improved robustness over a range of learning rates, but the inspected source does not state a sharp discrete-time stability boundary jointly in the outer step and adjustment strength.

The expanded differentiable-game treatment explicitly notes that the same adjustment was independently discovered by Gemp and Mahadevan as “Crossing-the-Curl.” On the elementary rotational subsystem, that work shows that the curl-derived correction points radially and establishes strong monotonicity properties for related fields. It does not state the exact explicit-Euler stability lens above for a general full singular spectrum.

A later convergence analysis of SGA and low-rank SGA proves global linear convergence for quadratic games under a sufficient parameter bound. Specializing its SGA theorem to the present pure-skew bilinear family gives
\[
\eta
<
\frac{\tau\mu^2}
{(1+\tau^2L^2)L^2}.
\]
The exact classification here shows that this sufficient bound is conservative by the explicit factor
\[
2(L/\mu)^2.
\]

Focused published-record searches for SGA bilinear stability, singular-value mode factors, fixed-step over-adjustment, and equivalent adjustment-window formulations did not identify an implication-equivalent exact threshold.

## Limitations

The theorem uses an exactly bilinear, full-rank, zero-sum game and an exact antisymmetric Jacobian.

It analyzes a fixed-step explicit SGA iteration rather than an adaptive optimizer wrapped around the adjusted field.

The later sufficient-bound comparison is specific to the pure-skew specialization of that theorem.

The exact linear analysis does not determine nonlinear basins, stochastic robustness, or behavior under low-rank Jacobian approximation.

## References

1. David Balduzzi, Sebastien Racaniere, James Martens, Jakob Foerster, Karl Tuyls, and Thore Graepel, “The Mechanics of n-Player Differentiable Games,” arXiv:1802.05642v1, first submitted 2018-02-15; ICML 2018.
2. Alistair Letcher, David Balduzzi, Sebastien Racaniere, James Martens, Jakob Foerster, Karl Tuyls, and Thore Graepel, “Differentiable Game Mechanics,” Journal of Machine Learning Research 20(84), 2019.
3. Ian Gemp and Sridhar Mahadevan, “Global Convergence to the Equilibrium of GANs using Variational Inequalities,” arXiv:1808.01531v1, first submitted 2018-08-04.
4. Nadja Vater, Katherine Rossella Foglia, Vittorio Colao, and Alfio Borzì, “A Low-Rank Symplectic Gradient Adjustment Method for Computing Nash Equilibria,” arXiv:2510.25716, 2025.
