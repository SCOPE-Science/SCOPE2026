# Wan's Igusa Kuranishi cone is Cohen--Macaulay of type \(4\)
## Finding
Let \(Z\) be the Igusa Calabi--Yau threefold in Wan's construction and let \(T_Z\) be its polystable tangent bundle. Wan identifies the semiuniversal analytic deformation base, with \(Z\) fixed, with the germ at the origin of
\[
\mathcal K=V(ab,bc,ca,de,ef,fd)\subset\mathbb C^6_{a,b,c,d,e,f}.
\]
Write
\[
S=\mathbb C[a,b,c,d,e,f],\qquad
R=S/(ab,bc,ca,de,ef,fd).
\]
Because the equations are homogeneous, \(R\) is simultaneously the coordinate ring of the affine cone and the associated graded ring of its local ring at the vertex.

The ring \(R\) is a two-dimensional Cohen--Macaulay level ring of Cohen--Macaulay type \(4\), and therefore is not Gorenstein. Its minimal graded free resolution over \(S\) is
\[
0\longrightarrow S(-6)^4
\longrightarrow S(-5)^{12}
\longrightarrow S(-3)^4\oplus S(-4)^9
\longrightarrow S(-2)^6
\longrightarrow S
\longrightarrow R
\longrightarrow0.
\]
Equivalently, its nonzero graded Betti numbers are
\[
\beta_{0,0}=1,\quad
\beta_{1,2}=6,\quad
\beta_{2,3}=4,\quad
\beta_{2,4}=9,\quad
\beta_{3,5}=12,\quad
\beta_{4,6}=4.
\]
Its Hilbert series is
\[
H_R(t)=\frac{(1+2t)^2}{(1-t)^2}
      =\frac{1+4t+4t^2}{(1-t)^2},
\]
so the Hilbert--Samuel multiplicity of the deformation germ at the origin is
\[
e(\mathcal K,0)=9.
\]

The singular locus is exactly the union of six coordinate axes,
\[
\operatorname{Sing}(\mathcal K)
=
\bigl(\{0\}\times V(de,ef,fd)\bigr)
\cup
\bigl(V(ab,bc,ca)\times\{0\}\bigr).
\]
At a nonzero point of any one of these axes, exactly three two-dimensional branches meet; the completed local model is a smooth one-dimensional factor times the three-axis curve.

Finally,
\[
\operatorname{Proj}R\subset\mathbb P^5
\]
is the Stanley--Reisner curve whose simplicial graph is the complete bipartite graph \(K_{3,3}\). It is a union of nine coordinate lines with six triple intersection points, has degree \(9\), and has arithmetic genus \(4\).

## Assumptions and scope
All rings are over \(\mathbb C\), with the six deformation parameters in degree one. The statement concerns Wan's semiuniversal deformation base before quotienting by automorphisms or by \(S\)-equivalence. It describes the local analytic germ through its homogeneous algebraic representative and its tangent cone; it does not assert that the corresponding coarse moduli space has the same local equations.

The terms Cohen--Macaulay type and level are used for the standard graded ring localized at its homogeneous maximal ideal, equivalently for its graded canonical module. The Hilbert--Samuel multiplicity is taken at the cone vertex.

## Proof
Put
\[
A=\mathbb C[a,b,c]/(ab,bc,ca),\qquad
A'=\mathbb C[d,e,f]/(de,ef,fd).
\]
Wan's equations split into the two disjoint triples, so
\[
R\cong A\otimes_{\mathbb C}A'.
\]

The three coordinate variables in the first factor give the Hilbert--Burch resolution
\[
0\longrightarrow \mathbb C[a,b,c](-3)^2
\xrightarrow{M}
\mathbb C[a,b,c](-2)^3
\xrightarrow{(ab,bc,ca)}
\mathbb C[a,b,c]
\longrightarrow A\longrightarrow0,
\]
where
\[
M=
\begin{pmatrix}
c&0\\
-a&a\\
0&-b
\end{pmatrix}.
\]
The two columns are syzygies, and the three maximal minors are \(ca,-bc,ab\), so the complex resolves the height-two ideal \((ab,bc,ca)\). The same resolution holds for \(A'\).

Tensor the two resolutions over \(\mathbb C\), now viewed over the six-variable polynomial ring \(S\). Since the variables are disjoint and tensoring over a field preserves exactness, the total complex is a free resolution of \(R\). Collecting total homological degrees gives
\[
F_1=S(-2)^6,
\]
\[
F_2=S(-3)^4\oplus S(-4)^9,
\]
\[
F_3=S(-5)^{12},
\qquad
F_4=S(-6)^4.
\]
Every differential has entries in the homogeneous maximal ideal, so this resolution is minimal.

Wan proves that the germ has nine irreducible components, all coordinate planes of dimension two. Hence \(\dim R=2\). The resolution has projective dimension \(4\), so Auslander--Buchsbaum gives
\[
\operatorname{depth}R=6-4=2=\dim R.
\]
Thus \(R\) is Cohen--Macaulay. For a Cohen--Macaulay quotient of a polynomial ring, the rank of the final module in a minimal free resolution is the Cohen--Macaulay type. Here that rank is \(4\). All four final summands have the same shift \(-6\), so the canonical module is generated in one degree: \(R\) is level. Since its type is greater than one, it is not Gorenstein.

The first three-axis factor has one constant monomial and three monomials in every positive degree, hence
\[
H_A(t)=1+3t+3t^2+\cdots=\frac{1+2t}{1-t}.
\]
Therefore
\[
H_R(t)=H_A(t)^2=\frac{(1+2t)^2}{(1-t)^2}.
\]
For a two-dimensional standard graded Cohen--Macaulay cone, the multiplicity is the numerator evaluated at \(t=1\), giving \(9\). Equivalently, the projectivized tangent cone has degree nine.

The curve \(V(ab,bc,ca)\subset\mathbb A^3\) is the union of the three coordinate axes and is smooth away from the origin. Smoothness of products over \(\mathbb C\) gives
\[
\operatorname{Sing}(A\times A')
=(\operatorname{Sing}A\times A')\cup(A\times\operatorname{Sing}A'),
\]
which is exactly the six coordinate axes stated above.

For the projective tangent cone, the ideal is squarefree monomial. Its Stanley--Reisner complex has vertex set
\[
\{a,b,c\}\sqcup\{d,e,f\},
\]
and a two-element face precisely when it contains one vertex from each part. Thus the complex is \(K_{3,3}\), with six vertices and nine edges. Consequently \(\operatorname{Proj}R\) is the corresponding union of nine coordinate lines. From the Hilbert series, the Hilbert function equals
\[
9n-3
\]
for every \(n\ge2\). Comparing with \(dn+1-p_a\) for a projective curve gives
\[
d=9,\qquad p_a=4.
\]

## Verification
The accompanying `verify.py` independently enumerates the Stanley--Reisner complex and applies Hochster's formula to all \(64\) vertex subsets. It recovers exactly the six nonzero Betti positions displayed above. It also enumerates standard monomials through degree \(12\), checks the Hilbert function against the closed Hilbert series, checks the resolution numerator identity, and verifies the \(K_{3,3}\) vertex/edge counts, degree, arithmetic genus, and multiplicity.

The verifier does not replace Wan's analytic identification of the Kuranishi germ, the Hilbert--Burch theorem, Auslander--Buchsbaum, or the standard relation between a final Betti rank and Cohen--Macaulay type. Those are the mathematical inputs used in the proof. The stored replay output ends in `VERIFY_OK`.

## Relationship to prior work
Wan determines the entire semiuniversal fixed-base deformation germ and proves that it is reduced with nine two-dimensional coordinate-plane components. Section 5.3 gives the six quadratic equations exactly and proves that no higher Kuranishi terms occur. The paper does not state the Cohen--Macaulay property, level type, minimal graded resolution, Hilbert series, multiplicity, six-axis singular stratification, or the \(K_{3,3}\) projectivized tangent-cone description.

Wan also points out that each three-axis factor has a classical predecessor: Aspinwall computes a cubic superpotential \(W=XYZ\) whose critical equations are \(XY=XZ=YZ=0\). Wan's compact example realizes the product of two such germs. Aspinwall's calculation does not determine the commutative-algebra invariants of Wan's later compact two-factor deformation base.

Targeted searches for the exact six-generator ideal together with Cohen--Macaulay, Gorenstein, Hilbert-series, Betti, Stanley--Reisner, singular-locus, and \(K_{3,3}\) formulations did not locate a source stating this fixed-germ profile. General Stanley--Reisner and Hilbert--Burch theory supplies the tools used in the proof but does not by itself tabulate these invariants for Wan's deformation germ.

## Limitations
The result is an exact algebraic profile of the semiuniversal deformation base, not a computation of a coarse moduli quotient. It does not analyze the automorphism action on the nine branches or determine invariants after \(S\)-equivalence.

The derivation is elementary once Wan's explicit equations are known. Accordingly, the main originality risk is that an unindexed note could have made the same commutative-algebra calculation, or that the profile might be considered an implicit consequence of standard Stanley--Reisner theory. The value claimed here is the complete structural diagnosis of the newly constructed deformation germ, especially the Cohen--Macaulay type-four and non-Gorenstein conclusions, rather than novelty of the underlying general algebraic tools.

## References
1. X. Wan, *Rigid and obstructed tangent bundles on Calabi--Yau threefolds*, arXiv:2609.27271v1, 2026, especially Theorem 1.5 and Section 5.3.
2. P. S. Aspinwall, *A McKay-like correspondence for \((0,2)\)-deformations*, arXiv:1110.2524v3, 2014, Section 7.
