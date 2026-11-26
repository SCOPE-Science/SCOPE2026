# Independent mathematical audit

## correctness

PASS

The first coordinate leaves t=s-u, yielding the stated monic quartic in u. Any two distinct u give a unique common (s,y) because 2 is invertible, so the first two binomial moments are q^2 and binom(q,2). Vieta on three roots determines a fourth, possibly repeated, and requires Q=-1, where Q has ternary determinant 1/2; with a specified equality the binary determinant is 2. Thus the all-tuple counts are q^2+alpha q, q-beta and, at all equal, 1+gamma. Inclusion–exclusion gives D3=q^2+(alpha-3)q+2+3beta+2gamma. For four roots elimination yields the same Q; in the partition sieve the six single pairs, three double pairs and four triple equalities have weights -1,+1,+2 and counts q-beta,1+beta,1+gamma respectively. All equal is impossible. This yields D4=q^2+(alpha-6)q+11+9beta+8gamma. The moments D3/6 and D4/24, with the normalization and first two moments, invert to the five given counts, support size and energy. The stated Fourier factor q^-2 follows by unnormalized Parseval on F_q^2. N4=0 at q=5, N4=1 at q=7, and q^2-7q-6>0 beyond the next eligible order q=11. Independently enumerated actual ordered graph sums in seven prime fields and F_125 (irreducible X^3+X+1 over F_5), agreeing with every multiplicity count, including (5844,5228,3877,61,615) over F_125. Replay: python3 /workspace/reproduction/2.py; see 2.txt. Only the written finite-field argument establishes the formulas at all orders.

## originality

PASS

Best-of-knowledge pass for exact all-field multiplicity distribution of the stated mixed graph pair, equivalently the specified quartic coefficient family. Earlier short-interval asymptotics, subset-sum sieves and Fourier counting backgrounds are not new. The energy alone is elementary and is not the basis of this originality decision.

## value

PASS

The full fiber distribution is a natural arithmetic input for mixed convolution and finite-field graph incidence questions. It separates field-dependent high multiplicities invisible to the pair-collision energy and determines both exact support size and the sharp first fourfold fiber. This is a uniform classification for all eligible finite fields, not an isolated recomputation or an assertion about weighted extension norms.

The dated certificate retains the supplied scientific assessment, sources and limitations.
