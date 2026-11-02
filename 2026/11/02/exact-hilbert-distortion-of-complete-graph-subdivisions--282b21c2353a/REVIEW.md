# Scientific review: exact Hilbert distortion of complete-graph subdivisions

## Correctness

**PASS.** The graph metric is exactly the Hamming distance restricted to singleton and doubleton indicators. Symmetrizing a Euclidean Gram matrix preserves the relevant linear inequalities, so no nonsymmetric embedding can evade the lower bounds. The two-orbit permutation representation decomposes into trivial, standard, and the doubleton-only orthogonal component, yielding a positive-semidefinite parameterization with \(C^2\leq AB\). The inequality between an incident singleton–doubleton squared distance and a disjoint-doubleton squared distance proves the infinite-dimensional bound for every \(n\geq5\). For \(n=4\), the nonincident singleton–doubleton constraint and disjoint-doubleton constraint jointly yield an algebraic minimax lower bound. At \(n=3\), the same covariance method gives \(9/4\); at \(n=2\) the metric is a path. Explicit centered-coordinate embeddings attain every bound. A standard-library exact checker tests 12,006 pairwise inequalities and independent graph-distance recurrences for small orders. All-order correctness comes from the written inequalities, not from the finite tests.

## Originality

**PASS, qualified.** The result determines least Euclidean distortion of the metric \(S(K_n)\), unlike the published classification of its isometric embedding into a Hamming cube. The distance-regular graph theory of Cioabă et al. does not apply to \(S(K_n)\) for \(n\geq4\), whose two vertex classes have distinct degrees. The Hamming-subset distance-matrix theorem of Doust and Wolf concerns an \(M\)-constant rather than a sharp least-distortion value. Results on uniform subdivision edge-flow projection constants and on partial subdivision negative-type exponents do not imply least Hilbert distortion. The value for \(n=3\) is a known six-cycle boundary, not a new standalone claim. No covering formula for \(n\geq4\) was identified in the searches, but failure to find one does not prove priority. The original full text of Beaudou et al. could not be inspected; its abstract and a detailed contemporary discussion concern Hamming embeddings, and it remains a qualified historical source risk.

## Value

**PASS.** The object is a canonical non-distance-regular partial cube with two natural rank layers; the target invariant is the least Hilbert distortion, not a chosen embedding's distortion. The result gives an all-order sharp invariant with an unexpected isolated algebraic exception at \(n=4\), rational formulas for every larger order, an exact limit, and optimal embeddings of dimension at most \(n-1\). The lower bound is attained using a local configuration of an incident singleton–doubleton pair and disjoint doubletons, giving a reusable symmetry/semidefinite technique. This is a structurally motivated exact invariant rather than an arbitrary small-instance table.

## Sources and limitations

Primary motivating research: Cioabă–Gupta–Ihringer–Kurihara, arXiv:2109.09708 (2021-09-20); Doust–Wolf, arXiv:2109.07052 (2021-09-15). The closest same-object reference is Beaudou–Gravier–Meslem, DOI 10.1137/070681909, whose accessible abstract proves a Hamming-embedding classification rather than the stated Hilbert distortion theorem. Available historical records were checked for implication overlap. Remaining risks include an older equivalent result phrased as two-rank Boolean metric distortion, a hidden lemma in the inaccessible full text, or a more general finite-metric distortion result specializing to this formula. Weighted and nonuniform subdivisions are not treated.

Self-review: passed. Independent audit: not yet performed.
