# Self-review: Exact dyadic eventual periods for A158690

## Correctness — PASS
The formula has fixed quantifiers \(k\ge2\), \(n\ge k+3\), and exact modulus \(2^{k+3}\). The Stirling/inclusion–exclusion transform is a finite computation at any index; modulo a fixed prime power its long tail vanishes. The normalized odd-base binomial congruence is proved uniformly, while the even-base terms vanish at the declared threshold. A valid fourth-power finite-difference annihilator reduces the remaining infinite sum to eight coefficients. Their two weighted sums are \(2\) and \(0\) modulo \(4\), proving the parity-sensitive obstruction and the exact least eventual period. Two independent coefficient algorithms and the exact finite-difference computations replay. Finite computations corroborate but do not replace the infinite proof.

## Originality — PASS
Kallat, arXiv:2609.07238v1, Sections 1–4, proves that \(\lambda(M)\) is an eventual period for any integer modulus \(M\), but gives no general formula for the *least* period. For \(M=2^r\), his bound is \(2^{r-2}\), whereas the new result supplies and proves the sharp period \(2^{r-3}\) for every \(r\ge5\). OEIS A158690 separately reports period two modulo \(16\) without the infinite result. Searches for the object, aliases, power-of-two periods, half-Carmichael periods and parity-sensitive lift, along with records addressing related but different sequences, did not reveal covering statements. The possibility of unindexed equivalent work remains.

## Value — PASS
The motivating theorem raises the natural issue of sharpness of the Carmichael period bound. An exact least period for every dyadic modulus beyond a fixed threshold is a substantive infinite quantitative classification, not a restatement of eventual periodicity. The parity-sensitive half-shift formula supplies the necessary minimality obstruction and explains an unexpectedly consistent factor-two saving.

## Scientific limitations
The least preperiod and non-dyadic least periods remain unknown here. The originality determination is limited by discoverability of available literature. There has been no independent mathematical audit.

Self-review: passed. Independent audit: not yet performed.
