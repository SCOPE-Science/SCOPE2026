# Independent mathematical audit

## correctness

PASS

Under tie-free common null the binary word is uniform among binom(N,m) fixed-composition words. At pooled rank j, F_m−G_n=B_j/(mn), H_N has jumps 1/N, so T=ΣB_j²/(mnN²). Hypergeometric variance yields E B_j²=mn j(N−j)/(N−1), summing E S=mnN(N+1)/6. R=1+Σ I_i. P(I_i=1)=2mn/[N(N−1)]. Condition on one adjacent transition: two distinguished positions contain one label each with equally likely orientations, remaining N−2 positions a uniform (m−1,n−1) word. Case j<i, j=i, j>i conditional means/variances give Σ_i E[S|I_i=1]=N(N−1)[(N−1)mn+N]/6; inserting into Σ_iCov(I_i,S) gives −mn(2mn−N)/3. Handle N=2,3 by enumeration. Independent exact Fraction exhaustive all compositions 2≤N≤11 matched formula, source verifier additionally checks 8,166 binary words through N12 and 777 conditional identities through N40. Algebra supplies all N, not finite extrapolation. For N≥3, mn≥N−1 ensures negativity; limit follows directly.

## originality

PASS

Best-of-knowledge novelty assessment compares identical mathematical statements and implications, not titles or a lack of search hits. Individual run and Cramér–von Mises null laws and pairwise transition covariance do not determine the cross moment. Comparison risks remain explicitly recorded; noncoverage is not asserted from abstracts of unread whole papers.

## value

PASS

The Wald–Wolfowitz runs test counts local rank alternations while Cramér–von Mises integrates the global squared two-sample empirical bridge. Their exact mixed null covariance is a motivated dependence/calibration statistic, with universal strict negative sign and nonzero proportional-sample limit. Neither marginal null law computes the coupling; not an arbitrary small parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
