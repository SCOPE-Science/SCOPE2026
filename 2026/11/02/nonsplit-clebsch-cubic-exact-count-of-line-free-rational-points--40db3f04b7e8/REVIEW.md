# Independent mathematical audit

## correctness

PASS

In characteristic p≥7 a singular point would have all squares equal, hence all coordinates ±a for nonzero a, and five signs cannot sum to zero. The fifteen pairing lines are distinct. For a primitive fifth root and z ranging over its five powers, the Fourier plane is spanned by the functions z and z^(−1). It lies on S by vanishing sums of the relevant characters. To verify its orbit size in every stated characteristic, any stabilizing permutation sends z and z^(−1) to a z+b/z and c z+d/z. Pointwise product 1 and linear independence of the characters 1,z²,z^(−2) force ac=bd=0 and ad+bc=1. Thus a stabilizer is exactly a multiplication by a fifth root or such a multiplication composed with inversion, giving orbit size 120/10=12. These lines have no identically zero coordinate, so they are distinct from the pairing lines; smoothness gives completeness at 27. Frobenius sends the Fourier plane to the plane of z²,z^(−2), with disjoint projectivizations by character independence; the same holds under any common coordinate permutation. Its square preserves the plane. Thus all six pairs are nonrational and skew, and no member can contain a rational point. In the pairing arrangement, two distinct missing coordinates force a common support of size two, giving ten support-pair points each on three lines. With the same missing coordinate, the union of the two matchings is a four-cycle enforcing alternating values; there are three distinct double points per missing coordinate. There are no other meetings, so the union has 15(q+1)−20−15=15q−20 points. For the Picard calculation, the integer Gram matrix has G·1=5·1 and G²+4G=3J. The independent check /workspace/review_evidence/clebsch_gram.js, replayable with node, confirmed these identities using only the incidence rule: equal missing coordinate or a shared pair. Trace −15 gives multiplicity five for −4 and hence rank six. The line classes span a nondegenerate six-dimensional space (a seven-dimensional span would give rank seven). Frobenius fixes it and acts nontrivially on Picard since it exchanges distinct lines, which cannot be numerically equivalent by self-intersection −1 and nonnegative mutual intersection. The orthogonal complement is therefore negated. The cubic point formula gives q²+5q+1; subtraction gives (q−3)(q−7), including 0 at 7 and 60 at 13. The finite integer matrix check applies in all the stated characteristics by the proved incidence rule. The uploaded verifier was inspected, not executed; its prime-field tests would not alone establish the result or the skew conjugacy.

## originality

PASS

The claim being credited is the exact complement of the union of all geometric lines for the specified nonsplit form, not the classical lines, general Frobenius formula, or isolated small-field examples. The strongest distinct overlap in the catalogue is a later, broader incidence spectrum. No earlier equivalent formula is established by the inspected comparisons; the historical risk is bounded below.

## value

PASS

Off-line rational points are a natural arithmetic invariant of a classical cubic, and excluding all geometric lines is stronger than simply excluding known rational ones without a descent argument. The formula gives the sharp exceptional q=7 boundary and exact abundance over every admissible extension, useful when an argument requires a rational point avoiding the exceptional curves. It is not an extrapolation from a list of prime fields or just a computation of the standard Picard trace.

The dated certificate retains the supplied scientific assessment, sources and limitations.
