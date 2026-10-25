# Independent mathematical audit

## correctness

PASS

From normalized Bergman monomials e_k=sqrt(k+1)z^k, direct integration yields two forward weights w_(k,h)=h sqrt(k+1)/((k+h)sqrt(k+h+1)). The self-commutator has diagonal d_k and only q=n-m offdiagonals. Exact rational/square-root expansions give d_k=-2Q/k^3+6P/k^4+O(k^-5), c_k proportional to -B/k^3 with B=mn(m+n)|ab|; gauging remote chains gives quadratic form sum V_k |x_k|^2 - sum beta_k |x_(k+q)-x_k|^2. The leading V coefficient is 2(B-Q)/k^3 and Q-B=m^3|b|^2(r-n/m)(r-(n/m)^2). The k^-4 critical coefficient W has positive value 4n^2(n-m)^2|b|^2 at lower ratio n/m, but negative -2n^3(n-m)^2|b|^2/m at upper ratio (n/m)^2; remote tent test functions with L approximately K^(3/4) establish infinitely many positive directions at lower endpoint, while negative V tails bound positive index elsewhere. Negative diagonal gives infinitely many negative eigenvalues. T_g Hilbert–Schmidt implies H trace class, trace zero; band-tail norm O(N^-3) and negative separated coordinate compressions give s_j(H) comparable to j^-3 and S_p iff p>1/3. No individual eigenvalue formula or sharp coefficient in s_j claimed. Independently reproduced exact sympy Laurent coefficients for (m,n)=(1,2),(2,3),(2,5),(3,7); the source verify.py was inspected but not treated as proof.

## originality

PASS

The 1997 Bergman integration paper and 2013 Dirichlet/Bergman Schatten theory concern membership of T_g, not sign-sensitive inertia of T_g*T_g-T_gT_g*. Classical Cesàro self-commutator has a matching cubic power but is a different operator. No direct binomial signed-inertia phase diagram or asymmetric endpoints located. Some relevant historical full text not independently inspected; originality is qualified.

## value

PASS

The complete two-parameter positive-eigenvalue-infinity phase with opposite inclusivity of the two exact algebraic endpoints is a nontrivial spectral classification of a natural operator; the trace-class zero-trace condition alone does not predict the sign boundary. Sharp j^-3 decay yields a meaningful Schatten cutoff.

The dated certificate retains the supplied scientific assessment, sources and limitations.
