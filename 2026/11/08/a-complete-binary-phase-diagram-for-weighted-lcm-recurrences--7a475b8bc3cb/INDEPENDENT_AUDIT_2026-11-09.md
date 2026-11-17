# Independent mathematical audit

## correctness

PASS

The exact factor b_n=n/gcd(n,A_{n-1}) gives nu2(b_n)=max(0,nu2(n)-nu2(A_{n-1})). With K even, internal dyadic-block indices have odd b_n; at powers of two valuation increases by exactly t=nu2(K+2) when previous V_r=r, hence b_n=2 and the claimed ceiling staircase. With K odd, all odd indices >=3 produce even multipliers; for even n>=6 their accumulated factors force nu2(A_{n-1})>=nu2(n), making b_n odd. Direct n=4 modulo12 computation gives {1,3,11}; all n>=5 multipliers are even, proving lower bound. Induction covers all n, not just tested n.

## originality

PASS

PASS for the coefficient-wide phase diagram, not the known K=2 staircase. Cloitre Proposition 6.5 establishes K=2 only; §7.4 raises other coefficients. OEIS has K=2 and related unweighted special cases, but not an all-positive-K even/odd dichotomy with K mod12 boundary. Uniform dyadic induction is a natural nontrivial extension; priority beyond indexed work remains qualified.

## value

PASS

The complete binary transition diagram for the natural weighted-LCM recurrence solves the coefficient-extension direction of its motivating source: infinite logarithmically sparse even increments for every even K versus finite support for all odd K, including a nontrivial mod12 boundary. A full parameter classification may be useful without settling primality of other increments.

The dated certificate retains the supplied scientific assessment, sources and limitations.
