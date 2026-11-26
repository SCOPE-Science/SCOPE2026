# Independent mathematical audit

## correctness

PASS

Final assessment is of the corrected RESULT.md. The frozen line 6 lists q five times, giving thirteen entries of total size 4N+q; as written that multiset is false. The endpoint formula and proof already require q exactly four times, so the replacement removes the one extra entry and leaves the substantive theorem and proof unchanged. Independently, in a length-N interval only residues 0 and N/2 have fewer than two odd-part bits fixed by the residue. The former gives g(m) at index Nm; the other is g(2m+1) or g(2m-1), fixed by parity of m for a fixed start phase. In each parity class g(m) takes both values at arbitrarily large m, so each labelled cut and bit choice occurs. Allouche's 4N complexity theorem then forces all labels to represent distinct strings. Around an even site the two odd neighbors differ, hence the two incident directed edges consist of one transition and one equal pair; the direction of the transition is determined by the left odd neighbor, regardless of the even bit. There are q transitions each way. At a zero even site the equal pair is 00, and at a one even site it is 11. The count of ones on the even sites of the unmodified prefix is q-1 by g(2r)=g(r) and the dyadic prefix weight recurrence, so toggling h exceptional bits gives B_h. Cutting an edge of type ba subtracts exactly that closing edge and gives endpoints a,b. Bigrams and endpoints determine letter counts and conversely the letter and bigram counts recover the endpoints. Thus different triples give distinct nonempty classes and each has binom(2,h)B_h(ba) strings. For h=1 there are four size-2q classes; the other levels together give two q-1, four q, and two q+1. These are twelve classes of total size 16q=4N. Independently enumerated starts for N=16,32,64,128 from the two lowest relevant index bits, deduplicated strings and binned by endpoints, weight and transition count; the sample counts match the proven spectrum. The repair was diffed against the original and the corrected literal multiset checked against the formula.

## originality

PASS

The corrected claim is the adjacent-pair, endpoint-resolved dyadic fibre-size spectrum, not the ordinary complexity, the four-template catalogue by itself, or regularity of class counts. The strongest same-day records give the same templates for a different statistic or exactly this type of statistic on a different word. Neither examined claim states the ordered adjacent-pair counts of the circles or the resulting twelve dyadic paperfolding fibres. The unavailable 1994 full text remains a specific priority risk, not a verdict.

## value

PASS

For a natural automatic word the fibre sizes answer how many distinct strings are compatible with one local observation (endpoints and pair counts). Total factor complexity or the number of 2-Abelian signatures cannot answer that question. The dyadic restriction is tied to the two exceptional residues, and the ordered-cut calculation gives an all-level ambiguity distribution, with an explicit factor-two multiplicity effect from the middle weight level. This is a motivated quantitative invariant rather than a sampled list or another statement of ordinary complexity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
