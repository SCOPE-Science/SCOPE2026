# Independent mathematical audit

## correctness

PASS

In characteristic two the sparse polynomial satisfies the polynomial identity P(X+1)+P(X)=P_prime(X)=1+X^(2^(r-2))+X^(2^(m-2)). This additive derivative has kernel {0,1}, since gcd(m,m-r)=1, and image 1+ker(field trace) of cardinality q/2. For D(x)=F(x+a)-F(x), Taylor modulo 4 gives D(x+2u)-D(x)=2u(F_prime(x+a)-F_prime(x))=0 because P_prime(t+1)=P_prime(t); similarly D(x+a)-D(x)=2(aF_prime(x)-D(x))=0 because P difference equals P_prime at residue level. Thus D is constant on each paired union of two residue classes of size 2q. Distinct pairs have different output residues, so exactly q/2 occupied cells with multiplicity 2q, for every coefficient lift including higher-degree terms. Independent exact GF2 polynomial expansion verified nine admissible (m,r) pairs through m=11; this is corroboration, not an infinite all-lifts proof.

## originality

PASS

Fukui 2610.21178v1 proves two-to-one binary derivatives and general ordinary-unit rows, but explicitly leaves the residue-one exceptional case to an upper bound and small examples. Rønjom–Sandrib give the bound <=2q, not occupied output identities; 2610.21169 concerns a global optimum. Fukui 2610.21178v2 was posted October 27 after the frozen October 25 record and studies k>=3 for a special coefficient choice, rather than all GR(4,m) coefficient lifts; potential related lemma noted but not silently treated as earlier coverage.

## value

PASS

It determines the complete row, support and multiplicities in exactly the exceptional unit residue class left bounded but not tabulated in earlier general differential-uniformity theorems. Lift-independence at characteristic four and trace-hyperplane output structure are natural and potentially useful fine invariants beyond a uniform upper bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
