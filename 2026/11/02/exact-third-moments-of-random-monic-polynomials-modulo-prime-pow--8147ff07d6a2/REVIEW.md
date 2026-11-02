# Scientific review: exact third root-count moments

## Correctness

**PASS.** The theorem fixes independent uniform lower coefficients of a monic polynomial of degree at least three. The first two moments follow by solving one or two linear evaluation conditions. For three evaluations, the three-by-three Vandermonde matrix has Smith exponents \(0,t,s\), with \(t\) the least difference valuation and \(s\) the truncated sum of all difference valuations minus \(t\). The exact valuation partition of two translated sample points distinguishes the case of three different first digits from a uniquely coalescing pair; all equality cases and the prime two are included. The resulting two geometric sums give the stated parity-specific formulas. The accompanying exact arithmetic program independently checks full coefficient enumeration for cubic and quartic polynomials and direct triple counting. These finite tests are supporting evidence, not the infinite proof.

## Originality

**PASS, subject to priority risk.** The nearest recent paper, Simhi (2026), bounds local root-count moments at modulus \(p^2\) in a squarefree-values setting, but the inspected §§2, 3.1 and 5 do not supply the all-exponent exact third moment or its parity dependence. Bhargava–Cremona–Fisher–Gajović (2022) and Caruso (2022) study genuine \(p\)-adic roots rather than root classes modulo arbitrary \(p^k\). Prior finite-modulus exact distributions at the second and third levels do not imply formulas for every exponent. Targeted statement- and alias-based searches found no covering result. A previously published equivalent moment identity or a systematic framework permitting it as a specialization remains possible; the assessment is not an independent or exhaustive priority certificate.

## Mathematical value

**PASS.** The exact third moment is a natural statistic of root clustering in random polynomial congruences and is directly motivated by the use of local root moments in squarefree-value questions. The result captures every prime and exponent and exhibits a substantial change of scale: linear variance but exponentially growing third moment, with different sharp constants according to exponent parity. The degree threshold is natural because it corresponds to independence of three evaluation constraints. No fourth moment or full distribution is claimed.

## Key literature and limitations

O. Simhi, *Squarefree values of random polynomials are Gaussian mixtures*, arXiv:2610.29911v1 (21 October 2026); M. Bhargava et al., *The density of polynomials of degree n over \(\mathbb Z_p\) having exactly r roots in \(\mathbb Q_p\)* (2022), DOI:10.1112/plms.12438; X. Caruso, *Where are the zeroes of a random p-adic polynomial?* (2022), DOI:10.1017/fms.2022.27. Residual priority risk concerns unindexed or differently formulated modular-congruence moment identities, especially at higher prime-power exponents.

Self-review: passed. Independent audit: not yet performed.
