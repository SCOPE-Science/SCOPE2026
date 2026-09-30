# Independent Audit — Prime-square local rigidity for 31 unresolved exponents in the Lebesgue–Nagell equation

**Audit date:** 2026-09-30 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `0d18beb80832e6eb5e05966dadfb4ef67c0435ef`  
**Audited current source tree:** `0d18beb80832e6eb5e05966dadfb4ef67c0435ef`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` directory tree exactly matches the assigned source-tree SHA. GitHub was used only as read-only evidence. The dated independent-audit marker files were absent when this guarded change set was prepared.

## Correctness — PASS

PASS. Katz–Pratt’s full text confirms the required ingredients: the reduction to the single r=1 Thue equation for the relevant range, Theorem 7.7 giving x-1 congruent to (2/p)b mod p, Theorem 2.3 upgrading y congruent -1 mod p to x congruent ±1 mod p^2, and Conjecture 8.1 as the local-triviality target. Modulo p, only the endpoint terms of F_p survive, giving a+(2/p)b congruent 1. Every coefficient of both partial derivatives is divisible by p, so translating (a,b) by multiples of p leaves F_p unchanged mod p^2. I independently recomputed the p candidate residue classes for all 84 unresolved primes using exact arithmetic in (Z/p^2Z)[sqrt(2)]; the unique surviving class was (1,0) for exactly the 31 primes listed in the record, with no discrepancy.

## Originality — PASS

PASS. Katz–Pratt explicitly formulate local triviality as Conjecture 8.1 and describe only modest progress in Section 8. Their Theorem 10.1 leaves the q=p, s>1 solution count as p^s d with an unspecified positive integer d; it does not identify the 31 primes for which the normalized p^2 branch is uniquely trivial. Targeted searches found no prior prime-square classification or the same 31-prime list. The novelty is the finite exact p^2 specialization and its consequence for those unresolved exponents, not the Thue reduction or Katz–Pratt congruence lemmas.

## Scientific value — PASS

PASS. The result proves the source paper’s local-triviality conjecture for 31 of the 84 exponents left after the global reductions. It is a meaningful exact partial advance and is fully reproducible, while correctly stopping short of claiming that any of the corresponding global Diophantine equations has been solved.

## Independent checks

- After arXiv/open-access attempts did not expose the full article text, used authorized Oxford institutional retrieval for Katz–Pratt and read the relevant reduction, Theorems 2.3, 5.3, 7.7, Conjecture 8.1, Proposition 8.2 and Theorem 10.1 discussion.
- Reproved the mod-p affine condition and the mod-p^2 translation invariance of F_p.
- Independently tested all 84 residual exponents 17<=p<=911 with p congruent 13,17,19,23 mod 24 using exact quadratic-ring binary exponentiation; precisely the submitted 31 primes had unique residue class (1,0).
- Checked that the source’s Theorem 10.1 does not compute the relevant positive integer d for q=p,s>1 and therefore does not already state the 31-prime result.
- Rechecked the final implication from b congruent 0 to x congruent ±1 mod p, y congruent -1 mod p, and then x congruent ±1 mod p^2.
- Current main directory tree exactly equals the assigned tree; audit markers are absent and VERIFICATION.md retains the verified blob SHA.

## Limitations

- The theorem is local and does not rule out nontrivial integer solutions for any of the 31 exponents.
- The other 53 residual exponents retain multiple compatible residue classes modulo p^2 under this test.
- The 31-prime list is computer-assisted, though the reduction is proved and the audit independently reproduced the entire finite computation exactly.

## Evidence and references

- https://doi.org/10.1007/s11139-026-01334-4
- https://arxiv.org/abs/2507.12397
- https://arxiv.org/abs/2001.09617
- https://doi.org/10.1112/S146115701200006X
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/20/lebesgue-nagell-local-triviality-prime-square--017777632623

This guarded change set updates only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
