# Review of the endpoint-gap saturation theorem

## Correctness — PASS

The stated word has exactly three markers and two zero runs of length \(m\). For any partition, the first output block is a suffix and the last is a prefix, proving both endpoint inequalities. Conversely, the five-piece construction, with \(A=m-s\), \(B=m-p\), \(i=\max(0,q-B)\), and \(j=B+i-q\), has nonnegative exponents and reverses to the prescribed output. Empty zero-only pieces can be omitted. Stars-and-bars counting subtracts two disjoint forbidden end-gap events and simplifies exactly to \((m+1)^3\). All quantifiers, the case \(m=0\), and partition boundaries are covered. The independent cut-mask enumeration agrees at all \(m\le7\). No finite experiment is used as an infinite proof.

## Originality — PASS, with access risk

The closest available primary full text, Mahalingam–Maity–Pandoh (2023), studies palindromic richness of block reversals and does not give the fixed-family endpoint-gap image theorem. The foundational Mahalingam–Maity–Pandoh–Raghavan (2021) abstract reports global maximum/minimum image cardinalities and equivalence classes rather than this exact family; its full text could not be examined, so subsumption remains a risk. Searches for three equally spaced markers, cube cardinalities, block inversion aliases, and the image language located no matching theorem in the research-record index or open literature. A000578 is the generic cube sequence, not an image count. Search nonmatches do not prove uniqueness.

## Mathematical value — PASS

A natural periodic three-marker word has a complete, efficiently testable image language: two elementary endpoint inequalities suffice for *every* attainable string. This gives a nontrivial exact image count for an infinite family under a multi-block permutation operation and a limiting reachable fraction of \(3/4\). The structural converse is central: the cube count alone, or an unmotivated small value table, would not explain reachability. The result is a natural complete sparse-word classification, not an arbitrary finite slice.

## Scope and remaining risks

The claim does not classify all words with three ones, unequal marker spacings, or any four-marker family. The independent audit has not been performed. A full-text comparison with the 2021 paper remains desirable; its abstract alone cannot rule out a stronger result there.

Self-review: passed. Independent audit: not yet performed.
