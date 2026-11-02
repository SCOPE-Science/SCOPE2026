# Scientific review

## Correctness — PASS

The multiset intersection criterion is proved from deletion-shadow containment. A heavy coordinate (multiplicity at least three) can occur in at most one codeword; exceptional words have all multiplicities at most two. At length five, two compatible exceptional words require disjoint doubled-symbol supports; at lengths at least six, any two exceptional words have multiset intersection at least four. This gives the sharp cardinality bounds with explicit constant-word-plus-exceptional-word witnesses. The labeled census is separately obtained by counting the possible heavy-word completions of exceptional cases: twelve pairs times twenty-four at length five; four times 144 plus six times 22 at length six; four times four at length seven; one at length eight. Exact graph and exceptional/heavy enumerations agree. The orbit counts follow from the exact finite fixed-point tables and Burnside's lemma; the included recursive verifier enumerates all candidate words and all compatible sets of optimal size without duplication. No numerical solver or unverified infinite extrapolation is used.

## Originality — PASS, with residual priority risk

The closest recent primary work [1] develops the same fixed-small-output regime, but at three survivors its general \(q=4\) certificate bound is ten, not the exact sequence here, and it does not enumerate optimal codebooks. Its exact \(q=4\) results are for one deletion rather than three survivors. The follow-up [2] addresses ball geometry, not maximizing-codebook structure, and the foundational [3] gives general constructions and bounds rather than this optimizer census. Searches for quaternary three-survivor multiset packings, tetrahedral discrete-simplex codes, and exact class counts did not identify a stronger encompassing theorem. The closest research-index overlap concerns a ternary three-survivor profile, which does not imply the quaternary values. A differently phrased older discrete-simplex table or private/unindexed work could still cover some finite sizes or counts; this has not been independently ruled out.

## Value — PASS

The three-survivor channel is explicitly investigated in [1] yet its general bound leaves a wide gap at four symbols. The result closes the complete first unresolved alphabet case for every length at least five and counts **all** optimal codes in the four nonstable lengths. Its change from six to five to four codewords identifies precise finite-size transitions, and its orbit count shows that the 708 labeled optimizers at length six represent 46 inequivalent designs. Both optimal cardinality and structural census are natural parameters relevant to unordered-token reconstruction, not arbitrary slices of an unrelated table. No universal higher-alphabet or decoder-complexity improvement is claimed.

## Closest literature and limitations

[1] Kreindel–Essayag–Zabokritskiy, arXiv:2601.05636, Section 4.4; [2] the same authors, arXiv:2603.18322, Sections 1–2 and the development of ball bounds; [3] Kovačević–Tan, arXiv:1612.08837, Sections I, II, IV. The exact count at larger lengths is not treated; finite orbit enumerations depend on replayable standard-library code. Remaining risk concerns an unindexed or older exact table for discrete-simplex packings. No external validation has been performed.

Self-review: passed. Independent audit: not yet performed.
