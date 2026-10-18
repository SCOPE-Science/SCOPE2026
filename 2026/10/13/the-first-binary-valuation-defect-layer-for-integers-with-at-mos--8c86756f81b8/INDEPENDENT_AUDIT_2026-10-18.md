# Independent mathematical audit

## correctness

PASS

For Omega(n)<=2, the only shapes are p, p², pq. Write p+1=2^r u and q+1=2^s w (u,w odd). The explicit v2(sigma(p^a)) formula excludes odd prime squares, p=2^a (a>=2), and non-Mersenne odd primes; n=2 has defect 1. For n=2q defect=1 iff q Mersenne. For odd pq, the rational ratio pq/2^(r+s)=(u−2^(−r))(w−2^(−s)) lies in (1,2] only for p=3,q=5; all other u,w parity cases yield either defect 0 or >=2. Checked boundary p=3,q=5 gives 15/8. Independent exact integer sigma/omega sieve n<=20000 gave precisely [2,6,14,15,62,254,16382], matching the proposed fibre; source script has 200000 check, not claimed as independently rerun. Symbolic case partition, not the bounded sieve, establishes all allowed n.

## originality

PASS

The full prime-factorization description of the adjacent positive defect-one fibre under Omega(n)<=2 is not the zero-fibre theorem of Amdeberhan et al.; in particular 15 is a non-Mersenne semiprime with defect one. Algebraic case analysis is elementary but the resulting natural sharply bounded arithmetic classification is not a routine parameter substitution.

## value

PASS

The first positive deficit above a sharp arithmetical inequality is a natural fibre, not an arbitrary numerical slice. The exact characterization singles out the exceptional odd semiprime 15 and a Mersenne-prime family, potentially useful for adjacent-extremal sigma valuation investigations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
