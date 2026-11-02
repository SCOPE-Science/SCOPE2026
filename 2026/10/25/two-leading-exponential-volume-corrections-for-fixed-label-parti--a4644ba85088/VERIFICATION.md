---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

Reconstructed the polytope from Behrend et al. Proposition 2.8 and verified simplex Dirichlet tails m!Vol({sum_I x_i>h})=sum_{j<|I|} binom(m,j) h^j(S-h)^(m-j). Single-coordinate forbidden caps have normalized volume A^m, pair cap intersection (B-1)^m. Integrating the two-coordinate facet violation with both caps gives (m-B)B^(m-1)+(B-1)^m. Bonferroni cancellation removes pair cap intersections exactly. Pair-pair and pair-cap overlaps have residual <C; higher rank k>=3 have residual <=C and at most O_n(m^(2n-3)) multiplicity. This proves the stated error for fixed n>=5; C/B<1 proves the ratio limit. Independently checked pair integral by exact arithmetic/numerical integration; finite hull computations do not prove asymptotics.

## originality

PASS

The same object and normalization are identified with the original partial-permutohedron facet description. Behrend et al. prove n<=4 exact volume cases and pose n>4 as a problem/conjecture, not a theorem implying the supplied fixed-n>=5 coefficient. Related published partial-permutohedron results found by semantic search concern inradius, circumball, ellipsoids or diameter. Best-of-knowledge claim survives comparison, without absolute priority certification.

## value

PASS

An explicitly motivated open fixed-label volume enumeration problem receives a uniform-in-m three-layer asymptotic for every fixed n>=5, including a nontrivial polynomial coefficient and a sharp next-exponential-base remainder. The result is structural rather than a small table or simple substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
