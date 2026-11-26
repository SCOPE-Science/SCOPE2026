# Independent mathematical audit

## correctness

PASS

Pass for the complete corrected RESULT.md in /workspace/repairs/5. The frozen proof at line 51 falsely said that the quotient two-term transform with separation M/2 vanishes on half the frequencies whenever the two coefficients have equal magnitude. At N=8 take f(0)=f(4)=1, f(2)=f(6)=i and all other coefficients zero. Then F1=0 while the transform of F0 is 2+2i(−1)^j, nonzero at all four quotient frequencies. The replacement uses the necessary and sufficient condition u=±v: the exact expression u+v(−1)^j either vanishes on one parity or nowhere. It retains the correct main theorem and equality description. Independent replay of the final proof: after factoring out the largest common dyadic spacing, a three-term polynomial has a singleton parity, so it cannot vanish at both ±z; the two-term count follows from the kernel of the cyclic power map. Parseval and equality in the triangle and Cauchy inequalities give |B|≥N/4; at equality B−B lies in the annihilator of the span of A−A, forcing exactly four elements in that span and character phases on its coset. The even and odd Fourier indices are exactly the transforms of F0,F1 with the stated phases. One antipodal pair gives two folded supports of size 2 or 3; two pairs with both branches nonempty give two supports of size at most 2; both yield at least M total nonzeros. For two pairs and one vanishing branch, a nonopposite separation has gcd≤M/4, and the opposite separation has the corrected explicit dichotomy. With no pairs and noncoset projected support, induction applies to both size-four folds (this subcase cannot occur at M=4). For a projected order-four coset each support count is a positive multiple of M/4; a total below 3M/4 forces both to be character extrema. The ratio of their folded coefficients between consecutive coset points would have fourth power 1, whereas the ratio from the original lifts has fourth power −1. At all N the example has distinct exponents and disjoint zero sets at odd k and k≡4 mod 8, proving 3N/8 is attained.

## originality

PASS

Reassessed for the repaired theorem. Credit only the exclusion of intermediate supports for arbitrary nonzero complex coefficients across all dyadic cyclic orders, not the indicator gap, order-eight case, product lower bound/equality description or three-atom bound. Those genuine overlaps are acknowledged. The phase correction leaves the scope of the gap unchanged and is not itself credited as a new theorem.

## value

PASS

The repaired gap quantifies how far any nonextremal four-spike complex spectrum must be from the uncertainty minimum in every dyadic cycle. This is an exact structural invariant of the unrestricted complex problem: the known indicator example attains the bound, but unrestricted coefficient cancellations could have made it false. The correction preserves the sharp separation and minimum-equality geometry without claiming robustness or complete second-level classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
