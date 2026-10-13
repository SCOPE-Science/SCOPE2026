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

The symbolic check is the proof in `RESULT.md`: for \(e_m(d)=\lfloor m/d\rfloor+(m\bmod d)\), a step that keeps \(q=\lfloor m/d\rfloor\) fixed changes the exponent by exactly \(-q\). Therefore, below the maximum valuation, if no quotient changes then the full product strictly decreases. Only right endpoints of quotient plateaus can minimize.

The standalone `verify.py` uses Python integer arithmetic only. It enumerates every exponent vector of lengths one, two, and three with entries from \(1\) to \(25\), compares the full degree search with the quotient-breakpoint candidate search, verifies strict descent at each omitted interior degree, and checks the universal candidate-count bound. It also verifies the Reyssat exponent vector \((10,1,5)\).

Observed replay output:

`VERIFY_OK exhaustive_vectors=16275 max_exponent=25 reyssat_candidates=2,3,5,10 reyssat_minimizer=5`

The finite enumeration is not an exhaustive proof for arbitrary valuations. It is a reproducibility and boundary check for the exact symbolic argument. No external or independent validation was performed.
