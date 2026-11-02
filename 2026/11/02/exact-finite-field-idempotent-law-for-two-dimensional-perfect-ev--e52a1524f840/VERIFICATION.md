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
# Verification and reproducibility

The executable `verify.py` is self-contained Python 3. It performs an exact exhaustive census of \(Ax^{[2]}=x\) for every invertible matrix \(A\) over \(\mathbb F_q\), with \(q\) in \(\{2,3,4,5,7,8,9,11,16\}\). Finite extensions are implemented as explicit polynomial quotients; the code checks that every nonzero field element has a multiplicative inverse. The direct algebra count is compared against the closed probability law. Separately, the program uses the actual fiber sizes of projective squaring to calculate the second and third moments, comparing these with moments of the enumerated distributions.

The observed raw counts for \(N=0,1,2,3\) were:

| \(q\) | Raw counts | Total invertible matrices |
| --- | --- | ---: |
| \(2\) | `(2,3,0,1)` | 6 |
| \(3\) | `(16,20,8,4)` | 48 |
| \(4\) | `(60,90,0,30)` | 180 |
| \(5\) | `(160,208,64,48)` | 480 |
| \(7\) | `(672,900,216,228)` | 2016 |
| \(8\) | `(1176,1764,0,588)` | 3528 |
| \(9\) | `(1920,2624,512,704)` | 5760 |
| \(11\) | `(4400,6100,1000,1700)` | 13200 |
| \(16\) | `(20400,30600,0,10200)` | 61200 |

All nine checks passed and the checker printed `VERIFY_OK`. A matrix-by-matrix finite census is not an infinite proof; the universal theorem is supplied by the projective three-point-incidence argument in `RESULT.md`.

To replay from the directory containing the extracted files, run `python3 verify.py`. No packages beyond the Python standard library are required. Independent mathematical auditing has not been performed.
