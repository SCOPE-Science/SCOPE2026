# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The proof has two independent threshold mechanisms that meet at the same reciprocal series.

For the positive direction, dyadic comparability implies uniformly in \(t\in[0,1]\)
\[
\sum_{k\in\mathbb Z}W_L(t+k)^{-1}
\asymp
1+\sum_j(2^{-j}+L(2^j))^{-1}.
\]
Convergence gives both \(F\in L^1\) and the \(L^2\) periodization estimate needed in the Olevskii–Ulanovskii uniqueness argument. Their construction then applies without changing its geometric or completeness ingredients. The dense-shift step is legitimate because the fiber sequence \(F(t+k)\) is absolutely summable for almost every \(t\).

For the negative direction, the normalized dyadic trigonometric blocks used in the recent endpoint proof have disjoint Fourier supports. Under the present weight their squared norms are bounded by a constant times
\[
a_j=2^{-j}+L(2^j).
\]
The energy-minimizing convex coefficients are proportional to \(a_j^{-1}\); the squared norm of the averaged block is therefore bounded by the reciprocal of the partial sum \(\sum a_j^{-1}\). Divergence supplies arbitrarily small-norm finite interpolants while the geometric-sum estimate supplies local uniform smallness. The successive-correction argument then gives a continuous global function vanishing on any prescribed uniformly discrete set while taking value one off that set.

The two directions therefore use exactly complementary convergence/divergence of the same series. For \(L(r)=\log^\beta(e+r)\), dyadic comparability is immediate and \(a_j\asymp j^\beta\), giving the sharp boundary \(\beta=1\).

No numerical computation or empirical evidence is used.

## Originality

**PASS, to the best of our knowledge.**

Olevskii–Ulanovskii's 2017 paper was checked at its section on Sobolev spaces with periodic spectral gaps, including the periodization lemma and proof of its uniqueness theorem. The published statement is formulated for Sobolev weights with exponent \(\alpha>1/2\). Its proof visibly contains the reciprocal-summability mechanism used in the positive half of the present theorem, so no novelty is claimed for that mechanism by itself.

Bertolini–Florit-Simon–Liehr–Taylor, arXiv:2609.20805, was checked at the theorem asserting sharpness of the Sobolev threshold and at the finite interpolation / successive-correction part of the endpoint proof. Their result treats the power scale \(1+|t|^{2\alpha}\): for \(S=A+\mathbb Z\), uniformly discrete uniqueness holds exactly when \(\alpha>1/2\). Their endpoint construction supplies the block method used here at and below the power threshold.

The new claim is the matching weighted dichotomy for dyadically comparable \(L\), including the optimized reciprocal-energy averaging in the negative direction, and its consequence that the critical Sobolev power has the further exact logarithmic threshold
\[
1+|t|\log^\beta(e+|t|),\qquad \beta=1.
\]
Searches combining periodic weak/spectral gaps, Paley–Wiener uniqueness, weighted Fourier norms, logarithmic Sobolev smoothness, critical weights, uniformly discrete uniqueness sets, and reciprocal-weight conditions found no matching theorem or logarithmic threshold.

No specifically identified inaccessible source was found whose available title or statement gives concrete evidence of prior coverage. The main residual risk is that the source preprint is extremely recent and the weighted extension is structurally close to its endpoint construction, so an unindexed parallel observation remains possible.

## Value

**PASS.**

The result sharpens a newly completed power-scale threshold into an exact boundary within critical logarithmic smoothness. It shows that the transition at Sobolev exponent \(1/2\) is not a terminal endpoint: at exactly the critical power, a logarithmic gain stronger than \(\log^1\) restores uniformly discrete uniqueness, while \(\log^1\) and every smaller logarithmic correction do not.

The reciprocal-series formulation is more informative than the logarithmic corollary. It identifies a single analytic quantity that controls both sides of the transition for a broad dyadically regular weight class, and it explains why the endpoint block averaging can be improved from equal weights to inverse-energy weights.

## Literature checked

- S. Bertolini, E. Florit-Simon, L. Liehr, M. A. Taylor, arXiv:2609.20805, especially the periodic-gap sharpness theorem and the finite interpolation / successive-correction construction.
- A. Olevskii, A. Ulanovskii, arXiv:1609.04571 / Sbornik: Mathematics 208 (2017), especially the section on Sobolev spaces with periodic spectral gaps, the periodization lemma, and the proof of the corresponding uniqueness theorem.
- Searches for logarithmic or weighted refinements of periodic-gap Paley–Wiener uniqueness, including synonymous formulations involving critical Sobolev regularity and uniformly discrete uniqueness sets.

## Scope of the claim

The novelty claim is limited to the reciprocal-weight convergence/divergence criterion for the stated dyadically comparable class, the inverse-energy block averaging proving the divergent half, and the resulting \(\beta=1\) logarithmic threshold.

No novelty is claimed for the Olevskii–Ulanovskii periodization construction, the existence of uniqueness sets above the Sobolev power threshold, the recent proof of failure at \(\alpha\le1/2\), its bandlimited interpolation lemma, or the standard geometric-sum estimates.
