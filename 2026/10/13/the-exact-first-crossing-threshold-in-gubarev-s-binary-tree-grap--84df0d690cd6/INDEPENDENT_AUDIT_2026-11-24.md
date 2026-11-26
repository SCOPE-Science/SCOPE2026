# Independent mathematical audit

## correctness

PASS

In the graph of §4.2, an x/y step changes gap height by ±1 and an a-jump preserves it. By Definition 5.1, two distinct grid heights visited force a crossing: select successive different visited grid heights, and the last visit to the first before the first visit to the other. Without a crossing, the height window has width at most 2n−2 (the interval between neighboring excluded grid heights on either side of the sole allowed grid height, truncated at a boundary; an interval with no grid is no wider). Lemma 5.2's proof bounds a path in a width-R window by 2L_R. Independently, within a nonzero bottom-height window the path cannot pass beyond the two siblings whose parent is below the allowed window, and their height-R truncations have word lengths L_R; a path edge cannot exceed that count, since truncated leaves can only be jumped or left untraversed. At bottom height zero only the root truncation is needed. For N≥2n divisible by n, take a vertex at depth N−2n. Between its opening and closing symbols traverse both child subtrees, with unit x/y steps above depth N−1 and one a-jump at each depth-N−1 vertex. The two truncated child words are exactly ℓ_(2n−2), so the length is 2L_(2n−2). The visited heights lie in [N−2n+1,N−1], containing only grid height N−n; for n=1 the path consists of two jumps at that grid height. Hence the forced-crossing threshold is 2L_(2n−2)+1 in the stated range. Section 6 gives at least e edges per contributing path and requires a first crossing to invoke the same vanishing boundary block; choosing e equal to the new sufficient threshold works even when N=n. This does not prove a sharp index of T_S(f). Inspected frozen verify.py and verification_output.txt without executing: the recorded DP is a bounded sanity check (N=2n for n=1–6, N=3n for n=1–4), not the proof.

## originality

PASS

The noncovered finding is the matching crossing-free path and the resulting exact cutoff, not the height-window upper bound or the availability of that smaller sufficient exponent. The frozen record itself credits the upper bound to the proof of Lemma 5.2. The first-crossing algebraic consequence is routine from that upper bound and is not separately credited as novel.

## value

PASS

The maximum crossing-free length determines the sharp stopping point for a specific graph argument underlying nilpotency, not merely a slightly different upper estimate. The family of extremizers shows that a smaller exponent cannot be certified solely by universally forcing the first crossing in graphs of the asserted heights. This is useful even though the tightness of the nilpotency index itself is not resolved.

The dated certificate retains the supplied scientific assessment, sources and limitations.
