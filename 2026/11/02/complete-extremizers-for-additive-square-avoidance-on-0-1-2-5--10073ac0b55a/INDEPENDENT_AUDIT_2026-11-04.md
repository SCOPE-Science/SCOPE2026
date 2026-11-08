# Independent mathematical audit

## correctness

PASS

For prefix sums P0..Pt, newly appending a creates forbidden equal-sum adjacent blocks of half-length k iff a=2P_{t+1−k}−P_{t+1−2k}−P_t; this exactly characterizes every permissible extension. Actual verify_forbidden.cpp and independent verify_direct.cpp inspected. A fresh compiled execution of the first complete DFS traversed exactly 299596819 nodes, counted depths 80..87 as 2696,1530,792,338,120,38,8,0, and printed eight distinct length-86 winners; independently checked reversal pairing and Parikh classes from those strings. The DFS is complete by induction on prefixes, not merely sampled. The second implementation uses separate sliding sums but not fully rerun this execution.

## originality

PASS

Zhang 2026 proves only maximum length 86 and prints one witness, with same 299596819 search visit total. His technical supplement/electronic archive was identified but full contents were not successfully read, so the possibility it reports all winning words or implicit counts is material. Freedman–Brown 2016 concerns an endpoint-sum alphabet family with a different avoidance statement. This census is additional conditional on the unavailable supplementary file not already containing the eight-word list.

## value

PASS

Equality-case census, reversal orbit structure and Parikh classes for a natural four-letter alphabet singled out in a recent sharp maximum-length theorem is a concrete finite-extremal classification, not rediscovery of maximal length.

The dated certificate retains the supplied scientific assessment, sources and limitations.
