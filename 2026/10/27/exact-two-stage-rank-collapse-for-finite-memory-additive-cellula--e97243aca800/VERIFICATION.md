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

The reproducibility file `verify.py` implements the sitewise \(p\)-neighbor shift sum, constructs the \(k\)-layer companion map directly, and performs modular Gaussian elimination on every power through the predicted nilpotency index. It asserts equality with the theoretical rank formula at each power, rather than checking only the final zero matrix. Running `python verify.py` produces the recorded `verification_output.txt`; 17 tested triples pass and the \((p,L,k)=(3,9,2)\) illustration produces Jordan sizes \((10,8)\). No symbolic numerical approximation is used in these checks. The general result rests on the group-algebra and Jordan-kernel proof in `RESULT.md`; the finite test suite is not an exhaustive certificate for all primes and memory orders.

The source-level comparison directly inspected the complete four-page Endo (2026) article. The relevant general Guan–He (1986) full text was inaccessible; only its publisher abstract was available. Accordingly, priority beyond the inspected literature requires further verification. Independent auditing has not occurred.
