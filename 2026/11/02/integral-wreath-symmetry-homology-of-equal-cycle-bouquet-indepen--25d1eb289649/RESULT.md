# Integral wreath-symmetry homology of equal-cycle bouquet independence complexes

## Finding
Fix integers \(m\ge2\) and \(L\ge4\). Form the bouquet graph \(B_{m,L}\) by identifying one distinguished vertex in each of \(m\) vertex-disjoint simple cycles \(C_L\); no other vertices are identified. Put \(X_{m,L}=\operatorname{Ind}(B_{m,L})\), the simplicial complex of independent graph-vertex subsets. Its full graph automorphism group is the wreath product \(W_m=(C_2)^m\rtimes S_m\), acting by independent reversals of the cycle petals and by permutation of petals.

For \(g=(\epsilon,\sigma)\in W_m\), where \(\epsilon_i\in\{0,1\}\) records reversal of petal \(i\), define the integral line character
\[
\chi_{a,b}(g)=(-1)^{a\sum_i\epsilon_i}\operatorname{sgn}(\sigma)^b.
\]
Its integer exponents are understood modulo \(2\). The complete *reduced integral homology as a \(W_m\)-module* is as follows; every displayed group is a single copy of \(\mathbb Z\), and every undisplayed reduced homology group is zero.

* If \(L=3q\), \(q\ge2\), then
\[
\widetilde H_{mq-1}(X_{m,L};\mathbb Z)=\mathbb Z_{\chi_{\lceil q/2\rceil,q}},\qquad
\widetilde H_{m(q-1)}(X_{m,L};\mathbb Z)=\mathbb Z_{\chi_{\lfloor(q-1)/2\rfloor,q-1}}.
\]
* If \(L=3q+1\), \(q\ge1\), then
\[
\widetilde H_{mq-1}(X_{m,L};\mathbb Z)=\mathbb Z_{\chi_{\lfloor q/2\rfloor,q}}.
\]
* If \(L=3q+2\), \(q\ge1\), then
\[
\widetilde H_{mq}(X_{m,L};\mathbb Z)=\mathbb Z_{\chi_{\lceil q/2\rceil,q}}.
\]

The respective ordinary homotopy types are \(S^{mq-1}\vee S^{m(q-1)}\), \(S^{mq-1}\), and \(S^{mq}\). These are nonequivariant assertions; the module identification above is equivariant.

In particular, the full symmetry quotient \(X_{m,L}/W_m\) has one positive-degree rational homology generator exactly in the following cases, and none otherwise: \(L=3q\) with \(q\equiv0\pmod4\) (degree \(mq-1\)); \(L=3q\) with \(q\equiv1\pmod4\) (degree \(m(q-1)\)); \(L=3q+1\) with \(q\equiv0\pmod4\) (degree \(mq-1\)); or \(L=3q+2\) with \(q\equiv0\pmod4\) (degree \(mq\)). All ranges stated above still apply.

A minimal informative case is the bouquet of two hexagons:
\[
\operatorname{Ind}(C_6\vee_v C_6)\simeq S^2\vee S^3,
\]
so its reduced integral homology has rank one in each of degrees \(2\) and \(3\). This distinguishes the correct attachment from the single-sphere subcase displayed in a previous wedge-of-cycles calculation [2].

## Assumptions and scope
The graph is a *one-vertex bouquet*, not a Cartesian product, matching complex, or a chain of fused polygons. A \(C_L\) has exactly \(L\) graph vertices and \(L\) edges. The common vertex \(v\) has graph degree \(2m\); all others have degree \(2\). Because \(m\ge2\), every graph automorphism fixes \(v\), permutes its \(m\) cycle components, and may independently reverse each, proving \(\operatorname{Aut}(B_{m,L})=W_m\). Integral homology is singular homology of the geometric realization, and \(\mathbb Z_\chi\) means the rank-one lattice with action through the stated sign character.

## Proof
**1. Exact link and deletion.** Let \(K=\operatorname{del}_v X_{m,L}\) and \(A=\operatorname{lk}_v X_{m,L}\). Removing \(v\) from each \(L\)-cycle leaves a path on \(L-1\) vertices; removing its *closed neighborhood* (\(v\) plus its two cycle neighbors in each petal) leaves a path on \(L-3\) vertices. Therefore, as simplicial complexes with the natural wreath action,
\[
K=\operatorname{Ind}(P_{L-1})^{*m},\qquad
A=\operatorname{Ind}(P_{L-3})^{*m},\qquad
X_{m,L}=K\cup_A(v*A).
\]
The last equality is an actual pushout of simplicial complexes, not merely a homotopy decomposition. It yields the functorial cofiber sequence \(A\to K\to X_{m,L}\to\Sigma A\).

**2. Integral path topology.** For a vertex path \(P_t\), the fold \(N(t)\subseteq N(t-2)\) for \(t\ge4\) deletes vertex \(t-2\), leaving \(P_{t-3}\sqcup P_2\). Consequently
\[
\operatorname{Ind}(P_t)\simeq\Sigma\operatorname{Ind}(P_{t-3}).
\]
Together with the direct bases \(P_1,P_2,P_3\), this proves the familiar classification: \(\operatorname{Ind}(P_{3q})\simeq S^{q-1}\); \(\operatorname{Ind}(P_{3q+1})\) is contractible; and \(\operatorname{Ind}(P_{3q+2})\simeq S^q\). The same recurrence supplies integral homology and excludes torsion.

**3. Reflection degrees from a signed fixed-face count.** Let \(R_t\) reverse the vertex order in \(P_t\). Write \(F_j=\sum_{I\subseteq V(P_j),\,I\text{ independent}}(-1)^{|I|}\). Then \(F_0=1\), \(F_1=0\), \(F_j=F_{j-1}-F_{j-2}\); hence \((F_j)\) is the period-six sequence \((1,0,-1,-1,0,1,\ldots)\). A reflection-stable face consists of symmetric pairs, with a possible central fixed vertex. The pair reflection reverses its two vertices, and thus contributes one negative orientation sign. Direct enumeration of allowable pairs gives the reduced Lefschetz traces
\[
\widetilde L(R_{2h})=-F_{h-1},\qquad
\widetilde L(R_{2h+1})=F_{h-2}\quad(h\ge2),
\]
with the cases \(t=2,3\) checked directly. Since there is one reduced integral homology generator in degree \(q-1\) for both relevant path lengths, comparing its alternating trace yields
\[
R_{3q}|\widetilde H_{q-1}=(-1)^{\lfloor q/2\rfloor},\qquad
R_{3q-1}|\widetilde H_{q-1}=(-1)^{\lceil q/2\rceil}.
\]
These are equalities of automorphisms of \(\mathbb Z\), not just rational characters. The period-six recurrence proves them for all \(q\), rather than extrapolating a finite experiment.

**4. Joins and the group sign.** The \(m\)-fold join of a complex homotopy equivalent to \(S^{d}\) has one free reduced homology group in dimension \(m(d+1)-1\), canonically identified with the tensor product of its \(m\) reduced homology lines with a single suspension shift. Reflecting one factor acts by its path reflection degree. Exchanging two factors of dimension \(d\) acts by \((-1)^{(d+1)^2}=(-1)^{d+1}\) on the oriented join chain. Thus the \(m\)-factor module is \(\chi_{a,d+1}\) when each reflection has degree \((-1)^a\).

**5. The three residue classes.** If \(L=3q\), the path classification gives \(K\simeq S^{mq-1}\) and \(A\simeq S^{m(q-1)-1}\). Since \(m\ge2\), the latter sphere dimension is strictly smaller than the former. Every map \(A\to K\) is therefore null-homotopic, giving the claimed ordinary wedge homotopy type. The cofiber exact sequence identifies homology in the two distinct degrees, equivariantly and integrally, with respectively \(\widetilde H_{mq-1}(K)\) and \(\widetilde H_{m(q-1)-1}(A)\), proving both line characters.

If \(L=3q+1\), \(A\) is contractible and \(K\simeq S^{mq-1}\), so inclusion \(K\to X_{m,L}\) is an equivariant isomorphism on all integral reduced homology. If \(L=3q+2\), \(K\) is contractible while \(A\simeq S^{mq-1}\); the natural connecting map gives the integral equivariant isomorphism \(\widetilde H_{mq}(X_{m,L})\cong\widetilde H_{mq-1}(A)\). Inserting step 3 into step 4 proves the claimed formulas in every case.

**6. Rational quotients.** For a finite group acting simplicially, subdivision gives a cellular quotient for which rational homology identifies with the invariant rational homology of the original space. Each positive-dimensional homology module here is a line. It has an invariant precisely when its independent petal-reflection exponent is even *and* its petal-permutation exponent is even. Applying this parity test to the displayed modules yields the exact congruences stated in the finding.

## Verification
Run the accompanying standalone `checker.py` using Python 3. It independently enumerates independent faces of small bouquets, uses exact bitset elimination over \(\mathbb F_2\) to compute reduced Betti numbers, and computes signed simplicial Lefschetz traces over \(\mathbb Z\) for every automorphism in the tested wreath groups. Its successful output ends `BOUQUET_CYCLE_HOMOLOGY_AND_SIGNED_CHARACTER_CHECKS_OK`.

Cases: \((m,L)=(2,4),(2,5),(2,6),(2,7),(2,8),(2,9),(2,10),(3,4),(3,5),(3,6)\); every one of their \(8\) or \(48\) group elements is checked. A standalone run log is included. These finite checks are corroborations, not proofs of the universal parameter ranges or the integral torsion statement, which follow from the preceding cofiber argument.

## Relationship to prior work
Daundkar, Panja and Prasad [2] studied one-vertex wedges of paths and cycles and establish broad nonequivariant sphere-wedge assertions. Their displayed cycle-wedge reduction in Lemma 3.3 replaces the vertex link by a path with \(L-2\) vertices, whereas deleting the common vertex and its two neighbors from a cycle gives a path with exactly \(L-3\) vertices. In particular, the single-sphere \(C_6\)-by-\(C_6\) subcase displayed in their proof of Theorem 3.5 does not supply the additional degree-two class detected here. The present result uses the correct link, gives all integral homology ranks and complete natural wreath-group characters in every equal-cycle family, and derives the full-symmetry quotient congruences.

The general vertex cofiber framework of Adamaszek [3] already supplies the abstract map \(A\to K\) and its null-map splitting condition; the path homotopy recurrence is classical [1]. Neither general construction by itself states the equal-cycle bouquet module formulas, their reflection degrees, or the quotient congruences. Goyal, Shukla and Singh [4] examine Mycielskians, categorical products, and local modifications of cycles rather than these bouquet modules. Related published results about Dutch-windmill **matching** complexes concern a different simplicial complex, not a reduction of this finding.

## Limitations
The result is restricted to \(m\ge2\), identical simple cycle petals of length \(L\ge4\), their graph-induced full wreath symmetry, and integral homology or rational quotient homology. No equivariant *homotopy-type* decomposition is claimed from the nonequivariant wedge splitting, and no integral homology statement is claimed for orbit-space quotients. Independent external validation has not been performed. Exhaustive literature discovery is not mathematically possible; unidentified equivalent sources remain a bibliographic risk.

## References
[1] D. N. Kozlov, *Complexes of directed trees*, Journal of Combinatorial Theory A 88 (1999), 112–122; cited for the classical path and cycle independence-complex recurrences.

[2] N. Daundkar, S. Panja, S. Prasad, *Independence complexes of wedge of graphs*, arXiv:2303.08798, first public 2023-03-15, particularly Section 3, Lemma 3.3 and Theorem 3.5. https://arxiv.org/abs/2303.08798

[3] M. Adamaszek, *Splittings of independence complexes and the powers of cycles*, arXiv:1106.6250, Section 3, especially Proposition 3.1. https://arxiv.org/abs/1106.6250

[4] S. Goyal, S. Shukla, A. Singh, *Homotopy Type of Independence Complexes of Certain Families of Graphs*, arXiv:1905.06926, Sections 3–5. https://arxiv.org/abs/1905.06926
