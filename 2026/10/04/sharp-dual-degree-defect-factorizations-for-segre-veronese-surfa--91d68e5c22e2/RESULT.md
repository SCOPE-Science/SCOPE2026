# Sharp dual-degree defect factorizations for Segre--Veronese surfaces

## Finding
For integers \(1\le a\le b\), let
\[
X_{a,b}=\varphi_{|\mathcal O(a,b)|}(\mathbb P^1\times\mathbb P^1)\subset\mathbb P^{(a+1)(b+1)-1}.
\]
Its projective dual is a hypersurface and
\[
\Delta(a,b):=\deg X_{a,b}^\vee=6ab-4a-4b+4.
\]
Since \(\deg X_{a,b}=2ab\), the dual degree satisfies the exact defect factorizations
\[
\Delta(a,b)-\deg X_{a,b}=4(a-1)(b-1)
\]
and
\[
3\deg X_{a,b}-4\sqrt{2\deg X_{a,b}}+4-\Delta(a,b)
=4(\sqrt b-\sqrt a)^2.
\]
Thus, writing \(D=ab\),
\[
2D\le\Delta(a,b)\le 6D-8\sqrt D+4.
\]
The lower equality holds exactly for \(a=1\), and the upper equality exactly for \(a=b\).

For a fixed positive integer \(D\), define
\[
a_D=\max\{d:d\mid D,\ d\le\sqrt D\}.
\]
Among all factor pairs \(1\le a\le b\) with \(ab=D\), the dual degree is uniquely maximized at
\[
(a,b)=(a_D,D/a_D)
\]
and uniquely minimized at \( (a,b)=(1,D)\).

## Assumptions and scope
The ground field is \(\mathbb C\). The integers \(a,b\) are positive, so \(\mathcal O(a,b)\) is very ample and gives the complete Segre--Veronese embedding. The statement concerns the ordinary projective dual hypersurface and its projective degree. The optimization is over embeddings of \(\mathbb P^1\times\mathbb P^1\) having the same embedded surface degree \(2D\), equivalently over positive factor pairs \(ab=D\).

## Proof
Let \(H_1,H_2\) denote the two ruling classes on \(\mathbb P^1\times\mathbb P^1\), normalized by \(H_1^2=H_2^2=0\) and \(H_1H_2=1\). Put \(L=aH_1+bH_2\). The discriminant-class formula for a smooth embedded surface is the top Chern class of the first jet bundle. Using
\[
0\longrightarrow \Omega_X^1\otimes L\longrightarrow J_1(L)\longrightarrow L\longrightarrow0,
\]
one obtains
\[
c_2(J_1(L))=c_2(X)+2K_XL+3L^2.
\]
For \(X=\mathbb P^1\times\mathbb P^1\),
\[
c_2(X)=4,\qquad K_X=-2H_1-2H_2,\qquad L^2=2ab,
\]
so
\[
c_2(J_1(L))=4-4a-4b+6ab.
\]
This class is positive for all \(a,b\ge1\). In the Katz--Kleiman--Holme discriminant formalism, the corresponding conormal push-forward vanishes in the dual-defective case; hence the nonzero class also shows that the dual has codimension one. Therefore
\[
\Delta(a,b)=6ab-4a-4b+4.
\]
The embedded degree is \(L^2=2ab\). Direct subtraction gives
\[
\Delta(a,b)-2ab=4(ab-a-b+1)=4(a-1)(b-1).
\]
Also
\[
6ab-8\sqrt{ab}+4-\Delta(a,b)
=4(a+b-2\sqrt{ab})
=4(\sqrt b-\sqrt a)^2,
\]
which proves the sharp two-sided envelope and both equality statements.

Now fix \(D=ab\) and restrict to \(1\le a\le b\), so \(1\le a\le\sqrt D\) and \(b=D/a\). Since
\[
\Delta(a,D/a)=6D-4\left(a+\frac Da\right)+4,
\]
maximizing \(\Delta\) is equivalent to minimizing \(a+D/a\). The real function \(u+D/u\) is strictly decreasing on \(0,\sqrt D\), so on the divisor set it is minimized at the largest divisor \(a_D\le\sqrt D\), proving the unique maximum. The same monotonicity gives the unique minimum at \(a=1\).

## Verification
The symbolic proof above is complete and does not depend on finite enumeration. A standalone exact-arithmetic checker independently verifies the jet-class formula on \(1\le a\le b\le100\), and for every \(1\le D\le5000\) enumerates all factor pairs, verifies the unique minimum and maximum, and checks the sharp square-root envelope without floating-point comparisons. The replay output is included with the package.

## Relationship to prior work
Feher, Nemethi, and Rimanyi give a general degree formula for discriminants of irreducible representations and explicitly place it in the Katz--Kleiman--Holme theory of projective duality. The representation \(\operatorname{Sym}^a\mathbb C^2\otimes\operatorname{Sym}^b\mathbb C^2\) has the Segre--Veronese surface above as its closed highest-weight orbit, so their framework covers the pointwise discriminant-degree computation. The new statement isolated here is the pair of exact geometric defect factorizations and the resulting sharp fixed-embedded-degree extremal classification across all bidegrees. A later study of degrees and Euclidean-distance degrees of Segre products discusses dual degrees and a Segre--Veronese hyperdeterminant extension, but the inspected material does not state this fixed-degree envelope or its equality classification.

## Limitations
The result is restricted to complete Segre--Veronese embeddings of \(\mathbb P^1\times\mathbb P^1\). It does not classify dual degrees for higher products or for incomplete linear systems. The originality assessment is bounded by the inspected sources and searches; an equivalent fixed-degree extremal statement could exist under different terminology. The finite checker is regression evidence only and is not used as an infinite proof.

## References
1. L. M. Feher, A. Nemethi, R. Rimanyi, "The degree of the discriminant of irreducible representations," arXiv:math/0502500v1, first public 2005-02-23. The paper gives the general discriminant-degree framework for highest-weight orbits and cites the Katz--Kleiman--Holme projective-duality formula.
2. P. Draisma et al., "Asymptotics of degrees and ED degrees of Segre products," Advances in Applied Mathematics 133 (2022), article 102242, doi:10.1016/j.aam.2021.102242. The paper treats projective dual degrees of Segre products and discusses a Segre--Veronese hyperdeterminant extension.
