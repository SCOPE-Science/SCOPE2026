---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

For the exact printed ETM-3D ODE and rho>=0, independently reconstructed A and N. For any SPD centered W, odd cubic C_W=u^TWN(u) would dominate the quadratic derivative at t u or -t u, so global strict negativity forces C_W≡0. Independently solved all seven cubic coefficients: W=diag(a,1,2-a) after positive scaling, 0<a<2. Computed M=(WA+A^T W)/2, its negative-definite principal-minor criterion, det M=-F(a,rho)/4, F(0,rho)=-10 and F(2,rho)=-4rho^2. Independent exact SymPy checks recovered disc_a(F)=120P and exactly two positive P roots in (2.188758,2.188759) and (3.355161,3.355162). Exact root counts: F(a,1) has two roots in (0,2), F(a,5/2) and F(a,4) have none; discriminant and nonvanishing endpoint signs extend the feasibility conclusion over all rho>0, separately checking rho=0. M≺0 implies dV/dt<=-c||u||^2, hence global exponential stability for every rho<rho*. Independently checked disc_x Q=12000P; Q has no real root at rho=0 or 1, two at 5/2, four at 4, so its first real double root is born at rho*. The equilibrium substitution y=5x/D,z=x(rho+x)/D satisfies f1=-x Q/D^2, f2=f3=0; resultant_x(Q,D)=-500(rho^2-5) prevents denominator degeneracy at rho*, while gcd_r(P,Q(0,r))=1 excludes x=0. Thus a distinct real equilibrium exists at rho*, preventing global attraction and proving sharpness. The source verifier was inspected; identities and root counts were independently recomputed in /mnt/data private work script rather than inferred from ALL_VERIFY_OK.

## originality

PASS

Best-of-knowledge original exact ETM-3D parameter boundary and forced centered-quadratic certificate classification. The defining October 2026 article supplies the vector field, energy-preserving triad, equilibrium quartic and two numerical saddle-node positions, but its proved global result is ultimate boundedness, not origin convergence. Goyal–Pontes Duff–Benner supplies the general energy-preserving quadratic Lyapunov test without performing the ETM-specific discriminant/root analysis. The matching Resultary listing is this same record indexed publicly, not an independent antecedent. No distinct source inspected implies the exact algebraic sharp threshold or its first saddle-node coincidence.

## value

PASS

The ETM-3D benchmark exhibits parameter-dependent bifurcations. Locating the exact first global-attractor loss is a motivated dynamical boundary: it upgrades the source’s numerical first saddle-node and global boundedness to an all-initial-condition exponential-stability theorem with sharp failure at an explicitly isolated algebraic parameter. The cubic-cancellation classification shows a nontrivial coincidence: the full class of globally strict centered quadratic certificates loses feasibility at the same value where nonzero equilibria first appear. That exact phase boundary and certificate rigidity are reusable for bifurcation/control comparisons and are neither a routine restatement of a general quadratic-energy criterion nor a merely numerical refinement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
