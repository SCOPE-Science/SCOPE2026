# A computable global extinction–escape separatrix for a homogeneous quadratic population map

## Finding

For an open parameter chamber of a positive homogeneous quadratic map, the entire strict-positive phase space is divided by one **explicitly evaluable, invariant, codimension-one radial graph**: below it every orbit tends to the origin; above it every coordinate tends to infinity; on it every orbit converges to the unique positive nonzero fixed point. The graph is given by a uniformly and geometrically convergent product with a rigorous error bound. In the equal-parameter case it has a unique minimum at the balanced composition, maxima at the simplex vertices, and an explicit nonzero quadratic curvature at its minimum.

**Theorem.** Fix an integer \(d\ge3\) and parameters \(\theta_1,\ldots,\theta_d>0\). Define
\[
 c=\frac{2d-1}{\sum_{i=1}^d\theta_i^{-1}},\qquad
 q_i=2-\frac{c}{\theta_i}.
\]
Assume \(q_i>0\) for every \(i\). Then automatically \(\sum_i q_i=1\). On \((0,\infty)^d\) consider the map
\[
 H_i(x)=\frac{\theta_i x_i}{2}\left(x_i+2\sum_{j\ne i}x_j\right)
      =\frac{\theta_i x_i}{2}\left(2\sum_jx_j-x_i\right).
\]
For any initial \(x\), write \(t=\sum_i x_i>0\) and \(p_i=x_i/t\), so \(p\) belongs to the open simplex \(\Delta^\circ=\{p_i>0,\sum_i p_i=1\}\). Define
\[
 Z(p)=\sum_{i=1}^d\theta_i p_i(2-p_i),\qquad
 A(p)=\frac{Z(p)}2,\qquad
 F_i(p)=\frac{\theta_i p_i(2-p_i)}{Z(p)}.
\]
For all \(p\) in the closed simplex \(\Delta\) set
\[
 \boxed{\quad
 T_*(p)=\exp\!\left[-\sum_{j=0}^{\infty}2^{-j-1}
               \log A(F^{\circ j}(p))\right].\quad}
\]
The series converges uniformly on \(\Delta\); \(T_*\) is positive and continuous and satisfies the exact invariance equation
\[
 T_*(F(p))=A(p)T_*(p)^2.
\]
For every \(p\in\Delta^\circ\), the projective iterates \(F^{\circ n}(p)\) converge to \(q\). With \(x^{(n)}=H^{\circ n}(tp)\), exactly one of the following alternatives holds:
\[
 \begin{array}{lll}
 0<t<T_*(p)&\Longrightarrow&x^{(n)}\longrightarrow 0,\\
 t=T_*(p)&\Longrightarrow&x^{(n)}\longrightarrow (2/c)q,\\
 t>T_*(p)&\Longrightarrow&x_i^{(n)}\longrightarrow+\infty\quad\text{for all }i.
 \end{array}
\]
The first and third alternatives have double-exponential radial growth/decay. Thus \(\{T_*(p)p:p\in\Delta^\circ\}\) is the entire strict-positive extinction–escape boundary and the global stable set of the positive fixed point \((2/c)q\).

Put
\[
 B_\theta=\max\left\{\left|\log\frac{\min_i\theta_i}{2}\right|,
                       \left|\log\max_i\theta_i\right|\right\}.
\]
Writing \(T_{*,N}\) for the same expression truncated at \(j=N-1\), the explicit uniform certificate is
\[
 \boxed{\quad |\log T_{*,N}(p)-\log T_*(p)|\le 2^{-N}B_\theta
 \quad\text{for all }p\in\Delta.\quad}
\]
For equal parameters \(\theta_i=\theta>0\), let \(e=(1/d,\ldots,1/d)\), \(B=2-1/d\), and \(\lambda=2(d-1)/(2d-1)\). Then
\[
 \boxed{\quad
 \frac{2}{\theta B}\le T_*(p)\le\frac2\theta\qquad(p\in\Delta),\quad}
\]
with equality on the left **only** at \(e\), and on the right **only** at a vertex of \(\Delta\). Moreover, as \(v\to0\) in the tangent hyperplane \(\sum_i v_i=0\),
\[
 \boxed{\quad
 T_*(e+v)=\frac{2}{\theta B}
 \left(1+\frac{\|v\|_2^2}{B(2-\lambda^2)}+o(\|v\|_2^2)\right).\quad}
\]
In particular the balanced composition is a genuinely curved, nonflat minimizer of the global basin boundary.

## Assumptions and scope

All inequalities defining the positive parameter chamber are strict. The theorem concerns discrete time, every dimension \(d\ge3\), all strictly positive initial coordinates, and no upper bound on initial total mass. The graph extends continuously to the closed simplex, but the trichotomy's middle-limit formula is asserted only for strictly positive compositions: boundary faces can possess different nonzero fixed points. The radial variable \(t\) is total mass, not Euclidean norm. The asymptotic symbols for the symmetric expansion mean a limit within \(\sum_i p_i=1\). No general claim is made for parameter sets outside the displayed interior-fixed-point chamber.

## Proof

**1. Exact projective/radial factorization and fixed point.** Set \(x_i=tp_i\). Homogeneity gives
\[
 H_i(tp)=\frac{t^2}2\theta_i p_i(2-p_i),\qquad
 \sum_iH_i(tp)=A(p)t^2,
\]
so the next composition is exactly \(F(p)\). The formula for \(c\) implies \(\sum_iq_i=2d-c\sum_i\theta_i^{-1}=1\). Since \(q_i>0\), it lies in the open simplex, and \(\theta_i(2-q_i)=c\), hence \(F(q)=q\), \(A(q)=c/2\) and \(H((2/c)q)=(2/c)q\). Conversely any strictly positive fixed point must solve \(\theta_i(2-p_i)=\mathrm{constant}\), so the positive fixed point is unique.

**2. Global attraction of the projective composition.** Fix \(p\in\Delta^\circ\) and put \(r_i=p_i/q_i\), \(M=\max_i r_i\), \(m=\min_i r_i\). Since \(\sum_iq_ir_i=1\), unless \(p=q\) one has \(0<m<1<M\). Write
\[
 h_i=\frac{p_i(2-p_i)}{q_i(2-q_i)}
     =r_i\frac{2-p_i}{2-q_i}.
\]
The scalar function \(s\mapsto s(2-s)\) is strictly increasing on \((0,1)\). If \(r_i>1\), then \(1<h_i<r_i\); if \(r_i<1\), then \(r_i<h_i<1\); and if \(r_i=1\), then \(h_i=1\). Since \(F_i(p)/q_i=h_i/(\sum_jq_jh_j)\), its projective spread satisfies
\[
 \frac{\max_i F_i(p)/q_i}{\min_i F_i(p)/q_i}
 =\frac{\max_i h_i}{\min_i h_i}<\frac{M}{m}.
\]
Let \(R(p)=M/m\). Thus \(R(F^{\circ n}p)\) strictly decreases unless \(p=q\). Because \(m\le1\le M\), the bound \(R(p_n)\le R(p)\) implies \(1/R(p)\le p_{n,i}/q_i\le R(p)\) for every \(n,i\). The orbit therefore stays in a compact subset of the open simplex. If its decreasing spread had limit strictly greater than one, a convergent subsequence would have a limit \(\bar p\ne q\); continuity and the strict inequality above would give \(R(F(\bar p))<R(\bar p)\), contradicting convergence of the spread. Hence \(R(p_n)\to1\), and normalization \(\sum_i p_{n,i}=1\) yields \(p_n\to q\). This proves the global projective assertion without assuming a nonstandard convergence lemma.

**3. Uniformly certified separatrix.** For every \(p\in\Delta\),
\[
 \frac{\min_i\theta_i}{2}\le A(p)\le\max_i\theta_i,
\]
because \(1\le 2-p_i\le2\). Thus all logarithms are bounded in absolute value by \(B_\theta\), uniformly under iteration. The weighted logarithmic series converges uniformly and its tail beyond index \(N-1\) is at most \(2^{-N}B_\theta\). This proves positivity, continuity, and the stated truncation bound. Splitting off the first term of the series gives
\[
 \log T_*(p)=-\tfrac12\log A(p)+\tfrac12\log T_*(F(p)),
\]
which is the exact invariance equation.

For a trajectory with total mass \(t_n\) and composition \(p_n=F^{\circ n}(p)\), write \(u_n=\log t_n\). The radial recursion is
\[
 u_{n+1}=2u_n+\log A(p_n).
\]
Iterating and subtracting the infinite defining series gives the **exact finite-time identity**
\[
 \boxed{\quad
 u_n=2^n\log\frac{t_0}{T_*(p)}
      -\sum_{k=0}^{\infty}2^{-k-1}\log A(p_{n+k}).\quad}
\]
The last sum is uniformly bounded by \(B_\theta\). Consequently, if \(t_0<T_*(p)\) then \(u_n\to-\infty\) on a doubly exponential scale, and if \(t_0>T_*(p)\), then \(u_n\to+\infty\) on that scale. Since \(p_n\to q\) in the open simplex, these conclusions hold coordinatewise for \(x^{(n)}=t_np_n\). On the threshold \(t_0=T_*(p)\), the first term vanishes. By projective convergence and continuity, the second term tends to \(-\log A(q)=-\log(c/2)\); hence \(t_n\to2/c\), and \(x^{(n)}\to(2/c)q\). Every point off the threshold falls into one of the two other cases, so this graph is exactly the entire positive basin boundary and stable set.

**4. Symmetric extrema and curvature.** Suppose every \(\theta_i=\theta\). For all \(p\in\Delta\),
\[
 A(p)=\frac\theta2\left(2-\sum_i p_i^2\right).
\]
The simplex inequality \(1/d\le\sum_i p_i^2\le1\) gives \(\theta/2\le A(p)\le\theta B/2\), with the upper equality only at \(e\) and lower equality only at vertices. Since the same bounds hold for every projective iterate, the weighted geometric mean defining \(T_*\) lies between their reciprocals. Equality at an endpoint requires equality already for the strictly positive first weight, proving the two unique-attainment assertions.

For the local expansion let \(p=e+v\) with \(\sum_i v_i=0\). Then exactly
\[
 A(e+v)=\frac{\theta B}{2}\left(1-\frac{\|v\|_2^2}{B}\right),
\]
while the derivative of \(F\) on the tangent hyperplane at \(e\) is scalar multiplication by \(\lambda=2(d-1)/(2d-1)\), with \(0<\lambda<1\). In a sufficiently small invariant neighborhood of \(e\), the derivatives of the iterates are uniformly bounded by a geometric rate \(\kappa^j\) for some \(\lambda<\kappa<1\). Therefore the quadratic terms in the series for \(\log T_*\) admit termwise dominated convergence; for each fixed \(j\), \(F^{\circ j}(e+v)-e=\lambda^jv+o(\|v\|_2)\). Consequently,
\[
 \log T_*(e+v)=-\log(\theta B/2)
   +\frac{\|v\|_2^2}{B}
       \sum_{j=0}^{\infty}2^{-j-1}\lambda^{2j}
   +o(\|v\|_2^2).
\]
The geometric series equals \(1/(2-\lambda^2)\). Exponentiation yields the claimed expansion, completing the proof.

## Verification

The standalone `check.py` uses only the Python standard library and may be executed as `python check.py`. It verifies the direct polynomial/projective factorization exactly using rational arithmetic for dimensions 3, 4, and 7; numerically checks the strict projective-ratio decrease, the threshold functional equation and interior fixed points for equal and unequal coefficients; checks the symmetric curvature coefficient; and tests the three radial regimes with 180-digit decimal arithmetic. Its recorded terminal marker is `ALL_FINITE_CHECKS_PASSED`. Each finite check is a consistency test, **not** an infinite-dimensional or all-parameter proof. The analytical argument above establishes every quantified assertion.

For reproducible rigorous evaluation at arbitrary parameters satisfying the chamber condition, compute \(p_j=F^{\circ j}(p)\) and the first \(N\) terms of the product. Regardless of numerical roundoff, the exact-real truncation error in \(\log T_*\) is no larger than \(2^{-N}B_\theta\); any floating-point implementation must account for its own arithmetic error separately. The existence/classification theorem itself does not require floating-point evaluation.

## Relationship to prior work

Shoyimardonov and Rozikov introduced this exact quadratic operator and classified its fixed points. Their arXiv paper (2024) and journal version (2025) establish a two-dimensional extinction–escape separating curve qualitatively and give a polynomial **approximation** for an example; in arbitrary dimension they identify invariant subregions known to decay or escape and the positive fixed point's unstable line. Neither version gives the uniformly evaluable global threshold graph or the strict-positive trichotomy in every dimension. Those pre-existing facts are fully credited.

Lins (2022) and the older nonlinear Perron–Frobenius literature provide broad projective convergence theorems for order-preserving, positively homogeneous or subhomogeneous maps. In particular, an appropriately rescaled degree-one version of this map can be analyzed by those general methods, so convergence of the composition alone is **not** claimed as a standalone novel theorem. The distinct result here is the specific entire basin graph, its uniform numerical certificate, and its sharp symmetric geometry, proved directly and jointly with global convergence. The infinite-product device uses elementary homogeneity and does not claim to invent nonlinear spectral theory.

## Limitations

No claims are made about the critical orbit limit for an initial state with zero coordinates, nor about the global projective dynamics outside the positive-fixed-point chamber. The infinite product is an exact convergent representation, not a finite elementary formula. Finite numerical experiments do not establish the global theorems. Existing broad positive-operator convergence theory may offer shorter proofs of the projective step, and equivalent basin-graph formulas in unindexed literature remain a publication-priority risk. No independent audit is asserted.

## References

1. S. K. Shoyimardonov and U. A. Rozikov, *Discrete-Time Dynamical Systems Generated by a Quadratic Operator*, arXiv:2409.13450, first posted 2024-09-20. https://arxiv.org/html/2409.13450v1 .
2. S. K. Shoyimardonov and U. A. Rozikov, *Discrete-Time Dynamical Systems Generated by a Quadratic Operator*, Russian Journal of Nonlinear Dynamics **21** (2025), 399–418, DOI:10.20537/nd250803. https://nd.ics.org.ru/upload/iblock/cc9/nd250803.pdf .
3. B. Lins, *Convergence of iterates in nonlinear Perron-Frobenius theory*, arXiv:2207.14098, first posted 2022-07-28. https://arxiv.org/abs/2207.14098 .
4. B. Lemmens and R. Nussbaum, *Nonlinear Perron–Frobenius Theory*, Cambridge University Press (2012), especially the general theory of projective metrics and subhomogeneous maps.
