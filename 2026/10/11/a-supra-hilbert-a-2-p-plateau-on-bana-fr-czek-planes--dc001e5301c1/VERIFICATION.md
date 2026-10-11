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

Let
\[
a=\lambda^{-1},
\qquad
b=\sqrt{1-\lambda^{-2}},
\qquad
\kappa=1-2\lambda^{-2}.
\]
For \(\lambda\ge\sqrt2\), \(\kappa\ge0\).

The exact mixed-branch support maximum is
\[
1+\tau+
\sqrt{a^2(1-\tau)^2+b^2(1+\tau)^2}
=
1+\tau+\sqrt{1+2\kappa\tau+\tau^2}.
\]
The support condition is global because
\[
(\lambda^2-1)(\lambda-t)^2-(1-t^2)
=
\lambda^2-2+(-\lambda^2+\lambda t+1)^2\ge0
\]
for every \(t\in[-1,1]\), and the opposite sign follows by replacing \(t\) with \(-t\).

The same-branch bounds are
\[
2\sqrt{1+\tau^2}
\]
for the Euclidean branch and \(2\) for the strip branch. Since
\[
\sqrt{1+2\kappa\tau+\tau^2}\ge\sqrt{1+\tau^2}
\]
and
\[
1+\tau\ge\sqrt{1+\tau^2},
\]
the mixed branch dominates.

With
\[
G_\lambda(\tau)=
\frac{1+\tau+\sqrt{1+2\kappa\tau+\tau^2}}2,
\]
the \(p=2\) logarithmic derivative satisfies
\[
\left(
\frac{G_\lambda'}{G_\lambda}
-\frac{\tau}{1+\tau^2}
\right)
G_\lambda\sqrt{1+2\kappa\tau+\tau^2}(1+\tau^2)
=
\frac{(1-\tau)\left(\kappa(1+\tau)+\sqrt{1+2\kappa\tau+\tau^2}\right)}2
\ge0.
\]
For every finite \(p\ge2\),
\[
\frac{\tau^{p-1}}{1+\tau^p}
\le
\frac{\tau}{1+\tau^2},
\]
so the normalized generalized-Baronti profile is nondecreasing. At \(\tau=1\),
\[
G_\lambda(1)=1+\sqrt{1-\lambda^{-2}}.
\]

The pair
\[
x=(a,b),
\qquad
y=(-a,b)
\]
has \(N_\lambda(x)=N_\lambda(y)=1\) and attains every displayed mixed-branch profile value. No numerical search or finite enumeration establishes the result.
