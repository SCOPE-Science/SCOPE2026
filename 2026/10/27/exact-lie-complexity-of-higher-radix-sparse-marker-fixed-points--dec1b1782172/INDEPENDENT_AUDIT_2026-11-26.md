# Independent mathematical audit

## correctness

PASS

In the one-sided fixed point, all ones occur at block ends. The preimage has no adjacent ones, so the longest zero run is 2r-1 (attained in the image of 10; the initial run is only r-1). For n<2r every one-marker rotation 0^a 1 0^b fits using the images of 10 or 01 and the zeros in the next block, since min(a,b)<=r-1. Together with the zero necklace this gives two. Two chosen ones in a complete necklace force both complementary circular distances to be multiples of r, by considering cuts on either arc. Thus such necklaces require r|n, and at the only multiple r in the base interval two ones cannot fit. At nonmultiples above the base interval even the one-marker necklace fails, since one rotation would need at least 2r zeros. For n=rm with m>=2 the zero necklace is impossible. The marker residue fixes block phase in every occurrence of an aligned representative, so completeness implies completeness of the unique preimage up to rotation. In reverse, every complete preimage has a zero (it cannot be 1^m), hence its image has a marker; every offset below r of an aligned occurrence is realized by replacing only initial zeros by zeros from the next block. Images cannot collapse two preimage necklaces because a rotation between aligned marker-containing words moves by a multiple of r. This proves the recursion; n=r is covered separately by the base case. Dividing out whole powers works for composite r as well. There are 2(r-1) possible reduced lengths, each yielding a disjoint geometric progression, proving both counting consequences. The supplied verify_lie.py was read, not executed. Separate 50,000-letter prefix checks at r=2,3,4,5 matched in all 108 cases; replay: /workspace/branches/4e9d84bc-9d85-4c3b-b17e-1da8dfe33aa9/small_lie_check.py, log small_lie_check.log in the same directory. The all-length proof does not rely on prefix saturation.

## originality

PASS

The exact radix-two spectrum exists in a distinct Resultary record. The frozen claim excludes it. The inspected evidence does not supply the all-integer r>=3 spectrum or its higher-radix desubstitution bijection. This judgment credits the overlap and does not infer priority from the shared date.

## value

PASS

The higher-radix family is defined by a natural period-doubling substitution with sparse fixed-phase markers. Its all-rotations spectrum is a stricter invariant than ordinary factor counts. The classification determines a logarithmically sparse support explicitly, including composite radices, and its desubstitution shows how whole necklace classes, not just individual factors, are preserved. This is a substantive exact family calculation beyond the known binary-length control, not a new general theorem about all substitutive words.

The dated certificate retains the supplied scientific assessment, sources and limitations.
