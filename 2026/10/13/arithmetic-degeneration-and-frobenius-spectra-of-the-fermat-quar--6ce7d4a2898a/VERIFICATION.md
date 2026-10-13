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

The standalone \(\texttt{verify.py}\) uses exact integer arithmetic in \(\mathbb Z[T]/(T^4+1)\). Its complete determinant enumeration covers \(\binom{28}{3}=3276\) triples and its projective pair census covers \(\binom{28}{2}=378\) pairs. It checks the full determinant-norm histogram, multiplicity-class partition, and four cyclotomic Frobenius fixed-point profiles. In finite characteristic it constructs \(\mathbb F_{p^2}\) as a quadratic extension and checks the complete geometric and rational incidence spectra at eleven explicitly listed primes, including all three exceptional primes. A replay prints \(\texttt{VERIFY\_OK}\).

The all-prime proof is not a mere sample experiment: nonzero determinants have exact cyclotomic norms divisible only by \(2,3,5,17\), so no new concurrency can arise for any other odd prime. A separate exact computation handles each remaining exceptional odd prime. The mathematical premises are the standard \(28\)-bitangent count for a smooth genus-three quartic in characteristic not \(2\) and the explicit line restrictions. Residual limitation: no externally independent audit of the theorem, implementation, or originality has occurred.
