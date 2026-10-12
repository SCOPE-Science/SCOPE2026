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

The exact seed laws are
\[
P_X=\frac35\delta_{-83/100}+\frac3{10}\delta_{123/100}+\frac1{10}\delta_{135/100},
\]
\[
P_Y=\frac3{20}\delta_{-9/5}+\frac{27}{50}\delta_{-2/5}+\frac14\delta_{9/10}+\frac3{50}\delta_5.
\]

The standalone script checks the seed with `fractions.Fraction`. It verifies the means and MADs, support-transition probabilities for the expectile equation, the piecewise formulas at deterministic rational points, and the sign certificates
\[
\operatorname{disc}(30074a^2-16688a+2643)=-39452984<0
\]
and
\[
6872(2/11)^2+8386(2/11)-1521=27939/121>0.
\]
It also verifies the exact standardized stop-loss values
\[
\widetilde S_X(4/5)=1/5,
\qquad
\widetilde S_Y(4/5)=73441/569900,
\]
with gap
\[
40539/569900>0.
\]

The analytic smoothing step is verified in the proof rather than by finite computation. Its ingredients are bounded Wasserstein convergence, strict monotone-root stability for expectiles, the endpoint extensions of the normalized \(s_2\)-profile, and continuity of MAD and stop-loss transforms.

Expected successful terminal line:
`VERIFY_OK breaks=1/104,2/11,210/859 sf_gap=40539/569900`.
