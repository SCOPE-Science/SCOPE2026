# Scientific assessment of the Pareto-maxima corner-count covariance

## Correctness — PASS

Under iid sampling with independent continuous coordinates, ordering by decreasing first coordinate turns the Pareto-maxima count into a sum of upper-record indicators of the second coordinates. The count in a fixed upper-right rectangle becomes the number of second-coordinate threshold exceedances in the first \(a\) ordered observations, conditional on the first-coordinate exceedance count \(A_n=a\). Relative-rank independence gives zero mixed terms at indices at most \(a\); at each later record index \(i>a\), the mixed covariance with an earlier exceedance indicator equals

\[ -\frac{(1-q)\bigl[1-(1-q)^{i-1}\bigr]}{i(i-1)}. \]

Summing proves the claimed conditional formula with the zero boundary cases \(a=0,n\). Mixing the binomial law of \(A_n\) yields the unconditional strict negative sign. The telescope \(a\sum_{i=a+1}^n[i(i-1)]^{-1}=1-a/n\), together with a geometric-tail bound, gives the exact fixed-parameter limit \(-(1-p)(1-q)\) and the published positive exponential error bound.

Independent exact-rational checking reconstructed all 199 permutation cells at \(2\le n\le7\), plus 297 grid cases through \(n=34\). It confirms the rational examples \(-1/16\) and \(-15/128\) at \(p=q=1/2\), for \(n=2,3\). Such finite checks are corroboration, not the infinite-domain proof.

## Originality — PASS, with explicit priority limitations

The claim has the equivalent form of an upper-record-count covariance against fixed-threshold exceedances on an initial prefix of iid observations. Mean maxima counts in Bentley, Kung, Schkolnick and Thompson (1978), marginal planar maxima limit theorems in Bai, Hwang, Liang and Tsai (2001), and maximal-indicator correlation/variance theorems in Jacobovic and Zuk (2022) do not by themselves determine this cross moment. The present theorem evaluates the joint statistic for all sample sizes and thresholds and gives its limiting covariance and finite-sample error. Searches of related exact mathematical findings did not locate equivalent coverage; an unsuccessful search is not priority certification.

Barbour and Xia (2001) is a plausible additional primary source, but its complete text could not be examined. An earlier joint record/empirical-process identity under a different formulation may cover the calculation. These are retained residual risks, not artificially dismissed.

## Mathematical value — PASS

The two observables are natural descriptors of a random Pareto skyline: total frontier size and occupancy of a fixed northeast corner. The strict negative interaction is nontrivial because the frontier size is independent of either coordinate threshold count (and their pair). Exact conditional values, a nonzero universal fixed-threshold limit, and an exponential quantitative envelope are useful finite-sample structural information rather than a restatement of a marginal harmonic expectation.

## Domain and verification limits

The stated theorem is restricted to two dimensions, iid pairs with independent continuous coordinates, fixed \(0<p,q<1\), and \(n\ge2\). No assertion concerns dependent coordinates, tied observations, thresholds depending on \(n\), other dimensions, causal effects, or stochastic order. There is no Lean proof or external expert attestation.

## Primary literature

- J. L. Bentley, H. T. Kung, M. Schkolnick and C. D. Thompson (1978), *On the Average Number of Maxima in a Set of Vectors and Applications*, DOI 10.1145/322092.322095.
- Z.-D. Bai, H.-K. Hwang, W.-Q. Liang and T.-H. Tsai (2001), *Limit Theorems for the Number of Maxima in Random Samples from Planar Regions*, DOI 10.1214/EJP.v6-76.
- A. D. Barbour and A. Xia (2001), *The Number of Two-Dimensional Maxima*, DOI 10.1239/aap/1011994025; complete-text comparison remains pending.
- R. Jacobovic and O. Zuk (2022), *A correlation inequality for random points in a hypercube with some implications*, arXiv:2209.00346.
