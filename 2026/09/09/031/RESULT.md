# Saxl containment for the staircase square at n=15: certified 176-constituent row

## Context
The Saxl conjecture (2012) asserts that at triangular n = k(k+1)/2, the
Kronecker square of the staircase partition rho(k) = (k,k-1,...,1) contains
every irreducible character of S_n. Proven families cover hooks and two-rows
(Pak-Panova-Vallejo), dominance-comparable constituents (Ikenmeyer), and
triple-hooks / Durfee size 3 (Li, with thresholds n_3=14, n_4=28), plus
splitting/modular theory (Bessenrodt-Bowman). No prior source certifies the
full containment row at the next triangular case n=15. This record settles
that finite case by exact computation.

## Definitions
- n=15, 15! = 1307674368000, p(15)=176.
- rho = (5,4,3,2,1) |- 15, the staircase partition; self-conjugate.
- chi^lam(mu): irreducible S_n character; |C| = class size of type mu;
  z_mu = 15!/|C|.
- Kronecker coefficient g(rho,rho,nu) = <chi^rho chi^rho, chi^nu>
  = sum_C |C| chi^rho(C)^2 chi^nu(C) / 15!.
- Class-sum certificate S_nu = sum_C |C| chi^rho(C)^2 chi^nu(C) = g_nu * 15!.

## Result
Let rho=(5,4,3,2,1) |- 15. Then for all 176 partitions nu of 15,
g(rho,rho,nu) >= 1. Hence chi^rho tensor chi^rho contains every irreducible
character of S_15; the Saxl conjecture holds at n=15.
Exact data: dim(rho)=292864; min g = 1 attained exactly at nu=(15) and
nu=(1^15); max g = 18269 at nu=rho; transpose symmetry g(nu)=g(nu^t) holds,
with exactly 4 self-conjugate nu: (8,1^7):292, (6,3^2,1^3):10340,
rho:18269, (4^3,3):1440. Degree identity: sum_nu g_nu dim(nu) = dim(rho)^2
= 85769322496. Full 176-entry (nu,g,S) table in artifacts/staircase_row.json.

## Proof / Evidence
Machine proof by exact integer arithmetic (not statistical evidence):
1. Full S_15 character table (176 x 176) computed from-scratch by
   Murnaghan-Nakayama recursion chi^lam(mu)=sum_H (-1)^ht(H) chi^{lam\H}(mu\mu_1)
   via beta-sets (mn_murnaghan_nakayama.py); no character-table library call.
2. Audits, independently recomputed by auditor: 176/176 dimensions match hook
   formula; sum dim^2=15!; 176/176 row norms sum_C chi^2|C|=15!; 176/176 column
   norms sum_lam chi^2=z_mu; sum class sizes = 15!.
3. 176 exact inner products g(rho,rho,nu); all quotients positive integers;
   all 176 class-sum certificates replay exactly (0/176 fails).
4. Independent second MN implementation (rim-strip walk, verify_independent.py)
   reproduces the table byte-identically (0/30976 mismatches); orthogonality,
   hook dimensions, and all 176 certificates replay: VERIFY_OK.

## Limitations
- Finite case n=15 only; no general proof of Saxl for n>15.
- Machine proof; no human-readable uniform reason for positivity.
- Both MN programs share the MN idea and one authorship; residual risk of a
  common conceptual slip, mitigated by four independent identities and
  self-checking integer certificates re-verifiable in GAP/Sage.
- No dominance-order / Durfee-size analysis performed.

## Reproducibility
- artifacts/mn_murnaghan_nakayama.py: MN + partition/class-size code.
- artifacts/chartable15.json: committed table, classes, dimensions.
- artifacts/staircase_row.json: 176 (nu,g,class_sum) entries.
- artifacts/verify_independent.py: independent MN + full replay; prints VERIFY_OK.
- Auditor reran verify_independent.py in inputs/artifacts with VERIFY_OK and
  recomputed all identities listed above.

## References
- Pak-Panova-Vallejo, Kronecker products, characters, partitions, and the tensor
  square conjectures, arXiv:1304.0738 (hooks, two-rows).
- Ikenmeyer, The Saxl Conjecture and the Dominance Order, arXiv:1410.6549
  (dominance-comparable constituents).
- Li, Saxl Conjecture for triple hooks, arXiv:1811.10967 (Durfee 3, n_3=14, n_4=28).
- Bessenrodt-Bowman, Splitting Kronecker squares, 2-decomposition numbers,
  Catalan Combinatorics, and the Saxl conjecture, arXiv:2202.03066.
