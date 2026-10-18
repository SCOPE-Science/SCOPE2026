# Complete bivariate tail-dependence region under an independence sub-diagonal section

## Finding
Fix \(a\in(0,1)\). Let \(\mathcal C_a\) be all bivariate copulas \(C\) obeying
\[
C(a+t,t)=(a+t)t\qquad(0\le t\le 1-a).
\]
The function prescribed is the sub-diagonal section of the independence copula \(\Pi(u,v)=uv\). Define (when the limits exist)
\[
\lambda_L(C)=\lim_{\varepsilon\downarrow0}\frac{C(\varepsilon,\varepsilon)}{\varepsilon},\qquad
\lambda_U(C)=\lim_{\varepsilon\downarrow0}\frac{\mathbb P_C(U>1-\varepsilon,V>1-\varepsilon)}{\varepsilon}.
\]
**The exact joint identification region is**
\[
\big\{(\lambda_L(C),\lambda_U(C)):C\in\mathcal C_a,\text{ both limits exist}\big\}=[0,a]\times[0,a].
\]
In particular every ordered pair is attained *simultaneously* by an actual copula, including \((a,a)\); there is no tradeoff between the two tails. This holds for \(a>1/2\), when the natural lower-left and upper-right squares overlap.

## Assumptions and scope
A copula is a Borel probability measure \(\mu\) on \([0,1]^2\) with both marginals uniform, identified with its cumulative distribution \(C(u,v)=\mu([0,u]\times[0,v])\). The parameter \(a\) is fixed in the open unit interval. No smoothness, exchangeability, joint density, or prescribed diagonal is assumed. The tail coefficients are the standard diagonal lower-left and upper-right limits and are nonnegative when they exist. Endpoints are realized using singular couplings; the theorem is not a statement about the absolutely continuous subfamily.

## Proof
**Upper bounds.** For \(0<\varepsilon<1-a\), monotonicity and the known section give
\[
C(\varepsilon,\varepsilon)\le C(a+\varepsilon,\varepsilon)
=\varepsilon(a+\varepsilon).
\]
Consequently \(\lambda_L(C)\le a\). For the upper tail, the event \(\{U>1-\varepsilon,V>1-\varepsilon\}\) is contained in \(\{U>1-\varepsilon,V>1-a-\varepsilon\}\). By inclusion-exclusion and the section at \(t=1-a-\varepsilon\), the probability of the latter is
\[
1-(1-\varepsilon)-(1-a-\varepsilon)
+C(1-\varepsilon,1-a-\varepsilon)=\varepsilon(a+\varepsilon).
\]
Thus \(\lambda_U(C)\le a\), proving containment in the asserted square.

**Attaining arbitrary tails.** Take any \(\ell,u\in[0,a]\), and set \(\theta=\ell/a\), \(\eta=u/a\), and \(b=1-a\). Begin with Lebesgue product measure \(\mu_0\) on \([0,1]^2\). On the lower-left square \(Q_L=[0,a]^2\), replace its restriction by
\[
(1-\theta)\,\mu_0|_{Q_L}+\theta\,\nu_L,
\qquad \nu_L(E)=a\int_0^a\mathbf1_E(z,z)\,dz.
\]
These two finite measures have identical coordinate marginals, each equal to \(a\mathbf1_{[0,a]}(z)\,dz\), and total mass \(a^2\). Leave the measure unchanged off \(Q_L\), obtaining \(\mu_1\). Then \(\mu_1\) has uniform global marginals, and every rectangle \([0,a+t]\times[0,t]\) contains the entire horizontal extent of \(Q_L\). Its mass is therefore unchanged by this substitution, because the second marginal of the restricted measure is preserved. Hence the prescribed sub-diagonal section remains exact. For \(0<\varepsilon<\min(a,b)\), the lower-left corner mass is exactly
\[
\mu_1([0,\varepsilon]^2)=(1-\theta)\varepsilon^2+\theta a\varepsilon.
\]

Now restrict \(\mu_1\) to \(Q_U=[b,1]^2\) and call this finite measure \(\rho\), with coordinate marginals \(\rho_X,\rho_Y\). They have equal total mass, so they admit a comonotone coupling \(\rho^{\uparrow}\): if that common total mass is \(m>0\), take \(S\) uniformly distributed on \((0,m)\) and couple the generalized inverse cumulative functions of the two marginal measures evaluated at \(S\). The measure \(\rho^{\uparrow}\) has precisely the same two (not necessarily uniform) marginals as \(\rho\). Replace \(\rho\) inside \(Q_U\) by
\[
(1-\eta)\rho+\eta\rho^{\uparrow},
\]
leaving \(\mu_1\) elsewhere unchanged; call the result \(\mu\). Both global marginals remain uniform, so \(\mu\) defines a copula.

This second patch is supported in \(V\ge b\), and hence cannot change \(\mu([0,a+t]\times[0,t])\) for \(t<b\). By continuity of the uniform second marginal, the equality extends to \(t=b\). It is likewise disjoint from \([0,\varepsilon]^2\) for \(\varepsilon<b\), so the lower coefficient remains \(\ell\).

For \(0<\varepsilon<\min(a,b)\), all points with first coordinate greater than \(1-\varepsilon\), or second coordinate greater than \(1-\varepsilon\), lie outside \(Q_L\) in that coordinate. The first patch therefore leaves their joint law on the respective terminal strips equal to the original product law. In particular,
\[
\rho_X((1-\varepsilon,1])=\rho_Y((1-\varepsilon,1])=a\varepsilon,
\quad
\rho((1-\varepsilon,1]^2)=\varepsilon^2.
\]
The quantile-comonotone coupling saturates the minimum of those two terminal marginal masses, giving
\[
\rho^\uparrow((1-\varepsilon,1]^2)=a\varepsilon.
\]
Consequently, for all sufficiently small \(\varepsilon>0\),
\[
\mu((1-\varepsilon,1]^2)
=(1-\eta)\varepsilon^2+\eta a\varepsilon.
\]
Hence \(\lambda_U(\mu)=\eta a=u\). Together with \(\lambda_L(\mu)=\theta a=\ell\), this proves the entire closed square. The proof does not assume disjointness of \(Q_L\) and \(Q_U\), which is the key point when \(a>1/2\). \(\square\)

## Verification
A standalone exact-rational checker, `check_tail.py`, discretizes the two marginal-preserving rectangle replacements. For the first replacement it uses a diagonal coupling on a square checkerboard. For the second it uses the monotone northwest-corner quantile coupling of the restricted row and column masses. It verifies all row and column marginals, the entire prescribed sub-diagonal section at lattice points, and the exact terminal-cell probability identities for varying rational parameters, including overlapping squares. Its run completed **26,912 exact rational assertions**. The finite checker is a reproducibility aid, not an infinite-dimensional proof; the preceding measure argument proves the continuous and arbitrary-real statements.

## Relationship to prior work
Xie and Zou (2026) develop general sub-track-section constructions and pointwise upper and lower quasi-copula bounds; in their Section 7 they analyze statistical characterizations of a lower bound and concordance order. The line segment used here is the identity sub-diagonal case, but the present result is an exact *simultaneous feasible set of two tail limits under the independence section*, not a pointwise quasi-copula bound.

Quesada-Molina, Saminger-Platz and Sempi (2008) introduced constructions and sharp quasi-copula bounds for prescribed sub-diagonal sections, and de Amo, Díaz Carrillo and Fernández Sánchez (2013) established existence of absolutely continuous copulas with such sections. Durante, Saminger-Platz and Sarkoci (2009) introduced rectangular patchwork as a tool for changing tail dependence; the two marginal-preserving patches here use that established construction philosophy. None of those mathematical techniques is claimed as new. The finding isolates a precise identifiability region and its simultaneous attainability, including the case of overlapping corner squares. This is an assessment of examined statements rather than a claim of exhaustive priority certification.

## Limitations
The exact region is proved for the independence sub-diagonal section, not for arbitrary prescribed sections or curves; the resulting copulas can be singular, and no density-constrained attainable region is asserted. The result concerns existence of ordinary tail coefficients, not higher-order tail expansions or all tail-copula functions. The patchwork literature is broad, and an unlocated exact corollary remains a priority risk.

## References
1. J. Xie and W. Zou (2026), *Quasi-copulas with a prescribed sub-track section*, arXiv:2610.01247v1, first public 2026-10-01, https://arxiv.org/abs/2610.01247.
2. J. J. Quesada-Molina, S. Saminger-Platz and C. Sempi (2008), *Quasi-copulas with a given sub-diagonal section*, Nonlinear Analysis 69, 4654–4673, https://doi.org/10.1016/j.na.2007.11.021.
3. F. Durante, S. Saminger-Platz and P. Sarkoci (2009), *Rectangular Patchwork for Bivariate Copulas and Tail Dependence*, Communications in Statistics—Theory and Methods 38, 2515–2527, https://doi.org/10.1080/03610920802571203.
4. E. de Amo, M. Díaz Carrillo and J. Fernández Sánchez (2013), *Absolutely continuous copulas with given sub-diagonal section*, Fuzzy Sets and Systems 228, 105–113, https://doi.org/10.1016/j.fss.2012.10.002.
5. B. De Baets, H. De Meyer and M. Úbeda-Flores (2011), *Constructing Copulas with Given Diagonal and Opposite Diagonal Sections*, Communications in Statistics—Theory and Methods 40, 828–843, https://doi.org/10.1080/03610920903480866.
