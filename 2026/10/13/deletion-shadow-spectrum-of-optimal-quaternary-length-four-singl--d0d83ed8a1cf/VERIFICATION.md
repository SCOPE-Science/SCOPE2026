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

Install the versions in `requirements.txt` and run `python verify_profiles.py`.

The verifier constructs every quaternary length-four word and every distinct one-deletion shadow from first principles. It formulates the exact binary set-packing model on the \(64\) received length-three words, proves the optimum cardinality \(24\), and then fixes that cardinality while optimizing total shadow coverage. It obtains exact integer optima \(60\) and \(64\).

Separate feasibility models for coverage \(60\) through \(64\) establish that only \(60\), \(62\), and \(64\) are possible. The verifier then tests every integer tuple \( (n_1,n_2,n_3,n_4) \) with 24 codewords and coverage in the proved interval by adding exact group-cardinality constraints. The feasible tuples are exactly the six stated in the finding.

`witnesses.json` contains one code for every surviving profile. These six witnesses are checked by direct set operations, independent of the optimizer-selected incumbent. The historical quaternary code printed as Table 2 by Kim, Lee, and Oh is also reconstructed and checked to have profile \( (4,12,0,8) \) and coverage \(60\).

The optimization uses binary integrality with SciPy 1.17.0 and HiGHS and requests zero relative MIP gap. It is a finite computer-assisted verification, not an exact-arithmetic formal proof certificate.

Expected output is recorded byte-for-byte in `verification_output.txt`.
