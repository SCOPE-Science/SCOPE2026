# Independent mathematical audit

## correctness

PASS

The frozen claim that the covariance is always negative when r+s>n lacked the individual bound: e.g. n=4,r=1,s=5 gives C5 identically zero and covariance zero. The complete replacement RESULT.md now states strict negativity only for distinct lengths both at most n, with the zero case explicit. SLOGAN.txt also now specifies n>=4 for rigidity. Independently checked the repaired theorem: shifting marked cycle counts in the Ewens law leaves the normalizer ratio Fn(m), times the marking factors; q[a]=(n-a)/(D-a), D=n+theta-1, is strictly monotone in a with sign of increment 1-theta, giving all feasible product comparisons. For fixed r,s, summing log q[r+a]-log q[a] cancels the order 1/n terms and gives -(theta-1)rs/n²+O(n^-3), yielding the stated covariance limit. At theta=1 the ratio is constant and at theta=2 it is affine in marked size, giving respectively 0 and -4/(n+1)². For necessity, Cov(C1,Cs)=-theta²(theta-1)Fn(s)/(D(D-s)) for admissible s>=2. In subtracting the s=3 value from s=2 the remaining factor is 1-(n-2)/(D-3)=(theta-2)/(D-3); every denominator factor is positive, including at n=4. This proves the iff across the full domain. The frozen finite verification is corroboration only; its loops sample lengths at most n and cannot justify the original out-of-range wording. No frozen script was executed.

## originality

PASS

Credit the repaired finding only for classifying the positive theta that give equal covariance on all admissible distinct-length pairs in the unconditioned law for each n>=4. The classical law, marked moments, and direct sign and asymptotic calculations are acknowledged input or context, not separate originality credit. The strongest retrieved neighbor results do not classify this uniformity or establish a structural theorem covering it.

## value

PASS

The admissible range removes the unavoidable incompatibility of pairs whose total length exceeds n. Classifying exact constancy within that range distinguishes an exceptional nonzero covariance profile from uniform-permutation cancellation and from the generic merely asymptotic coincidence of length coefficients. The precise finite-n classification, not re-evaluating the familiar sampling formula, is the useful contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
