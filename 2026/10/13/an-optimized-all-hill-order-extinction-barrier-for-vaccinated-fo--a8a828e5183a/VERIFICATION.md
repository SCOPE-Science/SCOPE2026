---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For the stated deterministic ODE, nonnegativity and boundedness follow from the inward coordinate faces, the human-population balance N'=Lambda-mu*N-d*I, and the stable environmental equation. The uninfected S,V subsystem is Metzler and Hurwitz; variation of constants with its nonnegative infection losses gives the exponentially accurate componentwise upper ceiling at S0,V0, including for arbitrary finite initial data above those values. Differentiating g_n(C)/C gives the claimed unique positive maximizer and the optimal scalar envelope, with the inequality also holding at zero. Strict threshold makes the eventual perturbed infection comparison Hurwitz via the positive-vector test. At equality the positive left nullvector gives the exact identity for Z; its possible positive drift is bounded by an integrable exponential times bounded Z. Adding the tail integral of this bound gives monotonicity and convergence of Z. On the omega-limit set S<=S0 and V<=V0, and constant Z with I>0 or C>0 forces S=S0,V=V0, where S'<0. Positivity of I or C persists briefly, contradicting constancy of Z. If E>0 with I=C=0 then I' is positive, also impossible there. Thus E,I,C decay to zero, and S,V,R converge by stable equations. At equality the local direct-transmission number is strictly below one, and g'_n(0)=0; the disease-free Jacobian is block triangular with Hurwitz blocks and yields trajectory-wise eventual exponential convergence. The rational witnesses check by substitution (thresholds 43/204 and 1). This is a sufficient condition, not an optimal epidemic threshold or an applied eradication guarantee. The frozen verify.py was inspected and not executed; it is a finite check, not proof for all n.

## originality

PASS

The checked source establishes a different, n=1 global criterion and discusses n>=2 separately. The strongest catalogue comparisons use a related neutral-threshold proof for different equations and thresholds. The distinct supported content is the sharp scalar Hill envelope coupled to the disease-free susceptible/vaccinated composition and an inclusive sufficient global extinction threshold for the stated n>=2 system, with eventual exponential convergence.

## value

PASS

The result addresses the model paper's distinction between local and global extinction for higher-order response. The composition-based sufficient bound can certify a case the coarser total-population envelope does not. In particular the equality case and its exponential convergence are useful distinctions because the bounding matrix is neutral, not strictly stable, at that boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
