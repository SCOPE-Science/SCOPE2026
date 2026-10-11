# Sharp small-scale strong-rotundity coefficient of real \(L_p\) spaces for \(p>2\)

## Finding

Let \((\Omega,\Sigma,\mu)\) be a measure space admitting two disjoint measurable sets of strictly positive finite measure. Let \(X=L_p(\mu;\mathbb R)\) with \(2<p<\infty\). Define
\[
\phi_p(t)=\frac{|t+1|^p-|t|^p-p|t|^{p-2}t}{p},\qquad
c_p=\min_{t\in\mathbb R}\phi_p(t).
\]
Then \(0<c_p<1/p\), and García-Pacheco's **global index of strong rotundity** satisfies
\[
\eta_X(\varepsilon)\ge c_p\varepsilon^p\quad(0\le\varepsilon\le2),
\qquad
\boxed{\lim_{\varepsilon\downarrow0}\frac{\eta_X(\varepsilon)}{\varepsilon^p}=c_p}.
\]
In particular, \(c_4=1/12\); hence every such real \(L_4\) space has \(\lim_{\varepsilon\downarrow0}\eta_X(\varepsilon)/\varepsilon^4=1/12\). The first estimate is global in scale, while the coefficient's attainability is asserted only in the small-scale limit.

## Assumptions and scope

The unit sphere and closed unit ball of a Banach space \(X\) are \(S_X\) and \(B_X\). Put
\[
\Pi_X=\{(x,f)\in S_X\times S_{X^*}:f(x)=1\},
\quad H_f=\{z\in X:f(z)=1\}.
\]
For \(\varepsilon\in[0,2]\), the local and global indices in the cited 2023 definition are
\[
\eta_X(\varepsilon;(x,f))
=\operatorname{dist}\bigl(H_f,\{y\in B_X:\|x-y\|\ge\varepsilon\}\bigr),
\quad
\eta_X(\varepsilon)=\inf_{(x,f)\in\Pi_X}\eta_X(\varepsilon;(x,f)).
\]
Distance between two sets means infimum of pairwise norms. The two disjoint finite-positive-measure sets provide an isometric copy of real \(\ell_p^2\). No nonatomicity or infinite-dimensionality is assumed. The assertion concerns real scalars and exponents strictly above \(2\). When \(p=2\), the cited source already computes \(\eta_X(\varepsilon)=\varepsilon^2/2\) in dimensions at least two.

## Proof

**1. Distance to the supporting hyperplane.** For a pair \((x,f)\in\Pi_X\) and \(y\in B_X\), the functional norm gives \(\|z-y\|\ge 1-f(y)\) for all \(z\in H_f\). Choosing \(z=y+(1-f(y))x\) yields \(z\in H_f\) and equality. Thus
\[
\eta_X(\varepsilon;(x,f))
=\inf_{\substack{\|y\|\le1\\\|x-y\|\ge\varepsilon}}(1-f(y)).
\tag{1}
\]

**2. Sharp pointwise remainder.** For \(p>2\), the scalar function \(a\mapsto |a|^p/p\) is strictly convex. For \(b\ne0\), homogeneity (and simultaneous sign reversal) gives
\[
\frac{|a+b|^p-|a|^p-p|a|^{p-2}ab}{p|b|^p}
=\phi_p(a/b)\ge c_p.
\]
For \(b=0\) the same inequality holds trivially. Strict convexity implies \(\phi_p(t)>0\). Its continuous growth \(\phi_p(t)\sim\frac{p-1}{2}|t|^{p-2}\to\infty\) as \(|t|\to\infty\) ensures that the minimum exists and is positive. Moreover, \(\phi_p(0)=1/p\), while its derivative at zero is \(1>0\), so moving to a small negative \(t\) strictly lowers \(\phi_p\); hence \(c_p<1/p\). The minimizers lie in \((-1,0)\): for \(t\ge0\), the derivative \(\phi_p'(t)=(t+1)^{p-1}-t^{p-1}-(p-1)t^{p-2}\) is nonnegative by convexity of the power function, so \(\phi_p(t)\ge 1/p\). For \(t=-s\le-1\), \(\phi_p(-s)=((s-1)^p-s^p+ps^{p-1})/p\) is nondecreasing as a function of \(s\ge1\) (differentiate and compare the power increment to its endpoint derivative), so \(\phi_p(t)\ge(p-1)/p>1/p\).

**3. Uniform lower bound.** Every unit vector \(x\in X\) has the unique norm-one supporting functional
\[
J_p(x)(y)=\int_\Omega |x|^{p-2}xy\,d\mu.
\]
Integrating the scalar remainder for \(a=x\), \(b=y-x\) yields
\[
\frac{\|y\|_p^p-1}{p}+1-J_p(x)(y)
\ge c_p\|y-x\|_p^p.
\]
For \(\|y\|_p\le1\), the first term on the left is nonpositive; therefore \(1-J_p(x)(y)\ge c_p\|y-x\|_p^p\). Equation (1), followed by the infimum over unit \(x\), gives the global lower bound for all \(0\le\varepsilon\le2\).

**4. Matching upper coefficient.** Choose any minimizer \(t_p\in\mathbb R\) of \(\phi_p\), and select disjoint unit vectors \(e_1,e_2\) supported on finite-positive-measure sets. For sufficiently small \(h>0\), put
\[
 x_h=(1-|t_p|^ph^p)^{1/p}e_1+t_ph e_2,
 \qquad
 y_h=(1-|t_p+1|^ph^p)^{1/p}e_1+(t_p+1)h e_2.
\]
Both vectors have norm \(1\), and \(\|x_h-y_h\|_p\ge h\) because their second coefficients differ by exactly \(h\). Taylor expansion of \((1-u)^{1/p}\) at \(u=0\), and the formula for the support functional, give
\[
1-J_p(x_h)(y_h)
=\frac{|t_p+1|^p-|t_p|^p-p|t_p|^{p-2}t_p}{p}\,h^p+O(h^{2p})
=c_ph^p+O(h^{2p}).
\]
Equation (1) with \(\varepsilon=h\) implies \(\eta_X(h)\le c_ph^p+O(h^{2p})\). Combined with the global lower bound, this proves the two-sided limit as \(h\downarrow0\), for every sufficiently small positive \(h\), not merely along a discrete subsequence.

**5. Exact quartic coefficient.** For every real \(a,b\), direct expansion gives
\[
\frac{(a+b)^4-a^4-4a^3b}{4}
=\frac32 b^2\left(a+\frac b3\right)^2+\frac1{12}b^4.
\]
Consequently \(c_4=1/12\), attained in the scalar minimization at \(t_4=-1/3\).

## Verification

The standalone Python 3 standard-library program `verify.py` checks the quartic factorization using exact rational arithmetic on 441 scalar pairs. It separately tests 19,607 numerical scalar samples over seven exponents above two and 35 explicit two-point unit-sphere pairs approaching the predicted sharp asymptotic coefficient. A representative check for \(p=4\) returns \(c_4=0.0833333333333\) and normalized deficits approaching that value as \(h\) decreases. These computations are diagnostic only; the infinite-domain and all-exponent assertions are established by the analytic proof above, not by enumeration.

To reproduce, use a standard Python 3 installation and run `python verify.py` in the directory containing the extracted document files.

## Relationship to prior work

García-Pacheco (2023, Definition 2.1) introduces precisely the global index used here and evaluates it for Hilbert spaces (Corollary 2.1), with a general comparison to local convexity in Theorem 2.4. The present theorem computes its **sharp non-Hilbert small-scale coefficient** uniformly across the entire real \(L_p\) class for \(p>2\), not the already-known Hilbert branch. Standard Clarkson-Hanner modulus estimates give a power-type lower bound, but the sharp global supporting-hyperplane coefficient is finer; at \(p=4\), the new coefficient \(1/12\) improves the leading coefficient \(1/32\) obtainable directly from the general inequality \(\eta_X\ge 2\delta_X\). Campos-Jiménez and García-Pacheco (2024) study the index through faces and the core of the unit sphere, without this coefficient. Sprung (2019) studies Bregman lower bounds for powers of norms; the scalar remainder is a related tool, but its general estimates are not a statement of the global strong-rotundity asymptotic with a matching two-coordinate extremizing family. A quantitative sharp power-remainder bound, if independently known, does not by itself give the equality of this **norm-one constrained global index** without the upper construction.

## Limitations

The coefficient is an exact one-dimensional minimization, not an elementary closed form for every real \(p\). Apart from the lower bound, no finite-\(\varepsilon\) exact formula for \(\eta_X\) is asserted. The theorem does not cover \(1<p<2\), nonreal spaces, or one-dimensional \(L_p\). Older sharp Bregman inequalities, including the Xu–Zhang (1989) paper cited by Sprung, may contain relevant constants; that inaccessible source remains a comparison risk. 

## References

1. F. J. García-Pacheco, *The index of strong rotundity*, AIMS Mathematics **8** (2023), 20477–20486. DOI: 10.3934/math.20231043. First online publication 25 June 2023. https://www.aimspress.com/aimspress-data/math/2023/9/PDF/math-08-09-1043.pdf
2. A. Campos-Jiménez and F. J. García-Pacheco, *The core of the unit sphere of a Banach space*, AIMS Mathematics **9** (2024), 3440–3452. DOI: 10.3934/math.2024169. https://www.aimspress.com/aimspress-data/math/2024/2/PDF/math-09-02-169.pdf
3. B. Sprung, *Upper and lower bounds for the Bregman divergence*, Journal of Inequalities and Applications **2019**, article 4. DOI: 10.1186/s13660-018-1953-y. https://link.springer.com/article/10.1186/s13660-018-1953-y
4. Z.-B. Xu and Z.-S. Zhang, *Another set of characteristic inequalities of \(L^p\) spaces*, Acta Math. Sinica **37** (1989), 433–439, cited in [3]; full text not inspected.
