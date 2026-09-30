# Independent Audit — 2026-09-30

**Record:** `2026/09/20/linear-wise-independent-rademacher-bounded-stopping-bias--ffc9773418a4`  
**Title:** Square-root bounded-stopping bias under linear-wise independent Rademacher increments  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `b308d2b9445c84c071fb5cd8a93c0079d19abac8`  
**Disposition:** **PASSED**

## Three-axis assessment

- **Correctness — PASS:** The theorem package checks out independently. For any index K in the second block, S_{m+K}=S_m+R_K and pathwise min_j R_j <= R_K <= max_j R_j; E S_m=0 and the second block has the ordinary iid simple-walk law, giving the sharp two-block envelope. In the linear construction, the first m coordinate signs reveal U and hence the whole future block, so the first future maximizer is already F_m-measurable and T=m+K is a legitimate stopping time. A dependence among the coefficient vectors [I_m A] is exactly (Ay,y), so the least relation weight is d(A)=min_{y!=0}(wt(Ay)+wt(y)) and the family is (d(A)-1)-wise independent. The random-injective-map first-moment bound is valid because each fixed nonzero y maps uniformly to a nonzero m-bit vector; the entropy condition requires R<1/2 and R<1-h_2(delta), exactly as stated. I independently enumerated simple walks through ell=8 and reproduced the closed forms for E M_ell. Narayanan's published four-wise maximal second-moment theorem supplies the O(sqrt N) unrestricted upper bound once k>=4.
- **Originality — PASS:** The classical components are correctly delimited. Benjamini–Kozma–Romik construct k-wise/pairwise-independent random walks with unusual path behavior, and Narayanan determines maximal-moment phenomena including the four-wise O(sqrt N) scale; neither located source states the exact two-iid-block stopped-sum envelope, a future iid block completely revealed at the boundary, or the systematic-code realization preserving the endpoint at linear-wise independence. Focused searches for stopping-time bias under k-wise independence, orthogonal-array/code formulations, and predictable iid tails did not locate the filed theorem. Originality therefore passes to the best of the available literature, with a residual terminology risk in older orthogonal-array/resilient-function or stopping-counterexample literature.
- **Scientific value — PASS:** The result sharply quantifies why coordinate k-wise independence does not substitute for the conditional-mean property behind optional stopping. It gives both an exact extremal envelope in a natural two-block class and a global Theta_delta(sqrt N) consequence for every fixed independence fraction below one half, plus an explicit near-half-wise simplex family. This is a meaningful probabilistic/pseudorandomness boundary result.

## Independent findings
- For ell=1,...,8, direct enumeration gives E M_ell = 1/2,3/4,1,19/16,11/8,49/32,27/16,467/256, exactly matching the displayed central-binomial formulas.
- The future-maximizer rule is a stopping time because the entire future block is measurable at time m in the construction; it does not illegally use information unavailable to the natural filtration.
- The relation-code distance d(A) is exactly the circuit size of the character coefficient family [I_m A], so the k-wise-independence claim has no hidden sufficiency gap.
- The fixed-fraction construction uses R<1/2, ensuring ell<=m and hence the existence of injective A; the entropy inequality is h_2(delta)<1-R.

## Independent checks
- Re-derived the two-block envelope and the stopping-time measurability argument from first principles.
- Enumerated all 2^ell simple-walk paths for ell<=8 and checked the closed form for a_ell exactly.
- Re-derived the code relation criterion and the first-moment existence bound for an injective F_2-linear map.
- Checked the global upper-bound transfer from Narayanan's four-wise maximum-distance second-moment theorem by Cauchy–Schwarz.

## Literature evidence
- https://doi.org/10.1214/ECP.v11-1201 — Benjamini–Kozma–Romik (2006), k-wise-independent random-walk constructions; no exact bounded-stopping envelope located.
- https://doi.org/10.1002/rsa.21075 — Narayanan (2022), maximal moments for limited-independent walks; abstract explicitly gives the four-wise O(sqrt n) maximum-distance scale used for the upper bound.
- https://doi.org/10.2307/2038147 — Joffe (1971), classical globally dependent pairwise-independent families; background rather than the filed stopping theorem.

## Limitations
- The sharp constant a_ell is for the two-iid-block subclass, not for all k-wise-independent walks.
- The unrestricted fixed-fraction statement is order-sharp rather than constant-sharp.
- Originality remains qualified by the possibility of an equivalent older formulation under orthogonal arrays, resilient functions, or pseudorandom stopping rules.

The assigned source tree remained unchanged from the inventory/source-tree-check interval through current main commit `eff2c6312cec5b0dee5115e5f42211a853092dfb`; the exact tree audited is `b308d2b9445c84c071fb5cd8a93c0079d19abac8` and matches the assignment guard. GitHub was used only as read-only evidence; no repository writes were made. Audit timestamps and this audit-file date use UTC under the task-specific audit contract.
