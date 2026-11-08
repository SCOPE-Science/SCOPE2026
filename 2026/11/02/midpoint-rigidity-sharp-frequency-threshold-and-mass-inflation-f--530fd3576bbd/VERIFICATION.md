---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Unisolvence of evaluations on span{1,cos(omega*x),sin(omega*x)} for 0<omega<pi yields D=Vprime V^{-1}; the middle diagonal SBP equality forces the interior site to 0. The displayed D and diagonal P directly satisfy all nine entries. Endpoint signs give the iff interval 0<omega<2*pi/3. Hprime=2 sin(omega)(omega-sin(omega))>0 proves strict mass inflation; series and critical limits give the stated coefficients. The unbounded-frequency, nondiagnonal norm cases are not asserted. Independent verification: Independently formed the trigonometric sampling matrices in SymPy, verified exact PD+D^T P = diag(-1,0,1); checked the Taylor expansion M=2+(2/45)omega^4+omega^6/126+... and a feasible-frequency example. Inspected verify_fsbp.py and its normalization. No floating-point sample establishes the infinite interval.

## originality

PASS

Best-of-knowledge: inspected accessible closely related primary PDFs, searched published mathematical records for aliases/stronger results, and compared implications. Abstract existence via positive quadrature is acknowledged, but substituting a specific 3-node trigonometric nodal matrix is not the entire published sharp iff condition with strict mass inflation. Residual priority limitations are explicit.

## value

PASS

The minimal positive-norm trigonometric SBP construction has a sharp geometric/frequency feasibility classification and an unexpected unavoidable mass defect, two natural design constraints distinct from generic SBP existence. The derived threshold and divergence are not a renamed algebraic identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
