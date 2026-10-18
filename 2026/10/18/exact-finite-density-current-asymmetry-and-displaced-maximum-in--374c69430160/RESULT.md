# Exact finite-density current asymmetry and displaced maximum in deformed exclusion

## Finding

For the periodic deformed exclusion process defined below, the stationary mean net bond current is exactly

\[
J_n=(1-q)[K]_t^2\frac{[z^{n-1}]\left(F(z)^L/(1+z)^2\right)}{[z^n]F(z)^L},\qquad
F(z)=\prod_{j=0}^{K-1}(1+t^jz).
\]

For \(1\le n\le N-1\), with \(N=KL\), its particle--hole current difference obeys the **strict, parameter-uniform sign law**

\[
\operatorname{sgn}(J_n-J_{N-n})=\operatorname{sgn}\bigl((t-1)(2n-N)\bigr).
\]

For \(0\le q<1\), equality occurs exactly at \(t=1\) or \(2n=N\). Thus equality of the canonical stationary weights under particle--hole complement does not imply equality of the mean currents at complementary densities. The corresponding product-state flux has the unique maximizing density

\[
\rho_*(t)=\sum_{j=0}^{K-1}\frac{t^j}{1+t^j},
\]

strictly below \(K/2\) for \(t<1\) and strictly above it for \(t>1\). This is an exact nonequilibrium transport classification rather than an estimate of a particular finite-size graph.

## Assumptions and scope

Fix integer ring length \(L\ge3\) and occupation capacity \(K\ge2\). Put \(N=KL\). Each site has an occupation in \(\{0,1,\ldots,K\}\), and the particle count \(n\) is conserved. At a nearest-neighbor bond with occupations \((a,b)\), clockwise and counterclockwise hops have rates respectively

\[
[a]_t([K]_t-[b]_t),\qquad
q[b]_t([K]_t-[a]_t),\qquad
[a]_t=\sum_{j=0}^{a-1}t^j,
\]

for \(t>0\) and \(0\le q<1\). Let \(J_n\) be the stationary mean clockwise rate minus the stationary mean counterclockwise rate across a specified bond, with \(J_0=J_N=0\). The canonical stationary law is the product weight conditioned on total occupancy \(n\), as established by Ayyer and Misra. Here \([z^m]P(z)\) means the coefficient of degree \(m\), interpreted as zero when \(m<0\). The grand-canonical formulas concern a translation-invariant independent-site product stationary law with positive fugacity \(z\), and are not an assertion of dynamical independence.

## Proof

**Step 1: canonical weight and the two local generating functions.** The known canonical stationary weight can be written, up to a factor depending only on \(n\), as \(\prod_i w_{\eta_i}\), where

\[
w_a=t^{a(a-1)/2}\begin{bmatrix}K\\a\end{bmatrix}_t,
\qquad
F(z)=\sum_{a=0}^K w_az^a=\prod_{j=0}^{K-1}(1+t^jz).
\]

The last identity is the finite \(t\)-binomial theorem. The source's exponent \((a-1)(a-2)/2\) differs by \(1-a\); the total factor is \(t^{L-n}\), constant within the canonical sector. The Gaussian-binomial identity \([a]_t\begin{bmatrix}K\\a\end{bmatrix}_t=[K]_t\begin{bmatrix}K-1\\a-1\end{bmatrix}_t\) yields

\[
G_+(z):=\sum_a[a]_tw_az^a=[K]_t\frac{zF(z)}{1+z},
\qquad
G_-(z):=\sum_a([K]_t-[a]_t)w_az^a=[K]_t\frac{F(z)}{1+z}.
\]

These are polynomials: the common denominator cancels the \(j=0\) factor of \(F\). Under the canonical product measure, the joint distribution at two sites is invariant under their exchange. Hence the expected counterclockwise rate is \(q\) times the expected clockwise factor, even though the instantaneous dynamics is asymmetric. Conditioning on total occupancy gives

\[
J_n=\frac{1-q}{Z_n}[z^n]G_+(z)G_-(z)F(z)^{L-2}
=(1-q)[K]_t^2\frac{[z^{n-1}]\left(F(z)^L/(1+z)^2\right)}{Z_n},\quad Z_n=[z^n]F(z)^L>0.
\]

**Step 2: convert complementary-density current to a second coefficient.** Expand the product \(F(z)^L\) into \(N\) labeled Bernoulli levels: at each physical site, level \(j\in\{0,\ldots,K-1\}\) has weight \(t^j\) if occupied and weight one otherwise. Condition on precisely \(n\) occupied levels. Summing levels within a physical site gives the canonical weights \(w_a\); the levels are only an auxiliary representation of the stationary law.

The first coefficient formula counts the event that level zero at a specified site is occupied and level zero at its neighbor is vacant, multiplied by \((1-q)[K]_t^2\). Complementing all levels and simultaneously replacing each level label \(j\) by \(K-1-j\) maps the \(n\)-sector to the \((N-n)\)-sector and preserves normalized conditioned weights: the ratio of transformed to original unnormalized weights is a constant depending on \(n\) alone. Exchangeability of the two physical sites therefore gives

\[
J_{N-n}=\frac{(1-q)[K]_t^2}{Z_n}
\,w\,[z^{n-1}]\left(\frac{F(z)^L}{(1+wz)^2}\right),
\qquad w=t^{K-1}.
\]

**Step 3: reciprocal-root strict unimodality determines the sign.** Put

\[
H(z)=\frac{F(z)^L}{(1+z)^2(1+wz)^2}=\sum_{m=0}^{N-4}h_mz^m,
\qquad r=\sqrt w,
\qquad H(y/r)=\sum_{m=0}^{d}g_my^m,\quad d=N-4.
\]

The polynomial \(H\) has factors \((1+t^jz)\) of multiplicity \(L-2\) at \(j=0,K-1\) and multiplicity \(L\) at all intermediate \(j\). Because \(L\ge3\), all multiplicities are positive. After rescaling by \(r\), its \(d\) strictly positive factor parameters occur in reciprocal pairs, with no net prefactor. It follows that \(g_m=g_{d-m}>0\). Because all the roots are strictly negative real numbers, Newton's elementary-symmetric inequalities make the sequence \((g_m)_{m=0}^{d}\) strictly log-concave (there are at least two factors). The symmetry and strict log-concavity imply strict growth toward the center and strict decrease afterward, allowing only the two equal middle entries when \(d\) is odd. Thus

\[
\operatorname{sgn}(g_{n-1}-g_{n-3})
=\operatorname{sgn}(N-2n)
\]

for \(1\le n\le N-1\), using zero for indices outside \(\{0,\ldots,d\}\). To see this explicitly, the indices \(n-1\) and \(n-3\) have midpoint \(n-2\), while the coefficient symmetry center is \(d/2=N/2-2\); symmetric strict unimodality compares their distance from that center.

Combining Step 1 and Step 2, factoring the difference of rational functions, and using \(h_m=r^m g_m\) gives

\[
J_n-J_{N-n}=
\frac{(1-q)[K]_t^2(1-w)}{Z_n}\bigl(h_{n-1}-wh_{n-3}\bigr)
=\frac{(1-q)[K]_t^2(1-w)r^{n-1}}{Z_n}(g_{n-1}-g_{n-3}).
\]

Since \(\operatorname{sgn}(1-w)=-\operatorname{sgn}(t-1)\) for \(K\ge2\), this is exactly the claimed sign law and equality classification. The cases \(n=1,N-1\) are included by the coefficient convention.

**Step 4: unique peak of the grand-canonical current.** At fugacity \(z>0\), the \(K\) auxiliary levels at each site are independent Bernoulli variables with occupation probabilities \(zt^j/(1+zt^j)\). Consequently the mean site occupation and stationary net current are

\[
\rho(z)=z\frac{F'(z)}{F(z)}=\sum_{j=0}^{K-1}\frac{zt^j}{1+zt^j},\qquad
J(z)=(1-q)[K]_t^2\frac{z}{(1+z)^2}.
\]

The derivative \(\rho'(z)>0\), so maximizing current in density is equivalent to maximizing \(z/(1+z)^2\), which is uniquely maximal at \(z=1\), of value \((1-q)[K]_t^2/4\). Every term in \(\rho_*(t)\) with \(j>0\) is strictly increasing in \(t\); thus \(\rho_*(t)\) is strictly increasing since \(K\ge2\), equals \(K/2\) exactly at \(t=1\), and has the endpoint limits \(1/2\) and \(K-1/2\).

## Verification

The standalone, standard-library script `check_transport.py` checks 852 exact rational identities, independently enumerates canonical configurations and verifies stationary master equations and bond currents, compares complementary-density signs, and checks grand-canonical local moment identities. It covers \((K,L)=(2,3),(2,4),(3,3),(3,4),(4,3)\), four positive rational deformation parameters and two asymmetry parameters. For example, at \(K=3\), \(L=4\), \(t=2\), and \(q=0\), it gives \(J_8=24304/1783>J_4=13720/1783\); the optimal product-state density is \(59/30\). The quantified theorem is proved analytically above; finite experiments are corroboration, not an exhaustive test of all parameters.

## Relationship to prior work

Ayyer and Misra, *An exactly solvable asymmetric K-exclusion process* (arXiv:2310.03343, first available 5 October 2023), establish the precise rates, canonical product weights, partition function, particle--hole **stationary-law** symmetry and polynomial palindromicity, but do not state an explicit canonical current law or the strict transport-asymmetry classification. Section 6 calls nonequilibrium properties a further direction. Their auxiliary two-dimensional process is an established representation, not claimed here as new.

Evans and Waclaw, *Condensation in stochastic mass transport models: beyond the zero-range process* (arXiv:1312.5642), give broad misanthrope factorization conditions. These justify the underlying product-form context but do not directly supply the specific complementary-current strict sign theorem. Ayyer and Misra's later *An exactly solvable asymmetric simple inclusion process* (arXiv:2510.09191, Section 4.2) computes a current in a different inclusion model, mainly at the undeformed value, not this finite \(K\)-exclusion theorem. These distinctions concern implications, not differences in wording.

## Limitations

All assertions here concern stationary mean single-bond particle flux on a periodic finite ring or the independent-site product stationary ensemble; no statement is made about integrated-current fluctuations, current large deviations, open-boundary driving, or hydrodynamic-limit shocks. The two grand-canonical endpoints are limits in deformation strength; the formulas require finite strictly positive \(t\). At \(q=1\) the net current vanishes, so the strict sign law has the stated \(q<1\) hypothesis. A more general theorem on factorized misanthrope currents or real-rooted coefficients may imply parts of this finding; independent priority review has not been conducted.

## References

1. A. Ayyer and S. Misra, *An exactly solvable asymmetric K-exclusion process*, arXiv:2310.03343 (first public version 2023-10-05), https://arxiv.org/abs/2310.03343; see Sections 2, 3, 3.1--3.3, 5 and 6.
2. M. R. Evans and B. Waclaw, *Condensation in stochastic mass transport models: beyond the zero-range process*, arXiv:1312.5642 (2013), https://arxiv.org/abs/1312.5642.
3. A. Ayyer and S. Misra, *An exactly solvable asymmetric simple inclusion process*, arXiv:2510.09191 (2025), https://arxiv.org/abs/2510.09191; Section 4.2.
4. I. Newton, elementary-symmetric coefficient inequalities (classical result), used only for the strictly log-concave coefficient argument.
