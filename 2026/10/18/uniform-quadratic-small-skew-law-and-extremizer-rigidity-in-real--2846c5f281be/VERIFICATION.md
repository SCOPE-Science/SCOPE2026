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

# Proof and reproducibility checks

The analysis requires only the scalar fourth-root Taylor theorem, Hölder, and the power-mean comparison. Reproduce it as follows: expand \(\|x+\tau y\|_4^4\) and \(\|\tau x-y\|_4^4\) for normalized real functions; the coefficients must be \((1,4C,6D,4E,1)\) and \((1,-4E,6D,-4C,1)\). Squaring \(R=x^2-y^2+\sqrt2xy\) produces \(\int(x^4+y^4)+2\sqrt2F\), since the \(x^2y^2\) terms cancel. Using \(C=-E=-1/(2\sqrt2)\), \(D=1/2\), the common transformed fourth power is \(1-\sqrt2\tau+3\tau^2+\sqrt2\tau^3+\tau^4\). Its positive fourth root has expansion \(1-\tau/(2\sqrt2)+9\tau^2/16+O(\tau^3)\).

To reproduce the sharp pair choose any disjoint normalized real \(L_4\) functions \(f,g\), let \(a^2=(\sqrt3+1)/(2\sqrt2)\) and \(b^2=(\sqrt3-1)/(2\sqrt2)\), and set \(x=af+bg\), \(y=-bf+ag\). The exact square identity gives all first-variation equality cases and the proof's full lower bound. The estimate \(|B-9/16|\le4\|R\|_2\) is obtained using the two inner products displayed in the proof; inserting it *before* optimizing the defect gives the stated near-minimizer rigidity.

Low-dimensional numerical tests of the infimum and the coefficients were performed as nonproof diagnostics. There is no external certificate, formal proof, or independent audit; the complete dimension-free proof is in RESULT.md.
