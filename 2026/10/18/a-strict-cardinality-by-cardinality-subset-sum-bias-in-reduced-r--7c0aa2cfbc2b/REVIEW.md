# Independent mathematical audit

## correctness

PASS

CRT makes the reduction from U_N onto F_p^× surjective for every p|N. Being a group homomorphism, it has equal fibers of size m=φ(N)/(p-1). For each nontrivial additive character, the p-1 nonzero values of the exponent run over all nonidentity p-th roots; thus the character product is ((1-(-z)^p)/(1+z))^m. Its degree-r coefficient is (-1)^r B_{p,m}(r), because every term of degree r in the product has the same sign. Fourier inversion gives the two count levels: the nontrivial-character sum is p-1 at zero and -1 at each other residue. Every degree from 0 to (p-1)m is representable by filling m slots of capacity p-1, so the difference is nonzero, including p=2 and both endpoint cardinalities. Uniformity modulo N would project to uniformity modulo p. At odd p, evaluating the alternating polynomial at z=1 and removing the empty subset gives zero; this only proves cancellation after projection, not pooled equidistribution modulo composite N. I independently enumerated literal combinations for 2≤N≤16 and compared integer counts for all divisor primes, sizes and residues with the coefficient formula. Frozen verify.py was inspected, not executed; its descending dynamic program checks 2≤N≤96. The infinite theorem follows from the character calculation, not either finite enumeration.

## originality

PASS

The supported distinct claim is the evaluated two-level prime-projection law for all cardinalities of the full reduced residue set, with strict nonzero bias and resulting nonuniformity modulo N. Neither general character inversion nor pooled odd-modulus unit-subset uniformity is distinct. The strongest related published computations either pool the layers, treat an initial interval, or count tuples with gcd constraints but allow repetition. The two strongest local indexed comparisons have different cardinality conventions or objects. The polynomial simplification and sign-definiteness exploit equal fibers and the exact product of nonidentity prime roots, rather than substituting parameters into a covering evaluated subset-count theorem. The comparison is bounded and not a priority certification.

## value

PASS

Layer-by-layer strict nonuniformity answers a natural question raised by the standard pooled odd-modulus theorem. The sign and exact magnitude explain how the pooled projected distributions cancel despite strict bias in every layer. The result also excludes uniformity in cases where total-count divisibility cannot: for example N=21,r=6 has 924 subsets, divisible by 21, but the three projected counts are 402,261,261. This is an all-moduli structural statement, not a recomputation of a small case or an unevaluated use of character orthogonality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
