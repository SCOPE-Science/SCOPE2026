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
# Verification

The companion `artifacts/verify.py` uses only the Python standard library and exhausts all transitively closed strict orders whose labels are already in a linear extension through six vertices. Every finite poset has such a labeling, so every isomorphism type is represented.

For each poset the script computes the nonalgebraic one-point-extension count in two independent ways:

1. by enumerating all ternary statuses `below / incomparable / above` for the new point and checking the ideal/filter/cross conditions;
2. by enumerating antichains and counting separated ordered pairs \((X,Y)\) with every \(x\in X\) below every \(y\in Y\).

It verifies
\[
c(P)=2J(P)-1+q(P),
\]
the injective-union consequence \(q(P)\le 2^n-J(P)\), and the two stability inequalities
\[
\binom{n+2}{2}+\operatorname{inc}(P)\le c(P)\le 2^{n+1}-1-\operatorname{cmp}(P).
\]

Across sizes \(0\) through \(6\), it checks 5232 naturally labeled posets, with row counts
`1, 1, 2, 7, 40, 357, 4824`.
It also verifies that the unique naturally labeled minimizer is the full chain and the unique maximizer is the empty relation (the antichain), with minima
`1, 3, 6, 10, 15, 21, 28`
and maxima
`1, 3, 7, 15, 31, 63, 127`.

The replay ends with `VERIFY_OK`.

This finite computation checks the combinatorial bridge and equality cases in small sizes; the uniform proof in `RESULT.md` is independent of the computation.
