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

The proof is symbolic and unbounded. The finite program `verify_set_sigma.py` is only a regression check.

It enumerates all \(1\le A\le12\), all odd primes \(p\le2000\), and all exponent pairs \((a,b)\in[1,A]^2\). For every candidate it computes \(\sigma(2^a p^b)\), tests membership in \(Set(2^A p)\), and compares the exact fiber with the predicted singleton Mersenne criterion.

Observed output:

`VERIFY_OK cases=3624 A_max=12 p_max=2000 primes=302`

Representative nonempty fibers include \(Set(2^2\cdot3,\sigma)=\{6\}\), \(Set(2^3\cdot7,\sigma)=\{28\}\), and \(Set(2^5\cdot31,\sigma)=\{496\}\).

The computation does not establish the theorem outside the tested range; that role is supplied by the factorization proof in RESULT.md.
