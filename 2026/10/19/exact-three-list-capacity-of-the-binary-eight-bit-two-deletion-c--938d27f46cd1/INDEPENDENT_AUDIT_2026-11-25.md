# Independent mathematical audit

## correctness

PASS

I independently rebuilt all incidences by inserting two binary symbols in each length-six output, deduplicating each (word,output) pair. The 23 distinct witness words give an output-load distribution of 1 zero, 2 ones, 20 twos and 41 threes. I checked the nonnegative integer dual on all 256 words, and the 48-support rational primal on all 64 rows and every source unit cap. Their objectives coincide at 1082/45, so 24 is the rounded upper bound. Equality with 24 would leave an exact budget of 6 for selected slacks, omissions of the two 36-weighted constant words and unused weighted row capacity. This forces both constants and only slack-at-most-six words. Instead of replaying the supplied 113-case search, I branched directly on individual word inclusions and exclusions over all such candidates. Every discard uses the three-list capacity, remaining size, insufficient remaining defect budget, or forced saturation of a row whose weight exceeds that budget. For a row needing d occurrences to saturate, if fewer than d candidates remain its unavoidable deficit bounds the budget from below, and if exactly d remain in a mandatory row they must all be selected. No fractional or floating test enters this search. It exhausted 18,941 nodes without a 24-word completion. The construction and the exclusion together establish 23, not just a bound.

## originality

PASS

The closest exact table at length eight is for list cap two; the closest list-cap-three entry is at length seven. Neither implies 23 or the cap-three fractional optimum. The closest published inequalities apply to the model but do not determine its integral or fractional value at this parameter.

## value

PASS

The cap-three regime is a natural list-decoding problem, and the result exhibits an explicit failure of the rounded incidence LP bound at a reproducible short-block instance. Even with optimal fractional weights, rounding gives a number unattainable by any actual code. The exact witness and integral exclusion give a benchmark for stronger packing converses and exhaustively checked code designs, beyond an isolated numerical best candidate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
