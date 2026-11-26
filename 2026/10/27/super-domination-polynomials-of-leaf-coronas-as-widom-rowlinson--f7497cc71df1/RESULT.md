# Counting super dominating sets of leaf coronas is #P-complete

## Finding
Counting all super dominating sets is \(\#\mathrm P\)-complete under polynomial-time Turing reductions even for one-leaf coronas of bases of maximum degree at most three. These coronas have maximum degree at most four. The reduction from the two-species Widom–Rowlinson count is parsimonious: for every finite simple graph \(H\) of positive order, the super dominating sets of its one-leaf corona \(W(H)=H\circ K_1\) correspond bijectively to homomorphisms \(H\to P_3^\circ\), the three-vertex path with a loop at every vertex.

The full super-domination polynomial of this class is already covered by the heterogeneous pendant-corona formula [1]. The contribution claimed here is the interpretation as a fixed-target homomorphism count and the resulting bounded-degree complexity classification, not a first enumeration of these sets or a new Widom–Rowlinson partition function.

## Definitions
All input graphs are finite, simple and undirected. The corona attaches one private leaf \(v'\) at every base vertex \(v\). A set \(D\) is super dominating when each omitted vertex \(u\) has a selected witness \(w\in D\) with \(N(w)\cap(V(W(H))\setminus D)=\{u\}\). The count includes the full vertex set. The target \(P_3^\circ\) permits all unordered state pairs except its two distinct endpoints.

## Proof
**Bijection.** A core–leaf arm cannot have both vertices omitted, because its leaf would have no selected neighbor. Map the arm to the middle state if both vertices are selected, and to the two endpoint states according as only the core or only the leaf is selected. An omitted core is witnessed by its own selected leaf. An omitted leaf is witnessed by its selected core exactly if none of that core's base neighbors is omitted. Hence the sole adjacency restriction on the three arm states is that the opposite endpoint states cannot be adjacent. This is also the specialization to one private leaf of the admissibility rule of [1]: an omitted leaf may be attached only outside the closed base neighborhood of the omitted cores. Each homomorphism uniquely reconstructs the selected subset, establishing the count identity.

**Complexity.** Dyer and Greenhill [2, §5, p. 29] establish \(\#\mathrm P\)-hardness of the Widom–Rowlinson count on base graphs of maximum degree at most three, using nonsingularity of its adjacency matrix. The two-species case is the reflexive path here, including the middle vacancy state. The general constant-bound theorem alone would not specify degree three. The corrigendum [3] addresses the proof of the general theorem involving disconnected targets; it does not change the cited bound for this connected target. The map \(H\mapsto W(H)\) adds one vertex and one edge at each base vertex, so is linear in an adjacency-list encoding, raises the degree bound by exactly one on base vertices, and preserves the count by the bijection. Membership in \(\#\mathrm P\) is by guessing a subset and checking the witness condition deterministically in polynomial time, with one branch per subset. Thus the restricted counting problem is \(\#\mathrm P\)-complete under polynomial-time Turing reductions; only the transfer map from the Widom–Rowlinson count is asserted parsimonious.

## Relation to the known polynomial
The weights \(z^2,z,z\) for the middle and the two endpoint states count selected vertices. Thus the known corona polynomial can also be written in the usual spin-model component form [4]:
\[
\mathcal S_{W(H)}(z)=\sum_{U\subseteq V(H)}2^{c(H[U])}z^{2|V(H)|-|U|},
\]
where \(c\) counts components and \(c(\varnothing)=0\). Here \(U\) is the set of arms in endpoint states, with one common endpoint state per induced component. The equivalent boundary formula in [1, Finding and Enumeration] is valid for arbitrary positive leaf multiplicities; setting every multiplicity to 1 covers the entire polynomial above. The component form also gives \([z^n]\mathcal S=2^{c(H)}\) for \(n=|V(H)|\); this minimum coefficient is prior work [1, 5]. For connected \(H\) of order \(n\ge2\), it gives \([z^{n+1}]\mathcal S=\sum_v 2^{c(H-v)}\), equal to \(2n\) exactly when no vertex deletion disconnects the base. This is a coefficient consequence of the polynomial and not a separate originality claim.

## Reproducibility and limits
Run the accompanying `verify.py` with Python 3 from the package directory to compare direct subset checks, the component form and homomorphism counts on 183 finite base-graph instances. These checks do not verify the hardness theorem; the proof uses the published fixed-target result. The full Kaidash chapter [6] was unavailable for statement-level comparison, leaving priority uncertainty. The complexity classification stated here does not claim hardness for tree bases, larger pendant bundles, general attachments, or smaller maximum degree.

## References
1. [*Super-domination polynomial of arbitrary heterogeneous pendant coronas*](https://github.com/Resultary/2026/blob/main/2026/10/12/SCOPE-super-domination-polynomial-of-arbitrary-heterogeneous-pendant-c--08492630563f/RESULT.md), Finding and Enumeration.
2. M. Dyer and C. Greenhill, [*The complexity of counting graph homomorphisms*](https://algorithms.leeds.ac.uk/wp-content/uploads/sites/117/2017/09/dg00b.pdf), *Random Structures & Algorithms* **17** (2000), 260–289, Theorem 1.1 and §5, especially the subcubic Widom–Rowlinson statement.
3. M. Dyer and C. Greenhill, *Corrigendum: The complexity of counting graph homomorphisms*, *Random Structures & Algorithms* **25** (2004), 346–352.
4. [*Widom–Rowlinson partition functions as 1-type polynomials of the generic diameter-3 metric space*](https://github.com/Resultary/2026/blob/main/2026/10/4/SCOPE-widom-rowlinson-partition-functions-as-1-type-polynomials-of-the--ec80747a5989/RESULT.md), Finding; the same weighted spin model is identified with metric one-point extensions there, not with this domination count.
5. [*Minimum super dominating sets of one-leaf coronas*](https://github.com/Resultary/2026/blob/main/2026/10/4/SCOPE-minimum-super-dominating-sets-of-one-leaf-coronas--304999ba8c77/RESULT.md), Finding.
6. P. A. Kaidash, *Super Domination Polynomial of a Graph*, DOI [10.1007/978-3-031-73365-9_6](https://doi.org/10.1007/978-3-031-73365-9_6), 2024 (full text not inspected).
