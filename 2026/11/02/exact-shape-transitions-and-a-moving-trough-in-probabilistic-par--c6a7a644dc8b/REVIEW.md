# Independent mathematical audit

## correctness

PASS

Use the known exact conditional last-preference law Q_{n,p}(j)=(c_{n,j}+p sum_{k>j}c_{n,k}+(1-p)sum_{k<j}c_{n,k})/(n+1)^(n-1), with c_{n,k}=binomial(n-1,k-1) k^(k-2)(n-k+1)^(n-k-1), empty street exponents convention. Its adjacent difference is ((1-p)c_{n,j+1}-p c_{n,j})/denominator. Algebra gives c_{n,j+1}/c_{n,j}=h_j/h_{n-j}, h_j=(1+1/j)^(j-1), strictly increasing to e. Hence ordered thresholds T_{n,j}=h_j/(h_j+h_{n-j}) produce all monotone, U-shaped and tied trough cases; the endpoint maximum is selected by sign(1-2p). For fixed p<1/2 minima stabilize near a boundary via tau_j=h_j/(h_j+e). For p_n=1/2+t/n, expansion log h_k=1-3/(2k)+O(1/k²) uniformly for interior fractions gives n(T_{n,j}-1/2)->(3/8)(1/(1-x)-1/x); invert to u(t)=1/2+t/(sqrt(9/4+4t²)+3/2). Inspected full independent verifier constructing weighted arrivals for n<=6 and exact thresholds through n=80; source has analytic proof for all n. Handles n=2, endpoints p=0,1 and two central minima.

## originality

PASS

Durmić et al. (2022/2023) Theorem 3 already gives the full exact conditional last-preference distribution Q, so the marginal formula is prior and not claimed novel. The inspected primary PDF does not state the complete sharp threshold ordering, fixed-bias boundary-layer stabilization or critical p-1/2~1/n moving-trough profile. Harris/Ribeiro/Yin later extend the known law to unequal m,n, but no same sharp shape profile identified in material consulted. Best-of-knowledge original analytical classification despite derivability from prior formula.

## value

PASS

The exact marginal of the parking process is a natural observable; classifying every possible shape and tie as p varies and the nontrivial macroscopic trough migration at 1/n bias gives a meaningful asymptotic transition that does not appear by inspection of the distribution formula alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
