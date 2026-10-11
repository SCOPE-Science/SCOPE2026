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
For orthogonal signals
\[
x=r(\cos\theta,\sin\theta),\qquad y=s(-\sin\theta,\cos\theta),
\]
the squared magnitude-measurement distance for the three unit Mercedes vectors expands exactly to
\[
D^2=\frac32(r^2+s^2)-rsL(2\theta),
\]
with
\[
L(t)=|\sin t|+|\sin(t+2\pi/3)|+|\sin(t+4\pi/3)|.
\]
Periodicity reduces the bound to \(0\le t\le\pi/3\), where
\[
L(t)=2\sin(t+\pi/3)\le2.
\]
Therefore
\[
D^2\ge\frac12(r^2+s^2)+(r-s)^2\ge\frac12(r^2+s^2).
\]
The imported orthogonal-pair reduction converts this exact bound into the global phaseless inequality with constant \(\sqrt2\).

Sharpness is checked directly at
\[
x=(1,1)/\sqrt2,\qquad y=(-1,1)/\sqrt2.
\]
The quotient signal distance is \(\sqrt2\), while the three absolute coefficient differences are \(0,1/\sqrt2,1/\sqrt2\), whose Euclidean norm is \(1\). Hence the ratio is exactly \(\sqrt2\).

No numerical search, finite enumeration, or unproved certificate is used in the proof. The only external theorem needed for globality is the published orthogonal-pair reduction for phase-retrieval stability.

Scope limit: this verifies the real, unit-norm Mercedes frame under Euclidean norms. It does not verify an analogous complex statement or an optimum over all three-vector frames.
