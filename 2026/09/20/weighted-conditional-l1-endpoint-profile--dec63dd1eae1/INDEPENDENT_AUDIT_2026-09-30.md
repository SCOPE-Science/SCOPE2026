# Independent Audit — Exact L1 endpoint profile for weighted conditional expectation operators

**Audit date:** 2026-09-30 (UTC) (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `441857670bd8daf43dc5b8881dac09ce9421e5c8`  
**Audited current source tree:** `441857670bd8daf43dc5b8881dac09ce9421e5c8`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` directory tree exactly matches the assigned source tree. GitHub was used read-only, and the dated independent-audit files were absent when this guarded change set was prepared.

## Correctness — PASS

PASS. On an A-atom A_n the operator is rank one with exact norm c_n=E(|w|)(A_n)||u chi_{A_n}||_infinity; this is the L1-dual norm of f↦int_{A_n}uf and not the average E(|u|)(A_n). The L1 direct-sum decomposition therefore gives the finite-rank truncation upper bound. Disjoint near-norming vectors on k large atomic blocks, or k disjoint A-measurable pieces of the non-atomic block, give the matching Bernstein lower bound and hence a_k=b_k=max(gamma,c_k^*). The countable version supplies a 1-complemented l1 subspace on which T is bounded below, proving the exact compact/FSS/SS distances. The atomic rank-one expansion gives the nuclear upper bound, while finite diagonal compressions and the trace pairing give the reverse nuclear-norm inequality. The two displayed source counterexamples are valid.

## Originality — PASS

PASS, with unusually strong source-specific evidence. The current arXiv text of Al Ghafri–Shamsigamchi–Estaremi explicitly states the L1 nuclear series using E(|w|)(A_n)E(|u|)(A_n), and its Proposition 2.6 proof explicitly bounds the functional phi_n(f)=int u f by E(|u|)(A_n). On L1 the exact norm is ||u chi_{A_n}||_infinity, so the submitted correction addresses a concrete published/preprint endpoint error rather than merely proposing a new notation. The older 2013/2014 compactness literature gives the prior boundedness/compactness framework. No inspected source gives the corrected all-k approximation/Bernstein profile, the common compact/FSS/SS distance, or the exact corrected nuclear norm. General multiplication–conditional-expectation representation theory is prior input and receives no novelty credit.

## Scientific value — PASS

PASS. The corrected L1 block invariant simultaneously repairs the endpoint compactness/nuclearity picture and yields a complete quantitative profile: all approximation/Bernstein numbers, three ideal distances, complemented-l1 obstructions, and the exact nuclear norm. The elementary counterexamples make the failure mode of the average-based criterion transparent and reusable.

## Independent checks

- Re-derived the exact atomic rank-one block norm from (L1)^*=L-infinity.
- Checked the non-atomic lower-witness construction by restricting the measure C↦mu(C intersect {|qu|>t}) to the A-nonatomic part and splitting it into disjoint positive A-measurable pieces.
- Reconstructed the contractive projection onto the disjoint l1 witness and the strict-singularity distance argument.
- Reconstructed the nuclear lower bound by finite l1 diagonal compression and the trace inequality.
- Read the open arXiv full text of arXiv:2602.19105. Its lines for Proposition 2.6 explicitly use ||phi_n||<=E(|u|)(A_n), and Theorem 2.9 states the corresponding average-based L1 nuclear series.
- Checked the trivial-conditioning rank-one compactness counterexample and the growing-block example where the average criterion converges but the operator fixes a complemented l1.
- GitHub current main has exactly the assigned directory tree SHA; the dated audit files are absent and VERIFICATION.md retains the verified blob SHA.

## Limitations

- The theorem is specific to the same-space L1 endpoint and does not revise the distinct reflexive-Lp theory.
- General multiplication–conditional-expectation representation results may encode parts of the block decomposition abstractly; novelty is restricted to the corrected endpoint profile and exact quantitative consequences.
- The audit evaluates the mathematics of the current public arXiv version; later source revisions could correct the cited endpoint statements.

## Evidence and references

- https://arxiv.org/abs/2602.19105
- https://doi.org/10.7153/oam-07-05
- https://doi.org/10.1007/s11117-013-0229-5
- https://jot.theta.ro/jot/archive/2002-048-001/2002-048-001-002.html
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/20/weighted-conditional-l1-endpoint-profile--dec63dd1eae1

This guarded change set changes only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
