# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The proof uses only the basic minimal-vector properties of Ashikhmin and Barg.
Their Lemma 2.1 states that every minimal support has size at most \(n-k+1\),
that minimal vectors span the code, and that a nonminimal binary codeword splits
as a sum of two nonzero codewords with disjoint smaller supports.

Under the stated full-gap condition, the first property forces every minimal
word to have weight exactly \(d\). Recursively applying the disjoint-support
split terminates because support size strictly decreases, and it partitions any
nonzero codeword into minimum words. Weight additivity on disjoint supports then
gives \(d\)-divisibility.

For two distinct minimum words, divisibility applied to their sum gives
\(2d-2s\in\{d,2d\}\), where \(s\) is their support intersection. Hence
\(s\in\{d/2,0\}\). For odd \(d\), all minimum supports are disjoint. Since the
minimum words span and disjoint nonzero words are independent, exactly \(k\) of
them occur. The resulting direct-sum form makes the remaining parameter
calculation immediate: for odd \(d>1\), a full gap permits only \(k=1\), or
\(k=2,n=2d\).

A compact exhaustive checker enumerates all binary linear codes of length at
most 6 and dimension at most 3 and confirms the claimed divisibility and the
odd-distance restriction in every full-gap case encountered. These finite checks
support but do not replace the proof.

## Originality

He, arXiv:2609.20344v1, proves a mirror vanishing band from a shorter initial
weight gap under a rate hypothesis. The paper uses the same Ashikhmin--Barg
binary disjoint-decomposition lemma but states a local reflected interval around
\(2d\), not global \(d\)-divisibility or the odd-distance classification when
the initial gap reaches \(n-k+1\).

Ashikhmin--Barg (1998) supplies all structural ingredients and is not claimed as
new. Chubenko--Kurz studies divisible minimal codes, where every nonzero word is
minimal together with a divisibility assumption; that direction is distinct
from deriving divisibility of an arbitrary binary code from a spectral gap that
forces only its minimal words to have one weight.

Targeted searches covered the exact full-gap formulation, synonymous statements
about all minimal words having minimum weight, divisibility, disjoint minimal
vectors, odd minimum distance, and the recent arXiv identifier. They found the
classical minimal-code literature and the recent mirror-band paper but no prior
statement of this global closure theorem or its odd-distance rigidity. Searches
of the current SCOPE archive by source identifier and claim family found no
overlap.

The originality claim is therefore only to the best of our knowledge. The main
residual risk is that the result is a short consequence of a classical lemma and
could exist as uncited folklore or in terminology not captured by the searches.
Priority risk is also elevated because arXiv:2609.20344v1 is very recent. No
inaccessible paper was identified as a concrete coverage threat; the most
relevant primary structural source, Ashikhmin--Barg, was inspected in full, and
the recent mirror-band source was inspected at theorem/statement level.

## Value

The result turns an endpoint vanishing condition on only the low-weight part of
the spectrum into a global arithmetic restriction on every codeword. It also
gives a sharp qualitative obstruction for odd minimum distance: in dimension at
least three, the initial vanishing interval cannot reach the universal maximal
minimal-support bound. This provides a simple structural boundary complementary
to the recent local mirror-band theorem.

## Limitations

The hypothesis is stronger than the short-gap assumption in the motivating
preprint. The disjoint-decomposition mechanism is binary-specific. For even
minimum distance, half-size intersections between minimum supports remain
possible and no full classification is given. No independent audit has been performed.
