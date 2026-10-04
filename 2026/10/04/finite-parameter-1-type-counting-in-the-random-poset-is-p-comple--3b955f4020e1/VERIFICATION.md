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

The companion `artifacts/verify.py` uses only the Python standard library and has two independent implementations of the finite one-point-extension count.

The first enumerates ternary status assignments to the old vertices and tests the ideal/filter/cross conditions. The second directly adjoins a new point, inserts the declared strict-order relations, and checks irreflexivity, antisymmetry, and transitivity of the full enlarged relation.

The replay enumerates every transitively closed poset whose labels are in a topological order through five vertices: 1, 1, 2, 7, 40, and 357 posets for sizes 0 through 5, respectively, or 408 finite posets in total. For every one it checks that the two extension counters agree.

It then computes the number `J(P)` of ideals independently and verifies, for `m=1,2,3`,

\[
c(P\oplus C_m)=c(P)+mJ(P)+\binom{m+1}{2}.
\]

It separately checks the reduction identity

\[
J(P)=c(P\oplus C_2)-c(P\oplus C_1)-2
\]

for every enumerated poset, and checks the closed forms `c(C_n)=binom(n+2,2)` and `c(A_n)=2^(n+1)-1` through seven points.

The output reports the observed count ranges by size, then

`checked_posets= 408`

and finally `VERIFY_OK`.

The replay checks the finite combinatorial bridge and reduction identity. It does not re-prove the classical theorem that counting antichains in a finite poset is #P-complete; that theorem is cited as an external mathematical input.
