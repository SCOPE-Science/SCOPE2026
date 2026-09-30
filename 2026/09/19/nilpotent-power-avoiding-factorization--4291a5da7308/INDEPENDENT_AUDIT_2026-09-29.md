# Independent audit — 2026-09-30

Record: `2026/09/19/nilpotent-power-avoiding-factorization--4291a5da7308`  
Assigned and audited source tree: `eee543e82bddbc54010a78e0f35d46d119d7949c`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Current RESULT.md blob: `0813c333414750251a5d2216b6874627f9a0f10e`  
Disposition: **passed**

## Correctness

**independently_supported**. The nilpotent factorization is correct. Writing G=P×H with P supported on primes dividing k and H coprime to k, every P-vertex flows to 1 while h↦h^k permutes H. Over a directed H-cycle of length r, the vertices over each cycle position form a copy of the same rooted P-tree T, with the H-coordinate shifted by the P-depth. If A=α(T\{1}) and ε=α(T)-A, then ε∈{0,1}; excluding every root gives rA, and when ε=1 the additional selectable roots form an independent set on the r-cycle, contributing floor(r/2), including zero for a loop. Summing gives s_k(G)=|H|A+εs_k(H). For an H-element of order d, the power-map cycle length is ord_d(k), giving the stated order-spectrum formula. On C_{p^a}, the rooted levels have sizes φ(p^j); alternating-level matchings prove the displayed A_p(a) formulas and the parity value of ε. Independent exact functional-graph optimization on small cyclic groups and the committed 600-case verifier are consistent with the closed formula, including s_2(C_20)=12.

## Originality

**qualified_with_inaccessible_structural_prior**. Blackburn–Hart–McVeagh introduce the power-avoiding invariant and focus on groups with very large avoiding sets; Qureshi–Reis and later Fernandes/Qureshi/Reis/Ribas provide prior functional-graph structure and invariants. Targeted searches did not locate the exact independent-set factorization, the coprime order-spectrum expression, or the all-n cyclic prime-power formula in those accessible sources. The most relevant older nilpotent structural paper, Fernandes–Reis (Discrete Mathematics 347 (2024), 114000), was not available through open-access routes; authorized institutional retrieval stopped at a human-verification gate and was not bypassed. McVeagh's 2026 thesis likewise was not available in a form that could be fully inspected. Originality is therefore supported only for the optimization formulas, with those inaccessible sources retained as explicit residual prior-art risks.

## Scientific value

**meaningful_exact_reduction**. The theorem separates the genuinely primary difficulty from an explicit coprime cycle term for every finite nilpotent group, and it completely evaluates the cyclic group under prime powering. This converts a recently emphasized extremal invariant into a computable structural formula well outside the near-|G| regime, while appropriately not claiming a closed group-theoretic expression for the nonabelian primary tree statistic.

## Literature and evidence checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/19/nilpotent-power-avoiding-factorization--4291a5da7308
- https://arxiv.org/abs/2609.18513
- https://arxiv.org/abs/2107.00584
- https://doi.org/10.1016/j.disc.2024.114000
- https://arxiv.org/abs/2609.20516
## Literature access note

The prior source `10.1016/j.disc.2024.114000` was not available as lawful open full text. Authorized institutional retrieval reached a publisher human-verification gate; it was not bypassed. It is **not** claimed to have been read in full.

## Limitations

- For a general nonabelian primary Hall factor P, the rooted-tree statistics A and ε are not evaluated in closed group-theoretic form.
- Power-map functional-graph structure is prior art; novelty is confined to the exact optimization and closed cyclic formulas.
- Fernandes–Reis (2024) could not be read in full because authorized retrieval required human verification; no claim is made about inaccessible theorem text there.
- McVeagh's 2026 thesis was not fully inspected and remains a residual prior-art risk.
