# Independent mathematical audit

## correctness

PASS

Circle integration selects equal index sums of ordered triples. Independent Haar phases make the signed multiplicity vectors an orthonormal character basis, so subtracting the constant term makes variance the sum of squared coefficients. The identical-multiset cases (three distinct, one repeated, all equal) give 36 binom(n,3)+9n(n−1)+n. Cancel the common multiset on either side of a nonzero character: residual mass one is impossible by the equal-sum constraint. At mass two, four distinct indices admit a freely chosen common third index; it contributes 36 off that support and 18 on it, hence 36(n−2). Distinct signed pair characters have count (2n³+n)/12+O(n²), since the triangular pair-count energy is (2n³+n)/3, one coincidence costs a degree of freedom, and each character has four orderings. At mass three, the residual triples specify the original multisets; six distinct indices give exactly 36 orderings and coefficient 36. Independently, the ordered equal-sum triple energy equals the coefficient of z^(3n−3) in (1+⋯+z^(n−1))⁶ by reflecting the second triple. Inclusion–exclusion gives binom(3n+2,5)−6 binom(2n+2,5)+15 binom(n+2,5), hence (11/20)n⁵+O(n⁴). Coincidences leave at most five variables subject to a nontrivial linear equation, costing O(n⁴), so the signed character count is (11/720)n⁵+O(n⁴). With repeated residual indices, mass-two support ≤3 gives O(n²) characters with coefficient O(n); mass-three support ≤5 gives O(n⁴) with coefficient ≤36. All bounds use finitely many index patterns, giving absolute constants. Squaring the generic coefficients and summing gives 216+99/5=1179/5. Dividing by n⁶ and adding the O(n⁻²) squared bias gives the stated mean-square relation.

## originality

PASS

Earlier results establish normalized sixth-moment concentration for this ensemble and exact variance at power four. Neither gives the first nonzero sixth variance coefficient or resolves its two contributions. Credit the earlier concentration and the lower-order pair mechanism; the supported distinct claim is the quantitative sixth-power law.

## value

PASS

This quantifies the fluctuation scale and exact mean-square error of the first integrated even power beyond the fourth for a natural iid unimodular ensemble. The separation between inherited pair collisions and genuinely new triple collisions explains why a fourth-moment formula alone cannot give the constant. The result is a useful benchmark for quantitative concentration or fluctuation theorems without asserting a CLT.

The dated certificate retains the supplied scientific assessment, sources and limitations.
