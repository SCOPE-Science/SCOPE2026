# Scientific review

**Correctness — PASS.** The risk formula follows from the published Gaussian complete-sketch Student law, with degrees of freedom explicitly evaluated and the integrability threshold checked. The Chebyshev extremizer is attained by positive barycentric weights, not merely bounded by a minimax polynomial. The integer allocation proof controls all candidate reserves with an exponential lower bound and treats the otherwise degenerate integral tie. The standalone numerical verifier passed Chebyshev stationarity, independent Gaussian draws, and finite-budget checks.

**Originality — PASS, qualified.** The one-shot Student distribution and deterministic Chebyshev GMRES minimax result are classical/previously published and are excluded from any independent novelty claim. The distinct assessed claim is the exact sharp Gaussian-sketch Krylov fixed-budget risk together with the eventual unique integer reserve and its \(\sqrt K/4\) scale. The inspected sGMRES and sketch-and-recycle research gives subspace embedding/empirical oversampling, not this exact mean-square allocation. Related published mathematical records concerned deterministic GMRES(1), gradient methods, Kaczmarz, and Haar CG, with non-implications documented in the accompanying audit. A specialized identical allocation optimization might have escaped discovery; independent priority review is needed.

**Value — PASS.** Given a fixed number of Gaussian sketch rows, extra Krylov vectors reduce polynomial approximation error but amplify random inverse-Wishart risk; both effects are real and compete. Their exact minimax balance predicts an integer reserve proportional to the square root of the spectral condition number, with a sharp finite-moment cliff. This is a natural budget-selection benchmark rather than an arbitrary numerical invariant.

**Limitations.** The result is exact-arithmetic and one-shot, not a guarantee of runtime optimality or a validation of sketch reuse and adaptive stopping. The limiting reserve is pointwise in each fixed condition bound. Existing Gaussian Student and Chebyshev facts are openly credited.

Self-review: passed. Independent audit: not yet performed.
