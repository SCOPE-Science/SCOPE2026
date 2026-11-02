# Scientific review: integral incidence degeneration of the Cefalù Kummer configuration

## Correctness — PASS

The theorem is an exact equality of finite schemes over the full base of integers. Each four-point marked component is the free rank-four group ring of two order-two sign coordinates. On each of the twelve ordered cross-component pairs, incidence eliminates one independent sign character, leaving a rank-eight free group ring. On each of the four diagonal pairs, the independent sign products satisfy \(1+r+s=0\) and \(r^2=s^2=1\), which force \(3=0\), \(r=s=1\), leaving a length-four group ring over \(\mathbb F_3\). The disjointness of coordinate components rules out missing overlap contributions. The characteristic-two local algebras and exceptional square-quadric reductions follow from these same universal presentations. The standalone verifier confirms the coefficients, combinatorial counts, and decisive integer determinant; it is not substituted for the algebraic proof.

## Originality — PASS, with residual risk

Catanese, arXiv:2101.10501, establishes the polynomial, sixteen generic nodes/tropes, their classical \((16_6)\) incidences, and the square reductions at the primes two and three. Those are specifically not claimed as new. Relevant full-text work of Dolgachev (2024, DOI 10.1112/blms.13033) and Kondō–Schröer (arXiv:1912.12015) concerns different characteristic-two Kummer models and does not calculate the stated marked incidence closure. Targeted semantic research-record searches compared the same scheme/parameter statement to the closest recovered IDs. The integral decomposition, characteristic-three vertical components, and characteristic-two local thickness were not found stated or implied in inspected primary materials. Priority in unindexed literature remains uncertain.

## Mathematical value — PASS

The full arithmetic incidence scheme of the distinguished \((16_6)\) configuration is a motivated complete invariant. It separates 96 horizontal incidences from sixteen genuinely characteristic-three incidences and retains length-eight inseparable incidence structure where reduced characteristic-two points coalesce. It provides an exact geometric boundary for one natural integral model, rather than a routine count or an unsupported global Kummer generalization.

## Scope, reproducibility, and limitations

The proof concerns marked schematic closures of the original sixteen points and sixteen polar planes, not the entire singular/trope schemes of the nonreduced exceptional quartics. Exact ring isomorphisms supply the infinite-base proof; `verify_incidence.py` supports the finite computations. Results are self-reviewed but have not received independent audit.

Self-review: passed. Independent audit: not yet performed.
