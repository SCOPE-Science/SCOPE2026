# A sharp Spearman envelope beyond the restricted Kimeldorf–Sampson copula box
## Finding
Consider the two-parameter polynomial family
\[
C_{\alpha,\beta}(u,v)=uv\bigl[1+\alpha(1-u)(1-v)+\beta(1-u^2)(1-v^2)\bigr],
\qquad 0\le u,v\le1.
\]
Its mixed derivative is
\[
c_{\alpha,\beta}(u,v)=
1+\alpha(1-2u)(1-2v)+\beta(1-3u^2)(1-3v^2).
\]
Call a real pair \((\alpha,\beta)\) **fully admissible** if
\[
c_{\alpha,\beta}(u,v)\ge0
\quad\text{for all }(u,v)\in[0,1]^2.
\]
This is the exact copula-validity condition: the margins are already uniform and nonnegative density makes the candidate two-increasing. The fully admissible parameter set contains but is not limited to the restricted rectangle used in the 2026 source.

**Theorem (sharp extension envelope).** Over the entire fully admissible set,
\[
\boxed{\max \rho_S=\frac{\sqrt{57}-3}{12}
=0.379152869605895\ldots.}
\]
This maximum is attained at one and only one admissible pair,
\[
\boxed{
\alpha_*=-3+\frac{7\sqrt{57}}{19},
\qquad
\beta_*=1-\frac{\sqrt{57}}{19}.
}
\]
Numerically,
\[
\alpha_*=-0.218482050163408\ldots,
\qquad
\beta_*=0.602640292880487\ldots.
\]

The 2026 article specifies a smaller box
\[
|\alpha|\le\frac12,\qquad |\beta|\le\frac18,
\]
then describes its bounds as necessary and sufficient for copula validity and states the maximal uniform-margin correlation is
\[
\frac{25}{96}=0.260416666666667\ldots.
\]
The latter bound is correct **within that chosen box**, but the box is not necessary for nonnegativity of the same polynomial density. The full valid extension permits greater rank dependence than that box, and even greater rank dependence than the usual FGM copula cap \(1/3\).

## Assumptions and scope
The optimization ranges over **all real** \((\alpha,\beta)\) satisfying pointwise nonnegativity of the displayed continuous polynomial density on the **closed** unit square. Margins are uniform by construction. Spearman's rho of the copula is the quantity optimized, not Pearson correlation after arbitrary nonlinear marginal transforms.

The theorem preserves the algebraic copula family but relaxes the author's additional rectangular constraints. It does not say that the value \(25/96\) is wrong for the more restrictive model the authors actually fitted. The broader parameter class is a mathematically natural *admissible continuation* of that model.

## Proof
**Step 1: derive the objective.** For any copula \(C\),
\[
\rho_S=12\int_0^1\int_0^1(C(u,v)-uv)\,du\,dv.
\]
Here
\[
\int_0^1u(1-u)\,du=\frac16,
\qquad
\int_0^1u(1-u^2)\,du=\frac14,
\]
so
\[
\boxed{\rho_S=\frac{\alpha}{3}+\frac{3\beta}{4}.}
\]

**Step 2: one exact supporting inequality.** Put
\[
t_*:=\frac{9-\sqrt{57}}{24}\in\left(0,\frac1{\sqrt3}\right).
\]
This is the smaller root of
\[
24t^2-18t+1=0,
\]
so
\[
2(1-3t_*^2)=\frac94(1-2t_*).
\]
Any fully admissible density must be nonnegative at \((t_*,1)\):
\[
0\le c_{\alpha,\beta}(t_*,1)
=1-\alpha(1-2t_*)-2\beta(1-3t_*^2).
\]
Because \(1-2t_*>0\), this implies
\[
\frac{\alpha}{3}+\frac{3\beta}{4}
=\frac{\alpha(1-2t_*)+2\beta(1-3t_*^2)}{3(1-2t_*)}
\le\frac1{3(1-2t_*)}
=\frac{\sqrt{57}-3}{12}.
\]
This upper bound is global and does not assume signs or impose a rectangular parameter region.

**Step 3: realize the bound.** Define
\[
\beta_*:=\frac1{2-6t_*+6t_*^2}>0,
\qquad
\alpha_*:=-6t_*\beta_*.
\]
Elementary algebra gives exactly the radicals in the theorem and
\[
-1<\alpha_*<0,\qquad\beta_*>0.
\]
For these parameters the density's upper edge has an exact double zero:
\[
\boxed{c_{\alpha_*,\beta_*}(u,1)=6\beta_*(u-t_*)^2\ge0.}
\]
The lower edge is
\[
c_{\alpha_*,\beta_*}(u,0)
=1+\alpha_*(1-2u)+\beta_*(1-3u^2).
\]
As a function of \(u\) this is concave, and the endpoint values satisfy
\[
c_{\alpha_*,\beta_*}(0,0)
=1+\alpha_*+\beta_*=\frac{6\sqrt{57}}{19}-1>0,
\]
\[
c_{\alpha_*,\beta_*}(1,0)
=6\beta_*t_*^2>0.
\]
Therefore \(c_{\alpha_*,\beta_*}(u,0)>0\) for every \(u\in[0,1]\).

If \(u\le1/\sqrt3\), the density as a function of \(v\) is a quadratic whose \(v^2\) coefficient is
\[
-3\beta_*(1-3u^2)\le0.
\]
It is concave in \(v\), so its minimum on \([0,1]\) occurs at an endpoint. Both endpoint values have just been proved nonnegative. Symmetry covers the region where \(v\le1/\sqrt3\).

In the remaining square \(u,v>1/\sqrt3\), both factors \(1-2u\) and \(1-2v\) are negative, hence their product is in \([0,1]\). The product \((1-3u^2)(1-3v^2)\) is nonnegative. Thus
\[
c_{\alpha_*,\beta_*}(u,v)
\ge1+\alpha_*>0.
\]
This covers the entire closed square and proves full admissibility. Since \(c(t_*,1)=0\), the upper bound is attained.

**Step 4: uniqueness.** Any maximizer must have \(c_{\alpha,\beta}(t_*,1)=0\). Since \(t_*\in(0,1)\) and the edge density is nonnegative, its derivative with respect to \(u\) must vanish at \(t_*\). Hence
\[
\partial_u c_{\alpha,\beta}(t_*,1)=2\alpha+12\beta t_*=0.
\]
Solving this equation with \(c_{\alpha,\beta}(t_*,1)=0\) uniquely gives the pair \((\alpha_*,\beta_*)\) above.

## Verification
The included standalone Python/SymPy checker validates the source copula's density and Spearman formula symbolically. It verifies the exact quadratic equation for \(t_*\), the supporting-line identity, the sharp-value radicals, the upper-edge square factor, both lower-edge values, and the derivative condition ensuring uniqueness.

The checker also evaluates the density on a numerical grid, reporting the predicted zero at \((t_*,1)\) and \((1,t_*)\). The infinite-square nonnegativity conclusion does **not** depend on grid sampling: it is established by the analytic concavity-and-sign argument above.

## Relationship to prior work
Kimeldorf and Sampson (1975) introduced the pertinent bivariate uniform polynomial construction and discussed choosing coefficients to ensure nonnegative densities. The polynomial family itself and the general idea of copula uniform representations are therefore prior work. Their article is not cited as having established the sharp constant in this theorem; available extracted formulas from the archival article were partially degraded, so that historical comparison has some residual uncertainty.

Alawady et al. (2026) work with the strict rectangle \(|\alpha|\le1/2\), \(|\beta|\le1/8\). They give the same density and uniform-margin correlation formula, but state that the rectangle is necessary and sufficient for copula validity. Their upper bound \(25/96\) follows from linear maximization on that restricted rectangle. This theorem analyzes the strictly larger **maximal validity domain** of their unchanged polynomial expression and establishes its sharp rank-dependence cap with a uniquely optimal admissible pair.

The classical FGM subfamily \(\beta=0\) allows \(|\alpha|\le1\) and has \(|\rho_S|\le1/3\). That bound is an established special-case result, not the envelope for the full two-term polynomial family.

Focused searches for admissibility, equivalent polynomial kernels, unrestricted positivity, exact rank-correlation caps, the source DOI, and the radical constant located no published covering theorem. This is evidence of a gap, not an assertion that all possible unpublished or unindexed statements have been excluded.

## Limitations
The theorem does not determine the entire two-dimensional admissible parameter region; it exactly solves only the motivated linear rank-correlation optimization over that region.

It does not change any fitted result constrained to the original smaller parameter rectangle. It does not establish maximum **Pearson** correlation for arbitrary nonuniform EW margins.

Some formulas in the archival 1975 article were not recoverable cleanly from the available full-text extraction; an undiscovered prior derivation of the same envelope remains a residual originality risk.

## References
1. M. A. Alawady, H. M. Barakat, M. J. A. Alrawashdeh, D. A. Abd El-Rahman and I. A. Husseiny, “A thorough examination of the bivariate Kimeldorf-Sampson extended Weibull family in light of versatile statistical applications,” *AIMS Mathematics* 11 (2026), 9093–9125. DOI: 10.3934/math.2026375.
2. G. Kimeldorf and A. R. Sampson, “Uniform representations of bivariate distributions,” *Communications in Statistics* 4 (1975), 617–627. DOI: 10.1080/03610928308827274.
3. W. Schucany, W. C. Parr and J. E. Boyer, “Correlation structure in Farlie-Gumbel-Morgenstern distributions,” *Biometrika* 65 (1978), 650–653. DOI: 10.2307/2335922.
