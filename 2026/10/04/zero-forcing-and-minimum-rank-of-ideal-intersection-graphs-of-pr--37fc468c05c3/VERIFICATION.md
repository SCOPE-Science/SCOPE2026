---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

Every nonzero proper ideal is indexed by a nonempty proper support \(S\subsetneq[r]\), and adjacency is exactly \(S\cap T\ne\varnothing\). The incidence matrix \(B\) has rank \(r\) because the singleton-support columns are the standard basis; therefore \(B^\mathsf{T}B\) is a rank-\(r\) real symmetric pattern matrix with off-diagonal entry \(|S\cap T|\), giving \(M\ge(2^r-2)-r\). Independently replaying the stated white family \(\{1,2\},\{2,\ldots,r\},\ldots,\{r\}\) gives exactly \(r\) successive forces, hence \(Z\le(2^r-2)-r\). The standard inequality \(M\le Z\) closes both bounds and yields \(\operatorname{mr}=r\). A fresh rational reconstruction in this audit reproduced ranks and forcing sizes for \(r=3,4,5\); those finite checks are corroborative only.

## originality

PASS

The closest primary paper on the same ideal-intersection graph explicitly analyzes products of fields and several classical graph invariants, but does not state zero forcing, maximum nullity, or minimum rank. The foundational zero-forcing paper supplies only the general inequality. Fresh Resultary comparison under both ring and subset-intersection formulations returned the assigned record as the exact match and no broader published theorem that determines these three parameters for the whole Boolean-intersection family.

## value

PASS

The theorem exactly recovers the number of field factors from a standard inverse-eigenvalue invariant and simultaneously determines zero forcing and maximum nullity for the entire family. The result is a natural structural invariant of a canonical algebraic graph, not an arbitrary finite computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
