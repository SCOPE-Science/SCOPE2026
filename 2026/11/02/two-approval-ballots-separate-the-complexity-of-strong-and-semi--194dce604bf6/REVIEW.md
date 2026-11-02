# Scientific review: two-approval separation

## Correctness — PASS

For a cohesive candidate \(c\), its full supporter set generates the strongest relevant requirement. Under pair approvals, a two-element intersection \(I_c=\{c,d\}\) forces every approving ballot of \(c\) to equal \(\{c,d\}\). Consequently each requirement edge has a degree-one endpoint, the requirement graph is a star forest, and one component representative satisfies all of its candidate requirements. A committee of size \(k\) can satisfy requirements in at most \(k\) components, making the sum-of-largest-weights formula both an upper bound and constructively attainable. NP-hardness follows by mapping cubic-graph edges to pair-approval voters and vertices to candidates; under \(k\ge |V|/2\), every candidate is cohesive and SSJR holds exactly for vertex covers. Both promise restrictions and trivial-bound cases are handled explicitly. The included integer verifier passed exact enumeration of 67,028 bounded profiles, 4,822 groupwise committee comparisons, and cubic examples. General correctness rests on the proof, not extrapolation from finite checks.

## Originality — PASS, subject to independent assessment

Chingoma et al. (2026), arXiv:2609.29332, Definitions 4–8, Theorems 15, 20 and appendices, already provide the SJR/SSJR objective, unrestricted NP-hardness, and tractability for interval profiles. The exact two-approval star decomposition is not implied by their CI/VI restriction, because triangle approval ballots fall outside both domains. Their reduction does not establish the claimed all-candidates-cohesive, cubic-support, pair-ballot hardness promise. Aziz et al. (2017) provide the original axioms and unsatisfiability examples; Brill et al. (2022) analyze individual representation, a different strengthening. Cubic VERTEX COVER hardness is pre-existing and fully credited. Mathematical-record searches using several aliases and statement-level queries found no matching result in the returned hits, but this is not a proof of novelty. Residual priority risk: relevant earlier sparse-approval or graph-representation results might be unindexed or phrased differently.

## Value — PASS

The sharp one-to-two approval-arity boundary explains why two superficially similar one-cohesive-group representation requirements diverge computationally at the sparsest nontrivial ballot size. The exact weighted-star optimization gives both a constructive optimum and a feasibility test for SJR in a domain outside known interval tractability. The hardness persists in a natural three-supporter regular profile and therefore cannot be attributed to unbounded approval width or anomalously popular candidates. The result informs sparse committee-design models and complexity classifications without assuming a large empirical application or claiming stronger multi-level proportionality.

## Limits of the assessment

No proof of historical uniqueness is offered; unindexed earlier work remains possible. The integer experiments confirm bounded cases only. The theorem addresses SJR score optimization and SSJR existence, not the full SSJR optimization landscape or the stronger all-level variant of strong representation.

Self-review: passed. Independent audit: not yet performed.
