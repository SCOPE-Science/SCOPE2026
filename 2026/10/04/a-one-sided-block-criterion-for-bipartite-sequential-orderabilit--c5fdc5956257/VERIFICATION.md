---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

The mathematical proof was reconstructed directly from the definitions.

1. Fixing the order of the \(A\)-vertices fixes the sequence at every \(B\)-vertex, because simplicity permits at most one incident edge from each \(A\)-block.
2. At a vertex \(a\in A\) of degree \(d\), properness makes all incident colours distinct, so the \(d!\) internal block orders yield \(d!\) distinct sequences.
3. Its \(d\) neighbours forbid at most \(d\) sequences. The inequality \(d!>d\) holds for every \(d\ge3\).
4. Internal choices at different \(A\)-vertices do not alter any fixed \(B\)-sequence, so the local choices coexist in one global concatenated edge order.

The packaged `verify.py` was also replayed from the finalized payload. It exhaustively checks \(67,404\) proper edge-colourings over the stated finite regular bipartite strata and reproduces `verification_output.txt` exactly. These computations are finite regression tests only; they are not evidence for the universal quantifier beyond the deductive proof.

Scientific limits retained: multigraphs are not covered by the proof; improper colourings are not covered; one-sided degree \(2\) is not universally sufficient; nonbipartite regular degrees \(3,4,5\) remain outside the claim. Direct primary full-text access was unavailable during originality comparison and is recorded as a bibliographic residual risk.
