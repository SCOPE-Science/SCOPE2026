# Independent mathematical audit

## correctness

PASS

For sample size n-1 the hypergeometric count takes j-1,j with probabilities p=j/n,q. The binomial comparator has equal mass at those two points b=binom(n,j)p^j q^(n-j), so D_n(j)=-log(b)-h(p) exactly. Uniform Stirling away from p=0,1 yields F_n=0.5 log(2 pi n)+G(p)+A(p)/n+O(n^-3), G=0.5log(pq)-h(p), A=(1/p+1/q-1)/12. Endpoint exclusion plus unique maximizer G(1/2) localizes all integer argmax. At p=1/2+delta, G-G0=-(8/3)delta^4+..., A-A0=(4/3)delta²+..., giving δ=O(n^-1/2) and rescaled f(x)=4x²/3-8x⁴/3 with maxima x=±1/2, gain 1/6. Direct high-precision enumerations at n=100,400,1600 verify displacement and gain trends; no finite-n uniqueness claimed.

## originality

PASS

Comparison literature develops KL inequalities and fixed-fraction hypergeometric/binomial divergence, but the sample size here is n-1 and the target is maximizing composition with a square-root imbalance. Checked relevant primary Johnson–Gavalakis–Kontoyiannis full HTML; no direct implication of this near-census exact extremum from quoted existing theorems. Priority risk for unnoticed saddlepoint tables remains.

## value

PASS

The extremal composition of a canonical information divergence is unexpectedly not balanced; the degenerate quartic saddle plus 1/n correction produces an exact universal square-root displacement and second-order gain. A natural exact near-census invariant useful for finite population comparison.

The dated certificate retains the supplied scientific assessment, sources and limitations.
