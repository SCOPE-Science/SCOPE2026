# Exact quinary multiset one-deletion optima at lengths \(9\) and \(10\)

## Finding

For multisets over five symbols, the two first blocklengths beyond the finite cases computed in [1] have the exact values
\[
 S_5(9,1)=143,\qquad S_5(10,1)=201.
\]
Both are attained by the established prime-field one-syndrome construction. The new contribution is the computationally sharp upper bounds at these two blocklengths, not the construction itself or a proof for all blocklengths.

## Assumptions and scope

The alphabet is exactly \(\{0,1,2,3,4\}\). A transmitted multiset of size \(n\) is its multiplicity vector \(x=(x_0,\ldots,x_4)\) with nonnegative integer entries summing to \(n\). Its one-deletion shadow consists of the vectors \(x-e_i\) for all \(i\) with \(x_i>0\). A code corrects one deletion precisely when the shadows of distinct codewords are disjoint. The invariant \(S_5(n,1)\) maximizes the number of codewords; no restriction to linear, additive, or symmetric constructions is imposed.

Only \(n=9\) and \(n=10\) are claimed. The bounds are computational finite searches, not a general argument that Conjecture 21 holds for all larger lengths.

## Proof

**Lower bounds.** For \(a\in\mathbb Z/5\mathbb Z\), let
\[
 C_a(n)=\{x:\sum_{i=0}^4 x_i=n,\ \sum_{i=0}^4 i x_i\equiv a\pmod5\}.
\]
When \(y=x-e_i\), the syndrome of \(x\) is the syndrome of \(y\) plus \(i\) modulo five. Thus each received \(y\) has at most one possible parent in each \(C_a(n)\), and every \(C_a(n)\) corrects one deletion. Stars-and-bars enumeration gives \(\binom{13}{4}=715\) words of length nine and \(\binom{14}{4}=1001\) words of length ten. For nine, the five syndrome classes each have size \(143\); for ten, the zero class has \(201\) and each nonzero class has \(200\). The standalone combinatorial verifier rechecks these integers without external data. These witness constructions and their general class-size formula are prior work [1].

**Exact upper-bound reduction.** List all \(N=\binom{n+4}{4}\) vectors \(x\) and introduce a binary variable \(z_x\) for each. For every \(y\) with \(\sum y_i=n-1\), impose
\[
 \sum_{i=0}^{4} z_{y+e_i}\leq1.
\]
Maximizing \(\sum_x z_x\) over binary variables is *exactly* \(S_5(n,1)\): every feasible selection has pairwise disjoint deletion shadows, and every such code induces a feasible selection. This equivalence is elementary and has no numerical approximation.

Independently, construct the graph on those \(x\), with an edge between \(x\) and \(x-e_i+e_j\) whenever \(i\ne j\) and \(x_i>0\). Two distinct words share a one-deletion output if and only if they differ by precisely one such transfer. Thus the identical optimum is described by binary variables with pair constraints \(z_x+z_{x'}\leq1\) for all edges. The combinatorial verifier constructs all conflict edges in both ways and checks their exact equality.

**Exhaustive computation.** For \(n=9\), the shadow formulation has 715 binary variables, 495 shadow inequalities and 2475 nonzero constraint entries; the edge formulation has 4950 conflict inequalities. For \(n=10\), these figures are 1001, 715, 3575 and 7150, respectively. The complete supplied programs solve each integer program using SciPy's mixed-integer branch-and-bound interface to HiGHS, with the relative optimality tolerance set to zero. All four runs terminated with reported optimal status, an incumbent equal (within numerical tolerance) to the constructed lower bound, and a *dual upper bound* below the next integer: below 144 for \(n=9\) and below 202 for \(n=10\). Since the objective is integer, these certify the asserted sharp upper bounds conditional on the numerical solver's correctness. In the shadow formulation, the returned binary solution was also rounded and verified against every exact incidence constraint.

The combinatorial cross-check separately verifies that the two generated conflict graphs agree edge-for-edge, that the zero-syndrome witnesses have the stated sizes and no conflicting pair, and that their vertices cover all weak compositions. Hence the result is not inferred from a limited sample of candidate codes.

## Verification

Use Python 3 with NumPy and SciPy. The five standalone scripts under `verification/` are runnable individually:

`python verification/combinatorial_check.py`

`python verification/shadow_n9.py`

`python verification/shadow_n10.py`

`python verification/edges_n9.py`

`python verification/edges_n10.py`

The recorded outputs for all five scripts are included in `verification/recorded_outputs.txt`. In the observed execution, SciPy version 1.17.0 and NumPy version 2.3.5 were installed. Reruns require the same mathematical optimizer, but can differ in time and tiny floating-point rounding.

## Relationship to prior work

Reference [1], particularly Section 5.5 and Conjecture 21, reports the exact five-symbol optimum for lengths one through eight and explicitly conjectures that the sum-modulo-five class is optimal for all but lengths two and four. Its first two uncomputed cases are the present \(n=9,10\). The construction attaining 143 and 201 is not new. Reference [2] develops general finite-dimensional multiset and deletion bounds but was not found to force these sharp values. Reference [3] studies geometry of multiset deletion balls and bounds rather than settling these two finite integer optima. The present conflict graph is the unit-transfer graph (distance two in \(\ell_1\)); broader simplicial rook graphs allowing larger transfers are **not** equivalent. No claimed implication of a stronger prior theorem was identified in the inspected sources; equivalent coverage in older grid-code tables remains a risk.

## Limitations

The computational upper bound is dependent on SciPy/HiGHS's floating-point mixed-integer solver and its reported global dual bounds; no independently checkable exact rational branch-and-bound trace or alternative analytic proof is provided. Two independently enumerated formulations and exact combinatorial cross-checks lessen modeling risk, but their optimizers use the same backend and are not independent mathematical certifications. The theorem neither asserts uniqueness of the optimum nor resolves the five-symbol conjecture beyond these two lengths. The literature search cannot rule out unindexed prior coverage.

## References

[1] A. Kreindel, I. Barouch Essayag, and A. L. Zabokritskiy, *Multiset Deletion Codes: Cyclic Constructions, Bounds, and Exact Results*, arXiv:2601.05636v2 (first public version 2026-01-09), especially §5.5, Conjecture 21. https://arxiv.org/html/2601.05636v2

[2] M. Kovačević and V. Y. F. Tan, *Codes in the Space of Multisets—Coding for Permutation Channels with Impairments*, arXiv:1612.08837. https://arxiv.org/abs/1612.08837

[3] A. Kreindel, I. Barouch Essayag, and A. L. Zabokritskiy, *Polynomial Constructions and Deletion-Ball Geometry for Multiset Deletion Codes*, arXiv:2603.18322 (2026). https://arxiv.org/abs/2603.18322
