# Review

## Correctness
PASS. The proof reconstructs the two generating-function tails exactly. Sufficiency is shown by explicit tail bounds at the proposed thresholds and monotonicity for larger bases. Necessity treats the only possible modular-wrap escape: if a sub-threshold base survives \(n=1\), the first tail must be at least one full modulus. That forces \(b=2a+s\) into \(s\le a-1\) for the \(X\)-coordinate and \(s\le y-1\) for the \(Y\)-coordinate. In those ranges the \(n=2\) tail is proved to lie strictly between \(1\) and \(b^2\), so it cannot vanish after reduction modulo \(b^2\). The packaged exact replay checks the finite ranges stated in VERIFICATION.md.

## Originality
PASS. The 2025 source gives the formulas for sufficiently large bases and one \(d=7\) example using bases \(143\) and \(64\), but no general coordinate-wise least-base theorem. The September 2026 source proves only the least common base and explicitly uses both coordinates together in its sharpness argument. Its \(d=7\) discussion again records the two separate example bases without a general formula. Targeted semantic-database searches for separate Pell extraction thresholds, aliases, and the proposed \(2X_1(Y_1+1)\) expression returned no covering result. Exact web searches likewise surfaced the September 2026 source rather than an earlier coordinate-wise classification.

## Value
PASS. The recent source makes base size part of the optimization problem for fixed arithmetic expressions and proves a sharp common threshold. Separating the coordinate thresholds is therefore a natural structural refinement, not an arbitrary finite slice. The \(Y\)-threshold can be much smaller than the common one, and the proof explains the modular-wrap phenomenon that prevents \(n=1\) alone from proving individual minimality. The result gives the exact base needed when only one Pell coordinate is required.

## Closest literature and limitations
The closest source is Dumitru–Prunescu, arXiv:2609.28649, Section 9.1, which proves the common threshold \(2X_1(X_1+1)-1\). The earlier Prunescu–Sauras-Altuzarra paper, arXiv:2405.04083, Corollary 37 and Example 38, supplies the formulas and the \(d=7\) bases. The claim is limited to these fixed extraction formulas and does not assert a globally optimal arithmetic representation.

Same-model review: passed. Independent audit: not yet performed.
