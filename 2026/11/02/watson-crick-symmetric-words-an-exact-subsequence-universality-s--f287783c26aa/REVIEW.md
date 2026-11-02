# Self-review

## Correctness — PASS

The claimed all-parameter statement is reconstructed from three steps: (i) disjoint rich-interval packing across a reverse-complement midpoint gives the exact \(2r\) or \(2r+1\) index; (ii) unique arch factorization and surjective-word generating functions produce the three rational components; and (iii) an exact shortest-host argument identifies permutation blocks and counts invariant central blocks. The cross-midpoint necessity uses greedy left-end minimality and its reversed right analogue, not any empirical extrapolation. Independently specified literal subsequence enumeration and exact coefficient comparison returned `WC_UNIVERSAL_VERIFY_OK symmetric_hosts=32199 literal_checks=2647 bivariate_profiles=24 shortest_classifications=10`. All lengths, pairings, and index conventions are explicitly scoped.

## Originality — PASS, subject to residual literature uncertainty

The closest discovered primary predecessor is Barker et al. (2020), especially Proposition 15 on ordinary palindromes and Proposition 18 on a word concatenated with a letter-permuted image. The first has the identity reversal but not complement pairing; the second has symbol relabeling but not word reversal. Neither directly gives the stated central orbit-cover condition and all-alphabet distribution of reverse-complement-fixed words. Mahalingam et al. (2020) establish the Watson–Crick palindromic/conjugacy setting but do not study scattered subsequence universality. Schnoebelen and Veron (2023) give general index algorithms. Relevant research-record searches identified unconstrained universal-word enumeration and palindromic duplication codes but no equivalent symmetric index spectrum. An inaccessible or unindexed equivalent statement remains possible.

## Value — PASS

The Watson–Crick involution is a natural symmetry in theoretical DNA strings. It is not an arbitrary slice of universal words: the symmetry imposes exact pair-orbit coverage in the unfinished arch, and the result resolves the entire length/index distribution, shortest possible length, and *all* shortest hosts simultaneously for every even alphabet. The sharp observation that this symmetry incurs no minimum-length cost at odd indices, unlike ordinary palindromicity, gives structural motivation beyond a single numerical count. No biological efficacy or independent novelty validation is claimed.

Self-review: passed. Independent audit: not yet performed.
