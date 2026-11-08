# Independent mathematical audit

## correctness

PASS

For q=3,4 and n>=17, start from the published unrestricted maximum 1+binom(n,2). Coordinatewise normalization sends a chosen codeword to zero, leaving weight-two and weight-four layers. The six alternative non-common-core upper bounds in Lin–Djaljapayan–Yu Theorem 7.1 (4n+32,6n+25,4n+22,4n+26,4n+17,7n-11) are strictly below 1+binom(n,2) at n=17 and have smaller increments thereafter; independently checked gaps at 17,18,25,100. With no weight-four words, their isolated-support deficit Eq.(5) forces exactly one word per pair and symbol matching on each coordinate, hence the complete binary-alternative two-flip shell. Otherwise all four-supports share a fixed core pair with three disjoint external edges. Lemma 6.1 bounds |C4|<=binom(n-2,2) and |C2|<=2n-3; optimum forces equality in both. Erasing the core produces a full synchronized weight-two shell on n-2>=15 outer coordinates; any weight-two support must touch the core, and every core or spoke support occurs exactly once. Distance-three exclusions force core and outer symbols to match the weight-four layer, yielding a two-flip shell about the core word. Its center is unique because a noncentral pair word has a disjoint pair word at distance four, and alternatives are uniquely read from the shell, giving (q(q-1))^n distinct labeled codes and one Hamming-isometry orbit. The infinite rigidity uses the published structural lemmas and proof, not the nonexhaustive construction scripts.

## originality

PASS

Lin–Djaljapayan–Yu October 2026 proves the maximum code size and supplies the canonical construction and decisive combinatorial inequalities. The primary paper was read through the relevant original full-text sections; it does not state the equality-case unique binary shell classification, labeled count (q(q-1))^n, or uniqueness of center as a theorem. The claimed new inference uses equality saturation and symbol synchronization in the known bounds. The companion q>=5 paper and older binary size bounds do not imply all q3,q4 extremizers.

## value

PASS

The optimum size and standard shell example were already known, but a complete classification of all extremizers is mathematically stronger: ruling out noncanonical codes, proving a unique shell center and fixed alternative symbols, determining one orbit and a closed labeled count for every n>=17. This is a natural sharp rigidity question in extremal Hamming coding, not a numerical recomputation of the old maximum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
