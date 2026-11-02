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

Execute `python3 check.py` using Python 3 standard library. The direct enumerator checks all 256 joint valuation outcomes for each of 16 assignments and compares probabilities with independent Bernoulli-sum convolutions. It verifies the ex-ante expected balance of \(7/10\), the exact assigned probabilities \(13144772641/25600000000\) and \(13170400347/25600000000\), the improvement \(12813853/12800000000\), and that only the proposed alternative and its agent swap maximize the four-good ex-post probability. A supplemental 125-case three-good grid check confirms the analytic singleton-maximizer theorem on that finite grid. The universal proof is the algebraic exchange identity and its global \([0,1]^3\) sign analysis; no finite enumeration is claimed to establish the continuum theorem. Verification does not establish bibliographic novelty or independent review.
