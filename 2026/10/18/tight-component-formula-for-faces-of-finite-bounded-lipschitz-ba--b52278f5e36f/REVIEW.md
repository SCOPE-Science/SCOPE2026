# Scientific review: finite bounded-Lipschitz faces

## Correctness — PASS
The statement separates nonconstant boundary points from interior points and the two constant endpoints. For nonconstant boundary functions, the sum norm is the finite maximum of independently indexed signed coordinate values plus oriented edge slopes. Its active inequalities are exactly the product of signed sup-norm anchors and tight-oriented edges. Common active-equality increments propagate as an affine rescaling of the function plus one constant per tight component. One free constant survives for each anchorless component; the common slope parameter survives precisely if no component contains both anchor signs. The resulting nullity is \(u+\varepsilon\), equal to minimal-face dimension. No infinite-sampling inference enters the proof. Exact rational rank computations reproduced the same dimension on 46,000 boundary configurations, including two distinct four-point examples from the motivating paper; the proof itself covers arbitrary real finite metrics.

## Originality — PASS
The closest direct source, Hille–Theewis (2023, Section 6; arXiv:2305.08500v1), gives necessary conditions and explicitly exhibits a non-extreme function satisfying their tested local conditions; it does not state the complete component formula. Their 2022 paper gives only a half-space / linear-programming method. The tight-graph connectivity characterization of Bredies–Chirinos Rodriguez–Naldi (arXiv:2304.14039v1) concerns pinned pure Lipschitz seminorm balls rather than the sum norm. Targeted semantic and bibliographic searches showed no equivalent finite BL sum-norm theorem in retrieved publications, and historical claim-level comparisons found no duplicate. Residual risk: a non-indexed earlier paper or an abstract active-facet statement that implicitly specializes to the same graph formula.

## Mathematical value — PASS
This closes a concrete missing sufficiency question for finite BL sum-norm extreme points, motivated directly by two counterexamples in the 2023 paper, and computes the dimension of *every* minimal face rather than merely testing vertices. The resulting quadratic-time connected-component criterion works for all finite metrics, including spaces with disconnected tight graphs, and is useful for reducing finite dual bounded-Lipschitz norm optimization to genuinely extreme potentials. It is not a restatement of an existing pure-Lipschitz connectivity theorem: the coupling of positive and negative anchors is essential.

## Scope and risks
No infinite-space extension, vector-valued generalization, or algorithm for enumerating all vertices is claimed. The exact-rational tests are finite checks only. All comparison sources cited in the scientific audit are read at the indicated levels, with the unresolved bibliographic risk noted. No independent scientific audit has occurred.

Self-review: passed. Independent audit: not yet performed.
