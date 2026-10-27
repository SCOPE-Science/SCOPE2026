# A square-summability criterion and two critical exponents for weighted recursive-tree path length

## Finding
For a weighted recursive tree with **arbitrary strictly positive deterministic vertex weights**, define \(p_j=w_j/(w_1+\cdots+w_j)\) and the centered depth innovation \(\xi_j\) and its variance \(v_j\) as below. Then the centered total path length satisfies the exact dichotomy

\[
\frac{T_n-\mathbb E T_n}{n}\xrightarrow{\mathrm{a.s.},\,L^2}
Z=\sum_{j=2}^{\infty}p_j\xi_j
\quad\Longleftrightarrow\quad
Q:=\sum_{j=2}^{\infty}p_j^2v_j<\infty.
\]

Whenever the condition holds, \(\operatorname{Var}(T_n)/n^2\to Q>0\). Whenever it fails, \(\operatorname{Var}(T_n)/n^2\to\infty\); no claim is made about other normalizations or about almost-sure convergence alone in this regime.

For the natural **stretched-exponential total-weight regime** \(p_j\sim c j^{-a}\), with \(c>0\) and \(0<a<1\), the condition holds exactly for \(a>2/3\). More precisely,

\[
\operatorname{Var}(T_n)\sim
\begin{cases}
c\,\mathrm B(1-a,3)n^{3-a}, & 0<a<1/2,\\
\dfrac{c^3}{c^2+1/2}\,\mathrm B(1/2,3)n^{5/2}, & a=1/2,\\
\dfrac{c^3}{1-a}\,\mathrm B(2-3a,3)n^{4-3a}, & 1/2<a<2/3,\\
3c^3n^2\log n, & a=2/3,\\
Qn^2, & 2/3<a<1,
\end{cases}
\]
where \(\mathrm B(u,3)=\int_0^1t^{u-1}(1-t)^2\,dt\) and \(Q\) in the last line depends on the full weight sequence. Thus \(a=1/2\) changes the *local innovation mechanism*, while \(a=2/3\) marks the *global square-integrability threshold*.

## Assumptions and scope
Start with rooted vertex \(1\) of depth \(D_1=0\). For each integer \(j\ge2\), choose the parent \(K_j\in\{1,\ldots,j-1\}\) independently of preceding parent choices with probabilities
\[
\mathbb P(K_j=i)=\frac{w_i}{W_{j-1}},\qquad W_j=\sum_{i=1}^jw_i,
\]
where each deterministic \(w_i>0\). Define \(D_j=1+D_{K_j}\), \(T_n=\sum_{i=1}^nD_i\), \(p_j=w_j/W_j\) (hence \(p_1=1\) and \(0<p_j<1\) for \(j\ge2\)), and \(\mathcal F_j=\sigma(K_2,\ldots,K_j)\). Set
\[
\xi_j=D_j-\mathbb E(D_j\mid\mathcal F_{j-1}),\qquad v_j=\mathbb E\xi_j^2,
\]
with \(\xi_2=0\). The first theorem assumes no regularity on the weights. The explicit asymptotics assume only \(p_j\sim c j^{-a}\), not a prescribed rate of convergence or an exact power law. Such sequences exist; for example \(p_j=c/(j^a+c)\) for \(j\ge2\), with \(W_1=w_1=1\), \(W_j=W_{j-1}/(1-p_j)\), and \(w_j=p_jW_j\). Since \(\sum_{j\le n}p_j\asymp n^{1-a}\), these have stretched-exponentially growing \(W_n\), outside polynomial-total-weight assumptions.

## Proof
**1. Input identities.** The elementary martingale-depth calculation in [1, §5] gives
\[
T_n-\mathbb ET_n=\sum_{j=2}^n(1+(n-j)p_j)\xi_j,
\qquad
v_2=0,\quad v_{j+1}=(1-p_j^2)v_j+p_j(1-p_j).
\]
The innovations are pairwise orthogonal. Define \(V_n=\sum_{j=2}^{n-1}p_j(1-p_j)\) and \(Q_n=\sum_{j=2}^{n-1}p_j^2v_j\). The recurrence telescopes to \(v_n=V_n-Q_n\), so \(0\le v_n\le V_n\).

**2. Sufficiency of \(Q<\infty\).** The martingale \(M_n=\sum_{j=2}^np_j\xi_j\) converges almost surely and in \(L^2\) to \(Z\), since \(\sum_j\mathbb E(p_j\xi_j)^2=Q\). We also prove
\[
\sum_{j=2}^{\infty}\frac{v_j}{j^2}<\infty.
\]
If \(V_\infty<\infty\), the \(v_j\)'s are bounded. If \(V_\infty=\infty\), then \(v_j=V_j-Q_j\ge1\) eventually because \(Q_j\le Q\). Consequently \(\sum_jp_j^2<\infty\), and Cauchy–Schwarz gives \(v_n\le V_n\le\sum_{j<n}p_j=O(\sqrt n)\). In either case the displayed series converges. Therefore the martingale series \(\sum_j\xi_j/j\) converges almost surely and in \(L^2\). The exact decomposition
\[
\frac{T_n-\mathbb ET_n}{n}
=M_n+\frac1n\sum_{j=2}^n\xi_j
-\frac1n\sum_{j=2}^njp_j\xi_j
\]
then converges almost surely to \(Z\): apply Kronecker's lemma separately to \(\sum_j\xi_j/j\) and \(\sum_jp_j\xi_j\). Orthogonality gives \(n^{-2}\sum_{j\le n}v_j\to0\). Furthermore,
\[
\frac1{n^2}\sum_{j\le n}j^2p_j^2v_j\longrightarrow0
\]
by dominated convergence against the finite summable sequence \((p_j^2v_j)\). Thus both remainders vanish in \(L^2\), proving the implication. Since \(v_3=p_2(1-p_2)>0\) and \(p_3>0\), \(Q>0\).

**3. Necessity of \(Q<\infty\).** From the same identity,
\[
\frac{\operatorname{Var}(T_n)}{n^2}=
\sum_{j=2}^n\left(p_j+\frac{1-jp_j}{n}\right)^2v_j.
\]
For each fixed \(j\), the coefficient tends to \(p_j\). Fixing any finite number of terms, taking a lower limit as \(n\to\infty\), and then increasing that number shows
\[
\liminf_{n\to\infty}\frac{\operatorname{Var}(T_n)}{n^2}\ge Q,
\]
including \(Q=\infty\). Hence if \(Q\) diverges the scaled variances diverge, contradicting \(L^2\) convergence; the criterion is exact.

**4. Innovation-variance asymptotics for \(p_j\sim cj^{-a}\).** Put \(b_j=p_j(1-p_j)\). The recurrence is \(v_{j+1}-v_j=b_j-p_j^2v_j\). We claim
\[
v_j\sim
\begin{cases}
j^a/c,&0<a<1/2,\\
\dfrac{c}{c^2+1/2}j^{1/2},&a=1/2,\\
\dfrac{c}{1-a}j^{1-a},&1/2<a<1.
\end{cases}
\]
For \(a>1/2\), the inequality \(v_j\le\sum_{i<j}p_i=O(j^{1-a})\) implies \(p_i^2v_i=O(i^{1-3a})\). Its sum through \(j\) is \(o(j^{1-a})\) for every \(a>1/2\); thus \(v_j=V_j-Q_j\sim c j^{1-a}/(1-a)\).

For \(a<1/2\), compare the recurrence with deterministic barriers \(u_j=A j^a\). The one-step difference \(b_j-p_j^2u_j-(u_{j+1}-u_j)\) is \((c-c^2A+o(1))j^{-a}\); choose \(A=(1\pm\varepsilon)/c\) to obtain strict opposite signs for large \(j\). Discrepancies caused by the finite starting index decay as \(\prod_{i=J}^{j-1}(1-p_i^2)=\exp[-\Theta(j^{1-2a})]\), negligible relative to the barriers. The two comparisons prove \(v_j\sim j^a/c\). At \(a=1/2\), use barriers \(u_j=A\sqrt j\); the analogous residual is \([c-(c^2+1/2)A+o(1)]j^{-1/2}\). The product of contraction factors now decays polynomially because \(\sum p_i^2\sim c^2\log j\), still negligible compared with \(\sqrt j\). Barriers around \(A=c/(c^2+1/2)\) prove the middle formula.

**5. Global variance asymptotics.** The previous formulas give \(q_j=p_j^2v_j\) asymptotic, respectively, to
\[
 cj^{-a},\quad
\frac{c^3}{c^2+1/2}j^{-1/2},\quad
\frac{c^3}{1-a}j^{1-3a}.
\]
In particular \(Q<\infty\) exactly when \(a>2/3\). The total-path-length identity can be rewritten
\[
T_n-\mathbb ET_n=n\sum_{j\le n}p_j(1-j/n)\xi_j+\sum_{j\le n}\xi_j.
\]
In every regime the second term has variance \(\sum_{j\le n}v_j=O(n^{1+\max(a,1-a)})=o(n^2)\); the covariance cross term is negligible by Cauchy–Schwarz. When \(a<2/3\), the weighted Riemann-sum rule applied to \(q_j\) gives
\[
\sum_{j\le n}q_j(1-j/n)^2
\sim K n^{\gamma+1}\int_0^1t^\gamma(1-t)^2dt,
\]
with the corresponding \(q_j\sim K j^\gamma\) and \(\gamma>-1\). At \(a=2/3\), \(q_j\sim3c^3/j\) and this weighted sum is \(3c^3\log n+o(\log n)\). For \(a>2/3\), dominated convergence yields the limit \(Q\). Multiplying by \(n^2\) gives each stated variance asymptotic. This also proves the sharpness of both exponents.

## Verification
A self-contained Python program `verify.py` enumerates 6,104 recursive-tree configurations over 35 rational attachment-probability input sequences, checking exactly (as rational numbers) the total-path-length mean and variance against the recurrence for every tree through seven vertices. It additionally evaluates the variance recurrence for a realizable family \(p_j=c/(j^a+c)\) at \(n=300000\) at five representative exponents. The latter are **finite-scale illustrations**, not certificates for the infinite asymptotics; convergence of normalized constants can be slow near the thresholds. Run `python3 verify.py` with a standard Python 3 installation. The infinite criteria and leading constants are proved above, not inferred from experiments.

## Relationship to prior work
Gałązka and Wdowicka [1] establish the exact path-length innovation representation and variance recurrence, and prove linear-scale almost-sure and quadratic-mean convergence when \(p_j=O(1/j)\). Their discussion explicitly asks for a characterization of more general deterministic weights admitting a linear-scale limit. The present theorem uses their identities but replaces that sufficient condition by a **necessary-and-sufficient innovation-energy criterion**, and resolves an explicit class with superpolynomial total-weight growth and two variance transitions. It does not claim novelty for the original identities, classical martingale convergence, or standard regular-variation sums. Sénizergues [2] develops weighted-tree geometric and profile results; Mailler and Uribe Bravo [3] study related weighted-tree depth scales. Those contexts motivate checking aliases but do not constitute evidence that their uninspected sections lack implicit equivalent claims.

## Limitations
The result concerns positive deterministic label-based attachment weights with independent parent choices, not adaptive random weights or preferential attachment using evolving degrees. It characterizes joint almost-sure-and-\(L^2\) convergence to the specified martingale limit; it does not classify possible non-\(L^2\) almost-sure limits when \(Q=\infty\), nor prove a central limit theorem under the larger variance scales. The explicit constants require \(p_j\sim cj^{-a}\) and \(0<a<1\). A complete historical uniqueness claim is not asserted; implicit deductions from broader profile or martingale literature remain possible. The proof and finite tests have not undergone independent audit.

## References
[1] M. Gałązka and H. Wdowicka, *Total Path Length in Power-Weight Recursive Trees: Martingale Limits and Global Fluctuations*, arXiv:2610.00614v1, publicly submitted 2026-09-30, especially §§5, 6 and 10. https://arxiv.org/html/2610.00614v1

[2] D. Sénizergues, *Geometry of weighted recursive and affine preferential attachment trees*, arXiv:1904.07115 (2019). https://arxiv.org/abs/1904.07115

[3] C. Mailler and G. Uribe Bravo, *Random walks with preferential relocations and fading memory: a study through random recursive trees*, arXiv:1810.02735 (2018). https://arxiv.org/abs/1810.02735

[4] M. Pain and D. Sénizergues, *Height of weighted recursive trees with sub-polynomially growing total weight*, arXiv:2204.05908 (2022). https://arxiv.org/abs/2204.05908
