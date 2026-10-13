# Every optimal five-output two-error one-unknown X-code is \(K_{2,3}\)
## Finding
For the standard binary \((m,n,d,x)\) X-code model,
\[
M(5,2,1)=6.
\]
Moreover, equality is rigid. Every six-codeword \((5,6,2,1)\) X-code consists entirely of Hamming-weight-two codewords. If the five coordinates are regarded as vertices and each weight-two support as an edge, the six supports are exactly the edges of a complete bipartite graph \(K_{2,3}\). Conversely, every labeled \(K_{2,3}\) on the five coordinates gives a valid \((5,6,2,1)\) X-code. Thus there are exactly \(10\) labeled maximum codes. The coordinate-permutation group \(S_5\) acts transitively on them, and the stabilizer of each maximum has order \(12\).

## Assumptions and scope
An \((m,n,d,x)\) X-code is a set \(\mathcal X\) of \(n\) distinct binary vectors of length \(m\) such that, for every set \(U\subset\mathcal X\) of exactly \(x\) unknown codewords and every disjoint error set \(E\subset\mathcal X\) with \(1\le |E|\le d\), the superimposed OR \(\bigvee U\) does not cover the XOR \(\bigoplus E\). Here only \(m=5\), \(d=2\), and \(x=1\) are considered. For a code of size at least two the zero vector is impossible, because a one-word error consisting of the zero vector has zero XOR and is covered by every unknown word.

For \(x=1\) and \(d=2\), writing codewords as supports, the condition is equivalently: the support family is an antichain, and for every three distinct supports \(A,B,D\), none of \(A\mathbin{\triangle}B\subseteq D\), \(A\mathbin{\triangle}D\subseteq B\), or \(B\mathbin{\triangle}D\subseteq A\) holds.

## Proof
A lower bound of six comes from the six edge-incidence vectors of \(K_{2,3}\). This graph has girth four, and the classical graph formulation of fan-out-two X-compactors identifies a graph of girth \(g\) with a constant-weight-two \((|V|,|E|,g-2,1)\) X-code.

For the upper bound and the equality classification, the finite search space is exhaustive. A maximum has size at least six, so it contains no zero codeword and is a subset of the \(31\) nonzero vectors of \(\mathbb F_2^5\). The packaged verifier examines every one of the
\[
\binom{31}{6}=736281
\]
six-subsets and every one of the
\[
\binom{31}{7}=2629575
\]
seven-subsets. Two independently implemented predicates are evaluated on every candidate: one directly tests the OR/XOR X-code definition, and the other tests the antichain/symmetric-difference formulation above. They agree on every candidate. Exactly ten six-subsets are valid and no seven-subset is valid. Since the X-code property is hereditary under deleting codewords, absence of a valid seven-subset excludes every larger code.

Each of the ten valid six-subsets is then checked to have six weight-two vectors. Its support graph has degree multiset \((3,3,2,2,2)\), and its edge set is exactly all six cross edges between the two degree-three vertices and the remaining three vertices. Hence every maximum is \(K_{2,3}\). Choosing the two-vertex part gives \(\binom{5}{2}=10\) labeled maxima, agreeing with the exhaustive census. Direct enumeration of all \(120\) coordinate permutations gives one orbit of size \(10\), so the stabilizer has order \(120/10=12\).

## Verification
Run `python3 artifacts/verify.py`. The verifier uses integer bit operations only and has no external dependencies. It replays a complete include/exclude search, the fixed-size exhaustive census with both predicates, the packaged census comparison, and the full coordinate-permutation orbit calculation. Its recorded output is:

```text
COMBINATIONS_CHECKED_6=736281
COMBINATIONS_CHECKED_7=2629575
SEARCH_NODES=1499
SMALL_MAXIMA=1,2,3,4
VERIFY_OK M(5,2,1)=6 labeled_maxima=10 all_K23=true S5_orbits=1 orbit_size=10 stabilizer=12
```

The verifier SHA-256 is `d0425ee1a147635addd8d095cb2233b1e7cc0ee7eabe1d9b3ad63acf64ffff0c`. The census SHA-256 is `eaff0c285f1905b3b48cbf90b010827af3d8633cd6ea5285b22e6c0639f5e6b6`. The recorded replay-output SHA-256 is `ae2e234bb963007abd77448db16fa4e02ea2c50b33ffde1dc67f2c5dfa9bbf42`.

## Relationship to prior work
Wohl and Huisman studied practical compactors in which every input has fan-out two and used graph theory to model that restricted class. Fujiwara and Colbourn later gave the equivalent X-code definition, defined \(M(m,d,x)\), explicitly noted that exact determination of \(M(m,d,x)\) is difficult beyond the one-error/one-unknown special case, and restated the graph-girth equivalence for constant-weight-two codes. Their graph theorem, together with the classical extremal structure of triangle-free graphs on five vertices, covers the fan-out-two \(K_{2,3}\) construction and its constant-weight-two optimality. It does not imply that arbitrary-weight \((5,n,2,1)\) X-codes cannot do better, nor that every unrestricted optimum must have weight two. The present finding is precisely that unrestricted equality statement and its complete labeled/symmetry census.

Later general work on optimal X-code length gives asymptotic and closed-form bounds for arbitrary parameters rather than this finite equality classification. Targeted searches for the exact parameter, its graph alias, and the unrestricted equality statement found no published statement that implies the ten-code census.

## Limitations
The theorem is only for binary \((5,n,2,1)\) X-codes. It does not classify larger output dimensions, other error/unknown parameters, or nonbinary variants. The 2003 one-page proceedings papers were available through metadata and abstracts rather than complete text; the 2010 paper was inspected in full through its lawful arXiv copy. An obscure or poorly indexed finite enumeration could therefore remain a residual originality risk. No independent audit has been performed.

## References
1. P. Wohl and L. Huisman, “Analysis and Design of Optimal Combinational Compactors,” Proc. IEEE VLSI Test Symposium, 2003, DOI:10.1109/VTEST.2003.1197639.
2. S. S. Lumetta and S. Mitra, “X-codes: Error Control with Unknowable Inputs,” Proc. IEEE International Symposium on Information Theory, 2003, DOI:10.1109/ISIT.2003.1228116.
3. Y. Fujiwara and C. J. Colbourn, “A Combinatorial Approach to X-Tolerant Compaction Circuits,” IEEE Transactions on Information Theory 56(7), 3196–3206, 2010, DOI:10.1109/TIT.2010.2048468; lawful full text at arXiv:1508.00481v1.
4. Y. Tsunoda and Y. Fujiwara, “Explicit Bounds on the Length of Optimal X-Codes,” Proc. IEEE International Symposium on Information Theory, 2017, DOI:10.1109/ISIT.2017.8007113.
