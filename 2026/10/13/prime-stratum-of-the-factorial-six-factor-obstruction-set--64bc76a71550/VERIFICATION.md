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

The proof separates an exact finite calculation from an infinite analytic step.

`verify_prime_R.py` computes factorial squarefree parts from Legendre valuations and checks all \(38\) cases \(12\le c\le49\). It also checks \(s(11!)=77\), \(s(12!)=231\), and the five explicit counterexamples for primes below \(13\). Finally it stress-tests every prime up to \(401\) and all \(c\le500\). Expected replay:

`VERIFY_OK finite_tail=38 small_prime_witnesses=5 prime_stress=79 c_max=500 threshold_11_12=77,231`

The infinite tail is not inferred from this finite experiment. For \(c\ge50\), Nagura's theorem is applied to \((c+1)/2\), \(2c/3\), and \(5c/6\), producing three disjoint primes of exact factorial valuation one. Their product is at least \(5c^3/18>c^2\). The prime classification then follows algebraically by toggling the \(p\)-parity in the squarefree part of \(pc!\).

The critical external input is Nagura's published prime-interval theorem. Its statement was cross-checked against an open-access later paper that explicitly records the interval \([x,6x/5)\) for \(x\ge25\).
