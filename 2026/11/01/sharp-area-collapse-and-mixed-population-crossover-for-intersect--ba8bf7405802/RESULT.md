# Sharp area-collapse and mixed-population crossover for intersections of planar Brownian hulls

## Finding

Let \(K_1,K_2,\ldots\) be independent convex hulls of standard planar Brownian motions on \([0,1]\), each started at the origin. Let \(B_1,B_2,\ldots\) be independent convex hulls of standard planar Brownian bridges from the origin to itself on \([0,1]\), independent also of the motions. For nonnegative integers \(m,n\), with \(m+n\geq1\), put
\[
J_{m,n}=\bigcap_{i=1}^{m}K_i\cap\bigcap_{j=1}^{n}B_j,
\qquad A_{m,n}=\mathbb E\operatorname{area}(J_{m,n}).
\]
The convention for an empty intersection of one type is to omit that type.

Write \(L_m=\log m\), \(L_n=\log n\), and let \(\gamma\) denote Euler's constant. The two pure-population area laws have the following *second-order* expansions, with the constants and logarithmic corrections shown:
\[
A_{m,0}=\frac{\pi^4}{4m^2L_m^2}\left[1-\frac{2\log L_m+3\log(4/\pi)-1+\gamma}{L_m}+o(L_m^{-1})\right]\quad(m\to\infty),
\]
\[
A_{0,n}=\frac{\pi}{nL_n}\left[1-\frac{\log L_n+\log2}{L_n}+o(L_n^{-1})\right]\quad(n\to\infty).
\]

There is a single critical two-population scale: if \(m\to\infty\) and \(n=n_m\geq0\) satisfies \(n_m/(m^2\log m)\to\lambda\in[0,\infty)\), then
\[
A_{m,n_m}\sim\frac{\pi^4}{4m^2(\log m)^2}\,\Phi(\lambda),\qquad
\Phi(\lambda)=\int_0^\infty x\exp\left(-x-\frac{\pi^3\lambda}{4}x^2\right)\,dx.
\]
The function \(\Phi\) is strictly decreasing and continuous on \([0,\infty)\), with \(\Phi(0)=1\). Its large-parameter endpoint satisfies \(\Phi(\lambda)\sim 2/(\pi^3\lambda)\); this is an asymptotic of the crossover function, **not** a uniform assertion for sequences with \(\lambda\to\infty\).

The same crossover has a radial extreme-value form. Set \(c=2\sqrt2/\pi^{3/2}\) and \(a_m=(c m\log m)^{-1}\). For any fixed unit direction \(u\) and \(x\geq0\),
\[
\Pr\big\{\rho_{J_{m,n_m}}(u)>a_m x\big\}
\longrightarrow\exp\left(-x-\frac{\pi^3\lambda}{4}x^2\right),
\]
and the convergence extends to every fixed positive moment of the scaled radial function.

## Assumptions and scope

Brownian motions are standard two-dimensional processes with independent standard coordinate motions, unit time duration, and a common deterministic starting location at the origin. Bridges are standard pinned two-dimensional Brownian bridges with the same duration. All paths are mutually independent, but no independence between directional radii of any *one* hull is assumed or used. All convex hulls are closed compact convex sets, and their intersection contains the origin. The area is ordinary two-dimensional Lebesgue area. Only expected intersection areas, not the distribution of random areas, are claimed. The formulas are asymptotic for the specified populations; finite-sample equalities are not claimed.

## Proof

**1. Exact area reduction.** Fix a direction \(u\) and let \(R_K=\rho_{K_1}(u)\), \(R_B=\rho_{B_1}(u)\). Denote their CDFs by \(F_K,F_B\) and survivals by \(S_K=1-F_K,S_B=1-F_B\). Each hull contains the origin, so the radial function of an intersection is the minimum of the individual radial functions. Independence across hulls gives
\[
\Pr\{\rho_{J_{m,n}}(u)>r\}=S_K(r)^m S_B(r)^n.
\]
By polar integration, Tonelli, rotational invariance, and the layer-cake formula,
\[
A_{m,n}=\frac12\int_0^{2\pi}\!\mathbb E\rho_{J_{m,n}}(u_\theta)^2\,d\theta
=2\pi\int_0^\infty r S_K(r)^m S_B(r)^n\,dr.\tag{1}
\]
This is an exact integral representation for all \(m,n\) in the stated range.

**2. Two radial distributions and their first two small-radius terms.** Kabluchko's 2026 coverage result gives, for the fixed direction, the distributional representations
\[
R_K\overset{d}=|Z|\sqrt{U},\qquad
R_B\overset{d}=\sqrt{V(1-V)}\,T,
\]
where \(Z\) is standard normal, \(U\sim\operatorname{Beta}(1/2,1/2)\), \(V\sim\operatorname{Unif}(0,1)\), and \(T\) has Rayleigh density \(t e^{-t^2/2}\) on positive \(t\); the variables in each display are independent. Differentiating the corresponding mixture integrals, then applying the classical integral representation of modified Bessel \(K_0\), gives for \(r>0\)
\[
F_K'(r)=\frac c2 e^{-r^2/4}K_0(r^2/4),\qquad
F_B'(r)=2r e^{-r^2}K_0(r^2),\qquad c=\frac{2\sqrt2}{\pi^{3/2}}.\tag{2}
\]
As \(z\downarrow0\), \(K_0(z)=-\log(z/2)-\gamma+O(z^2|\log z|)\). Integrating (2) from zero to \(r\) yields
\[
F_K(r)=cr\left[\log(1/r)+d_K\right]+O(r^3\log(1/r)),\quad d_K=1+\frac32\log2-\frac\gamma2,\tag{3}
\]
\[
F_B(r)=r^2\left[2\log(1/r)+d_B\right]+O(r^4\log(1/r)),\quad d_B=1+\log2-\gamma.\tag{4}
\]
The remainders are absolute for sufficiently small positive \(r\). In particular, the first coverage deficit is of order \(r\log(1/r)\) for Brownian motion but \(r^2\log(1/r)\) for a pinned bridge. Equation (2), including its constants, can also be checked directly by differentiating the two independent mixture integrals; it is not assumed as an unexplained new identity.

**3. Pure motions, including the subleading logarithmic term.** Set \(L=\log m\), \(a=(cmL)^{-1}\). From (3), for every fixed \(x>0\),
\[
mF_K(ax)=x\left[1+\frac{\log L+\log c+d_K-\log x}{L}\right]+o(L^{-1}).\tag{5}
\]
The error after scaling is uniform on compact positive \(x\)-sets and sufficiently controlled on growing integration windows as explained below. Since \(mF_K(ax)^2=o(L^{-1})\) on these windows, the survival \(S_K(ax)^m\) has the corresponding exponential expansion. Substituting into (1) with \(n=0\) gives
\[
\frac{A_{m,0}}{2\pi a^2}=
\int_0^\infty xe^{-x}\,dx-
\frac1L\int_0^\infty x^2e^{-x}(\log L+\log c+d_K-\log x)\,dx+o(L^{-1}).
\]
The integrals are \(1\), \(2\), and \(3-2\gamma\) for weights \(xe^{-x}\), \(x^2e^{-x}\), and \(x^2e^{-x}\log x\), respectively. Hence
\[
A_{m,0}=2\pi a^2\left[1-\frac{2(\log L+\log c+d_K)-3+2\gamma}{L}+o(L^{-1})\right].
\]
Using \(2\pi/c^2=\pi^4/4\) and \(2\log c+2d_K-3+2\gamma=3\log(4/\pi)-1+\gamma\) proves the first expansion.

**4. Pure bridges.** Set \(L=\log n\), \(b=(nL)^{-1/2}\). Equation (4) similarly implies
\[
nF_B(bx)=x^2\left[1+\frac{\log L+d_B-2\log x}{L}\right]+o(L^{-1}).\tag{6}
\]
Therefore (1) gives
\[
\frac{A_{0,n}}{2\pi b^2}=\int_0^\infty xe^{-x^2}\,dx
-\frac1L\int_0^\infty x^3e^{-x^2}(\log L+d_B-2\log x)\,dx+o(L^{-1}).
\]
Here \(\int_0^\infty xe^{-x^2}dx=1/2\), \(\int_0^\infty x^3e^{-x^2}dx=1/2\), and \(\int_0^\infty x^3e^{-x^2}\log x\,dx=(1-\gamma)/4\). Consequently the relative correction is \(\log L+d_B-1+\gamma=\log L+\log2\), giving the claimed second expansion.

**5. Uniform-integrability justification for Steps 3–4.** For the pure-motion expansion, restrict initially the scaled integrals to \(L^{-3}\le x\le 12\log L\); for the bridge expansion, use \(L^{-3}\le x\le\sqrt{12\log L}\). On these windows, (3)–(4) and \(\log(1-\varepsilon)=-\varepsilon+O(\varepsilon^2)\) yield an integrated error \(o(L^{-1})\): the relative exponent corrections are \(O((\log L)/L)\), and their squares are \(o(L^{-1})\). The discarded lower windows contribute \(O(L^{-6})\) to the normalized second moments. The discarded intermediate upper tails are \(o(L^{-1})\), because (3)–(4) provide \(mF_K(ax)\ge x/2\) and \(nF_B(bx)\ge x^2/2\) while the original radius stays at most a small fixed constant (and these lower estimates also hold on the displayed upper windows). To control radii beyond that constant, choose any fixed small \(\varepsilon>0\). For \(r\ge\varepsilon\), the factors \(S_K(\varepsilon)^{m-2}\) and \(S_B(\varepsilon)^{n-2}\), respectively, multiply an integrable two-copy tail \(\int_\varepsilon^\infty rS(r)^2dr\); the resulting contribution is exponentially smaller than the normalizing scales. This proves the stated termwise integration and the negligible errors without relying on formal nonuniform Taylor expansions.

**6. Mixed critical window.** If \(n_m/(m^2L_m)\to\lambda\), (3) and (4) at \(r=a_m x\) imply
\[
mF_K(a_m x)\to x,\qquad
n_mF_B(a_m x)\to\frac{2\lambda}{c^2}x^2=\frac{\pi^3\lambda}{4}x^2
\]
for each fixed \(x>0\). Quadratic logarithmic errors vanish in the product of survivals, proving the stated radial limit. Positive moments converge by the same tail-cutoff argument as above, using only the Brownian-motion factor to dominate the mixed survival. Integrating the limiting squared radius via (1) yields the crossover \(\Phi\), with \(\pi(2a_m^2)=\pi^4/(4m^2L_m^2)\). Monotone dominated convergence proves continuity of \(\Phi\), differentiation under the integral gives strict decrease, and the change of variables \(y=\sqrt{\pi^3\lambda/4}\,x\) gives \(\Phi(\lambda)\sim2/(\pi^3\lambda)\) as \(\lambda\to\infty\). This completes the proof.

## Verification

Run `python check_intersection.py` with SciPy installed. The independent code checks the Bessel-CDF representation against the original Gaussian/arcsine and Rayleigh/uniform mixtures at four nonzero radii per type; both small-radius constants at two radii; exact simplifications of the two correction constants; numerical finite-population second-order area predictions; and the mixed radial crossover at three positions. The completed run printed `INTERSECTION_CHECK_OK: 25 independent numerical/algebraic checks; mixed crossover and two pure second-order expansions`. These are finite corroborations, not proofs of the limiting assertions. The proof above provides analytic, quantified limit arguments.

## Relationship to prior work

Kabluchko (2026, arXiv:2609.21687) establishes the individual planar Brownian-hull and bridge-hull point-coverage laws used in Step 2, and studies their small- and large-distance asymptotics. The exact single-hull radial representations and standard Bessel identities are **prior ingredients**, not claimed as new. The present contribution is their simultaneous geometric use to quantify the shrinking *intersection* of many independent hulls, including a mixed-population critical threshold and explicit second-order pure-population area laws. Randon-Furling, Majumdar, and Comtet (2009, arXiv:0907.0921) and Šebek (2024, arXiv:2406.07079) compute properties of convex hulls of **unions** of multiple Brownian trajectories; union hulls grow with population, whereas the intersection here shrinks. The contrasting set operation makes their statements non-implicative for the claimed constants. A historically equivalent intersection asymptotic in alternate language cannot be ruled out definitively.

## Limitations

Only unit-time standard isotropic planar processes and mean areas are covered. Radial distributions across different angles within any single hull remain correlated; no independence of angles or concentration of random area is asserted. The mixed law is for finite \(\lambda\); the large-\(\lambda\) statement concerns the limiting crossover function, not a uniform regime with arbitrary simultaneous growth. The displayed next-order expansions are only for pure populations. The conclusion relies on the 2026 radial-distribution theorem and has not undergone independent mathematical validation or exhaustive historical-priority assessment.

## References

1. Z. Kabluchko, “Coverage probability of the planar Brownian convex hull,” arXiv:2609.21687, first posted 2026-09-18, https://arxiv.org/abs/2609.21687.
2. J. Randon-Furling, S. N. Majumdar, and A. Comtet, “Convex Hull of N Planar Brownian Motions: Exact Results and an Application to Ecology,” arXiv:0907.0921 (2009), https://arxiv.org/abs/0907.0921.
3. S. Šebek, “Convex Hull of Brownian Motion and Brownian Bridge,” arXiv:2406.07079 (2024), https://arxiv.org/abs/2406.07079.
4. NIST Digital Library of Mathematical Functions, modified Bessel function small-argument expansion, https://dlmf.nist.gov/10.31.
