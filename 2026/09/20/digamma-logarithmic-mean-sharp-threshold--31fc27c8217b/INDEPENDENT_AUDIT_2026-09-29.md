# Independent audit — Sharp two-sided threshold for a digamma logarithmic-mean inequality

**Audit date:** 2026-09-29 (UTC) (UTC)  
**Source path:** `2026/09/20/digamma-logarithmic-mean-sharp-threshold--31fc27c8217b`  
**Assigned and audited tree:** `d0e92c509660cc4b58e15c8290661b82a03fc761`  
**Repository snapshot:** `SCOPE-Science/SCOPE2026` at inventory commit `e9ed144c13b7834896a844cc4f9cac3c25a168a6`

## Disposition

**PASSED.** The claim survives independent review without a substantive research-file edit.

## Correctness

PASS. The two imported Alzer–Kwong inputs were checked against the source: 5ψ'(x)+3xψ''(x) is negative below its unique zero α0≈0.5615593996, and for fixed t>1 the normalized function U(a,t) is strictly increasing in a. From the sign inequality, P(x)=xψ'(x) satisfies d log P/d log x<-2/3 below α0; after x=α0e^{-s}, this yields the strict t^(1/3) comparison between adjacent logarithmic ψ-increments. The remaining coefficient bound (t-Λ)/(Λ-1)<t^(1/3) reduces with t=r^3 to H'(r)=(r-1)^4(r^2+r+1)/(3r^2(r^2+1)^2)>0. These combine with U-monotonicity to give F(a,b)<0 for b≤α0. Numerical evaluations on both sides of α0 independently confirm the sign change.

## Originality

PASS with normal priority uncertainty. Matejíčka (2018) explicitly posed the best-endpoint problem, recording only a smaller admissible lower-side range, while Alzer–Kwong (2023) establish the complementary large-parameter endpoint and the structural lemmas used here. Targeted searches for b0=α0, the exact α0 equation, and the logarithmic-mean formulation did not locate a prior published solution of the missing small-parameter half, and no obvious SCOPE duplicate was found. A differently phrased or poorly indexed solution remains possible.

## Scientific value

PASS. The result closes a named 2018 sharp-constant problem by identifying both endpoints with the same transition constant α0, and the proof isolates a reusable logarithmic-growth comparison for xψ'(x).

## Independent checks

- Verified the source lemma that 5ψ'+3xψ'' changes sign at α0 and the source theorem/argument giving strict increase of U(a,t) in a.
- Symbolically differentiated the auxiliary coefficient function and obtained exactly (r-1)^4(r^2+r+1)/(3r^2(r^2+1)^2).
- Numerically solved for α0=0.5615593996797983 and evaluated representative F(a,b): negative when b≤α0 and positive for α0≤a<b.
- Checked current main-path tree identity against the assignment snapshot.

## Literature and evidence

- https://doi.org/10.1186/s13660-018-1936-z — Matejíčka (2018), source of Open Problem 2 asking for the best endpoint constants.
- https://doi.org/10.1007/s10476-023-0206-6 — Alzer and Kwong (2023), source for the α0 sign lemma, monotonicity input, and sharp large-parameter direction.
- https://www.researchgate.net/publication/368935837_Mean_Value_Inequalities_for_the_Digamma_Function — Accessible full-text copy used to inspect the stated structural lemmas.

## Limitations

- The proof imports two published Alzer–Kwong lemmas rather than re-proving them from first principles.
- The sign in the mixed region a<α0<b is not classified.
- Originality is necessarily literature-bounded; an unindexed solution to the 2018 problem cannot be excluded absolutely.

## Repository guard

The current `main` record tree was checked against the assignment and is unchanged at `d0e92c509660cc4b58e15c8290661b82a03fc761`. This audit changes only the independent-audit channel in `VERIFICATION.md`; Lean and expert-attestation channels remain byte-for-byte semantically identical to the pre-audit file.
