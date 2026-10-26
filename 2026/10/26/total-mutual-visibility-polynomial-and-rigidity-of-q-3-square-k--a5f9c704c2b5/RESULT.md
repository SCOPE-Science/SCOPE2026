# Total mutual-visibility polynomial and rigidity of \(Q_3\square K_n\)

## Finding

Let \(H_n=Q_3\square K_n\), where \(n\ge2\). Define the total mutual-visibility polynomial
\[
\mathcal V_{\mathrm t}(H_n;z)=\sum_{X\in\mathcal T(H_n)}z^{|X|},
\]
where \(\mathcal T(G)\) is the family of vertex sets \(X\) such that every pair of vertices of \(G\) has a shortest path whose internal vertices avoid \(X\). Then
\[
\boxed{\mathcal V_{\mathrm t}(H_n;z)=2(1+4z)^n-1+4((1+z)^n-1)^2+12nz^2+24nz^2((1+z)^{n-1}-1)+12\binom n2z^4.}
\]

The degree is \(2n\), so \(\mu_{\mathrm t}(H_n)=2n\). For \(n\ge3\) the coefficient of \(z^{2n}\) is four. Its four sets are exactly the antipodal cylinders \(\{b,\bar b\}\times[n]\), where \(\bar b\) complements each of the three bits of \(b\). The small case \(n=2\), equivalently \(Q_4\), has sixteen maximum sets. For \(n\ge3\), every total mutual-visibility set of cardinality at least \(n+2\) lies inside a single antipodal cylinder, and for each \(n+2\le k\le2n\) the number of sets of size \(k\) is \(4\binom{2n}{k}\).

## Assumptions and scope

All graphs are finite and simple. The vertex set of \(H_n\) is \(\{0,1\}^3\times[n]\), with adjacency when exactly one Cartesian coordinate changes; the fourth coordinate belongs to a complete graph. Thus graph distance equals the number of differing coordinates. Vertices of the same fourth-coordinate layer carry three-bit labels. A three-bit word has even or odd parity according to the parity of its number of ones. There are four words of each parity, and the bitwise complement maps the two parity classes bijectively. The polynomial counts distinct vertex subsets in a fixed labeled graph (not automorphism orbits).

The proof uses the established characterization that a subset of a Hamming graph is a total mutual-visibility set if and only if no two selected vertices are at graph distance two [1, Theorem 6]. All remaining enumeration and rigidity arguments are given here.

## Proof

**Layer restriction.** Fix a fourth coordinate \(i\in[n]\). Any two distinct three-bit words with the same parity differ in exactly two coordinates. Consequently, an admissible set contains at most one even-parity and at most one odd-parity word in layer \(i\). Conversely, that restriction eliminates all distance-two pairs *within* the layer: even and odd three-bit words differ in either one or three coordinates.

Let \(A\subseteq[n]\) denote layers containing a selected even word and \(B\subseteq[n]\) layers containing a selected odd word. For each \(i\in A\), denote its even word by \(e_i\); for each \(j\in B\), denote its odd word by \(o_j\). An even word and an odd word selected in distinct layers \(i\ne j\) form a distance-two pair exactly when their three-bit words differ in one coordinate. Since opposite-parity three-bit words have Hamming distance one or three, the distance-two prohibition is equivalent to
\[
  o_j=\overline{e_i}\qquad(i\in A,\ j\in B,\ i\ne j).
\]
Any two selected words of the same parity in distinct layers are separated by an odd graph distance (one or three), so there are no further constraints.

**Constraint graph.** Form a bipartite graph \(D(A,B)\) with an even-symbol vertex for each index in \(A\), an odd-symbol vertex for each index in \(B\), and an edge between symbols \(i\in A\) and \(j\in B\) precisely if \(i\ne j\). Along every edge, the odd label must equal the complement of the even label. Hence every connected component, including an isolated symbol vertex, has *exactly four* permitted label assignments: choose any one of the four even three-bit words at an even-symbol vertex (or its odd complement at an odd-symbol vertex), then propagate by complement. Even-length paths preserve this choice; all cycles in a bipartite graph are even, so propagation is consistent. Thus fixed nonempty \(A,B\) contribute precisely
\[
4^{c(D(A,B))}z^{|A|+|B|},
\]
where \(c\) includes isolated vertices. This also proves that no configurations are omitted.

**Connectivity census.** When \(A\) and \(B\) are both nonempty, the graph \(D(A,B)\) is connected except in exactly three disjoint situations:

1. \(|A|=|B|=1\) and \(A=B\): two isolated vertices.
2. One side is a singleton whose index lies on the other side, with the other side having at least two vertices: a star plus one isolated vertex.
3. \(|A|=|B|=2\) and \(A=B\): two independent edges.

In each exceptional case the graph has exactly two components. To verify completeness, if both sides have at least two vertices then any two vertices on the first side have a common neighbor whenever the other side has at least three vertices, because each omits at most its matching index. In the two-by-two case, the graph is connected unless both matching edges are omitted, exactly case 3. The cases with a singleton side follow directly from its star of permitted edges.

**Generating function.** If \(A=\varnothing\) or \(B=\varnothing\), each chosen layer independently carries one of four words of the retained parity, contributing \(2(1+4z)^n-1\), with the empty set counted once. If \(A,B\) are nonempty, assigning four choices to every pair \((A,B)\) contributes the baseline
\[
4\big((1+z)^n-1\big)^2.
\]
Each two-component exception has sixteen assignments instead of the four included in this baseline, hence requires a correction of twelve per pair \((A,B)\). Case 1 contributes \(12nz^2\). In case 2, choose the singleton index in \(n\) ways, choose at least one additional index on the other side, and choose which parity is singleton, giving
\[
24nz^2\big((1+z)^{n-1}-1\big).
\]
Case 3 gives \(12\binom n2 z^4\). Their sum with the baseline is exactly the displayed polynomial.

**Degree and rigidity.** For \(n\ge3\), the pure-parity summands have degree at most \(n\), all exceptional terms degree at most \(\max\{n+1,4\}\le n+1\), and the only contribution to degrees \(k\ge n+2\) comes from \(4((1+z)^n-1)^2\), yielding \(4\binom{2n}{k}\). On the other hand, for each of the four unordered antipodal binary pairs \(\{b,\bar b\}\), every subset of \(\{b,\bar b\}\times[n]\) is admissible: distinct vertices have distance one, three, or four, never two. For positive \(k\), these four families have disjoint sets of size \(k\) (the four full cylinders partition the vertex set). They supply \(4\binom{2n}{k}\) sets at size \(k\). Equality with the full coefficient proves that *every* admissible set at these sizes is contained in a unique antipodal cylinder. In particular, maximum size is \(2n\), with precisely four maximum sets for \(n\ge3\). The rigidity threshold is sharp: choose even and odd three-bit words \(e,o\) at Hamming distance one, put both at fourth coordinate \(1\), and put \(\bar o\) in each of the remaining \(n-1\) layers. The resulting admissible set has \(n+1\) vertices and is not contained in any antipodal cylinder. When \(n=2\), the polynomial has leading term \(16z^4\); its degree is still \(2n\), but the two-column exceptional configurations create twelve additional maximizers. This proves every assertion.

## Verification

The accompanying `verify.py` reconstructs \(Q_3\square K_n\), enumerates all vertex subsets that avoid distance-two pairs without using the parity-component formula, and compares the resulting cardinality vector with the theorem for \(1\le n\le6\). It separately samples direct breadth-first-search tests of the *definition* of total visibility, disallowing marked internal vertices, and checks equivalence to the distance-two characterization for \(1\le n\le3\). The output is `VERIFY_OK`; exact vectors and the number of checked sets appear in the verifier output. These finite computations corroborate but do not replace the all-\(n\) proof above.

## Relationship to prior work

Bujtás, Klavžar, and Tian [1, Theorem 6] proved the distance-two characterization used in the first step. They determine the maximum total mutual-visibility number of all Hamming graphs with three factors, but provide only general bounds and growth estimates in arbitrary higher dimensions [1, Theorems 1–3]. The family here has four factors, and neither its exact polynomial nor the large-set rigidity is stated by those theorems. Bujtás, Klavžar, and Tian [2] subsequently defined and investigated total visibility polynomials and provided formulas for other graph families; the formula here does not follow from their universal maximal-set inclusion-exclusion formula without determining this family's specific admissible-set structure. Existing low-distance mutual-visibility results for hypercubes involve a different constraint (visibility *between* selected vertices, sometimes truncated by distance), not the total visibility condition used here. The proof of this result explicitly derives the missing enumerative information rather than claiming the distance-two criterion itself as new.

## Limitations

The family consists only of the four-factor Hamming graphs with three binary factors and a fourth complete-graph factor. No exact formula for arbitrary four-factor Hamming graphs is claimed. The small case \(n=2\) does not satisfy the four-maximizer rigidity statement. The originality assessment may miss unindexed specialized work on distance-two avoidance and mixed-alphabet codes; no independent external validation is claimed. Finite verification ends at \(n=6\), whereas the mathematical proof covers all integers \(n\ge2\).

## References

[1] C. Bujtás, S. Klavžar, J. Tian, *Total mutual-visibility in Hamming graphs*, arXiv:2307.05168 (first posted 2023-07-11), Theorems 1–3 and 6, https://arxiv.org/abs/2307.05168 .

[2] C. Bujtás, S. Klavžar, J. Tian, *Visibility polynomials, dual visibility spectrum, and characterization of total mutual-visibility sets*, Aequationes mathematicae 99 (2025), 1883–1901, https://doi.org/10.1007/s00010-025-01197-y .
