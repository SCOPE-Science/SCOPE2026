# Independent mathematical audit

## correctness

PASS

For the exact succession-merger kernel p_{j,k}=C(j-1,k-1)A_{k-1}/j!, j>=2, the transient matrix on states 2..n is triangular. Its diagonal entries satisfy q2=q3=1/2; recurrence A_m=m A_{m-1}+(m-1)A_{m-2} makes q4=11/24 and q_j strictly decreasing for j>=4. The 3-to-2 probability is 1/3>0, so the repeated 1/2 eigenvalue has a genuine Jordan link, visible from every n>=3 via positive p_{n,3}. Exact survival recursion gives S3(t)=2^-t(1+2t/3), and for n>=4 coefficient matching gives alpha_n=2 sum_{k<n}p_nk alpha_k/(1-2q_n), beta_n=(2 sum p_nk beta_k-alpha_n)/(1-2q_n). Positive alpha_n, all other eigenvalues <=11/24, and n4 exact (6t-60)2^-t+61(11/24)^t prove the fixed-n asymptotic and its sharp second base. The PGF recursion has a genuine order-two pole at z=2 and e^s moment boundary s<log 2 (n>=2), with n1=0. Independently recomputed exact permutation transition row sums and q_j through j=8; finite checks supplement the general triangular-spectrum proof. No n-uniform remainder or n-to-infinity limit is implied.

## originality

PASS

Best-of-knowledge PASS for a fixed-initial-size long-time double-Jordan-pole asymptotic with explicit nonzero linear prefactors and universal sharp second eigenvalue. Same-process Rao et al (2016) is a serious inaccessible-text priority risk, not automatically a scientific FAIL.

## value

PASS

For a natural absorbing combinatorial Markov chain, the repeated 1/2 mode yields an unusually persistent t2^-t far-tail bottleneck invisible in the previously emphasized n-growing CLT. Exact coefficients, sharp universal 11/24 secondary rate, and exponential-moment threshold quantitatively describe rare very-long runs for each initial size. This is motivated spectral/rare-event information, not novelty of generic finite-state rationality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
