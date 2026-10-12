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

The claim is analytic. Its critical checks are:

1. The source's Proposition 4.4 gives
\[
\delta^{(2)}\ge d_s=\frac{1-\sqrt{1-(2s-1)^{-2}}}{2}>0.
\]
2. Under the contradiction assumption \(r_A^{(m)}(\gamma)>0\), the source's Proposition 4.5 gives \(\alpha_i\ge d_s\) for intermediate chain points and, after solving its displayed positivity inequality, gives the explicit upper cutoff
\[
\alpha_i<\frac{1-q_s(\gamma)}2.
\]
3. The source's quoted Fagnani--Ravazzi inequality then gives every fully controlled intermediate transition a decrement at most \(-\eta_s(\gamma)\).
4. There are \(m-3\) such transitions before the final nonpositive transition, so
\[
r_A^{(m)}(\gamma)\le1-(m-3)\eta_s(\gamma).
\]
The chosen integer \(M_s(\gamma)\) makes the right-hand side strictly negative, contradicting nonnegativity.
5. The asymptotic exponent follows by expanding \(h_2(\delta_* -\Delta)\), then \(2^{s\varepsilon}-1\), then \(-\log_2(1-q^2)\).

The bundled checker recomputes the constants and stable small-gap ratios for representative even \(s\). It is a consistency check only; finite evaluations do not establish the infinite theorem.

Limits: the result gives a sufficient round certificate and no lower bound on the optimal number of rounds. The finite-blocklength size needed by the source's probabilistic distance theorem is not quantified here.
