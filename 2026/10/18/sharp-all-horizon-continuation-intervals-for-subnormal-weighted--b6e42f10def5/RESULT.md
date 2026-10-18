# Sharp all-horizon continuation intervals for subnormal weighted shifts

## Finding

**Theorem (sharp pointwise continuation).** Let \(W\) be a bounded subnormal unilateral weighted shift with strictly positive weights \(w_j\), and assume its Berger measure is supported in \([a,b]\), where \(0<a<b<\infty\). Fix any integer \(n\geq0\) and suppose the two observed consecutive squared weights are
\[
 w_n^2=m,\qquad w_{n+1}^2=s,\qquad v=m(s-m).
\]
Necessarily \(a\le m\le b\) and \(0\le v\le(m-a)(b-m)\). If \(v=0\), all future squared weights equal \(m\). For \(v>0\), define
\[
 c=m-\frac{v}{b-m},\qquad d=m+\frac{v}{m-a},
 \qquad p_+=\frac{m-c}{b-c},\qquad p_-=\frac{m-a}{d-a}.
\]
For each integer \(h\geq1\), put
\[
 L_h=\frac{(1-p_-)a^{h+1}+p_-d^{h+1}}{(1-p_-)a^h+p_-d^h},
 \qquad
 U_h=\frac{(1-p_+)c^{h+1}+p_+b^{h+1}}{(1-p_+)c^h+p_+b^h}.
\]
Then
\[
 \boxed{L_h\le w_{n+h}^2\le U_h.}
\]
For every fixed admissible \((a,b,m,v,n,h)\), both bounds are **attained by subnormal weighted shifts** whose tilted Berger measures have two atoms. Every intermediate value also occurs for some subnormal shift with exactly those observed weights and the same support constraint. For \(h\ge2\), each endpoint extremizer is uniquely determined at the level of the tilted Berger measure; if \(v=(m-a)(b-m)\), the two measures and endpoints coincide. This is a pointwise range for each horizon, not a claim that independently chosen values at different horizons are jointly realizable.

## Assumptions and scope

All weights are positive, the scalar Hilbert space is \(\ell^2(\mathbb N_0)\), and \(We_j=w_je_{j+1}\). A Berger measure \(\mu\) is a probability measure whose moments \(\gamma_j=\int t^j\,d\mu(t)\) satisfy \(w_j^2=\gamma_{j+1}/\gamma_j\). The measure is assumed supported inside the **strictly positive** compact interval \([a,b]\). A support bound is essential; without it the two measured weights do not determine these envelopes. We allow \(\mu\) to have smaller support than \([a,b]\).

The claim fixes \(n\), \(m\), and \(s\), not any earlier weights. All assertions hold for every \(n\ge0\), every admissible variance \(v\), and every integer horizon \(h\ge1\). The norm constraint implied by support is \(\|W\|\le\sqrt b\); equality holds for the upper extremizer when its measure charges \(b\).

## Proof

**1. Moment tilting.** Define \(d\nu_n(t)=t^n\,d\mu(t)/\gamma_n\). Writing expectation under \(\nu_n\) as \(\mathbb E\), we have
\[
 \mathbb E X=m,\quad \mathbb E X^2=m^2+v,
 \quad w_{n+h}^2=\frac{\mathbb E X^{h+1}}{\mathbb E X^h}.
\]
The support bound gives \(v\le(m-a)(b-m)\) by averaging \((X-a)(b-X)\ge0\). If \(v=0\), \(\nu_n\) is a point mass, so the strictly positive tilt implies \(\mu\) is the same point mass. Otherwise \(a<m<b\). The two measures
\[
 \nu_+=(1-p_+)\delta_c+p_+\delta_b,
 \qquad \nu_-=(1-p_-)\delta_a+p_-\delta_d
\]
are probability measures supported in \([a,b]\), with the same first and second moments \(m,m^2+v\) as \(\nu_n\). Their higher moment ratios are \(U_h\) and \(L_h\).

**2. Polynomial sign lemma.** Let \(h\ge2\), let \(0<r_1,r_2,r_3\), and put \(G(t)=\prod_{i=1}^3(t-r_i)\). For \(0<\lambda\le R=\max_i r_i\), divide \(f_\lambda(t)=t^{h+1}-\lambda t^h\) by \(G(t)\), obtaining a quadratic remainder \(P(t)\) and quotient \(Q(t)\). The quotient is nonnegative for every \(t\ge0\). Indeed, with \(H_j(r_1,r_2,r_3)\) denoting the complete homogeneous polynomial of degree \(j\) (and \(H_0=1\)), long division gives
\[
 Q(t)=t^{h-2}+\sum_{j=1}^{h-2}
 [H_j-\lambda H_{j-1}]t^{h-2-j}.
\]
Because one root equals \(R\), the generating-function recurrence gives \(H_j\ge R H_{j-1}\), hence every coefficient of \(Q\) is nonnegative. Its leading monomial is strictly positive for \(t>0\). The same formula covers \(h=2\) with \(Q=1\). In particular, \(f_\lambda-P=GQ\) has the sign of \(G\) on the positive interval.

**3. Upper endpoint.** Set \(\lambda=U_h\in[c,b]\). Choose \(G(t)=(t-c)^2(t-b)\). For \(t\in[a,b]\), \(G(t)\le0\), so \(f_\lambda(t)\le P(t)\). Since \(P\) has degree at most two, the two equal-moment measures \(\nu_n\) and \(\nu_+\) have the same integral of \(P\). Since \(f_\lambda\) vanishes after integration against \(\nu_+\), and \(G\) vanishes on its support, we obtain
\[
 \int f_\lambda\,d\nu_n\le\int P\,d\nu_n
 =\int P\,d\nu_+=\int f_\lambda\,d\nu_+=0.
\]
As \(\mathbb E X^h>0\), this proves \(w_{n+h}^2\le U_h\).

**4. Lower endpoint.** Set \(\lambda=L_h\in[a,d]\) and \(G(t)=(t-a)(t-d)^2\). Now \(G(t)\ge0\) throughout \([a,b]\). The same polynomial sign lemma, with largest root \(d\ge\lambda\), gives \(f_\lambda(t)\ge P(t)\). Integrating and comparing the first two moments with \(\nu_-\) gives \(\int f_\lambda\,d\nu_n\ge0\), hence \(w_{n+h}^2\ge L_h\). For \(h=1\), the ratio uses only the fixed first two moments, and both bounds equal \(s\).

**5. Sharpness, uniqueness, and every intermediate value.** For \(h\ge2\), the polynomial quotient is strictly positive at every \(t>0\). Equality in either integrated inequality forces the candidate tilted measure to live on the two roots \(\{c,b\}\) or \(\{a,d\}\), respectively. Its first two moments then determine the masses uniquely. Conversely, either extremal tilted measure \(\nu\) arises at the prescribed index \(n\): set
\[
 d\mu(t)=\frac{t^{-n}\,d\nu(t)}{\int x^{-n}\,d\nu(x)}.
\]
This is a probability measure supported inside \([a,b]\); its Berger moment construction yields the required positive subnormal unilateral weighted shift. (Here *Berger* is the intended name of the moment measure.) The interpolation \(\nu_\tau=(1-\tau)\nu_-+\tau\nu_+\), \(0\le\tau\le1\), preserves the first two moments and varies the positive higher-moment ratio continuously between its two endpoints. Thus every number in \([L_h,U_h]\) is attainable. The variance-maximal case forces the sole endpoint law \((1-p)\delta_a+p\delta_b\).

## Verification

Run `python checks/verify.py` with Python 3, NumPy, and SciPy installed. The standalone test script performs 4,500 exact rational comparisons of the proposed envelopes, together with exact rational positivity checks of the polynomial quotients. It also performs 240 linear-programming feasibility diagnostics over grids of 1,001 support locations. These finite tests do not constitute the infinite-dimensional proof, which is the moment-and-polynomial argument above.

## Relationship to prior work

Stampfli established the qualitative rigidity of subnormal weighted shifts under equality of neighboring weights; Curto, Ech-charyfy, El Azhar, and Zerouali study related propagation phenomena for operator-valued shifts. The present theorem is a **sharp quantitative continuation interval** from two neighboring scalar weights and a positive support bound, at every later index. Neither published qualitative rigidity statement itself provides both endpoint formulas, their uniqueness, and the exact interval of realizable future values. The classical Markov--Krein truncated moment and quadrature framework is relevant; the supplied polynomial sign argument addresses the particular higher-moment *ratio*, for which a generic expectation bound alone is not automatically a ratio bound.

## Limitations

This is restricted to scalar **subnormal** shifts with a strictly positive compact Berger support bound. It is not asserted for merely hyponormal shifts or for noncommuting operator-valued weights. The envelope is sharp separately at every fixed future index; it does not characterize joint feasible tuples of several future weights. The proof does not establish publication priority against every historical truncated-moment or quadrature theorem; that remains an independent literature-review risk. Independent mathematical audit has not been performed.

## References

1. R. Curto, A. Ech-charyfy, H. El Azhar, E. H. Zerouali, *Propagation Phenomena for Operator-Valued Weighted Shifts*, Results in Mathematics **81** (2026), article 16, first published 2025-12-13, DOI: 10.1007/s00025-025-02572-6. Open preprint: arXiv:2604.05370.
2. J. G. Stampfli, *Which Weighted Shifts Are Subnormal*, Pacific Journal of Mathematics **17** (1966), 367--379. https://msp.org/pjm/1966/17-2/pjm-v17-n2-p16-p.pdf.
3. R. E. Curto and L. A. Fialkow, *Recursively generated weighted shifts and the subnormal completion problem II*, Integral Equations and Operator Theory **18** (1994), 369--426, DOI: 10.1007/BF01200183 (classical completion context; complete text not checked).
4. S. Karlin and W. J. Studden, *Tchebycheff Systems: With Applications in Analysis and Statistics*, Interscience (1966), classical truncated-moment and quadrature background (full text not checked).
