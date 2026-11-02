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
# Reproducibility and verification

`python verify.py` (Python 3 with the widely available `mpmath` package) evaluates the exact critical constants at 70-digit precision, solves the midpoint/difference scalar equation by bisection, checks the two-cycle identities at nine parameter values, samples the proved no-root regions, and checks the square-root and return-multiplier expansions. The program passed 540 high-precision assertions when executed from the actual embedded source.

The key exhaustive analytical certificate is the signed derivative
\[
F_d=-(1+\pi b\cos(\pi d)+2rm)m'-\pi\sin(\pi m)\sin(\pi d)+2rd
<-(\pi\sqrt3-2)d<0
\]
for \(0<d<d_0\) and \(0\le r\le r_*<1\), together with the exact endpoint signs and strict negativity for \(r>r_*\). The code illustrates these results but does not formally verify a continuum. The local Taylor and Floquet asymptotics are proved in `RESULT.md`; reported decimal values are approximations, not theorem premises.

Direct complete-publisher-document access was unavailable, despite indexed inspection of the relevant mathematical sections. Independent audit has not been performed.
