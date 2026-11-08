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

For any complete allocation with h blocks given wholly to distinguished agent1, each whole block adds welfare 2 and every other block at most 1, so W<=t+h. Each other agent values h completed horizontal pairs in agent1 bundle, so EF-ell requires its own value >=h-ell; since at most t-h horizontal pairs remain, (n-1)(h-ell)<=t-h. Explicit balanced horizontal-pair assignments with primed remainders to agent1 achieve h=floor((t+(n-1)ell)/n) clipped to t and are EF-ell (if h=t, all blocks given to agent1 and ell>=t is required by formula; no contradiction). For EFX remove any primed good inside a whole block: horizontal pair values persist, hence nh<=t; ordinary EF optimal allocation with floor(t/n) whole blocks and remainder split as vertical pairs reaches t+floor(t/n). Valuations are for pairs of physical goods, not additive singletons, EFX deletion convention includes zero-marginal goods. Independent direct exhaustive assignment enumeration for n=2,t<=4; n=3,t<=2; n=4,t<=2 checked all directed agent comparisons and all ell=1,2,3, EF/EFX. Infinite result follows from inequalities and constructions.

## originality

PASS

Best-of-knowledge originality for the matching finite-parameter sharp upper/lower envelope and EF-vs-EF1 separation, not discovery of the block model or asymptotic obstruction.

## value

PASS

Sharp finite-parameter welfare frontier of the canonical complement-block obstruction, including exact EF/EFX equality and integer jump from EF to EF1. An exact invariant that future fair-division arguments can use as a tight test instance, while not claiming a theorem for all complement valuations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
