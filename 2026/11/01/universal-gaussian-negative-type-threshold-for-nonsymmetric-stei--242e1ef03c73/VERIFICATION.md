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

# Reproducibility and verification

The independent example checker is the embedded file `check_steiner.py`, requiring Python, NumPy, and SciPy. Run `python check_steiner.py` after extracting the file. It constructs and verifies cyclic \(2\)-\((13,3,1)\), affine \(\operatorname{AG}(2,3)\), projective \(\operatorname{PG}(3,2)\) point–line and two complete pair designs. It compares distances independently computed by graph shortest paths to the proposed incidence-distance formula; checks exact integer incidence products; checks centered eigenvalue counts at \(p_*/2\), \(p_*\), and \(p_*+0.07\); and verifies the contrast expression and its sign. All five constructions passed in the reported execution. Floating-point tolerances are explicitly visible in the script.

**Analytic work needed beyond finite checks.** The proof computes all subspace sectors from the Steiner axioms, shows the critical block-kernel eigenvalue vanishes, controls the endpoint two-dimensional determinants, proves the contrast negative for every allowed parameter, and invokes strict lower-exponent negative type. The script does not establish the universal quantifiers or the absence of prior published equivalences.

**Limits.** There is no independent audit, formal proof certificate, numerical exhaustive verification over all Steiner designs, or asserted existence for arbitrary design parameters.
