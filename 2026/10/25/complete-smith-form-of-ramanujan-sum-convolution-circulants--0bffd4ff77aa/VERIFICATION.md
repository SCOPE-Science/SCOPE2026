---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For each p^a, the Ramanujan prime-power identity splits the circulant into p^{a-1} copies of p^{a-1}(pI-J). Exact row/column operations and determinantal divisors give Smith factors 1,p^(p-2),0 for pI-J, with p=2 handled. Chinese-remainder permutation tensor products preserve integrally unimodular equivalences; independently sorting prime valuations across the phi(n) nonzero diagonal entries produces the stated divisibility-ordered factors, with n=1 and n=2 boundaries. The determinant product, exponent, congruence kernel and cyclicity criteria follow from those invariant factors. Independently constructed Ramanujan integer matrices and computed exact SymPy Smith forms for every 1<=n<=15; all factors matched. This finite test is not the all-n proof.

## originality

PASS

Fowler–Garcia–Karaali develop the classical Ramanujan prime-power and multiplicative identities and divisor/supercharacter tables. Schlage-Puchta evaluates a determinant of the tau(n)-by-tau(n) divisor-indexed matrix, not the n-by-n difference circulant nor its Smith form. Complex Fourier eigenvalues (n or 0) do not determine integral Smith data. No exact all-modulus invariant-factor formula was identified in Resultary; possible earlier integer-convolution literature remains a risk.

## value

PASS

Complete invariant factors, torsion exponent/order, cyclicity and all mod-m kernel counts form a natural integral-arithmetic refinement to the easily known Fourier rank of a canonical convolution operator. The multiplicative decomposition makes the answer usable at every modulus, not a finite table or numerical exercise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
