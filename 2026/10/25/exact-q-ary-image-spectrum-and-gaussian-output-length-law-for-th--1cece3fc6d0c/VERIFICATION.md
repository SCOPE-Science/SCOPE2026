---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

For every q≥2 and n≥1, deleting original-input first symbols of all noninitial runs removes exactly s−1 symbols where s=#input runs; deletion cannot increase runs, so any output y satisfies |y|+r(y)−1≤n. Conversely appending one new leading symbol to each noninitial run of y constructs a minimal preimage and padding by n−|y|−r(y)+1 new singleton runs (alternating letters, always possible for q=2) constructs every larger source length. Run-composition counting proves exact N_{n,m}, summing minimal feasible lengths gives qt z/((1−z)(1−tz−(q−1)tz²)); deterministic fiber representatives prove exact zero-error code size. Unique dominant pole near t=1 yields capacity and quasi-power characteristic function with μ=(1+1/√(4q−3))/2 and σ²=(q−1)/(4q−3)^(3/2)>0. New independent exhaustive image computation across 23 (q,n) pairs totaling 10785 input words and symbolic derivative identities checked; infinite CLT rests on analytic proof.

## originality

PASS

The original 2026 contextual deletion paper defines the same binary threshold mechanism, but its published fixed-k analyses/Section V do not state the complete threshold-one q-ary exact image language, finite length histogram, zero-error capacity, and distinct-output central limit law. Con–Ribeiro prove broader input-correlated synchronization capacity methods without this exact deterministic run-language evaluation. These are qualified priority comparisons, not proof against all older automata/transducer literature.

## value

PASS

Threshold-one is a natural exact endpoint and benchmark for context-dependent deletion channels, giving not just capacity but every finite-block output frequency and a genuine Gaussian law for lengths of uniformly chosen distinct outputs. It clarifies the distinction between uniform source inputs and uniform distinct outputs and supports exact zero-error representative codes. The structural image criterion is independently useful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
