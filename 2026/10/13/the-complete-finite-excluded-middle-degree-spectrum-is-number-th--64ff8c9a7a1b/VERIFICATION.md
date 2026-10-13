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

The bundled script `verify_complete_excluded_middle_spectrum.py` uses only exact integer and rational arithmetic. It performs the following checks:

1. Enumerates all labelled posets on one through five points, recovering the known counts \(1,3,19,219,4231\), for \(4{,}473\) posets total.
2. Constructs each upset Heyting algebra and computes \(\neg U\) exactly as the complement of the down-closure of \(U\).
3. Checks that the excluded-middle elements are exactly \(2^c\), where \(c\) is the number of comparability components of the dual poset.
4. Checks that the algebra size and excluded-middle degree factor across those components as \(|H|=\prod_i n_i\) and \(d_{\mathrm{EM}}(H)=\prod_i 2/n_i\).
5. Checks the reduced-fraction criterion for every enumerated algebra.
6. Checks the equivalence between the product description and arithmetic criterion over all tuples with one through four factors and \(2\le n_i\le12\), plus constructive converse cases through denominator \(150\).
7. Checks explicit member and nonmember regression values.

Expected terminal line:

`VERIFY_OK 89093 exact assertions; 4473 labelled posets checked`

This is a finite replay, not a substitute for the general proof. Independent audit has not been performed.
