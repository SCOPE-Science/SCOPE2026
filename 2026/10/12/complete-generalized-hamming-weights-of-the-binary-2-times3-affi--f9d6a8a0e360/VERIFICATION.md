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

# Verification details
The self-contained `artifacts/verify.cpp` enumerates all 1,024 binary coefficient masks and checks 1,024 distinct 64-coordinate evaluation vectors. It then generates every unique binary reduced-row-echelon basis for each subspace dimension one through ten and verifies the following computed minima and number of attaining subspaces:

`r = 1..10`:
`minimum = [24,36,42,48,54,56,60,62,63,64]`
`attainers = [112,448,64,28,1120,24,1456,2016,64,1]`
`subspace totals = [1023,174251,6347715,53743987,109221651,53743987,6347715,174251,1023,1]`

The stage totals equal the corresponding Gaussian binomial coefficients. The two middle-rank lower bounds are exhaustive over 53,743,987 and 109,221,651 subspaces, respectively, not extrapolations from test cases. A successful complete execution prints `VERIFY_OK`.

Reproduce with `g++ -O3 -std=c++17 artifacts/verify.cpp -o verify && ./verify`. The full run was performed using the included source. No external software certificate, independent audit or theorem prover is claimed. This certificate covers only this finite code; it does not establish a formula for all affine Grassmann codes.
