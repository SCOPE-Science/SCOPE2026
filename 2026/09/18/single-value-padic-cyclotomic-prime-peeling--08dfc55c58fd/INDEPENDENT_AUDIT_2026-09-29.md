# Independent audit — Single-value p-adic peeling of cyclotomic index radicals

**Audit date:** 2026-09-29 (UTC)  
**Source path:** `2026/09/18/single-value-padic-cyclotomic-prime-peeling--08dfc55c58fd`  
**Audited tree:** `667a08b781c4e6061e6d5db60bcd4197f0f98ef3`

## Disposition

**PASSED.** All three required axes pass. Publication may remain in the validated record set.

## Correctness

**PASS.** The p-adic recursion follows correctly from radical reduction and the squarefree Möbius product. After canceling all divisor factors supported on the recovered prefix, the unique smallest remaining exponent is the next prime p_{j+1}; every denominator is an l-adic unit because l divides x. The first coefficient also gives the sign mu(r) modulo an odd l, or modulo 4 when l=2 and a v_l(x)>=2. Independent exact tests over n<80 at bases 3,4,5 reproduced every prime support.

## Originality

**PASS.** This record substantially overlaps the earlier same-day SCOPE record 'Higher local cyclotomic prime extraction' (commit a584bf9c..., 2026-09-18 06:15:07Z): after radical reduction, its corrected prefix residual is algebraically the same j>=1 mechanism. The later record nevertheless adds a genuine j=0 normalization that extracts the first prime once mu(r) is recovered, gives the simple sign-recovery congruence from the one target value, and thereby closes an all-local single-target recursion for arbitrary n, including nonsquarefree binary indices. The originality pass is strictly limited to those additions; the higher-prefix mechanism is prior.

## Scientific Value

**PASS.** The incremental value is modest but real: it turns a higher-prime residual identity that presupposes a recovered prefix into a complete local recursion from one labeled cyclotomic value, and covers the nonsquarefree binary case where the unnormalized plus-extractor is uninformative. It should not be presented as an independently new higher-prime peeling mechanism.

## Independent checks

- Re-derived Phi_n(X)=Phi_rad(n)(X^{n/rad(n)}) and v_l(Phi_n(x)-1)=(n/rad(n))v_l(x).
- Verified that for every recovered prefix P_j the normalization leaves the unique smallest uncancelled exponent p_{j+1}, giving v_l(R_j-1)=a w p_{j+1}.
- Checked all denominators 1-x^{ad} are l-adic units.
- Verified U=(C-1)/x^a is congruent to -mu(r) modulo odd l, and modulo 4 under the stated binary hypothesis.
- Independent SymPy/rational-arithmetic replay for every 2<=n<80 at x=3,4,5 recovered exactly the sorted prime support.
- Compared with the earlier SCOPE record higher-local-cyclotomic-prime-extraction--01e648b0fd33 and isolated the genuinely new j=0/sign-recovery completion.

## Literature and prior-art boundary

- https://arxiv.org/abs/2609.18480 — Joseph M. Shunia (2026), Cyclotomic Prime Extractors; gives the radical valuation and binary least-prime/successive extraction mechanisms.
- https://arxiv.org/abs/1903.01962 — Pomerance and Rubinstein-Salzedo, classical cyclotomic Möbius-product/radical-reduction background.
- https://github.com/SCOPE-Science/SCOPE2026/commit/a584bf9c5219b31b4d59d77237508ff57017bc30 — Earlier same-day SCOPE publication of the equivalent higher-prefix local residual mechanism; originality of the assigned record is therefore narrowed to the first-step/sign-recovery completion.

## Limitations

- The higher-prime j>=1 residual identity is not original relative to the earlier same-day SCOPE record and must not be advertised as such.
- The recursion assumes n and x are already known; it is not an inversion algorithm for an unlabeled integer and does not claim practical integer-factorization efficiency.
- The binary sign step excludes squarefree n at x=2; that regime needs the separate least-prime extractor.

## Repository identity

The assigned source-tree SHA `667a08b781c4e6061e6d5db60bcd4197f0f98ef3` exactly matched the current tree at the audited path on `main`; no stale-tree substitution was used. GitHub was read only during this audit.
