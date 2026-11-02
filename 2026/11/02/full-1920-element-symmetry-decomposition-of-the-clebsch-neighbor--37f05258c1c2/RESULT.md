# Full \(1920\)-element symmetry decomposition of the Clebsch neighborhood homology

## Finding
Let \(V=\{x\in\mathbb F_2^5:\sum_i x_i=0\}\) and let \(C\) be the Clebsch graph with vertices \(V\), adjacent when their Hamming distance equals four. Let \(X=\mathcal N(C)\) be its ordinary Lovász open-neighborhood complex. Write \(T=V\) under addition and \(G=T\rtimes\mathfrak S_5\) for coordinate permutations and even translations. Then \(G=\operatorname{Aut}(C)\) has order \(1920\).

For a subset \(A\subseteq\{1,\ldots,5\}\), let \(\theta_A(t)=(-1)^{|A\cap\operatorname{supp}(t)|}\). Write \(U_r\) for the rational \((r-1)\)-dimensional standard representation of \(\mathfrak S_r\), and \(\varepsilon_r\) for its sign character. The **complete rational** reduced homology representation is concentrated in degree two and decomposes as the following three pairwise nonisomorphic irreducible rational modules:
\[
\begin{aligned}
\widetilde H_2(X;\mathbb Q)\cong{}&
\operatorname{Inf}_{\mathfrak S_5}^{G}(\bigwedge^2U_5)\\
&\oplus\operatorname{Ind}_{T\rtimes\mathfrak S_4}^{G}
   (\theta_{\{1\}}\otimes(\varepsilon_4\otimes U_4))\\
&\oplus\operatorname{Ind}_{T\rtimes(\mathfrak S_2\times\mathfrak S_3)}^{G}
  (\theta_{\{1,2\}}\otimes(\mathbf1_2\boxtimes\varepsilon_3)).
\end{aligned}
\]
Their dimensions are respectively \(6,15,10\), adding to \(31\). The induced modules are defined using the indicated stabilizers of the \(T\)-characters in the semidirect product. Every other reduced rational homology group vanishes, and
\[
\widetilde H_j(|X|/G;\mathbb Q)=0\quad\text{for all }j\ge0.
\]
Thus all \(31\) previously known two-dimensional homology classes disappear after taking the full symmetry quotient *with rational coefficients*. The quotient is not asserted contractible or integrally acyclic.

## Assumptions and scope
The graph is the standard \(5\)-regular Clebsch graph, **not** its \(10\)-regular complement. Its vertex set has sixteen even binary vectors. A nonempty subset is a face of \(X\) exactly when it lies in an open neighborhood of some graph vertex; all sixteen open neighborhoods have size five. All representation statements use characteristic zero. Only ordinary homology with the displayed geometric group action is considered.

## Proof
**1. Group and simplices.** The five neighbors of the zero vertex have Hamming weight four. Their ten pairwise sums are precisely the ten nonzero nonneighbors of zero. Therefore an automorphism fixing zero is uniquely determined by a permutation of its five neighbors. Every even translation and every coordinate permutation preserves adjacency, giving \(16\cdot5!=1920\) automorphisms and exhausting the group. Enumerating the nonempty faces in the sixteen open-neighborhood simplices, eliminating duplicates, yields the face vector
\[
(f_0,f_1,f_2,f_3,f_4)=(16,80,160,80,16).
\]

**2. Rational homology.** Assemble the integral simplicial boundary columns by deleting each vertex of each increasingly ordered face with coefficient \((-1)^i\). Direct finite checks give \(\partial^2=0\). Gaussian elimination over each of \(\mathbb F_2,\mathbb F_3,\mathbb F_5,\mathbb F_{101}\) gives the identical consecutive boundary ranks \((15,65,64,16)\). These ranks are *exact over \(\mathbb Q\)* without assuming a modular-to-rational equality: modular ranks lower-bound the rational ranks; the chain-complex inequalities \(\operatorname{rank}\partial_1+\operatorname{rank}\partial_2\le80\) and \(\operatorname{rank}\partial_3+\operatorname{rank}\partial_4\le80\) are attained by those lower bounds. Consequently the reduced rational Betti numbers are \(\widetilde b_2=31\) and zero otherwise. An existing published acyclic matching independently proves the stronger nonequivariant type \(X\simeq\bigvee^{31}S^2\); this previously known homotopy type is not new here.

**3. Complete character.** For \(g=(t,\sigma)\in G\), let \(gF\) denote its action on an increasingly ordered simplicial face \(F\). The signed reduced simplicial Lefschetz formula gives the character
\[
\chi(g)=-1+\sum_{k=0}^4(-1)^k
\sum_{\substack{F\in X_k\\gF=F}}
\operatorname{sgn}(g|_F).
\]
All \(1920\) group elements and the \(352\) faces are explicitly checked. Here the sign is the parity of the induced ordering permutation of the vertices of the preserved face. Because homology is concentrated in reduced degree two, the Lefschetz number is exactly \(\operatorname{tr}(g|\widetilde H_2)\). The full character sum is zero and its squared sum is \(5760\), so it has zero invariant multiplicity and character squared norm three. For independent coarse reproducibility, the element counts grouped by (order, fixed-vertex count, trace) are:

| Order | Fixed vertices | Trace | Count |
|---:|---:|---:|---:|
|1|16|31|1|
|2|0|-1|5|
|2|0|3|60|
|2|0|7|10|
|2|4|-5|60|
|2|8|-5|20|
|3|4|1|80|
|4|0|-1|260|
|4|2|1|240|
|5|1|1|384|
|6|0|-1|160|
|6|0|1|80|
|6|2|1|160|
|8|0|-1|240|
|12|0|-1|160|

The rows are **not** claimed to be conjugacy classes; each is an exact count of group elements with those three attributes.

**4. Irreducible decomposition.** Every character of \(T\cong\mathbb F_2^4\) is a \(\theta_A\), with \(A\) considered modulo its complement. Thus \(\mathfrak S_5\) has exactly three orbits on \(\widehat T\), of sizes \(1,5,10\), represented by \(\varnothing,\{1\},\{1,2\}\). For a permutation \(\sigma\) stabilizing a representative, the exact Fourier projection of the computed character is
\[
\chi_A(\sigma)=\frac1{16}\sum_{t\in T}\theta_A(t)\chi(t,\sigma).
\]
Checking every permutation in each stabilizer establishes three little-group characters. On \(\mathfrak S_5\), the first is \((u(\sigma)^2-u(\sigma^2))/2\), where \(u(\sigma)=\#\operatorname{Fix}(\sigma)-1\), namely \(\bigwedge^2U_5\). On \(\mathfrak S_4\), the second is \(\operatorname{sgn}(\sigma)(\#\operatorname{Fix}(\sigma)-1)\), namely \(\varepsilon_4\otimes U_4\). On \(\mathfrak S_2\times\mathfrak S_3\), the third is the sign character of the \(\mathfrak S_3\) factor. Each is irreducible over \(\mathbb Q\), and Clifford's little-group classification for the abelian normal subgroup \(T\) makes their induced representations pairwise nonisomorphic irreducibles. Their dimensions, respectively \(6\), \(5\cdot3=15\), and \(10\cdot1=10\), exhaust the calculated dimension \(31\).

**5. Quotient.** For a finite group acting simplicially on a finite complex, rational homology of the geometric quotient equals the invariant rational homology (pass to a barycentric subdivision and average finite-group chains). No nonzero positive-degree invariants remain by the character sum, and the quotient is connected. Hence all reduced rational homology of \(|X|/G\) vanishes.

## Verification
The included standalone standard-library program `verify.py` reconstructs the sixteen-vertex graph, all \(352\) nonempty simplices, exact signed face boundaries, and the complete \(1920\)-element graph-action table. It verifies group exhaustiveness, boundary composition, modular ranks at four primes and the rank-saturation rational argument, the signed Lefschetz character for every group element, \(\chi\)'s sum and norm, and all Fourier projection identities for the three dual-character stabilizers. Execute `python verify.py`. Success prints the marker `CLEBSCH_NEIGHBORHOOD_FULL1920_THREE_IRREDUCIBLES_VERIFIED`.

## Relationship to prior work
Robinson's relation/Dowker-complex framework (first publicly posted 2020-05-25) supplies the natural construction: the adjacency relation on the graph yields this neighborhood complex, and graph automorphisms act as relation automorphisms. It does **not** compute the 5-regular Clebsch character or its irreducible modules. Shukla's neighborhood-complex homotopy classification covers maximum-degree-three graphs and certain four-regular circulants; the Clebsch graph is five-regular and is not in those theorems. Matsushita–Wakatsuki compare neighborhood and Alexander-dual dominance constructions, not this group action.

A separately published mathematical calculation, *The 5-regular Clebsch neighborhood complex is a wedge of 31 2-spheres*, already establishes precisely the nonequivariant homotopy type of this same complex by an acyclic matching (see reference 4). That is **strictly weaker than** an equivariant module classification: two actions on the same 31-dimensional homology need not have the same traces, irreducible summands, or invariant dimension. The cited calculation explicitly does not claim an equivariant homotopy type. Other published symmetry calculations inspected concern other graphs and do not imply this Clebsch decomposition. Exact and alias searches identified no covering result; this is not a proof of universal bibliographic uniqueness.

## Limitations
The result is a complete finite equivariant **rational** calculation for one canonical graph. It does not determine integral module extensions, equivariant homotopy type, or the integral homology/fundamental group of the geometric quotient. An equivalent published or unpublished computation hidden under different group-theoretic or simplicial terminology may exist, and this remains a bibliographic originality risk. The 31-sphere nonequivariant homotopy classification is prior work and is never claimed as new.

## References
1. M. Robinson, *Cosheaf Representations of Relations and Dowker Complexes*, arXiv:2005.12348, first posted 2020-05-25, https://arxiv.org/abs/2005.12348; *Journal of Applied and Computational Topology* 6 (2022), 27–63, https://doi.org/10.1007/s41468-021-00078-y (primary MSC 55U10).
2. S. Shukla, *Homotopy Type of the Neighborhood Complexes of Graphs of Maximal Degree at most 3 and 4-Regular Circulant Graphs*, arXiv:1802.04526, https://arxiv.org/abs/1802.04526.
3. T. Matsushita and S. Wakatsuki, *Dominance complexes, neighborhood complexes and combinatorial Alexander duals*, arXiv:2312.02639, https://arxiv.org/abs/2312.02639.
4. *The 5-regular Clebsch neighborhood complex is a wedge of 31 2-spheres*, public mathematical result dated 2026-10-11, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-the-5-regular-clebsch-neighborhood-complex-is-a-wedge-of-31-2-sp--1dc11cc6574a.
5. Standard Clifford/Mackey theory for finite groups with an abelian normal subgroup, applied here with all little characters written and verified explicitly.
