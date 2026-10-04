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

The critical reduction is exact:
\[
1-a_1u=a_1(b-u)\quad\text{when}\quad b=b_1=1/a_1,
\]
so the prey drift is a negative square term plus \(-uv\). With \(L=u+v+w/a_3\), direct substitution cancels \(uv\) and \(vw\) and leaves three nonpositive terms. This identifies the full zero-derivative set as \(\{E_0,E_b\}\).

A standalone checker uses exact rational arithmetic only. It verifies an explicit positive parameter instance satisfying \(b_1=1/a_1\), confirms both equilibrium residuals vanish, checks the Lyapunov derivative identity at several rational states, confirms the scalar invariant-plane drift has the required sign on both sides of \(b\), and checks
\[
\frac{a_1b}{b+b_2}=\frac{1}{b+b_2}.
\]

The checker does not certify the universal theorem by enumeration. Global existence follows from bounded Lyapunov sublevels; convergence follows from LaSalle's invariance principle plus monotonicity; and the sharp rate follows from the exact reciprocal-variable differential identity. The full basin of \(E_b\) off \(v=0\) remains unclassified.
