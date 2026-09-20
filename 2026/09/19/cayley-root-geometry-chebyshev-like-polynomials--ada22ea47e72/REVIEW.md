# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The key reduction is exact: source equation (2.4) gives
\[
p_n(z)=(z-1)^{2n}P_n(((z+1)/(z-1))^2),
\]
and source Proposition 4.1, together with
\((z^2+1)/(z-1)^2=(u+1)/2\), gives the displayed \(Q_n\) formula for \(q_n\).

The Hurwitz claim follows from two independent ingredients that were checked separately: Eneström--Kakeya places the \(P_n\) roots inside \(|u|\le n/(n+1)\); for \(Q_n\), a direct triangle-inequality argument rules out \(|u|\ge1\). The inverse Cayley identity
\[
\operatorname{Re}\frac{w+1}{w-1}
=
\frac{|w|^2-1}{|w-1|^2}
\]
then gives strict left-half-plane location.

The discriminant derivation was checked at three levels. First, the product calculation for \(\operatorname{Disc}(Q_n)\) was rederived from
\[
(1-u)Q_n(u)=1+(n+1)u^n-(n+2)u^{n+1}.
\]
Second, the squared-variable and Möbius discriminant covariance formulas were checked directly from roots. Third, exact symbolic computations for \(1\le n\le6\) agree with the claimed \(\operatorname{Disc}(q_n)\). Applying the same derivation to \(p_n\) reproduces Proposition 5.4 of the source paper exactly, providing an additional consistency check.

For the limiting law, Erdős--Turán gives angular discrepancy \(O(\sqrt{\log n/n})\) because the coefficient \(\ell^1\)-norms grow only polynomially. The constant/leading coefficient ratio gives exact products of root moduli \(1/(n+1)\) and \(1/(n+2)\), which forces all but \(O_\delta(\log n)\) roots into every fixed annulus \(1-\delta<|u|\le1\). Haar convergence survives taking both square roots. The inverse Cayley map is discontinuous on the limiting unit circle only at \(w=1\), which has Haar measure zero, so the continuous-mapping argument gives the standard Cauchy pushforward.

No numerical experiment is used as a substitute for the proofs.

## Originality

**PASS, to the best of our knowledge.**

The directly relevant source, arXiv:2607.16940, was inspected in the sections defining both families and in the resultant/discriminant section. It gives the explicit formula for \(p_n\), the relation defining \(q_n\), the discriminant of \(p_n\), and then states that no analogous identity with only small prime factors seems to exist for \(\operatorname{Disc}(q_n)\). The source does not state the exact companion discriminant above. Its section outline and targeted full-text searches did not locate Hurwitz stability, Eneström--Kakeya localization, or an empirical zero-distribution theorem for these two families.

Targeted searches were made using the source title and arXiv identifier together with `zeros`, `zero distribution`, `Hurwitz`, `left half-plane`, `unit disk`, `discriminant q_n`, the exact auxiliary polynomial
\(1+u+\cdots+u^{n-1}+(n+2)u^n\), and the distinctive factor
\((n+2)^n+n^n\). No equivalent result was located. Searches of the current SCOPE archive by source identifier, family name, and zero-geometry/discriminant terminology likewise found no overlap.

The proof deliberately uses standard machinery rather than claiming it as new. Eneström--Kakeya is classical, and the Erdős--Turán zero-distribution theorem is classical; Soundararajan's 2019 exposition was consulted for the latter. Cauchy limits on the imaginary axis are also known in other constructions: O'Rourke--Reddy (2021) explicitly note the Cauchy zero law for \((z-1)^n+(z+1)^n\). That is related background, not coverage of the present sequences.

Residual risk remains because the Cayley reduction is elementary once source equation (2.4) is noticed, and general discriminant/resultant literature contains formulas that could imply the companion identity after a non-obvious specialization. The 2026 source is also recent enough that an unindexed follow-up could exist. No inaccessible paper was identified whose available metadata gives concrete reason to believe it already contains this specific \(q_n\) formula or the combined root-geometry result. The originality claim is therefore explicitly limited to the best of our knowledge.

## Value

**PASS.**

The result gives a unified zero-geometric mechanism for both newly introduced reciprocal families. It proves a strong global property—Hurwitz stability—for every degree, identifies the limiting zero measure as the Cauchy law on the imaginary axis, and supplies quantitative finite-\(n\) localization in Cayley coordinates.

The companion discriminant is also a direct substantive extension of the motivating paper: it provides the exact formula missing next to the known \(p_n\) discriminant and explains the observed failure of a small-prime-factor pattern through the explicit factor \(((n+2)^n+n^n)/2\).

## Limitations

The Apollonius inclusions are not asserted sharp. The limiting Cauchy statement is weak convergence, not a sharp direct discrepancy theorem on the unbounded imaginary axis. No irreducibility theorem is strengthened. The finding concerns only the two polynomial sequences in the cited source. No independent validation, formal proof-assistant verification, or independent audit is claimed.
