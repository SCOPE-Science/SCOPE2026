# Independent mathematical audit

## correctness

PASS

Totients of p²q/d give the four class sizes for d=p,pq,p²,q and sum to N. Adding truncated p- and q-valuations gives exactly the path of joins A–B–C–D, with only B internally complete. Two whites in any class form a fort. Conversely distinct primes ensure |A|,|D|≥2, so a blue A and D can remove a lone white B and C respectively, even if B or C is a singleton. The fully blue B and C then remove possible whites in A and D. Each class of size w therefore contributes u^(w−1)(u+w); multiplying gives the full polynomial and the product of the four class sizes as the minimum-set count. For real rank, the stated 4-by-4 class matrix has determinant 1 by expansion along the end rows, and its block lift has rank at most four and a nonsingular representative principal submatrix of order four. The lift has precisely the required off-diagonal pattern. Conversely a vector in the kernel of any graph-pattern matrix that is zero on a forcing set must be zero at the unique uncolored neighbor along each forcing step, so M≤Z gives rank at least four. This holds without assuming B or C has a blue mate. Independently checked all white sets by fort containment on directly multiplied residues at (p,q)=(2,3),(3,2),(2,5), agreeing with the full coefficients and omission criterion in each case. Replay: python3 /workspace/branches/independent_exact_checks.py, check_ring(). The packaged checker was inspected, not executed; the general result follows from the structural proof, not these samples.

## originality

PASS

The known zero-divisor graph framework, prior study of this graph family, twin obstructions, and general forcing-polynomial methods are not the distinct claims. The supported claims are the evaluation of every coefficient, every minimum set, and the matching real minimum rank for this nonlocal family including singleton middle classes. The compared statements do not settle the sufficient four-class forcing criterion or tight rank witness. The reported published gcd decomposition is credited as prior input rather than offered as an original result.

## value

PASS

The first nonsquarefree two-prime residue rings are a natural test family beyond local chain rings. The result gives explicit optimal seed choices and the entire forcing distribution from a simple arithmetic product, uniform in the singleton boundaries where twin-only reasoning cannot settle sufficiency. Independently it shows that the zero forcing lower bound for real rank is attained and that rank stays exactly four as the order grows. This is a concrete exact invariant and structural classification, not a new general compression method.

The dated certificate retains the supplied scientific assessment, sources and limitations.
