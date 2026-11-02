# Scientific review — exact three-square obstructions for superfactorials

## Correctness (PASS)

The individual-index criterion follows rigorously from Legendre's three-square theorem, the parity identities for \(\nu_2(S(2m))\) and \(\nu_2(S(2m+1))\), and the modulo-eight odd-factor recurrences. The binary formulas for \(A(m)\) and \(B(m)\) are obtained by iterating those recurrences. The density and the \(O(\sqrt X)\) estimate follow from an explicitly described \(32\)-state transfer matrix whose annihilating polynomial, connectivity and row/column sums are checked by exact integer operations. The sharp subsequence formula follows from \(34\) exact matrix identities and a specified Cayley--Hamilton recurrence of order \(34\), not from finite extrapolation. The standalone checker replays every finite certificate; it separately compares the index criterion to independently accumulated superfactorial odd parts and valuations through index \(4096\).

## Originality (PASS within inspected evidence)

The closest sources are Burns (2021, arXiv:2101.01567) and Burns (2022, arXiv:2203.16469). They study **ordinary factorials**, giving a binary classification and asymptotic joint-state counts. Their results, combined with the new even-index reduction, imply the \(3/16\) limiting density and a square-root error bound; neither is claimed to be a novel consequence in isolation. The inspected primary full texts do not state the superfactorial-specific binary criterion or the exact infinite dyadic fluctuation \(E(2^{8j+5})=3\cdot2^{8j+1}+2^{4j}\). Aliyev (2022) calculates superfactorial valuations but not their odd parts or three-square classification; OEIS A000178 lists the underlying sequence without the result. Searches for equivalent or broader coverage yielded no theorem with the final sharp statement. Unindexed or implicit-equivalence risks remain.

## Mathematical value (PASS)

Superfactorials are a standard arithmetic sequence, equal to integer Barnes-G values and consecutive-node Vandermonde determinants. Three-square representability is a classical, natural invariant on this sequence, while factorial three-square behavior already has a substantial literature. The theorem gives an explicit local binary characterization at every index, a global quantitative distribution, and an **exact** infinite dyadic discrepancy proving that the square-root exponent cannot be improved. The last exact oscillation is not furnished by merely knowing the density or asymptotic bounds for factorials; its full coefficient requires the transfer-matrix calculation.

## Closest literature and limitations

Source details and theorem-level implication comparisons appear in `RESULT.md` and `AUDIT.json`. Novelty is assessed against the accessible sources, not certified absolutely. The calculation neither supplies explicit three-square decompositions nor covers arbitrary products of factorials. Scientific conclusions are self-contained up to the finite exact matrix certificate; an independent scientific audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
