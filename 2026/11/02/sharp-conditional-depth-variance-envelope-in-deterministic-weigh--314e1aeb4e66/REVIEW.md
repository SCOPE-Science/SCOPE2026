# Independent mathematical audit

## correctness

PASS

For arbitrary deterministic positive weights, p_j=w_j/W_j in (0,1), the actual innovation-variance recurrence v_{j+1}=(1-p_j^2)v_j+p_j(1-p_j) with v_2=0 is cited from Gałązka--Wdowicka Proposition 5.3 and is independently consistent with parent-choice conditioning. Completing the square gives v_{j+1}=G(v_j)-(v_j+1)(p_j-1/[2(v_j+1)])^2, G(x)=x+1/[4(x+1)] strictly increasing for x>=0. Thus induction gives attained B_{j+1}=G(B_j) and unique fractions p_j=1/[2(B_j+1)] for j<n; all such fractions correspond to positive weights. Subtraction yields the exact nonnegative stability recursion. Squared shift b_{j+1}^2-b_j^2=1/2+1/(16b_j^2), b_j^2=j/2+O(log j), leads to (B_n+1)^2=n/2+(log n)/8+O(1). Independently recomputed exact rational deficit for four nonoptimal fractions, equality and dominance at every step; no numerical extrapolation proves the asymptotic.

## originality

PASS

Qualified PASS: Gałązka and Wdowicka prove the same universal variance recursion as a premise, but their path-length martingale study does not optimize it over the entire positive weight class. The global unique optimal control, exact deficit and logarithmic second-order asymptotic are new conclusions relative to the inspected source; an old generic deterministic-control result may be an alternative derivation.

## value

PASS

The expected conditional depth variance of the next vertex is a natural quantifier of uncertainty under preferential tree attachment. The all-weights sharp envelope, uniquely realizable evolving policy and stability identity solve a real extremal design question beyond fixed power laws; the sqrt(n) optimal regime and log correction are nontrivial.

The dated certificate retains the supplied scientific assessment, sources and limitations.
