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

The proof was checked as an exact convex-geometric argument.

For every convex body \(K\) and center \(c\), the maximal centrally symmetric subset with that center is
\[
S(c)=K\cap(2c-K).
\]
For \(c_\lambda=\lambda c_0+(1-\lambda)c_1\),
\[
\lambda S(c_0)+(1-\lambda)S(c_1)\subseteq S(c_\lambda).
\]
Brunn–Minkowski therefore implies concavity of
\[
|S(c)|^{1/2}.
\]
For a regular polygon, averaging any center over its rotation orbit gives the polygon center while preserving the overlap area at each orbit point, so the centered overlap is globally optimal.

For odd \(n\), the \(n\) outward edge normals and their negatives form \(2n\) equally spaced normals. Thus the centered overlap is a regular \(2n\)-gon with unchanged inradius \(r\). Using
\[
|P_m|=m r^2\tan\!\left(\frac{\pi}{m}\right)
\]
for a regular \(m\)-gon with inradius \(r\) gives
\[
\frac{|P_n\cap(-P_n)|}{|P_n|}
=
\frac{2\tan(\pi/(2n))}{\tan(\pi/n)}
=
1-\tan^2\!\left(\frac{\pi}{2n}\right).
\]

A direct polygon-intersection check for \(n=3,5,7,9\) matched the formula to floating-point precision. The computation is only a sanity check and is not part of the proof.

The uniqueness statement uses the classical theorem that every convex body has a unique maximum-volume centrally symmetric kernel, as explicitly recalled in the inspected 1998 source. Independent audit has not been performed.
