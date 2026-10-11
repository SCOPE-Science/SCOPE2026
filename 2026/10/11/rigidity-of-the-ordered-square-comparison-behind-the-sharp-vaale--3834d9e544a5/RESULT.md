# Rigidity of the ordered-square comparison behind the sharp Vaaler surface bound

## Finding

For an integer \(n\ge2\), define the positive ordered Gaussian integral
\[
\mathcal I(q_1,\ldots,q_n)
=
\int_{z_1>\cdots>z_n>0}
\exp\!\left(
-\frac12\sum_{j=1}^n q_jz_j^2
\right)\,dz,
\]
where \(q_j>0\). Put
\[
r_k=\sum_{j=1}^kq_j,
\qquad
1\le k\le n,
\]
and assume
\[
r_k\ge k
\qquad
(1\le k\le n).
\]

The ordered-square comparison used in the recent sharp surface-area extension of Vaaler's theorem states
\[
\sqrt{q_1}\,
\mathcal I(q_1,\ldots,q_n)
\le
\mathcal I(1,\ldots,1).
\]
For every \(n\ge2\), equality is rigid:
\[
\boxed{
\sqrt{q_1}\,
\mathcal I(q_1,\ldots,q_n)
=
\mathcal I(1,\ldots,1)
\quad\Longleftrightarrow\quad
q_1=\cdots=q_n=1.
}
\]

Consequently, consider the source orthoscheme
\[
B=\operatorname{conv}\{0,b_1,\ldots,b_n\},
\]
written in orthonormal coordinates as
\[
b_k=(\beta_1,\ldots,\beta_k,0,\ldots,0),
\qquad
\beta_j>0.
\]
If
\[
|b_k|\ge\sqrt{k}
\qquad
(1\le k\le n),
\]
then equality in the source's sharp local surface-to-unit-ball-sector estimate holds if and only if
\[
\beta_1=\cdots=\beta_n=1.
\]
Equivalently, the equality orthoscheme is, up to an orthogonal transformation, exactly
\[
\operatorname{conv}
\left\{
0,\,
e_1,\,
e_1+e_2,\,
\ldots,\,
e_1+\cdots+e_n
\right\},
\]
one of the standard flag orthoschemes in the cube.

The dimension assumption is necessary. For \(n=1\), the source comparison reduces by rescaling to an identity for every admissible \(q_1\).

## Assumptions and scope

The finding concerns the equality case of the ordered-square comparison and the orthoscheme sector estimate that form the local analytic core of the surface-area theorem in arXiv:2609.27798v1.

It does not assert that the cube is the unique global equality polytope in that theorem. The global proof also passes through a flag decomposition and geometric comparisons before the local orthoscheme estimate is applied. The present result identifies the unique equality geometry at the local Gaussian-comparison step for \(n\ge2\).

The integration region is the open Weyl chamber
\[
D_n=\{z\in\mathbb R^n:z_1>\cdots>z_n>0\}.
\]
Replacing strict inequalities by non-strict inequalities does not change the integral because the boundary has Lebesgue measure zero.

## Proof

The source proof begins with
\[
q_1=r_1\ge1.
\]
For \(n\ge2\), make its ordered-square substitution
\[
w_1^2
=
q_1z_1^2-(q_1-1)z_2^2,
\qquad
w_j=z_j
\quad
(2\le j\le n).
\]
Because \(z_1>z_2>0\) and \(q_1\ge1\), this gives a bijection of \(D_n\) with itself. Its inverse satisfies
\[
q_1z_1^2
=
w_1^2+(q_1-1)w_2^2.
\]
After multiplication by the prefactor \(\sqrt{q_1}\), the Jacobian contribution is
\[
J(w)
=
\frac{w_1}{\sqrt{q_1}\,z_1}
=
\frac{w_1}{
\sqrt{w_1^2+(q_1-1)w_2^2}
}
\le1.
\]
The transformed quadratic form has coefficient sequence
\[
\widetilde q_1=1,\qquad
\widetilde q_2=q_1+q_2-1,\qquad
\widetilde q_j=q_j
\quad
(j\ge3).
\]
Its first prefix sum is \(1\), and every later prefix sum is exactly \(r_k\). Hence the same summation-by-parts identity used in the source gives
\[
\sum_{j=1}^n\widetilde q_jw_j^2
\ge
\sum_{j=1}^nw_j^2.
\]
Thus the transformed Gaussian factor is pointwise at most the standard one.

If \(q_1>1\), then \(w_2>0\) throughout \(D_n\), so
\[
J(w)<1
\]
at every interior point. The transformed integrand is therefore strictly smaller than the standard Gaussian integrand throughout \(D_n\). Hence equality can occur only when
\[
q_1=1.
\]

Now assume \(q_1=1\). The substitution is the identity. Write
\[
\delta_k=r_k-k\ge0,
\qquad
1\le k\le n,
\]
and set
\[
z_{n+1}=0.
\]
A summation-by-parts identity gives
\[
\sum_{j=1}^n(q_j-1)z_j^2
=
\sum_{k=1}^n
\delta_k
\left(
z_k^2-z_{k+1}^2
\right).
\]
Every difference on the right is strictly positive on \(D_n\). Hence, if any
\[
\delta_k>0,
\]
then
\[
\sum_{j=1}^nq_jz_j^2
>
\sum_{j=1}^nz_j^2
\]
throughout the integration region, so the positive Gaussian integral is strictly smaller. Equality therefore forces
\[
\delta_k=0
\qquad
(1\le k\le n),
\]
that is,
\[
r_k=k
\qquad
(1\le k\le n).
\]
Taking successive differences gives
\[
q_k=r_k-r_{k-1}=1
\qquad
(1\le k\le n).
\]
The converse is immediate, proving the integral rigidity.

For the orthoscheme application, the source writes
\[
q_j=\beta_j^2.
\]
Then
\[
r_k
=
\sum_{j=1}^k\beta_j^2
=
|b_k|^2
\ge k.
\]
In the source's exact reduction, the local surface-to-unit-ball-sector quotient differs from
\[
\frac{1}{
\beta_1\mathcal I(q_1,\ldots,q_n)
}
\]
only by a positive dimension-dependent factor. Since
\[
\beta_1=\sqrt{q_1},
\]
equality in the local sharp estimate is equivalent to equality in the ordered-square comparison. The integral rigidity therefore gives
\[
\beta_j^2=1
\]
for every \(j\). Positivity of the \(\beta_j\) yields
\[
\beta_j=1,
\]
and the listed standard cube orthoscheme follows.

For \(n=1\), direct rescaling gives
\[
\sqrt{q_1}\mathcal I(q_1)=\mathcal I(1),
\]
so no one-dimensional rigidity is possible.

## Verification

The proof is analytic and uses only the source change of variables, positivity of the Gaussian integrand, and an exact summation-by-parts identity.

The bundled checker symbolically verifies the inverse/Jacobian identity and the summation-by-parts formula for arbitrary symbolic dimension through coefficient comparison. It also checks exact rational examples with admissible strict prefix slack and confirms that the quadratic excess is positive on ordered positive test points.

These computations are consistency checks only. The infinite-dimensional family of parameter choices is covered by the displayed analytic argument, not by finite testing.

## Relationship to prior work

Zwierzyński proves the all-dimensional surface-area inequality and introduces the ordered-square comparison that makes the orthoscheme estimate dimension-free. The paper proves the non-strict inequality but does not state an equality characterization for the ordered-square lemma or for the resulting local orthoscheme quotient.

Karasev's earlier paper proves the surface-area theorem only in dimensions \(2\) and \(3\). It states that the cube attains equality, but it does not give an if-and-only-if equality classification and does not contain the later all-dimensional ordered-square comparison.

Targeted searches for equality in the ordered-square comparison, rigidity of the orthoscheme sector estimate, standard-cube flag orthoschemes as unique local extremizers, and broader equality formulations for the Vaaler surface theorem found no statement implying the result above.

## Limitations

The result is local to the analytic orthoscheme step. It does not prove global uniqueness of the cube among all polytopes satisfying the face-distance assumptions, because equality must also be traced through every geometric step of the flag decomposition.

No quantitative stability modulus is proved. The argument detects any nonzero prefix slack by strict positivity, but it does not convert the amount of slack into an explicit deficit in the surface-to-sector quotient.

The one-dimensional case is genuinely non-rigid under this normalization.

## References

1. M. Zwierzyński, *A Sharp Surface-Area Extension of Vaaler's Theorem*, arXiv:2609.27798v1, first public 19 August 2026. Primary MSC 52A38.
2. R. Karasev, *Rogers's proof of Vaaler's theorem*, arXiv:2505.16247v1, first public 22 May 2025. Primary MSC 52A38.
