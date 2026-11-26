# Independent mathematical audit

## correctness

PASS

For b=ℓ+1 and x²=qb+r, T_b(x)=x²−qℓ. Both 1 and ℓ are fixed, so either member of a nontrivial positive one-digit cycle has a nonzero residue not equal to 1. Applying the congruence twice gives x⁴≡x mod ℓ; the order is exactly 3, including exclusion of ℓ=2,3. When ℓ≡1 mod 3 the only possible pair is the two nontrivial roots u<v of z²+z+1, which square to each other; their modular sum −1 lifts to u+v=ℓ−1 since both are between 1 and ℓ−1. For positive n,s<ℓ with n²≡s, q=(n²−s)/ℓ is an integer ≥0 (n²−s>−ℓ), and n²=qb+(s−q). This is the actual Euclidean split giving T_b(n)=s exactly if q≤s, since s<b. The condition holds for u→v since u²<bv and reduces for v→u to v²≤bu, including equality. Substitution gives u²−(3ℓ−1)u+(ℓ−1)²≤0. The upper quadratic root is larger than (ℓ−1)/2, which exceeds u, so only the lower root matters. A separate bounded divmod calculation reproduced 2↔4, 7↔11 and 29↔37 for ℓ=7,19,67 and the absence of a cycle for ℓ=13 (3→9→16 in base 14) and ℓ=2,3. The frozen verify.py/VERIFICATION.md comparison over ℓ<20000 is finite corroboration, not the proof; no bundled code was executed.

## originality

PASS

Prior statements on the same square-split operator inspected here concern fixed points. The reduction modulo b−1 is familiar, but by itself gives only a two-cycle candidate, not a classification of actual one-digit orbits. No inspected source gives or implies the exact prime-field candidate plus the reverse-transition digit threshold. Prior cycles called Kaprekar in other sources refer in several cases to a different operator.

## value

PASS

Period two is the first nonfixed stratum of the classical square-split map, and prime b−1 is a natural arithmetic regime for its residue dynamics. The exact carry threshold decides which modular candidates produce a genuine digit cycle, a distinction that matters even at ℓ=13; at most one such pair needs checking. This is an unbounded complete classification in the stated stratum, not the standard modular congruence alone, an arbitrary finite census, or an existence claim about other bases or periods.

The dated certificate retains the supplied scientific assessment, sources and limitations.
