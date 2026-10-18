---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

In the original augmented trace code, choose an Fp-basis and the nondegenerate trace-pairing coordinate map phi:F_(p^m)->Fp^m. Each generator column is (phi(x),phi(y),1), hence nonzero and no two distinct defining-set points yield proportional columns: dual weights 1 and 2 are impossible. For gamma=Tr(-beta/alpha), setting y=-alpha^-1 makes the defining trace condition independent of x, so all x occur. For any nonzero t and odd p, the distinct columns at x=0,t,2t satisfy coefficients (1,-2,1), a nonzero weight-three dual relation, giving exact dual distance 3 for every stated p,m,alpha,beta. Independent explicit GF(9) field construction for p=3,m=2,alpha=beta=1 found 33 distinct columns, 80 dependent index triples, and full primal weight enumerator {0:1,18:32,21:96,24:112,33:2}, matching the source formula. This finite instance only checks the all-parameter proof.

## originality

PASS

The primary 2026 Theorem III.1 explicitly asserts dual distance 2 for the D1 family; the present projectivity correction is a contradictory, proved refinement, not a consequence of that false printed assertion. The source Table III example has internally inconsistent typesetting z^3 versus the stated [33,5,18] and Table I last weight 33; the independently reconstructed example supports z^33 and dual 3. Published nearby Resultary correction concerns D2 in Theorem III.5 rather than D1 in III.1.

## value

PASS

Correcting distance 2 to distance 3 changes a qualitative projectivity property for an entire all-parameter published code family and affects dual-distance-based constructions and classifications. It is not just a coordinate convention or a tiny standalone example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
