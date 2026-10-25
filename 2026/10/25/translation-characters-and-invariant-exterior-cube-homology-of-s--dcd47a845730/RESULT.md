# Translation characters and invariant exterior-cube homology of scale-two hypercube Vietoris–Rips complexes

## Finding

Let \(n\ge3\) be an integer, write \(Q_n=(\mathbb F_2)^n\) with Hamming distance, and put \(K_n=\operatorname{VR}_{\le2}(Q_n)\). The translation group \(T_n=(\mathbb F_2)^n\) and the coordinate permutations \(S_n\) act simplicially. The existing nonequivariant classification [1] identifies \(K_n\) with a wedge of three-spheres, with
\[
b_n=\dim_{\mathbb Q}\widetilde H_3(K_n;\mathbb Q)=\sum_{j=3}^{n}2^{j-3}\binom j3
=1+\frac{2^{n-3}(n-3)(n^2-3n+8)}3.
\]
The new conclusions are the following character and module determinations. For every \(t\in T_n\),
\[
\operatorname{tr}\!\left(t\mid\widetilde H_3(K_n;\mathbb Q)\right)=
\begin{cases}
b_n,&t=0,\\
1+2^{n-2}(n-3),&1\le\operatorname{wt}(t)\le2,\\
1,&\operatorname{wt}(t)\ge3.
\end{cases}
\]
For \(a\in T_n\), let \(\lambda_a(t)=(-1)^{a\cdot t}\) and \(k=\operatorname{wt}(a)\). Its multiplicity is
\[
m_{n,k}=\begin{cases}
\binom n3,&k=0,\\
\dfrac{n-3}{6}\bigl(3k^2-3(n+1)k+n^2+2\bigr),&1\le k\le n.
\end{cases}
\]
Moreover, as \(\mathbb Q[S_n]\)-modules,
\[
\widetilde H_3(K_n;\mathbb Q)^{T_n}\cong\bigwedge^3\mathbb Q^n.
\]
In particular the invariant space under \(T_n\rtimes S_n\) is zero. Only degree three has nonzero reduced homology.

## Assumptions and scope

The Rips convention is inclusive: a nonempty subset of \(Q_n\) is a simplex if and only if every pair has Hamming distance at most two. Coordinates and translations are over \(\mathbb F_2\). Group characters and isotypic multiplicities are over \(\mathbb Q\). All statements quantify over every integer \(n\ge3\); this is a statement about graph-metric Rips complexes, **not** the intrinsic Čech nerve. The nonequivariant sphere-wedge theorem and rank formula are imported from [1]; the representation formulas and their geometric basis are the contributions established here.

## Proof

**Concentrated homology.** By [1], \(K_n\simeq\bigvee^{b_n}S^3\), so for every simplicial automorphism \(g\) its ordinary Lefschetz number is \(L(g)=1-\operatorname{tr}(g\mid\widetilde H_3(K_n;\mathbb Q))\). The cited homotopy equivalence is used only for homology concentration and its established rank, not as an equivariant equivalence.

**Invariant simplices under translations.** If \(t\ne0\), each orbit on vertices consists of a two-point set \(\{x,x+t\}\). An invariant face must be a union of such pairs. If \(\operatorname{wt}(t)\ge3\), none is a simplex: each orbit already contains a pair farther than two. Therefore \(L(t)=0\) and the trace is one. If \(\operatorname{wt}(t)=1\) or two, let \(G_t\) be the graph whose vertices are the \(2^{n-1}\) translation orbits and whose edges connect distinct orbits exactly when their union of four vertices has diameter at most two. The invariant faces of \(K_n\) are precisely unions of cliques of \(G_t\). A union of \(j\) orbits has \(2j\) vertices, and the translation acts on its oriented simplex as the product of \(j\) disjoint transpositions, with sign \((-1)^j\). Thus its signed Lefschetz contribution is \((-1)^{2j-1}(-1)^j=(-1)^{j+1}\); consequently \(L(t)=\chi(\operatorname{Cl}(G_t))\).

For \(\operatorname{wt}(t)=1\), identify each orbit by its \(n-1\) remaining coordinates. The two-bit diameter bound joins precisely pairs differing in one remaining coordinate, so \(G_t=Q_{n-1}\), a triangle-free graph with \(2^{n-1}\) vertices and \((n-1)2^{n-2}\) edges. For \(\operatorname{wt}(t)=2\), an orbit has one of two parity labels in the translated coordinate pair, together with the \(n-2\) remaining coordinates. Each orbit connects to the orbit of the other parity label with either the same remaining coordinates or exactly one different remaining coordinate. This graph is bipartite, hence triangle-free; it too has \(2^{n-1}\) vertices and \((n-1)2^{n-2}\) edges. In both cases,
\[
L(t)=2^{n-1}-(n-1)2^{n-2}=2^{n-2}(3-n).
\]
The trace formula follows from the Lefschetz identity.

**Fourier multiplicities.** Maschke's theorem applies over \(\mathbb Q\), and all characters of \(T_n\) take values in \(\{\pm1\}\). Fourier orthogonality gives
\[
m_{n,k}=2^{-n}\sum_{t\in T_n}(-1)^{a\cdot t}\operatorname{tr}(t\mid\widetilde H_3).
\]
For \(k>0\), \(\sum_t(-1)^{a\cdot t}=0\); the contribution of nonzero elements of weight one or two beyond their baseline trace one equals \(2^{n-2}(n-3)\) times
\[
(n-2k)+\frac{(n-2k)^2-n}{2}.
\]
Together with \(b_n-1\) from the identity, substitution yields the displayed quadratic multiplicity. For \(k=0\), summing every trace yields \(\binom n3\); this also follows by a direct finite binomial identity from the displayed expression for \(b_n\). In particular all the given rational multiplicities are nonnegative integers, as guaranteed by their character-theoretic construction.

**Canonical geometric invariant classes.** Fix a three-coordinate subset \(I\subseteq\{1,\ldots,n\}\) and a setting of the other \(n-3\) coordinates. These choices determine an embedded three-cube \(C\subset Q_n\). Its scale-two Rips subcomplex is the boundary of a four-dimensional cross-polytope, hence is a three-sphere. Let \(z_C\in\widetilde H_3(K_n;\mathbb Z)\) be its oriented fundamental cycle, with orientation fixed by increasing order of the coordinates in \(I\). Let \(E_C\) be its tetrahedral face consisting of the four even-parity vertices in the free three coordinates. The face \(E_C\) is contained in no four-simplex of \(K_n\): any vertex within \(C\) but outside \(E_C\) has Hamming distance three from an even-parity vertex; any vertex outside \(C\) differs in a fixed coordinate and has free-coordinate distance at least two from one of those four vertices. Moreover \(E_C\) uniquely determines \(C\), since the three coordinate directions occur as the support of its difference vectors. The oriented cycle \(z_C\) has coefficient \(\pm1\) on \(E_C\). Therefore these fundamental cycles are linearly independent in integral homology: the coefficients of the distinct \(E_C\) are homology-invariant and form an identity minor on this collection of cycles.

Translations inside the three free coordinates act on the sphere \(\operatorname{VR}_{\le2}(Q_3)\) with orientation degree \(+1\). To see this, identify its four antipodal vertex pairs with the four even-parity vertices of \(Q_3\). Each two-bit translation induces a double transposition on these four pairs, and translation by \((1,1,1)\) exchanges the vertices within all four antipodal pairs. Both have degree \(+1\), giving the claim for the translation generators. Therefore, for each \(I\), the sum \(Z_I=\sum_{C\text{ with free coordinates }I}z_C\) is nonzero and translation-invariant. The \(\binom n3\) classes \(Z_I\) are independent by their \(E_C\) coefficients. Their number matches the Fourier-computed dimension of \(\widetilde H_3(K_n;\mathbb Q)^{T_n}\), so they form its basis.

For \(\pi\in S_n\), the induced automorphism of an individual cross-polytope sphere permutes free coordinate directions. Its orientation degree is the sign of that permutation: on the four antipodal pairs it fixes the zero even-parity vertex and permutes the three remaining even-parity vertices in the same way. Thus \(\pi Z_I=\operatorname{sgn}(\pi|_I)Z_{\pi I}\), where the sign refers to ordering the three-element index set. This is exactly the standard basis action on \(\bigwedge^3\mathbb Q^n\). Finally \(\bigwedge^3\mathbb Q^n\) has no \(S_n\)-invariants for \(n\ge3\): any proposed invariant coefficient of a basis wedge must negate itself under transposition of two of its three labels.

## Verification

A standalone script, `vr_cube_translation_check.py`, using only standard Python, generates all candidate maximal cliques (unit balls, square faces and parity tetrahedra) and their subfaces, independently checks simplex diameter constraints and Euler characteristics, and calculates oriented-simplex Lefschetz traces directly. For every translation in dimensions three through six, these traces match the theorem; Walsh multiplicities are independently enumerated. In dimension three all \(48\) cubical affine automorphisms are checked; the exterior-cube character after translation averaging is checked for all \(24\) coordinate permutations of the four-cube and representatives of all seven permutation classes of the five-cube. It prints `RIPS_QN_TRANSLATION_CHARACTER_CHECKS_OK 281`. Reproduce with `python3 vr_cube_translation_check.py`.

The finite tests are corroboration, not proof for all \(n\); the arbitrary-dimension proofs above establish the results. The script does not compute integral Smith normal forms, nor does the theorem assert integral complete-module classification.

## Relationship to prior work

The nonequivariant sphere-wedge decomposition and its rank are from Adamaszek–Adams [1]. Adams–Virk [2] supply constructions of cross-polytopal classes and independence estimates, but do not give the rational translation character, all its Fourier multiplicities, or the complete coordinate action on the translation-fixed subspace. Briggs–Feng–Wells [3] study facets at multiple scales; their results do not imply the displayed action. Results concerning the scale-two intrinsic hypercube Čech nerve are about a different complex with a different homological degree and cannot be substituted for this Rips calculation. Likewise a weight-restricted Rips sublevel has a different vertex set. A search without a match cannot exclude uncataloged equivalent work.

## Limitations

The result gives the complete translation character and the coordinate-permutation structure of the translation-fixed part, not the entire full-group character at nontrivial coordinate permutations. The representation is classified over \(\mathbb Q\); integral extension and torsion questions for the full action remain outside scope. The prior work supplies the nonequivariant homotopy classification. No claim is made about Vietoris–Rips scales greater than two, any equivariant homotopy equivalence, or independent mathematical validation.

## References

[1] M. Adamaszek and H. Adams, *On Vietoris--Rips complexes of hypercube graphs*, arXiv:2103.01040, first publicly submitted March 1, 2021. https://arxiv.org/abs/2103.01040.

[2] H. Adams and Ž. Virk, *Lower bounds on the homology of Vietoris–Rips complexes of hypercube graphs*, arXiv:2309.06222, first submitted September 12, 2023. https://arxiv.org/abs/2309.06222.

[3] J. Briggs, Z. Feng, and C. Wells, *Facets in the Vietoris–Rips complexes of hypercubes*, arXiv:2408.01288, first submitted August 2, 2024. https://arxiv.org/abs/2408.01288.
