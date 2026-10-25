---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

Define D(r)=r xor next r; Q(r)=¬F D(r), P(r)=r xor Q(r). On W=N0×N0 with spatial order along i at fixed j and temporal successor (i,j+1), let p=(i even), q=(j>=i), r=p xor q. Along each temporal orbit r changes exactly once at j=i for i>=1, never for i=0, so Q=q and P=p. Substituting these two observations into the four Vooijs–Fernández-Duque conditions yields satisfiability at (0,0). The obstruction proof requires only arbitrary formula observations a,b: in any finite generated spatial upset, the alternating spatial successor relation produces mutually accessible points with opposite a. Formula 1 keeps a and makes b persistent along time; formulas 3/4 produce conflicting eventual b witnesses, and comparing their witness times contradicts persistence and monotonicity. Hence no finite generated upset. All variable-free formulae are spatially and temporally constant (for nonempty reflexive frames) and thus satisfiable on a singleton iff satisfiable anywhere; one genuine atom is sharp. The source proof and original two-variable Lemma 3.1 were inspected side by side, including the page image.

## originality

PASS

Best-of-knowledge, subject to explicitly documented priority risks: searched the available Resultary records and primary literature, compared the exact claimed quantifiers/invariants to prior implications rather than matching titles, and did not treat inaccessible full text as proof of noncoverage.

## value

PASS

Proving the exact minimum number of propositional letters for failure of the locally finite model property sharpens an established foundational counterexample. One-variable temporal-change encoding provides a genuine expressivity reduction in full Alexandrov DTL and separates this from the variable-free fragment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
