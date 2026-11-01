# Scientific review: shortest one-joker scattered-subsequence covers

## Correctness — PASS

The claim has explicit quantifiers \(q\ge2\) and \(k\ge1\) and a per-target single-symbol matching definition for the joker. The all-equal-symbol targets force at least \(k-1\) ordinary copies of each alphabet letter, proving the minimum-length lower bound. At equality, the target \(b^{r+1}a^{k-r-1}\) rules out unequal numbers of \(a\) and \(b\) before the joker. Appending a repeated copy of the last letter of an absent prefix pattern forces both ordinary sides to be universal. A proved greedy-arch lemma characterizes minimum-length ordinary universal words as concatenations of permutations. This yields the exact iff classification and a nonovercounting enumeration. Explicit construction proves attainability. The finite verification covers 18 parameter pairs and 61,609 hosts, but is corroboration rather than a substitute for the proof. No boundary cases are omitted.

## Originality — PASS with bounded-literature risk

Barker et al. (arXiv:2003.04629v1, 2020) treat scattered subsequence universality for ordinary hosts, including the classical arch factorization; the wildcard-host minimum classification is not stated there. Adamson (arXiv:2304.04583v1, 2023) counts ordinary hosts, not joker hosts. Chen et al. (arXiv:1601.06456, 2016) study joker hosts but require contiguous targets exactly once, not scattered subsequences at least once. Adamson et al. (arXiv:2311.10658v1, 2023) study universal ordinary words in regular languages, rather than a set of target-dependent completions of a single partial host. The closest accessible related record on insertion distance measures ordinary-symbol insertions and does not imply this joker placement or enumerator. Targeted query searches found no statement-equivalent result. The nonexistence of an unindexed specialization is not established; it is a residual risk.

## Mathematical value — PASS

The object is a natural partial-word analogue of minimum-length universal supersequences, relevant when a single wildcard position can stand for any missing letter in distinct patterns. The theorem supplies an exact all-alphabet, all-order minimum, rigid characterization of **all** optimizers, and exact cardinality. The forced equality of prefix symbol counts and exclusion of joker positions internal to permutation rounds are genuine structural constraints rather than numeric examples or a direct substitution into an ordinary-word formula. It gives the entire minimal design space, not an arbitrary finite slice. No claim is made about longer, multiple-joker, cyclic or uniquely-occurring designs.

## Residual scientific limitations

The theorem is self-contained and the finite program tests only the stated ranges. A differently named characterization in unindexed partial-word literature could duplicate part of the result, and the classification is not an independent external validation. Comparison of available primary full text and accessible related summaries does not yield absolute uniqueness.

Self-review: passed. Independent audit: not yet performed.
