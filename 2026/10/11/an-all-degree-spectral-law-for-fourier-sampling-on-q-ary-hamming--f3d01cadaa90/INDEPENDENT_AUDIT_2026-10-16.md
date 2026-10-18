# Independent mathematical audit

## correctness

PASS

For all integers q>=3, n>=2 and 1<=d<=min(k,n-k), the contrast/activity tensor decomposition is valid for the cyclic alphabet without a finite-field assumption. Restricting a fixed s-contrast sector reduces its Gramian to biased Bernoulli weight-(k-s) restriction; harmonic coefficient degree j has dimension C(n-s,j)-C(n-s,j-1), and the raising-incidence identity yields the stated normalization. The generating-function identity restricts every lifted F_{a,h} to kappa_{s,j,a} H_h, a rank-one block in radial lifting degree. Summing positive multiplicities gives rank C(n,d)(q-1)^d; activity equation L=(sum 1_{xi !=0}-k) multiplies H_{<=d-1} injectively under the interior bound, hence its image has exactly the remaining nullity. Independently formed complex Fourier Gram matrices on full G and shells at (q,n,k,d)=(3,4,2,2),(4,4,2,2),(3,5,2,2),(3,4,1,1). Their positive ranks 24,54,40,8 and zero multiplicities 9,13,11,1 agree with all formula eigenvalues, max numerical error below 1.2e-15; finite tests corroborate, not prove, the quantified harmonic argument. Inspected actual frozen RESULT.md and artifacts/verify.py, not just VERIFY_OK.

## originality

PASS

The explicit rational ALL-degree spectrum including positive multiplicities and one-equation full kernel is a broader statement than previously published d=1 and d=2 formulas and than classical binary Johnson harmonic bases. The cited general association-scheme representations do not by themselves explicitly give this q-ary Fourier-band compression spectrum; best-of-knowledge PASS with risk of implicit historical Terwilliger reductions.

## value

PASS

A natural complete spectral classification of an unsymmetrized, degree-truncated Fourier sampling operator. The rank, exact kernel and quotient singular values quantify recoverable bandlimited data for every interior shell and arbitrary degree; the d>=3 regime is genuine new higher-harmonic structure rather than merely recomputing a low-degree table. No asymptotic condition-number theorem is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
