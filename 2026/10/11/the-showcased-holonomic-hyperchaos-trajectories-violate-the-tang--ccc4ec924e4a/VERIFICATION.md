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

The packaged checker uses exact rational arithmetic and a small dependency-free polynomial algebra. It verifies the three printed equation-(3.5) numerators against the compact identity
\[
L^2\dot p=L^2B(q)-q\big(q\cdot B(q)+\|p\|^2\big),
\]
then verifies, after clearing \(L^2\),
\[
\dot S=-\frac{R}{L^2}\big(q\cdot B(q)+\|p\|^2\big),\qquad R=\|q\|^2-L^2,\quad S=q\cdot p.
\]
It also checks that each published configuration has \(\|q\|^2=L^2\) at \(L=0.01\), evaluates the three exact tangent defects, and evaluates \(\dot R(0)=2S(0)\).

The checker is finite algebra supporting the stated identities; it is not a numerical simulation and does not test the existence or nonexistence of hyperchaotic invariant sets for correctly initialized data on \(R=S=0\). The scientific conclusion is limited to the incompatibility of the three published numerical initial conditions with the stated holonomic phase space.
