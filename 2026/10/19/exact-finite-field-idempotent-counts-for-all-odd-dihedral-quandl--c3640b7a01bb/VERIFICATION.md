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

## Reproducibility
Run `python3 verify.py` with Python 3.8 or later and no external dependencies. The checker first determines \(d_r,H_r,h_r,s_r,a_r,\epsilon_r,N_r\) from elementary modular arithmetic and evaluates the formula. Separately, it enumerates all coefficient vectors in each of fourteen finite examples and directly evaluates \(u^2\) in the quandle algebra. The checker represents \(\mathbb F_4\) as \(\mathbb F_2[t]/(t^2+t+1)\).

The examples are \((3,2),(3,4),(3,5),(5,2),(5,3),(5,4),(5,7),(7,2),(7,3),(9,2),(9,5),(11,2),(13,2),(15,2)\). All fourteen comparisons passed; the output terminates with `VERIFY_OK`. Specific checks include counts \(12\) for \((5,2)\), \(80\) for \((9,2)\), \(68\) for \((11,2)\), and \(768\) for \((15,2)\).

## Limits
Exhaustive enumeration certifies only these finitely many algebra instances. The general result for all odd \(n\) and all prime powers \(q\) coprime to \(n\) is supported by the independent symbolic character-orbit and Galois-descent proof in `RESULT.md`. No external independent audit has been performed. The excluded modular case cannot be tested by the same Fourier argument.
