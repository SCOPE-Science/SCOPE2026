# Independent Audit — 2026/09/17/harmonic-resonance-critical-hardy-rellich--1d70aa9a6c53

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `8ed7932528496ad33202ee784bb34722564dbe69`
- Disposition: **PASSED**

## Correctness

**PASS** — The logarithmic-cutoff resonance calculation is correct. For a homogeneous harmonic h=r^beta Y, both |Delta(h eta(log r/L))|^N |x|^a and the critical left-hand density become scale invariant precisely at a=N(1-beta); the plateau contributes order L while transition errors are order L^(1-N). Taking h=x_1 gives beta=1 and therefore a=0, so the weighted inequality fails there; taking h=1 gives beta=0 and a=N. For the two harmonic exponents beta=m and beta=-(m+N-2), the claimed arithmetic resonance families follow. Inside -N<a<N(N-1), only a=0 and a=N remain, matching the record's corrected Muckenhoupt-range statement. This direct calculation also explains why the later 2026 published abstract claiming a=N as the unique critical weight cannot be correct for the stated Hessian/Laplacian functional.

## Originality

**PASS** — Classical weighted-Sobolev theory already ties exceptional Laplacian weights to homogeneous harmonic polynomials: McOwen's 1979 Theorem 0 describes Fredholm failures at arithmetic weight sequences. That broad resonance mechanism is therefore not new. The record's narrower contribution is nevertheless original relative to the located literature: it applies logarithmic harmonic cutoffs to the newly introduced critical Hardy-Rellich functional, identifies the missing a=0 obstruction, and resolves the open endpoint issue in Majdoub's recent extension. No pre-2026-09-17 source located states these exact counterexamples for this functional.

## Scientific value

**PASS** — The result corrects a live error in a very recent Hardy-Rellich line of work and supplies a reusable mechanism for detecting all harmonic resonances. It also cleanly separates the exact Muckenhoupt-range validity set from the much larger global failure lattice. The post-record journal article published on 2026-09-20 still advertises a=N as the unique critical weight, so the audited counterexample remains scientifically consequential.

## Sources

- A critical Hardy-Rellich inequality (Hernán Castro): https://arxiv.org/abs/2511.16537 — Introduces the critical functional; the current preprint literature is the immediate target of the correction.
- An extension of a critical Hardy--Rellich inequality: explicit constants and the sharp weight range (Mohamed Majdoub): https://arxiv.org/abs/2606.15668 — Recent extension claiming a=N as the unique critical weight and extending the Laplacian formulation to the Muckenhoupt range.
- The Behavior of the Laplacian on Weighted Sobolev Spaces (Robert C. McOwen): https://doi.org/10.1002/cpa.3160320604 — Full text independently checked via authorized Oxford access; Theorem 0 gives classical harmonic-polynomial exceptional weights for the weighted Laplacian.
- Sharp Weight Range for Critical Hardy–Rellich Inequalities (Mohamed Majdoub): https://doi.org/10.56947/5j6t3z94 — Published 2026-09-20, after this record; its abstract still states that the dimension weight is the unique critical value.

## Limitations

- The pass is for the resonance/counterexample theorem and corrected validity set, not for any new general Fredholm theory.
- McOwen's 1979 harmonic-weight framework substantially predates the general resonance idea; originality is limited to this critical Hardy-Rellich application.
- The post-record journal article is not treated as prior art because it was published after the 2026-09-17 record.

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was read only as evidence and no repository mutation was performed. Open-access/preprint sources were checked first. Authorized Oxford institutional access was used only for the McOwen full text after open-access retrieval attempts did not provide the needed theorem text.
