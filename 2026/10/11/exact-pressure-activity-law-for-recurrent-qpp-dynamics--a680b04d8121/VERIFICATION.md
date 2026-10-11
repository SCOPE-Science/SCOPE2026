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

The bundled `verify.py` uses exact symbolic differentiation to reconstruct
\[
L\!\left(\frac{y^2}{2}\right)=xy,
\]
\[
L(xy)=x^2+y^2(z-1)-\delta xy,
\]
\[
Lz=\eta(h-z-y^2z),
\]
and
\[
L(\log z)=\eta\left(\frac hz-1-y^2\right).
\]
It also verifies the exact algebraic identity
\[
\frac1z-\frac1Z+\frac{z-Z}{Z^2}=\frac{(z-Z)^2}{zZ^2},
\]
which is the only extra step in the fluctuation decomposition. Running the packaged script produces the included `VERIFY_OUTPUT.txt` ending in `VERIFY_OK`.

The invariant-measure proof is analytic and not finite enumeration. Compact support inside \(z>0\) is essential for the logarithmic observable. The zero-activity rigidity argument uses invariance of the zero set \(x=0\) and the remaining scalar pressure dynamics; the checker does not replace that dynamical argument.

No statement about existence of a periodic orbit, chaotic attractor, or invariant measure at a particular parameter vector is verified here. No independent audit has been performed.
