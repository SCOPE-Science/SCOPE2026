# Independent mathematical audit

## correctness

PASS

The greedy arch count is m with a run of length one and 2m−1 otherwise: when both runs are longer, after 0^a1 the arches alternate 1^(b−1)0 and 0^(a−1)1, with a final all-1 rest. For a word of length one more than the arch count, a greedy match cannot lag beyond its indexed arch, and any match strictly earlier than that arch would leave enough full arches to fit the whole remaining target. Thus each matched letter must occupy the corresponding arch. For a,b≥2, the first match must be terminal (otherwise both symbols remain in the first arch), the absent last letter must be 0, and an early match can only be followed by a terminal match and only when its own initial run has length one. A last early match is possible iff a=2 and there is a later odd arch. This gives the no-adjacent-early Fibonacci recurrence (bases 1,2), independent choices at exactly m−1 alternating positions in the mixed cases, and the forced path spelling (10)^m when both runs are at least three. For arches 01 with empty rest, legal prefixes consist of terminal matches followed by early matches, yielding m+2 absent words. When b=1<a the terminal 1 is forced in every arch and either final symbol fails. When a=1<b, appending 0 and working backward forces the terminal zeros in arches 2,...,m, but the initial 01 may contribute either letter: no 0 remains in that first arch after either match. In the source's Step 2 the backward forcing of the preceding terminal zero applies only when that preceding arch is not the first one. For m=1, 00 and 10 directly give the two absences in this case; when a,b≥2 only 10 is absent at length two, so the early-terminal wording at m=1 does not affect the claim. The all-parameter conclusion follows from the greedy proof, not the source author's finite tests.

## originality

PASS

The supported distinct claim is the complete run-sensitive five-regime classification, specifically the mixed-run power-of-two count and the transition to a singleton for both lengths at least three. Two diagonal branches are demonstrably covered by distinct catalogue records and are not credited as original individually. The greedy arch characterization and the universality length relation are also prior inputs.

## value

PASS

This is a motivated all-parameter classification on the simplest periodic two-run hosts, not a sampled census. Equal shortest lengths do not imply similar scarcity: the exact cardinality can grow with Fibonacci or powers of two or be one. It is useful to separate effects of the two run lengths and locate exactly when another increment in run lengths stops mattering. The value rests on those distinctions and the full classification, not on rediscovering the diagonal cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
