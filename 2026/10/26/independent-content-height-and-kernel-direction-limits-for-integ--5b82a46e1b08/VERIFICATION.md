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
# Reproducible finite checks and analytic limits

Run `python3 verify.py` using the Python standard library. The script lists each finite cutoff and checks the exact integer identities, returning:

`VERIFY_OK direct_and_parameter_sets=19 max_T=50 sector_content_checks=175 alternate_content_counts=299 all_exact=PASS`

The checker reconstructs all nonzero \(2\times2\) square-zero integral matrices by direct enumeration in symmetric entry boxes for nineteen cutoffs up to \(50\), compares this with a distinct primitive-projective parametrization, and checks the totient count. For thirteen cutoffs it tests 175 content, radial-height, and central-slope-window counts by two independent arithmetic routes; for all cutoffs from \(1\) through \(299\), it checks agreement of the sum over primitive-line heights with a separate sum over scalar contents.

The limit theorem has infinitely many parameter values and is not established by this finite verifier. Its proof instead requires uniqueness of primitive decomposition, the elementary planar lattice discrepancy estimate, Möbius inversion, the harmonic sum, and an endpoint tightness argument. No external proof assistant, independent review, or infinite computation is claimed.
