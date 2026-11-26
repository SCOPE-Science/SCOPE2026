# Independent mathematical audit

## correctness

PASS

The aaa targets force at least three copies of each letter, and three successive permutations suffice for all aba. For distinct a,b, failure of aba forces all three b's into the two exterior gaps of the a-span, giving four projections. Exchanging a and b gives four more, with precisely the two disjoint-span arrangements in both sets; the union is the six listed projections. In the recurrence, the transition for the third occurrence of b checks exactly what has been seen strictly between its first and third occurrences, and no later transition can alter that interval. Every legal word gives exactly one path, and appending a distinct letter at any state gives a disjoint class of completions. Independently generated every first-appearance-canonical three-of-each word for q=1 through 5 and greedily matched each target subsequence directly, without a mask recurrence or pair-projection filter. At q=4 the 15400 representatives yielded 3334 covers, or 80016 labeled; at q=5 the 1401400 representatives yielded 148543 covers, or 17825160 labeled. The action is free since every label appears. For full universality the greedy alphabet blocks are necessary: their terminal letters can only be matched at their block endpoints or later, and appending a letter missing from the residual suffix gives a missing subsequence if there are fewer than three blocks. At minimum length these blocks are permutations. Thus 24^3=13824 and the ratio is 1667/288. Replay: python3 /workspace/evidence/5.py; output /workspace/evidence/5.out. This is abstract word combinatorics and supplies no biological validation.

## originality

PASS

Exact binary overlap is established and excluded from the distinct contribution. On the compared evidence, the all-alphabet classification and higher-alphabet census are not covered by the binary arch-refined enumeration, the all-pattern universality algorithms, or contiguous palindrome problems. The exact all-pattern count is acknowledged as a comparison, not a separate novelty claim.

## value

PASS

The alphabet size and the length 3q are intrinsic to the target family, not arbitrary enumeration parameters. The local obstruction characterization and reproducible exact counts answer how much the set of shortest hosts expands when only palindromic length-three targets are required rather than all patterns; the exact four-symbol ratio measures that distinction. The all-alphabet recurrence is useful even though there is no asymptotic or closed form, and no practical or biological effectiveness is inferred.

The dated certificate retains the supplied scientific assessment, sources and limitations.
