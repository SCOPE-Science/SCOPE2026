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
# Verification record

The proof uses (i) the characteristic-\(p\) Newton identities for invertible \(1,\ldots,m\), (ii) a full-rank Vandermonde argument at singular candidates, (iii) an explicit triangular coordinate-translation identity at \(n=p\), and (iv) complete-intersection local multiplicity and Serre normality. These four steps establish the all-primes/all-admissible-integers claim, independently of numerical tests.

The included `verify.py` enumerates all rational projective points in seven **small selected** cases over the prime field and calculates the exact Jacobian rank in that field. The expected checks include no rational singular points below the prime, a unique rational singular point at the prime, and a rational singular witness above it. Its output ends with `VERIFY_OK`. It additionally checks an exact factorial count of a standard finite monomial set. This is only a finite sanity check; it cannot independently establish geometric smoothness, uniqueness of geometric singular points, or normality.

The projective cases have degree \(m!\) as an integer even if the characteristic divides \(m!\); in the stated range \(p>m\), it does not. The first boundary at \(p=m+1\) is a nonreduced zero-dimensional local complete intersection. Source inspection and comparison have residual historical-priority risk; the work has not been independently audited.
