# Exact visibility laws for concentric spherical shells in odd dimensions

## Finding
Let \(d\ge2\) be an integer, let \(0<a<1\), and let
\[
S_{d,a}=\{x\in\mathbb R^d:a\le\lVert x\rVert_2\le1\}.
\]
Choose \(X,Y\) independently with the uniform \(d\)-dimensional volume distribution on \(S_{d,a}\). Write \(b_d(a)=\mathbb P([X,Y]\subseteq S_{d,a})\) for the Beer index (two-point visibility probability). Define
\[
\alpha_a(r)=\arccos(a/r),\quad
c_d=\frac{\Gamma(d/2)}{\sqrt\pi\,\Gamma((d-1)/2)},\quad
H_d(t)=c_d\int_0^t\sin^{d-2}u\,du.
\]
For every \(d\ge2\), the *exact radial-cap identity* is
\[
\boxed{b_d(a)=\frac{d^2}{(1-a^d)^2}
\int_a^1\!\int_a^1 r^{d-1}s^{d-1}
H_d\bigl(\alpha_a(r)+\alpha_a(s)\bigr)\,dr\,ds.}
\]
Furthermore, \(b_d\) is strictly decreasing on \((0,1)\), with limits \(1\) and \(0\) as \(a\downarrow0\) and \(a\uparrow1\), respectively.

**Exact odd-dimensional laws.** For every odd \(d\ge3\), the function \(b_d(a)\) is a rational function of \(a\) with rational coefficients. In particular, letting \(Q_5(a)=1+a+a^2+a^3+a^4\),
\[
\boxed{b_3(a)=\frac{(1-a)(9a^3+27a^2+24a+8)}{8(1+a+a^2)^2},}
\]
\[
\boxed{b_5(a)=\frac{(1-a)^2(65a^6+260a^5+405a^4+320a^3+160a^2+64a+16)}{16Q_5(a)^2}.}
\]
At equal inner and outer-radius ratio \(a=1/2\), these give \(b_3(1/2)=223/392\) and \(b_5(1/2)=10397/15376\).

**Universal thin-shell exponent.** For every integer \(d\ge2\),
\[
\boxed{b_d(a)\sim\kappa_d(1-a)^{(d-1)/2}\quad(a\uparrow1),}
\]
where the strictly positive explicit constant is
\[
\boxed{\kappa_d=\frac{2^{(d+1)/2}\Gamma(d/2)}{\sqrt\pi\,\Gamma((d+1)/2)}
\sum_{j=0}^{d-1}\frac{\binom{d-1}{j}}{(j+2)(d+1-j)}.}
\]
Thus \(\kappa_3=17/18\) and \(\kappa_5=129/40\). The planar version of the visibility law is already known and is *not* proposed as novel here; the dimension-dependent rationality and explicit three-/five-dimensional formulas are the main additions.

## Assumptions and scope
All distances are Euclidean; the probability measure is normalized Lebesgue volume, *not* surface area of either sphere. Two endpoints are chosen independently. Their connecting closed Euclidean segment is visible when it avoids the *open* central ball of radius \(a\). Degenerate endpoints and tangencies have probability zero and do not affect the formulas. The scale is normalized to outer radius \(1\); by similarity, the parameter for general inner/outer radii is their ratio. Statements hold for every real \(a\in(0,1)\) and stated integer dimensions, without asymptotic restrictions except where explicitly indicated.

## Proof
**1. Critical visibility angle.** Fix endpoint radii \(r,s\ge a\), and let their angular separation be \(\theta\in[0,\pi]\). In the plane through the origin and endpoints, the boundary between visible and blocked segments is a common tangent line to the inner radius-\(a\) circle. In the tangent right triangles, the radii from the origin to the endpoints make angles \(\alpha_a(r)\) and \(\alpha_a(s)\) to their respective tangent rays. Thus the segment avoids the open inner ball if and only if
\[
\theta\le\alpha_a(r)+\alpha_a(s).
\]
For \(r=a\) or \(s=a\), this remains valid in the limiting tangent sense. Since the outer unit ball is convex, there is no additional obstruction from its exterior. Conditional on one uniform direction, the angle of the other has density \(c_d\sin^{d-2}\theta\) on \([0,\pi]\); the normalizing constant follows from \(\int_0^\pi\sin^{d-2}\theta\,d\theta=\sqrt\pi\Gamma((d-1)/2)/\Gamma(d/2)\). Independent radial distributions have densities \(d r^{d-1}/(1-a^d)\) on \([a,1]\). Multiplying and integrating establishes the boxed radial-cap identity.

**2. Strict decrease.** With independent \(U,V\) uniform on \((0,1)\), couple radii at every \(a\) by
\[
R_a=(a^d+(1-a^d)U)^{1/d},\qquad T_a=(a^d+(1-a^d)V)^{1/d}.
\]
For each \(0<U<1\), the ratio \(a/R_a\) is strictly increasing in \(a\), because
\[
\frac{d}{da}\log(a/R_a)=\frac{U}{a[a^d(1-U)+U]}>0.
\]
Consequently \(\alpha_a(R_a)+\alpha_a(T_a)\) strictly decreases pointwise; \(H_d\) strictly increases on \((0,\pi)\), proving strict decrease of \(b_d\). Dominated convergence gives the endpoint limits.

**3. Three dimensions.** Let \(A=a/R_a\), \(B=\sqrt{1-A^2}\), and let \(\mu_{pq}=\mathbb E[A^pB^q]\). In dimension \(3\), \(H_3(t)=(1-\cos t)/2\), while
\[
\cos(\alpha_a(r)+\alpha_a(s))=A(r)A(s)-B(r)B(s).
\]
Independence yields \(b_3=(1-\mu_{10}^2+\mu_{01}^2)/2\). Direct integration gives
\[
\mu_{10}=\frac{3a(1-a^2)}{2(1-a^3)},\qquad
\mu_{01}=\frac{(1-a^2)^{3/2}}{1-a^3}.
\]
Substituting and factoring proves the exact \(b_3\) rational formula.

**4. Five dimensions.** Here \(H_5(t)=(2-3\cos t+\cos^3t)/4\). Therefore
\[
 b_5=\frac12-\frac34(\mu_{10}^2-\mu_{01}^2)
 +\frac14(\mu_{30}^2-3\mu_{21}^2+3\mu_{12}^2-\mu_{03}^2).
\]
Writing \(Q=Q_5(a)\) and \(\Delta=1-a^2\), elementary radial antiderivatives give
\[
\begin{aligned}
\mu_{10}&=\frac{5a(1+a)(1+a^2)}{4Q},
&\mu_{01}&=\frac{(1+a)(2a^2+3)\sqrt\Delta}{3Q},\\
\mu_{30}&=\frac{5a^3(1+a)}{2Q},
&\mu_{21}&=\frac{5a^2(1+a)\sqrt\Delta}{3Q},\\
\mu_{12}&=\frac{5a(1-a)(1+a)^2}{4Q},
&\mu_{03}&=\frac{(1-a)(1+a)^2\sqrt\Delta}{Q}.
\end{aligned}
\]
Substitution into the cubic cosine identity and exact common-denominator expansion yield the stated \(b_5\) formula. These six moments and the algebraic identity are also independently checked by the supplied verifier.

**5. Rationality in all odd dimensions.** Put \(d=2m+1\). Since \(d-2=2m-1\) is odd, integrating \(\sin^{d-2}\theta\) gives \(H_d(\theta)\) as a rational-coefficient polynomial in \(\cos\theta\), with only odd nonconstant powers and constant term \(1/2\). After substituting \(\cos(\alpha(r)+\alpha(s))=A(r)A(s)-B(r)B(s)\) and expanding, independence makes each nonconstant term a rational linear combination of squares \(\mu_{pq}^2\), where \(p+q=k\) is an odd number not exceeding \(d-2\). The unnormalized radial moment integrand is
\[
 a^p r^{d-1-p-q}(r^2-a^2)^{q/2}\,dr.
\]
Its exponent on \(r\) is a positive odd integer. The substitution \(z=r^2-a^2\) reduces it to a *finite binomial sum* of powers of \(1-a^2\), with at most one factor \(\sqrt{1-a^2}\) when \(q\) is odd, divided by \(1-a^d\). Squaring removes that factor; hence every \(\mu_{pq}^2\), and thus \(b_d(a)\), is rational over \(\mathbb Q(a)\).

**6. Thin-shell limit.** For \(\varepsilon=1-a\), the uniform-radial coupling above satisfies, uniformly for \(u\in[0,1]\),
\[
\frac{\alpha_a((a^d+(1-a^d)u)^{1/d})}{\sqrt\varepsilon}
\longrightarrow\sqrt{2u}.
\]
The cap distribution has the boundary expansion
\[
H_d(t)=\frac{\Gamma(d/2)}{2\sqrt\pi\,\Gamma((d+1)/2)}t^{d-1}+O(t^{d+1}).
\]
Its bounded convergence over independent uniform \(U,V\) gives
\[
\lim_{a\uparrow1}\frac{b_d(a)}{(1-a)^{(d-1)/2}}
=\frac{2^{(d-1)/2}\Gamma(d/2)}{2\sqrt\pi\,\Gamma((d+1)/2)}
\mathbb E[(\sqrt U+\sqrt V)^{d-1}].
\]
Finally \(\mathbb E[U^{j/2}V^{(d-1-j)/2}]=4/[(j+2)(d+1-j)]\). A finite binomial expansion yields the stated \(\kappa_d\) and its dimensional specializations.

## Verification
The supplied `verify_shell_visibility.py` requires only the Python standard library. Running `python verify_shell_visibility.py` produces `EXACT_IDENTITIES_OK` followed by a numerical diagnostic and `VERIFY_OK`. The exact part computes the moment expansion independently of the displayed formulas and checks the closed three- and five-dimensional rational identities at \(4d+1\) distinct rational arguments. After clearing the stated denominators, their difference has polynomial degree at most \(4d\), so more than \(4d\) exact zeros certify the identity at *every* permitted radius ratio; this is an exact algebraic certificate, not approximate interpolation. A separate fixed-seed simulation directly minimizes distances along random endpoint segments and checks two parameter values in each dimension; it is a diagnostic only and supplies no proof of the general statements. The geometric angle argument and asymptotic proof do not depend on simulation.

## Relationship to prior work
The standard two-point visibility or Beer index is the central object in Balko, Jelínek, Valtr, and Walczak [1]. Their studied results concern comparison bounds for convexity measures and higher-order indices, rather than the present dimensional shell evaluation. Hodge, Marshall, and Patterson [2] **already computed the planar annulus visibility coefficient**, so a two-dimensional annulus formula is expressly not claimed as new. An examined full-text segment of [2] presents a planar polar integral and its evaluation. The three-/five-dimensional rational identities, the all-odd-dimensional rationality mechanism, and the universal dimension-specific thin-shell leading constant do not follow merely by taking the same planar formula at another radius. Targeted title/phrase and semantic searches found no equivalent full-dimensional shell statement, although a search cannot establish priority.

## Limitations
This concerns concentric *Euclidean* shells and independent volume-uniform endpoints; neither off-center holes nor boundary-uniform choices are covered. Rationality is proved for odd dimensions only; the even-dimensional integral identity and asymptotic exponent still hold. The method does not furnish a similarly short displayed numerator for every higher odd dimension, although it yields a finite algorithm. The planar coefficient is previously published, and unindexed historical calculations for spherical shells may exist. The algebraic verifier checks the displayed closed formulas; it does not independently certify geometric premises or the all-dimensional theorem. No independent audit has been performed.

## References
1. M. Balko, V. Jelínek, P. Valtr, B. Walczak, “On the Beer index of convexity and its variants,” arXiv:1412.1769v1 (first publicly posted 2014-12-04), subsequently *Discrete & Computational Geometry* 57 (2017), 179–214, DOI:10.1007/s00454-016-9821-3.
2. J. K. Hodge, E. Marshall, G. Patterson, “Gerrymandering and Convexity,” *College Mathematics Journal* 41(4) (2010), 312–324; accessible author-text manuscript dated 2010-02-18 (the manuscript date is not asserted to be its first online-publication date).
