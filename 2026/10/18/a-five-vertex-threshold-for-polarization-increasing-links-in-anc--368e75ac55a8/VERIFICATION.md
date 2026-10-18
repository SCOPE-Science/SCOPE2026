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

# Verification record

The included `verify.py` is the complete executable exact-arithmetic certificate for this claim. Python 3 and SymPy 1.10+ are sufficient; run `python verify.py` in the same directory. The program constructs graphs directly from edge masks, canonically quotients graph relabelings, covers all nonedge insertions and all binary innate assignments using complement invariance, and tests nonpositive coefficients of the **cleared rational polarization difference**, not evaluations on an interval grid.

Expected count summary: connected unlabeled graph counts \(1,2,6\) for sizes \(2,3,4\); nontrivial decorated comparisons \(0,3,77\); nonzero nonpositive polynomial certificates \(58\), identically zero cases \(22\). The five-vertex path's matrix-inverse calculation yields
\[
\Delta(a)=-\frac{2a^3(a^4+4a^3-7a-3)}{(a^2+3a+1)^2(a^2+5a+3)^2};
\]
its exact rational test differences are \(\Delta(1)=2/405\) and \(\Delta(2)=-496/34969\). The verifier checks the number of positive roots of the quartic. It does not establish novelty or empirical validity, which remain separate issues.

Scientific limits: computations alone do not establish anything about graphs larger than the explicitly enumerated lower-bound range; the five-vertex witness and its one-root property follow independently from the symbolic identity. The classification is restricted to connected unweighted graphs, binary innate opinions and homogeneous positive anchoring. The prior-literature comparison is not independent validation.
