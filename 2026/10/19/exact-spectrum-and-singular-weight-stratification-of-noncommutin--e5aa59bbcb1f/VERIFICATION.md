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
# Computational verification and mathematical limits

Run `python verification/check.py` from a directory containing this standalone script. The implementation requires Python 3 standard library only. It reconstructs the exponent-\(p\) finite Heisenberg multiplication and the full regular left-convolution matrix for \(p=3,5,7\). Exact row reduction is carried out modulo primes \(\ell\equiv1\pmod{3p}\), with primitive \(p\)- and cube roots in the test field. It checks the independently calculated predicted nullity \(Z+(p-1)p\mathbf1_{\{F=0\}}\) at \(n=1\) against full-matrix rank in 15 cases. All completed runs returned `VERIFY_OK`.

The checker tests the one-Heisenberg-plane case in auxiliary finite characteristic; it does not prove the theorem over \(\mathbb C\), nor does it exhaust infinitely many primes, weights, or dimensions. The proof in `RESULT.md`, specifically the regular representation multiplicities, quantum-binomial trace argument, and recurrence for geometric kernel dimension, is required for unrestricted correctness.
