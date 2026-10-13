# Reciprocal scale makes the modified Muth likelihood globally strictly concave
## Finding
For every deterministic sample \(x_1,\ldots,x_n>0\), with \(n\ge1\), from the modified Muth scale model of Barakat et al. (2026), set \(\eta=1/\theta\). The log-likelihood becomes
\[
\ell(\eta)=n\log\eta-n\log2+2\sum_{i=1}^n\log(e^{\eta x_i}-1)+\eta\sum_{i=1}^n x_i-\sum_{i=1}^n(e^{\eta x_i}-1).
\]
It is globally strictly concave on \((0,\infty)\), tends to \(-\infty\) at both ends of that interval, and therefore has exactly one interior global maximizer. Consequently the modified Muth scale parameter has a unique maximum-likelihood estimate for every positive sample.

The original scale coordinate behaves differently: its log-likelihood is eventually convex as \(\theta\to\infty\). Thus the likelihood is globally well behaved, but global concavity is revealed by reciprocal scale rather than by the source's original \(\theta\)-coordinate.

## Assumptions and scope
The source defines the modified Muth scale density, for \(x>0\) and \(\theta>0\), by scaling its canonical density. For a positive sample \(x_1,\ldots,x_n\), its Section 3.1 log-likelihood is
\[
\ell(\theta)=-n\log(2\theta)+2\sum_{i=1}^n\log(e^{x_i/\theta}-1)+\frac1\theta\sum_{i=1}^n x_i-\sum_{i=1}^n(e^{x_i/\theta}-1).
\]
No stochastic asymptotics, sample-size lower bound beyond \(n\ge1\), or generic-position condition is needed. The result concerns maximum likelihood for the single scale parameter only; it does not address the source's maximum-product-spacing or minimum-distance estimators.

## Proof
Put \(\eta=1/\theta\). Differentiation gives the score
\[
U(\eta)=\ell'(\eta)=\frac n\eta+\sum_{i=1}^n x_i\left(\frac{2e^{\eta x_i}}{e^{\eta x_i}-1}+1-e^{\eta x_i}\right).
\]
A second differentiation yields
\[
\ell''(\eta)=-\frac n{\eta^2}-\sum_{i=1}^n x_i^2e^{\eta x_i}-2\sum_{i=1}^n\frac{x_i^2e^{\eta x_i}}{(e^{\eta x_i}-1)^2}.
\]
Every term on the right is negative for \(\eta>0\) and \(x_i>0\), so \(\ell\) is strictly concave on the whole positive half-line.

As \(\eta\downarrow0\),
\[
\log(e^{\eta x_i}-1)=\log\eta+\log x_i+o(1),
\]
so
\[
\ell(\eta)=3n\log\eta+2\sum_{i=1}^n\log x_i-n\log2+o(1)\longrightarrow-\infty.
\]
As \(\eta\to\infty\), each observation contributes
\[
2\log(e^{\eta x_i}-1)+\eta x_i-(e^{\eta x_i}-1)
=-e^{\eta x_i}+3\eta x_i+O(1),
\]
which tends to \(-\infty\). Hence \(\ell(\eta)\to-\infty\) at both boundaries. Continuity therefore gives an interior maximizer, and strict concavity makes it unique. Equivalently, \(U(\eta)\) is strictly decreasing, with \(U(\eta)\to+\infty\) as \(\eta\downarrow0\) and \(U(\eta)\to-\infty\) as \(\eta\to\infty\); the MLE is the unique positive score root.

Finally, return to the original scale. The large-\(\theta\) expansion \(e^{x_i/\theta}-1=x_i/\theta+O(\theta^{-2})\) gives
\[
\ell(\theta)=-3n\log\theta+2\sum_{i=1}^n\log x_i-n\log2+o(1).
\]
Differentiating the corresponding asymptotic expansion, or expanding the exact second derivative one order further, gives
\[
\ell''(\theta)=\frac{3n}{\theta^2}+o(\theta^{-2})>0
\]
for all sufficiently large \(\theta\). Therefore global concavity in the original scale coordinate is impossible even though the maximizer is unique.

## Verification
The critical derivative can be checked observation by observation. For
\[
h(\eta;x)=2\log(e^{\eta x}-1)+\eta x-(e^{\eta x}-1),
\]
one has
\[
h''(\eta;x)=-x^2e^{\eta x}-\frac{2x^2e^{\eta x}}{(e^{\eta x}-1)^2}<0.
\]
Adding the contribution \(-n/\eta^2\) from \(n\log\eta\) proves strict concavity without numerical sampling. The two boundary expansions prove existence, so the argument establishes both existence and uniqueness rather than merely uniqueness conditional on a stationary point.

No finite experiment is used to infer a global property. The proof applies to every finite positive sample. The only excluded data configurations are those containing zero, which lie outside the model's stated open support.

## Relationship to prior work
Barakat et al. (2026) derive the likelihood and score for the modified Muth scale parameter. They report numerical evidence of a single maximum and state that formal proofs of unimodality and uniqueness are left for future theoretical work. The same article says numerical inspection suggests concavity in practice. The result here closes the maximum-likelihood part of that stated gap exactly: reciprocal scale gives strict global concavity and a unique score root for every positive sample. It also clarifies that the original-scale numerical concavity cannot be a global theorem because the original-scale likelihood is eventually convex.

Jodrá, Jiménez-Gamero, and Alba-Fernández (2015) study maximum-likelihood estimation for the classical Muth distribution. Their likelihood analysis solves the score numerically and checks the second derivative at a candidate solution; the inspected treatment does not establish the present modified-Muth reciprocal-scale theorem or a samplewise global uniqueness result.

Focused searches using the model name, DOI, likelihood-concavity terminology, reciprocal-scale aliases, and unique-MLE terminology located no statement implying this theorem and no correction notice covering it.

## Limitations
The theorem is about the modified Muth maximum-likelihood estimator for complete positive samples. It does not prove global convexity or uniqueness for the source's maximum-product-spacing, least-squares, weighted least-squares, Cramér–von Mises, or Anderson–Darling criteria.

The result also does not claim that Newton iteration from an arbitrary starting value is globally convergent without safeguards. Strict monotonicity of the reciprocal-scale score does, however, permit bracketing and one-dimensional safeguarded root finding.

An unindexed note or a sufficiently general likelihood theorem under different terminology could contain an equivalent observation; no such covering source was found in the searches and primary-source inspections performed here.

## References
1. H. M. Barakat, H. S. Bakouch, M. A. Abd Elgawad, H. Semary, M. A. Alawady, I. A. Husseiny, M. G. Enany, and T. S. Taher, “The modified Muth distribution: Statistical properties, entropy measures, and parameter estimation,” AIMS Mathematics 11 (2026), 6269–6296. DOI: 10.3934/math.2026259.
2. P. Jodrá, M. D. Jiménez-Gamero, and M. V. Alba-Fernández, “On the Muth Distribution,” Mathematical Modelling and Analysis 20 (2015), 291–310. DOI: 10.3846/13926292.2015.1048540.
