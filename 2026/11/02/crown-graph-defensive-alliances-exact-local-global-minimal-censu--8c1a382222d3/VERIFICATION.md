---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

Each crown vertex has degree n-1; the ordinary defensive inequality reduces to y-1_(i in Y)>=t=floor((n-1)/2) on selected a_i and analogously on b_i. For overlap r=0 both occupancies >=t; if r>0 both >=s=t+1. Removing one vertex proves locally minimal iff (r=0,x=y=t) or (r>=2,x=y=s); removing a suitable pair across the common indices proves globally minimal iff the latter overlap has r>=3. Exact labeled choices D=C(n,t)C(n-t,t), H(n,r)=C(n,s)C(s,r)C(n-s,s-r) yield the two polynomials, parity binomial-square simplifications, and Stirling tail proportions. Checked n=3,4 exceptions, disjoint/overlapping cases, and meaning of inclusion globally minimal vs dominating. Independent direct adjacency-mask enumeration checked all nonempty subsets, single-deletion and arbitrary-subset minimality for n=3..7 (not inferred solely from formula).

## originality

PASS

Best-of-knowledge originality after direct claim/implication comparison with published same-object and general methods. Known ingredients, exact overlaps, and inaccessible/plausible priority alternatives are explicitly retained; unsuccessful search alone is not novelty proof.

## value

PASS

A complete labeled inclusion-minimality census of the canonical crown family, including the previously easily conflated local/global distinction and nontrivial odd/even binomial-square law, is a natural useful combinatorial invariant. The exact exceptional r=2 layer and asymptotic rarity quantify a mathematically motivated contrast; this is not simply a generic domination parameter renaming.

The dated certificate retains the supplied scientific assessment, sources and limitations.
