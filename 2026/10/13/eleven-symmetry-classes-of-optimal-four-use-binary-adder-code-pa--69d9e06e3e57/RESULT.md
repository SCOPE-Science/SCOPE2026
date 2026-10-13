# Eleven symmetry classes of optimal four-use binary-adder code pairs

## Finding
For ordered pairs of subsets \(A,B\subseteq\{0,1\}^4\), call \((A,B)\) uniquely decodable when \((a,b)\mapsto a+b\) (coordinatewise integer addition) is injective on \(A\times B\). Exactly \(2448\) ordered labeled pairs satisfy \(|A||B|=36\) and unique decodability. The maximum possible product is \(36\) (a known optimum), and all its attaining pairs consist of \(768\) pairs of sizes \((4,9)\), \(912\) of sizes \((6,6)\), and \(768\) of sizes \((9,4)\). Under simultaneous coordinate permutations, simultaneous bitwise complements of both users, and swapping users, the \(2448\) pairs form exactly \(11\) orbits, with sizes \(48\) once, \(96\) three times, \(192\) three times, and \(384\) four times. The *census and classification* constitute the finding; the maximum \(36\) is not claimed new.

## Assumptions and scope
Both users use arbitrary nonempty subsets of \(\{0,1\}^4\) with no linearity or equal-size assumption. A subset is encoded as a 16-bit integer, whose bit at index \(v\) indicates membership of the binary four-vector with integer label \(v\). The channel output alphabet is \(\{0,1,2\}^4\). Codebooks are ordered until the symmetry group explicitly allows swapping. Primary MSC 94B25.

## Proof
For any \(A\), let \(D(A)=\{a-a':a,a'\in A, a\ne a'\}\subseteq\{-1,0,1\}^4\). Two distinct ordered input pairs collide precisely when their differences satisfy \(a-a'=b'-b\), so unique decodability is equivalent to forbidding, for distinct \(b,b'\in B\), the difference \(b-b'\in D(A)\). Form the graph \(G_A\) on the sixteen binary words with edge \(bb'\) whenever \(b-b'\in D(A)\). Then \(B\) is valid if and only if it is independent in \(G_A\). The maximum product for fixed \(A\) is \(|A|\alpha(G_A)\).

Complementing a chosen coordinate in *both* codebooks transforms the integer channel sum at that coordinate by \(z\mapsto2-z\); it preserves injectivity and cardinalities. Thus every pair is equivalent to one with the all-zero vector in \(A\), and it suffices to enumerate the \(2^{15}=32768\) such nonempty \(A\). The exact recurrence \(\alpha(G[S])=\max\{\alpha(G[S\setminus\{v\}]),1+\alpha(G[S\setminus N[v]])\}\), with \(\alpha(G[\varnothing])=0\), is applied for every normalized \(A\). This exhaustive finite algorithm establishes \(|A|\alpha(G_A)\le36\), and equality occurs.

For equality, \(|A|\) divides \(36\); for each normalized \(A\) satisfying this restriction the second exhaustive algorithm tests every \(B\) of cardinality \(36/|A|\) for independent-set status. It enumerates exactly \(966\) normalized pairs: \(192\) at \((4,9)\), \(342\) at \((6,6)\), and \(432\) at \((9,4)\). Undoing all sixteen possible simultaneous translations via XOR and deduplicating yields \(2448\) ordered labeled pairs. A third exhaustive algorithm applies all \(24\) coordinate permutations, \(16\) simultaneous complements, and \(2\) user orders, canonically choosing the least integer pair in each orbit; it finds the eleven orbit representatives and sizes in `orbit_representatives.csv`. Every transformation is invertible and preserves the channel property, and all possible transformations are enumerated. Their orbit sizes sum to \(2448\), so no classes are missing.

## Verification
The package contains three standard C++ programs `adder4.cpp` (exact independent-set maximum), `adder4census.cpp` (equality-case enumeration), and `adder4orbits.cpp` (group-orbit classification), and `adder4_root_pairs.txt` (the normalized pair list). Build with a C++17 compiler and run in that order, executing programs in the directory containing the text data. The expected independent-set maximum is `36`; the normalized pair total `966`; the full pair total `2448`; and orbit count `11` with sizes `48:1,96:3,192:3,384:4`. Source code explicitly loops over all normalized masks; this is a finite exhaustive certificate, not an extrapolation from samples.

## Relationship to prior work
The classical two-user binary adder channel and its uniquely decodable code pairs are studied by Austrin--Kaski--Koivisto--Nederlof (2016), whose focus is upper bounds for asymptotic unbalanced families rather than classification of four-use equality cases. Earlier coding work supplies context, not a claim of new optimal cardinality. A KTH thesis (Queseth, 2024) discusses optimal short code constructions and may contain related finite classifications; reliable full-text comparison could not be completed. The explicit new claim is the complete \(2448\)-pair, eleven-orbit equality census.

## Limitations
The classification concerns exactly four channel uses and the stated full group. It implies neither a new asymptotic bound nor uniqueness under other equivalence conventions. The 2024 thesis is a residual priority risk. No independent external scientific audit has been performed.

## References
Austrin, P., Kaski, P., Koivisto, M., Nederlof, J., Sharper Upper Bounds for Unbalanced Uniquely Decodable Code Pairs, arXiv:1605.00462v1 (2016-05-02), https://arxiv.org/abs/1605.00462.
Queseth, E., Constructions of codes for the binary adder channel, KTH thesis (2024), URN urn:nbn:se:kth:diva-360250, full text not retrieved.
Shi, K. and Watanabe, T., work on uniquely decodable code pairs for binary adder channels (1994).
