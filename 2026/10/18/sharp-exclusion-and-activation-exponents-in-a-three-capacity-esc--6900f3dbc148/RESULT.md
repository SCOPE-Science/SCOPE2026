# Sharp exclusion and activation exponents in a three-capacity escort biodiversity benchmark

## Finding
Fix three formally admissible species with distinct capacity scores \(\Lambda=(0,1,2)\). For \(q>0\), choose a probability vector \(p=(p_0,p_1,p_2)\) to maximize Hill diversity of order \(q\) subject to the escort capacity mean \(b\in[0,2]\):
\[
D_q(p)=\left(\sum_{i=0}^2p_i^q\right)^{1/(1-q)},\qquad
b=\frac{p_1^q+2p_2^q}{p_0^q+p_1^q+p_2^q}\quad(q\ne1).
\]
At \(q=1\), use \(D_1(p)=\exp(-\sum_i p_i\log p_i)\) and \(b=p_1+2p_2\); take \(0\log0=0\). There is exactly one optimizer \(p^*(q,b)\) for every such order and budget.

For \(0<q<1\), put
\[
B(q)=\frac{1}{1+2^{q/(1-q)}}.
\]
The optimizer has support \(\{0,1\}\) for \(0<b\le B(q)\), support \(\{0,1,2\}\) for \(B(q)<b<2-B(q)\), and support \(\{1,2\}\) for \(2-B(q)\le b<2\). At \(b=0\) or \(2\) the unique optimizer is the corresponding extreme single species. In particular, the *third* species enters the benchmark precisely above \(b=B(q)\); the corresponding high-budget exclusion is its reflected counterpart. In contrast, for every \(q\ge1\) all three optimized abundances are positive whenever \(0<b<2\).

The activation of the formerly absent high-capacity species has an additional sharp order transition. For fixed \(0<q<1\), let \(\delta=b-B(q)\downarrow0\). There is a positive explicitly specified coefficient \(A_q\) for which
\[
p^*_2(q,B(q)+\delta)\sim A_q\,\delta^{\gamma(q)},\qquad
\gamma(q)=\begin{cases}1/q,&0<q\le1/2,\\1/(1-q),&1/2\le q<1.\end{cases}
\]
The expressions agree at \(q=1/2\). The activation exponent is minimized there, at \(\gamma(1/2)=2\), and diverges toward either endpoint \(q\downarrow0\) or \(q\uparrow1\). The low-capacity species exhibits the same exponent under reflection \(b\mapsto 2-b\).

## Assumptions and scope
The finite three-species simplex is closed and includes zero entries. The capacity scores \(0,1,2\) are an affine normalization of three equally spaced nonnegative capacities; they are not assumed to be empirical habitat measurements. The equality budget \(b\) is the escort average, not the ordinary mean when \(q\ne1\). The phrase 'species exclusion' means zero weight in the mathematical *maximum-potential benchmark*, not biological extinction or a dynamical species loss. The result covers every \(q>0\) and every feasible \(b\in[0,2]\), but not \(q=0\), unequal capacity spacings, or additional ecological constraints.

For the activation coefficient, write
\[
s=(1-q)/q,\quad k=2^{1/s},\quad b_0=(1+k)^{-1},\quad u_0=1-b_0,\quad Z_0=u_0^{1/q}+b_0^{1/q},
\]
\[
K=s\bigl(u_0^{s-1}+2b_0^{s-1}\bigr),\qquad
L=s\bigl(u_0^{s-1}+4b_0^{s-1}\bigr).
\]
Then \(A_q=C_q^{1/q}/Z_0\) with
\[
C_q=\begin{cases}
K/L,&0<q<1/2,\\
K/(L+1),&q=1/2,\\
K^{1/s},&1/2<q<1.
\end{cases}
\]
All these quantities are finite and positive for fixed \(0<q<1\).

## Proof
**Step 1 (escort convexification, including boundaries).** Define \(y_i=p_i^q/\sum_jp_j^q\). For \(q>0\) this is a homeomorphic bijection of the *closed* simplex with inverse
\[
p_i=\frac{y_i^{1/q}}{Z(y)},\qquad Z(y)=\sum_jy_j^{1/q}.
\]
The escort budget becomes \(y_1+2y_2=b\). Since \(\sum_i p_i^q=Z(y)^{-q}\), the diversity is
\[
D_q(p)=Z(y)^{q/(q-1)}.
\]
For \(0<q<1\), maximizing diversity is exactly minimizing the strictly convex function \(F(y)=\sum_i y_i^r\) with \(r=1/q>1\) over the compact line segment \(y\ge0\), \(\sum y_i=1\), \(y_1+2y_2=b\). For \(q>1\), it is maximizing strictly concave \(F\), with \(0<r<1\), over the same segment. The strictness on the convex segment proves uniqueness in each case. At \(q=1\), strict Shannon concavity proves uniqueness directly.

**Step 2 (full support for \(q\ge1\)).** For \(0<b<2\), the slice contains a strictly positive feasible vector: choose a small positive middle/upper weight and adjust the remaining weights. If \(q>1\), the derivative of \(y^r\) at zero is \(+\infty\), so moving any boundary candidate toward a positive feasible point increases \(F\) by order \(\epsilon^r\) while changing the positive coordinates by \(O(\epsilon)\). Thus the unique maximizer of \(F\) has full support. For \(q=1\), replacing \(y^r\) by \(-\sum p_i\log p_i\), the gain \(-\epsilon\log\epsilon\) likewise forces full support. At \(b=0\) and \(2\), feasibility forces the respective extreme point.

**Step 3 (global active-set classification for \(0<q<1\)).** Write \(r=1+s\), \(s>0\). On a relative interior optimum, the KKT conditions for the strictly convex \(F\) read \(r y_i^s=\alpha+\beta i\) on positive coordinates and \(\alpha+\beta i\le0\) at zero coordinates. These conditions are necessary and sufficient, since the slice has a strictly feasible point for each \(0<b<2\). A positive affine sequence at both extreme capacity indices must also be positive in the middle, hence an optimum cannot have support \(\{0,2\}\). The other possible two-point faces are the adjacent faces \(\{0,1\}\) and \(\{1,2\}\).

On \(\{0,1\}\), the only feasible escort profile is \(y=(1-b,b,0)\). The first two KKT values extrapolate to \(\alpha+2\beta=r[2b^s-(1-b)^s]\). The boundary is optimal precisely when this is nonpositive, equivalently
\[
2b^s\le(1-b)^s\quad\Longleftrightarrow\quad b\le B(q).
\]
On \(\{1,2\}\), the only feasible profile is \(y=(0,2-b,b-1)\), and the corresponding unoccupied first-coordinate KKT condition is \(2(2-b)^s-(b-1)^s\le0\), equivalently \(b\ge2-B(q)\). A lone interior-capacity species is not optimal for \(b=1\), since it violates the strict KKT inequality; lone extreme species are feasible only at budget endpoints. Therefore, throughout the complement of the two boundary regimes, the unique minimizer is strictly positive on all coordinates. Its inverse escort gives the unique \(p^*\).

**Step 4 (critical onset exponent and coefficient).** Near the lower transition put \(b=b_0+\delta\), \(t=y_2\), so the feasible profile is
\[
y(t,b)=(1-b+t,\;b-2t,\;t).
\]
The interior stationarity equation \(\partial_t F=0\), after division by \(r\), is
\[
(1-b+t)^s-2(b-2t)^s+t^s=0.
\]
The solution satisfies \(t\to0\) by continuity of the unique strictly convex minimizer. Expanding only the two positive-base terms about \((t,b)=(0,b_0)\) gives
\[
0=-K\delta+Lt+t^s+o(\delta+t).
\]
The constants \(K,L>0\) are exactly those in the statement. If \(s>1\), \(t^s=o(t)\) and \(t\sim(K/L)\delta\). If \(s=1\), \(t=K\delta/(L+1)+o(\delta)\). If \(0<s<1\), \(t=o(\delta)\) and \(t^s\sim K\delta\), so \(t\sim (K\delta)^{1/s}\). These comparisons follow by monotonicity of the strictly convex first derivative and the positivity of \(L\). Finally \(p_2=t^{1/q}/Z(y)\) and \(Z(y)\to Z_0\), giving the coefficient and exponent. Reflection of coordinates \(0\leftrightarrow2\) sends \(b\) to \(2-b\) and proves the high-budget counterpart. This completes the proof.

## Verification
A standalone standard-library Python program in `verify_escort.py` checks the exact \(q=1/2\) solution over 199 rational budgets, checks the support regimes and KKT root solutions for 2,189 order/budget combinations, and tests the predicted leading activation coefficients across all three cases \(q<1/2\), \(q=1/2\), and \(q>1/2\). These finite checks are reproducible corroboration; the preceding analytic proof establishes all continuous-parameter and asymptotic statements.

For \(q=1/2\) the escort optimizer can be given in closed form:
\[
y^*(b)=\begin{cases}
(1-b,b,0),&0\le b\le1/3,\\
((5-3b)/6,1/3,(3b-1)/6),&1/3\le b\le5/3,\\
(0,2-b,b-1),&5/3\le b\le2.
\end{cases}
\]
Because \(D_{1/2}(p)=1/\sum_i y_i^2\), the maximum attainable Hill diversity is
\[
D_{1/2}^{\max}(b)=\begin{cases}
[(1-b)^2+b^2]^{-1},&0\le b\le1/3,\\
[1/3+(b-1)^2/2]^{-1},&1/3\le b\le5/3,\\
[(2-b)^2+(b-1)^2]^{-1},&5/3\le b\le2.
\end{cases}
\]
For example at \(b=1/4\), the unique potential abundance vector is \(p^*=(9/10,1/10,0)\), and \(D_{1/2}^{\max}=8/5\); the third species is excluded despite being admissible.

To reproduce, run `python verify_escort.py` using Python 3.9 or newer. It has no network or package dependencies.

## Relationship to prior work
Eguchi, *An information-geometric framework for mapping maximum potential biodiversity* (arXiv:2606.09906, first public 2026-06-06), supplies the ecological potential benchmark, escort capacity constraint, and formal truncated \(q\)-exponential stationary form (Sections 4.2 and 5.2). These general ingredients are not new. The present result determines the **global optimizer and exact active-set boundaries for the natural first nontrivial three-level capacity slice**, together with the previously unquantified order-dependent species-activation critical exponent and coefficient.

The reciprocal escort transformation and equivalence with an ordinary-mean Rényi optimization are established in Bercher, *Escort entropies and divergences and related canonical distribution* (arXiv:1109.3311, Section 2.3). Here that existing duality is used rather than claimed as original. Eguchi, *Information Geometry for Maximum Diversity Distributions* (arXiv:2412.03835, Section 3), studies the distinct ordinary linear-mean capacity constraint; in particular its full-support regime for low diversity order is not the escort-constrained active-set phase diagram derived here. The familiar Gibbs distribution at \(q=1\) is also prior mathematics.

## Limitations
The characterization is for an **exact equality** escort constraint and three equally spaced capacity scores, not for arbitrary uneven scores or inequality budgets. A zero weight belongs only to an *optimization benchmark*; no population-dynamic invasion, local extinction, empirical utility, or biological selection conclusion follows. The activation exponent is a fixed-\(q\), one-sided \(\delta\downarrow0\) statement; it is not a uniform joint limit in \(q\) and \(b\). Historical and recent work on Tsallis/Rényi maximum entropy already implies generic power-law stationary forms, so the originality rests on the **specific exact phase diagram and critical onset classification**, not on introducing escort measures or power-law solutions. Independent validation and exhaustive knowledge of unindexed literature are not claimed.

## References
1. S. Eguchi, *An information-geometric framework for mapping maximum potential biodiversity*, arXiv:2606.09906, first posted 2026-06-06, https://arxiv.org/abs/2606.09906.
2. S. Eguchi, *Information Geometry for Maximum Diversity Distributions*, arXiv:2412.03835, first posted 2024-12-05, https://arxiv.org/abs/2412.03835.
3. J.-F. Bercher, *Escort entropies and divergences and related canonical distribution*, arXiv:1109.3311, 2011, https://arxiv.org/html/1109.3311v1.
4. M. O. Hill, *Diversity and evenness: a unifying notation and its consequences*, Ecology 54 (1973), 427–432, https://doi.org/10.2307/1934352.
