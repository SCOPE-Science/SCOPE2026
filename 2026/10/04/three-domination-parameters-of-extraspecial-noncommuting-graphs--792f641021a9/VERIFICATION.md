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

The verification separates the infinite proof from finite corroboration.

1. **Exact graph model.** For an extraspecial group, the quotient \(G/Z(G)\) is a symplectic vector space. Each nonzero quotient vector has exactly \(p\) group-element lifts, and two lifts are adjacent precisely when the symplectic pairing of their vectors is nonzero.

2. **Upper-bound witness.** A symplectic basis has \(2n\) vectors. Choosing one lift of each basis vector gives a dominating set; the \(n\) hyperbolic pairs are edges, so the same set is total dominating and has a perfect matching.

3. **Lower-bound mechanism.** If the selected quotient vectors span a proper subspace \(W\), then every group element lying above \(W^\perp\setminus\{0\}\) commutes with the entire selected set and therefore must itself be selected. This forces
\[
p(p^m-1)+2n-2m
\]
selected vertices when \(m=\dim W^\perp\), and
\[
p(p^m-1)\ge2m
\]
gives the bound \(2n\).

4. **Finite replay.** The standalone checker builds the full symplectic blow-up graph and exhaustively searches all candidate sets through the optimum for
\[
(p,n)=(2,1),(3,1),(2,2).
\]
It separately constructs \(D_8\) and \(Q_8\) from multiplication and checks their ordinary domination value. It also replays the elementary lower-bound inequality on a finite parameter grid.

Exact output:

```text
VERIFY_OK
symplectic_model_p=2_n=1: vertices=6 gamma=2 gamma_t=2 gamma_pr=2
symplectic_model_p=3_n=1: vertices=24 gamma=2 gamma_t=2 gamma_pr=2
symplectic_model_p=2_n=2: vertices=30 gamma=4 gamma_t=4 gamma_pr=4
D8_and_Q8_actual_group_checks=gamma_2
lower_bound_inequality_grid=p2..17_m1..12_passed
```

The finite search is not an infinite certificate. The arbitrary-\(p\), arbitrary-\(n\) theorem is proved by the symbolic symplectic argument.
