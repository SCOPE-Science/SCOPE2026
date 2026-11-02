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
# Reproducible analytical checks

Run `python verify_halfturn.py` using Python 3 and SymPy. The script passes exact symbolic checks for the twist root identity, determinant-one one-step derivative, both return traces, identity return at a reversing collision, and the unique closed-form crossover for \(\varepsilon=1\). Direct numerical iterations check all available central half-turn cycles at four explicit parameter triples and evaluate their two-step derivative independently of the trace formula. The source's reported example \((a,\varepsilon,b)=(0.515,0.1,0.3259)\) is compared with \(b_c=0.325836900672316\ldots\).

Logical completeness rests on monotonicity of \(\omega\) on \((0,1)\), the exhaustive sign cases, exact return products, and monotonicity of the crossover function. Finite calculations cannot prove the infinite real-parameter theorem; these steps are proved in RESULT.md. This work does not verify general period-two dynamics outside the central half-turn class or nonlinear elliptic stability.
