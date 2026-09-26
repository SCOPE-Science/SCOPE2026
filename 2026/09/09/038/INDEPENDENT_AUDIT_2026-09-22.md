# Independent audit — 2026/09/09/038

Date: 2026-09-26. Disposition: retain accepted, with a narrowed originality claim.

## Correctness — PASS

I independently reconstructed all (2^{16}=65536) skew sequences with first sign fixed and recomputed every aperiodic autocorrelation and energy. All odd-lag correlations vanish; the full 281-bin energy histogram, sum 32,505,856, mean 496, minimum 88, maximum 5,456, and exactly four minimizer indices 10112, 15366, 26963, 29397 match. Hence the merit optimum (1089/176=99/16) and the (Fge6) candidate set are exact.

For the six proposed frontier sequences, I evaluated the degree-32 polynomial directly at all 32,768 grid points. Their maxima agree with the stored numbers to floating roundoff. The standard trigonometric Bernstein sampling bound (Mle g/cos(32pi/32768)), with the candidate's outward upper factor, places the six suprema in the disjoint stated intervals. The four merit optimizers have grid lower bounds 1.3076486 or 1.4166389, excluding the stipulated (Mle1.25) rectangle.

I also checked domination **without trusting the stored million-byte grid table**. For each of the other 65,530 independently reconstructed sequences, I compared its direct grid lower bound with the applicable frontier member's certified sup-norm upper bound at no greater energy. A 16-point grid settles 56,598, 32 points settle 8,844 more, 64 points settle 82, and 128 points settle the last six. The frontier intervals and energies make the three reversal pairs incomparable at the available bounds. This certifies the six-member Pareto set in the stated skew family.

## Originality — PASS only for the joint result

Packebusch and Mertens (2015), a primary source omitted from the candidate's prior-work comparison, explicitly computed all optimal skew-symmetric sequences to length 119 and print **(N=33,E=88,Fapprox6.188)** with two symmetry-class representatives in their Table 3. Thus the exact merit optimum and optimizers are already known, contrary to the record's suggestion that earlier evidence was confined to heuristic long-length windows. The checked sources do not print the full length-33 joint merit–flatness frontier, rigorous sup-norm enclosures or the 65,536-member joint certificate. Those are the bounded original contribution. The rectangle threshold 1.25 is chosen by the candidate, so its exclusion is a corollary rather than an independent research boundary.

## Scientific value — PASS, bounded

The certified tradeoff among merit factor and circle sup-norm supplies an exact small example connecting two established optimization programs. Its use is limited to the normalized skew length-33 family; the merit optimum alone and the arbitrary rectangle line add no novelty.

## Sources

- Packebusch and Mertens, *Low Autocorrelation Binary Sequences*, arXiv:1512.02475, abstract and Table 3 p. 14: https://arxiv.org/pdf/1512.02475
- Balister et al., *Flat Littlewood Polynomials Exist*, arXiv:1907.09464: https://arxiv.org/abs/1907.09464
- Candidate `artifacts/Ehist.json`, `artifacts/frontier.json`, `artifacts/gmax_all.json`; independent energy and direct-grid domination replay above.
