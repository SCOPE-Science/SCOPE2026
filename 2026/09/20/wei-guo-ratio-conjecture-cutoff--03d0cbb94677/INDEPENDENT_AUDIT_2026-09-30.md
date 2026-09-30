# Independent audit — 2026-09-30

**Record:** `2026/09/20/wei-guo-ratio-conjecture-cutoff--03d0cbb94677`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Assigned/current source tree:** `5c8169bc786e8dcc2b68bbb6c44cdd46419e0afb`  
**Disposition:** passed

## Correctness — PASS

PASS. Substitution q=e^{-t} gives F_i=A_{i+1}(q)/((1-q)A_i(q)) with the stated Eulerian normalization. The Eulerian recurrence implies monicity, constant term one, simple negative roots, and nonvanishing of A_{i+1} at roots of A_i. For i>=3, the product of root moduli is one and there are at least two distinct negative roots, so at least one root lies in (-1,0). It produces a genuine pole at z=-log(-r)-i*pi with positive real part. By Hausdorff--Bernstein--Widder, a completely monotone function is a Laplace transform; finiteness for every positive real argument makes that transform holomorphic on Re z>0, so agreement on the positive axis with the meromorphic Eulerian quotient is incompatible with an interior genuine pole. The explicit positive discrete Laplace expansions for i=0,1,2 are correct. For i=3, r=-2+sqrt(3) gives the stated pole log(2+sqrt(3))-i*pi.

## Originality — PASS

PASS. Wei and Guo's open-access 2014 article was inspected directly: Section 5 states Conjecture 12 that the two ratio families are completely monotone for every nonnegative index. Targeted searches by conjecture number, exact negative-order polylogarithm ratio, Eulerian quotient, and complete-monotonicity terminology did not locate a published cutoff or all-i>=3 pole obstruction. Later Eulerian real-rootedness work supplies background root geometry rather than a resolution of this conjecture. No specific inaccessible paper emerged as a likely covering source; the remaining risk is only a differently phrased or poorly indexed observation.

## Scientific value — PASS

PASS. This is a complete resolution of a named conjecture, not merely a first counterexample: it identifies exactly i=0,1,2 as the positive cases and gives one structural obstruction covering every i>=3. The pole/half-plane-holomorphy method is concise and reusable for related rational functions after exponential substitution.

## Findings

- The source paper explicitly states the all-index assertion as Conjecture 12.
- For every i>=3, a denominator Eulerian root in (-1,0) yields a nonremovable pole in the right half-plane.
- The three surviving indices have explicit positive discrete Laplace-series representations.

## Independent checks

- Re-derived the Eulerian quotient and recurrence indexing through A_3 and A_4.
- Reproved the root-in-(-1,0) lemma from monicity, constant term, and simplicity.
- Checked holomorphy of the representing Laplace transform on every smaller right half-plane via exponential domination of derivatives.
- Expanded the i=0,1,2 cases coefficient-by-coefficient as nonnegative exponential sums.

## Literature evidence

- https://doi.org/10.1155/2014/851213 — Wei and Guo (2014), open-access source; Section 5 explicitly states Conjecture 12 for all indices.
- https://doi.org/10.1112/jlms.70083 — Athanasiadis (2025), modern Eulerian real-rootedness context; does not resolve the Wei--Guo ratio conjecture.

## Limitations

- The proof does not identify the first derivative order or first real t witnessing a sign failure for each i>=3.
- Stronger notions such as logarithmic complete monotonicity are not classified.
- A differently phrased, unpublished, or poorly indexed prior observation remains possible.

No GitHub write was performed by this audit. The guarded change set only stages this audit evidence and updates the independent-audit channel in `VERIFICATION.md`; it leaves the research claim files unchanged.
