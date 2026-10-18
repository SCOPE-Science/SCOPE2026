# Independent mathematical audit

## correctness

PASS

Let u>=3, j=2^u, r=j+u, M=2^r, N=M-j-1. For S_N=sum_{k=1}^N2^k/k in Q_2, both infinite log sum_{k>=1}2^k/k and dilog sum_{k>=1}2^k/k^2 vanish by 2-adic log(-1)=0 and Li_2(z)+Li_2(z/(z-1))=-log^2(1-z)/2 at z=2. Normalize -S_N as its tail by 2^(M-r). Endpoint k=M-j and k=M terms cancel to valuation j. Replacing intermediate (M-a)^(-1) by -a^(-1) has valuation >=3u-1 error; geometric expansion gives sum_{s>=1}2^(us)H_s. The s=1,2 layers vanish below j by full-series tails; s=3 has unique minimum b=4 with v2(2^b/b^3)=-2, giving 3u-2, while all s>=4 and endpoints remain >=3u-1. Hence v2(S_N)=M-r+3u-2. The known identity a_N=(N!/2^N)S_N and Legendre v2(N!/2^N)=-s2(N)=-(r-1) give v2(a_N)=M-2r+3u-1. Independent modular tail checks u=3..8 and full recurrence N=2039 match; finite tests are not the infinite proof.

## originality

PASS

Farhi (2022) establishes the recurrence/truncated-log representation; Dubickas (2024) proves a general lower bound with equality only at Mersenne indices. Those results do not specify this non-Mersenne sparse family or exact growing third-order excess, which requires new cancellation analysis. The classical p-adic dilogarithm functional identity is not claimed as novel. Related Resultary valuation findings concern other sequences. Search failures are not proof of universal novelty.

## value

PASS

The original problem is arithmetic divisibility of a natural integer sequence. An explicit infinite family of non-Mersenne indices with exact unbounded valuation excess reveals cancellation invisible to the sharp general lower bound and is a motivated precise invariant, not a random numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
