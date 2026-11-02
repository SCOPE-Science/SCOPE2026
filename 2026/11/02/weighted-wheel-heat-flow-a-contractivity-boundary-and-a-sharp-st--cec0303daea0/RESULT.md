# Weighted wheel heat flow: a contractivity boundary and a sharp star-limit amplification envelope

## Finding
Let \(m\ge5\) be an integer. Form the wheel \(W_m=K_1\vee C_m\), with hub \(h\) and cyclic rim vertices \(v_0,\ldots,v_{m-1}\). Every spoke has heat conductance \(r>0\); every rim edge has heat conductance \(1\). All edges, irrespective of conductance, have unit length in the graph shortest-path metric. Let \(L_{m,r}\) be the unnormalized, counting-measure Laplacian and \(H_t=\exp(-tL_{m,r})\). Write
\[
 \operatorname{Lip}(f)=\max_{uv\in E(W_m)}|f(u)-f(v)|,
 \qquad \Lambda_{m,r}(t)=\sup_{\operatorname{Lip}(f)>0}
 \frac{\operatorname{Lip}(H_tf)}{\operatorname{Lip}(f)}.
\]

**Sharp contractivity classification.** The inequality \(\Lambda_{m,r}(t)\le1\) for **every** \(t\ge0\) holds precisely in the following cases:

* \(m=5\) and arbitrary \(r>0\);
* \(6\le m\le9\) and \(0<r\le 2/(m-5)\).

For \(m\ge10\), every \(r>0\) produces \(\Lambda_{m,r}(t)>1\) at some arbitrarily small positive times. Thus increasing the rim size causes a transition from a positive contractive conductance interval to **no** positive contractive spoke conductance at all. In particular, the first unit-conductance wheel in this family to exhibit amplification has \(m=8\) rim vertices (nine vertices altogether).

**Exact sharp conductance envelope.** Put
\[
 F_m(s)=\left(2-\frac4m\right)e^{-s}
          -\left(1-\frac4m\right)e^{-(m+1)s}\qquad(s\ge0).
\]
Then, for every \(r>0\), \(t\ge0\),
\[
 \Lambda_{m,r}(t)\le F_m(rt),
 \qquad
 \lim_{r\to\infty}\Lambda_{m,r}(s/r)=F_m(s)
 \quad\text{for each fixed }s\ge0.
\]
For \(m=5\), the sharp supremum over all \(r>0\) and \(t\ge0\) equals \(1\). For every \(m\ge6\), define
\[
 s_m=\frac1m\log\!\left(\frac{(m+1)(m-4)}{2(m-2)}\right),
 \qquad
 C_m=\frac{2(m-2)}{m+1}
 \left(\frac{2(m-2)}{(m+1)(m-4)}\right)^{1/m}.
\]
Then \(s_m>0\) and
\[
 \boxed{\sup_{r>0,\,t\ge0}\Lambda_{m,r}(t)=C_m>1.}
\]
The positive-time supremum for fixed \(m\ge6\) is **not attained** at any finite spoke conductance; it is approached with \(r\to\infty\) and \(t=s_m/r\). Moreover,
\[
 \boxed{\lim_{m\to\infty}C_m=2,\qquad
 \sup_{m\ge5,\,r>0,\,t\ge0}\Lambda_{m,r}(t)=2,}
\]
where the final supremum is not attained for finite \(m,r,t\). The exact expression is a sharp *across-conductances* envelope, **not** a formula asserting equality for the finite-conductance norm at each time.

## Assumptions and scope
All functions are real valued on the \(m+1\) vertices. The hub and rim vertices carry counting measure; the Laplacian is \((Lf)(u)=\sum_{v\sim u}c_{uv}(f(u)-f(v))\). The rim-cycle edges have conductance exactly one and the spokes have the common positive conductance \(r\). The metric is the unweighted shortest-path metric, independent of the conductances. Because an edgewise unit bound is equivalent to a graph-Lipschitz bound, no nonedge constraints need to be added. Constants are factored out when defining the operator seminorm.

## Proof
**1. A complete extremal calculation at a spoke.** Orient a spoke from the hub to \(v_0\). Normalize \(f(h)=0\), \(f(v_0)=-1\), \(\operatorname{Lip}(f)\le1\), and let \(x_i=f(v_i)\). Then \(-1\le x_i\le1\), and \(|x_i-x_{i+1}|\le1\) cyclically. Set \(S=\sum_i x_i\) and \(T=x_1+x_{m-1}\). The tight-spoke difference \(H_tf(h)-H_tf(v_0)\) equals \(1\) at time zero, with derivative
\[
 \left.\frac{d}{dt}\right|_{t=0}
 \{H_tf(h)-H_tf(v_0)\}=rS-r-2-T.
 \tag{1}
\]
Because \(x_0=-1\), its two neighbors lie in \([-1,0]\), so \(-2\le T\le0\). The two next-nearest rim values are at most \(1+x_1\) and \(1+x_{m-1}\), respectively, and all remaining \(m-5\) values are at most \(1\). These are distinct positions when \(m\ge5\). Consequently
\[
 S\le-1+T+(2+T)+(m-5)=m-4+2T.
\]
Substituting into (1) yields
\[
 rS-r-2-T\le r(m-5)-2+(2r-1)T.
\]
For \(r\ge1/2\), the maximum is therefore \(r(m-5)-2\), attained by the cyclic rim word having \(x_0=-1\), both neighbors \(0\), and every remaining entry \(1\). For \(0<r\le1/2\), the maximum is \(r(m-9)\), attained by the cyclic rim word with \(x_0=x_1=x_{m-1}=-1\), \(x_2=x_{m-2}=0\), and all other entries \(1\). Both words satisfy every rim-edge Lipschitz constraint (also for \(m=5\)). Hence the **exact** largest tight-spoke derivative is
\[
 \boxed{\sigma_m(r)=\max\{r(m-9),\ r(m-5)-2\}.}
 \tag{2}
\]
Negating a potential handles the opposite spoke orientation.

**2. From the local calculation to all-time contractivity.** On a tight rim edge, the spoke part of the generator contributes derivative \(-r\) to the oriented difference. The rim-cycle part contributes at most zero: its heat flow is a convex average of cyclic shifts, so it is contractive in the cyclic edge-Lipschitz seminorm. Thus no tight rim edge can have positive instantaneous derivative. By (2), no tight spoke can have positive derivative precisely when \(\sigma_m(r)\le0\).

For completeness, the infinitesimal criterion is sufficient on this finite graph without invoking an external curvature theorem. For any \(f\), the function \(t\mapsto\operatorname{Lip}(H_tf)\) is the maximum of finitely many absolute analytic edge differences. Its upper right derivative at any time is the maximum of the derivatives of its presently active signed edges. If every norm-one tight edge derivative is nonpositive, rescaling \(H_tf\) at that time shows this upper derivative is nonpositive everywhere; hence the Lipschitz seminorm never increases. Conversely, if \(\sigma_m(r)>0\), an explicit maximizing potential from Step 1 has an initially increasing unit spoke difference, proving \(\Lambda_{m,r}(t)>1\) for all sufficiently small \(t>0\).

Solving \(\sigma_m(r)\le0\) produces the claimed cases: for \(m=5\) both branches are negative; for \(6\le m\le8\), the constraint is \(r\le2/(m-5)\); for \(m=9\), one branch is identically zero and the same bound applies; for \(m\ge10\), the branch \(r(m-9)\) is positive for every \(r>0\). In the unit-spoke case \(r=1\), amplification first occurs at \(m=8\).

**3. Commuting star and rim heat flows.** Let \(L_\star\) be the unit-conductance star Laplacian on the same vertex set, and \(L_\circ\) the unit-conductance rim-cycle Laplacian acting as zero on the hub. Then
\[
 L_{m,r}=rL_\star+L_\circ,
 \qquad [L_\star,L_\circ]=0,
 \qquad H_t=e^{-rtL_\star}e^{-tL_\circ}.
\]
The commutator vanishes because \(L_\circ\) kills the constant rim vector and \(L_\star\) is scalar on the rim zero-sum subspace. The operator \(e^{-tL_\circ}\) is wheel-Lipschitz contractive: it averages rim values within the fixed interval \([f(h)-1,f(h)+1]\), while cyclic convolution cannot increase any rim-edge difference. Thus
\[
 \Lambda_{m,r}(t)\le\|e^{-rtL_\star}\|_{\mathrm{Lip}\to\mathrm{Lip}}.
 \tag{3}
\]

**4. Exact star norm measured in the wheel metric.** Let \(s\ge0\), \(A=e^{-(m+1)s}\), and \(B=e^{-s}\). After setting \(f(h)=0\) and writing \(\bar x=m^{-1}\sum_i x_i\), star heat gives
\[
 (e^{-sL_\star}f)(h)-(e^{-sL_\star}f)(v_i)
 =-B x_i+(B-A)\bar x.
 \tag{4}
\]
For a fixed \(x_i=a\in[-1,1]\), this right side is maximized by making every other rim value as large as constraints allow. When \(-1\le a\le0\), its two neighbors are at most \(a+1\), and all remaining rim vertices are at most one; these upper bounds can be achieved simultaneously. Consequently \(\bar x\le(3a+m-1)/m\). When \(0\le a\le1\), the corresponding bound is \(\bar x\le(a+m-1)/m\). On either interval, the resulting right side of (4) is strictly decreasing in \(a\), since its slopes are \(-B+3(B-A)/m<0\) and \(-B+(B-A)/m<0\), respectively. The unique maximizer at \(s>0\), up to wheel rotations, is therefore
\[
 x_i=-1,\qquad x_{i-1}=x_{i+1}=0,
 \qquad x_j=1\quad\text{at all remaining rim vertices}.
\]
Its mean is \((m-4)/m\), giving exactly \(F_m(s)\). The opposite orientation follows by negation. A rim edge under star heat has difference multiplied by \(B\), which is no larger than \(F_m(s)\), because
\[
 F_m(s)-B=(1-4/m)(B-A)\ge0.
\]
Therefore \(\|e^{-sL_\star}\|_{\mathrm{Lip}\to\mathrm{Lip}}=F_m(s)\), proving the upper bound in the finding.

**5. Sharpness, nonattainment, and the limit.** For fixed \(m,s\), take \(t=s/r\) and let \(r\to\infty\) in the commuting factorization: \(e^{-(s/r)L_\circ}\to I\) while the star factor stays \(e^{-sL_\star}\). The finite-dimensional operator norm is continuous, so \(\Lambda_{m,r}(s/r)\to F_m(s)\).

At \(s>0\), the star extremizer from Step 4 is unique in each spoke orientation. For \(t>0\), the rim heat kernel has strictly positive entries, so a nonconstant rim input whose values lie in \([-1,1]\) is mapped to values strictly between its original minimum and maximum. It cannot produce the extremal spoke pattern containing both \(-1\) and \(1\). A constant rim input cannot produce it either. Also, a rim edge has star norm \(B<F_m(s)\). Hence the inequality in (3) is strict at finite \(r,t>0\), and positive-time envelope maxima are unattained at finite conductance.

Finally, \(F_m(0)=1\) and \(F_m'(0)=m-5\). For \(m=5\), the derivative is strictly negative for every \(s>0\), giving supremum one. For \(m\ge6\), the derivative has exactly one positive zero at \(s_m\), by solving \(e^{-ms}=2(m-2)/((m+1)(m-4))\). This is its strict global maximum; substitution yields \(C_m\). Its formula gives \(C_m<2\) at every finite \(m\) and \(C_m\to2\) as \(m\to\infty\), completing the proof.

## Verification
The companion executable `verify_wheel_heat.py` uses only the Python standard library. It exhaustively checks the sharp derivative formula at six exact rational conductances for each of \(m=5,\ldots,10\). Exhaustiveness for each finite test follows from integrality of the graph-Lipschitz polytope: after fixing the hub to zero, edge-difference inequalities are a network-matrix system with integer bounds, so all vertices have integer coordinates in \(\{-1,0,1\}\).

The same program independently constructs heat kernels by uniformization of the continuous-time Markov generator, compares the full and commuting-factor heat kernels, and checks finite-time Lipschitz norms by direct optimization over every integral extreme potential at selected sizes and conductances. It also checks the peak expression and convergence toward two. Execution:

`python3 verify_wheel_heat.py`

These are finite corroborating calculations. The all-parameter assertion and limiting envelope are proved in the five analytic steps above, not inferred from a finite numerical census.

## Relationship to prior work
Ollivier's 2007/2009 transport-curvature theory gives the conceptual Lipschitz/transport-contraction setting. Münch and Wojciechowski's 2017 work gives a general Laplacian curvature formula and a semigroup Lipschitz characterization on weighted graphs; the present finding evaluates the relevant extremal functional for a specified wheel family and adds an exact across-conductances, finite-time amplification envelope. Chen, Lin, Liu and You (2025) classify positive Lin–Lu–Yau curvature on generalized Halin graphs and explicitly include wheels, but their wheel computation uses the **degree-normalized** Laplacian and the corresponding transition kernel, not the unnormalized, counting-measure conductance model used here. A result about positive normalized curvature is not an implication for this distinct generator. The wheel family is canonical, but the specific threshold formula, sudden failure of all contractive conductances at \(m=10\), and exact attained-in-the-limit envelope were not found in these inspected sources.

## Limitations
No pointwise closed formula for \(\Lambda_{m,r}(t)\) at every finite \(r,t\) is asserted. The sharp envelope is over varying spoke conductance for each fixed rim size. The result requires the equal positive spoke conductance, unit rim conductance, real functions, unweighted graph distance, and the unnormalized Laplacian. It does not assert corresponding results for normalized generators, nonuniform spoke weights, general Halin graphs, or graph metric edges whose lengths change with conductance. Absence of an equivalent unindexed computation from the literature is not certified.

## References
1. Y. Ollivier, *Ricci curvature of Markov chains on metric spaces*, first arXiv submission 2007-01-30, arXiv:math/0701886, later Journal of Functional Analysis 256 (2009), 810–864. https://arxiv.org/abs/math/0701886
2. F. Münch and R. K. Wojciechowski, *Ollivier Ricci curvature for general graph Laplacians: Heat equation, Laplacian comparison, non-explosion and diameter bounds*, arXiv:1712.00875 (2017). https://arxiv.org/abs/1712.00875
3. K. Chen, H. Lin, S. Liu and Z. You, *Halin graphs with positive Lin–Lu–Yau curvature*, arXiv:2505.04470 (2025). https://arxiv.org/abs/2505.04470
