# Sharp Haar Bowen-ball constants for unipotent Jordan toral dynamics

## Finding
For each integer \(d\ge2\), set \(S_d=d(d-1)/2\) and define the coefficient-body volume
\[V_d=\operatorname{vol}_d\left\{(a_0,\ldots,a_{d-1})\in\mathbb R^d:\max_{0\le t\le1}\left|\sum_{j=0}^{d-1}a_jt^j\right|\le1\right\}.\]
For the unipotent Jordan torus homeomorphism specified below, every Bowen ball has the sharp Haar-volume asymptotic
\[m_d(B_n(z,\varepsilon))=\frac{\varepsilon^d}{n^{S_d}}\left(\prod_{j=0}^{d-1}j!\right)\left(V_d+O_d(n^{-1})\right),\qquad 0<\varepsilon<1/4.\]
In dimension three, the new explicit coefficient-volume identity is \(V_3=272/9\), giving the limit \(544\varepsilon^3/9\) after multiplication by \(n^3\). The established polynomial-entropy exponent \(S_d\) is context, not a novelty claim.

## Assumptions and scope
Write \(\mathbb T=\mathbb R/\mathbb Z\) with circular distance \(\|s-t\|_{\mathbb T}=\min_{k\in\mathbb Z}|s-t-k|\). On \(\mathbb T^d\) use \(\rho(x,y)=\max_j\|x_j-y_j\|_{\mathbb T}\). Let \(m_d\) be normalized Haar (Lebesgue) probability and
\[F_d(x_1,\ldots,x_d)=(x_1,x_2+x_1,\ldots,x_d+x_{d-1})\pmod1.\]
For \(n\ge1\), define \(B_n(z,\varepsilon)=\{w:\rho(F_d^k w,F_d^k z)<\varepsilon\text{ for every integer }0\le k<n\}\). Fix \(d\ge2\) and \(0<\varepsilon<1/4\), then let \(n\to\infty\). The big-O constant depends only on \(d\); in particular it is uniform over centers and fixed allowed radii. Open versus closed inequalities do not change the volume.

## Proof
**1. No modular wrapping in a Bowen ball.** By translation invariance put \(z=0\). The difference \(u\in\mathbb T^d\) has a unique representative \((u_1,\ldots,u_d)\in(-\varepsilon,\varepsilon)^d\) at time zero. Put \(r_1(k)=u_1\), \(r_j(k+1)=r_j(k)+r_{j-1}(k)\) for \(j\ge2\). Induct on \(j\). If the preceding coordinate satisfies \(|r_{j-1}(k)|<\varepsilon\) for every observed time, then consecutive values of \(r_j\) differ by less than \(\varepsilon\). When both consecutive values have circular distance less than \(\varepsilon\) from zero, their nearest-integer representatives cannot change: two different integer neighborhoods would require a jump greater than \(1-2\varepsilon>\varepsilon\). Starting from \(r_j(0)\in(-\varepsilon,\varepsilon)\), the integer is always zero. Thus the Bowen constraints are equivalent to the real inequalities \(|r_j(k)|<\varepsilon\) for all \(j\) and \(0\le k<n\).

**2. Polynomial coefficient scaling.** The highest coordinate is
\[P_n(k)=r_d(k)=\sum_{\ell=0}^{d-1}\binom{k}{\ell}u_{d-\ell},\]
with generalized binomial coefficients interpreted as polynomials. Put \(N=n-1\) and \(Q_n(t)=P_n(Nt)=\sum_{\ell=0}^{d-1}a_\ell t^\ell\). The triangular map from \((u_d,u_{d-1},\ldots,u_1)\) to the ordinary coefficients \((a_0,\ldots,a_{d-1})\) has diagonal \(N^\ell/\ell!\), hence absolute Jacobian \(N^{S_d}/\prod_{\ell=0}^{d-1}\ell!\). The highest-coordinate constraints are exactly \(|Q_n(k/N)|<\varepsilon\) for \(k=0,\ldots,N\).

**3. Sampling and remaining coordinates.** Write \(M=\sup_{0\le t\le1}|Q_n(t)|\) and \(m= d-1\). Markov's polynomial inequality on \([0,1]\) states \(\sup|Q_n'|\le2m^2M\). Choosing the closest grid node, within \(1/(2N)\), yields \(M\le\varepsilon+(m^2/N)M\); hence \(M\le\varepsilon/(1-m^2/N)\) for \(N>m^2\). This gives inclusions between the sampled coefficient body and continuous sup-norm coefficient bodies of radii \(\varepsilon\) and \(\varepsilon/(1-m^2/N)\). Their volumes are \(\varepsilon^dV_d\) and \(\varepsilon^dV_d(1-m^2/N)^{-d}\). In particular all ordinary coefficients are bounded by \(C_d\varepsilon\) (finite-dimensional norm equivalence). Inverting the triangular binomial-to-power change of basis inductively gives \(|u_{d-j}|\le C_d\varepsilon N^{-j}\) for \(j=0,\ldots,d-1\). Therefore, for each lower coordinate \(j<d\),
\[\max_{0\le k\le N}|r_j(k)|\le C_d\varepsilon/N^{d-j}.\]
For all sufficiently large \(N\), every lower-coordinate constraint is automatic whenever the highest-coordinate sampled constraint holds. Consequently the actual Haar measure equals the sampled coefficient-body volume times \((\prod_{\ell=0}^{d-1}\ell!)N^{-S_d}\). The preceding inclusions imply
\[m_d(B_n(z,\varepsilon))=\varepsilon^d N^{-S_d}\left(\prod_{\ell=0}^{d-1}\ell!\right)V_d(1+O_d(N^{-1})).\]
Replacing \(N=n-1\) by \(n\) establishes the theorem. Every bound is uniform in \(z\) by translation invariance, and in \(\varepsilon\) by homogeneity.

**4. Exact quadratic volume.** Parametrize quadratic polynomials by
\[p(t)=u(1-t)+vt+wt(1-t),\]
where \(u=p(0)\), \(v=p(1)\). The transformation \((u,v,w)\mapsto(a_0,a_1,a_2)\) has absolute determinant one. For \(|u|,|v|\le1\), the inequalities \(-1\le p(t)\le1\) for all \(t\in[0,1]\) are equivalent to
\[-\bigl(\sqrt{1+u}+\sqrt{1+v}\bigr)^2\le w\le\bigl(\sqrt{1-u}+\sqrt{1-v}\bigr)^2.\]
Indeed the upper constraint requires \(w\le (1-u)/t+(1-v)/(1-t)\), whose minimum over \(0<t<1\) is the indicated square; the lower constraint is analogous. The admissible curvature interval has this exact length, so integration over \([-1,1]^2\) gives
\[V_3=16+4\left(\int_{-1}^{1}\sqrt{1-u}\,du\right)^2=16+4\left(\frac{4\sqrt2}{3}\right)^2=\frac{272}{9}.\]
Multiplying by \(0!1!2!=2\) yields \(544/9\), as asserted.

## Verification
The accompanying standalone `verify.py` uses exact fractions to check \(V_3=272/9\), the factor \(544/9\), and 5,950 exact finite orbit identities for the binomial-coordinate formula in dimensions two through six. It independently approximates \(V_3\) by midpoint quadrature over the derived admissible curvature intervals on three grids; the last approximation is about 30.2223. Execute `python3 verify.py` with standard Python 3. The infinite limit, modular lifting and Markov-step uniformity follow from the written analytic proof, not the finite diagnostics.

## Relationship to prior work
Cantat and Paris-Romaskevich, Lemma 4.4 of *Automorphisms of compact Kähler manifolds with slow dynamics* (2020), already prove \(h_{\mathrm{pol}}(F_d)=d(d-1)/2\) via polynomial iterates and spanning/separating grids. That exponent, its Jordan normal form, and corresponding coarse orbit-complexity estimates are prior art, not claimed here. Their lemma does not calculate the exact Haar measure of an individual Bowen ball, the coefficient-body limit \(V_d\), or the sharp three-dimensional number \(544/9\). Corrêa (2026) motivates renewed quantitative investigation of polynomial entropy on tori through rotation sets and lower bounds for homotopically trivial dynamics, without supplying this volume law. The new content is a sharp metric-and-measure-dependent local constant, rather than another derivation of an entropy exponent.

## Limitations
The result applies to the specified Jordan block with max-coordinate circular metric and Haar measure; it is not metric independent and does not provide sharp constants for arbitrary compatible metrics, nonlinear perturbations, or general unipotent matrices. The formula determines \(V_d\) as an exact finite-dimensional convex volume for every dimension but evaluates it numerically in closed form only for \(d=2,3\). The established entropy exponent is not new. General literature could contain an equivalent coefficient-body volume formula under a different name; no absolute priority is claimed.

## References
1. H. Corrêa, *Polynomial entropy and rotation sets*, Archiv der Mathematik (published 2026-09-12), DOI 10.1007/s00013-026-02286-3, https://doi.org/10.1007/s00013-026-02286-3.
2. S. Cantat and O. Paris-Romaskevich, *Automorphisms of compact Kähler manifolds with slow dynamics*, arXiv:2002.03615 (2020), especially Lemma 4.4 and its proof, https://arxiv.org/abs/2002.03615.
3. A. A. Markov, classical polynomial derivative inequality on an interval; used in its standard scaled form \(\|p'\|_{\infty,[0,1]}\le2m^2\|p\|_{\infty,[0,1]}\) for degree at most \(m\).
