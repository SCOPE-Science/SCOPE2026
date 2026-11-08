---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

A leaf copies its core at the next synchronous step. For each nonisolated core vertex with one or two base neighbors, define two ports (actual neighbors, or neighbor and self for a degree-one core), converting inertial tie into a three-bit median. For initial core X and leaves Y, core B after one step and A after two satisfy Bv=M(Xports,Yv), Av=M(Bports,Xv). Median absorption gives Av=M(Bports,Av); if both A-port bits contradicted Bv, each port vertex would force its X-bit to 1-Bv, contradicting Bv=M(Xports,Yv). Thus Bv=M(Aports,Bv), so (A,B) is two-periodic, yielding pointwise F^4=F^2, even infinite disconnected degree<=2 bases. Isolated bases are immediate swaps. Independent full initial-state enumeration for all labelled degree<=2 bases up to five core vertices corroborates; explicit K1,3 corona orbit 33->18->32->0 proves degree3 obstruction, and alternating odd-cycle configuration reaches zero after m steps. The analytic local proof, not finite testing, supplies the infinite claim.

## originality

PASS

Goles–Olivos 1980 establish eventual period <=2 for finite symmetric threshold networks but not uniform entry time <=2, and Benjamini et al 2014 obtain a.s. period-two under probabilistic invariance assumptions on certain infinite graphs, not pointwise every configuration on leaf coronas. Benjamini–Zakharov–Zhukovskii 2026 give worst-case stabilization on finite odd-degree trees; cycle coronas are not trees, path corona endpoints are even-degree, and infinite coronas lie outside. The all-state local F4=F2 identity and degree-3 obstruction are not directly entailed by these prior statements. Specialization under threshold-with-memory terminology remains residual priority risk.

## value

PASS

A graph-family-wide exact two-round stabilization identity, sharp for both finite and infinite graphs, meaningfully distinguishes whiskered from unwhiskered majority clocks and provides a local algebraic mechanism beyond eventual-period two. The sharp degree threshold and explicit counterexamples are motivated boundaries.

The dated certificate retains the supplied scientific assessment, sources and limitations.
