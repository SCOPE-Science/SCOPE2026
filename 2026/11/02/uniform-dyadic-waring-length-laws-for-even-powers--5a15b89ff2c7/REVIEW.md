# Independent mathematical audit

## correctness

PASS

For every even integer k>=4, s=v2(k), m=s+2, B=2^m<=2^k. Odd kth powers in Z2 are exactly 1+B Z2 and even kth powers lie in 2^k Z2. For t<B represented sums split disjointly into h+B Z2 for 1<=h<=t (h odd bases), plus 2^k times the same t-summand set; no cancellation between branches. Consequently A_{k,t}(n)=min(t+1,2^n) for n<=m, t2^{n-m}+1 for m<n<=k, and t2^{n-m}+A(n-k) for n>k; t=B covers all residues. Induction gives the exact periodically bounded discrepancy from c2^n with c=t/[B(1-2^-k)]. Stripping valuation in blocks k gives pointwise minimal length rho if nonzero normalized rho mod B, else B. Disjoint Haar layers give probability 2^k/[B(2^k-1)] for each t<B and (2^k-B)/[B(2^k-1)] for t=B. Restriction k>=4 even, zero-length at a=0 and t=0 treated explicitly.

## originality

PASS

Qualified PASS: unit kth-power image and extremal Waring number over Z2 are known from Kowalczyk–Miska; Arias–Borja–Anaya already compute the k=4 finite census for 3<=t<=15. The all-even-k exact finite modulus and full probability distribution are not given there, but are elementary developments of this prior structural fact; older Small 1977 paper full text unavailable.

## value

PASS

Complete uniform finite-modulus counting and entire Haar minimal-length distribution for all even exponents is a natural arithmetical representation invariant, substantially finer than maximal length alone and extends a known fourth-power census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
