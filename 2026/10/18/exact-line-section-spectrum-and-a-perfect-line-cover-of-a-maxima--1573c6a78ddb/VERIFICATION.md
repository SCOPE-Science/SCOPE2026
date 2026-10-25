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

PASS. Over k=F5[u]/(u^2-2), c=1+2u, homogeneous derivative equations reduce geometric singularity to invertibility of the 3x3 (2 diagonal, c offdiag) or 2x2 (2,c;c,2) matrices; none singular since c not in F5 and 4-c^2 nonzero. Thus smooth genus 3. Independently constructed all 651 canonical projective triples and evaluated quartic in exact F25, obtaining 56 points. Enumerating all 651 lines yields precisely 63 zero-, 168 one-, 196 two-, zero three-, 224 four-secants, each curve point having respective 3,7,16 incidence counts. Independently tested all fourteen explicit encoded line triples, each with four different rational curve points, and their sets are pairwise disjoint, covering all 56. Hasse–Weil upper bound 25+1+2*3*5=56 verifies maximality and Bezout four-intersection cap gives lower bound 14. These are finite exhaustive field checks plus proved geometric inequalities, not a generalization to other fields.

## originality

PASS

Best-of-knowledge PASS after actual Git proof and independent bounded checks, Resultary semantic search, and comparisons of the precise claim against materially read primary texts and theorem scopes. No examined theorem/database supplies the same final formula or exact incidence certificate. Identified overlaps and access limits are credited; failed searches alone are not treated as a proof of novelty.

## value

PASS

PASS. The explicit maximal genus-three Klein quartic over F25 is a natural exceptional finite-geometric object. A saturated exact 14-line cover together with the complete 651-line section histogram and uniform point-incidence data addresses a published exact covering question at a sharp finite field, not just a known curve point count. The model-specific exact information could be reused in finite-plane incidence research; there is no unsupported claim of a general finite-field theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
