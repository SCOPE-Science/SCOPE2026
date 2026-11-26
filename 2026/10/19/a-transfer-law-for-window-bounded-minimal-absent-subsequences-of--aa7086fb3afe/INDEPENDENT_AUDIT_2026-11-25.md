# Independent mathematical audit

## correctness

PASS

The first letter can start at its own phase. A chosen occurrence of a letter has the next desired letter at the positive residue gap d_j, and taking the earliest such position realizes the minimum span S=1+Σd_j. An endpoint deletion saves its adjacent gap, including for length two; an interior deletion saves q if the two gaps sum to more than q and zero otherwise, including exactly q. Thus E=S−p must be positive and at most both endpoint gaps, which ensures E≤q; all interior saves must then be q. Single deletions suffice by downward closure, and there are no one-letter obstructions. Each admissible gap path, initial letter and eligible excess contributes exactly one word at p=1+Σd_j−E≥1. The resolvent starts with the zero-transition term for length two; endpoint correction yields (1) without negative powers in the resulting series. The q=2 determinant is 1−tz²−t²z³ and the weighted numerator is 2t²z(2+z+tz²). At t=1 the initial data and recurrence follow by coefficient comparison. The positive pole r is simple and dominant (equality in |z²+z³|≤r²+r³ forces the positive phase), giving C=−N(r)/(rQ′(r)). The supplied verification material was inspected, not executed. Independent agreement of complete word sets for 26 cases (q=2, p≤12; q=3, p≤8; q=4, p≤6), and of binary length histograms through p=12, is replayable via python3 /workspace/branches/c7bfc94d-63aa-4c2e-9455-1a0f9020c4e6/check_windows.py. These are finite checks; the span/deletion and transfer proof covers all parameters.

## originality

PASS

The supported distinct contribution is the simultaneous window-by-length law and complete endpoint-excess and neighboring-gap classification for permutation streams. General bounded-range p-MAS algorithms, finite-linear powers and binary minimum-span spectra supply relevant ingredients or different data, but the inspected results do not give this general-q obstruction law.

## value

PASS

A full obstruction antichain for the union of windows answers which patterns first fail, not simply how many patterns are present. The classification gives a local test with sharply distinct endpoint and interior rules; the q-state resolvent counts every length and window size, including growth from the binary pole. It resolves a natural domain not determined by fixed-host spectra or marginal counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
