# The sharp rim-deletion price frontier and critical window in wheel resistance design

## Finding

For every integer \(n\ge3\), consider the wheel \(W_{n+1}=K_1\vee C_n\). Its \(n\) hub-to-rim edges (spokes) each have price \(P>0\) per unit conductance and its \(n\) consecutive rim edges each have price \(Q>0\). All \(2n\) conductances are independently designable and nonnegative under total expenditure at most \(B>0\). The objective is the sum \(\mathcal K=\sum_{u<v}R_{uv}\) of unordered-pair effective resistances; disconnected allocations have infinite objective.

**Theorem (complete price frontier).** There is exactly one global minimizer. Define \(\theta=Q/P\) and \(\theta_c(n)=2(n+1)/n\). Each spoke receives the same conductance \(a_*>0\) and each rim edge receives the same conductance \(b_*\ge0\). All rim conductances vanish **if and only if** \(\theta\ge\theta_c(n)\). In this regime,
\[
 a_*=\frac{B}{nP},\qquad b_*=0,\qquad \mathcal K_*=\frac{Pn^3}{B}.
\]
For \(0<\theta<\theta_c(n)\), the ratio \(z_*=b_*/a_*\) is the unique positive solution of
\[
Q\left(\frac1{n+1}+\sum_{k=1}^{n-1}\frac1{1+c_kz}\right)
=(P+Qz)\sum_{k=1}^{n-1}\frac{c_k}{(1+c_kz)^2},\qquad
c_k=2-2\cos\left(\frac{2\pi k}{n}\right),
\]
and
\[
a_*=\frac{B}{n(P+Qz_*)},\quad b_*=z_*a_*,\quad
\mathcal K_*=\frac{n(n+1)}B(P+Qz_*)
\left(\frac1{n+1}+\sum_{k=1}^{n-1}\frac1{1+c_kz_*}\right).
\]
The equations characterize the **unrestricted** optimizer; equal edge weights within a class are conclusions, not optimization assumptions.

At fixed \(n\), put \(\delta=\theta_c(n)-\theta\downarrow0\). The onset of rim investment and the strict improvement over the optimal star obey
\[
\frac{b_*}{a_*}=\frac{n^2}{4(n+1)(n-2)}\,\delta+O_n(\delta^2),\qquad
\frac{Pn^3}{B}-\mathcal K_*
=\frac{Pn^5}{8B(n+1)(n-2)}\,\delta^2+O_n(\delta^3).
\]
For fixed \(P,Q>0\), as \(n\to\infty\),
\[
\frac{b_*}{a_*}\longrightarrow \max\left\{0,\frac P Q-\frac12\right\},\quad
\frac{B\mathcal K_*}{n^3}\longrightarrow
\begin{cases}\frac12\sqrt{Q(4P-Q)},&Q<2P,\\P,&Q\ge2P.\end{cases}
\]
In the finite-size critical window \(Q=2P(1+\eta/n)\), for any fixed real \(\eta\) and sufficiently large \(n\) so that \(Q>0\),
\[
n\frac{b_*}{a_*}\longrightarrow \max\left\{0,\frac{1-\eta}{2}\right\}.
\]
In particular, at exactly \(Q=2P\) every finite wheel invests positively in its rim, although the optimal rim-to-spoke ratio is asymptotic to \(1/(2n)\).

## Assumptions and scope

Edges form a simple undirected wheel, including \(n=3\), for which the underlying graph is \(K_4\). The Laplacian is the unnormalized conductance Laplacian. Prices are constant within the spoke class and within the rim class, but individual conductances need not be symmetric. The expenditure inequality is saturated at every finite optimum by homogeneity. The Kirchhoff objective uses *all* \(\binom{n+1}{2}\) unordered vertex pairs and unit electrical injections, without additional vertex masses.

## Proof

**Uniqueness before symmetry.** For any connected allocation \(w\), let \(L(w)\) be its Laplacian and \(J=\mathbf1\mathbf1^{\mathsf T}/(n+1)\). The matrix \(H=L+J\) is positive definite and \(\mathcal K=(n+1)(\operatorname{tr}H^{-1}-1)\). Along any nonzero feasible conductance perturbation \(E\) on a simple graph, its Laplacian perturbation \(\Delta L\) is nonzero (its off-diagonal entries recover the individual edge perturbations). The second derivative is
\[
2(n+1)\operatorname{tr}(H^{-1}\Delta L H^{-1}\Delta L H^{-1})>0.
\]
Indeed, writing \(A=H^{-1/2}\Delta L H^{-1/2}\), this is \(2(n+1)\operatorname{tr}(A^2H^{-1})>0\). Thus the connected-domain objective is strictly convex and its budget-constrained minimizer is unique. Existence follows from compactness of the budget simplex and divergence of the resistance objective toward disconnection; the all-spoke allocation is a finite competitor. Since rotation of the rim preserves prices, uniqueness forces identical weights within each of the two edge orbits. The common spoke conductance must be positive or the hub is isolated.

**Spectrum and exact reduction.** Write the common spoke and rim conductances as \(a>0\) and \(b\ge0\). The hub-versus-constant-rim eigenmode has eigenvalue \((n+1)a\); the nonconstant discrete Fourier modes of the rim have eigenvalues \(a+c_kb\) for \(1\le k<n\). Hence
\[
\mathcal K=(n+1)\left[\frac1{(n+1)a}+\sum_{k=1}^{n-1}\frac1{a+c_kb}\right].
\]
Substituting \(z=b/a\) and the exact expenditure \(n(Pa+Qb)=B\) yields \(\mathcal K=n(n+1)F_n(z)/B\), where
\[
S_n(z)=\frac1{n+1}+\sum_{k=1}^{n-1}\frac1{1+c_kz},\qquad F_n(z)=(P+Qz)S_n(z).
\]
For numerical or symbolic evaluation without a trigonometric sum, set \(d(z)=\sqrt{1+4z}\) and \(u(z)=2z/(1+2z+d(z))\). The finite Poisson-kernel identity gives, for \(z>0\),
\[
S_n(z)=\frac{n}{d(z)}\frac{1+u(z)^n}{1-u(z)^n}-\frac n{n+1},
\]
with continuous value \(S_n(0)=n^2/(n+1)\). This follows by expanding \((1+2z-2z\cos t)^{-1}\) into its absolutely convergent Fourier series and summing over the \(n\)-th roots of unity.

**Exact activation threshold.** The root-of-unity sums yield \(\sum_{k=1}^{n-1}c_k=2n\) and, for \(n\ge3\), \(\sum_{k=1}^{n-1}c_k^2=6n\). Therefore
\[
F_n'(0)=\frac{Qn^2}{n+1}-2Pn
=\frac{Pn^2}{n+1}\bigl(\theta-\theta_c(n)\bigr).
\]
In the affine budget variable \(b\), the objective is strictly convex. If this boundary derivative is nonnegative, its unique minimum is \(b=0\); if negative, it moves into \(b>0\). As \(a\to0\), the hub-mode contribution diverges, so an interior minimum exists and has the displayed stationarity equation. The value at \(b=0\) equals \(Pn^3/B\).

**Local onset.** At \(\theta=\theta_c(n)\), differentiating once more gives \(F_n''(0)=12Pn-4Qn=4P(n-2)>0\). Expanding the unique interior stationary point via the implicit function theorem gives the linear formula for \(z_*\). Substitution into the quadratic Taylor expansion of \(F_n\) gives the stated quadratic improvement, including the exact coefficient.

**Large wheels and critical window.** On every compact \(z\)-interval, the Fourier Riemann sum and its first derivative converge uniformly:
\[
\frac{S_n(z)}n\longrightarrow\frac1{\sqrt{1+4z}}.
\]
The limiting objective is \((P+Qz)/\sqrt{1+4z}\), with unique minimizer \(\max\{0,P/Q-1/2\}\). If the limiting minimizer is positive, bracketing the unique finite-\(n\) stationary point between two fixed points of opposite derivative signs proves convergence. If \(Q>2P\), the exact finite threshold eventually forces \(z_*=0\); the equality case follows from the next calculation. Substitution gives the limit for \(B\mathcal K_*/n^3\).

For \(Q_n=2P(1+\eta/n)\) and fixed \(c\ge0\), the exact moment sums and uniformly bounded \(c_k\) give
\[
\lim_{n\to\infty}\frac1P F_n'(c/n)=2(\eta-1)+4c.
\]
When \(\eta\ge1\), the finite threshold yields \(z_*=0\). Otherwise the limiting derivative changes sign exactly at \(c=(1-\eta)/2\); uniqueness and derivative bracketing show \(nz_*\to(1-\eta)/2\). This proves the critical-window claim.

## Verification

The standalone file `wheel_opt_verify.py` can be run with Python 3, NumPy, SciPy, and SymPy. It checks the original unrestricted weighted Laplacian, not only the reduced scalar objective. A symbolic five-vertex example with \(P=13\), \(Q=17\), \(B=1\) has \(a_*=b_*=1/120\), positive Laplacian eigenvalues \(1/40\) and \(1/24\), each of multiplicity two, and \(\mathcal K_*=640\).

The program completed 144 independently assembled full-spectrum comparisons, 144 independent finite Poisson-kernel comparisons, 144 budget/stationarity checks, 2,160 arbitrary asymmetric feasible allocations, 12 independently constrained numerical optimizations, and five large-wheel critical-scaling comparisons. The theorem for all sizes and prices is analytical; the finite experiments neither establish infinity-wide correctness nor exhaust the continuum of feasible conductances.

## Relationship to prior work

Ghosh, Boyd and Saberi (2008, Section 5.2, equation (38), pages 59–60) explicitly solve the **equal-price** wheel conductance-design reduction and give the same basic Fourier spectrum; those facts are established prior work, not new claims here. Their general strictly convex framework also underlies the argument. The assessed additional conclusions concern two *unequal* class prices: the exact all-or-nothing rim activation frontier, the finite critical exponent and coefficient, the large-wheel priced allocation limit, and its critical-window scaling. The 2006 conference precursor is a source for the classical framework. Li, Yang and Zhang (2008) consider Kirchhoff indices of weighted wheels, but their full primary text was not accessible for a decisive optimization comparison. Searches of published mathematical research records returned wheel-related geometry and other spectral problems, not an implication-equivalent resistance-cost allocation classification.

## Limitations

The cost law has two orbit-constant positive prices, not arbitrary individual edge costs. The criterion optimizes total resistance, not worst-case pair resistance, failure robustness or algebraic connectivity. Exact formulas for the interior branch require solving a strictly unimodal one-variable stationarity equation; a closed radical for every size is not asserted. Publication priority is not established by absence of search matches; the weighted-wheel literature cited above remains a residual coverage risk. Independent validation has not been performed.

## References

1. A. Ghosh, S. Boyd and A. Saberi, *Minimizing Effective Resistance of a Graph*, SIAM Review **50** (2008), 37–66. DOI: 10.1137/050645452. Accessible author-hosted full text: https://stanford.edu/~boyd/papers/pdf/eff_res.pdf (Section 5.2 and Eq. (38)); earlier conference version: *Proceedings MTNS*, Kyoto, July 2006.
2. C. Li, Y. Yang and H. Zhang, *Kirchhoff index of weighted wheel graphs*, Journal of Lanzhou University **44**(3) (2008); bibliographic record: https://www.researchgate.net/publication/268625211_Kirchhoff_index_of_weighted_wheel_graphs_W_n_ab . The full article was not inspected.
3. S. Gago Álvarez, *Kirchhoff index of a non-complete wheel* (2016), repository record: https://upcommons.upc.edu/bitstreams/f366ab53-0bb6-480b-978f-ae0761f63ca1/download . The download was inaccessible during comparison; the object is a non-complete wheel, not the full wheel considered here.
