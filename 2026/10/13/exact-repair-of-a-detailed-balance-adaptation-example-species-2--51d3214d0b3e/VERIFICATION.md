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
The reaction vectors are \((-1,1,1)^\top\) and \((1,0,-1)^\top\). Solving the two orthogonality equations gives the one-dimensional conservation-law space \(\operatorname{span}\{(1,0,1)^\top\}\).

For a fixed positive signal \(s\), direct substitution verifies the unique positive equilibrium
\[
N_2=\frac1{cr}=e^{-E_2},\qquad N_3=rs=e^{E_1-E_3}s.
\]
Thus the species-2 equilibrium is signal independent, while species 3 is not when the signal level changes.

For a time-dependent admissible signal, the proof uses the exact identity
\[
\frac{d}{dt}\left[x_*h(X)+ru h(Y)\right]
=-au(XY-1)\log(XY)-bru(Y-1)\log Y+r\dot u(1-Y),
\]
with \(h(z)=z\log z-z+1\). The last term is absolutely integrable under the assumed exponentially decaying logarithmic signal rate; boundedness and eventual positivity make the two dissipation terms uniformly continuous, so their integrability forces them to zero. This yields \(Y\to1\) and \(X\to1\).

At the detailed-balance initial state, the first derivatives vanish. Since \(u(t)-u(0)\sim t\), \(u'(0)=1\), and differentiation gives \(n_2''(0)=K_1>0\). The bundled `verify.py` checks the stoichiometric and steady-state algebra using exact rational arithmetic. It is a consistency check, not a numerical proof of the infinite-time limit.
