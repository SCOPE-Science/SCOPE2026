# Simple-homotopy reduction of the twenty-five-vertex Schrijver independence complex

## Finding
Let \(G=SG_{4,2}\) be the Schrijver graph whose vertices are cyclically stable four-subsets of \(\{1,\ldots,10\}\), with two vertices adjacent precisely when their underlying subsets are disjoint. Then
\[
\operatorname{Ind}(G)\simeq S^3\vee S^4\vee S^4.
\]
More precisely, the face poset of \(\operatorname{Ind}(G)\) admits an explicit acyclic Forman matching whose ordinary Morse CW complex has one zero-cell, one three-cell and two four-cells; both four-cell attaching maps have degree zero. Consequently its reduced integral homology is \(\mathbb Z\) in degree three, \(\mathbb Z^2\) in degree four, and zero in every other degree.

## Assumptions and scope
A four-subset \(A\subseteq\{1,\ldots,10\}\) is *cyclically stable* if no two of its elements are adjacent modulo ten, including the pair \(\{1,10\}\). List all such sets in increasing lexicographic order as \(A_0,\ldots,A_{24}\). There are exactly twenty-five. The edge set of \(G\) consists of the sixty unordered pairs \(\{A_i,A_j\}\) with \(A_i\cap A_j=\varnothing\). A face of \(\operatorname{Ind}(G)\) is a family of those stable sets that is pairwise intersecting. Thus the graph is defined independently of any drawing or software graph-library labeling. The claim concerns this single finite complex, not arbitrary Schrijver parameters or its distinct Lovász neighborhood complex.

## Proof
**Face set.** Encode a family of graph vertices by a 25-bit nonnegative integer. For each index \(i\), let \(N_i\) be the bit mask of all graph neighbors of \(A_i\). Starting from the singleton family containing only the empty face, successively add to the face collection every mask \(F\cup\{i\}\) with \(i\notin F\) and \(F\cap N_i=\varnothing\). Induction on \(i\) proves this constructs exactly every independent set, once. The exact face counts in dimensions zero through nine are
\[
(25,240,1160,3140,5079,5160,3370,1380,320,32).
\]
There are 19,906 nonempty faces and, with the empty face, 19,907 masks.

**Matching.** Use the fixed pivot sequence, in zero-based lexicographic indexing,
```
(12, 9, 3, 21, 19, 13, 11, 18, 17, 15, 5, 8, 2, 7, 0, 4)
```
At each pivot \(i\), among the faces not yet removed, match every pair \((F,F\cup\{i\})\) whose two members remain, then remove both members before advancing. No mask is matched twice; the construction yields 9,952 augmented pairs, one of which contains the empty face. Remove that single empty-face pair from consideration to obtain an ordinary matching of 9,951 pairs on the nonempty faces. Its four critical faces are one zero-face (the vertex previously matched to the empty face), the three-face with mask `11008`, and the four-faces with masks `98690` and `8405089`. These are actual masks in the explicitly fixed indexing, not opaque external certificates.

**Acyclicity.** For each nonempty face and each one-element deletion, orient the corresponding Hasse incidence downwards unless it is a matched pair, in which case orient upwards. The verifier enumerates every incidence, including those of the augmented face poset, giving 110,730 incidences. It topologically sorts the full directed graph and processes all 19,907 masks. Hence the augmented orientation has no directed cycles; removing the empty mask and its incident edges gives the claimed acyclic ordinary matching. By Forman's discrete Morse theorem, the complex is homotopy equivalent to a CW complex with one zero-cell, one three-cell and two four-cells.

**Integral attaching degrees.** Orient every simplex by its increasing vertex indices. If \(F\) is obtained from \(B\) by deleting the vertex of index \(j\), its signed incidence is \((-1)^{|\{i\in F:i<j\}|}\). To compute the Morse differential from dimension four to three, recursively project each three-face onto the unique critical three-face: return one on that critical face; return zero on an upper member of a matching from dimension two to three; and, if \(F\) is the lower member of a matching with four-face \(B\), solve the unit-incidence boundary equation for its coefficient by substituting the projections of all other three-faces in \(\partial B\). This recursion terminates because the complete matching is acyclic. Summing these projected coefficients in the boundaries of the two critical four-faces gives, with their integer signs, exactly \((0,0)\). Thus the cellular attaching maps \(S^3\to S^3\) have degrees zero. Since \(\pi_3(S^3)\cong\mathbb Z\) via degree, both maps are nullhomotopic. The Morse CW complex is therefore the stated wedge of spheres.

## Verification
Run `python3 verify_homotopy.py` and `python3 verify_homology.py` with Python 3.10 or later. Both are standalone standard-library programs and construct the graph directly from the cyclic-stability definition. The first checks the precise face vector, matching pairs, critical-cell masks and dimensions, every Hasse incidence, a complete acyclicity topological sort, and the signed **integer** projection of each four-cell attachment. The second independently reconstructs all independent sets and performs mod-two boundary-rank elimination, giving ordinary Betti numbers \(\beta_0=1\), \(\beta_3=1\), \(\beta_4=2\), all others zero. The independent field computation is corroboration only; it does not substitute for the integral attaching calculation.

The first script prints `VERIFY_HOMOTOPY_OK vertices=25 edges=60 faces=19907 pairs=9951 critical=1x0+1x3+2x4 incidences=110730 attaching=[0,0]`; the second prints `VERIFY_HOMOLOGY_OK faces=19907 betti_mod2={0:1,3:1,4:2}`.

## Relationship to prior work
Braun's *Independence Complexes of Stable Kneser Graphs* (arXiv:0912.0720v1, submitted 2009-12-03) defines precisely this graph family and, in the introduction and Section 4, identifies the topology of \(\operatorname{Ind}(SG_{n,2})\) as unresolved in that work. His Theorem 1.4 concerns the different parameter family \(SG_{2,k}\); Theorem 1.5 computes the independence complex of the related, but nonisomorphic, auxiliary graph \(E_{2n+2}\). Neither theorem asserts the present homotopy type. Braun and Zeckner's later *Deformation Retracts of Neighborhood Complexes of Stable Kneser Graphs* (arXiv:1102.1984v1, submitted 2011-02-09) treats the **neighborhood complex**, which is not the independence complex. Kozlov's *Simple homotopy types of Hom-complexes, neighborhood complexes, Lovász complexes, and atom crosscut complexes* (arXiv:math/0503613v1, submitted 2005-03-28; primary MSC 57Q10) provides closely relevant formal-deformation topology but no calculation for this graph. The result here is a finite explicit discrete-Morse calculation, not a consequence claimed by any of these papers.

## Limitations
Only \(SG_{4,2}\) is classified here. No general \(SG_{n,2}\) formula, persistence barcode, or statement about neighborhood complexes follows. The proof uses a machine-replayable finite enumeration and exact integer arithmetic; the entire finite case is exhaustive, but no infinite family was tested exhaustively. The comparison with literature does not establish priority over all possible unindexed work.

## References
- B. Braun, *Independence Complexes of Stable Kneser Graphs*, arXiv:0912.0720v1 (2009), https://arxiv.org/abs/0912.0720 . See Introduction, Section 2 and Section 4.
- B. Braun and M. Zeckner, *Deformation Retracts of Neighborhood Complexes of Stable Kneser Graphs*, arXiv:1102.1984v1 (2011), https://arxiv.org/abs/1102.1984 .
- D. N. Kozlov, *Simple homotopy types of Hom-complexes, neighborhood complexes, Lovász complexes, and atom crosscut complexes*, arXiv:math/0503613v1 (2005), https://arxiv.org/abs/math/0503613 .
- R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
