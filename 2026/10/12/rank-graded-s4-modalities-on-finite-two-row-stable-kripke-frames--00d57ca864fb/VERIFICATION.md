---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Finite verification

Run `python3 verify.py` using only the Python standard library. An executed replay returned:

`VERIFY_OK 22665 exact assertions; 21844 bounded subset candidates exhaustively tested through n=8; 2143 bounded sublattices through n=8; 351 interior operator tables checked through n=6; 46912 unrestricted function tables screened through n=3; 65536 stable-bimodule candidates screened (16 stable, 4 S4) on n=2; bivariate generating function checked through n=10`

The independent computational routes are: direct meet/join closure on every subset containing the bounds, an unrelated word-condition implementation applied to every same candidate, explicit right-adjoint table construction and operator axioms, unrestricted enumeration of every function on the four- and six-element lattices, direct enumeration of every binary relation on the four-world stable frame against all of the source's stability axioms, and exact formal power-series expansion of the proposed rational function. The finite tests establish the stated finite instances, not the unlimited theorem; the proof in `RESULT.md` handles every \(n\ge2\).

The direct frame checker also confirms that on \(W_2\) there are 16 stable bimodules in total and exactly four whose induced right adjoint satisfies T and 4, with fixed-rank distribution \(u^2+2u^3+u^4\). The full-image rank and total-count formula are checked independently through \(n=8\).

Any future audit should separately inspect the relevant duality and the fixed-set/word arguments rather than interpreting this run as external certification. Independent audit has not been performed.
