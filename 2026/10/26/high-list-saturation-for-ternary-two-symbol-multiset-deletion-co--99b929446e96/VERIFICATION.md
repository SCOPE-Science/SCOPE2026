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

For n>=4 each ternary length-n multiset has one or more heavy coordinates (multiplicity >=2), exactly 12 messages have only one heavy coordinate, and all remaining messages incur at least two monochrome-list incidences. Thus 2|C|-T <= H <= 3L and T<=12 imply |C|<=floor(3L/2)+6. For L>=6 the twelve one-heavy vectors and balanced two-heavy edge vectors with t_01=t_12=floor((L-4)/2),t_02=ceil((L-4)/2) achieve the bound: n>=ceil(L/2)+1 ensures all edge vectors valid and distinct, and mixed/pure traces each have load <=L. For L=5 the thirteen-word length-four deletion and injective, trace-preserving maximum-coordinate lift work for all permitted n. Equality at even L forces T=12,H=3L and every remaining word exactly two-heavy; no stronger uniqueness claim. Independent enumeration checked all six signatures, L=5..39 three permitted lengths, and the complete 2^15 subcodes at n=4.

## originality

PASS

Novelty best-of-knowledge is the complete unbounded high-list regime L>=5 and even-L structural equality conditions; the known unique-decoding (L=1) and earlier four-list cases are credited and excluded.

## value

PASS

The multiset channel with two surviving symbols is the smallest nontrivial trace family; the exact all-high-L capacity solves a natural incidence hypergraph list-packing problem. Even-L rigidity identifies unavoidable codewords and saturated received-symbol constraints, valuable structure beyond a numerical optimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
