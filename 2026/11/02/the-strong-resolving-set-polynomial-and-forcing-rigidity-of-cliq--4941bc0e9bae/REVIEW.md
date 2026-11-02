# Scientific review

**Correctness: PASS.** The proof explicitly uses the published MMD/vertex-cover correspondence, computes the cycle MMD graph and independent-set polynomial through a transfer matrix, and checks the equality structures separately for even cycles, odd cycles of length at least five, and the exceptional triangle. The forcing-number deductions use the classified minimum bases. An independent direct-definition finite computation checks all polynomial coefficients and the forcing cases listed in RESULT.md. Risk: no independent review and finite tests cannot prove an infinite formula.

**Originality: PASS, subject to a stated priority risk.** The scalar strong dimension is credited to the 2013 product theorem [1], and the forcing invariant is credited to the 2017 source [2]. The novel candidate is a complete cardinality polynomial, all optimal bases, and the forcing law for the clique–cycle Cartesian family. The general enumeration framework of 2023 [3] does not provide this family-specific evaluated formula. A potentially equivalent prior independence-polynomial formula of the categorical product would imply the all-set result; targeted equivalent-formulation searches did not find one, but a missed earlier source remains possible.

**Mathematical value: PASS.** The family \(K_q\square C_n\) is a natural repeated-clique cyclic network; its full strong-resolving-set polynomial enumerates all redundant landmark deployments rather than only the minimum. The full optimizer census and parity/exception forcing law quantify minimum-set rigidity and robust reconstruction, a meaningful extension of the known scalar dimension.

**Nearest literature and limitations.** [1] Rodríguez-Velázquez et al. (2013) provides the MMD product mechanism and known dimension; [2] Lenin et al. (2017) defines forcing and solves the single-cycle case; [3] Bergougnoux et al. (2023) treats general minimal-set enumeration. The result assumes \(q\ge3,n\ge3\); there is no claim for arbitrary products or independent certification of publication priority.

Self-review: passed. Independent audit: not yet performed.
