# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The core conjugacy is an exact coordinate calculation. The step map \(i\mapsto i+v\) partitions the coordinates into \(d=\gcd(n,v)\) cycles of length \(\ell=n/d\). On each cycle, the first generalized family becomes exactly the standard \(\chi_\ell\) rule. For the second family, reversal plus bitwise complement is an involution \(T\), and direct expansion gives \(T\chi_\ell T(z)_t=z_t+z_{t-2}z_{t-1}+z_{t-1}\). The permutation condition from the source paper implies \(\ell\) is odd, so the ordinary block is invertible.

The inverse-degree corollary follows from the established degree \((\ell+1)/2\) for \(\chi_\ell^{-1}\), together with invariance of algebraic degree under invertible affine conjugacy. The differential-uniformity statement follows from the known restriction-weight formula for ordinary \(\chi\): the minimum nonzero restriction weight is 2, hence maximum DP is \(1/4\); a direct product preserves that maximum by activating one block. The iterate and order claims are immediate from conjugacy to a direct product of identical factors.

Finite exhaustive checks independently reproduced both conjugacies for \((n,v)=(6,2),(10,2),(12,4)\), inverse degrees for the first two cases, and differential uniformity for \(n=6,10\). They are supporting checks, not substitutes for the proof.

No hidden hypothesis requiring \(\gcd(v,n)=1\) remains: the whole point of the coordinate permutation is to expose the \(d\) separate cycles. Since \(v\not\equiv0\pmod n\), \(\ell>1\); under the source paper's permutation condition \(\ell\) is odd and therefore at least 3.

## Originality

The motivating preprint, arXiv:2609.19548v1, was inspected in full HTML. It introduces the two families and proves that they permute exactly when \(2^k\mid v\). Its derivative-equation proof groups coordinates into cycles \(C_i=\{i+tv\}\), and it remarks that the iterates of the two named families behave similarly. It does not state that the functions themselves are coordinate-conjugate to a direct product of standard \(\chi\), does not give the reversal-complement conjugacy for the second family, and does not state the inverse-degree, complete composite-spectrum, order, or no-cross-block-diffusion consequences.

The closest prior cryptanalytic source inspected in full is Mella--Mehrdad--Daemen (2023), which explicitly defines and analyzes composite \(\chi\) as parallel ordinary \(\chi_\ell\) circles and gives convolution formulas for both differential and linear spectra. That paper predates the new skip-step family and does not identify it with composite \(\chi\). The 2024 algebraic-properties paper gives the ordinary inverse-degree formula. The 2025 ChiChi generalization and the 2026 Kriepke--Kyureghyan sibling family concern different even-dimensional constructions.

Targeted searches used the motivating arXiv identifier, the family name, the coordinate formula, `composite chi`, `parallel chi`, `gcd(n,v)`, differential properties, and the cited neighboring constructions. No prior source stating the present structural identification or its corollaries was found. The current SCOPE archive was also searched by arXiv identifier and synonymous terminology, with no matching record found before publication.

The originality claim is deliberately narrow: ordinary \(\chi\), composite \(\chi\), their differential/linear spectrum machinery, affine-equivalence invariance, and the inverse formula are all prior work. The claimed contribution is the explicit structural classification of the newly introduced skip-step permutations as composite \(\chi\) and the resulting parameter-level consequences. Because the observation becomes short once the coordinate cycles are exposed, folklore and near-simultaneous priority risk are material.

No inaccessible source was identified as a particularly likely direct cover of the claim. The most relevant neighboring papers listed above were accessible at least at theorem/article level, and the two strongest comparison sources were available in full text.

## Value

The result changes the interpretation of the recent even-dimensional construction. For even \(n\), every valid named map necessarily decomposes into at least two independent nonlinear circles; increasing the ambient state size need not increase inverse algebraic degree, order, or intrinsic nonlinear diffusion if \(\ell=n/\gcd(n,v)\) stays small. It also makes the full differential and linear profile available immediately from existing composite-\(\chi\) formulas instead of requiring a new cryptanalytic enumeration. Finally, the affine conjugacy gives an exact reason for the source paper's observed similarity of iterates.

The result should not be read as a break of any full cipher: external linear mixing can couple the blocks between nonlinear layers. Its value is a structural and cryptanalytic classification of the nonlinear permutation family itself.
