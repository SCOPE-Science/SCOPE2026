# A sharp Lambert-\(W\) law for epidemic overshoot with power-law susceptible incidence

## Finding
Consider closed susceptible–infected–removed (SIR) epidemics with incidence \(\beta S^pI\), with real exponent \(p\ge2\). In the vanishing-initial-infection limit, let \(M(p)\) be the supremum, over every initially supercritical transmission-to-recovery ratio, of the fraction infected **after the peak of infectious prevalence**. Then \(M\) is strictly decreasing and
\[
M(2)=\tfrac14,\qquad
pM(p)=W\!\left(\frac{p-1}{e}\right)+o(1)
=\log p-\log\log p-1+o(1)
\quad(p\to\infty),
\]
where \(W\) is the positive real Lambert function, characterized by \(W(z)e^{W(z)}=z\). More exactly, for each finite \(p\ge2\),
\[
M(p)=\max_{0<s<1}\left\{
\left[\frac{(p-1)(1-s)}{s^{1-p}-1}\right]^{1/p}-s
\right\}.
\]
Thus the worst post-peak burden has a precise logarithmic-over-linear high-exponent decay, with a nontrivial \(-\log\log p-1\) correction.

## Assumptions and scope
The deterministic homogeneous population fractions satisfy
\[
\dot S=-\beta S^pI,\qquad
\dot I=\beta S^pI-\gamma I,\qquad
\dot R=\gamma I,
\]
with \(\beta,\gamma>0\), real \(p\ge2\), and \(S+I+R=1\). Initial fractions are \(S(0)=1-\eta\), \(I(0)=\eta\), \(R(0)=0\), and \(\eta\downarrow0\). Write \(q=\gamma/\beta\); the maximization domain is \(0<q<1\). For each such \(q\), the epidemic has one interior prevalence maximum for sufficiently small positive \(\eta\). Denoting its time by \(t_*\) and the limiting susceptible fraction by \(S_\infty\), define
\[
O_p(q)=\lim_{\eta\downarrow0}\bigl(S(t_*)-S_\infty\bigr),\qquad
M(p)=\sup_{0<q<1}O_p(q).
\]
The result concerns limiting outbreaks initiated by arbitrarily small positive seeds, **not** arbitrary macroscopic initial infections, heterogeneous contact structures, vaccination, stochastic processes, or incidence nonlinear in \(I\).

## Proof
**1. Exact final-size and peak identities.** Along each positive orbit, division of the first two equations yields
\[
\frac{dI}{dS}=-1+qS^{-p}.
\]
Consequently \(I+S-q\int_1^S u^{-p}\,du\) is constant. Since \(R\) is increasing and bounded and the vector field is bounded on the population simplex, \(I(t)\to0\). For fixed \(0<q<1\), taking \(\eta\downarrow0\) gives the nontrivial final-size equation
\[
1-s=qH_p(s),\qquad H_p(s)=\int_s^1u^{-p}\,du
=\frac{s^{1-p}-1}{p-1}.
\]
For clarity, this is the nontrivial branch: \(G(s)=1-s-qH_p(s)\) is strictly concave, has \(G(1)=0\), is positive immediately to the left of \(1\), and tends to \(-\infty\) as \(s\downarrow0\); hence it has exactly one additional root \(s\in(0,1)\). The nontrivial root is selected by every sufficiently small positive initial infection. Also \(\dot I=0\) at the unique prevalence peak, where \(S=q^{1/p}\).

For any \(s\in(0,1)\), the equation defines \(q=(1-s)/H_p(s)\in(0,1)\). Because \(H_p(s)<(1-s)s^{-p}\), its peak susceptibility \(h_p(s)=q^{1/p}\) satisfies \(s<h_p(s)<1\). Hence every \(s\in(0,1)\) is realized, and the displayed formula for \(M(p)\) follows. Its objective is continuous, positive on the interior, and tends to zero at both endpoints (for \(p>1\), use \(q\sim(p-1)s^{p-1}\) near zero). Thus a maximizer exists in the interior.

**2. Strict dependence on incidence exponent.** If \(U_s\) is uniform on \([s,1]\), then
\[
h_p(s)=\left(\mathbb E[U_s^{-p}]\right)^{-1/p}.
\]
For fixed \(0<s<1\), the \(L^p\)-norm of the nonconstant positive random variable \(1/U_s\) increases *strictly* with \(p\); equivalently \(h_p(s)\) decreases strictly. For \(p_2>p_1\ge2\), evaluate at an interior maximizer \(s_2\) of the \(p_2\) objective:
\[
M(p_2)=h_{p_2}(s_2)-s_2
<h_{p_1}(s_2)-s_2\le M(p_1).
\]
At \(p=2\), \(H_2(s)=(1-s)/s\), so \(h_2(s)=\sqrt{s}\) and \(\max_{0<s<1}(\sqrt{s}-s)=1/4\), attained at \(s=1/4\).

**3. Sharp large-exponent asymptotics.** Put \(L=\log(p-1)\), \(y=1-s\), and
\[
A_p(s)=\log\frac{(p-1)(1-s)}{s(1-s^{p-1})}.
\]
An exact rearrangement yields
\[
h_p(s)-s=s\left(e^{A_p(s)/p}-1\right).
\]
We first locate the maximum. For \(p\ge2\), the inequality \(1-s^{p-1}\ge1-s\) gives \(h_p(s)\le p^{1/p}s^{1-1/p}\). For any fixed \(\varepsilon\in(0,1/2)\), splitting the right-hand side into two exponential increments and using \(e^v-1\le ve^v\) gives uniformly on \(s\le1-\varepsilon\),
\[
p(h_p(s)-s)\le(1-\varepsilon)^{1-1/p}\bigl(\log p+O((\log p)^2/p)\bigr)+O(1).
\]
(The uniform \(O(1)\) uses \(\sup_{0<s<1}s^{1-1/p}(-\log s)\le1/[e(1-1/p)]\).)

For \(0<y\le p^{-1/2}\), set \(t=(p-1)y\). Since \(s^{p-1}\le e^{-t}\) and \(t/(1-e^{-t})\le1+t\),
\[
0<A_p(s)\le\log\frac{1+t}{s}\le\tfrac12\log p+O(1).
\]
It follows that \(p(h_p(s)-s)\le(\tfrac12+o(1))\log p\) uniformly there.

On the remaining band \(p^{-1/2}\le y\le\varepsilon\), one has \(s^{p-1}\le e^{-\sqrt p(1-o(1))}\), and \(A_p(s)=O(\log p)\) uniformly. Taylor's theorem therefore gives the **uniform** expansion
\[
p(h_p(1-y)-(1-y))=F_L(y)+o(1),\quad
F_L(y)=(1-y)\left[L+\log\frac{y}{1-y}\right].
\]
The function \(F_L\) is strictly concave because
\[
F_L''(y)=-\frac1y-\frac1{1-y}-\frac1{y^2}<0.
\]
Writing \(z=(1-y)/y\), its sole critical point is defined by
\[
z+1=L-\log z,\qquad
z=W\!\left(\frac{p-1}{e}\right).
\]
At this point \(y=(1+z)^{-1}\) and \(F_L(y)=z\). For sufficiently large \(p\), this critical point lies inside the band. Its value is \(\log p-\log\log p-1+o(1)\), which exceeds both preceding upper bounds for sufficiently large \(p\). Thus the true maximizing \(s\) lies in the band and the uniform approximation yields
\[
pM(p)=W\!\left(\frac{p-1}{e}\right)+o(1).
\]
The standard identity \(W(x)+\log W(x)=\log x\) proves the stated two-term logarithmic expansion. This completes the proof.

## Verification
Run `python3 verify.py` using the accompanying standalone standard-library script. On the packaged script, the finite cross-checks pass: the quadratic case has \(s_*=1/4\) and \(M(2)=1/4\); the cubic maximum agrees with the previously published value near \(0.2174\); and tested exponents exhibit strict decreasing maximal overshoot. Directly substituting the computed \(h_p(s)\) into the final-size relation validates the parameterization on a grid. At four increasing large exponents the discrepancy between \(pM(p)\) and \(W((p-1)/e)\) shrinks. These samples **do not prove** strict monotonicity for every real \(p\) or the limit as \(p\to\infty\); the analytical arguments above do.

## Relationship to prior work
Nguyen, *Upper Bounds on Overshoot in SIR Models with Nonlinear Incidence* (first public preprint 2023-03-03, arXiv:2303.01653; journal version 2024), develops the general conserved-quantity/final-size strategy and explicitly calculates the cubic \(p=3\) case. Its general framework supplies the starting identity here, but neither its worked examples nor its general algorithm establishes the **strict exponent ordering** or the **sharp Lambert-\(W\) large-exponent law**. Nguyen, Freedman, Ozbay and Levin (arXiv:2303.01650) analyze the bilinear \(p=1\) case. The novel claim is solely the across-exponent theorem and sharp asymptotic, not rediscovery of the general final-size method or a previously published fixed-exponent maximum.

## Limitations
This is a theorem about one homogeneous deterministic SIR family and the vanishing-seed limit. Increasing an incidence exponent while independently recalibrating the transmission parameter need not yield pointwise smaller overshoot at a **fixed** reproduction ratio: the ordering proved here concerns the supremum over all supercritical ratios. No data-fitting or applied forecasting claim is made. The relation \(pM(p)=W((p-1)/e)+o(1)\) is asymptotic rather than exact at finite \(p\); no rigorous numerical error bound at a chosen finite \(p\) is asserted. Literature searches cannot establish uniqueness against all unindexed publications.

## References
1. M. M. Nguyen, *Upper Bounds on Overshoot in SIR Models with Nonlinear Incidence*, arXiv:2303.01653 (first submitted 2023-03-03); revised journal article, *npj Complexity* **1**, 11 (2024), DOI:10.1038/s44260-024-00010-2.
2. M. M. Nguyen, A. S. Freedman, S. A. Ozbay, S. A. Levin, *Fundamental Bound on Epidemic Overshoot in the SIR Model*, arXiv:2303.01650 (first submitted 2023-03-03); *Journal of the Royal Society Interface* **20**, 20230322 (2023).
