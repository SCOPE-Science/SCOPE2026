# Independent mathematical audit

## correctness

PASS

Encode independent sets as cyclic symbols 0,A,B; AA forbidden adjacent, BB forbidden two columns apart. Every length-5 window has a zero; the only nonzero four-run is ABBA, yielding α≤floor(4n/5) and matching templates. When n=5k, k zero-columns force five translates of (0ABBA)^k, each isolated under token jumps. When n=5k+4, exactly one nonzero run is length three (ABA/ABB/BBA), all others ABBA, so there are 3n optima X_i,Y_i,Z_i. A case analysis of single-symbol changes and moving a zero yields only X_i–Y_i, X_i–Z_i, Y_i–Z_{i+5}, each realizable as an edge-slide. Gcd(n,5)=1 makes this degree-two graph C_{3n}. Independently enumerated all optima and moves for n=5,9,10 from original 2n-vertex graph: counts5,27,5 and degrees0,2,0; n=9 was one 27-cycle. Inspected both exact source verification programs. These finite checks supplement the all-k word/run proof.

## originality

PASS

Known independence-number α=floor4n/5 and maximal-set counts are explicitly excluded as prior; the exact token-jump/sliding adjacency graph for both infinite residues is additional information not determined by mere counts. Generic token-sliding graph theory does not identify the given GP(n,2) optima.

## value

PASS

The explicit exchange geometry distinguishes a frozen optimum phase n≡0 mod5 and a fully connected cycle phase n≡4 mod5. It supplies natural optimization-landscape connectivity and diameter invariants for an established symmetric cubic graph family, not an arbitrary slice or known number restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
