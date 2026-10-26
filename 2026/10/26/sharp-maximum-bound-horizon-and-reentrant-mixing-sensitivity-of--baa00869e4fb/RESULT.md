# Sharp maximum-bound horizon and reentrant mixing sensitivity of unstabilized Allen–Cahn ETD1

## Finding
For every integer \(n\ge2\) and mixing rate \(\gamma>0\), the conventional **unstabilized** exponential-Euler time-step \(\Phi_h\) for the complete-graph Allen–Cahn system maps the cube \([-1,1]^n\) into itself if and only if \(0<h\le h_*(n,\gamma)\). The **unique** threshold lies strictly between \(0\) and \(1/2\) and satisfies
\[
2\left[h_*+\frac{n-1}{\gamma}(1-e^{-\gamma h_*})\right]
=1+(n-1)e^{-\gamma h_*}.
\]
For fixed \(n\), \(h_*(n,\gamma)\) tends to \(1/2\) as \(\gamma\) tends to either zero or infinity, and has **exactly one** global minimum at an intermediate positive mixing rate. There is therefore a sharp, nonmonotone effect of diffusion on the maximum-bound-preserving step budget. The result also gives an exact extremal overshoot beyond the threshold and its quadratic onset.

## Assumptions and scope
Let \(n\ge2\), \(\gamma>0\), \(h>0\), \(\Pi=n^{-1}\mathbf1\mathbf1^{\mathsf T}\), and \(Q=\gamma(\Pi-I_n)\). On \(\mathbb R^n\) consider
\[
\dot u=Qu+f(u),\qquad f(u)_j=u_j-u_j^3.
\]
The exact dynamics preserve \([-1,1]^n\), because at an upper boundary component the diffusion term is \(\gamma(\bar u-1)\le0\) and the reaction vanishes; the analogous lower-boundary inequality also holds.

The **unstabilized** exponential Euler map considered here is
\[
\Phi_h(u)=e^{hQ}u+\left(\int_0^h e^{sQ}\,ds\right)f(u).
\]
It is **not** the linearly stabilized ETD1 method, which changes both the generator and reaction splitting. All assertions concern exact arithmetic and one time step; cube invariance then extends inductively to arbitrarily many steps.

Set \(a=n-1\), \(r=e^{-\gamma h}\), and
\[
\begin{aligned}
p_d&=\frac{1+ar}{n}, & p_o&=\frac{1-r}{n},\\
k_d&=\frac{h+a(1-r)/\gamma}{n}, & k_o&=\frac{h-(1-r)/\gamma}{n}.
\end{aligned}
\]
The suffixes \(d\) and \(o\) denote diagonal and off-diagonal coefficients of the exponential and integrated exponential, respectively. All four are strictly positive for \(h>0\).

## Proof
**1. Exact reduction to scalar coefficient tests.** Since \(\Pi^2=\Pi\),
\[
e^{sQ}=\Pi+e^{-\gamma s}(I_n-\Pi).
\]
Thus each output component is the sum, over input components, of scalar functions \(g_{p,k}(v)=pv+k(v-v^3)\), with one diagonal pair and \(n-1\) off-diagonal pairs. When \(p,k>0\), \(g_{p,k}\) is odd and its global maximum on \([-1,1]\) is
\[
M(p,k)=\begin{cases}
p,&2k\le p,\\
\displaystyle \frac{2(p+k)^{3/2}}{3\sqrt{3k}},&2k>p.
\end{cases}
\]
Indeed, the derivative is \(p+k-3kv^2\). If \(2k\le p\), it is nonnegative on \([0,1]\); otherwise the unique positive interior maximizer is \(v=\sqrt{(p+k)/(3k)}\). It follows by coordinatewise maximization and oddness that
\[
\max_{u\in[-1,1]^n}\|\Phi_h(u)\|_\infty
=M(p_d,k_d)+aM(p_o,k_o).
\]
Because \(p_d+ap_o=1\) and \(M(p,k)\ge p\), equality with one is equivalent to **both** \(2k_d\le p_d\) and \(2k_o\le p_o\). Any violated inequality gives an explicit input vector whose corresponding output exceeds one; thus these conditions are necessary as well as sufficient.

**2. The unique sharp threshold.** The off-diagonal semigroup coefficient \(p_o(s)=(1-e^{-\gamma s})/n\) is strictly increasing. Hence for \(0<h\le1/2\),
\[
k_o(h)=\int_0^hp_o(s)\,ds<hp_o(h)\le\frac12p_o(h).
\]
The diagonal semigroup coefficient \(p_d(s)=(1+ae^{-\gamma s})/n\) is strictly decreasing. Consequently \(2k_d(h)/p_d(h)\) strictly increases from zero as \(h\) increases. At \(h=1/2\), \(k_d(h)>hp_d(h)=p_d(h)/2\). There is exactly one crossing in \((0,1/2)\), and inserting the coefficient formulas yields the defining equation in the Finding section. For \(h>1/2\), a constant initial vector reduces the method to the scalar Euler map \(v\mapsto v+h(v-v^3)\), whose maximum on \([-1,1]\) exceeds one since its slope at \(v=1\) is \(1-2h<0\). Therefore no later preservation window exists: the iff holds for **all** \(h>0\).

**3. Exact worst-case overshoot and quadratic onset.** For \(h_*<h\le1/2\), the off-diagonal pair still satisfies \(2k_o<p_o\), so the exact maximal positive overshoot is
\[
D(h):=\max_{u\in[-1,1]^n}\|\Phi_h(u)\|_\infty-1
=\frac{2(p_d+k_d)^{3/2}}{3\sqrt{3k_d}}-p_d>0.
\]
An attaining vector has one component \(v_* =\sqrt{(p_d+k_d)/(3k_d)}\) and all other components equal to one. Let \(h_*=h_*(n,\gamma)\), and write \(p_*=p_d(h_*)\), \(k_*=k_d(h_*)=p_*/2\). With \(\delta=2k_d-p_d\), expansion of the displayed exact maximum gives \(D=\delta^2/(6p_*)+O(\delta^3)\), hence
\[
D(h)=\frac{[2p_*-p_d'(h_*)]^2}{12k_*}(h-h_*)^2+o((h-h_*)^2).
\]
The coefficient is strictly positive because \(p_d>0\) and \(p_d'<0\).

**4. Exactly one intermediate-mixing minimum.** Parametrize the threshold by \(y=\gamma h_*\) and \(a=n-1\):
\[
\gamma(y)=\frac{2[y+a(1-e^{-y})]}{1+ae^{-y}},\qquad
h(y)=\frac{y(1+ae^{-y})}{2[y+a(1-e^{-y})]},\quad y>0.
\]
The numerator of \(\gamma(y)\) increases and its positive denominator decreases, so \(\gamma(y)\) increases continuously from zero to infinity. Direct differentiation shows that the sign of \(h'(y)\) is the sign of
\[
H_a(y)=e^y-(1+y+y^2)+a(1-y-e^{-y}).
\]
Here \(H_a(0)=H_a'(0)=0\), \(H_a''(0)=-(a+1)<0\), and \(H_a'''(y)=e^y+ae^{-y}>0\) for \(y\ge0\). Thus \(H_a''\) crosses zero exactly once, followed by one strictly positive zero each of \(H_a'\) and \(H_a\). Hence \(h(y)\) decreases and then increases, with a **unique** minimizer \(y_n>0\) determined by \(H_{n-1}(y_n)=0\). For \(n=2\), this gives \(y_2=2.3046029877\ldots\), \(\gamma_{\mathrm{opt}}=5.8279854435\ldots\), and \(h_{\min}=0.3954373274\ldots\).

**5. Limiting regimes.** The implicit threshold equation and elementary expansions yield, for fixed \(n\),
\[
h_*(n,\gamma)=\tfrac12-\frac{n-1}{8n}\gamma+O_n(\gamma^2)\quad(\gamma\downarrow0),
\]
\[
h_*(n,\gamma)=\tfrac12-\frac{n-1}{\gamma}+O_n(e^{-\gamma/4})\quad(\gamma\to\infty).
\]
For fixed \(\gamma>0\), dividing the threshold equation by \(n-1\) and letting \(n\to\infty\) gives
\[
\lim_{n\to\infty}h_*(n,\gamma)=\frac{\log(1+\gamma/2)}{\gamma}.
\]
Uniqueness and monotonicity of the scalar threshold equation justify these limits.

## Verification
The accompanying standalone standard-library program `verify_etd1_complete_graph.py` can be run with `python3 verify_etd1_complete_graph.py`; the expected final line is `VERIFICATION_OK 32817`. It checks the matrix coefficients and row sums, sharp extrema against explicit witnesses and sampled inputs, root equations, strict off-diagonal inequalities, the unique mixing minimum across selected dimensions, and several asymptotic diagnostics. Its 32,817 finite checks are reproducibility aids **not** proofs of the stated universal results; the proofs appear above.

For example, with \(n=2\), \(\gamma=6\), \(h=0.45<1/2\) and initial state approximately \((0.9596213,1)\), the unstabilized step exceeds the upper bound by approximately \(0.0014409\). This is a one-step overshoot of a trajectory whose exact flow remains inside the cube.

## Relationship to prior work
Du, Ju, Li and Qiao's 2019 nonlocal Allen–Cahn paper proves the discrete maximum principle for **stabilized** ETD1 and ETDRK2, with stabilization parameter at least two; its model and explicit exponential methods motivate studying the complementary unstabilized splitting. Their unconditional results neither assert nor imply an unrestricted time-step maximum principle for the unstabilized map. Du and Zhu's earlier works study ETD stability and Allen–Cahn applications; the precise complete-graph sharp threshold, the coupled dimension–mixing phase diagram and the overshoot coefficient were not located in the inspected accessible source material. The general 2020/2021 maximum-bound framework establishes sufficient conditions for stabilized ETD methods; it does not give this unstabilized optimal threshold. These distinctions do not constitute proof of publication priority.

## Limitations
The theorem concerns exactly the complete-graph coupling, cubic reaction, unshifted generator, exact exponential convolution, and cube preservation for **every** admissible initial vector. It does not cover arbitrary weighted graphs, other nonlinearities, nonexact exponential approximations, energy monotonicity, or stabilized ETD methods. The sharp maximum-norm expression is an operator-level worst-case bound, not a typical trajectory error. A closely related 2005 paper was not fully obtainable and specialized unindexed literature remains an originality risk. Independent scientific evaluation has not been performed.

## References
1. Q. Du, L. Ju, X. Li, Z. Qiao, *Maximum principle preserving exponential time differencing schemes for the nonlocal Allen–Cahn equation*, SIAM J. Numer. Anal. **57** (2019), 875–898. First preprint 2019-02-13, https://arxiv.org/abs/1902.04998, DOI:10.1137/18M118236X.
2. Q. Du, W.-X. Zhu, *Analysis and applications of the exponential time differencing schemes and their contour integration modifications*, BIT Numer. Math. **45** (2005), 307–328, DOI:10.1007/s10543-005-7141-8.
3. *Maximum bound principles for a class of semilinear parabolic equations and exponential time differencing schemes*, https://arxiv.org/abs/2005.11465 (2020 preprint).
