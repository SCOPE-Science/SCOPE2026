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

The bundled `verify.py` uses only exact rational arithmetic. It checks the following consequences of the printed moment system and Figure 5 labels:

1. With \(r=113/100\), the positive-variance feasibility endpoint is \(a=1-1/r=13/113\).
2. The positive-term upper bound for the quartic part is
\[
2r^3a^4+3r(r^2-1)a^2=\frac{292201}{22600000}.
\]
3. The printed noise level gives
\[
rv=\frac{226}{15625},\qquad
rv-\frac{292201}{22600000}=\frac{173427}{113000000}>0.
\]
Hence the quartic equilibrium equation cannot vanish anywhere in the biologically feasible interval.
4. At the rounded reported point \((\mu,s)=(33/100,3/5000)\), the first moment update is \(49833/200000\), giving residual \(-16167/200000\neq0\).

Running `python verify.py` returns `VERIFY_OK` when all exact assertions hold.

Limits: this verifies the printed equations and labels only. It does not reconstruct unavailable simulation code or infer an intended alternative parameter pair.
