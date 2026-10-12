# Self-review

## Correctness
**PASS.** The conjugate equality is factored exactly, so for odd prime conductor and integer \(c\neq1\) all \(p-1\) conjugates are distinct and the generated field is the full cyclotomic field. The discriminant-index identity then reduces the index to a Vandermonde quotient. Counting unordered nonzero pairs with fixed sum modulo \(p\) gives multiplicities \((p-1)/2\) at zero and \((p-3)/2\) elsewhere, and the cyclotomic product identity yields exactly \(|1-c|\,|1-c^p|^{(p-3)/2}\). The boundary \(c=1\) is excluded before this step. The power-basis classification follows directly from the positive integer factors. Supplementary computations agree with the formula but are not used as an infinite proof.

## Originality
**PASS.** The closest inspected 2026 paper studies the identical element \(u=\zeta+c\zeta^{-1}\), but its Proposition 2.1 is a theorem for the proper-subfield case and its Lemma 2.4 only characterizes that case by conjugate collisions. At odd prime conductor, the new argument shows that every integer \(c\neq1\) lies in the complementary full-field case and computes the exact index there. Washington's cited result handles \(c=1\), while Shah--Nakahara's published scope concerns certain index-two imaginary abelian subfields. Targeted formula, discriminant, generator, and alias searches found no stronger statement implying the claim. Residual bibliographic risk remains that an older equivalent formula is recorded under different terminology.

## Value
**PASS.** The order index is the canonical quantitative obstruction to the same explicit element being a power-basis generator. Determining it exactly for the full integer one-parameter family at prime conductor converts the source's qualitative proper-subfield/full-field split into a sharp integral-basis classification. The answer is uniform in \(p\) and \(c\), isolates the exceptional quadratic case \((p,c)=(3,2)\), and gives a reusable closed form rather than a finite computation.

## Closest literature and limitations
The primary motivating source is arXiv:2609.38844v1. The closest older cyclotomic references found in its bibliography and targeted searches concern the maximal real subfield or restricted index-two imaginary abelian subfields. The result is limited to odd prime conductor and integral \(c\); composite conductors may have additional Galois-orbit and pair-sum structure. The originality check is targeted and does not constitute an exhaustive bibliography.

Self-review: passed. Independent audit: not yet performed.
