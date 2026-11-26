# Independent mathematical audit

## correctness

PASS

For the scattered pattern, every occurrence uses four strictly ordered runs. A five-run host either has an unusable leading 1-run or an unusable trailing 0-run; deleting it and padding a participating run strictly improves any positive count. At four runs the count is the product of their lengths, maximized by balancing the positive integer parts. In the proposed six-run host the second selected bit lies either in the inserted singleton 1 or in the following run of length b-1. Summing these two contributions leaves the gain (a-1)(b-1+d)-cd over abcd; the four balanced residues yield t^2-3t+1, t^2-t, t^2 and t^2-t, each strictly positive in its n>=9 range. I separately enumerated all compositions of n with both starting bits, counting by the middle two runs, and obtained unrestricted/restricted pairs (1,1), (2,2), (5,4), (9,8), (16,16) at lengths 4–8. The six-run witnesses 010101 and 0010101 achieve 5 and 9, respectively. This proves the claimed exact exception set, with no extrapolation or assertion of six-run global optimality.

## originality

PASS

The length-six failure and its alternating witness are already in Menon–Singh, as the frozen text credits. The supported distinct result is the exact five-run capacity together with the complete finite exception set and explicit six-run improvements for every other length. The analogous published catalogue result treats different patterns, and the closest structural results compared do not supply this classification.

## value

PASS

The known alternating counterexample shows that matching the target's four runs can fail once. The reviewed theorem determines exactly when even a five-run budget fails, and shows that a six-run witness already certifies this obstruction at every nonexceptional length. The isolated return to equality at n=8 is part of a full structural boundary, not an arbitrary small-value census. The balanced-product formula alone is elementary; the value is its exact comparison to unrestricted packing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
