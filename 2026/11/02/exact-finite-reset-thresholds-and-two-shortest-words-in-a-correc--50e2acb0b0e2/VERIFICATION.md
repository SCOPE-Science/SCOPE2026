---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Exact claim is restricted to integers 3<=p<=15 for the corrected transition tables. The finite power automaton BFS layers from the full state set exhaust every reachable subset before any singleton; its shortest-path counts distinguish letter labels and count every shortest reset word. A distinct inverse-image BFS uses reversed subset transitions. The two explicit words target q_2 with length 3p^2+4p-1. Reconstructed state tables and independent forward BFS for p=3..9 returned precisely the reported minimum length, count two, and subset counts (199,597,1587,3951,9454,21998,50157). The source forward and reverse programs and witness code were inspected; much larger p=10..15 exhaustive outputs were not independently rerun. This is a finite exact enumeration, not an all-p lower-bound proof.

## originality

PASS

Wang (arXiv:2610.07044v1) provides the corrected automata, a construction establishing rt(A_p)<=3p^2+4p-1, and a different specified-state collision threshold, but the inspected sections do not prove the global reset threshold equals that upper bound nor enumerate shortest words. The assessed two-word finite-range exact census is not implied by Wang or Szykuła; related Resultary shortest-word enumerators concern other transition systems. Historical priority remains best-of-knowledge.

## value

PASS

The corrected Figure 3 family is a concrete synchronizing-automata threshold example with a published global upper bound and an open exact sharpness issue. Exhaustive exact sharpness for thirteen consecutive parameters plus the complete surprising two-word minimizer classification gives a meaningful, reproducible finite cutoff and distinguishes global reset length from pair-compression claims. It does not masquerade as a solution for all p.

The dated certificate retains the supplied scientific assessment, sources and limitations.
