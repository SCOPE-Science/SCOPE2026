# Sharp price-threshold and water-filling law for minimax vertex coherence on weighted stars

## Finding

**Theorem.** Let \(m\ge2\), \(n=m+1\), \(B>0\), and let \(c_1,\ldots,c_m>0\) be arbitrary edge-conductance prices. On the star with hub \(0\) and leaves \(1,\ldots,m\), assign arbitrary independent conductances \(w_i>0\) subject to \(\sum_{i=1}^m c_iw_i\le B\). Let \(L(w)\) be its weighted combinatorial Laplacian and define the *worst-vertex disagreement variance proxy* \(\Phi(w)=\max_{0\le v\le m}(L(w)^\dagger)_{vv}\), where \(\dagger\) denotes the Moore--Penrose pseudoinverse. Equivalently, for the stochastic consensus model \(dx=-L(w)x\,dt+dW\) with independent unit-intensity Brownian inputs, the largest stationary variance of a vertex's deviation from the network mean equals \(\Phi(w)/2\).

Put \(\alpha=m^2-1\). There is a **unique** scalar \(\tau>0\) satisfying
\[
\sum_{i=1}^m\left(\frac{c_i}{\tau}-1\right)_+=\alpha,
\qquad (s)_+=\max\{s,0\}.
\]
Set \(y_i=\min\{1,\sqrt{c_i/\tau}\}\) and \(Z=\sum_{i=1}^m c_i/y_i\). Then the **unique global minimizer** is
\[
\boxed{w_i^*=\frac{B}{Zy_i},\quad i=1,\ldots,m.}
\]
Let \(A=\{i:c_i>\tau\}\), \(k=|A|\), and \(C_A=\sum_{i\in A}c_i\). The threshold is in fact a finite piecewise-rational calculation:
\[
\tau=\frac{C_A}{\alpha+k},\qquad
\boxed{\Phi_* =\frac{1}{n^2B}\left(\sqrt{(\alpha+k)C_A}+\sum_{i\notin A}\sqrt{c_i}\right)^2.}
\]
At equality \(c_i=\tau\) the corresponding conductance still belongs to the common-resistance tier, but its dual weight is zero; the strict definition of \(A\) removes any ambiguity. Thus the high-price edges have equal optimal resistances, while lower-price edges have resistances proportional to \(\sqrt{c_i}\).

Writing \(C=\sum_i c_i\), **all conductances are equal if and only if**
\[
\boxed{\min_i c_i\ge\frac{C}{m^2+m-1}.}
\]
If the inequality fails, the uniquely optimal allocation is nonuniform. Relative to equal conductances with the same price budget, the improvement is universally bounded and the bound is sharp:
\[
\boxed{1\le\frac{\Phi_{\rm equal}}{\Phi_*}\le
\frac{m^2+m-1}{m^2}=1+\frac1m-\frac1{m^2}.}
\]
The right-hand bound is approached as one price retains a fixed positive value and all other strictly positive prices tend to zero; it is not attained by a strictly positive price vector.

## Assumptions and scope

The graph is the ordinary \(m\)-leaf star, no loops or parallel edges, and each leaf edge has a positive independently chosen symmetric conductance. Prices and budget are strictly positive; \(m\) is an integer at least two. The graph is connected for every admissible allocation because every conductance is positive. The pseudoinverse is taken on the full \(n\)-vertex Laplacian with the consensus zero mode removed. No symmetry is imposed on prices or decisions. The optimization is over a *fixed star topology*; this does not claim optimality among other graphs. The stochastic interpretation assumes independent equal-intensity unit white noise at each vertex and measures deviations from the instantaneous network mean.

The scalar-root construction is exact, not a numerical prescription requiring an optimization oracle: sort the prices in nonincreasing order and, for each possible active cardinality \(k\in\{1,\ldots,m\}\), compute \(\tau_k=(c_{(1)}+\cdots+c_{(k)})/(\alpha+k)\). Exactly the consistent threshold (with \(c_{(k)}>\tau_k\ge c_{(k+1)}\), treating \(c_{(m+1)}=0\)) produces the strict active set; boundary ties can be assigned to the zero-dual-weight tier. Equivalently, monotone bisection computes the unique positive root.

## Proof

**1. Exact vertex variances.** Write \(r_i=1/w_i>0\) and \(S=\sum_i r_i\). On a star the effective resistance between hub and leaf \(i\) is \(r_i\), and the resistance between leaves \(i,j\) is \(r_i+r_j\). For any connected \(n\)-vertex graph, the exact identity
\[
(L^\dagger)_{vv}=\frac1n\sum_{u}R_{vu}-\frac1{n^2}\sum_{u<v}R_{uv}
\]
follows by expanding \(R_{uv}=(e_u-e_v)^\mathsf T L^\dagger(e_u-e_v)\) and using \(L^\dagger\mathbf1=0\). For the star, \(\sum_{u<v}R_{uv}=mS\), \(\sum_uR_{0u}=S\), and \(\sum_uR_{iu}=S+(m-1)r_i\) for a leaf. Therefore
\[
(L^\dagger)_{00}=\frac{S}{n^2},\qquad
(L^\dagger)_{ii}=\frac{S+\alpha r_i}{n^2},\quad
\alpha=(m-1)n=m^2-1.
\]
All leaf variances strictly exceed the hub variance, so
\[
\Phi(w)=\frac{S+\alpha\max_i r_i}{n^2},\qquad
\sum_i\frac{c_i}{r_i}\le B.
\]
Since scaling all positive conductances upward lowers \(\Phi\) strictly, every optimum exhausts the budget.

**2. A global sharp dual bound.** For any probability vector \(p\in\mathbb R^m_{\ge0}\), \(\sum_i p_i=1\), put \(a_i=1+\alpha p_i\). For all feasible \(r\), the maximum dominates its \(p\)-weighted mean, and Cauchy--Schwarz gives
\[
\begin{aligned}
n^2\Phi(w)&=\sum_i r_i+\alpha\max_i r_i
\ge\sum_i a_ir_i\\
&\ge\frac{\left(\sum_i\sqrt{a_ic_i}\right)^2}{\sum_i c_i/r_i}
\ge\frac{\left(\sum_i\sqrt{a_ic_i}\right)^2}{B}.
\end{aligned}
\]
These inequalities hold globally, for arbitrary asymmetric allocations, without convex-programming regularity assumptions.

**3. Optimize the bound and attain equality.** The function \(f(p)=\sum_i\sqrt{c_i(1+\alpha p_i)}\) is strictly concave on the probability simplex because all \(c_i,\alpha\) are positive. Its unique maximizer obeys the elementary Lagrange multiplier / one-sided derivative conditions
\[
p_i^*=\frac1\alpha\left(\frac{c_i}{\tau}-1\right)_+.
\]
Normalization gives \(\sum_i(c_i/\tau-1)_+=\alpha\). The left side is continuous and strictly decreasing where positive, tends to infinity as \(\tau\downarrow0\), and vanishes at \(\tau\ge\max_i c_i\); hence its positive root is unique. Put \(y_i=\min(1,\sqrt{c_i/\tau})\). Then \(a_i^*=\max(1,c_i/\tau)\) and
\[
\sqrt{\frac{c_i}{a_i^*}}=\sqrt\tau\, y_i.
\]
Choose \(r_i^*=(Z/B)y_i\) with \(Z=\sum_i c_i/y_i\). Its budget is exactly \(B\). Cauchy--Schwarz is an equality because \(r_i^*\) is proportional to \(\sqrt{c_i/a_i^*}\); and every index with \(p_i^*>0\) has \(y_i=1\), the maximal resistance, so the weighted-maximum bound is also an equality. Thus the proposed allocation meets the global lower bound and is optimal.

Equality in Cauchy--Schwarz for the fixed \(p^*\) forces any global minimizer to have \(r_i\propto\sqrt{c_i/a_i^*}\); budget saturation fixes the proportionality constant. Hence the minimizer is **unique**. Summing the optimized square roots separately over \(A=\{c_i>\tau\}\) and its complement gives \(f(p^*)=C_A/\sqrt\tau+\sum_{i\notin A}\sqrt{c_i}\). The threshold equation gives \(C_A=(\alpha+k)\tau\), proving the exact closed-value formula and tier description.

**4. Exact uniform threshold.** A uniform conductance allocation has \(r_i=C/B\) and \(\Phi_{\rm equal}=(m+\alpha)C/(n^2B)\). The dual equality conditions can hold at a common resistance precisely when \(a_i^*/c_i\) is independent of \(i\); writing \(\sum_i p_i^*=1\) gives \(p_i^*=((m+\alpha)c_i/C-1)/\alpha\). This is nonnegative for every \(i\) exactly when \(c_i\ge C/(m+\alpha)\). This proves both directions of the uniform-optimality criterion. Outside this range uniqueness implies a strict improvement.

**5. Sharp price-uniformity factor.** Let \(d_i=c_i/C\), so \(\sum_i d_i=1\), and take the admissible dual vector \(p_i=d_i\). Since \(0<d_i\le1\),
\[
\sqrt{d_i(1+\alpha d_i)}\ge d_i\sqrt{1+\alpha}.
\]
The global lower bound therefore gives
\[
\Phi_*\ge\frac{C(1+\alpha)}{n^2B}=\frac{Cm^2}{n^2B}.
\]
Combining with the explicit equal-conductance value proves the universal factor \((m+\alpha)/(1+\alpha)=(m^2+m-1)/m^2\). Finally, with \(c_1=1\) and every other \(c_i=\varepsilon>0\), the dual-optimal expression tends to \(f(p^*)^2=1+\alpha\) as \(\varepsilon\downarrow0\), establishing sharpness as a limit. For strictly positive prices and \(m\ge2\), the inequality just used is strict for all \(i\) with \(0<d_i<1\), so the upper ratio is not attained.

## Verification

An exact five-node rational certificate takes \(m=4\), prices \((240,32,1,4)\) and budget \(B=284\). Here \(\alpha=15\), \(\tau=16\), \(A=\{1,2\}\), \(y=(1,1,1/4,1/2)\), \(Z=284\), optimal resistances \((1,1,1/4,1/2)\) and conductances \((1,1,4,2)\). The weighted budget is exactly \(284\), and direct exact inversion of \(L+\mathbf1\mathbf1^\mathsf T/5\) confirms \(\Phi_*=71/100\). This verifies a genuinely nontrivial two-price-tier case without floating-point assumptions.

The standalone `verify.py` reproduces this rational certificate with SymPy; checks boundary and active-set profiles; and performs 96 seeded random positive-price comparisons using full numerical Laplacian pseudoinverses, a separately solved constrained minimization, exact primal-dual identities to tolerance, and 2,880 feasible asymmetric allocations. It also checks the sharp equal-conductance comparison and cost-concentration limit. Its captured output is in `verification_output.txt`. These are finite supporting checks: the five-step mathematical argument above proves the theorem for all stated parameter values.

## Relationship to prior work

Ghosh, Boyd and Saberi (MTNS 2006; SIAM Review 2008) establish convex optimization for total effective resistance and discuss, as an extension, minimization of the **maximum pairwise effective resistance**. Neither is the present objective, which is the maximum **diagonal entry of the Laplacian pseudoinverse**, a centered average-resistance quantity. For a star, the pairwise maximum is the sum of the two largest edge resistances, whereas the worst vertex coherence is \((\sum_i r_i+\alpha\max_i r_i)/n^2\); these are not equivalent optimization problems and generally yield different optimal allocations.

Patterson and Bamieh (arXiv:1310.2592v1, 2013) derive the connection between first-order noisy consensus and the pseudoinverse trace, focusing on mean network coherence and fractal scaling. Summers, Shames, Lygeros and Dörfler (arXiv:1411.4884v1, 2014) optimize **trace coherence** by adding edges to a network, rather than optimizing worst-vertex coherence over all independently priced edges of a fixed star. Van Mieghem, Devriendt and Cetinay (2017) explicitly study individual pseudoinverse diagonal entries and give an unweighted-star formula, but do not derive this all-price minimax conductance allocation in the inspected material.

The new contribution assessed here is specifically the *arbitrary-price minimax-vertex* allocation, unique active-set law, exact equal-conductance threshold, and sharp worst-case uniform-allocation comparison. General convexity and resistance identities are credited to the established literature; no assertion of absolute priority is made.

## Limitations

Only connected weighted stars, independent unit-intensity node noise, and linear positive edge prices are covered. The objective is a worst-vertex stationary variance, not average coherence, spectral-gap speed, worst-pair resistance, or worst-case transient amplification. The rightmost sharp ratio is a supremum approached by price vectors, not a positive-price maximizer. Unindexed specialized optimization literature may contain an equivalent star allocation result; no independent validation has been performed. Numerical testing alone cannot establish the result outside its finite test cases.

## References

1. A. Ghosh, S. Boyd, A. Saberi, *Minimizing Effective Resistance of a Graph*, Proceedings of the 17th International Symposium on Mathematical Theory of Networks and Systems, Kyoto, July 24--28, 2006, pp. 1185--1196. Full text: https://stanford.edu/~boyd/papers/pdf/eff_res_mtns06.pdf. Expanded version: *SIAM Review* 50(1) (2008), pp. 37--66, doi:10.1137/050645452.
2. S. Patterson, B. Bamieh, *Consensus and Coherence in Fractal Networks*, arXiv:1310.2592v1, submitted October 9, 2013. https://arxiv.org/html/1310.2592v1.
3. T. Summers, I. Shames, J. Lygeros, F. Dörfler, *Topology Design for Optimal Network Coherence*, arXiv:1411.4884v1, submitted November 18, 2014. https://arxiv.org/html/1411.4884v1.
4. P. Van Mieghem, K. Devriendt, H. Cetinay, *Pseudoinverse of the Laplacian and best spreader node in a network*, *Physical Review E* 96 (2017), 032311, doi:10.1103/PhysRevE.96.032311. Author full text: https://www.nas.ewi.tudelft.nl/people/Piet/papers/PhysRevE2017_pseudo_inverse_Laplacian.pdf.
