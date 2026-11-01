---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Bu et al. Theorem 5.1 gives common-two-value existence with ex-post EFX+fPO. For the stated three-level 3×4 matrix, any EFX allocation has nonempty bundles and pattern (2,1,1); evaluating 36 pair/singleton configurations yields exactly 14 EFX, of which exactly five survive integral PO against all 81 complete allocations. Their ex-ante envy inequalities have surpluses (0,0,3,−1,−1), (1,1,−2,−1,−1), (−3,−3,5,3,3). The combination 3d13+d32=−y forces y=0; d12=−z then z=0; d32=−3x forces x=0, contradicting x+y+z=1. Independent enumeration reconstructed the 81/14/5 counts and exact certificate.

## originality

PASS

Bu et al. prove universal ex-ante EF with ex-post EFX+fractional PO for common bi-valued values. Aziz already establishes arbitrary-value 3-agent/4-good impossibility, but the inspected witness has five distinct levels and does not imply failure with just three. The precise shared singleton-value alphabet cutoff three is a genuine additional boundary; original broader impossibility is credited.

## value

PASS

Determining the sharp shared singleton-value alphabet boundary between universal best-of-both-worlds existence and failure is a natural parameter question. The new exact three-level witness and compact impossibility certificate sharpen a previously known unrestricted impossibility theorem, without claiming the general no-lottery phenomenon as new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
