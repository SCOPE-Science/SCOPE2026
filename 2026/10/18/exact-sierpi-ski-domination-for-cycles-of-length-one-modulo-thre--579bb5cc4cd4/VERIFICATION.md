---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

For n>=3 and k>=1, with m=3k+1, every layer of C_n ⊗_f C_m needs at least k dominators since k-1 internally covers at most 3k-3 and external connecting edges at most two. Equality kn forces exactly one internal hole and a unique tiling by k disjoint triple neighborhoods in each layer; each of the n connecting edges must cover exactly one distinct hole, forcing a coherent cyclic orientation and f(i+2)-f(i) in S_k={2,5,...,3k-1} modulo m. The i↦i+2 orbit lengths are n (odd n) or n/2 (even n). Zero-sum closed walks exist at all even lengths, at odd >=5 for k>=3, odd >=7 for k=2, and only even for k=1; 3-step and (k=2) 5-step sums are impossible. A periodic four-pattern map and one extra selected hole produce kn+1 universally. This yields all exceptional n. Independently tested modular walks and direct graph domination for 304 pairs 3<=n<=40,1<=k<=8; the infinite reasoning is the layer/step equivalence, not finite DP.

## originality

PASS

The minimization over all connecting maps is not ordinary Cartesian domination. Reformulating equality as zero-sum walks is justified by layer rigidity and permits exact classification unavailable from the older two-point range.

General definitions and two-valued bounds are not stronger coverage of all exceptional pairs; the exact ε table strictly refines them. An earlier indexed submitted-draft formula was considered but its purported extra implication is contradicted by a valid n=7,k=3 kn witness and did not survive into the accepted version.

The parameter space is unbounded in both n and k; isolated old examples do not specify the closed-walk length spectrum or exact two-parameter exceptions.

The new theorem strictly resolves an open binary ambiguity; it implies prior bounds, whereas those bounds do not force its exception set.

## value

PASS

The 2024 foundational paper leaves an exact two-valued domination problem on cycles; the equality/exception classification resolves it uniformly over n,k and reveals a reusable correspondence with closed walks in a finite cyclic group. This is a structural classification, not a routine numeric special case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
