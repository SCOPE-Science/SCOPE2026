# Same-model review

Same-model review: passed. Cross-model review: not yet performed.

## Correctness

**PASS.**

The density and parameterization were checked against Lawford, arXiv:2609.20393. With \(a=c-3/2\), Proposition 2.11 gives exactly
\[
g_a(x)=\frac{a}{\sqrt{2\pi}}\int_0^1
\lambda^{1/2}(1-\lambda)^{a-1}e^{-\lambda x^2/2}\,d\lambda,
\]
and the source's tail result is \(g_a(x)\sim a|x|^{-3}\), equivalently
\(P_a(|X|>x)\sim a/x^2\) for fixed \(a>0\).

The Hellinger proof was checked at the scale where the Gaussian density and polynomial tail exchange dominance. The density crossover solves
\[
a|x|^{-3}\asymp\phi(x),
\]
hence \(x^2=2\log(1/a)+3\log\log(1/a)+O(1)\). The proof deliberately brackets this crossover using
\[
s_a^2=2L_a+2\log L_a,\qquad
r_a^2=2L_a+6\log L_a.
\]
The beta-precision representation gives the uniform two-sided tail
\[
P_a(|X|>x)=a/x^2\{1+o(1)\}
\]
at both cutoffs. The probability mass between them is
\(o(a/L_a)\), while the Gaussian mass beyond \(s_a\) is also
\(o(a/L_a)\).

For the central region, the exact likelihood ratio
\[
R_a(x)=a\int_0^1(1-u)^{1/2}u^{a-1}e^{ux^2/2}\,du
\]
was used rather than the fixed-\(a\) tail expansion. Splitting at the endpoints gives
\[
|R_a(x)-1|
\le C a(1+x^2)+
C a e^{x^2/2}(1+x^2)^{-3/2}
\]
for \(|x|\le s_a\). Squaring against the Gaussian density yields
\(O(a^2)+O(aL_a^{-5/2})=o(a/L_a)\). Beyond \(r_a\), the cross-affinity is negligible by Cauchy-Schwarz, leaving the hypergeometric tail mass
\(a/(2L_a)\). This verifies the constant in
\[
H^2(P_a,P_0)\sim a/(2L_a).
\]

The iid statement uses exact Hellinger-affinity tensorization. The exponent is
\[
nH^2(P_{a_n},P_0)/2
\sim
\frac{n a_n}{4\log(1/a_n)},
\]
so the critical affinity \(e^{-\kappa/4}\) for
\(a_n=\kappa(\log n)/n\) has the stated constant.

The critical maximum law was checked directly from the precision-mixture survival probability at
\(x_n(y)=\sqrt{2y\log n}\). For \(y\ge1\),
\[
nP_{a_n}(|X|>x_n(y))\to\kappa/(2y).
\]
For \(y<1\), the Gaussian component of the distribution already forces the normalized maximum above \(y\). At \(y=1\), the Gaussian exceedance count tends to zero while the algebraic component leaves intensity \(\kappa/2\), producing the stated atom.

The minimum-distance blindness statement was checked independently of contiguity. Lawford's Lemma 3.8 supplies uniform bounds on the first two \(c\)-derivatives of \(G_c\), hence
\[
\|G_{3/2+a_n}-\Phi\|_\infty=O(a_n).
\]
When \(\sqrt n a_n\to0\), the triangular empirical CDF therefore has the same first-order Brownian-bridge limit as under the null. The score, curvature, consistency, and quadratic tightness argument used in the source's boundary proof then transfer directly, yielding the null mixture limit for the fit-improvement statistic.

For \(a_n=\tau/\sqrt n\), a maximum threshold
\(\sqrt{2(1+\varepsilon)\log n}\) has null exceedance probability tending to zero, whereas its expected alternative exceedance count is asymptotic to
\[
\tau\sqrt n/\{2(1+\varepsilon)\log n\}\to\infty.
\]
This explicitly proves failure of contiguity and total-variation separation.

The infinite forward KL and chi-square divergences were checked from the fixed-\(a\) algebraic density tail against the Gaussian exponential tail.

## Originality

**PASS, to the best of our knowledge.**

Lawford's full text was inspected around the density and tail lemmas, beta-precision representation, Remark 3.2 on failure of differentiability in quadratic mean, Theorem 3.23 on local empirical-process power, Corollary 3.24.1 on \(c=3/2+\tau/\sqrt n\), and the proof step invoking contiguity. The paper does not calculate a Hellinger rate, an iid detection boundary, or an extreme-value critical profile. It explicitly leaves likelihood-based inference as future work.

Cai and Wu (2014) give general sparse-mixture detection theory in which Hellinger distance and extreme likelihood-ratio behavior determine detection boundaries. This establishes that the general detection principle is prior art; no inspected statement specializes their framework to the beta-precision hypergeometric path or gives the constant
\(H^2\sim a/[2\log(1/a)]\).

Morozova and Panov (2021) study triangular mixture models with vanishing heavy-tailed impurity and derive nonclassical limits for maxima. Their work makes clear that a discontinuous extreme-value limit from a shrinking heavy component is not a new general mechanism. The maximum theorem here is claimed only as the explicit critical profile induced by Lawford's beta-precision family and as a constructive witness for noncontiguity.

Searches for combinations of the hypergeometric family name, arXiv identifier 2609.20393, beta-precision normal mixtures, Gaussian boundary, Hellinger distance, contiguity, and logarithmic detection rates did not locate a prior statement of the sharp Hellinger asymptotic or the \((\log n)/n\) boundary for this family.

No inaccessible paper was identified whose title or abstract specifically indicates the displayed Hellinger asymptotic. Residual originality risk remains from general normal-scale-mixture and sparse-contamination theory under different notation. The originality claim is therefore limited to the explicit sharp boundary geometry and its consequences for this newly introduced path, not to Hellinger tensorization, sparse-mixture detection, or heavy-impurity extreme-value theory themselves.

## Value

**PASS.**

The result quantitatively resolves the nonregularity that the source paper identifies but does not measure. It shows that the parameter becomes statistically detectable at order \((\log n)/n\), much closer to the Gaussian boundary than the \(n^{-1/2}\) scale of the minimum-distance CDF theory.

This distinction has a concrete inferential consequence. At the Hellinger-critical scale the full iid experiments already have nontrivial separation, yet the source minimum-distance statistic has its null first-order law. Conversely, at \(a_n=\tau/\sqrt n\), an extreme-value test is consistent, so those alternatives cannot be contiguous even though they produce a standard root-\(n\) drift in the empirical CDF. This separates two notions of locality that coincide in regular models but diverge sharply here.

The result also pinpoints the scientific issue in the contiguity sentence used in the source proof without overclaiming: the minimum-distance local-power formula may be recoverable by a direct score/curvature argument, but contiguity is false for the hypergeometric root-\(n\) path.

## Sources inspected

- S. Lawford, *Gaussian Boundary Inference in a Hypergeometric Heavy-Tailed Family*, arXiv:2609.20393 (2026), especially the density/tail results, Proposition 2.11, Remark 3.2, Theorem 3.23, Corollary 3.24.1, and their proofs.
- T. T. Cai and Y. Wu, *Optimal detection of sparse mixtures against a given null distribution*, IEEE Transactions on Information Theory 60 (2014), 2217-2232.
- E. Morozova and V. Panov, *Extreme Value Analysis for Mixture Models with Heavy-Tailed Impurity*, Mathematics 9 (2021), 2208.
- Classical normal scale-mixture context cited by the source paper, including Andrews-Mallows and Barndorff-Nielsen-Kent-Sorensen, was used only as background; no claim of novelty is made for the mixture representation itself.

## Scientific limitations retained

The sharp calculation treats the standardized one-parameter path and does not analyze plug-in location/scale, identify the full critical likelihood-ratio experiment, or provide second-order Hellinger terms. The maximum limit is a model-specific specialization of known heavy-impurity extreme-value phenomena. General sparse-mixture and normal-scale-mixture theory remains a residual source of possible abstract coverage.
