# A universal codimension-three singular locus for the Grassmannian isotropic quadric
## Finding
Let \(V=\mathbf C^n\) carry the standard nondegenerate symmetric bilinear form \(q\), let \(2\le k\le n-2\), and let
\[
D_{k,n}
=
\operatorname{Gr}(k,V)\cap
\left\{
\sum_{|I|=k}p_I^2=0
\right\}
\]
be the isotropic-quadric section in the Plücker embedding. Then
\[
\operatorname{Sing}(D_{k,n})
=
\Sigma_2
:=
\left\{
W\in\operatorname{Gr}(k,V):
\dim(W\cap W^{\perp_q})\ge2
\right\},
\]
and
\[
\operatorname{codim}_{\operatorname{Gr}(k,V)}
\operatorname{Sing}(D_{k,n})=3.
\]

More generally, for every integer \(r\) with
\[
1\le r\le\min(k,n-k),
\]
the exact-radical stratum
\[
\Sigma_r^\circ
=
\left\{
W:
\dim(W\cap W^{\perp_q})=r
\right\}
\]
has dimension
\[
\dim\Sigma_r^\circ
=
k(n-k)-\binom{r+1}{2}.
\]
Consequently the closed degeneracy locus
\[
\Sigma_r
=
\left\{
W:
\dim(W\cap W^{\perp_q})\ge r
\right\}
\]
has codimension \(\binom{r+1}{2}\). In particular, the general-\(k\) codimension bound in Friedman--Hoşten--Rosana, Theorem 2.3, can be sharpened from at most \(\binom{k+1}{2}\) to exactly \(3\).

## Assumptions and scope
Everything is over \(\mathbf C\). The bilinear form \(q\) is nondegenerate. The range \(2\le k\le n-2\) is essential for the codimension-three singular stratum to be nonempty. For \(k=1\) or \(k=n-1\), the corresponding Plücker quadric section is smooth.

The statement concerns the singular geometry of the isotropic-quadric section. It does not assert that every three-dimensional projective model inside \(\operatorname{Gr}(k,n)\) meets this singular locus, and therefore it does not replace the separate dimension obstruction for ED-generality proved in the initiating source.

## Proof
Choose the standard affine chart on \(\operatorname{Gr}(k,n)\) in which a \(k\)-plane is the row space of
\[
A=[I_k\ B],
\qquad
B\in\operatorname{Mat}_{k\times(n-k)}(\mathbf C).
\]
By Cauchy--Binet,
\[
\sum_{|I|=k}\det(A_I)^2
=
\det(AA^{\mathsf T})
=
\det(I_k+BB^{\mathsf T}).
\]
Thus on this chart \(D_{k,n}\) is the determinant hypersurface
\[
F(B)=\det M(B)=0,
\qquad
M(B)=I_k+BB^{\mathsf T}.
\]
The matrix \(M(B)\) is the Gram matrix of \(q|_W\), so
\[
\dim\ker M(B)=\dim(W\cap W^{\perp_q}).
\]

Differentiating the determinant gives
\[
dF
=
\operatorname{tr}\!\left(
\operatorname{adj}(M)\,dM
\right),
\qquad
dM=dB\,B^{\mathsf T}+B\,dB^{\mathsf T},
\]
hence
\[
\nabla_BF
=
2\,\operatorname{adj}(M)B.
\]
If \(\operatorname{rank}M\le k-2\), then \(\operatorname{adj}(M)=0\), so the point is singular. Conversely, suppose \(\operatorname{rank}M=k-1\). Then
\[
\operatorname{adj}(M)=c\,vv^{\mathsf T}
\]
for some \(c\ne0\) and nonzero \(v\in\ker M\). If the gradient vanished, then \(v^{\mathsf T}B=0\), equivalently \(B^{\mathsf T}v=0\). But then
\[
Mv
=
v+B(B^{\mathsf T}v)
=
v\ne0,
\]
contradicting \(v\in\ker M\). Therefore every corank-one point of \(D_{k,n}\) is smooth and
\[
\operatorname{Sing}(D_{k,n})=\Sigma_2.
\]

It remains to compute the dimensions of the radical strata. Fix \(r\) with
\[
1\le r\le\min(k,n-k)
\]
and let \(R=W\cap W^{\perp_q}\) have dimension \(r\). First choose \(R\) as a totally isotropic \(r\)-plane. The orthogonal Grassmannian of such \(R\) has dimension
\[
r(n-r)-\binom{r+1}{2}.
\]
For fixed \(R\), the quotient \(R^\perp/R\) is a nondegenerate quadratic space of dimension \(n-2r\), and \(W/R\) is a \((k-r)\)-plane in it on which the induced form is nondegenerate. Nondegeneracy is open, so the fiber has dimension
\[
(k-r)(n-k-r).
\]
Adding gives
\[
\dim\Sigma_r^\circ
=
r(n-r)-\binom{r+1}{2}
+
(k-r)(n-k-r)
=
k(n-k)-\binom{r+1}{2}.
\]
Hence \(\Sigma_r\) has codimension \(\binom{r+1}{2}\). For \(r=2\) this is \(3\), and the stratum is nonempty precisely in the stated range \(2\le k\le n-2\).

## Verification
The accompanying checker verifies the dimension identity for \(678\) admissible triples \((n,k,r)\) with \(4\le n\le20\), symbolically verifies the Cauchy--Binet chart identity for \(k=2\) and \(k=3\), and checks exact corank-two singular and corank-one smooth witnesses for \(2\le k\le10\). These finite checks are consistency tests only. The theorem for all admissible \(n,k,r\) is established by the symbolic argument above.

For example, taking
\[
B=\operatorname{diag}(i,i,1,\ldots,1)
\]
gives a Gram matrix \(I_k+BB^{\mathsf T}\) of corank \(2\), and the exact symbolic gradient vanishes. Replacing the second \(i\) by \(1\) gives corank \(1\), and the exact symbolic gradient is nonzero.

## Relationship to prior work
Friedman--Hoşten--Rosana identify this Plücker quadric as the relevant non-transversality divisor for Euclidean-distance optimization on \(\operatorname{Gr}(k,n)\). Their Theorem 2.3 gives the general upper bound
\[
\operatorname{codim}\operatorname{Sing}(D_{k,n})
\le
\binom{k+1}{2},
\]
and their \(k=2\) analysis yields the exact codimension \(3\) case. The calculation above shows that codimension \(3\) is in fact universal for every \(2\le k\le n-2\).

The earlier paper of Friedman--Rosana--Sturmfels develops the metric algebraic geometry only for \(\operatorname{Gr}(2,n)\), so it does not cover the higher-\(k\) statement. Classical symmetric-degeneracy literature contains the local fact that corank at least \(2\) has codimension \(3\) in a space of symmetric forms; for example, Agrachev--Gamkrelidze record this for the determinant hypersurface in a Lagrangian-Grassmannian chart. The point needed here is the global pullback to the ordinary Plücker Grassmannian together with the exact radical-stratum dimension calculation.

## Limitations
No statement is made about the degree, irreducible-component structure in maximal-isotropic boundary cases, or scheme-theoretic multiplicities of the loci \(\Sigma_r\). The result is over \(\mathbf C\) and uses a nondegenerate symmetric form. The exact codimension computation by itself does not imply a stronger universal dimension cutoff for ED-generality, because avoiding a codimension-three subvariety is not controlled solely by dimension inside an arbitrary projective ambient variety.

A residual originality risk remains that older orthogonal-degeneracy or quadratic-Grassmannian literature may state the same global radical-stratum formula under different terminology. The checked sources contain the local symmetric-matrix analogue and the \(k=2\) Grassmannian case, but no checked source states the all-\(k\) conclusion above.

## References
1. Hannah Friedman, Serkan Hoşten, Andrea Rosana, *Euclidean Distance Optimization Within the Grassmannian*, arXiv:2610.02018v1, 2026.
2. Hannah Friedman, Andrea Rosana, Bernd Sturmfels, *Distance Optimization in the Grassmannian of Lines*, arXiv:2601.22843v1, 2026.
3. A. Agrachev, R. Gamkrelidze, *Symplectic Methods for Optimization and Control*, Section 4, determinant-hypersurface discussion.
4. Graham Denham, Mathias Schulze, Uli Walther, *Matroid connectivity and singularities of configuration hypersurfaces*, arXiv:1902.06507v4.
