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

Run `python checker.py` using Python 3 with the standard library. The generated `checker_output.txt` is the actual standard output of the checker executed against this package's source code.

The checker evaluates exact central-binomial expressions across ten degrees, reproduces the all-degree maximum at degree one in these test cases, verifies 30 nonzero equatorial associated-Legendre identities, and compares an independent Simpson quadrature of the polarization cross integral through degree eight. The recorded maximum discrepancies are \(5.551\times10^{-17}\) and \(1.196\times10^{-13}\) respectively.

Exact checks through ten degrees do not prove a universal result. The proof relies on the explicitly written hemisphere boundary identity, parity formula, strictly decreasing azimuthal product ratios, and strictly decreasing degree ratios. No computer-assisted infinite certification or independent audit is claimed.
