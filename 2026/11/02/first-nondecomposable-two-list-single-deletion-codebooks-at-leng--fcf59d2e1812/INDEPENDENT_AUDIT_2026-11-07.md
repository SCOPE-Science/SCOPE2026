# Independent mathematical audit

## correctness

PASS

PASS. For each n=1..7, the exact 0-1 packing rows count distinct one-deletion outputs (not repeated positions) with capacity <=2. Independent BigInt rational-checker reconstructed every incidence, verified feasible witness sizes 2,3,4,7,12,19,33, checked all reported rational upper-leaf equalities, and exhaustively replayed each branch: one-leaf dual at each n=1..6, 101-node 51-leaf proof excluding 34 length-seven words, and separate 25-node 13-leaf capacity-one proof excluding 17. The explicit unique-deletion code reaches 16. Direct syndrome enumeration gives sums of two largest disjoint VT classes 2,3,4,7,12,19,32. For n=7 every union of two uniquely decodable codes has cardinality <=2*16=32<33. For n<=6 the corresponding unions attain M2(n). Exact certificate comparisons use arbitrary-size integers, not lossy floating-point parsing. The theorem is only n<=7.

## originality

PASS

PASS best-of-knowledge. Lin full 2026 primary paper defines this precise same-channel t-list deletion model and uses VT-class unions to prove asymptotic lower bounds, but does not derive exact n7 capacity 33 or failure of decomposition. No 2019 paper treats t=1 unique-deletion maxima (including the established 16), not list-two 33; Song et al. treat the strictly stronger deletion-plus-substitution channel. Resultary exact length-six single-deletion census concerns unique decoding, not length-seven list-two optimality. Older enumerations may nonetheless cover the same number.

## value

PASS

PASS. At the first natural blocklength n=7, optimal two-list single-deletion packing becomes genuinely stronger than any disjoint union of two ordinary correcting codes. Exact capacity 33 versus decomposition ceiling 32 is a substantive structural threshold and independently checkable benchmark for a natural finite coding model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
