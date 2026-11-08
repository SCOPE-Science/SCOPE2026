# Independent mathematical audit

## correctness

PASS

PASS. Fourteen coordinates count length-1,2,3 binary scattered patterns with successive selected indices differing by >=3. Last-position partition gives C_i(p)=C_(i-1)(p)+[w_i=last(p)] C_max(0,i-3)(prefix(p)), including the empty-pattern convention. An independently written iterative exact-integer deck enumerator traversed EVERY binary word for n=7..17: all 2^n observations are distinct for 7<=n<=16; at n=17, 131072 words yield 131056 vectors, exactly 16 doubletons and no larger fiber. A second literal-index implementation independently matched all n=7..10, and direct checks of all 16 collision pairs and reversal/complement orbit actions corroborated the four size-four orbits (source file COLLISIONS.csv). This is a rigorously bounded finite census; nothing is claimed for n>=18 or vacuous n<7.

## originality

PASS

PASS best-of-knowledge. The gap-three multiplicity deck is different from ordinary deletion output sets and from the published two-separated gap case. Full original Golm et al. paper proves general bounds (41 at these parameters) but not this length-17 first informative threshold or exact 16-fiber first-failure census; Day et al. address constrained pattern sets, not their full multiplicities. Resultary nearest binary deletion-reconstruction record treats another channel and cannot imply this multiset observation. Nonindexed equivalent finite enumeration remains possible.

## value

PASS

PASS. The first failure of injectivity after length-three observations become genuinely available is a natural sharp reconstruction boundary. Complete first-failure fiber sizes and reversal/complement orbit classification quantify information loss and are not simply a single arbitrary collision witness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
