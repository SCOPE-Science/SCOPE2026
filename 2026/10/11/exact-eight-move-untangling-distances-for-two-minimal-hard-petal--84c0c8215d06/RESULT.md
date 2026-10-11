# Exact eight-move untangling distances for two minimal hard petal unknots
## Finding
Let \(\mathcal M=\{\mathsf T^{\pm},\mathsf X,\mathsf R,\mathsf S\}\) be the petal-permutation move set consisting of trivial petal addition/deletion, crossing exchange, height rotation, and half-turn. Let \(d_{\mathcal M}\) count every move in \(\mathcal M\) with cost one, while cyclic rotation of the indices is part of the definition of a petal word and therefore has cost zero. For
\[
\alpha=(0,2,4,1,5,7,3,8,6),\qquad
\beta=(0,2,5,3,8,1,7,4,6),
\]
the exact distances to the one-petal word are
\[
d_{\mathcal M}(\alpha,(0))=d_{\mathcal M}(\beta,(0))=8.
\]

## Assumptions and scope
The conventions and move definitions are those of Vernitski, arXiv:2610.01596v1. In particular, \(\alpha\) and \(\beta\) are the two named nine-petal hard-unknot representatives whose excess is \(2\). The prior result that each is hard is used as an input; the present claim concerns the number of moves, not knot-type certification or excess. No statement is made here about \(\gamma\), about every member of the six hard dihedral orbits, or about other move sets.

## Proof
Write \(a\), \(d\), and \(p\) for the numbers of trivial petal additions, trivial petal deletions, and petal-number-preserving moves, respectively, in an untangling path from a nine-petal word to \((0)\). Only \(\mathsf T^+\) and \(\mathsf T^-\) change the number of petals, by \(+2\) and \(-2\). Hence
\[
d-a=4,
\]
and a path of length \(L\) satisfies
\[
L=a+d+p=2a+4+p.
\]
Vernitski proves that \(\alpha\) and \(\beta\) are hard for \(\mathcal M\), so every untangling path has \(a\ge 1\). Therefore any hypothetical path with \(L\le 7\) must have exactly one addition, exactly five deletions, and at most one petal-number-preserving move.

It remains to exclude those short possibilities. The accompanying exact verifier uses the published definitions of \(\mathsf T^{\pm}\) and \(\mathsf X\), identifies cyclic index rotations, and makes the lower-bound search strictly easier by allowing arbitrary \(\mathsf R\) and \(\mathsf S\) moves at zero cost. Thus every genuine path of length at most \(7\) is represented in the relaxed search by one \(\mathsf T^+\), five \(\mathsf T^-\), and at most one \(\mathsf X\). The exhaustive relaxed search finds, for each of \(\alpha\) and \(\beta\), \(144\) symmetry classes after one addition, only one class after one addition followed by one deletion, six classes after one addition and one crossing exchange, and no class after one addition and two deletions. In particular neither count pattern with one addition and five deletions reaches \((0)\), with or without one crossing exchange. Hence \(d_{\mathcal M}\ge 8\).

For the matching upper bound, Vernitski gives explicit untangling sequences for both \(\alpha\) and \(\beta\). Each sequence has one \(\mathsf T^+\), two \(\mathsf X\), and five \(\mathsf T^-\) moves, hence eight moves total. The verifier independently checks every transition of those two displayed sequences against the move definitions. Thus \(d_{\mathcal M}\le 8\), proving equality.

## Verification
Run `python3 artifacts/verify_petal_distance.py`. It uses only the Python standard library and prints

`VERIFY_OK alpha_distance=8 beta_distance=8`

followed by the finite-state counts used in the lower bound. The verifier checks the two eight-move upper-bound paths and exhaustively enumerates the relaxed short-path state space described above. The relaxation is one-sided in the safe direction: treating \(\mathsf R\) and \(\mathsf S\) as free can only shorten paths, so failure to reach \((0)\) in the relaxed search proves failure for the original counted move metric.

## Relationship to prior work
Vernitski proves that the two words are hard and have excess \(2\), and gives explicit untangling sequences as upper bounds realizing that excess. The paper's computational search is organized by a maximum allowed petal count, and its tables record hardness and excess data; it does not state a shortest-move distance for \(\alpha\) or \(\beta\). The eight-step displayed sequences therefore give only the upper bound needed here. The new ingredient is the exact short-path exclusion, which converts those sequences into geodesics in the move graph.

Colton, Glover, Hughes, and Sandberg prove that trivial petal additions/deletions and crossing exchanges connect any two petal permutations of isotopic knots. That completeness theorem supplies the underlying move calculus but no minimum-length statement for these two words.

## Limitations
The computation proves only the two stated distances under the move set \(\mathcal M\). It does not determine the distance for \(\gamma\), classify distances of all hard nine-petal words, or compare alternative generating sets. The checker relies on Vernitski's already-certified facts that \(\alpha\) and \(\beta\) represent the unknot and are hard; it does not re-certify knot type. The finite enumeration is exhaustive only for the short-path regime forced by the counting identity above, which is sufficient for the claimed lower bound.

## References
1. A. Vernitski, *Some petal diagrams of the unknot are hard*, arXiv:2610.01596v1, first posted 2026-10-01.
2. L. Colton, C. Glover, M. Hughes, and S. Sandberg, *A Reidemeister type theorem for petal diagrams of knots*, Topology and its Applications 267 (2019), 106896; arXiv:1812.08930.
