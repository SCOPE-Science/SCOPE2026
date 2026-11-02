# Sharp compact-recurrence boundary and ballistic drift corridor for a cosine-memory map

## Finding

For the two-dimensional cosine-memristor map introduced by Zhang, Liu, Wei, Jiang, Lyu and Bi, an exact coefficient threshold separates universal escape from the possibility of compact recurrent motion. On the full real plane, set
\[
 F(x,y)=(a+bc\cos(dy)x,\ y+ex),\qquad r=|bc|,
\]
where \(a,b,c,d,e\) are nonzero real parameters. Then:

1. If \(0<r<1\), every forward trajectory has bounded first coordinate and its second coordinate escapes ballistically. For every initial state,
\[
 \frac{1}{1+r}\le\liminf_{N\to\infty}\frac{y_N-y_0}{aeN}
 \le\limsup_{N\to\infty}\frac{y_N-y_0}{aeN}
 \le\frac{1}{1-r}.
\]
Both endpoint constants are optimal across admissible coefficients, even among trajectories whose first coordinate is constant.

2. If \(r=1\), no bounded forward trajectory exists. In fact, whenever \(0<r\le1\), the map has no compactly supported invariant probability measure, hence no periodic point or nonempty compact invariant set in the plane.

3. If \(r>1\), every compactly supported invariant probability measure \(\mu\) satisfies the exact identity
\[
 a^2=(r^2-1)\int x^2\,d\mu-r^2\int x^2\sin^2(dy)\,d\mu,
\]
so \(\int x^2\,d\mu\ge a^2/(r^2-1)\). Every primitive period-two orbit has opposite first coordinates of magnitude at least \(|a|/(r-1)\). For each \(r>1\) an admissible map has an explicit period-two orbit attaining the latter bound. Thus \(r=1\) is the sharp boundary **for parameter-uniform impossibility versus possible compact recurrence**; existence above it is not asserted for every choice of the remaining parameters.

## Assumptions and scope

The domain is \(\mathbb R^2\), not a quotient cylinder. The second coordinate \(y\) is **not** reduced modulo a period; an orbit may be stationary after such reduction while escaping to infinity in the plane. All five coefficients are nonzero real constants and \(r=|bc|>0\). A forward trajectory satisfies \((x_{n+1},y_{n+1})=F(x_n,y_n)\) for \(n\ge0\). A compactly supported invariant probability is a Borel probability on the plane with compact support and \(F_*\mu=\mu\). A period-two orbit is a two-point orbit of least period two, not a fixed point of the quotient dynamics.

The map is continuous. It has no fixed point: \(y'=y\) forces \(ex=0\), hence \(x=0\), whereas \(x'=a\ne0\).

## Proof

**A. The exact stationary-square balance.** Let \(\mu\) be any compactly supported invariant probability measure. From \(y'-y=ex\) and stationarity,
\[
 \int x\,d\mu=0.
\]
Using \(x'-a=bc\cos(dy)x\), stationarity, and the preceding mean identity gives
\[
 \begin{aligned}
 r^2\int x^2\cos^2(dy)\,d\mu
 &=\int(x'-a)^2\,d\mu\\
 &=\int x^2\,d\mu+a^2.
 \end{aligned}
\]
Rearrangement yields the exact identity in the finding. If \(r\le1\), its right side is nonpositive while \(a^2>0\), a contradiction. Thus no such measure exists. Any bounded forward orbit of a continuous map on the plane generates, by weak accumulation of its empirical probability measures on its compact orbit closure, a compactly supported invariant probability. Hence no bounded forward orbit exists for \(r\le1\). Likewise a nonempty compact forward-invariant set has an invariant probability, so none exists.

For \(r>1\), dropping the nonnegative sine integral yields the stated root-mean-square lower bound. In particular, as \(r\downarrow1\) with \(|a|\) bounded away from zero, no compact recurrent set can remain inside any fixed horizontal strip \(|x|\le M\), since any invariant probability on such a set would violate the bound.

**B. A complete escape-speed corridor for \(r<1\).** Write \(u_n=x_n/a\) and \(\kappa_n=bc\cos(dy_n)\). The scalar recursion is
\[
 u_{n+1}=1+\kappa_nu_n,\qquad |\kappa_n|\le r<1.
\]
Consequently
\[
 |u_n|\le r^n|u_0|+\frac{1-r^n}{1-r},
\]
so \((u_n)\) is bounded. For \(N\ge1\), let \(m_N=N^{-1}\sum_{n=0}^{N-1}u_n\) and \(q_N=N^{-1}\sum_{n=0}^{N-1}u_n^2\). Since \((u_{n+1}-1)^2\le r^2u_n^2\), summation and exact telescoping give
\[
 (1-r^2)q_N-2m_N+1
 \le\frac{(u_0-1)^2-(u_N-1)^2}{N}=O(N^{-1}).
\]
The remainder is uniform in \(N\) for any fixed initial state. Jensen's inequality \(q_N\ge m_N^2\), with \(1-r^2>0\), implies
\[
 (1-r^2)m_N^2-2m_N+1\le O(N^{-1}).
\]
Its limiting zero set is the interval bounded by the two exact roots \(1/(1+r)\) and \(1/(1-r)\). Therefore every accumulation point of \(m_N\) lies in that interval. Finally,
\[
 \frac{y_N-y_0}{aeN}
 =\frac1N\sum_{n=0}^{N-1}u_n=m_N,
\]
which proves the claimed corridor and the linear escape of \(y_N\) in the direction of \(ae\).

Both bounds are sharp. For any fixed \(0<r<1\), take \(a=c=d=1\) and \(b=r\). For the lower endpoint, choose \(e=2\pi(1+r)\) and initial state \((x_0,y_0)=(1/(1+r),\pi)\). It gives \(x_n=1/(1+r)\) and \(y_n=\pi+2\pi n\). For the upper endpoint, choose \(e=2\pi(1-r)\) and initial state \((1/(1-r),0)\); then \(x_n=1/(1-r)\) and \(y_n=2\pi n\). The first-coordinate phase-locking follows from \(\cos(y_n)=\mp1\), respectively. These are drifting trajectories, not periodic points in the plane.

**C. The sharp period-two amplitude barrier.** Let \((x_0,y_0)\mapsto(x_1,y_1)\mapsto(x_0,y_0)\) be a primitive two-cycle. Summing the two \(y\)-increments gives \(e(x_0+x_1)=0\), hence \(x_1=-x_0\). Because \(a\ne0\), the first coordinate is nonzero. Put \(B_j=bc\cos(dy_j)\), so \(|B_j|\le r\). The two \(x\)-equations read
\[
 a=-(1+B_0)x_0=(1+B_1)x_0,
 \qquad B_0+B_1=-2.
\]
In particular, \(r\ge1\), and from part A necessarily \(r>1\). Since \(B_1\ge-r\), the sum equation yields \(B_0\le r-2\). Together with \(B_0\ge-r\), this gives
\[
 1-r\le1+B_0\le r-1,
 \qquad |x_0|=\frac{|a|}{|1+B_0|}\ge\frac{|a|}{r-1}.
\]
The same holds for \(|x_1|\).

To show **exact sharpness and realizability** for every \(r>1\), set
\[
 \theta=\arccos(1-2/r)\in(0,\pi),\qquad
 a=c=d=1,\quad b=r,\quad e=(r-1)(\pi-\theta).
\]
The two distinct points
\[
 P=\left(\frac1{r-1},\pi\right),\qquad
 Q=\left(-\frac1{r-1},2\pi-\theta\right)
\]
form an exact two-cycle: \(\cos\pi=-1\), \(\cos(2\pi-\theta)=1-2/r\), and the chosen \(e\) makes the second-coordinate increments cancel. Their amplitude equals \(1/(r-1)\), attaining the universal bound. The example establishes existence, not attraction or nonlinear stability.

## Verification

The accompanying standalone file `checker.py` uses symbolic polynomial identities and high-precision trigonometric evaluation. It checks both branches of the explicit two-cycle at eight values of \(r>1\), both sharp ballistic examples across five values of \(0<r<1\) for twelve steps per endpoint, and twenty long finite-trajectory drift comparisons with independent initial conditions. It also checks the factorization of the quadratic drift constraint. All tests passed. The infinite conclusions, the universal boundary, and the lack of bounded orbits follow from parts A–C, not from finite sampling. Reproduce with `python checker.py`; SymPy and mpmath are dependencies.

## Relationship to prior work

Zhang et al., *Chinese Physics B* **31** (2022), 100503, introduce exactly this cosine-memory map and report numerical bifurcations, hidden periodic orbits, and escape regions. Their explicit fixed-point test establishes only the absence of equilibria, which does not exclude compact periodic or chaotic motion. The inspected mathematical and numerical sections do not state a coefficient-uniform compact-recurrence obstruction, exact drift interval, stationary-square balance, or sharp period-two amplitude barrier.

Ramadoss et al., *European Physical Journal Plus* **137** (2022), 211, establish a more general memristor-map construction \((x',y')=(\alpha M(y)x+c,y+x)\) and report numerical dynamics for several examples, including a cosine term combined with additional linear feedback. That general model can include a rescaled version of the present map, but its published fixed-point criterion and examples do not imply the present universal orbit-escape conclusions. Other published exact periodic-orbit and stationary-moment results for different maps do not dominate a statement about this specific nonlinear recursion.

## Limitations

The recurrence boundary \(r=1\) is sharp in the sense that no parameter choices admit bounded orbits for \(r\le1\), whereas examples admit a two-cycle for every \(r>1\); it does **not** assert the existence of a cycle for every fixed choice of \(a,d,e\) above the threshold. The two-cycle example is not claimed to attract an open basin. The mean-square estimate is a necessary condition, not a sufficient condition for compact recurrence. The speed corridor requires \(r<1\); the endpoint \(r=1\) only has the proved nonexistence of bounded forward orbits. On a quotient cylinder, drifting trajectories can become periodic, so the full-plane scope is essential. Publication-priority comparison is limited to inspected sources and available research indexes; an unindexed prior calculation could overlap. Independent mathematical validation has not been performed.

## References

1. L.-P. Zhang, Y. Liu, Z.-C. Wei, H.-B. Jiang, W.-P. Lyu, Q.-S. Bi, “Extremely hidden multi-stability in a class of two-dimensional maps with a cosine memristor,” *Chinese Physics B* **31** (2022), 100503, DOI: https://doi.org/10.1088/1674-1056/ac7294. The accepted manuscript was online by 2022-05-24; publisher rich HTML: https://cpb.iphy.ac.cn/fileCPB/journal/article/cpb/html/2022/1674-1056/cpb_31_10_100503.shtml.
2. J. Ramadoss, A. Ouannas, V. K. Tamba, G. Grassi, S. Momani, V.-T. Pham, “Constructing non-fixed-point maps with memristors,” *European Physical Journal Plus* **137** (2022), 211, DOI: https://doi.org/10.1140/epjp/s13360-022-02433-z.
