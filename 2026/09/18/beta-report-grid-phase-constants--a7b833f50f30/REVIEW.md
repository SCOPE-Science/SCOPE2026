# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The p-value transformation \(E=-\log(1-U)\) was checked directly: the null becomes \(\operatorname{Exp}(1)\), the \(\operatorname{Beta}(1,\theta)\) alternative becomes \(\operatorname{Exp}(\theta)\), and the two-site likelihood ratio is monotone in \(E_1+E_2\). The oracle boundary is therefore the Gamma(2,1) quantile \(a_\alpha\).

For the phased equal-step log-evidence reports, each regular-bin likelihood ratio is explicit and decreases geometrically with the bin index. This verifies the ordering of report diagonals used by the report-space Neyman--Pearson test. The tail cell starts at or beyond the oracle boundary for \(\rho\in[0,1]\), and its likelihood ratio is below the two relevant boundary diagonals, so no omitted tail cell can enter before them.

Only the diagonals \(i+j=L-2\) and \(i+j=L-1\) intersect the continuous oracle boundary. Direct exponential integration gives the four full-diagonal masses and two partial-boundary masses displayed in `RESULT.md`. Their exact null-size randomization yields the stated finite-\(L\) deficit formulas. Taylor expansion gives the two quadratic phase branches, which agree at \(\rho=1/2\). The phase function is minimized uniquely at \(1/2\), where its value is \(1/24\), versus \(1/6\) at aligned endpoints.

The accompanying deterministic script evaluates the exact formulas without numerical integration, checks convergence of \(m^2d\) to the theorem's constant, and checks the phase curve against its limiting formula. For \(\alpha=0.05,\theta=2,m=8,\rho=1/2\), it reproduces the reported deficit \(1.0867749303\times10^{-4}\).

## Originality

The closest source is Dubey and Huo (2026), arXiv:2609.19708. Their Proposition 2.5 gives the class-optimal \(\Theta(m^{-2})\) loss for one hypothesis, and their numerical study explicitly notes grid-alignment oscillations in \(m^2\) times the equal-width-report deficit. Thus neither the inverse-square exponent nor the existence of alignment effects is claimed as new.

Classical high-rate detection quantization is also prior art. Poor (1988), DOI 10.1109/18.21219, gives a general second-order fine-quantization result and applies it to binary signal detection; its abstract also states analogous companded-quantizer formulas and an optimal compander. Gupta and Hero (2003) and Villard and Bianchi (2010) study high-rate quantization for detection criteria based on asymptotic performance such as error exponents. These sources establish that second-order loss and quantizer design are classical themes.

The originality claim is restricted to the exact finite boundary formulas for the two-site \(\operatorname{Beta}(1,\theta)\) fixed-level problem, the explicit piecewise phase law
\[
\Phi(\rho)=\{1-3\min(\rho,1-\rho)^2\}/6,
\]
the resulting factor-four separation between half-cell and aligned phases, and the fact that the phase-optimal lattice is independent of \(\theta\). Targeted searches for shifted or offset high-rate Neyman--Pearson quantizers, quantization phase at a detection boundary, and p-value quantization did not locate these statements. The assessment is therefore **to the best of our knowledge**, not a claim of exhaustive literature coverage.

The principal residual originality risk is Poor (1988): the accessible abstract confirms a highly general fine-quantization theorem, but the full theorem and all binary-detection specializations were not inspected. That source may subsume part of the second-order mechanism. No inspected statement, however, supplies the present source-specific two-diagonal finite formulas or the displayed phase curve. This is a residual risk, not evidence of known coverage.

## Value

The result converts an observed finite-resolution oscillation into an explicit asymptotic law and a concrete report-placement rule. Within the log-evidence lattice family, changing only the grid phase changes the leading loss constant by a factor of four while leaving the \(m^{-2}\) exponent unchanged. The half-cell placement is simultaneously phase-optimal for the full \(\operatorname{Beta}(1,\theta)\) family because it depends only on the null level \(\alpha\).

In the benchmark \(\alpha=0.05,\theta=2,m=8\), the exact half-phased log-evidence deficit is about \(0.0681\%\) of oracle power, compared with the \(0.72\%\) relative deficit reported by Dubey and Huo for equal-width p-value cells. The comparison demonstrates practical constant-factor value without claiming global optimality.

## Limitations

The result is for \(K=1\), two independent sites, and homogeneous \(\operatorname{Beta}(1,\theta)\) alternatives. It optimizes only the phase of the displayed log-evidence lattice, not the full class of measurable reports. Randomization at a report likelihood-ratio atom is allowed. No corresponding phase law is proved here for multiple hypotheses, heterogeneous sites, or general decreasing alternative densities.
