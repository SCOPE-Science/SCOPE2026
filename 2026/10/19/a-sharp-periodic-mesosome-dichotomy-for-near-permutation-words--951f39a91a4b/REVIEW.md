# Scientific review: periodic mesosomes in near-permutation words

## Correctness — PASS

The claim is quantified for every integer \(q\ge2\) and every period containing exactly one duplicated symbol. The full proof reduces any prospective mesosome to equality of cyclic arcs of residue length. Singleton-letter uniqueness confines their symmetric difference to the two positions of the duplicated symbol. The exact cardinality \(2\min(r,n-r)\) then forces adjacent duplicates. The explicit distinct-conjugate witness of half-length \(n-1\) proves attainability, and residues rule out every shorter half-length. Circular class enumeration uses a singleton to establish primitivity, followed by a fused-pair bijection. The packaged direct-conjugacy checker independently agrees for every labeled necklace with \(2\le q\le7\). No infinite conclusion is inferred from those finite tests.

## Originality — PASS, with residual uncertainty

[1] develops mesosomes and explicitly treats binary alphabets; its proofs do not cover periods on \(q\ge3\) individually distinguished letters. [2] studies applying one alphabet permutation or transformation to an entire half, which is not the same condition as rotating its positions. Its stronger-looking existence assertions do not imply which near-permutation periods avoid positional-conjugate factors, nor their exact shortest length and class counts. Targeted record searches found no statement equivalent to the theorem; broader circular repetition literature can cover stricter square-avoidance questions without classifying non-square mesosomes. Equivalence in unindexed or differently named literature remains a risk, so novelty is not claimed as formally certified.

## Mathematical value — PASS

The first noninjective circular content family—exactly one collision of two equal letters—has a sharp, nontrivial dichotomy between permanent avoidance and a forced mesosome of the exact shortest possible length. Unlike pure-permutation periods, the words here contain repeated symbols; unlike general high-multiplicity periods, the theorem supplies a complete classification and an explicit factorial necklace distribution for every alphabet size. The boundary separates arbitrarily long periodic avoidance from immediate finite witnesses and supplies a natural base case for extending mesosome theory beyond binary words.

## Closest literature and limitations

[1] R. Cummings, J. Shallit, P. Staadecker, *Mesosome Avoidance* (2021), arXiv:2107.13813v1; full text consulted.

[2] T. Ng, P. Ochem, N. Rampersad, J. Shallit, *New results on pseudosquare avoidance* (2019), arXiv:1904.09157v1; relevant full sections on alphabet permutations and transformations consulted.

The result excludes other multisets, ordinary-square avoidance and arbitrary aperiodic words. Computational checks run only through seven letters, while the proof covers every finite alphabet size. Independent audit is outstanding.

Self-review: passed. Independent audit: not yet performed.
