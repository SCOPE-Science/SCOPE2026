# A sharp likelihood-ratio threshold for proportional-odds shock maxima

## Finding
Fix an integer \(n\ge 1\), two occurrence probabilities \(p,q\in(0,1)\), and two positive proportional-odds parameters \(\alpha,\beta>0\). Let \(M_{n;p,\alpha}\) and \(M_{n;q,\beta}\) be the maximum claims of two independent homogeneous portfolios, defined precisely below. For **every** strictly positive continuous baseline density on \((0,\infty)\), the likelihood-ratio order
\[
M_{n;p,\alpha}\le_{\mathrm{lr}}M_{n;q,\beta}
\]
holds if and only if
\[
\boxed{\begin{cases}
\beta p(1-q)\le\alpha q(1-p), &\beta\ge\alpha,\\[2mm]
(n-1)(\beta q-\alpha p)\ge2(\alpha-\beta), &0<\beta<\alpha.
\end{cases}}
\]
Here the first and second lines are alternatives selected by the parameter comparison, not simultaneous requirements. Equality is permitted in either line.

In particular, when \(\beta<\alpha\), the order is possible at some finite portfolio size if and only if \(\beta q>\alpha p\). In that event it holds exactly for the integers
\[
n\ge 1+\left\lceil\frac{2(\alpha-\beta)}{\beta q-\alpha p}\right\rceil.
\]
For example, \(\alpha=2,\ \beta=1,\ p=1/5,\ q=9/10\) gives an exact transition: the order fails for \(1\le n\le4\) and holds for every \(n\ge5\). Thus a portfolio with individually lighter claim severities but more frequent claims can dominate in the stronger likelihood-ratio sense, and the precise number of risks matters.

## Assumptions and scope
Let \(F\) be a continuously differentiable distribution function supported on \([0,\infty)\), with \(F(0)=0\), \(\lim_{x\to\infty}F(x)=1\), and \(f(x)=F'(x)>0\) for every \(x>0\). Write \(s(x)=1-F(x)\). A proportional-odds severity \(X_\alpha\) has survival function
\[
\mathbb P(X_\alpha>x)=\frac{\alpha s(x)}{1-s(x)+\alpha s(x)},\qquad x\ge0.
\]
Let \(I_p\) be Bernoulli with success probability \(p\), independent of \(X_\alpha\). Let \(M_{n;p,\alpha}\) be the maximum of \(n\) independent copies of \(I_pX_\alpha\). The comparator \(M_{n;q,\beta}\) is defined analogously with the **same baseline** and a potentially different occurrence probability and odds parameter. The two portfolios need not be coupled with one another, because the order depends only on their laws.

The distributions place positive mass at zero and are absolutely continuous with strictly positive density on \((0,\infty)\). The order \(A\le_{\mathrm{lr}}B\) means that the Radon–Nikodym likelihood ratio \(d\mathcal L(B)/d\mathcal L(A)\), with respect to the common measure \(\delta_0+dx\), is nondecreasing on \(\{0\}\cup(0,\infty)\). Thus **the jump at zero must also be checked**: comparing continuous densities alone is insufficient.

The theorem compares portfolios of equal fixed size \(n\), homogeneous independently thinned severities within each portfolio, and a common unrestricted positive baseline. No uniform integrability or tail moment assumptions are imposed.

## Proof
Set \(s=s(x)\in(0,1)\) and introduce the positive affine functions
\[
D_\alpha(s)=1-s+\alpha s,\qquad
E_{p,\alpha}(s)=1-s+\alpha(1-p)s.
\]
Since the one-risk distribution function is \(E_{p,\alpha}(s)/D_\alpha(s)\), independence gives, for \(x>0\),
\[
G_{n;p,\alpha}(x)=\left(\frac{E_{p,\alpha}(s)}{D_\alpha(s)}\right)^n,\qquad
G_{n;p,\alpha}(0)=(1-p)^n.
\]
Differentiating, using \(s'(x)=-f(x)\), gives the strictly positive density
\[
g_{n;p,\alpha}(x)=\frac{np\alpha f(x)E_{p,\alpha}(s)^{n-1}}{D_\alpha(s)^{n+1}}.
\]
Consequently, the comparator's density divided by the first density equals
\[
R(s)=\frac{q\beta}{p\alpha}
\left(\frac{E_{q,\beta}(s)}{E_{p,\alpha}(s)}\right)^{n-1}
\left(\frac{D_\alpha(s)}{D_\beta(s)}\right)^{n+1}.
\]
The survival coordinate \(s(x)\) is strictly decreasing, so \(R(s(x))\) is nondecreasing in \(x>0\) exactly when \(d\log R/ds\le0\) for all \(0<s<1\). Define
\[
h=\beta(1-q)-\alpha(1-p),\qquad
P(s)=\frac{E_{p,\alpha}(s)E_{q,\beta}(s)}{D_\alpha(s)D_\beta(s)}.
\]
Direct differentiation, including the factors with exponents \(n-1\) and \(n+1\), yields the exact identity
\[
\frac{d}{ds}\log R(s)
=\frac{n-1}{E_{p,\alpha}(s)E_{q,\beta}(s)}h
-\frac{n+1}{D_\alpha(s)D_\beta(s)}(\beta-\alpha)
=\frac{H(s)}{E_{p,\alpha}(s)E_{q,\beta}(s)},
\]
where
\[
H(s)=(n-1)h-(n+1)(\beta-\alpha)P(s).
\]
Each ratio \(E_{p,\alpha}/D_\alpha\) is a strictly decreasing function of \(s\), because its derivative equals \(-p\alpha/D_\alpha(s)^2<0\). Therefore \(P(s)\) is strictly decreasing with
\[
P(0)=1,\qquad P(1)=(1-p)(1-q).
\]

The atom likelihood ratio is \(((1-q)/(1-p))^n\), while the continuous likelihood ratio has right-hand limit
\[
\lim_{x\downarrow0}R(s(x))
=\frac{\alpha q}{\beta p}
\left(\frac{1-q}{1-p}\right)^{n-1}.
\]
The atom-to-density ordering requirement is therefore **equivalent** to
\[
\beta p(1-q)\le\alpha q(1-p).\tag{A}
\]

If \(\beta\ge\alpha\), the function \(H(s)\) has its greatest value at \(s=1\). Since the identity
\[
h-(\beta-\alpha)(1-p)(1-q)
=\beta p(1-q)-\alpha q(1-p)
\]
holds, condition (A) implies
\[
H(1)\le-2(\beta-\alpha)(1-p)(1-q)\le0.
\]
Thus the atom condition already forces the continuous likelihood ratio to be nondecreasing. Conversely, any likelihood-ratio order must satisfy (A), proving the first branch, including \(\alpha=\beta\).

If \(0<\beta<\alpha\), \(H(s)\) takes its greatest value at \(s=0\). The continuous likelihood ratio is nondecreasing exactly when
\[
H(0)=2(\alpha-\beta)-(n-1)(\beta q-\alpha p)\le0.
\]
This inequality forces \(\beta q>\alpha p\), hence \(q>p\); using \(\beta<\alpha\) then gives \(\beta p(1-q)<\alpha q(1-p)\). Therefore (A) holds automatically, proving the second branch. Conversely, failure of the displayed inequality yields \(H(s)>0\) near \(s=0\), so the positive-part likelihood ratio decreases for sufficiently large \(x\), ruling out the order. Both branches are necessary and sufficient, and the integer threshold and example follow by elementary rearrangement. \(\square\)

## Verification
The supplementary standalone script `verify.py` uses Python's exact rational arithmetic to compare the claimed parameter criterion against the extremal derivative and zero-atom conditions. It also independently expands both forms of the logarithmic derivative for representative parameter grids, including each boundary and the example with its sharp integer transition. Run with `python verify.py` using Python 3.10 or later; no third-party packages or external files are needed. The recorded execution passed 76,803 exact-rational checks. Those finite tests are **not** substitutes for the proof of the universal statement above, which rests on monotonicity of the product \(P(s)\) and endpoint algebra.

## Relationship to prior work
Panja, Kundu, Hazra and Pradhan (first public online version April 4, 2023) study the same Bernoulli-thinned proportional-odds largest-claim model. Their main theorems concern usual stochastic and reversed-hazard orders and, in a multiple-outlier setting, star order; in their concluding remarks they specifically propose investigation of **likelihood-ratio order** as a future direction. Their stated implications do not give an if-and-only-if likelihood-ratio comparison or the portfolio-size transition identified here. Das and Kayal (arXiv:2104.08605, first available April 17, 2021) establish comparison criteria for a general family of heterogeneous largest claims in different stochastic orders, but their inspected results do not supply the present sharp likelihood-ratio criterion for a shared proportional-odds baseline. Related stochastic-comparison literature on smallest claims and specialized severity families does not directly establish the present two-branch theorem.

The Wiley article by Kundu, Kundu and Hawlader (2023, DOI 10.1111/stan.12296) studies largest claims including Marshall–Olkin severities in a broader semiparametric setting. Only its abstract and bibliographic information could be examined; its complete theorem list is an unresolved bibliographic priority risk rather than evidence of noncoverage. Equivalence through a differently parameterized general likelihood-ratio theorem cannot be excluded without further human literature review.

## Limitations
This theorem does not treat heterogeneous risks within a portfolio, unequal portfolio sizes, dependent shocks, or independent portfolios with different baseline distributions. It excludes zero/one occurrence-probability endpoints and severities with atoms or support gaps. The criterion does **not** determine risk premiums or magnitudes of stochastic-order differences. The relative novelty assessment has residual uncertainty because a closely related 2023 article was not available in full text; no independent validation or priority determination has occurred.

## References
1. A. Panja, P. Kundu, N. K. Hazra and B. Pradhan, *Stochastic comparisons of largest claim and aggregate claim amounts*, Probability in the Engineering and Informational Sciences 38 (2024), 245–267. First published online 2023-04-04. DOI: https://doi.org/10.1017/S0269964823000104 . Open primary text: https://www.cambridge.org/core/journals/probability-in-the-engineering-and-informational-sciences/article/7436F764CB9968770B541811B7402F5E .
2. S. Das and S. Kayal, *Ordering results between the largest claims arising from two general heterogeneous portfolios*, Filomat 35 (2021), 1315–1332. First preprint 2021-04-17. https://arxiv.org/abs/2104.08605 .
3. P. Kundu, A. Kundu and B. Hawlader, *Stochastic comparisons of largest claim amounts from heterogeneous portfolios*, Statistica Neerlandica 77 (2023), 497–515. DOI: https://doi.org/10.1111/stan.12296 . Full text not inspected.
4. H. Nadeb, H. Torabi and A. Dolati, *Stochastic comparisons of the largest claim amounts from two sets of interdependent heterogeneous portfolios*, Mathematical Inequalities & Applications 23 (2020), 35–56. Preprint https://arxiv.org/abs/1812.08343 .
