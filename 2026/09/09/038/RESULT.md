# Exhaustive joint merit-flatness census of skew-symmetric Littlewood polynomials at length 33

## Context

Low-autocorrelation binary sequences and Littlewood-polynomial flatness are two classical but different sequence-design objectives. The merit-factor optimum in the skew-symmetric length-33 class is not claimed as new by itself: exact LABS enumerations, including Packebusch and Mertens (2016), cover optimal skew-symmetric sequences well beyond length 33. The contribution here is the exhaustive **joint** merit-flatness census at length 33, including a certified Pareto frontier and a rigorous exclusion region.

## Definitions

Let \(N=33\). Fix the global sign by \(a_0=+1\) and enumerate the \(2^{16}\) skew-symmetric sign sequences satisfying \(a_{16+j}=\((-1)^j\) a_{16-j}\) for \(j=1,\ldots,16\). For a sequence \(a\), let \(C_k\) be its aperiodic autocorrelations, \(E=\sum_{k=1}^{32} \(C_k^2\)\), and \(F=\(33^2\)/(2E)\). For \(P_a(z)=\sum_{k=0}^{32} a_k \(z^k\)\) define flatness \(M=\max_{|z|=1}|P_a(z)|/\sqrt{33}\).

For the rigorous grid comparison, let g(a) be the maximum sampled modulus on the G=32768 equally spaced unit-circle grid. Bernstein's inequality gives M(a)<=g(a) f_up/sqrt(33), with f_up=1.0000047062172828; the grid value itself is a lower bound.

## Result

1. The exact energy minimum is E=88, hence F_max=1089/176=99/16=6.1875, attained by exactly four sequences with half-indices 10112, 15366, 26963 and 29397, forming two reversal pairs. Across all 65,536 members there are 281 distinct energies, all energies are multiples of 8, the exact total energy is 32,505,856, and all odd-lag autocorrelations vanish.

2. No skew-symmetric length-33 sequence satisfies both F>=6 and M<=1.25. The only sequences with F>=6 are the four E=88 sequences. Their attained-grid flatness lower bounds are about 1.3076486 and 1.4166389, already above 1.25.

3. The certified joint Pareto set consists of six sequences in three reversal pairs:

- E=88: indices 10112/29397, with M in [1.3076486,1.3076548];
- E=120: indices 8777/30492, with M in [1.3004729,1.3004790];
- E=128: indices 46407/57362, with M in [1.2480442,1.2480501].

Every one of the other 65,530 sequences is certified dominated by one of these frontier members under the exact-energy / rigorous-flatness-interval comparison.

## Proof / evidence

`artifacts/verify.py` re-enumerates all 65,536 skew sequences, recomputes exact autocorrelation energies, checks the committed energy histogram and key direct-DFT grid maxima, and validates the Bernstein enclosure data. The committed machine-readable tables are `artifacts/frontier.json`, `artifacts/Ehist.json`, and `artifacts/gmax_all.json`.

The fresh audit independently repeated the full exact-energy census, evaluated the six frontier grid maxima, and performed a separate all-member FFT grid scan. For every nonfrontier sequence, an attained-grid lower bound was compared against a frontier member's Bernstein upper bound; all 65,530 nonfrontier members were certified dominated. Thus the Pareto claim does not rely merely on a saved success log.

## Limitations

- The merit optimum at N=33 is prior LABS knowledge; the originality claim is the joint merit-flatness census and its certified Pareto tradeoff.
- The space is only the skew-symmetric N=33 class with global sign fixed; no unrestricted length-33 LABS claim is made.
- Sup-norm upper bounds use a rigorous Bernstein grid enclosure rather than exact algebraic maximization.
- The rectangle (F>=6, M<=1.25) is a derived finite exclusion, not a separate literature record.

## Reproducibility

Run `python3 artifacts/verify.py`. The data files `artifacts/frontier.json`, `artifacts/Ehist.json`, and `artifacts/gmax_all.json` contain the frontier, energy histogram and all-member grid/energy data used by the certificate.

## References

- T. Packebusch and S. Mertens, “Low Autocorrelation Binary Sequences,” Journal of Physics A 49 (2016) 165001, arXiv:1512.02475.
- C. de Groot, D. Würtz and K. H. Hoffmann, “Low autocorrelation binary sequences: exact enumeration and optimization by evolutionary strategies,” Optimization 23 (1992), 369–384.
- P. Balister et al., “Flat Littlewood Polynomials Exist,” arXiv:1907.09464.
- J. Jedwab, D. J. Katz and K.-U. Schmidt, “Advances in the merit factor problem for binary sequences,” arXiv:1205.0626.
