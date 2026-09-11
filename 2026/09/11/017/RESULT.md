# Stage-2 Rokhlin tower table for a Z/3 coordinate-permutation block (dim ≤ 2 witness)

## Context

The Toms–Winter regularity program asks whether symmetry preserves or washes out
the irregularity (failure of strict comparison / Jiang–Su stability) of simple
nuclear non-Z-stable AH algebras. Covering theorems (Hirshberg–Winter–Zacharias;
Gardella; Gardella–Hirshberg–Santiago) show finite Rokhlin dimension with
commuting towers transfers regularity to crossed products, but assume the towers.
No published source gives a concrete commuting-tower bound for a Z/3
coordinate-permutation action on a Toms–Villadsen irregular AH base. The admitted
preset fallback asks for exactly one auditable datum: an explicit 9-contraction
tower table at fixed stage n0=2 with binary tolerances 0.01/0.01/0.05.

## Definitions

- Building block: X_1 = (S^2)^3, A_1 = M_2(C(X_1)),
  alpha_1 = id ⊗ sigma^* with sigma the cyclic shift of the three S^2 factors.
- Villadsen step: X_2 = X_1^3 with block projections pi_0, pi_1, pi_2,
  phi(f) = diag(f∘pi_0, f∘pi_1, f∘pi_2, f(x_0)), so A_2 = M_8(C(X_2)).
  Index blocks {0,1}, {2,3}, {4,5}; {6,7} is the point-evaluation corner.
- Action: tau = C ∘ D on the 9 position coordinates (C = block 3-cycle,
  D = diagonal inner shift; C, D commute, ord(tau) = 3); w the constant 8×8
  permutation unitary 0↦2, 1↦3, 2↦4, 3↦5, 4↦0, 5↦1, 6↦6, 7↦7 (w^3 = I).
  Stage-2 automorphism alpha_2 = Ad(w) ∘ tau^*, of exact order 3.
- Towers: for g ∈ Z/3 = {0,1,2}, l = 0,1,2 (three identical commuting towers),
  f_g^{(l)} = (1/3)·D_g + (99/1000)·P_c, constant in X_2, where D_g is the
  diagonal support projection on block g and P_c on the corner {6,7}.
  Each f_g^{(l)} is a positive contraction; all are diagonal, hence commuting.

## Result

For the fixed stage-n0=2 block above, the 9 explicit constant diagonal positive
contractions f_g^{(l)} satisfy:

- max equivariance error ‖alpha_2^h(f_g^{(l)}) − f_{g+h}^{(l)}‖ = 0 < 0.01
  (h = 1, 2; 18 checks);
- max orthogonality product ‖f_g^{(l)} f_{g'}^{(l)}‖ = (99/1000)^2
  = 9801/10^6 ≈ 0.0098 < 0.01 (g ≠ g'; 9 checks);
- uniform trace remainder tau(1 − Σ_{g,l} f_g^{(l)}) = 109/4000 = 0.02725 < 0.05
  for every extremal trace tau (constant towers ⇒ y-independent), hence on any
  fixed finite trace-simplex section;
- operator sum S = Σ_{g,l} f_g^{(l)} has eigenvalues 1 (×6) and 891/1000 (×2),
  i.e. S ≤ I: a genuine almost-cover from below.

Binary verdict: PASS.

## Proof / evidence

Exact rational arithmetic, no floating point. Equivariance: Ad(w) cycles the
three projection blocks D_g → D_{g+1} and fixes P_c, so
alpha_2(f_g) = f_{g+1} exactly (h = 2 by iteration). Orthogonality: D_g supports
are disjoint; products overlap only on the corner (c^2). Traces: per contraction
Tr = 2/3 + 2c; total Tr = 9(2/3 + 2c) = 6 + 18c = 7782/1000 at c = 99/1000;
normalized tr_8 = 3891/4000; remainder 109/4000, small and positive.
Replay: `python3 output/artifacts/verify_stage2_towers.py` → VERIFY_OK;
`python3 output/artifacts/verify_equivariant_step.py` certifies ord(tau) = 3,
C,D commutation, and the intertwining index identity.

## Limitations

- Finite-stage (n0=2) certificate only. Proves no limit Rokhlin-dimension bound
  dim_Rok^c(alpha) ≤ 2 and no Jiang–Su stability decision for C = A_T ⋊ Z/3.
- Uses three identical constant diagonal towers; permitted by the fallback's
  three inequality families, which impose no cross-tower constraints beyond them.
- The naive fixed-thread equivariant limit carries a character (non-simple), so
  promoting the table to the limit needs a simplicity-compatible redesign.
- Downstream use: concrete dim-≤2 data point at a fixed stage feeding
  HWZ/Gardella-type transfer inputs; any FAIL on re-evaluation localizes which
  tower property breaks.

## Reproducibility

Run `python3 output/artifacts/verify_stage2_towers.py` and
`python3 output/artifacts/verify_equivariant_step.py` from the record root;
both print VERIFY_OK using only exact rational/integer arithmetic (stdlib only).

## References

- Hirshberg–Winter–Zacharias, Rokhlin Dimension and C*-Dynamics.
- Gardella, Rokhlin dimension for compact group actions (arXiv:1407.1277).
- Gardella–Hirshberg–Santiago, Rokhlin dimension: duality, tracial properties,
  and crossed products.
- Hirshberg–Phillips, Rokhlin dimension: obstructions and permanence properties
  (arXiv:1410.6581).
