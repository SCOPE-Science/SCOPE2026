# Independent mathematical audit

## correctness

PASS

Let d=a-1 and (a-1)n=ax+(a+k)y. Mod d yields x+(k+1)y=dt for some t>=1 unless n=0; substitution n=at-ky with 0<=y<=floor(dt/(k+1)). Thus the t-th represented arithmetic progression has initial u_t=at-k floor(dt/(k+1)), terminal at, step k, with u_t>0. The floor increments give u_(t+k)<=at+k and u_(t+k)>=u_t+k; hence for each initial t in 1..k the successive progressions link without gaps, and gcd(a,k)=1 makes their k residues distinct. This proves full semigroup and gap-tail decomposition, Hilbert series, Frobenius max_t(u_t-k), and genus sum floor((u_t-1)/k) for every a>=2,k>=1. At k=2 (a odd >=3) thresholds O,E satisfy O>=3, O<E<=2O and E=2O or 2O-2; odd members below O+E and even members below 2O are indecomposable, with all larger decomposable, yielding the displayed minimal generator intervals and embedding dimension=multiplicity O, unbounded. Independent exact two-coin criterion checked 761 coprime pairs and 51610 memberships, including k=2 examples; these are finite support for the floor-inequality proof.

## originality

PASS

The candidate is a uniform explicit full residue-tail equality for the specific d=a-1 family and an explicit k=2 unbounded MED generator classification. Older general two-generator quotient algorithms and genus formulas are acknowledged as covering calculability and some consequences, not treated as new. Inspected general results do not state the full linked-parameter closed formula as written; PASS only as a best-knowledge specialized structural result, with real risk of derivability or prior exact specialization in Cabanillas/Liu.

## value

PASS

A complete explicit two-parameter residue-tail model of a numerical semigroup quotient (all gaps, Hilbert series and minimal generators for k=2) is a natural arithmetic invariant beyond computing isolated Frobenius numbers. The difference-two family supplies nonordinary unbounded maximal-embedding-dimension semigroups with a directly usable minimal generator structure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
