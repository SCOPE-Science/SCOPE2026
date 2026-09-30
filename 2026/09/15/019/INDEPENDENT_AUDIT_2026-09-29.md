# Independent Audit — 2026/09/15/019

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `ee9d75ed769f2e99d947d05b599965fc7e46832f`
- Disposition: **REPAIRED**

## Correctness

**PASS** — After removing the finite-binomial-factorization assertion, the remaining theorem checks. Substitution in the Pascaleff–Tonkonog potential gives the critical point ρ=(1/k,…,1/k,1,…,1) with value n+1. The Newton vertices form an n-simplex of normalized volume k^(k-1)(n+1); exactly the k vertices in the distinguished K_k are incident to affine-length-k edges, while all other edges have length one. These invariants exclude the Clifford simplex and, using the Chanda–Hirschi–Wang description of lifted Vianna Newton simplices, exclude every lifted Vianna torus. The original clause claiming that this consequently rules out every finite sequence of k=2 binomial/solid mutations was not proved: Pascaleff–Tonkonog explicitly describe finite-binomial non-factorization for k>2 as an expectation, not a theorem. The repaired text states only the proved one-step non-binomial fact and makes no finite-composition claim.

## Originality

**PASS** — Pascaleff–Tonkonog supply the higher-dimensional mutated potential, and Chanda–Hirschi–Wang supply the lifted-Vianna Newton-polytope pattern, but the explicit all-(n,k) critical point together with the normalized-volume/long-edge comparison gives a concrete family-level separation of these PT tori from both Clifford and all lifted Vianna tori. The located sources do not state that combined rigidity calculation.

## Scientific value

**PASS** — The corrected theorem gives two useful pieces of structure for the PT family: a uniform Floer-theoretic non-displaceability certificate and an explicit Newton-polytope invariant separating it from the principal previously constructed higher-projective-space families. Removing the unsupported finite-wall conclusion leaves a precise, reusable comparison theorem without overstating what is known.

## Sources

- The wall-crossing formula and Lagrangian mutations (James Pascaleff; Dmitry Tonkonog): https://arxiv.org/abs/1711.03209 — Corollary 5.8 gives the higher-dimensional CP^n potentials; the paper says k>2 mutations are non-binomial and only expects, rather than proves, that no finite binomial composition connects the chambers.
- Infinitely many monotone Lagrangian tori in higher projective spaces (Sayantan Chanda; Joé Brendel/Hirschi context; Bing Wang): https://arxiv.org/abs/2307.06934 — Provides the lifted Vianna family and its Markov Newton-simplex edge pattern used in the separation argument.

## Limitations

- The repaired theorem does not claim that the k>2 PT transformation is impossible to express as a finite composition of arbitrary binomial/solid mutations.
- The argument takes the PT existence/monotonicity/wall-crossing theorem and the standard Floer critical-point criterion as inputs.

## Repair applied

- Removed the unsupported claim that the k>2 wall-crossing cannot be realized by any finite sequence of k=2/binomial/solid mutations.
- Replaced `RESULT.md` and `SLOGAN.txt` with complete corrected text retaining the proved non-displaceability and Newton-polytope separation statements.
- The repaired record expressly distinguishes the proved one-step non-binomial statement from Pascaleff-Tonkonog's conjectural finite-wall expectation.

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was read only as evidence. Open-access/preprint sources were checked first; Oxford Download was not needed.
