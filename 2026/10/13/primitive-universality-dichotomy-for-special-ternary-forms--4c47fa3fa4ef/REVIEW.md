# Self-review

## Correctness
PASS. The proof reconstructs the representation identity from coprime two-square coordinates of \(d\). In every positive branch, a common divisor of the three constructed coordinates is forced to divide the Bezout right side, and the parity choices exclude the only possible factor \(2\) when that right side is \(2\). For even special \(d\), the residue \(4\pmod8\) is impossible primitively: odd \(c\) would force a sum of two squares congruent to \(6\pmod8\), while even \(c\) forces all three coordinates even. The free Bezout parameter makes the third coordinate unbounded, so finitely many zero-coordinate exceptions can be removed. The packaged checker independently tests representative parameters and residue classes.

## Originality
PASS. Lam's 2015 theorem and Dung--Thang's 2021 theorem classify ordinary nonzero universality and provide the closest construction, but neither requires \(\gcd(a,b,c)=1\) or states the primitive value set. The even branch shows a genuine implication gap: ordinary representations exist for integers congruent to \(4\pmod8\), whereas primitive ones are impossible. Searches using both “special number” and standard primitive-quadratic-form terminology did not locate the exact dichotomy. Broader spinor-genus literature was checked at the abstract level and did not expose this family-specific result.

## Value
PASS. Primitivity is a standard structural refinement for quadratic-form representations. The theorem gives a natural complete classification across the entire known special family: the odd parameters are primitively universal, while the even parameters miss exactly one residue class modulo \(8\). It therefore turns the parity mechanisms already present in the source constructions into a sharp local-global boundary rather than a finite or cosmetic refinement.

## Closest literature and limitations
The closest source is Lam's 2015 proof of ordinary specialness, followed by Dung and Thang's 2021 revisit. The new proof deliberately reuses their coprime sum-of-two-squares setup but adds common-divisor tracking and the modulo-\(8\) necessity argument. The result does not classify nonspecial \(d\), and it does not count primitive representations by height. A residual originality risk remains from broader classical theory of indefinite ternary quadratic forms.

Self-review: passed. Independent audit: not yet performed.
