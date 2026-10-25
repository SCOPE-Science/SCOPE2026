---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

The Hilbert–Schmidt kernel 1_{s<t} on L²(dt+aδ_{1/2}) has trace norm-square 1/2+a, excluding the atom self-pair. The range is an energy space with u(0)=0, atomic value u_-(1/2), independent one-sided traces and jump stiffness [u]²/a; norm includes a|u_-(1/2)|². The variational problem E(u,v)=κ²N(u,v) has Dirichlet/Neumann endpoints and two interface laws, whose determinant factors into cos(κ/2)-(aκ±1)sin(κ/2). Because cot(κ/2)-aκ is strictly decreasing on every (2πm,2π(m+1)), each branch has exactly one simple root, in strict order; no pole roots are missed. Expanding κ=2πm+2/(a2πm)±2/(a²(2πm)²)+... gives m⁴(s_{2m+1}-s_{2m+2})→1/(4π⁴a²), s_n~1/(πn), and S_p iff p>1. Independently checked algebraic determinant factorization and high-m roots for a=0.7,2 at m=40,150,600; for a=2, m=600 gives 0.000641623665 vs predicted 0.000641623891. Finite roots are diagnostic, not infinite proof.

## originality

PASS

Best-of-knowledge PASS restricted to the explicit singular-doublet classification and sharp quartic gap for this strict one-atom mixed measure. Ordinary Volterra n⁻¹ asymptotics, Sturm–Liouville transfer techniques and embedded-mass string theory are prior art. A very plausible older point-mass string paper was inaccessible in full and is a material originality risk, not automatically a failure.

## value

PASS

The midpoint one-atom Stieltjes clock is the simplest symmetric model with both continuous integration and an impulse; its exact two-branch spectrum and m⁻⁴ near-degenerate pair splitting are natural operator invariants, sharply distinct from m⁻² interpair gaps. A quantitative model benchmark remains useful even without a general several-atom theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
