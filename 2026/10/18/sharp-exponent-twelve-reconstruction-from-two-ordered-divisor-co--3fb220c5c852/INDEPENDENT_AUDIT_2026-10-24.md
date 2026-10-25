# Independent mathematical audit

## correctness

PASS

By stars-and-bars d_k(n)=prod_e binomial(e+k-1,k-1)^c_e. For exponent bound 12, six prime valuations (2,3,5,7,11,13) of d2 and d3 give a 12-by-12 integer matrix with columns e=1..12. Independently reconstructed all entries from definition and calculated exact det=1 and rank12 via SymPy, forcing equality of multiplicity vectors c_e from equal statistic pairs. Directly verified exponent multisets {2,2,13} and {1,6,8} both yield d2=126,d3=3780, disproving bound13. The bound is independent of number of distinct prime bases; prime identities themselves cannot be recovered.

## originality

PASS

The stars-and-bars ordered-divisor formulas are classical. Huxley–Lettington–Schmidt addresses associated divisor function polynomials, squarefree factors, sum systems and Dirichlet series, not the exact two-statistic injectivity cutoff with 12x12 unimodular recovery. Qualified originality survives inspected prior implications.

## value

PASS

How far a pair of natural low-order divisor-count statistics recovers the prime-exponent fingerprint is a meaningful inverse arithmetic question. Exact determinant-unimodularity through exponent12 and a sharp exponent13 collision provide a reusable finite characterization, rather than arbitrary enumerated parameter slices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
