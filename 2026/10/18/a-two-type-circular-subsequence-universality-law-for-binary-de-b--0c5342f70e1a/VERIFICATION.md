---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

For repeat gap L<=n-2, exactly two specified length-L+2 patterns each occur 2^(n-L-2) times, giving E_L=2^(n-L-1). All repeat events total 2^(n-1), leaving two long gaps; exactly two alternating length-n cyclic factors force either (n,n) or (n-1,n+1). Repeated equal pairs synchronize the greedy 3-state arch scanner; each gap produces floor(L/2) completed arches, and even-length gap contributes L/2 deficient cyclic cuts. Summing yields the stated floor/ceil throughput, D_n and D_n+n counts, with no inference from finite cases. Independently generated FKM de Bruijn cycles at each n=3..10 and checked every cyclic cut, all repeat gaps, K,H and de Bruijn uniqueness.

## originality

PASS

Known omnisequence/greedy arch theory characterizes scattered universality of general words and binary de Bruijn cycles guarantee contiguous factor coverage, but neither establishes the universal per-cut two-type exact distribution for every de Bruijn cycle. Prior Resultary count of unrestricted binary words is a different enumeration problem, not this per-cycle rigidity theorem.

## value

PASS

An exact universal rotational statistic of canonical de Bruijn cycles depends on only one local adjacency bit despite exponential variation in cycle structure. The complete all-order two-type classification and exact count of deficient roots are natural structural invariants, not one construction or a tiny table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
