# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The central expansion follows from the exact beta-gamma factorization \(Z_{1+\varepsilon}=S(1+\varepsilon V)\), with \(S\sim\Gamma(2r,1)\), symmetric \(V=2P-1\), and known beta moments \(\mathbb EV^2=1/(2r+1)\), \(\mathbb EV^4=3/[(2r+1)(2r+3)]\). Expanding the exact cdf and applying the implicit-function equation for a fixed quantile gives the stated quadratic coefficient. The coefficient changes sign only at \(m_q=2r+1\). Repeating the calculation to fourth order at that root gives the positive coefficient \((2r+1)/(2(2r+3))\), so the degenerate point is a quartically flat local minimum rather than an unresolved sign change.

The endpoint formulas were checked independently by conditioning on one gamma variable and differentiating the exact cdf at \(\alpha=0\) and \(\alpha=2+\). The variance-gamma and McKay expansions are then substitutions into the exact distributional representations used in Gaunt--Ouimet. Numerical inversion of the exact one-dimensional cdf representations supports the quadratic, quartic, endpoint, and distribution-specific formulas; the verification output is included as a standalone artifact.

## Originality

**PASS, to the best of our knowledge, with a deliberately narrow claim.** Gaunt and Ouimet (arXiv:2609.20212v1) establish global median monotonicity for the same two-gamma family and transfer it to variance-gamma and McKay distributions. Their results supply the global median ordering and endpoint limits, but do not state the general fixed-\(q\) Taylor coefficient, the transition quantile \(G_{2r}(2r+1)\), the critical quartic coefficient, or the displayed endpoint convergence rates.

The broader weighted-gamma crossing problem has substantial prior art. Bock--Diaconis--Huffer--Perlman (1987) prove tail inequalities and crossing results for gamma sums; Diaconis--Perlman (1990) analyze crossing locations under majorization, including the equal-weight comparator; Yu (2017) proves broad unique-crossing results and explicitly situates the earlier work. No novelty claim is made for Schur-convexity, unique crossing, or the existence of a crossing threshold.

Searches for the explicit curvature coefficient, the threshold at the \(\Gamma(2r,1)\) cdf evaluated at \(2r+1\), fourth-order quantile flatness, and small-noise variance-gamma/McKay median rates did not locate equivalent statements. Repository overlap searches by source identifier, mathematical object, and equivalent terminology found no matching accepted record.

The complete Diaconis--Perlman (1990) and Bock et al. (1987) texts were not directly inspected; only accessible abstracts/bibliographic material and later descriptions of their theorems were checked. They are therefore the most concrete residual originality risk, especially for the equal-weight crossing component. The originality claim is restricted to the explicit local quantile expansion, critical quartic refinement, and the distribution-specific endpoint rates, and is stated only to the best of our knowledge.

## Value

**PASS.** The result adds local geometry to a newly proved global median monotonicity theorem. It identifies the exact quantile at which equal weighting changes from locally maximizing to locally minimizing the quantile, resolves the degenerate case at fourth order, and converts qualitative endpoint convergence in two applied distribution families into explicit leading-order rates. These coefficients are useful for perturbative approximations and clarify why the median behaves differently from sufficiently high quantiles.

## Limitations

- Two iid gamma summands only.
- Local expansions in the weight parameter; no new global quantile crossing theorem is asserted.
- No uniform remainder estimates over \(q\), \(r\), or the distribution-family parameters.
- The complete Diaconis--Perlman (1990) and Bock et al. (1987) texts were not directly inspected.
- Independent audit has not been performed.
