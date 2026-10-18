# Scientific review

## Correctness — PASS
The result is a complete all-length theorem for the original cyclic-rotation BWT and fixed Hamming weight three. Its exact gap-by-gap lexicographic row-order rule proves the critical nonstandard sorting lemma, including zero-gap and periodic cases; a marked-row adjacency analysis yields the two/four/six classification. The six-run class has a rational gap-sum generating series, and the two-run cases are counted with correct rotational stabilizers. Subtraction from the complete \(\binom n3\) support count closes the spectrum. Direct enumeration of 8,854 words and an independent grouped-rotation calculation across 8,435 gap triples corroborate, but do not replace, the infinite proof. The special all-one length-three word is explicitly excluded.

## Originality — PASS with residual bibliographic risk
The closest fully inspected primary source, Mantaci et al., *Measuring the clustering effect of BWT via RLE* (2017), investigates run counts and establishes a general doubled-run upper bound; the complete paper does not determine the fixed-weight-three input distribution or give the present gap orientation theorem. Another closely relevant primary source, Mantaci et al., *On Fixed Points of the Burrows-Wheeler Transform* (2017), studies the same sparse alphabet slice but classifies BWT fixed points rather than run-number distributions; its Proposition 4.2 does not imply the three-level census. Classical perfect clustering characterizes the two-run subcase, which is not claimed independently original. Searches for aliases, equivalent gap descriptions, enumerations, and stronger coverage identified no such full spectrum, but inaccessible/unindexed earlier enumerations remain a risk.

## Value — PASS
The run count is the basic length of BWT run-length encoding and relevant to highly repetitive text indexes. The three-one layer is the first sparse layer with a possible six-run output, and the result gives a motivated natural exact spectrum for all lengths, a sharp gap-orientation decision rule, and the asymptotic fact that almost every fixed-weight-three word attains all six runs. This is an exact classification of a natural source ensemble, not an arbitrary parameter slice or a performance claim for actual compressors.

## Constraints and limits
The BWT is cyclic and has no terminator; the input is binary with exactly three ones and length at least four. This does not extend to larger Hamming weights or sentinel-based BWTs. Scientific priority remains subject to independent literature review.

Self-review: passed. Independent audit: not yet performed.
