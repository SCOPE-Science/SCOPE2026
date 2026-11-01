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

# Reproducibility

The file `check_cone_fourier.py` uses only the Python standard library. Running `python3 check_cone_fourier.py` exactly enumerates all characters and all quadratic-cone points for \(p=3\) and \(p=5\), checks each character sum by divisibility of an integer polynomial by the prime-square cyclotomic polynomial, verifies all spectral multiplicities and the trace identity, and prints `EXACT_QUADRATIC_CONE_P2_OK` twice.

The full theorem for every odd prime follows from exact Gauss sums, Ramanujan sums, and the smooth isotropic-cone lifting argument in `RESULT.md`. A finite computation cannot prove the universal statement. No independent audit or outside mathematical validation has been performed.
