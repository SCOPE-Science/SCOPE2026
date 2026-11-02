# Scientific review

## Correctness — PASS

The complete claim is reconstructed for \(k\ge2\) and \(n\ge3k-2\), without cyclic wraparound. A length-\(k\) read containing two markers detects the interior zero gap up to threshold \(k-1\); the Euler/de Bruijn flow imbalance recovers both end vertices when they differ. The only equal-boundary, nonzero-vertex case requires an interior gap at least \(k-1\) and boundary-gap sum exactly \(k-2\); each of the \(k\) single-one reads then appears exactly once. All other clipped triples are separated. The count of capped triples, minus exactly \(k-2\) repeated labels, proves stabilization; the all-capped triple is exactly the missing boundary profile. The verifier independently checked all complete read vectors across 110 cases and 31,240 words, including both directions of the equivalence criterion. Unchecked large parameters are settled by the combinatorial proof, not extrapolated from experiments.

## Originality — PASS (best-knowledge), residual risk stated

The exact linear weight-two fiber classification is not supplied by the examined general profile enumeration or the constrained de Bruijn maximal-cycle theory. Kiah–Puleo–Milenkovic analyze DNA profile vectors, restricted de Bruijn graph flows, and quasipolynomial/asymptotic profile counts but not an explicit sparse two-marker length-independent saturation law. Chee et al. analyze RLL sequence length, cycle merging, and enumeration of allowed windows, not read-multiset collisions of length-\(n\) words with exactly two ones. Jacquet et al. study asymptotic Markov-type matrix counting. A related exact length-limited **composition** observation for weight-two sources differs by recording unordered symbol counts across all read lengths and does not imply this fixed-length **ordered** profile equality criterion. An equivalent specialization elsewhere in the large general Markov-type literature is possible, so this is a self-review best-knowledge conclusion rather than an independent uniqueness certificate.

## Value — PASS

The property is a natural constrained deterministic sequencing channel: the output contains exact multiplicities of every contiguous, ordered read of fixed length, while the source is restricted to two rare markers. The complete ambiguity relation yields an operationally exact zero-error capacity. A finite sharp stabilization threshold is unexpected when the input word length keeps increasing; the unique high-multiplicity exception is explained by the equality of de Bruijn path endpoints. The conclusion holds for every read length, not only a finite census; the exact boundary \(3k-2\) is independently distinguished.

## Closest literature and limits

Sources: Chee et al. (arXiv:2403.01454v1, Sections 2 and 4); Kiah et al. (arXiv:1502.00517v1, Sections 2 and 3); Jacquet et al. (DOI 10.46298/dmtcs.2768, abstract and scope). The statement is confined to all-n exact profile counts and fibers under linear, two-one, non-noisy reads. Possible unlocated specializations are a residual originality risk.

Self-review: passed. Independent audit: not yet performed.
