---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

For a total dominating set \(D\), each coordinate hyperplane \(H_i\) is covered by the proper subspaces \(H_i\cap d^\perp\). If \(|D|\le q\), the finite-vector-space covering lemma forces one \(d^\perp\) to contain \(H_i\), hence \(d\) is on the \(i\)-th coordinate axis; doing this for every \(i\) gives \(|D|\ge n\). This proves the lower bound \(\min\{n,q+1\}\). The coordinate basis realizes \(n\); beyond the threshold, projective representatives of a suitable two-plane realize \(q+1\). Pairing arguments give the least even size: the basis construction handles \(n\le q+1\), anisotropic two-planes handle odd \(q\) beyond the threshold, a totally isotropic two-plane plus one extra vector handles even \(q,n\ge5\), and \((q,n)=(2,4)\) has the explicit four-vertex witness. Fresh exhaustive calculations for \((q,n)=(2,3),(2,4),(3,3),(3,4)\) reproduced both formulas; these finite cases are corroborative only.

## originality

PASS

Badawi and Abdulla–Badawi define and structurally analyze these dot-product graphs; the latter full paper treats finite-field structure in the two-factor case. Saleh–Megahed studies ordinary domination for total dot-product graphs over residue rings, not total or paired domination of the zero-divisor induced graph. A published SCOPE theorem gives total/paired domination for the ambient finite-field total dot-product graph, with \(q+1\) as the total-domination value; it does not imply the zero-divisor threshold because the induced graph has the strictly smaller value \(n\) when \(n<q+1\), and domination is not inherited monotonically from the ambient graph. No inspected source covers the two-regime formula.

## value

PASS

The result identifies a sharp and geometrically natural competition between the \(n\) coordinate hyperplanes defining the zero-divisor locus and the \(q+1\) hyperplanes of a projective line. Exact total and paired domination are standard strengthened domination invariants, and the dimension-field transition is a meaningful structural boundary rather than an arbitrary finite computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
