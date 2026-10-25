# Independent mathematical audit

## correctness

PASS

A primitive binary BWT word must start with 1 and end with 0, so for odd n>1 its run count is even and <=n-1. By published Lemma 8 (standard stable-rank LF permutation one n-cycle criterion), every candidate with n-1 runs corresponds exactly to one equal-adjacent gap, among n-1 positions; at n=49 every one of 48 candidates has orbit strictly <49, whereas each preceding odd n from 3 to 47 has at least one full-cycle candidate. A 46-run n=49 BWT has precisely three equal gaps; the complete 17296 possible gap triples contain exactly 1128 with one LF cycle, matching witness gap set (0,1,8). Independently recoded exhaustive singleton/triple enumeration and independently recreated results. Periodic necklace repetition leaves run number bounded by shorter primitive root length (for 49, 1 or 7), hence no missed extremizer. Finite result only for odd n<=49.

## originality

PASS

Fici–Gabory–Romana–Sciortino CPM 2026 supply the standard permutation criterion and nonbinary fully unclustered results; the published lemma number 8 was directly verified. Their binary even-length fully alternating topics and Mantaci et al ratio framework do not cover a first odd failure of near-alternating n-1 runs at 49 with multiplicity 1128.

## value

PASS

Maximal BWT run count is natural for run-length-compressed string indexing and distinguishes almost fully unclustered binary necklaces. First parity-allowed extremum failure and exact count of extremizing necklaces are a sharp finite structural boundary at a nontrivial length, independently valuable despite no all-length asymptotic theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
