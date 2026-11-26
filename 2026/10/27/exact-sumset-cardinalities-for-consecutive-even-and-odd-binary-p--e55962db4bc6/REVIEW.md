# Independent mathematical audit

## correctness

PASS

At position zero both summands have bit one, so output is zero with carry one. At position 2m the longer summand has bit one; the incoming carry t determines the top two output bits and gives disjoint initial classes. In an inward pair i,2m-i the shorter summand contributes a_i and a_{i-1}, while the longer contributes b_i at both. Thus the two carries and the previous shorter digit contain precisely the constraints needed to extend a candidate word. At position m they meet with independent center bit b_m and shorter bit a_{m-1}. This includes m=1 without any interior steps. Subset propagation counts a bit-pair word once regardless of representations, and the terminal rule counts distinct possible middle bits. With the correspondence A_m=v M^{m-1}w proved, an independently written bit-mask/backward-propagation reproduction, `python3 /workspace/branches/independent-palindrome-4.py`, gave 37 reachable nonempty subsets, all 37 integer residuals v M^k Q(M)w zero, direct enumeration agreeing for m=1..8, and numerator coefficients [2,-7,6,-4,-14,24,-8,0,0]. The characteristic recurrence of M extends the residual zeros for all k by Cayley–Hamilton; Q need not be the characteristic polynomial. The recurrence, initial counts and rational numerator therefore hold exactly, not by extrapolation.

## originality

PASS

The checked prior sources cover automata for palindrome sums, same-length counts, and bounds on exact-length sumsets, but not the mixed-length cardinality law. Neither the closest catalogue item nor the exact sequence search supplied coverage. The pass is for the explicit distinct-sum recurrence and generating function, not the automata method in general or exhaustive publication priority.

## value

PASS

The adjacent even/odd case is a natural first unequal-length instance of the established binary-palindrome sumset problem. It measures representation collisions through the number of distinct sums, not the easily counted pair multiplicity. The uniform exact recurrence allows arbitrary-length enumeration of the cardinalities without enumerating exponentially many pairs and provides a benchmark for more general sumset bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
