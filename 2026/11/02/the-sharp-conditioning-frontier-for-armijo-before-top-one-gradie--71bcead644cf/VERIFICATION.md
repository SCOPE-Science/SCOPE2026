---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Quadratic expansion gives exactly the full-gradient Armijo interval (0,α_*] and the compressed change −aα_*g_i²[1−a(1−σ)Q_ii‖g‖²/(g^TQg)]. Every g≠0 is realizable and its selected g_i is nonzero. As an independent check of the sharp geometric factor, put u=e_i, b=g/‖g‖, θ=angle of their lines and H=uu^T−rbb^T. For θ>0 the two eigenvalues h_+>0>h_- have sum 1−r and product −r sin²θ. Over Q with eigenvalues 1,κ, the maximum of tr(QH) is κh_++h_-: put the κ direction along h_+. Its zero at r≥1 gives κ(r−1)²=(κ−1)²r sin²θ. This also proves attainment; θ=0 or κ=1 gives r=1 directly. Top-one constrains θ≤π/4, and the maximum grows in κ and θ to R(K) at K and a tie. This proves both directions, strict descent below the frontier, equality with a permitted tie choice, and strict increase above it on an open unique-selection set by perturbation. At K=1 boundary equality holds for every gradient, and violation causes increase even without a tie. Solving the unscaled equality gives K+K^−1=2+2σ²/(1−σ) and 2.618… at σ=1/2. For example at σ=1/2, a=1, Q=[[57,−24],[−24,43]]/25 has eigenvalues 1 and 3 and g=(1,9/10) is a strict increasing witness: the governing ratio is 10317/4863>2. Inspected the verifier; its logged 3892 tests are finite numerical checks and not the sharpness proof.

## originality

PASS

Credit prior work for the compressed Armijo algorithm and classical sharp two-inner-product angle geometry. The distinct supported claim is the necessary-and-sufficient objective frontier for this specified maximal-step then top-one composition, including its threshold, equality mechanism and strict unique-selection failure regime. No inspected prior algorithm theorem or indexed exact frontier covers that claim. In particular, the geometric factor alone must not be presented as a new matrix inequality.

## value

PASS

There is a concrete algorithmically motivated gap between a full-gradient Armijo decision and the resulting sparse update. The exact two-coordinate boundary shows how much conditioning and scaling can be tolerated even before stochasticity or feedback enter, and separates a tie-attained boundary from genuinely increasing unique-coordinate instances. This is a usable sharp baseline for the method, not evidence about long-run convergence or novelty of the underlying matrix inequality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
