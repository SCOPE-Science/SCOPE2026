# Entropy-optimal resetting with a fixed opposite part on complete bipartite graphs

## Finding
Fix an integer \(n\ge2\). On \(K_{m,n}\), let a discrete-time walk reset to a distinguished vertex \(o\) in the \(m\)-vertex part with probability \(r\), and otherwise walk to a uniformly random neighbor. Write \(H_{m,n}(r)\) for the stationary entropy rate of the **observed vertex process**, with natural logarithms. For every selection of global maximizers \(r_{m,n}\) over \(0\le r\le1\), as \(m\to\infty\),
\[
r_{m,n}\sim (m^3 n)^{-1/4},\qquad
\max_r H_{m,n}(r)-\tfrac12\log(mn)\sim (m^3n)^{-1/4}.
\]
In particular the root-at-a-leaf star exponent persists when the opposite part has any fixed size greater than one, and the leading coefficient for both quantities is \(n^{-1/4}\) on the \(m^{-3/4}\) scale.

## Assumptions and scope
The graph is simple and undirected. The reset and hop probabilities are added when both lead to the same vertex. The stationary entropy rate is the stationary mean of the transition-row entropies, including the continuous endpoint values. No finite-size optimizer uniqueness is asserted.

## Proof
Put \(q=1-r\) and \(h(r)=-r\log r-q\log q\), with \(0\log0=0\). The class transitions are \(A\to B\) with probability \(q\) and \(B\to A\) with probability one. Thus the stationary class weights are \(1/(2-r)\) and \(q/(2-r)\). Rows from \(A\) have entropy \(h(r)+q\log n\), and rows from \(B\) have entropy \(g_m(r)=-a\log a-(m-1)b\log b\), with \(a=r+q/m\) and \(b=q/m\). This gives the exact formula used below,
\[
H_{m,n}(r)=\frac{h(r)+q\log n+qg_m(r)}{2-r}.
\]
At \(r=0\) this equals \(\tfrac12\log(mn)\), and at \(r=1\) it is zero. Continuity gives existence of a maximum.

Revealing the reset indicator for a row from \(B\) yields entropy \(h(r)+q\log m\). Its conditional entropy given the destination is \(d(r)=a h(b/a)\), since only arrival at \(o\) leaves the indicator ambiguous. For \(b>0\), \(0\le d(r)\le b\log(ea/b)\), by \(-(1-x)\log(1-x)\le x\); the bound extends by continuity at \(r=1\). Hence
\[
H_{m,n}(r)\le U(r)=h(r)+\frac{q\log n+q^2\log m}{2-r},
\qquad U(r)-H_{m,n}(r)=\frac{q}{2-r}d(r).
\]
Write \(s=(m^3n)^{-1/4}\). For \(t\) in any bounded interval of nonnegative reals, \(h(ts)=ts[1-\log(ts)]+O(s^2)\), and the two rational coefficients in \(U\) have first derivatives \(-1/4\) and \(-3/4\) at zero. The remainder after their linear terms is \(O(s^2\log m)\), as \(n\) is fixed. Therefore, uniformly on such intervals,
\[
\frac{U(ts)-\tfrac12\log(mn)}s\longrightarrow F(t)=t(1-\log t),\qquad F(0)=0.
\]
The gap \(U(ts)-H_{m,n}(ts)\) is \(O((\log m)/m)=o(s)\) there. In particular the scaled gain at \(s\) tends to 1.

To exclude global maximizers outside the local scale, differentiate the envelope:
\[
U'(r)=\log\frac{1-r}{r}-\frac{\log n+(1-r)(3-r)\log m}{(2-r)^2},\quad
U''(r)=-\frac1{r(1-r)}+\frac{2\log(m/n)}{(2-r)^3}.
\]
For large \(m\) the second derivative is negative on \((0,m^{-1/2})\), where the first negative term has magnitude at least \(\sqrt m\). On \([m^{-1/2},1/2]\) the first term of \(U'\) is at most \(\tfrac12\log m\), while the coefficient of the subtracted \(\log m\) is \(1-1/(2-r)^2\ge5/9\). For \(r\ge1/2\), \(U'<0\) in the interior. Thus \(U\) increases up to a unique peak and then decreases (its derivative tends to \(+\infty\) at zero).

Fix \(0<\varepsilon<1\). Since \(F(1\pm\varepsilon)<F(1)=1\), for large \(m\) the two envelope values at \((1\pm\varepsilon)s\) are strictly less than \(H_{m,n}(s)\le U(s)\). Unimodality then bounds \(U\) and hence \(H_{m,n}\) outside \([(1-\varepsilon)s,(1+\varepsilon)s]\) by the corresponding boundary values. All maximizers thus satisfy \(r_{m,n}/s\to1\). Uniform convergence on this bounded scale gives the claimed limiting scaled gain.

## Relationship to prior work and limitations
The star record [1] gives the exact leaf-root \(n=1\) optimizer and gain, both with constant one. The dense bipartite record [2] gives the same exact transition-entropy formula and the sharp proportional-part laws; its hypotheses exclude a fixed opposite part. Neither the star constant nor the proportional limit at a fixed positive ratio determines the fixed-\(n>1\) coefficient or global optimization here. The two records are cited for overlap, not as evidence of historical priority. The stationary and entropy frameworks are related to [3,4]. No intermediate regime with both part sizes growing and \(n/m\to0\) is asserted.

The companion `check_entropy.py` gives finite diagnostics, including for fixed \(n>1\), and retains tests for the star and proportional regimes as context. The proof above, not that numerical testing, establishes the asymptotic claim.

1. *Distinct optimal reset exponents at the hub and leaves of a star*, [record](https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-distinct-optimal-reset-exponents-at-the-hub-and-leaves-of-a-star--6fb1fef030da), Finding and Proof §§1, 5.
2. *Golden-ratio entropy-optimal resetting on dense complete bipartite graphs*, [record](https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-golden-ratio-entropy-optimal-resetting-on-dense-complete-biparti--fa1f991cbb3e), Finding and Proof §§1, 4–5.
3. Y. Wang and H. Chen, *Entropy rate of random walks on complex networks under stochastic resetting*, [arXiv:2208.05665](https://arxiv.org/abs/2208.05665).
4. A. P. Riascos, D. Boyer, P. Herringer and J. L. Mateos, *Random walks on networks with stochastic resetting*, [arXiv:1910.13568](https://arxiv.org/abs/1910.13568).
