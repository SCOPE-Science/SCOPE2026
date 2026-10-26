# Scientific review

## Correctness — PASS

The irreducible dihedral character formulas and normalization follow from the standard explicit two-dimensional representations for \(n\ge5\). For \(n\ge13\), root-of-unity orthogonality is applied only after bounding every Fourier frequency of the sixth-power Laurent polynomial by \(12\). Direct constant-term extraction gives exactly \((10,0,7,0,6,0,10)\) for mixed moments indexed by the number of second harmonics. Expanding the squared modulus yields the displayed polynomial in \(|a|^2,|b|^2,\operatorname{Re}(a\overline b)\). Differentiating and factoring the one-variable cubic proves the exact global nonnegative deficit and all equality cases. Strict low-order aliasing is proved by a positive six-step witness at each order. The independent coefficient-path checks in `artifacts/verify.py` and its recorded output corroborate the algebra, but only the proof covers all orders and coefficients.

## Originality — PASS, best knowledge

Searches compared nonabelian character packet sixth moments, the cyclic model \(\{-2,-1,1,2\}\), exact two-character inequalities, four-consecutive Fourier bands, and older Nikol'skii-type literature. Doktorski's general frequency-support estimates concern bounds that are sharp in order but do not state this exact constant. Full statements of related public four-consecutive-frequency, finite-order two-one-dimensional-character, and generalized-dihedral isotype results were compared: their assumptions do not yield this mixed nonlinear-character sixth-moment constant or full deficit. The closest four-frequency result applies to \(\{0,1,2,3\}\), which is not an affine translation and dilation of \(\{-2,-1,1,2\}\); the finite-order two-character formula concerns two **one-dimensional** frequencies, whereas the present trace-character space has four cyclic frequencies tied into two antipodal pairs. No inspected stronger result was found to imply the classification. Residual risk: an exact value may exist in unindexed classical low-degree trigonometric extremal tables or under alternate noncommutative-norm terminology. This review does not establish independent priority.

## Mathematical value — PASS

The natural first adjacent pair of genuinely nonlinear irreducibles of each dihedral group defines a basic noncommutative Fourier packet. The exact sharp norm is substantially larger than either single-character sixth moment and has an algebraic, nonbalanced optimizer. The theorem gives a dimension-independent nontrivial value for all large orders, proves precisely when aliasing ceases, and gives a globally exact, nonnegative two-component stability identity with complete complex equality cases. This is a full solution to a motivated infinite-family sharp norm problem, rather than a selected numerical example or a routine small gain.

## Relationship and limitations

The proof does not classify sharp constants at the eight exceptional orders \(5\le n\le12\), nor packets of other characters. Numerical tests supplement but do not replace exact Laurent identities. Unindexed literature may cover the formula. See the proof, source comparison and explicit residual risks in the result and audit documents.

Self-review: passed. Independent audit: not yet performed.
