# The 2026 Reche exponent improves Soundararajan–Young, not the modular-group record
## Finding
Relative to the publicly stated theorems, the unconditional modular-group comparison in Alberto Acosta Reche, arXiv:2610.01998v1, is not a new record. Reche's Corollary 1.3 gives the exponent
\[
\eta(y)=\frac12+\frac{\sqrt{81y^2+106y+33}-5-9y}4
\]
and specializes it at the admissible value \(\theta=1/6\). The resulting exponent is
\[
\eta(1/6)=\frac{\sqrt{1905}-27}{24},
\]
and it satisfies the exact strict chain
\[
\frac23<\eta(1/6)<\frac{25}{36}.
\]
Kaneko's arXiv:2402.12133v3 states an unconditional \(2/3+\varepsilon\) exponent for the modular surface. Therefore Reche improves the Soundararajan–Young \(25/36+\varepsilon\) exponent, but not Kaneko's stated modular-surface exponent.

## Assumptions and scope
The claim compares theorem statements in the cited public sources; it does not independently re-prove the deep analytic estimates in either paper. The comparison is restricted to the modular group/modular surface, where both statements apply. Reche's broader theorem for congruence subgroups of indefinite quaternion algebras is not claimed to be covered by Kaneko's modular-surface result.

The lead source was first public on 2026-10-01 and lists MSC classes 11M36 and 11M06, with 11M36 first.

## Proof
Reche states
\[
\eta(y)=\frac12+\frac{\sqrt{81y^2+106y+33}-5-9y}4.
\]
At \(y=1/6\),
\[
81y^2+106y+33=\frac{1905}{12},
\]
so
\[
\eta(1/6)=\frac{\sqrt{1905}-27}{24}.
\]
For the lower comparison,
\[
\eta(1/6)>\frac23
\]
is equivalent to \(\sqrt{1905}>43\), which follows from \(1905>43^2=1849\).

For the upper comparison,
\[
\eta(1/6)<\frac{25}{36}
\]
is equivalent to \(3\sqrt{1905}<131\). Squaring is legitimate because both sides are positive, and
\[
9\cdot1905=17145<17161=131^2.
\]
Hence
\[
\frac23<\eta(1/6)<\frac{25}{36}.
\]

Reche explicitly presents \(25/36+\varepsilon\) as the Soundararajan–Young benchmark and says his value improves it. Kaneko's earlier arXiv record states an unconditional \(2/3+\varepsilon\) prime-geodesic error exponent for the modular surface. The exact chain above therefore shows that Reche's specialized exponent is between those two stated exponents.

## Verification
The standalone verifier checks the two integer inequalities \(1905>43^2\) and \(9\cdot1905<131^2\), derives the exact expression for \(\eta(1/6)\), and checks its decimal value against direct high-precision evaluation. These checks verify only the algebraic comparison, not the analytic proofs of the cited prime-geodesic theorems.

## Relationship to prior work
Soundararajan and Young give the parameterized exponent \(2/3+\theta/6\); at \(\theta=1/6\) this is \(25/36\). Reche gives the new parameterized exponent \(\eta(\theta)\) and explicitly compares \(\eta(1/6)\) with \(25/36\).

Kaneko's arXiv:2402.12133v3 states an unconditional exponent \(2/3+\varepsilon\) for the modular surface, and later lecture notes on the Selberg trace formula describe \(2/3+\varepsilon\) as the current unconditional record due to Kaneko. Reche's full text contains no occurrence of “Kaneko” or arXiv:2402.12133.

Targeted semantic searches for a published comparison between Reche's \(\eta(1/6)\) and Kaneko's \(2/3\) returned no covering result. The current and immediately preceding collections of related findings were also searched by both arXiv identifiers, author names, “prime geodesic”, “subconvexity”, and the benchmark exponents without finding an equivalent claim.

## Limitations
This is a correction to a literature benchmark, not a new prime-geodesic error estimate. It treats Kaneko's theorem as a public theorem statement and does not independently validate its deep proof. If that theorem were later withdrawn or corrected, the record comparison would need reevaluation. The result does not diminish Reche's broader congruence-subgroup/quaternionic theorem, whose domain exceeds the modular-surface statement inspected here.

## References
1. Alberto Acosta Reche, *On the prime geodesic theorem*, arXiv:2610.01998v1, first posted 2026-10-01.
2. Ikuya Kaneko, *The Prime Geodesic Theorem and Bounds for Character Sums*, arXiv:2402.12133v3, first posted 2024-02-19.
3. K. Soundararajan and Matthew P. Young, *The Prime Geodesic Theorem*, Journal für die reine und angewandte Mathematik 676 (2013), 105–120, DOI:10.1515/crelle.2012.002.
