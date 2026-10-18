---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

PASS: For k syntactically distinct operands of modal subformulas, collecting a distinguished root and iteratively selecting a symmetric-difference witness when two positive operand sets have equal traces costs at most k-1 additions. Repeating for negative operand sets costs at most another k-1, because traces already separated cannot merge. For k>0 there are ≤2k−1 retained worlds; for k=0 one root suffices. Independent plus/minus atomic sets and arbitrary negative truth of nonmodal composites may be restricted; positive Boolean operations commute with restriction, and the four unrestricted extensional modal neighborhood memberships can be reassigned consistently whenever operand traces coincide. Structural induction preserves both signs for all F at retained worlds. The 2k−1 bound is genuinely sharp for the narrower simultaneous signed trace-separation task via disjoint singleton positive and negative operand supports, NOT claimed sharp for all equivalent model sizes. A polynomial countermodel certificate guesses two signed truth columns per F formula on ≤2k−1 worlds, checks positive Boolean identities and equal-operand-column/equal-modal-column coherence separately for each modality/sign, and reconstructs a model; tautology reduces via classical ¬H translated as T(H)→f and final disjunct f, giving coNP-hardness. The proof is arbitrary-world and arbitrary finite F, finite scripts only sanity checks. One concern: numerical random test logs alone prove nothing; assessment is grounded in the signed trace lemma, consistency induction and explicit hardness construction.

## originality

PASS

PASS best-of-knowledge: The primary Vaz Silva–Skurt 2026 CLoN paper specifies the two signs and four independently chosen neighborhood membership maps and proves semantic/correspondence properties, but did not state this explicit signed-trace bound or certificate complexity in inspected material. Dalmonte–Mazzullo (2023) proves coNP for fusions of *classical negation* non-normal modal systems via hypersequents; the complexity class by itself is prior, and those semantics do not automatically enforce preservation of independently interpreted rejection sets. Existing general neighborhood filtration arguments may potentially imply the witness construction abstractly and remain a stated risk. The novel credited object is the explicit sharp-as-trace bound and finite certificate for the exact weak-negation four-neighborhood clauses.

## value

PASS

PASS: The full signed-truth-preserving finite trace lemma is a structural small-model theorem on a naturally arising weak-negation modal semantics, with a linear bound in distinct operands rather than the number of truth valuations. An explicit NP-size countermodel certificate gives coNP-complete finite-premise local consequence and separates extensional four-neighborhood reasoning from stronger interacting models. The 2k−1 optimum is only for trace separation, not the minimum model size, a meaningful distinction stated in the claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
