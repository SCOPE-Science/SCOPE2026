# Eleven minimum zero-forcing orbits and their propagation times on the four-cube

## Finding

For ordinary zero forcing on the sixteen-vertex cube \(Q_4\), the \(2360\) minimum zero-forcing sets form exactly eleven orbits under the full automorphism group, as listed below. All have size eight, and every inclusion-minimal zero-forcing set is one of them, so \(Q_4\) is well-forced. When all available forces are applied simultaneously in each round, exactly \(8,816,1152,384\) minimum sets finish in \(1,2,3,4\) rounds, respectively.

| Least representative mask | Orbit size | Synchronous rounds |
|---:|---:|---:|
| 255 | 8 | 1 |
| 495 | 192 | 2 |
| 975 | 96 | 2 |
| 987 | 192 | 2 |
| 989 | 384 | 3 |
| 1695 | 48 | 2 |
| 1719 | 384 | 3 |
| 1971 | 192 | 2 |
| 1973 | 384 | 3 |
| 6030 | 96 | 2 |
| 6042 | 384 | 4 |

## Assumptions and scope

Vertices are four-bit vectors indexed by integers \(0,\ldots,15\); adjacency is Hamming distance one. A decimal mask \(s\) denotes the vertices whose bits in \(s\) are one. Initially these vertices are black and the others white. A black vertex can force its unique white neighbor, if it has exactly one. The round begins with a fixed coloring, and all targets available in that coloring are blackened at its end; repeated targets are counted only once. “Minimum” refers to cardinality; “inclusion-minimal” forbids any proper zero-forcing subset. Only ordinary zero forcing on \(Q_4\) is considered.

## Proof by exhaustive finite computation

1. **Exact synchronous update.** For a subset \(B\) of black vertices, put
   \[
   \Phi(B)=B\mathbin\cup\{w:\exists v\in B,\ N(v)\setminus B=\{w\}\}.
   \]
   If \(B\subseteq B'\) and \(w\in\Phi(B)\setminus B'\), its witnessing vertex is black in \(B'\) and still has just the one white neighbor \(w\). Thus \(\Phi\) is monotone. From any initial set all strict updates enlarge it, so they stop within sixteen rounds of additions. Any sequential forcing process stays in that terminal set: every legal target outside a larger force-closed set would contradict closure by the same witness argument. Conversely each synchronous batch can be applied sequentially by skipping already black targets, since all still-white targets keep their witnesses. Thus reaching all vertices under \(\Phi\) is equivalent to ordinary zero forcing, and the number of strict updates in a successful run is its synchronous time.
2. **Exhaustion and minimality.** The verifier computes \(\Phi\) to termination for all integers \(0\le s<2^{16}\), implementing \(N(v)\) as the four masks at \(v\mathbin{\mathrm{xor}}2^j\), \(0\le j<4\). A successful \(s\) is inclusion-minimal exactly when every single-vertex deletion is unsuccessful. This follows from upward closure of forcing, itself a consequence of monotonicity of \(\Phi\). The verifier obtains least successful size eight and exactly \(2360\) inclusion-minimal sets, all of size eight. It also checks directly that this family equals the successful sets of size eight.
3. **Group and orbits.** Translations by XOR with a fixed bit vector and coordinate permutations preserve the cube. After fixing 0 and its four neighbors, an automorphism fixes every vertex: by induction on Hamming weight \(r\ge2\), a vertex is the unique weight-\(r\) vertex adjacent to all its weight-\((r-1)\) predecessors obtained by deleting one bit. Indeed a weight-\(r\) neighbor must contain each predecessor's support, and their union is the original support. Hence the listed \(16\cdot24=384\) transformations are the full group. The verifier applies all of them to the least remaining mask, checks the orbit is wholly unassigned and has constant synchronous time, then removes it. This gives the eleven rows above and exhausts the family. Summing orbit sizes by time gives the round counts in the finding.

## Verification

Run `python3 verify_minimum_orbits.py` from this directory (Python 3.10 or later, standard library only). The program recomputes all subset decisions, minimality and orbit data, and checks exact agreement with `CLASSIFICATION.json`. This is a finite exhaustive check, not a theorem for cubes of other dimensions or a formal proof certificate.

## Relationship to prior work

The scalar \(Z(Q_4)=8\) is known from the hypercube result of the AIM Minimum Rank – Special Graphs Work Group (*Linear Algebra and its Applications* 428 (2008), 1628–1648). Brimkov, Cameron and Grubbs ([arXiv:2507.10826v1](https://arxiv.org/abs/2507.10826), §4 and Conclusion) already give examples of minimum sets realizing the four synchronous times; their conclusion leaves the complete minimum-set census open. The census here supplies exact orbit representatives and sizes, the multiplicity of each time, and the check that no larger inclusion-minimal set occurs. Curtis et al. ([arXiv:2208.12899](https://arxiv.org/abs/2208.12899), Figure 2 and Equation (1)) already give an exact aggregate forcing-probability curve for this graph, which encodes its size polynomial. Such counts by size do not identify symmetry classes or propagation times. The polynomial is not claimed here. The five-orbit fort classification is also not part of the finding; see the separate indexed record [Five orbit types of inclusion-minimal forts of \(Q_4\)](https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-five-orbit-types-of-inclusion-minimal-forts-of-q-4--4b4a85b72c98).

## Limitations

This is an exhaustive census of one specified graph using the ordinary color-change rule. The time counts are synchronous, not a claim about lengths of sequential forcing chains or other forcing variants. The comparisons above do not rule out other unindexed calculations.
