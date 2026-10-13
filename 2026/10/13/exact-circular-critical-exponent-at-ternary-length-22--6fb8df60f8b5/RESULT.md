# Exact circular critical exponent at ternary length \(22\)
## Finding
For a ternary circular word \((w)\), define its circular critical exponent \(\operatorname{CE}_\circ(w)\) to be the maximum exponent of a factor of any conjugate of \(w\). Among all ternary words of length \(22\),
\[
\min_{|w|=22} \operatorname{CE}_\circ(w)=\frac{20}{11}.
\]
Exactly \(132\) labeled length-\(22\) words attain this minimum. Up to rotation there are exactly six circular words, represented by
\[
\begin{aligned}
&\mathtt{0102012021201020121012},\\
&\mathtt{0102012021201210120212},\\
&\mathtt{0102012101202120121012},\\
&\mathtt{0102101210201021202102},\\
&\mathtt{0102101210212021012102},\\
&\mathtt{0102120210121021202102}.
\end{aligned}
\]
These six rotation classes form one orbit under permutations of the three letters together with reversal.

For the first representative, two factors attaining exponent \(\frac{20}{11}\) are
\[
\mathtt{12010201210120102012}
\quad\text{and}\quad
\mathtt{12010201202120102012},
\]
each of length \(20\) and least period \(11\).

## Assumptions and scope
A nonempty word of length \(L\) and least period \(p\) has exponent \(L/p\). A circular word \((w)\) is the set of conjugates of \(w\), and a factor of \((w)\) is a factor of some conjugate. Thus a factor considered here has length at most \(|w|\); no repeated winding around the circle is allowed.

The result concerns the ternary alphabet \(\{0,1,2\}\) at the single distinguished length \(22\). It does not claim a formula for the minimum circular critical exponent at other lengths.

## Proof
First generate every ternary length-\(22\) word whose linear factors all have exponent at most \(\frac{20}{11}\). The property is factorial, so exhaustive prefix extension is complete. When a letter is appended, any new violating factor must be a suffix. For every suffix of length \(L\) and every candidate period \(p<L\), reject exactly when \(p\) is a period and
\[
11L>20p.
\]
This integer inequality is equivalent to exponent strictly greater than \(\frac{20}{11}\).

The exact survivor counts at lengths \(0,1,\ldots,22\) are
\[
1,3,6,12,18,30,42,60,78,108,144,186,240,312,420,528,678,888,1140,1464,1920,2436,3042.
\]
Hence there are exactly \(3042\) length-\(22\) candidates that could possibly have circular critical exponent at most \(\frac{20}{11}\).

For each candidate, scan the doubled word \(ww\). Every factor of every conjugate is exactly a substring of \(ww\) that starts in one of the first \(22\) positions and has length at most \(22\). Computing the least period of each such substring gives the exact circular critical exponent. The minimum over all \(3042\) candidates is \(\frac{20}{11}\), attained by exactly \(132\) labeled words.

This proves the lower bound as well as attainment: if any length-\(22\) circular word had critical exponent below \(\frac{20}{11}\), its linear representative would have no factor of exponent above \(\frac{20}{11}\), so it would be among the \(3042\) exhaustively scanned candidates.

Canonicalizing the \(132\) minimizers by rotation produces the six representatives displayed above. Each has \(22\) distinct rotations, accounting for all \(132\) labeled minimizers. Applying all six alphabet permutations and reversal to the six circular classes gives one orbit.

## Verification
Run `python3 verify.py` beside `certificate.json`.

The verifier reconstructs the candidate language in two independent period-testing ways. One engine checks every possible period of each newly created suffix; the other computes the least period of each newly created suffix and compares its exponent with \(\frac{20}{11}\). Their complete level sets must agree through length \(22\).

It filters all \(3042\) candidates by an exact doubled-word circular threshold scan. For every surviving minimizer it independently computes the exact critical exponent by scanning every factor of every rotation. It verifies the \(132\) minimizers, the six rotation classes, their critical factors, and the single symmetry orbit.

## Relationship to prior work
Currie, Mol, and Rampersad prove that the only lengths with no \(\frac{7}{4}^+\)-free circular ternary word are \(5,7,9,10,14,16,17,22\), and they prove that every length at least \(23\) admits such a word. Their article therefore identifies \(22\) as the last exceptional length for the ternary intermediate threshold, but it does not determine the best achievable exponent at length \(22\).

The exact value \(\frac{20}{11}\) is a strict refinement of that statement: it quantifies how far the last exceptional length lies above \(\frac{7}{4}\). Shur's earlier classification of ternary square-free circular words shows in particular that length \(22\) admits a square-free circular word, which only implies that the optimum is below \(2\) and does not determine the exact value.

Targeted searches for the exact fraction, length, critical-exponent formulation, and the six representatives found the threshold paper and general circular-word literature but no published statement of this exact minimax value or equality classification.

## Limitations
The computation proves only the length-\(22\) minimax statement and its equality cases. It does not determine the analogous function for all lengths, nor does it improve the asymptotic circular repetition threshold.

The originality search cannot exclude an unpublished computation or an unindexed table containing the same length-\(22\) value. The result is independently reproducible from the definitions and does not rely on source-author code.

## References
1. J. D. Currie, L. Mol, and N. Rampersad, “Circular Repetition Thresholds on Some Small Alphabets: Last Cases of Gorbunova's Conjecture,” arXiv:1803.08145v1, first public version 2018-03-21; Electronic Journal of Combinatorics 26(2), #P2.31, 2019, DOI 10.37236/7985.
2. A. M. Shur, “On Ternary Square-Free Circular Words,” arXiv:1009.5759, Electronic Journal of Combinatorics 17(1), #R140, 2010.
