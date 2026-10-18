# Independent mathematical audit

## correctness

PASS

For each finite field F_q and 3-element E, the unordered nonconstant evaluation image of ax+b is aE+b, and two nonconstant messages give the same output iff their maps differ by affine set stabilizer H_E. The H_E action is free on affine parameter pairs so every nonconstant fiber has cardinality |H_E|, with q(q-1)/|H_E| such outputs; constant fibers are singleton. Faithful action H_E↪S3 leaves orders 1,2,3,6. Characteristic2 has no affine involution preserving odd triples, but primitive cube-root multiplication gives q(q-1)/3 order-3 triples if 3|q-1. Characteristic3 arithmetic progression triples are translation cosets with full six-element stabilizer, q(q-1)/6 of them; otherwise H_E trivial. Other odd characteristics yield q(q-1)/2 midpoint/arithmetic triples of order2, and q(q-1)/3 disjoint cube-root orbit triples of order3 only if 3|q-1; the rest order1. Verified independent exact affine-group/stabilizer enumeration for q=3 (one order6), q=5 (10 order2), q=7 (21 order2 plus 14 order3), q=8 (56 order1), plus direct unordered message fibers for those fields. First admissible q=8: every triple is rigid, thus all q^2=64 messages have distinct unordered outputs; q<8 prime powers 2,3,4,5,7 fail by classifications. The all-prime-power result rests on stabilizer orbit theory, not finite samples.

## originality

PASS

Zhang–Sun–Zhang–Ge 2026 full accessible paper concerns coordinate permutations PLUS insertion/deletion and polynomial-size alphabet constructions; checked sections do not give a complete q-dependent three-set affine stabilizer histogram. Camps-Moreno et al 2026 characterize global coordinate-permutation automorphisms for 1<k<n-1, which specifically EXCLUDES n=3,k=2; a related one-way affine inclusion is not the unordered message fiber count. Con–Shpilka–Tamo 2024 treats two-dimensional insertion/deletion codes, not exact zero-edit triple orbit enumeration in accessible summary. Resultary 3-point Fourier/perfect-hash findings use different objects and do not imply this classification.

## value

PASS

Loss of coordinate identities is the natural zero-edit obstruction to coordinate-permutation coding. The complete field-characteristic-dependent collision multiplicities and the sharp first field q=8 determine a motivated exact invariant of a fundamental Reed–Solomon boundary instance, usable for selecting viable evaluation sets. A full classification is intrinsically useful even without an asymptotic code-rate theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
