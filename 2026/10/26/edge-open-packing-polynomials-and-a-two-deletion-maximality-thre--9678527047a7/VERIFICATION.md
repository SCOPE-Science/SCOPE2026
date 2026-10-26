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

# Reproducibility notes

Execute the standard-library-only script `verification/verify_eop_matching.py` with Python 3. The script independently reconstructs every graph edge, checks pairwise compatibility by testing graph edges distinct from both members of a candidate pair, enumerates every compatible subset, and computes inclusion-maximality against every excluded edge. The checked domain comprises all \(78\) triples with \(3\le p,q\le6\) and \(0\le t\le\min\{p,q\}\). It reports PASS for \(15{,}961\) eligible subsets (empty subsets included). These are finite boundary checks, not an exhaustive verification over all integers. The unrestricted theorem is proved in `RESULT.md`.

No external or independent audit has been performed. The primary source provides the definition and neighboring comparison results; mathematical priority remains subject to further literature review.
