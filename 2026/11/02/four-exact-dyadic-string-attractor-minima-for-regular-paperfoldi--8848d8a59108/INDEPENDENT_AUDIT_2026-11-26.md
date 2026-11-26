# Independent mathematical audit

## correctness

PASS

For each factor, the union of its occurrence intervals is exactly the set of positions that can hit it. Each attractor must hit every support; summing these hitting constraints with nonnegative weights gives cardinality at least the total weight if each position has load at most one. I independently replayed pf_cert.json with /workspace/branches/paperfolding_replay.py, generating the word by low-bit isolation and scanning exact substrings by length. The replay verified all four upper witnesses, uniqueness of the 12, 15, 12, 21 packed factors respectively, their claimed first occurrences, and all position loads. In length order the distinct-factor counts were 6479, 25775, 102767, 410351; total weight units 80, 92, 96, 102; peak load 16 in each case. With denominator 16 the ceilings match the witness sizes 5, 6, 6, 7. This is exhaustive for the four finite prefixes, not a bound at other lengths.

## originality

PASS

The directly comparable prior Resultary record proves exactness only through length 64. Its four larger intervals do not determine these exact minima. Neither other inspected Resultary records nor the identified automatic-sequence work covers the four exact paperfolding values. The distinct-factor totals were already known and are not credited as new.

## value

PASS

The four consecutive doublings are the natural unresolved cutoff in the specific earlier paperfolding census, not arbitrary small instances. Exactness improves every earlier upper bound and settles whether the two consecutive sizes at 256 and 512 differ. Small rational lower certificates make the data useful as independently replayable benchmarks for studying attractors of automatic words, without implying an all-length trend.

The dated certificate retains the supplied scientific assessment, sources and limitations.
