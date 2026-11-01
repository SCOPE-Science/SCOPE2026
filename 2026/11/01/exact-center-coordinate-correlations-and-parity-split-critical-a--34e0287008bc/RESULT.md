# Exact center-coordinate correlations and parity-split critical amplitudes in heterochaos baker maps

## Finding
For each integer \(m\ge 2\), consider the critical two-dimensional heterochaos baker map defined below, initialized in planar Lebesgue measure. Write \(Y_n\) for its center coordinate and
\[
C_n=\mathbb E[(Y_0-\tfrac12)(Y_n-\tfrac12)],\qquad n\ge0.
\]
Put \(p_n(r)=2^{-n}\binom n{(n+r)/2}\) when \(0\le r\le n\) and \(n+r\) is even, and put \(p_n(r)=0\) otherwise. Every lag has the exact formula
\[
\boxed{C_n=\frac1{12}\sum_{\substack{0\le r\le n\\r\equiv n\ ({\rm mod}\ 2)}}m^{-r}(r+1)\big[p_n(r)-p_n(r+2)\big].}
\]
Let \(t(z)=(1-\sqrt{1-z^2})/z\), with \(t(0)=0\). Its algebraic generating function is
\[
\boxed{\sum_{n\ge0}C_nz^n=\frac{1+t(z)^2}{12(1-t(z)/m)^2},\quad |z|<1.}
\]
The exact critical decay has *two unequal leading constants*, depending on parity. With \(u=m^{-2}\), set
\[
\kappa_{\rm even}(m)=\frac{\sqrt{2/\pi}}6\frac{1+6u+u^2}{(1-u)^3},\qquad
\kappa_{\rm odd}(m)=\frac{\sqrt{2/\pi}}6\frac{4m^{-1}(1+u)}{(1-u)^3}.
\]
Then, as \(n\to\infty\) within the corresponding parity class,
\[
\boxed{C_n=\kappa_{\rm parity}(m)n^{-3/2}+O_m(n^{-5/2}).}
\]
The constants are distinct for **every** integer \(m\ge2\):
\[
\boxed{\kappa_{\rm even}(m)-\kappa_{\rm odd}(m)=\frac{\sqrt{2/\pi}}6\frac{1-m^{-1}}{(1+m^{-1})^3}>0.}
\]
In particular, the sequence \(n^{3/2}C_n\) has exactly two distinct subsequential limits. Further,
\[
\boxed{\sum_{n\ge0}C_n=\frac1{6(1-m^{-1})^2}},\qquad
\boxed{\lim_{N\to\infty}\frac1N\operatorname{Var}\!\left(\sum_{j=0}^{N-1}(Y_j-\tfrac12)\right)=\frac{3m^2+2m-1}{12(m-1)^2}}.
\]
All \(C_n\) are strictly positive, with \(C_0=1/12\) and \(C_1=1/(12m)\).

## Assumptions and scope
Let \(Q=[0,1)^2\). For each \(1\le i\le m\), define the alpha interval \(I_i=[(i-1)/(2m),i/(2m))\). On \(I_i\times[0,1)\) define
\[
F_m(x,y)=(2mx-(i-1),(y+i-1)/m).
\]
On the beta interval \([1/2,1)\), define
\[
F_m(x,y)=(2x-1,my-\lfloor my\rfloor).
\]
Endpoints and points on the countable forward/backward discontinuity set are irrelevant for Lebesgue statistical assertions; half-open intervals fix a concrete convention. Each rectangle branch is affine. The alpha branch images partition \([0,1)\) vertically with combined inverse-Jacobian weight \(1/2\). The beta branch has \(m\) vertical subbranches with combined inverse-Jacobian weight \(1/2\). Hence two-dimensional normalized Lebesgue measure is invariant. All expectations refer to \((X_0,Y_0)\) with this distribution, not to a fixed deterministic orbit. The central direction is critical because alpha contraction and beta expansion occur with probabilities \(1/2\) each. Primary classification: MSC2020 37A25.

## Proof
**1. Stack description.** Each alpha strip digit has probability \(1/(2m)\); beta has probability \(1/2\). Because the horizontal map consists of full branches, the successive alpha/beta choices are independent fair signs for initial Lebesgue-absolutely-continuous horizontal coordinate. Conditional on an alpha choice, its strip digit is independent uniform on \(\{0,\ldots,m-1\}\). These choices are independent of initial \(Y_0\). On alpha, \(y\mapsto(y+i-1)/m\) prepends an \(m\)-adic digit; on beta, \(y\mapsto my\bmod1\) removes the leading digit. Nonunique radix expansions form a null set.

Let \(S_0=0\), and let \(S_n\) count alpha choices minus beta choices through time \(n\). Define \(M_n=-\min_{0\le j\le n} S_j\) and \(H_n=S_n+M_n\). These are nonnegative integers. After the \(n\) updates, \(H_n\) newly prepended digits remain, and \(M_n\) initial digits have been removed. In an exact base-\(m\) decomposition there is a random newly prepended prefix \(V_n\), independent of \(Y_0\), and a remaining uniform tail \(Z_n\) such that
\[
Y_n=V_n+m^{-H_n}Z_n,\qquad Y_0=U_n+m^{-M_n}Z_n,
\]
where \(U_n\) is made from the removed initial digits and is independent of \(Z_n\). Given the full driving symbols, the covariance contributed by the shared tail is \(m^{-H_n-M_n}/12\), and the initial-coordinate conditional mean is always \(1/2\). Taking expectation gives
\[
C_n=\frac1{12}\mathbb E[m^{-(S_n+2M_n)}]. \tag{1}
\]

**2. Reflection count.** Put \(W_n=S_n+2M_n\). For \(r\ge0\) of the same parity as \(n\), the event \(W_n=r\) splits by \(M_n=h\), with \(0\le h\le r\) and endpoint \(S_n=r-2h\). The reflection principle counts paths from zero with minimum exactly \(-h\) and this endpoint: for each such \(h\), its probability is \(p_n(r)-p_n(r+2)\). Summing over the \(r+1\) permitted minima gives
\[
\mathbb P(W_n=r)=(r+1)[p_n(r)-p_n(r+2)]. \tag{2}
\]
Equations (1)–(2) prove the finite formula, including \(n=0\) and positivity.

**3. Resolvent.** The standard simple-walk binomial resolvent is
\[
\sum_{n\ge0}p_n(r)z^n=\frac{t(z)^r}{\sqrt{1-z^2}},\qquad
 t(z)=\frac{1-\sqrt{1-z^2}}{z}.
\]
After summing (2) and the absolutely convergent geometric derivative \(\sum_{r\ge0}(r+1)v^r=(1-v)^{-2}\), obtain
\[
\sum_{n\ge0}C_nz^n=
\frac{1-t(z)^2}{12\sqrt{1-z^2}(1-t(z)/m)^2}.
\]
The identity \((1-t^2)/\sqrt{1-z^2}=1+t^2\) yields the displayed algebraic generating function.

**4. Exact two-parity asymptotics.** The exact adjacent-binomial ratio is
\[
p_n(r)-p_n(r+2)=\frac{2(r+1)}{n+r+2}p_n(r).
\]
For fixed parity-compatible \(r\), Stirling's formula gives \(p_n(r)=\sqrt{2/(\pi n)}[1+O_r(n^{-1})]\). More quantitatively, for \(0\le r\le\sqrt n\) the relative approximation can be bounded by \(O((r+1)^2/n)\). For \(r>\sqrt n\), the summands are bounded by an exponentially small geometric tail in \(m^{-r}\), uniformly in \(n\). Since \(m\ge2\), summing the polynomially weighted error over \(r\) proves
\[
C_n=\frac{\sqrt{2/\pi}}{6n^{3/2}}
\sum_{\substack{r\ge0\\r\equiv n\ ({\rm mod}\ 2)}}(r+1)^2m^{-r}+O_m(n^{-5/2}). \tag{3}
\]
For even \(r=2j\), the geometric sum is \((1+6u+u^2)/(1-u)^3\). For odd \(r=2j+1\), it is \(4m^{-1}(1+u)/(1-u)^3\). Their difference is also the alternating square-weight sum
\[
\sum_{r\ge0}(-1)^r(r+1)^2m^{-r}
=\frac{1-m^{-1}}{(1+m^{-1})^3}>0.
\]
This proves both distinct amplitude formulas, their strict inequality, and the stated error term.

**5. Integrated covariance.** By (3), \(\sum_{n\ge0}|C_n|<\infty\). Letting real \(z\uparrow1\) in the exact generating function gives \(\sum_{n\ge0}C_n=1/[6(1-m^{-1})^2]\). Stationarity and absolute summability imply
\[
\lim_{N\to\infty}\frac1N\operatorname{Var}\!\left(\sum_{j=0}^{N-1}(Y_j-\tfrac12)\right)
=C_0+2\sum_{n\ge1}C_n=2\sum_{n\ge0}C_n-C_0,
\]
which simplifies to the claimed rational expression.

## Verification
The standalone standard-library checker `CHECK.py` compares three exactly rational, computationally independent finite-lag evaluations: (i) the reflection/binomial formula, (ii) direct action of the annealed Koopman operator on piecewise-affine functions followed by exact integration, and (iii) formal power-series expansion of the algebraic generating function. It passed 24 triple-method cases for integer \(m\in\{2,3,4,5\}\) through indicated finite lags and checks normalization at lags zero and one. Run with `python3 CHECK.py`. These finite checks do **not** replace the all-lag analytical arguments or the asymptotic proof.

## Relationship to prior work
Takahasi (arXiv:2307.08119, first posted July 16, 2023) introduced the relevant critical generalized heterochaos baker setting and established mixing of all orders, with exponential decay in noncritical regimes. Takahasi–Tsujii (arXiv:2408.16618, first posted August 29, 2024) established optimal order \(n^{-3/2}\) polynomial correlation bounds in the mostly neutral center case using a reduced Perron–Frobenius operator and an absorbing-walk comparison. That rate and random-walk technique are **prior work**, not originality claims here. The present exact stationary center-coordinate formulas determine the complete algebraic generating function, the unequal two-parity leading coefficients, and an exact Green–Kubo variance. These finer conclusions are not stated in the inspected source statements and arguments, though the earlier general operator machinery is related and might be used to derive them. Saiki–Takahasi–Yamamoto–Yorke (arXiv:2401.00836) give broader context for heterochaos baker maps. Two related indexed results on neutral periodic-fiber counts and density concern periodic geometry rather than this stationary temporal covariance; they do not imply the formulas above.

## Limitations
The exact formulas concern the planar critical symmetric family with integer \(m\ge2\), the Lebesgue stationary state, and the particular univariate center observable \(y-1/2\). They are not assertions for every Hölder observable, noncritical parameters, or arbitrary invariant states. The \(n^{-3/2}\) *order* of correlation decay is known; no priority is asserted for it. A complete publication-priority search is impossible to guarantee, and related general transfer-operator formulations may implicitly contain specializations of the exact formulas. The independent audit remains unperformed.

## References
1. H. Takahasi, *Exponential mixing for heterochaos baker maps and the Dyck system*, arXiv:2307.08119 (first posted 2023-07-16), https://arxiv.org/abs/2307.08119.
2. H. Takahasi and M. Tsujii, *Polynomial rate of mixing for the heterochaos baker maps with mostly neutral center*, arXiv:2408.16618 (first posted 2024-08-29), https://arxiv.org/abs/2408.16618.
3. Y. Saiki, H. Takahasi, K. Yamamoto and J. A. Yorke, *The dynamics of the heterochaos baker maps*, arXiv:2401.00836, https://arxiv.org/abs/2401.00836.
