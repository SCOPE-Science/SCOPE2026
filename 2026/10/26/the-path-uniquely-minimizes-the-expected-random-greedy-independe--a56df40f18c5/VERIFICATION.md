---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Let α_k=m(P_k) and ν(T)=Σ_vΣ_{C component of T−N[v]}α_|C|. The cited Krivelevich–Mészáros–Michaeli–Shikhelman 2024 Theorem 8.3 proves ν cannot decrease under proper KC transformations, Section 8.1 KC reachability builds any n-vertex tree from the path, and their equations give m(T)≥1+ν(T)/n with equality for the path. The new proof derives the strict subadditivity gap h(r,s)=α_r+α_s−α_{r+s}, with unique equality (r,s)=(2,2), by exact small values and an alternating-series error bound for the linear asymptote to α. For an initial path-to-spider KC move with arm lengths a,b,l≥1 the independently computed exact ν gain is h(a,l)+h(b,l)+Σ_{j=1}^{l−1}(α_{a+b+j}+α_j−α_{a+j}−α_{b+j}); the interior sum is nonnegative by the cited prior Lemma 8.2. Unless a=b=l=2 at least one h term is positive; in that exceptional case the j=1 term is exactly 2/15>0. Therefore every first proper path KC move is strictly increasing, and remaining steps are nondecreasing, proving the n≥4 strict path uniqueness. Independently rebuilt α by rational first-arrival recursion and ν by direct graph-component deletion: exact spider gain and positivity for all 216 triples a,b,l≤6, all h(r,s)≥0 for r,s≤44, and the exceptional value 2/15. Finite checks corroborate, not prove, unrestricted cases.

## originality

PASS

Best-of-knowledge statement-and-implication comparison with primary literature, published results and a new Resultary search; foundational premises credited; no negative-search priority inference. Equivalent formulation is that equality in universal lower expectation bound occurs only for P_n. This is not logically equivalent to the previously proved nonstrict m(T)≥m(P_n).

## value

PASS

Uniqueness of the extremizer is a genuine open equality-case gap flagged explicitly in the foundational tree-random-greedy paper, whose path-minimality theorem was nonstrict. The strict first-KC-step invariant and isolated subadditivity equality resolve this natural graph-extremal classification for every tree order, not merely improve a coefficient. The statement does not claim strictness for all KC moves or stochastic order of full greedy output distributions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
