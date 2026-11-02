# Scientific review: free class-two Lie endomorphism ranks

## Correctness

**PASS.** The defining universal property gives the independent choice of the generator blocks \(A\) and \(B\), while the bracket block is forced to be \(\bigwedge^2 A\). The critical image-rank identity is established by taking the central intersection of the image, not by incorrectly adding the raw ranks of the two diagonal blocks. With \(a=\operatorname{rank}A\), \(b=\binom a2\), and \(j=\operatorname{rank}(\ker A\to (\bigwedge^2V)/\bigwedge^2\operatorname{im}A)\), the total rank is exactly \(a+b+j\). Gaussian-binomial enumeration gives the formula with no missing lift factor; its specialization at \(z=1\) is \(q^{d(d+\binom d2)}\). The entire support, its gaps, and the two asymptotic limits follow from the stated formulas. Independent exhaustive enumerations in small fields agree with every coefficient.

## Originality

**PASS relative to inspected literature.** The 2019 Benito–Roldán-López article gives the generator-extension property and the invertibility criterion, so those ingredients are acknowledged as established. The 2017 Cagliero–Gutiérrez Frez–Szechtman paper is about uniserial representations, and the 2021 Ruan–Sheng–Zhang article uses the free class-two algebra as a Lie-algebra model. The inspected sections of these papers do not derive the complete image-rank distribution of **all** endomorphisms, forbidden intervals, or asymptotic rank-defect law. A related restricted result for commuting idempotent endomorphisms does not imply the nonidempotent multiplicities or singular spectrum. A result for Heisenberg Lie endomorphisms concerns a different nonfree family when the number of generators exceeds two. Unnoticed equivalent enumeration via linear-map bundle methods remains possible; priority is not independently certified.

## Value

**PASS.** Image ranks are an intrinsic invariant of an endomorphism monoid. The exact complete distribution gives a sharp series of finite-dimensional semigroup rank gaps of increasing lengths, including the growing gap immediately below automorphisms. The limiting theorem relates the normalized defect of a random Lie endomorphism to the universal finite-field square-matrix corank distribution, explaining how exterior-square forcing amplifies generator rank loss by a factor of order \(d\). These conclusions go beyond simply restating the automorphism criterion or counting maps of one prescribed rank.

## Closest literature and limitations

The principal precursor is P. Benito and J. Roldán-López, arXiv:1911.01897 (2019), especially Proposition 1. Supporting object models appear in L. Cagliero, L. Gutiérrez Frez and F. Szechtman, arXiv:1703.06214 (2017), and S. Ruan, J. Sheng and H. Zhang, *Journal of Algebra* 586 (2021). The theorem is for finite fields and free nilpotency class two only; it says nothing about conjugacy-class counts of endomorphisms or arbitrary class-two quotients. Earlier equivalent statements may exist under alternative terminology, and a separate specialist priority check remains worthwhile.

Self-review: passed. Independent audit: not yet performed.
