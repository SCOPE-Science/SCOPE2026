---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The fourth-order coefficient is correct. Independently expanding the spatial tenth power, the \(q/r=1/2\) square root, and the full time average gives the normalized spacetime quartic coefficient \((2201/1250)|a|^2+(444\sqrt5/625)\operatorname{Re}a-141/1000\), while the normalized \(L^2\)-mass factor contributes \((5/2)|a|^2+15/8\). Their difference is exactly \((6/625)(77|a|^2-74\sqrt5\operatorname{Re}a+210)\), whose completed square has unique minimizer \(a=37\sqrt5/77\) and minimum \(2238/1925>0\). The package checker independently recomputes the load-bearing Gaussian moments. Time-frequency selection with two \(h_3\) factors permits a stable second-order resonance only at \(n=6\) (the \(n=0\) mode is tangent); the inspected primary source's threshold Hessian is positive semidefinite on the tangent-orthogonal space with kernel exactly the complex \(h_3\) line. A second-order \(h_3\) component merely reparametrizes the kernel amplitude and does not change the quartic coefficient. The result correctly stops at reduced fourth-order positivity and does not claim full local maximality.

## originality

PASS

The same primary source identifies \(r=10\) as the one-dimensional stability threshold, proves the threshold Hessian is semidefinite with the \(h_3\) kernel, and explicitly leaves the threshold unresolved because higher Fréchet derivatives are needed. Full-text inspection found no fourth-order reduced coefficient or optimized \(h_6\) correction. The diagonal restriction literature concerns different exponent pairs, and current Resultary search returned the assigned record as the exact same-object hit without a covering fourth-variation theorem. The audited coefficient therefore survives best-of-knowledge implication comparison.

## value

PASS

The unique Hessian-kernel direction is exactly the obstruction left open in the motivating mixed-norm stability paper. Computing and optimizing the first nonzero reduced coefficient, and proving it remains positive after every second-order stable correction, is a motivated structural endpoint calculation. It sharply rules out the most immediate escape mechanism without overclaiming full local maximality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
