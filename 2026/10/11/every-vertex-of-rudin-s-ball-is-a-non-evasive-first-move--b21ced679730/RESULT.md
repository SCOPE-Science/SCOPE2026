# Every vertex of Rudin's ball is a non-evasive first move

## Finding
Let \(R\) be Rudin's triangulated 3-ball with 14 vertices and 41 tetrahedra, using the labeled facet list printed in Benedetti--Lutz. A vertex \(v\) of a simplicial complex \(K\) is called *admissible* here when both \(K-v\) and \(\operatorname{lk}_K(v)\) are non-evasive. This is exactly the condition that \(v\) can be the first vertex queried in the recursive definition of non-evasiveness.

Every vertex of \(R\) is admissible. Thus the known non-evasiveness of Rudin's ball is maximally flexible at the first step: no choice of first vertex can obstruct the recursion.

There is also a sharp second-step profile. For each first vertex \(v\), count the admissible vertices of \(R-v\). The multiset of these fourteen counts is
\[
\{11^6,9^4,5^4\}.
\]
Hence exactly \(6\cdot 11+4\cdot 9+4\cdot 5=122\) ordered pairs of distinct vertices can occur as the first two deletion queries in a recursive non-evasiveness witness.

## Assumptions and scope
The simplicial complex is the 41-facet labeled complex in Benedetti--Lutz, Theorem 6.3. Non-evasiveness is used in its standard recursive sense: a one-vertex complex is non-evasive; a larger nonempty complex is non-evasive when it has a vertex whose deletion and link are both non-evasive. The empty-face-only complex is not taken as a base case.

The result concerns admissibility for this exact labeled triangulation. The statement that all fourteen first choices are admissible is label independent; the second-step statement is given as a multiset and is therefore also invariant under relabeling.

## Proof
The bundled verifier stores the published 41 tetrahedra and canonicalizes each intermediate complex by retaining only inclusion-maximal faces. For a complex \(K\) and a vertex \(v\), it computes
\[
K-v=\{\sigma\setminus\{v\}:\sigma\in K\}
\]
followed by removal of subsumed facets, and it computes
\[
\operatorname{lk}_K(v)=\{\sigma\setminus\{v\}:v\in\sigma\in K\}
\]
with the same canonicalization.

A memoized exhaustive recursion then evaluates non-evasiveness exactly from the definition. For each of the fourteen vertices \(v\), it independently evaluates the two required predicates for \(R-v\) and \(\operatorname{lk}_R(v)\). All twenty-eight predicates are true, so every first vertex is admissible.

The same exact test is then applied to every remaining vertex of every first deletion \(R-v\). The numbers of admissible second vertices, in labels \(1,\ldots,14\), are
\[
11,11,11,11,11,11,9,9,9,9,5,5,5,5.
\]
Their multiset is therefore \(\{11^6,9^4,5^4\}\), and their sum is \(122\).

## Verification
Running `verify.py` from the package returns exactly

`VERIFY_OK facets=41 f=14,66,94,41 roots=14/14 second_profile=11x6,9x4,5x4 second_total=122 memo_states=28708`

The verifier first checks the face vector \((14,66,94,41)\), then checks all fourteen first-step conditions, then recomputes the complete second-step admissibility profile. No randomized search, timeout inference, or partial enumeration is used.

## Relationship to prior work
Rudin constructed the unshellable 14-vertex ball in 1958. Benedetti and Lutz later proved in Theorem 6.3 that Rudin's ball is non-evasive and printed the exact 41-facet list used here. Their proof exhibits one particular recursion beginning with vertex \(3\) and then a specified deletion sequence. The present statement is stronger in a different direction: every one of the fourteen vertices, not just one exhibited choice, satisfies the defining first-step condition, and the second-step flexibility has the exact profile above.

Searches for the exact object together with “every vertex deletion”, “all vertices”, “non-evasive roots”, “first query”, and equivalent deletion/link formulations found the published theorem that \(R\) is non-evasive, but no statement that all vertices are admissible or any exact two-step profile. The standard implication “vertex-decomposable implies non-evasive” does not cover the result because Rudin's ball is specifically used as a non-evasive ball that is not vertex-decomposable.

## Limitations
This is an exact finite statement about one canonical triangulation. It does not claim that arbitrary non-evasive balls have all vertices admissible, nor does it classify complete decision trees or count all non-evasiveness witnesses. The originality comparison is limited by indexing: an older unindexed computation could in principle have recorded the same root profile.

## References
1. M. E. Rudin, *An unshellable triangulation of a tetrahedron*, Bulletin of the American Mathematical Society 64 (1958), 90--91, DOI 10.1090/S0002-9904-1958-10168-8.
2. B. Benedetti and F. H. Lutz, *Knots in collapsible and non-collapsible balls*, arXiv:1303.2070v1; Electronic Journal of Combinatorics 20(3) (2013), P31, DOI 10.37236/3319.
