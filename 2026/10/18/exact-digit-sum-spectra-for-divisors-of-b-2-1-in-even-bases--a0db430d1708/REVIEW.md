# Scientific review: exact digit-sum spectra for divisors of \(b^2-1\)

## Correctness — PASS

The divisibility \(d(b+1)\mid N\) forces the ordinary base-\(b\) digit sum to be divisible by \(d\). Alternating digit sums modulo \(b+1\) exclude every odd sum at most \(b-1\). The displayed witnesses \(A=\sum_{j=0}^{2d-1}b^j\) and \(B=b^4+db^2+(d-1)b+(b-1)\) are independently checked modulo each coprime factor \(d\) and \(b+1\). They have digit sums \(2d\) and \(b-1+2d\), respectively. Concatenation proves all allowed sums are attained, including the boundary cases \(b=2\) and \(d=b-1\). The standalone automaton verifier exhaustively checks finite-state reachability for 28 parameter pairs and bounded target sums. No infinite conclusion is inferred from the finite tests.

## Originality — PASS within inspected evidence

The primary paper arXiv:2303.13017 gives necessary divisibility conditions and already guarantees all multiples of \(2d\) here via its Theorem 2, because \(s_b(d(b+1))=2d\). It treats the base-ten modulus \(33\) only by excluding digit sum \(3\) and explicitly poses determination of the entire output set as Question 2. The genuinely new content is the complete odd branch: the exact threshold and absence of any other holes. The theorem determines that entire example and an infinite natural family of divisors of \(b^2-1\). The 2020 paper arXiv:2002.02731 supplies general finite-state/attainability tools, but does not give this uniform exact formula. Relevant OEIS sequences concern restricted examples rather than the spectrum theorem. Targeted literature and mathematical-result searches did not reveal equivalent or stronger coverage. Unindexed or unpublished earlier solutions remain a risk; search failure is not proof of worldwide novelty.

## Mathematical value — PASS

This is a complete and sharp classification of a natural entire family of digit-sum images, not a finite isolated example. It settles the exact set (including all holes) for the published motivating \(b=10,n=33\) case and provides a uniform sharp largest excluded admissible sum, \(b-1\), independent of \(d\). The divisor-lattice choice is mathematically natural because all the moduli divide \(b^2-1\) and contain \(b+1\). It directly addresses the published question about exact out-neighborhoods when the congruence condition is insufficient. The result does not classify arbitrary moduli or odd bases.

## Sources and limits

Phunphayap–Noppakaew–Pongsriiam, arXiv:2303.13017, Sections 1–3, especially Theorem 1, Example 4 and Question 2; Clokie et al., arXiv:2002.02731, Theorems 3–4; OEIS A283742 and A216995. No independent mathematical audit has been performed.

Self-review: passed. Independent audit: not yet performed.
