# Independent mathematical audit

## correctness

PASS

An independent integer-only reproduction on all 15,361 permitted encodings checked exact nearest-even transitions, subnormals and the endpoints, both edge digests, cycle reachability, each basin cardinality and midpoint weight, and all entry-time maxima. It confirmed the 2,774 unequal edges, 10,194 unequal zero-basin memberships, both exact marginal Cesàro expectations and their printed approximations. For the actual repaired claim, weighting each common code by the difference of its two adjacent values (using one adjacent value at endpoints) gives cell lengths in units 2^(-25). Summing by both basin labels gave rows [11335435,0,21950155], [2730,22528,0], [2602,0,240982]. The joint table normalizes to 2^25 and its row and column sums agree with the independently reproduced marginals. Periodic tails justify the Cesàro average per state, and exact weighted cycle means justify the expectation. The new standard-library certificate, python3 verify_ensemble.py, was run and checked the joint law and exact means; the original uploaded script was not executed for this review.

## originality

PASS

The original graph-level contribution materially overlaps the inspected expanded-evaluation record's explicit credit for the identical binary16 baseline censuses, basin counts and digests. The target it cites was unavailable for direct reading. The corrected article credits both graphs and makes the common-start, midpoint-weighted joint law and its real-start consequences the claim, not the graph census. The reported counting tables and digests do not imply those directional masses from their published summary statistics. The strongest examined joint analogue uses different bfloat16 maps and encoding counts. This is a judgment on the demonstrated distinct remainder, not a priority claim or a conclusive comparison against unavailable text.

## value

PASS

Common-start comparison answers an initialization question that separate finite graph inventories do not: what fraction of actual uniformly drawn inputs change asymptotic fate, and in which direction? The exact table shows overwhelmingly one-way movement away from zero, with a small but nonzero reverse event that cannot be reconstructed from the mean shift or the difference of zero marginals. The object and initialization are canonical and the precise probabilities make a reusable finite-precision benchmark without asserting general numerical dynamics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
