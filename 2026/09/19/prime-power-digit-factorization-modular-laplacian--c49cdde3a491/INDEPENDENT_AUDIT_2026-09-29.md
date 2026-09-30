# Independent audit — Prime-power digit factorization in modular Laplacian dynamics

**Audit date:** 2026-09-29 (UTC)  
**Source path:** `2026/09/19/prime-power-digit-factorization-modular-laplacian--c49cdde3a491`  
**Audited tree:** `245250c4e7d3cc0aec21b4717b5d38132824c1e8`

## Disposition

**PASSED.** Correctness, originality on the stated boundary, and scientific value all pass. The record may remain in the validated set.

## Correctness

**PASS.** The prime-power renormalization is algebraically correct. If A=B mod p^k in a commutative integer algebra, factoring A^p-B^p shows an extra factor p in the geometric sum modulo p, hence A^p=B^p mod p^{k+1}. Starting from Frobenius P^q=D_q(P) mod p with q=p^{n-r+1} and iterating this lift r-1 times gives P^{p^n}=D_q(P^{p^{r-1}}) mod p^r. Writing t=t_<+sum_j d_j p^{r-1+j} and applying the special-time identity factor by factor proves the digit factorization; multiplying by P^s gives the epoch identity. Negative Laurent exponents cause no issue because D_q is a ring endomorphism. The saved verifier reports all special-time, arbitrary-time, and epoch checks passed for several asymmetric and Laplacian masks modulo 4, 8, and 9.

## Originality

**PASS.** The elementary p-adic lifting lemma, Frobenius, prime-power binomial congruences, and additive cellular automata over finite rings are prior art and are not treated as discoveries. On the deliberately narrow boundary claimed by the record, the contribution is the explicit source-model formula identifying the fixed depth kernel P^{p^{r-1}}, the complete base-p digit factorization of every constant-modulus time, and the all-seed epoch superposition law that rigorously explains the source paper's computational prime-power signatures. Repository searches found no earlier SCOPE record with this package, and targeted searches of the source-model and additive-CA literature did not locate an indexed source stating these same dynamical consequences.

## Scientific value

**PASS.** The result closes a concrete gap between prime-modulus Frobenius theory and the source paper's computational observations for moduli 4, 8, and 9. The arbitrary-time digit factorization is stronger than isolated recurrence snapshots: it gives a compact multiscale description of the full constant-modulus orbit and an exact finite-seed epoch identity, while correctly separating algebraic superposition from geometric disjoint-copy claims.

## Independent checks

- Reproved the p-adic lifting lemma and iterated it from ordinary Frobenius to modulus p^r.
- Derived the arbitrary-time factorization directly from the base-p expansion and checked the epoch identity by commutativity.
- Inspected the repository verifier and its saved output: all listed special-time, digit-factorization, and full-epoch tests pass for moduli 4, 8, and 9.
- Checked the source-paper abstract and older additive-cellular-automaton coverage to keep the novelty claim limited to the source-specific dynamical formulation rather than the underlying algebra.

## Literature and repository prior-art boundary

- https://arxiv.org/abs/2609.20416 — Nowak-Kępczyk, Long-Lived Carpet-Like Transients in Time-Dependent Modular Discrete Laplacian Dynamics; reports computational prime/prime-power modular signatures motivating the exact formulas.
- https://arxiv.org/abs/2511.17389 — Earlier Nowak-Kępczyk Frobenius-revival work; prime-field recurrence and empirical prime-power ladders are treated as prior context.
- https://doi.org/10.1016/S0167-2789(97)00074-2 — R. A. Dow, Additive cellular automata and global injectivity, Physica D 110 (1997), on additive cellular automata over finite commutative rings.

## Limitations

- The theorem concerns constant-modulus linear dynamics, not the genuinely time-dependent modulus schedules central to part of the source paper.
- Geometric replica statements require separated supports; the exact algebraic superposition law itself allows cancellation on overlap.
- Broad older additive-cellular-automaton and prime-power congruence literature remains a residual priority risk, so no broad first-discovery claim for the underlying polynomial congruence is warranted.

## Repository identity

The assigned source-tree SHA `245250c4e7d3cc0aec21b4717b5d38132824c1e8` matched the current tree at the audited path after comparison at inventory commit `e9ed144c13b7834896a844cc4f9cac3c25a168a6`, source-tree checked commit `253a0fe5d0217455660a277f9adb940030e567ad`, and current `main`. GitHub was read only during this audit.
