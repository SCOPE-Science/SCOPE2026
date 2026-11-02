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

# Reproduction and proof/experiment boundary

The self-contained `verification.py` requires only the Python 3 standard library. From the same directory run `python3 verification.py`.

The independent second-moment derivation uses \(Y_n=S_{T_n}X_{T_n}\) just after a sign flip. Conditional on an iid run length \(L_n\), with \(c=v/k\) and \(A_n=e^{-kL_n}\), its exact reversal map is
\[
Y_{n+1}=-A_nY_n-c(1-A_n).
\]
Write \(a=\mathbb EA_n\), \(b=\mathbb EA_n^2\), \(m=\mathbb EY_n\), \(M=\mathbb EY_n^2\). Stationary moments solve
\[
m=-c\frac{1-a}{1+a},\qquad
M=\frac{2c(a-b)m+c^2(1-2a+b)}{1-b}.
\]
The exact integrated squared position within one run is
\[
c^2L+\frac{2c(Y_n-c)(1-e^{-kL})}{k}
+\frac{(Y_n-c)^2(1-e^{-2kL})}{2k}.
\]
Dividing its expectation by \(\mathbb EL=\tau\) yields
\[
V_{\mathrm{reward}}=\frac{c^2\tau+2c(m-c)(1-a)/k+(M-2cm+c^2)(1-b)/(2k)}{\tau},
\]
which simplifies algebraically to the stationary-renewal-correlation formula in `RESULT.md`. The independent derivation uses no numerical fits.

Executed reproduction tests: 48 exact correlation-versus-reward comparisons using deterministic, exponential, Erlang-2 and symmetric two-point dwell times; 12 independent event-driven stationary squared-position time integrations (120,000 sampled runs per case, plus burn-in); Jensen-bound samples at 12 mean/rate pairs; weak-trap coefficient checks for three nondegenerate laws and the deterministic finite limit; and sharp unattained upper-envelope convergence. All assertions passed. The maximum observed independent-event-integration relative discrepancy in those 12 cases is below 0.4%. Random draws are seeded, making checks reproducible. The analytic derivation is the mathematical proof; finite stochastic examples are not exhaustive and cannot prove a universal waiting-law or continuous-parameter statement.

Scientific scope: identical iid orientation residence lengths, positive finite mean, fixed propulsion speed, overdamped harmonic trap, and stationary initialization. Inverse spectroscopy requires exact data over all positive trap stiffnesses. Scientific originality is subject to remaining literature-priority risk; independent audit has not been performed.
