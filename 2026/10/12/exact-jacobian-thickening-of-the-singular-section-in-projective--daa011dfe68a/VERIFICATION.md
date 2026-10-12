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
# Verification and limitations
The file `check_veronese_fitting.py` was executed with SymPy and returned `VERONESE_FITTING_CHECK_OK` for \(d=3,4,5,6\), confirming the explicit lower-triangular minors \(z_0^{d-1}\), the equations' vanishing in the Veronese algebra, and lengths \(5,15,34,65\). In the symbolic proof, for every integer \(d\ge3\), Fitting minors have degree at least \(d-1\), while an explicit minor gives \(z_0^{d-1}\). Characteristic-zero polarization implies all degree \(d-1\) Veronese elements occur. The product-chart Fitting identity and graded Hilbert-function calculation complete the general proof. Finite checks do not establish a theorem for all degrees; that implication comes only from the written argument. The cited projective \(K_m\)-regularity theorem is assumed from Satriano--Shen. Earlier implicit coverage of the local Fitting-power identity remains a literature risk.
