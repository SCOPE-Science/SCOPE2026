# Exact threshold for alternating herd immunity under perfect vaccine efficacy

## Finding

In the deterministic annual vaccination-decision map of Papst, O'Keeffe, and Strogatz [1], specialize to perfectly effective vaccination, positive vaccine morbidity, and a supercritical infection: vaccine-success probability \(s=1\), morbidity probability \(0<r<1\), and basic reproduction ratio \(R>1\). Let \(p_j\in[0,1]\) be vaccination coverage in year \(j\), and define the herd-immunity boundary \(p_c=1-1/R\). Set
\[
\Phi_R(q)=\begin{cases}0,&0\le q\le1/R,\\
\text{the unique positive solution of }\Phi=q(1-e^{-R\Phi}),&q>1/R.
\end{cases}
\]
The exact map is
\[
p_{j+1}=G_{R,r}(p_j)=(1-r)p_j+\Phi_R(1-p_j).
\]
Call a two-cycle *threshold-crossing* when its distinct elements obey \(0<p_-<p_c\le p_+<1\), and \(G(p_-)=p_+\), \(G(p_+)=p_-\).

Define the analytic inverse \(Y:(0,\infty)\to(0,\infty)\) by
\[
z=\frac{Y(z)}{1-e^{-Y(z)}}-1,
\qquad B(z)=\frac{2z-Y(z)}{z^2},\qquad z>0.
\]
Then \(B\) is strictly decreasing, \(\lim_{z\downarrow0}B(z)=2/3\), and \(\lim_{z\to\infty}B(z)=0\). Consequently there is a sharp cost threshold
\[
r_c(R)=\begin{cases}0,&1<R\le5/2,\\
\displaystyle\frac{z_c}{R-1},&R>5/2,\end{cases}
\]
where for \(R>5/2\) the **unique** \(z_c\in(0,R-1)\) solves \(B(z_c)=1/(R-1)\).

**Theorem.** A threshold-crossing two-cycle exists **if and only if** \(r\ge r_c(R)\). It is unique among threshold-crossing two-cycles. If \(r>r_c(R)\), it has \(p_-<p_c<p_+\) and is locally asymptotically stable, with its two-step multiplier strictly between \(-1\) and \(0\). If \(R>5/2\) and \(r=r_c(R)\), its upper state lies exactly at the nonsmooth herd boundary \(p_+=p_c\); no stability conclusion is made at that equality. When \(1<R\le5/2\), every \(0<r<1\) gives the strictly crossing, stable cycle.

The cost criterion can also be evaluated directly without finding the cycle:
\[
\Phi_R\!\left(\frac1R+r\left(1-\frac1R\right)\right)
\ \ge\ r(2-r)\left(1-\frac1R\right).
\]
For \(R>5/2\), this holds precisely for \(r\ge r_c(R)\). The result classifies these particular alternating-immunity cycles, not all possible attractors of the annual map.

## Assumptions and scope

The fraction vaccinated is \(p\in[0,1]\); the vaccine perfectly prevents infection for vaccinated individuals, with independent morbidity cost probability \(0<r<1\). In each year a negligible initial infectious seed drives the deterministic homogeneous SIR final-size law with reproduction ratio \(R>1\). At and above the herd boundary, the final size is assigned its nonoutbreak solution \(0\). Individuals follow the preceding year's success-or-failure heuristic of [1]. The theorem concerns the exact infinite-population map (not demographic or epidemic stochasticity), and quantifies one high-low period-two type by the inequality \(p_-<p_c\le p_+\).

The 2021 source [1] denotes the vaccine-success parameter by \(s\), vaccine morbidity by \(r\), and its disease reproduction number by \(\mathcal R_0\); we set \(s=1\), \(R=\mathcal R_0\). No other assumptions are added. The date of the public source is its arXiv version-one date, 2021-01-20.

## Proof

**1. Reduction to a one-dimensional crossing equation.** With \(s=1\), equation (3.7) of [1] simplifies exactly to \(G(p)=(1-r)p+\Phi_R(1-p)\). The SIR final size is positive precisely when \(1-p>1/R\), or equivalently \(p<p_c\). Thus any crossing cycle obeys
\[
p_-=(1-r)p_+,
\quad p_+=(1-r)p_-+\Phi_R(1-p_-).
\]
Writing \(v=p_+\), this is equivalent to the scalar zero equation
\[
F(v):=\Phi_R(1-(1-r)v)-r(2-r)v=0,\qquad p_c\le v\le1.
\]
The function \(q\mapsto\Phi_R(q)\) is continuous and nondecreasing, and strictly increasing on \((1/R,1]\). Hence \(F\) is continuous and strictly decreasing on \([p_c,1]\) because \(r(2-r)>0\). Moreover
\[
F(1)=\Phi_R(r)-r(2-r)<0,
\]
since \(0\le\Phi_R(r)\le r<r(2-r)\). Therefore there is precisely one such \(v\) when \(F(p_c)\ge0\), and none otherwise. At a zero, \(\Phi_R(1-(1-r)v)=r(2-r)v>0\), so automatically \(p_-=(1-r)v<p_c\). Also \(v<1\) from \(F(1)<0\). Since \(p_-<p_c\le v\), the orbit is genuinely period two.

**2. Universal inverse and the cost criterion.** Put \(q=1/R+t\), \(z=Rt>0\), and \(y=R\Phi_R(q)>0\). The final-size equation becomes \(y=(1+z)(1-e^{-y})\); equivalently,
\[
z=Z(y):=\frac{y}{1-e^{-y}}-1.
\]
For every \(y>0\), \(Z'(y)>0\). Explicitly,
\[
Z'(y)=\frac{e^y(e^y-1-y)}{(e^y-1)^2}>0.
\]
Also \(Z(0+)=0\) and \(Z(y)\to\infty\). Its inverse \(Y(z)\) is therefore globally well-defined and satisfies \(R\Phi_R(1/R+z/R)=Y(z)\). At the left endpoint \(v=p_c\), set \(z=r(R-1)\); then \(1-(1-r)p_c=1/R+z/R\), yielding the exact identity
\[
RF(p_c)=Y(z)-2z+\frac{z^2}{R-1}
=z^2\left(\frac1{R-1}-B(z)\right).
\]
Consequently existence is equivalent to \(B(r(R-1))\le1/(R-1)\).

**3. Shape and endpoints of \(B\).** Direct differentiation gives, for \(y>0\),
\[
Z''(y)=\frac{e^y[(y-2)e^y+y+2]}{(e^y-1)^3}>0
\]
and
\[
Z'''(y)=
-\frac{2e^{2y}[y(\cosh y+2)-3\sinh y]}{(e^y-1)^4}<0.
\]
For the first sign, define \(g(y)=(y-2)e^y+y+2\). We have \(g(0)=g'(0)=0\), and \(g''(y)=ye^y>0\). For the second sign, put \(h(y)=y(\cosh y+2)-3\sinh y\). Here \(h(0)=h'(0)=h''(0)=0\), and \(h'''(y)=y\sinh y>0\). Thus both asserted strict signs hold.

Differentiating the inverse relation \(Z(Y(z))=z\) therefore gives \(Y'(z)>0\), \(Y''(z)<0\), and
\[
Y'''(z)=\frac{3Z''(Y(z))^2-Z'(Y(z))Z'''(Y(z))}{Z'(Y(z))^5}>0.
\]
The expansion \(Z(y)=y/2+y^2/12+O(y^4)\) yields \(Y(z)=2z-2z^2/3+O(z^3)\). Furthermore,
\[
B(z)=\int_0^1(1-t)[-Y''(tz)]\,dt.
\]
Since \(-Y''\) is positive and strictly decreasing, \(B\) is positive and strictly decreasing, with limit \(2/3\) at zero. Since \(Z(y)=y-1+O(ye^{-y})\) as \(y\to\infty\), the inverse satisfies \(Y(z)=z+1+o(1)\), giving \(B(z)\to0\).

If \(1<R\le5/2\), then \(1/(R-1)\ge2/3>B(z)\) for every \(z>0\), so every positive cost yields strict crossing. If \(R>5/2\), the inequality fails for all sufficiently small positive \(z\). At \(z=R-1\) we have \(Y(z)>z\): this follows from \(Z(y)<y\), which is equivalent to the elementary strict inequality \(e^y>1+y\). Hence
\[
B(R-1)<\frac1{R-1}.
\]
By continuity and strict monotonicity there is exactly one \(z_c\in(0,R-1)\) with \(B(z_c)=1/(R-1)\), and the criterion holds exactly when \(z\ge z_c\). This proves the claimed sharp threshold.

**4. Local stability at strict crossings.** For \(q>1/R\), differentiation of the final-size relation, with \(y=R\Phi_R(q)>0\), gives
\[
\Phi_R'(q)=\frac{(1-e^{-y})^2}{1-(1+y)e^{-y}}=\frac1{Z'(y)}.
\]
The bound \(Z'(y)<1\) follows from \(e^y(y-1)+1>0\); the bound \(Z'(y)>1/2\) follows from \(Z''(y)>0\) and \(Z'(0+)=1/2\). Thus
\[
1<\Phi_R'(q)<2.
\]
At a strict crossing, the high state is epidemic-free and the low state has an outbreak. Hence
\[
G'(p_+)=1-r,\qquad G'(p_-)=1-r-\Phi_R'(1-p_-).
\]
The multiplier of the two-step return map is
\[
M=(1-r)[1-r-\Phi_R'(1-p_-)].
\]
The strict bounds above imply \(-(1-r^2)<M<-r(1-r)<0\), and in particular \(-1<M<0\). Standard one-dimensional hyperbolic fixed-point theory proves local asymptotic stability of this strict-crossing two-cycle. At \(p_+=p_c\) the map has a slope discontinuity, so this multiplier argument is not applied there.

## Verification

Run `python check_cycles.py` with `sympy` and `scipy` installed. The standalone checker reconstructs the final-size function using the strictly monotone inverse \(Z\), verifies the first three symbolic derivatives of \(Z\), computes critical morbidity for \(R=3,5,10\), and checks existence/nonexistence and negative-multiplier stability across 42 parameter pairs, along with 199 monotonicity comparisons for \(B\). Its finite computations are consistency checks; the proof above establishes the universal quantifiers.

Illustrative outputs include \(r_c(3)\approx0.2565052914448\), \(r_c(5)\approx0.6623715509410\), and \(r_c(10)\approx0.8728663770687\). At \(R=3\), \(r=1/2\), the computed crossing cycle is approximately \((p_-,p_+)=(0.344293083962,0.688586167924)\); at \(R=3\), \(r=1/4\), no crossing cycle exists. Each stated cycle was checked by two independent substitutions into the original annual map.

## Relationship to prior work

Papst, O'Keeffe, and Strogatz [1] introduce the annual behavioral vaccination map (their equation (3.7)) and describe biennial oscillations across the herd-immunity boundary for certain parameter choices (Section 4 and Figure 7). The cycle's general qualitative existence is **not** asserted here as new. Their Section 4 uses numerical iteration for positive morbidity; their Appendix derives explicit criteria for **zero** morbidity. Their inspected equation, positive-morbidity discussion, and Appendix do not state the perfect-efficacy sharp cost criterion, the \(R=5/2\) divide, or the multiplier bound proved here.

General SIR final-size relations and vaccination allocations were previously developed, e.g. [2,3]. These establish important epidemiological background but do not themselves analyze the repeated annual heuristic map in [1]. The new mathematical contribution is the all-parameter, exactly characterized existence and local stability of the threshold-crossing two-cycle in the natural perfect-efficacy slice, including the universal transition at \(R=5/2\). An equivalent earlier analysis under different terminology cannot be completely excluded.

## Limitations

The theorem is restricted to perfect vaccine efficacy \(s=1\), positive cost \(0<r<1\), and homogeneous deterministic infinitesimal-seed SIR seasons. It does not classify cycles entirely below the herd threshold, other periods, chaotic behavior, global basins of attraction, nor imperfect vaccination \(s<1\). It asserts local attraction only for strict crossings \(p_+>p_c\); the border case \(p_+=p_c\) is nonsmooth and is treated only for existence and uniqueness. Its threshold refers to yearly coverage crossing the herd boundary, not to guaranteed elimination of an infection in a stochastic population. Prior qualitative observations of biennial behavior remain fully credited to [1].

## References

[1] I. Papst, K. P. O'Keeffe, and S. H. Strogatz, *Modeling the interplay between seasonal flu outcomes and individual vaccination decisions*, arXiv:2101.07926v1, publicly submitted 2021-01-20; subsequently *Bulletin of Mathematical Biology* 84 (2022), article 36, DOI:10.1007/s11538-021-00988-z. Source: https://arxiv.org/abs/2101.07926.

[2] J. Arino, F. Brauer, P. van den Driessche, J. Watmough, and J. Wu, *A final size relation for epidemic models*, *Mathematical Biosciences and Engineering* 4 (2007), 159–175, DOI:10.3934/mbe.2007.4.159.

[3] M. J. Keeling and A. Shattock, *Optimal but unequitable prophylactic distribution of vaccine*, *Epidemics* 4 (2012), 78–85, DOI:10.1016/j.epidem.2012.03.001.
