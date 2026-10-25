---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-21.md",
      "INDEPENDENT_AUDIT_2026-10-21.json"
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

Reconstructed the Hamming geodesic rectangle identity and characterized a minimal rooted premise B via coordinate-matching row sets M_i: every M_i is nonempty and each row a has a private coordinate with M_i={a}. Singleton patterns are pairwise private, so 2<=r<=d; inclusion-exclusion counts all labeled rows with these singleton types, and private coordinates force distinct rows and prohibit x as a premise, justifying division by r!. For r=d each coordinate has one unique singleton and yields (q-1)^(d(d-1)). A one-pass unit rule deriving x from a minimal stem can have no smaller premise, proving forced canonical basis. The lower bound fixes r~d/2 private columns and varies remaining nonempty matching patterns to get exp(Omega(d^2)), while a pairwise interval-rule system repeatedly reaches hull in O(|V|^3). Independent direct stem/deletion enumeration compared 12 rank cases across (d,q)=(2,2),(3,2),(4,2),(2,3),(3,3),(2,4),(3,4), all matching; d=3,q=3 counts are 36 and 64. Finite checks are not the all-parameter proof.

## originality

PASS

Classical binary-alphabet rank numbers are exactly the previously enumerated minimal-set-cover spectrum, and generic prime rooted implications are established Horn theory; no novelty claimed for either. The surviving scoped original component is the weighted nonbinary all-rank formula on natural Hamming geodesic closures and the explicit quantitative one-pass versus iterated unit-basis representation gap. No source inspected gave their combined statement, but priority margin is modest and equivalent weighted-cover formulations remain possible.

## value

PASS

The q-ary Hamming graphs and geodesic hull operation are standard natural objects. Complete weighted root-circuit rank counts expose structural geometry of the closure operator, and the precise exp(Theta(d^2)) one-pass unit representation versus polynomial chained basis makes a concrete nontrivial closure-representation tradeoff. Neither generic correctness nor code alone supplies value; the quantitative natural family separation does.

The dated certificate retains the supplied scientific assessment, sources and limitations.
