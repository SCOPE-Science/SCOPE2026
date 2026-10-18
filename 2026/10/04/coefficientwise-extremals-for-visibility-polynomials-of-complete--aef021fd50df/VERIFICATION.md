---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-14.md",
      "INDEPENDENT_AUDIT_2026-10-14.json"
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

The domain is connected noncomplete complete multipartite graphs on fixed N>=3. Every selected pair in different parts is adjacent; two selected vertices in one part are geodesically visible exactly if an omitted vertex lies outside their part. For complement T of t>=1 vertices, the mutually disjoint bad events are T contained in some part of size >=t+2; hence r_{N-t}=C(N,t)-sum_{n_i>=t+2}C(n_i,t), and r_N=0. Parts at most 2 make every proper set visible, and a part >=3 produces a nonvisible proper set. For r_3, only the star has any bad triple and r_3(star)=C(N-1,3); for r_{N-1}, the exact formula is sum_{n_i<=2}n_i. At N>=6, K_{3,N-3} has near-top coefficient 0, below the star's 1, so no minimum; N=3,4,5 are checked by the remaining nontrivial coefficients. Independent elementary partition enumeration for N=3..13 reproduced maximum and threshold; actual verifier checks direct geodesics through N=10, partition enumeration through N=30; these computations corroborate the all-N proof, not replace it.

## originality

PASS

The new mathematical assertion is the fixed-order coefficientwise extremal classification and sharp nonexistence threshold. General join and complete-bipartite polynomial formulas are prior coverage of the counting machinery, not independently novel. Comparing the proof implications, maximum mutual-visibility NUMBER results and fixed-family coefficient formulas do not state the full cross-partition coefficient partial-order theorem. Best-of-knowledge original after a search of equivalent extremal language and closest primary texts, with explicit historical-phrase risk.

## value

PASS

Coefficientwise distributional extremality is a natural stricter problem than largest mutual-visible set size. Classifying all maximizers and the sharp N=6 first obstruction to a minimum reveals a genuine incompatibility of cubic and near-top extremizers. This is a substantive all-order structure theorem rather than a single small-graph calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
