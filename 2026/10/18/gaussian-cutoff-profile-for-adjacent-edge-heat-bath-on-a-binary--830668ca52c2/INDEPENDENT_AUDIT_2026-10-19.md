# Independent mathematical audit

## correctness

PASS

Walsh characters diagonalize the exact edge-heat-bath operator: lambda(S)=1-|edges incident to S|/n=1-(k+r)/n for nonempty proper S of size k and r cyclic runs. The exact run multiplicities are (n/r)*choose(k-1,r-1)*choose(n-k-1,r-1). At t=floor(n log n/4+cn), the mass from subsets with adjacent occupied indices vanishes in L2 via sum_{r,m>=1} (n e^{-4t/n})^r/r! * binom(m+r-1,r-1)e^{-2tm/n}, bounded by exp(A/(1-w))-exp(A)->0 where A=nw²=O(1), w=e^{-2t/n}->0. For fixed isolated k, eigenvalue (1-2k/n)^t matches b^k with b=(1-2/n)^t, and summable factorial tails finish L2 product approximation. A Gaussian CLT for log product density and bounded L2 norms yield TV 2Phi(e^{-2c}/2)-1, and Fourier Parseval yields exp(e^{-4c})-1 chi-square. Independently checked cyclic-run counts through n=8 and exact finite transitions/Walsh eigenvalues for n=4,5. Finite checks do not prove limit; proof handles any fixed c and all deterministic starting states by translation.

## originality

PASS

Best-of-knowledge originality established for the final exact claim, not for known supporting formulas: searched published Resultary records and compared actual mathematical statements, same-object literature, reductions and stronger plausible frameworks; this PASS is conditional on the explicitly documented access/priority risks.

## value

PASS

A sharp Gaussian cutoff window and a stronger L2 approximation for the full joint distribution of an overlapping local-update chain are natural and useful quantitative mixing statements, substantially more specific than proving only order-of-magnitude mixing or existence of cutoff.

The dated certificate retains the supplied scientific assessment, sources and limitations.
