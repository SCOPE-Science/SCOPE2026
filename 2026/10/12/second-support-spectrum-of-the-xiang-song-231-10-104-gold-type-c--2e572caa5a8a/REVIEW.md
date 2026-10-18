# Independent mathematical audit

## correctness

PASS

Reconstructed F_1024 using the displayed primitive degree-10 polynomial (x^10+x^6+x^5+x^3+x^2+x+1), verified generator order 1023 and absolute trace, built the defining set D of 231 coordinates, and independently obtained the 1023 nonzero codewords with ordinary frequencies 132 weight104, 396 weight112, 396 weight120, 99 weight128. For any binary two-space {u,v,u+v}, support size is exactly half the sum of its three nonzero weights, establishing lower bound 156. Exhaustive unique enumeration of all ((2^10-1)(2^9-1))/3=174251 two-spaces by canonical message triple u<v<u^v gave spectrum {156:440,160:3564,164:13464,168:30558,172:45144,176:43362,180:26664,184:9306,188:1584,192:165}; all 440 minimizers have three weight104 words. This complete finite domain is itself a valid finite mathematical proof, unlike partial sampling; independent checker uses a fresh trace/reduction implementation and disjoint support arithmetic, not a copied table.

## originality

PASS

The primary Xiang–Song paper supplies the specific code construction and ordinary weight distribution but not its two-dimensional support spectrum or d2 minimizer count. The usual generalized Hamming weights framework and independently indexed spectra on other code families do not determine the additive incidence among weight classes here. Searches by length/dimension/distance, defining polynomial and 440 minima located no same-object published table.

## value

PASS

Second generalized Hamming weight is the standard first nontrivial higher-support invariant of a linear code, relevant to subcode support geometry and leakage. The exact 440 extremal subspaces and complete 174251-space distribution reveal additive incidence data absent from the ordinary weight enumerator. The finite census is natural and complete for a primary-source named trace code, not an arbitrary small slice or a recomputation of a known table; no all-family formula is required for independent value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
