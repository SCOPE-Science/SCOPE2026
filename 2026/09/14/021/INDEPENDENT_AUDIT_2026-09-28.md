# Independent Audit — 2026/09/14/021

- Audit date: 2026-09-28 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `4d883e15776909eb92e4b12512c49bfaf9643cdf`
- Disposition: **PASSED**

## Correctness

**PASS** — The exact two-patch computation checks. At m=1 the stated transition matrices invert to V_E^{-1}=[[1/5,1/10],[0,1/6]] and V_I^{-1}=[[1/6,0],[1/6,1/3]], and multiplication gives H=[[1/10,1/20],[1/5,19/90]]. Its trace is 14/45, determinant 1/90, and discriminant 106/2025, so the Perron root is about 0.269951446, strictly larger than the largest isolated value 2/9. The movement generators have zero column sums and the M-matrix inverses are nonnegative, so the example falls within the stated next-generation-matrix setup and is a valid counterexample to universal upper bracketing.

## Originality

**PASS** — Earlier multipatch literature already shows that mobility can increase, decrease, or nonmonotonically change R0, and even that a connected system can persist when isolated patches do not, but the located sources use different compartment/group structures or additional travel mechanisms. I did not find a prior theorem or counterexample giving this exact stage-specific two-patch SEIR relay mechanism with opposite exposed and infectious movement matrices. The record's exact rational example therefore adds a genuinely model-specific obstruction rather than merely restating the nearby general phenomenon.

## Scientific value

**PASS** — A two-patch rational counterexample is a useful structural result because it invalidates a plausible universal spectral-radius bracketing claim under very small heterogeneous data and identifies the mechanism: progression and movement can route exposed and infectious stages through different favorable patches. It gives a compact regression test for any future sufficient-condition theorem and cleanly separates unrestricted stage-specific movement from settings where monotonicity or bracketing can be proved.

## Sources

- Travel Frequency and Infectious Diseases (Daozhou Gao): https://doi.org/10.1137/18M1211957 — Nearby prior result: R0 can increase, decrease, or vary nonmonotonically with movement, and connectivity can change persistence relative to isolated patches.
- The construction of next-generation matrices for compartmental epidemic models (O. Diekmann; J. A. P. Heesterbeek; M. G. Roberts): https://pmc.ncbi.nlm.nih.gov/articles/PMC2871801/ — Standard next-generation-matrix framework used to interpret the reduced spectral-radius calculation.

## Limitations

- The audit establishes the advertised failure of universal upper bracketing; it does not characterize sufficient hypotheses restoring a bracket.
- The large-coupling limit and global monotonicity in m are not needed for the counterexample and were not separately classified.

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was read only as evidence. Open-access/preprint sources were checked first; Oxford Download was not needed.
