# Independent mathematical audit

## correctness

PASS

I reconstructed the Kummer inputs directly from the displayed equation: the right side as a rational polynomial in u has q simple zeros of A=u^q-u with exponent 1, b=q(q-1) simple B-zeros with exponent r=(q^(n−1)-1)/(q−1), and pole degree Q=q^n. For even n, gcd(r,N=q^n+1)=1, as do gcd(1,N), gcd(Q,N), so all q²+1 finite/at-infinity branch places ramify fully. Tame Kummer Riemann–Hurwitz (p does not divide N) gives genus (q²−1)Q/2 independently of an inaccessible cited paper. The functions f_j=z^j/B(u)^floor(jr/N) have nonnegative valuation at every finite branch place, giving nongap orders w_j=qj+b(jr mod N). As gcd(r,N)=1 these represent every residue mod N; their sum/gap formula equals the calculated genus, so they are the complete Apéry set. Lattice fan rays with determinant N generate each nonnegative congruent (j,a), proving the complete progression <m,m+b,...,m+bK=Q,N>. Since 2m>N all listed generators are minimal. The largest Apéry order is w_m=q m+bQ, giving conductor q m+(b−1)Q and defect 2g−conductor=q²(q−1)K>0 (nonsymmetric). Independent Dijkstra residue-graph checks for (q,n)=(3,4),(4,4),(5,4),(3,6) agreed with all arithmetic assertions and computed the independent Apéry minima. Original source local valuation and genus descriptions remain a literature comparison/access limitation, but the Kummer equation itself suffices to rederive the needed tame ramification.

## originality

PASS

PASS best of knowledge with specific credit: Ma–Wang Lemma 4.1 already gives EVERY candidate progression element individually as nongaps, so their existence is NOT new. The claimed new information is exact semigroup equality, full Apéry set, minimality, conductor, embedding dimension and non-symmetry. Montanucci–Pallozzi Lavorante's closest complete semigroup theorem assumes odd n>=5 and does not cover this even family. The originating paper's inaccessible full text could contain a complete hidden statement; that material risk is expressly preserved and no whole-paper noncoverage asserted.

## value

PASS

The exact one-point Weierstrass semigroup of a recently introduced maximal-curve family is a canonical geometric invariant determining pole-order gaps and the dimensions of one-point code spaces. Uniform completeness, conductor, minimal generators and nonsymmetry for all even n>=4, q>2 go beyond the established inclusion of progression nongaps, and are a natural complete classification of an infinite family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
