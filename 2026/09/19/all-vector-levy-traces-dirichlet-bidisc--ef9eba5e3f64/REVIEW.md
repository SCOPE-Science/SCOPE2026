# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The proof uses two published inputs. First, equation (31) in S. Bera, *New York J. Math.* 32 (2026), gives for every bidisc polynomial \(p\)
\[
\|M_1p\|^2-\|p\|^2
=
\int_{\overline{\mathbb D}\times\mathbb T}|p(a,\zeta)|^2\,d\rho^{(1)}(a)\,dm(\zeta),
\]
and the symmetric formula for \(M_2\). Since the coordinate multipliers are bounded and polynomials are dense, the restriction maps extend to bounded \(L^2\) trace maps \(\Gamma_i\). Their polynomial intertwining \(\Gamma_iM_i=M_a\Gamma_i\) extends by continuity.

Therefore, for every \(h\) and \(n\ge0\),
\[
\|M_i^{n+1}h\|^2-\|M_i^nh\|^2
=
\|\Gamma_iM_i^nh\|_2^2
=
\int |a|^{2n}\,d\eta_{i,h}(a).
\]
Hence \(S_*\eta_{i,h}\) is the Hausdorff representing measure of the coordinate forward difference. Splitting its atom at \(1\) from the part on \([0,1)\) gives the stated drift and the factor \((1-t)^{-1}\) in the Levy measure. No division by \(1-t\) is made at \(t=1\).

Second, Theorem 2.4 of Bera--Sequeira, arXiv:2609.20346v1, gives for every vector the coordinate-face decomposition of the joint Levy measure when the pair defect vanishes. The bidisc multiplication pair has that zero-defect property, so the coordinate formulas combine to the stated joint formula.

The tomography argument was checked separately. The probes \(1,1+z_i^k,1-i z_i^k\) recover the real and imaginary parts of \(S_*(a^k\rho)\) from
\[
|1+a^k|^2=1+|a|^{2k}+2\operatorname{Re}(a^k),\qquad
|1-i a^k|^2=1+|a|^{2k}+2\operatorname{Im}(a^k).
\]
Disintegration over \(t=|a|^2\) then yields all angular Fourier coefficients on almost every interior fiber, while the drift yields all Fourier coefficients of the boundary restriction. Fourier uniqueness gives the reconstruction. The explicit comparison \(\delta_r\) versus \(\delta_{-r}\) also verifies that the \(h=1\) radial data can coincide while the \(h=1+z_1\) Levy data differ.

## Originality

Bera--Sequeira, arXiv:2609.20346v1, explicitly asks in Question 1.3 how the Levy measure for arbitrary \(h\) is related to the defining measures. Theorem 1.4 computes the defining-measure formula for \(h=1\), while Theorem 2.4 is an abstract all-vector face-decomposition theorem. Bera's 2026 model paper supplies the polynomial defect identity but does not state the arbitrary-vector trace formula or the tomography theorem.

Searches by the current arXiv identifier and title, arbitrary-vector Levy terminology, Dirichlet-type defect/representing-measure terminology, and equivalent measure-reconstruction language found no public statement of the all-vector bidisc formula or the countable tomography result.

The main residual prior-art risks are A. Aleman's 1993 Habilitationsschrift, Chapter IV, and A. Athavale--V. M. Sholapurkar, *Positivity* 3 (1999), 245--257. Their role in the one-variable completely-hyperexpansive theory is known, but complete searchable full text was not inspected here. They could contain equivalent one-variable trace formulations. This is not concrete evidence of prior coverage of the bidisc all-vector formula or tomography theorem.

The novelty claim therefore excludes the polynomial defect identity, the abstract zero-defect decomposition, Hausdorff moment uniqueness, disintegration, and Fourier uniqueness.

## Value and limitations

The result answers an explicit arbitrary-vector question and identifies an information boundary hidden by the \(h=1\) radial formula: the Levy part recovers interior defining mass, while the drift is essential for boundary mass. A countable family of elementary polynomial probes recovers both defining measures.

For general \(h\), the trace maps are \(L^2\) extensions, not asserted pointwise boundary values. The tomography theorem uses countably many probes. No claim is made for higher polydiscs or for tuples without the vanishing pair-defect hypothesis.
