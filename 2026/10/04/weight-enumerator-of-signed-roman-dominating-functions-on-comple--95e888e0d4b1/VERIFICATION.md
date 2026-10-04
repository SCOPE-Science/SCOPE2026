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

The proof is symbolic: for each part \(V_i\), the literal signed Roman closed-neighborhood condition reduces to \(W-\sigma_i+\mu_i\ge1\), and a label \(-1\) in that part has a required label \(2\) neighbor exactly when \(C-c_i\ge1\). The multinomial coefficient counts the labelings realizing each valid part profile.

The packaged script `artifacts/verify.py` independently enumerates every nondecreasing complete-multipartite profile through order \(9\), every labeling by \(\{-1,1,2\}\), and every weight coefficient. It compares a literal graph-neighborhood implementation against the profile criterion and compares brute-force weight counts against the multinomial aggregate.

Replay result:

`VERIFY_OK profiles=87 labelings=748341 valid_functions=489054 criterion_checks=748341 coefficient_checks=1215 max_order=9`

The finite check does not certify arbitrary order and is not used in place of the proof. The complete-multipartite scalar domination number from earlier literature is not re-certified as a novel result here.
