---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

For Fibonacci words W_j=W_(j-1) W_(j-2) the near-commutation W_j W_(j-1) and W_(j-1) W_j agrees through the first F_(j+1)-2 positions and differs in the final two, by induction. The infinite Fibonacci word starts W_k W_(k-1) W_k, so comparison with shift F_k gives first mismatch at n=F_(k+1)-2 for all k>=4. This nonzero first mismatch has canonical Zeckendorf word length k-1. Taking an arbitrary s-state MSD DFAO for the shift, product with the 2-state last-digit Fibonacci DFAO and a 4-state valid Zeckendorf recognizer yields a <=8s-state DFA accepting exactly canonical first differences. Shortest accepted word length k-1 forces >=k distinct prefix states, so 8s>=k. The published O(log F_k)=O(k) MSD upper bound gives Theta(k). Independent morphic-word checks corroborated first disagreement for k=4..16, not an infinite proof.

## originality

PASS

Known Moradi–Popoli–Shallit–Vukusic theorem proves MSD upper bounds for all shifts, but no MSD lower bound along c=F_k; its exact LSD theorem uses the reverse input direction. A separate November 2 Resultary exact-k theorem concerns c=F_k-2, not c=F_k, and its Myhill–Nerode witnesses do not imply this shifted-family first disagreement. The present explicit infinite subfamily lower bound survives those implications.

## value

PASS

Asymptotically tight state-complexity lower bound on a natural infinite Fibonacci shift sequence addresses a motivated open gap between general upper constructions and lower limits. The exact near-commutation witness is independent of arbitrary small cases and could guide minimal automaton analysis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
