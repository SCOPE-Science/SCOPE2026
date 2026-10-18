---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

Checked original Akhmedov–Akhmedov rectangular Mayer–Vietoris presentation in arXiv:2610.03756 (Sec.5, Lemma 11.2, Question 13.1) and verified product-framing eliminates meridional coupling: H1 ≅ coker A_S ⊕ Z/d, d=gcd(p,q), with A_S=[Q_{p,g}; -Q_{q,h}S] and coker Q_1=Z/p, coker Q_2=Z/q. Natural map coker A_S -> coker Q_1⊕coker Q_2 is well-defined and surjective, so finite H1 order divisible by pq*d. Independently reconstructed supplied symplectic transvection matrices S and original adapted cover Q matrices for the three cases, verified S^T J S=J, and enumerated ALL maximal minors using exact SymPy determinants rather than verifier logs: for (4,4) matrix 8x10: 7 nonzero minors, gcd=16; (3,3) 12x14: 7 nonzero, gcd=9; (6,2) 12x14: 4 nonzero, gcd=12. These equal pq, so the surjection is an isomorphism and direct split yields (Z/4)^3, (Z/3)^3, Z/6⊕(Z/2)^2 with minimal orders 64,27,24. Mapping class group onto Sp gives realizable gluing. The finite certificates establish these three witnesses, not all possible gluings; the symbolic quotient proves universal lower bound within product framing.

## originality

PASS

The primary source asks the three k=3 Smith-minimum problems and gives only weaker lcm divisibility. The new precise product-framed divisor and explicit symplectic minimizing certificates answer a natural restricted instance. Earlier k=1 gluing theorem cannot imply k=3 rectangular Smith minima; no independent covering Resultary finding located.

## value

PASS

Explicitly resolves three posed, structurally natural finite torsion-minimization cases and a stronger general divisibility obstruction; full exact Smith witness matters to constructions of rational-cohomology symplectic four-manifolds. Restricted product framing and limited parameter list stated precisely, no claim of arbitrary normal framing or complete census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
