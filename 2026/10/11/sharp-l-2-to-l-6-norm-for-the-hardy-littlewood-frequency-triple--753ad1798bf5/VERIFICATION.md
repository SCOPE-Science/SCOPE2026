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

The universal proof reduces the norm problem to the explicit two-variable rational function \(\Phi(X,r)\). The boundary estimate is exact: every two-frequency face has normalized sixth moment at most \(5/2\), whereas an interior test point gives \(11/3\). Hence every global maximizer satisfies the interior stationarity equations.

`artifacts/verify.py` uses exact rational polynomial arithmetic to certify the nontrivial algebraic step. It verifies the cleared identity that substitutes
\[
X=\frac{2(1-r^2)}{r^3+4r^2-3r-4}
\]
into the second stationarity equation and obtains the degree-ten polynomial \(R\). It constructs the full Sturm chain, proves there is exactly one root on the whole feasible interval \((1,23/20)\), and isolates that root to \((547/500,219/200)\). Exact sign checks then give \(0<X_*<1\).

The same program numerically reconstructs
\[
(X_*,Y_*,Z_*)=(0.334220497181418\ldots,0.362816605726877\ldots,0.302962897091705\ldots)
\]
and
\[
\mathsf C_{013,6}^6=3.676690884789743\ldots,\qquad
\mathsf C_{013,6}=1.242346821125471\ldots.
\]
It also evaluates the exact cubic self-convolution expression on 20,000 random complex triples as a corroborative stress test. Random sampling is not used to prove the global inequality.

Actual replay terminal line:
`VERIFY_OK sturm_feasible_roots=1 r=1.094331386704356 X=0.334220497181418 Y=0.362816605726877 Z=0.302962897091705 K=3.676690884789743 C6=1.242346821125471 random_cases=20000 max_random=3.674059471999777`

Scientific limits: the certificate proves the polynomial root count only after the analytic reduction, so both pieces are needed. No claim is made for other supports, other exponents, or a radical expression for the algebraic optimizer.
