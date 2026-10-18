---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

The 11-block morphism has fixed bits at residues 0,1,2,3,4,6,7,8,9,10 and only the bit at residue 5 depends on the source Thue--Morse symbol. For each shift residue pair and each of 11 source residues, independently treating occurrences of residue 5 as arbitrary bits is a stronger universal condition than actual correlations; checking all 121 ordered pairs yields exactly the 20 listed orientations. For 3^+-power avoidance, any factor of length 3p+1 and period p with p>=5 and 11 not dividing p has a fixed mismatch residue in 2p+1 comparison positions; p=11q yields a forbidden Thue--Morse cube of period q from the residue-5 positions; p=1..4 exhaust the six length-3 Thue--Morse factors and every 11-block offset. Thus both properties hold for all integer shifts in these classes; density is 20/121 because each residue pair has equal asymptotic frequency among a<b. A new independent checker reconstructs the 20 robust residue orientations and all short factors.

## originality

PASS

The primary 2023 publication includes the *identical* 11-uniform morphism and finite evidence for (1,5) and 122 other tested pairs. Those tests do not prove all quotient lifts; its positive-density Theorem 35 concerns only (1,a) and combines several morphisms, not one word simultaneously for a positive-density two-dimensional set of (a,b). The adversarial-residue template establishes a new unrestricted arithmetic family, conditional on no unindexed equivalent source note.

## value

PASS

The cited conjecture asks which pairs admit infinite binary 3^+-power-free pseudoperiodic words; replacing scattered finite witnesses by an exact two-dimensional family of density 20/121 for the same single morphism is a meaningful structural and quantitative extension. The family is sufficient only; it does not settle the full conjecture or characterize all pseudoperiods.

The dated certificate retains the supplied scientific assessment, sources and limitations.
