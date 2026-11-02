# Exact all-length binary three-gram multispectrum capacity

## Finding

For each binary word \(w\in\{0,1\}^n\) with \(n\ge3\), let \(h_3(w)=(h_u(w))_{u\in\{0,1\}^3}\), where \(h_u(w)\) counts all contiguous occurrences of the three-letter word \(u\), with overlaps counted and without wraparound. Let \(T_n=|\{h_3(w):w\in\{0,1\}^n\}|\). Then

\[
\sum_{n\ge3}T_nz^n=\frac{z^3(8-9z+7z^2-3z^3+6z^4+5z^5-z^6+2z^7-5z^8+3z^9)}{(1-z)^5(1+z)(1+z^2)(1+z+z^2)}.
\]

In particular, \(T_n\) is a degree-four quasipolynomial with least quasipolynomial period \(12\),
\[
T_n=\frac{13}{288}n^4+O(n^3),
\]
while \((T_3,\ldots,T_{14})=(8,15,28,52,92,151,240,363,532,757,1048,1416)\). Equivalently \(T_n\) is the exact maximal size of a length-\(n\) binary codebook with pairwise distinct contiguous three-gram *multiplicity* profiles.

## Assumptions and scope

Words are finite and linear, on the labeled alphabet \(\{0,1\}\). Their length is any integer \(n\ge3\). The observation is the entire ordered eight-component count vector, rather than a set of present substrings, and there is no cyclic wrapping or quotient by reversal or bit-complementation. An optimal codebook simply selects one word from each observed profile class.

## Proof

Represent each three-gram as a directed edge from its first two symbols to its last two symbols. The resulting binary order-two de Bruijn directed multigraph has vertices \(00,01,10,11\) and eight edge labels \(000,001,010,011,100,101,110,111\). A nonzero edge-multiplicity vector comes from a word exactly when its nonzero-edge underlying graph is weakly connected and its outdegree-minus-indegree vector \(\delta\) is either zero or has a unique entry \(+1\) and a unique different entry \(-1\). This is the directed Euler-trail criterion; any trail spells a word, and conversely the windows of every word form a trail.

Write the loop multiplicities \(u=h_{000}\), \(v=h_{111}\), and the other six as \(a=h_{001}\), \(b=h_{010}\), \(c=h_{011}\), \(d=h_{100}\), \(e=h_{101}\), \(f=h_{110}\). Flow conservation yields the exact identities
\[
d=a-\delta_{00},\qquad f=c+\delta_{11},\qquad b=a+e+\delta_{01}-c.
\]
The number of edges, \(m=n-2\), therefore satisfies
\[
m=u+v+3a+2e+c+\delta_{01}-\delta_{00}+\delta_{11}.
\]

For each of the \(255\) possible nonempty supports of the eight edge labels, apply the weak-connectivity test, choose one of the \(13\) allowed imbalance vectors, and impose that each specified present multiplicity is at least one and each absent multiplicity is zero. These equations reduce all profiles to nonnegative triples \((a,e,c)\), with the displayed identities defining \(b,d,f\). The two loops contribute either the factor \(1\) when absent or \(z/(1-z)\) when present. The sum over \(c\) is an ordinary finite geometric sum: when \(b>0\), its upper limit is \(a+e+\delta_{01}-1\), and when \(b=0\), it is fixed at \(a+e+\delta_{01}\). All remaining sums have a product of two geometric tails with, where needed, only the finitely many pairs satisfying \(a+e<L\) removed; this yields rational functions by exact algebra, not numerical interpolation.

The accompanying `verify_threegram.py` performs that finite support/imbalance decomposition as executable exact-integer rational arithmetic. Its support screening includes \(143\) formally contributing connected support masks; contributions from \(22\) masks cancel identically, leaving \(121\) genuinely attainable supports. The calculation collects \(1058\) signed geometric-series terms under the common denominator
\[
(1-z)^3(1-z^2)(1-z^3)(1-z^4).
\]
It obtains numerator coefficients (in ascending degree)
\[
(0,8,-9,-1,6,-1,8,-7,-3,-4,1,5,-3).
\]
Cancelling \(1-z^2\) gives
\[
\sum_{m\ge1}T_{m+2}z^m=\frac{8z-9z^2+7z^3-3z^4+6z^5+5z^6-z^7+2z^8-5z^9+3z^{10}}{(1-z)^3(1-z^3)(1-z^4)},
\]
which is the announced formula after multiplication by \(z^2\). The verifier constructs each denominator and performs integer polynomial division with an explicit multiplication identity, so the displayed rational identity is exact for every formal coefficient.

The reduced numerator does not vanish at a primitive third root, a primitive fourth root, or \(-1\), and has value \(13\) at \(1\). Thus the displayed denominator is coprime to the numerator. Partial fractions imply an all-\(n\) quasipolynomial with period dividing \(\operatorname{lcm}(2,3,4)=12\); the uncancelled primitive third and fourth roots force its least period to be divisible by both three and four, hence exactly \(12\). At \(z=1\), the order-five pole coefficient is \(13/(2\cdot2\cdot3)=13/12\), giving leading coefficient \(13/(12\cdot4!)=13/288\).

## Verification

Run `python3 verify_threegram.py`; it recomputes the complete exact rational identity and independently enumerates all \(2^n\) binary words for \(3\le n\le14\). Run `g++ -O2 -std=c++17 verify_threegram_independent.cpp -o verify_threegram_independent` then `./verify_threegram_independent 85`; it enumerates integer flow vectors directly without symbolic support sums. The two approaches agree for the first \(85\) coefficients, through word length \(87\). `verification_output.txt` gives the actual recorded outcomes, and `threegram_independent_results.txt` gives all the independent values. These finite confirmations are supplementary; the infinite theorem follows from the algebraic support decomposition and exact symbolic evaluation above.

## Relationship to prior work

Alanko and Pérez-López (first public version September 26, 2025) count *distinct k-mer strings on walks within an input labeled graph* and construct de Bruijn data structures; that is different from counting all possible multiplicity vectors of binary words of given length. Tesler's multi-de-Bruijn theory counts words in which *every* k-mer has the same prescribed multiplicity, whereas here every attainable nonnegative and connected three-gram multiplicity vector is counted exactly once. Existing binary two-gram multispectrum formulas concern the smaller observation length, and sets of *present* three-grams discard multiplicity. The result uses the classical Euler-trail criterion but not a known closed count for arbitrary ternary-window multiplicities.

## Limitations

This concerns exactly binary, length-three contiguous windows with multiplicities and all word lengths \(n\ge3\). It gives no formula for longer windows, larger alphabets, or the sizes of individual ambiguity classes. No independent mathematical audit has been performed, and an unindexed or unpublished enumeration could affect priority.

## References

1. J. N. Alanko and M. Pérez-López, *Computing k-mers in Graphs*, arXiv:2509.22885, first submitted 2025-09-26, https://arxiv.org/abs/2509.22885; full text https://arxiv.org/html/2509.22885v2.
2. G. Tesler, *Multi de Bruijn Sequences*, *Journal of Combinatorics* 8 (2017), 439–474, arXiv:1708.03654, https://arxiv.org/html/1708.03654v1.
3. Classical directed Euler-trail characterization, applied to the directed binary order-two de Bruijn multigraph.
