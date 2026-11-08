# A hidden type jump in the Jacobian singular schemes of line arrangements

## Finding

Let \(k\) be an algebraically closed field of characteristic \(p\geq 0\), and let \(C\subset\mathbb P^2_k\) be an arbitrary reduced union of projective lines. At a point \(P\) where exactly \(m\geq2\) distinct component lines meet, let \(T_P\) be the local Tjurina algebra of the **intrinsic singular subscheme** of \(C\), defined in affine coordinates by the local equation and its two first partial derivatives. Then:

1. For every characteristic, \(\dim_k T_P=(m-1)^2\) and its associated graded Hilbert series is \(\big(1+t+\cdots+t^{m-2}\big)^2\).
2. If \(p=0\), or \(p\nmid m\), or \(m=2\), the algebra \(T_P\) is Artinian Gorenstein of socle dimension \(1\), and its minimal graded resolution is the complete-intersection resolution of two forms of degree \(m-1\).
3. If \(p>0\), \(p\mid m\), and \(m\geq3\), the algebra \(T_P\) has Cohen–Macaulay type exactly \(2\), despite having *exactly the same Hilbert function* as the Gorenstein case. Its minimal graded free resolution over \(S=k[u,v]\) is
\[
0\longrightarrow S(-m)\oplus S(-(2m-2))
\longrightarrow S(-(m-1))^{\oplus2}\oplus S(-m)
\longrightarrow S\longrightarrow T_P\longrightarrow0.
\]
Its socle has two one-dimensional homogeneous components in degrees \(m-2\) and \(2m-4\). In particular, the singular subscheme is **not** locally a complete intersection at precisely the multiple points of multiplicity at least three divisible by the characteristic.

The conclusion applies to every reduced line arrangement, independent of the number and configuration of its other lines. It distinguishes a genuinely scheme-theoretic wild-characteristic jump that both the reduced singular-point configuration and the Tjurina lengths fail to detect.

## Assumptions and scope

The ground field is algebraically closed; the assertions are characteristic-independent whenever such a collection of distinct lines exists. A point of multiplicity \(m\) means that exactly \(m\) pairwise distinct lines of the arrangement pass through it. All local rings are at the indicated intersection point. The graded structure is obtained from the homogeneous tangent-line equation after multiplying the local affine equation by a unit. The relevant singular scheme is \(\operatorname{Spec}\big(k[[u,v]]/(f,f_u,f_v)\big)\); the equation \(f\) must be included, especially when the characteristic divides the total degree of the projective defining equation. The assertions concern line arrangements, not arbitrary plane-curve germs with the same tangent cone but additional higher-order terms.

## Proof

After translating \(P\) to the origin and changing affine coordinates, the product of the \(m\) lines through \(P\) is a squarefree homogeneous binary form \(F=\prod_{i=1}^{m} L_i\in S=k[u,v]\). The other component lines contribute a unit \(U\) in the completed local ring. Since \((UF,(UF)_u,(UF)_v)=(F,F_u,F_v)\), it suffices to study the homogeneous algebra \(A=S/(F,F_u,F_v)\); the latter is supported only at \((u,v)\), and its completion equals \(T_P\).

If the characteristic does not divide \(m\), Euler's identity \(uF_u+vF_v=mF\) gives \(F\in(F_u,F_v)\). The partial derivatives have no common projective zero: Euler would force \(F=0\), whereas at each distinct line factor the gradient of \(F\) is nonzero. Thus \(F_u,F_v\) form a homogeneous regular sequence of degree \(m-1\). This proves the complete-intersection resolution, Hilbert series, and one-dimensional top socle.

Assume now that \(p>0\) divides \(m\), with \(m\geq3\). Euler gives \(uF_u+vF_v=0\). Since \(u,v\) are coprime in \(S\), there is a homogeneous \(H\in S_{m-2}\) with
\[
F_u=vH,\qquad F_v=-uH.
\]
No linear factor of \(F\) divides \(H\): otherwise the gradient of the squarefree product would vanish at the generic smooth point of that component line. Hence \(F,H\) are coprime. The Tjurina ideal is
\[
I=(F,uH,vH),\qquad \sqrt I=(u,v).
\]
Write \(F=uB+vD\) with \(B,D\) of degree \(m-1\). The following matrix has maximal minors, up to signs, equal to the three generators of \(I\):
\[
M=\begin{pmatrix}0&H\\ v&-B\\ -u&-D\end{pmatrix}.
\]
Since \(I\) has height two, the Hilbert–Burch exactness criterion gives a free resolution whose generator shifts are \(m-1,m-1,m\) and whose syzygy shifts are \(m,2m-2\). All entries in \(M\) have positive degree for \(m\geq3\), so this resolution is minimal. The displayed minimal resolution follows.

The corresponding Hilbert series simplifies to
\[
\frac{1-2t^{m-1}-t^m+t^m+t^{2m-2}}{(1-t)^2}
=\frac{(1-t^{m-1})^2}{(1-t)^2}.
\]
It therefore has length \((m-1)^2\), identical to the complete intersection in the tame case. For a finite-length graded quotient of the regular two-variable ring, the socle degrees are the degrees of the final free-resolution shifts minus two. Here these are \(m-2\) and \(2m-4\), each of multiplicity one. Equivalently, the first socle element is explicitly the nonzero class of \(H\), since \(uH=vH=0\) in \(A\); the second lies in its one-dimensional highest nonzero graded piece. Thus the socle has dimension two, proving non-Gorensteinness and the failure of local complete intersection.

If \(m=2\) in characteristic two, a linear change of variables gives \(F=uv\) and \(I=(u,v)\), so the local algebra is \(k\) and is Gorenstein. All cases are exhausted.

## Verification

The supplied `verify_tjurina.py` uses exact finite-field arithmetic without external dependencies. It constructs squarefree products of linear forms, their first derivatives and each homogeneous degree of the ideal \((F,F_u,F_v)\), and checks the quotient Hilbert functions and whether adjoining \(F\) adds a generator. The tested triples are characteristic two over \(\mathbb F_4\) with \(m=4\) and \(m=3\), characteristic three over \(\mathbb F_3\) with \(m=3\) and \(m=4\), and characteristic five over \(\mathbb F_5\) with \(m=5\) and \(m=4\). Every test returned `ALL_CHECKS_PASSED`. The abstract universal proof above, not the finite tests, establishes the result in all allowed characteristics and multiplicities.

## Relationship to prior work

Greuel and Pham's 2013 study of Tjurina algebras in positive characteristic establishes the significance of scheme-theoretic singularity algebras and the limits of naive analytic reconstruction. Migliore, Nagel and Schenck investigate schemes supported on hyperplane-arrangement singular loci under a characteristic-zero hypothesis, with local complete-intersection structure for their ordinary components. Burity, Simis and Tohaneanu study Jacobian ideals of central arrangements and explicitly require that the characteristic not divide the arrangement degree for their main theorems; they exhibit pathologies when it does. The present statement differs by computing the full *intrinsic local Tjurina resolution and socle* in exactly that excluded characteristic range, uniformly for all line-arrangement intersections. It does not assert a new formula for the classical Tjurina length or a new intersection-lattice classification.

## Limitations

The result is about homogeneous local products of distinct lines (equivalently local germs of line arrangements). The Betti profile need not be invariant for arbitrary deformations retaining only the same tangent cone. The result does not determine global free resolutions of the homogeneous Jacobian ideal of an entire arrangement, nor the freeness of its logarithmic derivation sheaf. No priority claim against all specialist literature is asserted; independent historical and mathematical review remains necessary.

## References

- G.-M. Greuel and T. H. Pham, *Mather-Yau Theorem in Positive Characteristic*, arXiv:1308.5153, first public version 23 August 2013. https://arxiv.org/abs/1308.5153
- J. Migliore, U. Nagel and H. Schenck, *Schemes supported on the singular locus of a hyperplane arrangement in \(\mathbb P^n\)*, arXiv:1908.03939, 2019. https://arxiv.org/abs/1908.03939
- R. Burity, A. Simis and S. Tohaneanu, *On the Jacobian ideal of central arrangements*, arXiv:2101.02735, 2021. https://arxiv.org/abs/2101.02735
