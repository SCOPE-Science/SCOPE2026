# Independent mathematical audit

## correctness

PASS

The binary sign rule gives a(2m)=a(m), a(2m+1)=(−1)^m a(m), so Q_(2m)=(S(m),T(m−1)) and Q_(2m+1)=(S(m),T(m)); the intervening odd-to-even steps are horizontal. The four-adic S recurrences make the 0 and 2 branches odd and halve the target after removing a trailing 1 or 3; since only m=0 gives S(m)=1, the entire S=2^k index set consists of exactly k digits in {1,3}, in the order B_k(p). In the two-bit blocks 01 and 11 the nonleading 3 digits contribute two adjacent-11 counts each, so the leading digit alone fixes orientation. The T recurrences T(4r+1)=2T(r−1), T(4r+3)=2T(r) give child lower heights (2h+2,2h) for downward edges and (2h−1,2h+1) for upward edges. Starting from heights 0 and 1, this yields precisely the descending-even and ascending-odd lists. The disjoint time pairs exhaust all visits, so the endpoints of the one or two incident height intervals give the claimed indices and multiplicities, with no visits outside 0≤v≤2^k. Inverting the two height formulas and interleaving binary digits takes O(k) digit operations. The supplied verifier was read, not executed; a separate bounded direct sign-and-walk replay passed for k=1–5. No finite horizon is used in the proof of completeness.

## originality

PASS

The supported distinction is the closed chronological pairing of the selected times with vertical edge heights on every dyadic line, and the explicit bit-dilation inverse obtained from it. The range, multiplicities, general coordinate inversion and recurrences are known; the horizontal-coordinate hit indices are also represented in OEIS. The joint height/time law is a short specialized derivation from the known recurrences but was not found as a prior exact theorem, nor as a direct substitution into an inspected global inverse or range formula. Neither priority nor a complexity improvement over general inversion is asserted.

## value

PASS

Powers-of-two lines are natural boundaries of the four-adic recursion. The law gives their entire chronological edge permutation, including orientation, and an exact, no-scan map from height to the one or two visit times. It allows direct analysis of traversal order at arbitrarily large scales rather than recomputing positions or using the known multiplicity alone. The oriented height recursion, not a fresh table of S-hits or a new global coverage theorem, supplies that added usefulness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
