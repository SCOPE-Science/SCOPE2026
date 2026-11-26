# Cube symmetry on the rational homology of the cuboctahedral perfect-matching complex

## Finding

Let \(C=L(Q_3)\) be the cuboctahedral graph, the line graph of the three-dimensional cube. Its perfect-matching complex \(K\) has vertex set \(E(C)\); a set is a simplex if and only if it is a subset of a perfect matching of \(C\). The **rational character on \(\widetilde H_2(K;\mathbb Q)\)** of the natural cube symmetry group \(B_3=(\mathbb Z/2)^3\rtimes\mathfrak S_3\) is as follows. An element acts on \(\{0,1\}^3\) by permuting the coordinates and then translating by a binary vector. A coordinate cycle is positive if the sum of the translation bits along it is even, and negative otherwise.

| Positive lengths | Negative lengths | Class size | \(\chi_2\) |
|---|---|---:|---:|
| \((1,1,1)\) | none | 1 | 43 |
| \((1,2)\) | none | 6 | 1 |
| \((3)\) | none | 8 | 1 |
| \((1,1)\) | \((1)\) | 3 | -1 |
| \((2)\) | \((1)\) | 6 | 5 |
| \((1)\) | \((1,1)\) | 3 | -1 |
| \((1)\) | \((2)\) | 6 | 3 |
| none | \((1,1,1)\) | 1 | -5 |
| none | \((1,2)\) | 6 | -1 |
| none | \((3)\) | 8 | 1 |

In particular, \(\dim_{\mathbb Q}\widetilde H_2(K;\mathbb Q)^{B_3}=2\). The previously established nonequivariant homotopy equivalence \(K\simeq\bigvee^{43} S^2\) [1] is a prerequisite, not part of the new claim.

## Assumptions and scope

The cube graph is on \(\{0,1\}^3\) with adjacency at Hamming distance one. An edge of \(C\) is an unordered pair of distinct cube edges with a common endpoint. A perfect matching of \(C\) consists of six such pairs, covering all twelve cube edges. The complex does not include nonextendable matchings. The action is the one induced by coordinate permutations and binary translations on the cube. The result computes a rational character for this graph only. It does not assert an equivariant wedge equivalence or an integral module splitting.

## Proof

By [1], reduced rational homology is concentrated in degree two and has dimension 43 there. To calculate the induced action, first enumerate the facets of \(K\) without omitting any extendable matching. Choose the least unused vertex of \(C\), pair it with each unused neighbor in turn, and recurse on the unused vertices. A given perfect matching has a unique choice at each recursion step, and every successful branch gives a perfect matching. There are 32 facets of six edges each. The full downset has 1,428 nonempty faces, with face counts by dimension \((24,192,520,468,192,32)\).

Each cube symmetry acts on these faces since it preserves adjacency and perfect matchings. For a face \(\sigma\) stabilized as a set, the trace on its oriented chain basis line is the sign of the induced permutation. Faces not stabilized as a set contribute zero. The alternating trace on the augmented chain complex equals that on reduced homology, so
\[
\chi_2(g)=-1+\sum_{\varnothing\ne\sigma\in K,\ g\sigma=\sigma}(-1)^{|\sigma|-1}\operatorname{sgn}(g|_{\sigma}).
\]
Equivalently, a stabilized face that consists of \(r\) cycles of the simplicial vertex permutation contributes \(-(-1)^r\), including \(-1\) for the empty face. This follows because the cycle permutation has sign \((-1)^{|\sigma|-r}\).

For each of the six coordinate permutations and eight translations, take the induced permutation on the unordered cube edges, and then on the pairs of incident cube edges. Test each face for stability and sum its signed contribution. Grouping by the positive and negative coordinate-cycle lengths gives the ten rows in the Finding. The class-weighted sum of the traces is 96, so averaging over the 48 elements gives invariant dimension two.

## Verification

Run `python3 verify_cubocta_pm.py` with Python 3.10 or newer. It evaluates the exact signed trace of every symmetry on the full enumerated face set and records the trace and size of each class. `VERIFIER_OUTPUT.txt` records these results. The same program also checks the input homology by an acyclic discrete-Morse computation and computes full mod-two boundary ranks as a separate consistency check. The signed augmented traces, together with the homology concentration, give the rational character; mod-two ranks alone do not determine it.

## Relationship to prior work and limitations

The earlier exact study [1] uses the same graph, face convention and facets, and proves the integral homotopy type. That nonequivariant equivalence determines the dimension of reduced homology, but not the action on it. The ordinary matching complex has all matchings as faces. It has a different topology and its octahedral character [2] is on a different homology group. An inclusion into that complex cannot recover the present character from the ordinary degree-three character: the ordinary complex has zero reduced degree-two homology. The perfect-matching-complex framework and earlier honeycomb classifications are due to Bayer, Jelić Milutinović and Vega [3]. No inspected comparison gives the signed-cycle table above for the extendability subcomplex. This is a bounded comparison, not an exhaustive priority claim.

## References

1. *The cuboctahedral perfect-matching complex is a wedge of 43 two-spheres*, Resultary, 2026-10-25, [record](https://github.com/Resultary/2026/blob/main/2026/10/25/SCOPE-the-cuboctahedral-perfect-matching-complex-is-a-wedge-of-43-two--6019e1380eb9/RESULT.md).
2. *The full octahedral character of the cuboctahedral matching complex*, Resultary, 2026-10-18, [record](https://github.com/Resultary/2026/blob/main/2026/10/18/SCOPE-the-full-octahedral-character-of-the-cuboctahedral-matching-comp--7b3e0e6810dc/RESULT.md).
3. M. Bayer, M. Jelić Milutinović, and J. Vega, *Perfect Matching Complexes of Honeycomb Graphs*, *Electronic Journal of Combinatorics* **30** (2023), P2.45, [arXiv:2209.02803](https://arxiv.org/abs/2209.02803), doi:10.37236/11525.
