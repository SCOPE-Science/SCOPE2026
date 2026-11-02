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

Independently reconstructed the complete 72-state transfer matrix from maps (a,b)->(a,a+b),(a+b,b) mod 9 and exactly checked its degree-72 characteristic factorization with SymPy. The sextic q was independently verified irreducible mod 17; evaluating R(E)C at zero from exact integer recurrence gave 116619264, proving the q-mode occurs. Independent complex root calculations gave maximal pair modulus 1.439066724563126 and secondary pair 1.4081559256090412; actual check_stern9.py was inspected for exact rational Rouché-center certificates, so root separation is not inferred only from floats. Perron eigenvalue 2 is simple and uniform projection contributes exactly 2^k/72. Standard rational generating-function root growth gives limsup, not pointwise lower bounds.

## originality

PASS

The Deshouillers–Schinzel primary eight-page paper proves all primitive Stern-residue pairs have density 1/72 at modulus nine using an invertible finite automaton. It does not present the exact charpoly factor or scalar-mode certificate in Theorems 1.1,2.2,3.1–3.5 inspected. Distribution of logarithms by Bettin et al concerns a different statistic.

## value

PASS

The sharp failure of square-root scale and explicit dyadic discrepancy growth constant for a natural primitive residue pair quantify mixing beyond the known density theorem, with an exact recurrence certificate; a fixed modulus and pair are motivated by the first non-prime-power modulus where finite automaton mixing has exceptional modes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
