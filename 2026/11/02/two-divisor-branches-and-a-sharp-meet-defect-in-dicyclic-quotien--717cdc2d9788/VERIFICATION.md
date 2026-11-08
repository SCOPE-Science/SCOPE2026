---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For every m>=2 write m=2^s u (u odd); the normal-subgroup proof splits N inside the characteristic cyclic index-two A=<a> from N outside A. N inside A is <a^d>, d|2m, giving D_d when d|m and Dic(2^s e) when d=2^(s+1)e. Outside-A normal subgroups have intersection <a^d> with d|gcd(m,2); for even m precisely two additional index-two kernels appear, both yielding the already represented C2 quotient. The reverse embedding poset has D and Q reversed-divisibility branches meeting only at D1=C2 and top trivial T. D_d,d>1 and Q_e have no common lower bound, but common least upper bound D1; thus exactly tau(u)*(tau(m)-1) unordered meetless pairs, all joins, and 1+tau(2m) types. Unique involutions of noncyclic Dic exclude mixed embeddings, and C4 versus odd dihedral handles s=0. Direct independent multiplier-table enumeration of all normal kernels for m=2..9 agrees (m=2..9 outputs in local log); source CHECK.py also inspected but not accepted on VERIFY_OK alone. Formal all-m proof uses the subgroup classification and involution obstruction, not finite exhaustion.

## originality

PASS

Qualified best-of-knowledge PASS: Halder–Ballal establish the quotient-isomorphism reverse-embedding order, a distributive dihedral case and dicyclic nonlattice behavior; the complete two-branch comparability and exact number of missing meets do not appear in the accessible abstract or the inspected mathematics of the frozen package. Tărnăuceanu classifies solitary quotients, a different poset. The original arXiv full PDF was not accessible, so implicit full-text coverage remains a material historical-priority risk.

## value

PASS

Complete structure of the natural quotient-isomorphism poset of every cyclic-kernel dicyclic group, including an exact meet-defect cardinality, supplies a quantitative invariant distinguishing nonlattice from same-cardinality dihedral lattice. It fills a natural classification gap specified by Halder–Ballal; no arbitrary cutoffs or mere replacement of notation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
