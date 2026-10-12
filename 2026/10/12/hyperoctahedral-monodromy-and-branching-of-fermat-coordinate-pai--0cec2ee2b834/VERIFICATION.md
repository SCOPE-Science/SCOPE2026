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

The theorem is proved symbolically by a cyclotomic critical-point parametrization, elementary polynomial monodromy, geometric irreducibility of the Fermat base-change fibers, and a wreath-product stabilizer computation. No finite calculation is treated as proof for all degrees.

Reproducible exact arithmetic: from a directory containing the embedded file `checks/verify.py`, run `python checks/verify.py`. It requires Python 3 and SymPy; it checks exactly each integer degree \(4\le d\le25\). Its verified outputs include the degree \(m-1\) and squarefreeness of the discriminant of \(p_d(U)-v\), regularity at \(v=2\), and the explicit degree count for \(p_d\). Success prints `VERIFY_OK`. The standalone program does not certify infinite degrees or independently establish the geometric monodromy theorem.

The relevant primary published texts are Miura--Taki, arXiv:2608.25445v1, and Takahashi, DOI:10.4171/RSMUP/135-3. The 24 Fermat-quartic point locations and the plane quintic dihedral case are prior results, not newly asserted independent classifications. No independent audit has been performed.
