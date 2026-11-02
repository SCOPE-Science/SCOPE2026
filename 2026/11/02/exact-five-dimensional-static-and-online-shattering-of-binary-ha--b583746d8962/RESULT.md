# Exact five-dimensional static and online shattering of binary Hamming two-spheres

## Finding
For every integer \(d\ge 7\), consider the concept class
\[
\mathcal H^{(2)}_d=\{h_c:c\in\{0,1\}^d\},\qquad
h_c(x)=\mathbf1\{\operatorname{dist}_H(c,x)=2\},\quad x\in\{0,1\}^d.
\]
Its VC and deterministic realizable Littlestone dimensions both equal five:
\[
\boxed{\operatorname{VCdim}(\mathcal H^{(2)}_d)=\operatorname{Ldim}(\mathcal H^{(2)}_d)=5\quad(d\ge7).}
\]
The upper bound holds uniformly for all positive dimensions. The exact-distance-two relation is distinct from ordinary Hamming-graph adjacency, which tests distance one.

## Assumptions and scope
All bit strings have fixed length \(d\), their coordinates are labeled, Hamming distance counts differing coordinates, and both concepts and queries range over the full binary cube. The query returns one at **exactly** distance two, not at distance at most two. Distinct centers that induce identical concepts (possible at small dimensions) are identified; this does not affect any stated bound. VC shattering uses fixed query sets, and Littlestone shattering uses complete binary adaptive query trees in the standard deterministic realizable convention. The theorem makes no assertion about nonbinary alphabets, other Hamming radii, or induced subgraphs.

## Proof
We regard a bit string as a subset of \([d]\), using symmetric difference to represent bitwise XOR.

**Lemma 1 (positive fiber).** Fix the first query at the empty subset. Its positive hypotheses have centers \(E\in\binom{[d]}2\). For a subsequent query \(S\), the positive outcome is equivalent to
\[
|E\mathbin\triangle S|=2\iff |S|=2|E\cap S|.
\]
Consequently only three query types can have positive answers within this fiber: the empty query (which is constantly one), a two-element query (which tests whether an edge has exactly one endpoint in the queried pair), and a four-element query (which tests whether the edge is wholly inside the queried four-set). Every query of another size is constantly zero on this fiber.

**Lemma 2 (near-star bound).** Let \(a,b,c\) be distinct vertices and consider the edges
\[
\mathcal R=\{\{a,x\}:x\notin\{a,b,c\}\}\cup\{\{b,c\}\}.
\]
Every nonconstant query of the types in Lemma 1 has an answer fiber with at most three edges. For a four-set query there are at most three positive star edges, and including the exceptional edge can only reduce this maximum. For a two-set query not containing \(a\), at most two star edges plus the exceptional edge give a positive answer. For a two-set containing \(a\), either the query is \(\{a,b\}\) or \(\{a,c\}\) (both constant one), or exactly the edge \(\{a,x\}\) and the exceptional edge form the zero fiber. No complete depth-three binary tree can be shattered: either branch at its root would need at least four distinct hypotheses. Hence \(\operatorname{Ldim}(\mathcal R)\le2\).

**Lemma 3 (two-star bound).** For distinct \(a,b\), set
\[
\mathcal T_{a,b}=\{\{a,x\},\{b,x\}:x\notin\{a,b\}\}.
\]
A four-set query has at most four positive edges, as does a two-set disjoint from \(\{a,b\}\). The two-set \(\{a,b\}\) is constant one. Every other nonconstant two-set query contains exactly one of \(a,b\); each of its two answer fibers is isomorphic to a near-star from Lemma 2. Thus no query can have both answer fibers of Littlestone dimension at least three: in the first two cases one fiber has at most four elements, and in the last case both fibers have dimension at most two. It follows that \(\operatorname{Ldim}(\mathcal T_{a,b})\le3\).

**Lemma 4 (uniform upper bound).** On the edge-center class \(\binom{[d]}2\) with the queries described in Lemma 1, a nonconstant four-set query has only six positive centers, and a nonconstant two-set query has the two-star positive fiber of Lemma 3. Neither can root a complete depth-five tree, because such a root would require both branches to have depth at least four. The edge-center class therefore has Littlestone dimension at most four. Translation by the first query is an automorphism of the binary cube, so every positive first-query fiber in the original class has the same bound. Hence \(\operatorname{Ldim}(\mathcal H^{(2)}_d)\le5\) for all \(d\ge1\). Also \(\operatorname{VCdim}\le\operatorname{Ldim}\).

**Lower bound.** In seven coordinates, use the five fixed queries
\[
Q=\{0,e_1+e_2,e_1+e_3,e_1+e_4,e_1+e_5\},
\]
where addition is binary XOR. Encode those query vectors as integers \(0,3,5,9,17\) with coordinate one the least-significant bit. The accompanying file `witnesses.json` lists 32 distinct seven-coordinate centers, one for every binary labeling of these five queries, in increasing label-mask order. The standalone `verify.py` checks all 160 indicated center-query evaluations and confirms that all 32 response masks appear. Thus \(\operatorname{VCdim}(\mathcal H^{(2)}_7)\ge5\). Appending zero coordinates simultaneously to every witness center and query preserves all distance-two answers, so the same five queries are shattered for every \(d\ge7\). By \(\operatorname{VCdim}\le\operatorname{Ldim}\) and Lemma 4, both dimensions equal five.

## Verification
Run `python3 verify.py` in the directory containing `verify.py` and `witnesses.json`. The program uses only the Python standard library, verifies every finite lower-bound witness against the exact Hamming-distance predicate, and checks sample structural fibers in dimensions seven through ten. Its final output is `DISTANCE_TWO_ALL_CHECKS_PASS`. The all-dimensions upper bound is the mathematical argument of Lemmas 1–4, **not** an extrapolation from those sample checks.

## Relationship to prior work
Adler, Benediktsson, and Macpherson study the VC dimension of open neighborhoods of standard Johnson and Hamming graphs. Their Hamming graphs join vertices at **distance one**, and they prove the optimal VC ceiling three for that edge relation. Their paper describes the distance-two vertex layer but does not replace the edge relation by an exact-distance-two query relation. The present five-dimensional classification concerns precisely that different relation, whose VC dimension exceeds three. The known open-neighborhood analyses for triangular and higher Johnson graphs similarly query Johnson adjacency, whereas Lemma 1 allows additional four-set containment queries; neither comparison implies the present bound by renaming parameters. General closure bounds for Littlestone dimension do not give the sharp value five here.

## Limitations
The novelty comparison is restricted to inspected accessible literature and semantic research-record searches; it is not proof of historical priority. The full Hamming-graph paper was inspected in its openly available accepted manuscript, including its definitions, principal theorems, and the section on Hamming neighborhoods. The theorem does not classify the smaller binary dimensions, nonbinary shells, or arbitrary other radii. No independent audit has been performed.

## References
1. I. Adler, B. G. Benediktsson, and D. Macpherson, *Vapnik–Chervonenkis Dimension and Density on Johnson and Hamming Graphs*, arXiv:2007.16042, first posted 2020-07-31; *Discrete Applied Mathematics* **312** (2022), 29–44. https://arxiv.org/abs/2007.16042 ; accepted full text: https://eprints.whiterose.ac.uk/id/eprint/178584/1/Adler_Benediktsson_Macpherson.pdf
2. B. Ghazi, N. Golowich, R. Kumar, and P. Manurangsi, *Near-tight Closure Bounds for the Littlestone and Threshold Dimensions*, ALT 2021, PMLR **132**, 686–696. https://proceedings.mlr.press/v132/ghazi21a.html
