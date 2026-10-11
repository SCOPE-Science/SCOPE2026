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

The primary source defines the sharp radius by
\[
p\frac{1-R^m}{1+R^m}
=
\frac{2R^{2k}}{1-R^{2k}}.
\]

Set
\[
R=e^{-s/k},
\qquad
\lambda=m/k.
\]
Then the equation becomes exactly
\[
p\tanh(\lambda s/2)=\frac{2}{e^{2s}-1}.
\]
The first side is strictly increasing in \(s\) and the second strictly decreasing, so the positive solution is unique.

For \(\lambda\to\infty\), monotonicity gives a positive limit and direct passage to the equation yields
\[
s_p(\lambda)\to
\frac12\log(1+2/p).
\]

For \(\lambda\downarrow0\), the equation forces
\[
s_p(\lambda)\to\infty
\]
and then
\[
\lambda s_p(\lambda)\to0.
\]
Therefore
\[
p\lambda s/2
\sim
2e^{-2s},
\]
which gives
\[
(2s)e^{2s}\sim\frac{8}{p\lambda}
\]
and hence
\[
s_p(\lambda)\sim
\frac12W\!\left(\frac{8}{p\lambda}\right).
\]

For \(\lambda=2\), writing
\[
y=e^{-2s}=R^{2k}
\]
gives
\[
p(1-y)^2=2y(1+y),
\]
whose unique solution in \((0,1)\) is
\[
y=\frac{p}{p+1+\sqrt{4p+1}}.
\]

Representative bisection checks of the original and transformed equations agreed to numerical precision. These checks are not part of the proof.
