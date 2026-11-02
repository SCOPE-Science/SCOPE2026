# Scientific review: exact finite-block joint two-adic binomial valuations

## Correctness — PASS

The stated scope is all integers \(L\geq0\), with uniform sampling on \(0\leq n<2^L\). Legendre's identity makes the first valuation \(s_2(n)\) and the second \(2s_2(n)-s_2(3n)\); the latter counts carries in the addition \(n+2n\). The three states \(t=b_{i-1}+c_i\) and all six bit transitions are explicitly specified. Crucially, the terminal column is weighted by \((1,1,v)^{\mathsf T}\), accounting for the carry beyond the last sampled input digit. Matrix inversion gives the rational length-generating function. Its mixed and second derivatives prove the moment formulas for every length, not just sampled lengths. The displayed nonzero Hankel determinant proves generic linear-representation minimality. Independent exact integer and rational checks on all small dyadic blocks confirm each critical boundary and algebraic calculation. No finite test is treated as a proof for unbounded lengths.

## Originality — PASS, with explicit historical-priority uncertainty

Schmid's 1984 paper and Schmidt's 1983 paper establish general binary-multiple digit-sum theory. The complete primary text of the 1984 article was unavailable; an equivalent finite-length formula may be implicit there. Drmota and Krattenthaler's 2018 paper was inspected and explicitly proves the general asymptotic joint central limit law and covariance, so neither the leading covariance \(5L/12\) nor the Gaussian law is claimed as new. Sun's 2010 paper was inspected for its divisibility results involving the same binomial families; these do not produce finite-block joint frequencies. A prior support-only valuation-pair classification covers which pairs are attainable, not their exact multiplicities on a finite dyadic block. The distinct assertion examined here is the exact rational bivariate finite-block generating law, the generic three-state lower bound and all finite-length covariance corrections. Subject-specific and equivalence searches did not locate the same complete claim. Historical uniqueness remains subject to the inaccessible original Schmid text and possibly other old digit-correlation work.

## Mathematical value — PASS

The joint valuation count is a natural refinement of known digit-sum dependence: it determines every simultaneous divisibility frequency for two familiar factorial ratios at every finite dyadic scale. The complete generating function is reusable for arbitrary joint moment or tail calculations. The covariance correction distinguishes even and odd block lengths and contains terms that asymptotic limit laws discard. The nonzero Hankel certificate proves that the three-state structure cannot be compressed further as a generic linear transfer. These are finite-scale arithmetic facts, not a restatement of a Gaussian theorem or a single routine numerical table. No broader infinite-multiplier generalization is claimed.

## Literature and limitations

Closest archival paper: J. Schmid, *The joint distribution of the binary digits of integer multiples*, Acta Arithmetica 43 (1984), 391–415, DOI 10.4064/aa-43-4-391-415; full text not inspected owing to access. Other comparators: W. M. Schmidt (1983); M. Drmota and C. Krattenthaler, arXiv:1803.02178 (2018); Z.-W. Sun, arXiv:1004.4623 (2010); and J. C. Chen, H.-K. Hwang and V. Zacharovas, arXiv:1212.6697 (2012). The distribution is restricted to the prime two, the two named binomial families and complete dyadic initial intervals. Full historical-priority proof and independent mathematical audit remain outstanding.

Self-review: passed. Independent audit: not yet performed.
