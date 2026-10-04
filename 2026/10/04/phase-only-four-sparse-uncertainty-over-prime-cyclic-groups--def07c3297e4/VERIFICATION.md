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
The universal theorem is proved analytically. The decisive checks are:

1. At a Fourier zero, four unit summands add to zero. The polynomial with those four roots has vanishing first and third elementary symmetric sums, hence is even, so the summands split into antipodal pairs.
2. On \(\mathbb Z_p\) with prime \(p\), the same antipodal pairing cannot recur at two distinct frequencies.
3. Three distinct zero frequencies would force the three different perfect matchings; comparing coefficient ratios would make \(-1\) a \(p\)-th root of unity, impossible for odd \(p\).
4. Two distinct zero frequencies force the support identity \(x_1+x_4=x_2+x_3\), and the explicit coefficients in `RESULT.md` realize two zeros whenever this identity holds.
5. The all-one coefficient vector realizes zero zeros, and a one-parameter pair-cancellation family realizes exactly one zero after avoiding finitely many phases.

The script `artifacts/verify.py` evaluates the discrete Fourier transform for every four-element support for all primes from \(5\) through \(31\). It checks the no-zero and one-zero witnesses and, on every centrally symmetric support, the explicit two-zero witness. These finite checks corroborate the formulas only; they are not an infinite proof.
