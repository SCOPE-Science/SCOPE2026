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

The primary input is the published product system
\[
A'=\frac{B-2A}{3AB},
\qquad
B'=\frac{A-2B}{3AB}.
\]

With
\[
S=A+B,\qquad D=A-B,
\]
direct algebra gives
\[
S'=-\frac{S}{3AB},
\qquad
D'=-\frac{D}{AB}.
\]
The quotient rule therefore yields
\[
\frac{d}{dt}\left(\frac{D}{S^3}\right)=0.
\]

Writing
\[
D=cS^3
\]
gives
\[
A=\frac S2(1+cS^2),
\qquad
B=\frac S2(1-cS^2),
\]
and
\[
AB=\frac{S^2}{4}(1-c^2S^4).
\]
Consequently
\[
S'=-\frac{4}{3S(1-c^2S^4)}.
\]
Integrating this scalar equation yields the exact clock
\[
t=\frac38(S_0^2-S^2)-\frac{c^2}{8}(S_0^6-S^6).
\]

At \(S=0\),
\[
T=\frac38S_0^2-\frac18(A_0-B_0)^2
=\frac{A_0^2+4A_0B_0+B_0^2}{4}.
\]

For
\[
\delta=D/S=cS^2,
\]
the exact remaining-time identity is
\[
T-t=\frac{S^2}{8}(3-\delta^2).
\]
If \(c\ne0\), this is equivalently
\[
T-t=\frac{\delta(3-\delta^2)}{8c}.
\]

The checker verifies all of these identities symbolically. It also expands the inverse relation at extinction:
\[
S^2=\frac83(T-t)+O((T-t)^3),
\]
which gives the claimed first-order anisotropy decay.

The diagonal case \(A_0=B_0\) is checked separately and agrees exactly with
\[
A(t)^2=A_0^2-\frac23t,
\qquad
T=\frac32A_0^2.
\]

No numerical trajectory is used to establish an infinite-time or finite-extinction conclusion.
