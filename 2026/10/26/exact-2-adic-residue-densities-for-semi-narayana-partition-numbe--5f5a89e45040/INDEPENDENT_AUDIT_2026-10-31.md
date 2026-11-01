# Independent mathematical audit

## correctness

PASS

The generating function with digits 0,1,3 yields the asserted c(2m)=c(m), c(2m+1)=c(m)+c(m-1) recursion. The explicitly given A and B are unimodular; the 7 nonzero mod-2 states form one orbit. The congruences A^3=I+2E (mod4) and A^(3*2^(r-1))=I+2^r D (mod2^(r+1)), together with the 14 determinant-one conjugate displacement witnesses for all parity states, inductively imply transitivity on every primitive triple modulo 2^r. Averaging A/B gives an irreducible doubly stochastic finite Markov chain, aperiodic because A fixes (1,0,0); dyadic-cylinder decomposition upgrades fixed-length binary mixing to natural density at unrestricted cutoffs. Exact marginal and valuation fractions then follow by counting primitive triples. Independent recurrences and matrix-orbit sizes matched all primitive states modulo 2,4,8,16,32; the unbounded result rests on the lifting proof, not those bounded checks.

## originality

PASS

Ballantine–Beck prove parity for this same semi-Narayana coefficient sequence (even precisely n ≡3,5,6 mod7), implying the known even proportion 3/7. Their result does not imply a uniform joint distribution of three consecutive coefficients modulo every 2^r, nor the higher valuation distribution; these need the exhibited 2-adic matrix-lifting and Markov orbit argument. Relevant Resultary semantic search returned other 2-adic partition and Thue–Morse results, not this primitive-triple measure. Best-of-knowledge additional theorem, without asserting absence of all equivalent automata literature.

## value

PASS

The object is a natural restricted binary partition sequence whose parity structure was previously understood; the previously unknown joint distribution and full valuation profile give an exact, reusable arithmetic invariant, with an infinite family of moduli and genuine uniformity of primitive states rather than a trivial parity reformulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
