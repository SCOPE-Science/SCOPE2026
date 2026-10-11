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

Run `python gold_checker.py` with Python 3 and no third-party packages. The script constructs the four binary fields with sizes \(4,16,64,256\) from the displayed monic irreducible polynomials, verifies the multiplicative field property, checks all affine \(\mathbb F_4\)-lines and exact incidence ranks, and compares the direct convolution fiber energies with the sharp inequality on deterministic random complex inputs. It checks explicit quadratic-trace equality cases in each field and exhaustively enumerates signs at \(q=4,16\). The observed code nullities \(3,7,13,21\) and small-field admissible sign counts \(8,128\) agree with the theorem. There are \(66\) direct energy/optimizer trials. The all-dimension proof is symbolic and relies on the stated derivative identity, nonnegativity of Cauchy gaps, and the induction for the affine-line parity code; finite checks alone are not a proof for arbitrary \(m\).
