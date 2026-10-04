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

The determinant proof was replayed directly from the Fourier matrix. For a repeated restriction class, subtracting one repeated column from the other gives a column supported only at the extra point. Expansion along that column leaves a full \(m\times m\) Fourier matrix, whose absolute determinant is \(m^{m/2}\).

The accompanying `verify.py` constructs canonical basis partners for every \(2\le m\le24\) and every \(1\le k\le m-1\). It computes the determinant independently by complex Gaussian elimination and checks
\[
|\det T(E_m,B_k)|=
m^{m/2}|1-e^{2\pi i k/m}|.
\]
It also checks the parity-dependent maximizing value and evaluates the normalized determinant formula for large \(m\). The script prints `VERIFY_OK`.

Finite numerical replay is not used as proof of the universal statement; it is only a consistency check of the analytic derivation.
