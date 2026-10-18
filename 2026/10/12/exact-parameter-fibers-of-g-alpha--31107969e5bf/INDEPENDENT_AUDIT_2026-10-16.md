# Independent mathematical audit

## correctness

PASS

Unique factorization reduces g_alpha(n)=g_beta(n) to lcm(e_i,alpha)=lcm(e_i,beta) for every i. For each prime ell, write m=min_i v_ell(e_i)=v_ell(h). The max-vector (max(v_ell(e_i),v_ell(alpha)))_i is constant for valuations <=m and injective for valuations >m because some e_j has valuation exactly m. Thus equality is equivalent to equality of max(v_ell(alpha)-m,0) at every ell, precisely alpha/gcd(alpha,h)=beta/gcd(beta,h). For normalized s, primes ell dividing both h,s have alpha-valuation m+v_ell(s); primes in h not s have exponent 0..m; all other primes fixed. This gives alpha=s h_s d for d|h^(s), with tau(h^(s)) elements, h=1 injectivity and infinitely many output classes. Independently compared all pairs alpha,beta<=80 for exponent tuples (6,10),(12,24,36),(4,8,12),(3,5,7),(8).

## originality

PASS

PASS best-of-knowledge: Mittou 2023 Theorem 2.2 characterizes only the special fiber g_alpha(n)=n as alpha|gcd(e_i). The full 2025 Mittou follow-up Theorems 2.1-2.6 gives compositions/inequalities and a relation varying the base integer (same alpha), not the fixed-base relation between two parameters alpha,beta. The classification of every normalized s fiber and its exact cardinality is distinct from the known s=1 case. Proof elementary but the complete orbit/fiber invariant is not simply copied from a table.

## value

PASS

The g_alpha family is a named natural arithmetic-function construction. Knowing exactly when different parameter values are redundant gives a complete parameterization, computable fiber sizes, and a clean injectivity criterion for this family; a future study of composition/orbits can use these collision classes. Although short prime-adic reasoning, a full natural-family fiber classification can be independently useful; no contrived finite slice is involved.

The dated certificate retains the supplied scientific assessment, sources and limitations.
