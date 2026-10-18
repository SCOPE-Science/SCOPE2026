---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

Jongeneel Proposition 3.5 proves f_eps=(-eps*x1^3+x2,-x1^3-x2^3) is globally asymptotically stable and has no smooth Morse Lyapunov function; its nilpotent-Hessian obstruction was inspected in full text. a(x)=exp(-1/||x||²) off zero and zero at origin is C-infinity flat. F-=a*f_eps and F+=-a*x share the zero full Taylor jet; V+=||x||² strictly decreases under F+. A positive bounded time change preserves GAS and all strict Lyapunov inequalities off zero, so a hypothetical Morse Lyapunov for F- would contradict Jongeneel. No analytic-category assertion.

## originality

PASS

The no-Morse GAS example and necessary semisimplicity condition in Jongeneel do not construct two GAS fields with identical full infinite jet and opposite Morse Lyapunov status. Older smooth orbital-equivalence results use a multiplier nonvanishing at the equilibrium, whereas the essential flat multiplier vanishes. Best-of-knowledge new counterexample, with unindexed-folklore risk.

## value

PASS

Full formal Taylor data cannot classify Morse Lyapunov existence even among globally asymptotically stable smooth planar systems. A constructive jet-invisibility boundary is a motivated mathematical negative result, not merely a renamed source counterexample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
