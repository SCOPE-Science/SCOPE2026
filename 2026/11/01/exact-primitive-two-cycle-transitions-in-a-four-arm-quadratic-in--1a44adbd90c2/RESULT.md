# Exact primitive two-cycle transitions in a four-arm quadratic interval map

## Finding
Let \(N_2(p)\) be the number of **geometrically distinct primitive period-two orbits** of the continuous symmetric Lawnik–Berezowski map \(F_p:[0,1]\to[0,1]\), with \(1/4\le p\le1/2\), defined below. Put
\[
A(p)=4p^4+8p^3-2p^2-4p+1,\qquad
B(p)=4p^4-8p^3+6p^2-4p+1.
\]
Let \(\alpha\) be the unique zero of \(A\) in \((1/4,1-1/\sqrt2)\), and let \(\beta\) be the unique zero of \(B\) in \((1-1/\sqrt2,1/2)\). They satisfy
\[
\alpha=0.2548478862885574065\ldots,\quad
p_0=1-1/\sqrt2=0.2928932188134524755\ldots,\quad
\beta=0.3754808118008128342\ldots.
\]
Then the **complete** primitive two-cycle count is
\[
\boxed{
N_2(p)=\begin{cases}
6,&1/4\le p<\alpha,\\
5,&p=\alpha,\\
4,&\alpha<p<p_0,\\
3,&p_0\le p<\beta,\\
2,&p=\beta,\\
1,&\beta<p\le1/2.
\end{cases}}
\]
At \(\alpha\) and \(\beta\), two distinct primitive two-cycles merge into one cycle passing through the central corner \(1/2\); at \(p_0\), a primitive two-cycle collapses onto a fixed point at that corner. These are **all** changes in the primitive two-cycle count in the stated parameter range.

## Assumptions and scope
For real \(t\), define \(q_p(t)=2t/p-t^2/p^2\). For each real parameter \(p\in[1/4,1/2]\), define
\[
F_p(x)=\begin{cases}q_p(x),&0\le x\le1/2,\\q_p(1-x),&1/2\le x\le1.\end{cases}
\]
The two displayed branches agree at \(x=1/2\), and \(F_p([0,1])\subseteq[0,1]\). A primitive two-cycle is an unordered set \(\{x,y\}\subset[0,1]\), with \(x\ne y\), \(F_p(x)=y\), and \(F_p(y)=x\). This is a census of **real interval orbits**, not rounded or digitized states. It makes no claim about higher periods, global mixing, invariant densities or cryptographic security. Primary classification: MSC2020 37E05.

## Proof
**1. Only three parameters permit a change.** Let \(h(p)=F_p(1/2)=(4p-1)/(4p^2)\). This function increases from zero to one on the parameter interval and equals \(1/2\) exactly at \(p_0=1-1/\sqrt2\). A solution of \(F_p^2(x)=x\) can cross a nonsmooth seam only if \(x=1/2\), or if \(F_p(x)=1/2\). In both cases it must satisfy \(F_p(h(p))=1/2\), and the corresponding orbit is \(1/2\longleftrightarrow h(p)\). Exact substitution gives
\[
F_p(h(p))-\tfrac12=
-\frac{(2p^2-4p+1)A(p)}{16p^6}
\quad(p\le p_0),
\]
\[
F_p(h(p))-\tfrac12=
-\frac{(2p^2-4p+1)B(p)}{16p^6}
\quad(p\ge p_0).
\]
The first quartic is strictly decreasing on \([1/4,p_0]\): its second derivative is positive there, while \(A'(p_0)=68-50\sqrt2<0\). Its endpoint signs are opposite. The second has derivative \(B'(p)=4(p-1)(4p^2-2p+1)<0\) on \([p_0,1/2]\), also with opposite endpoint signs. Thus the sole possible seam parameters are \(\alpha,p_0,\beta\), and each is as described in the statement. The rational bounds \(0.25484<\alpha<0.25485\) and \(0.37548<\beta<0.37549\) follow by direct exact signs.

**2. No interior periodic root can be created or destroyed.** On a region where both \(x\) and \(F_p(x)\) lie on fixed sides \(L=[0,1/2]\), \(R=[1/2,1]\), the equation \(F_p^2(x)=x\), multiplied by \(p^6\), is one of four polynomial equations:
\[
\begin{aligned}
H_{LL}&=p^6(q_p(q_p(x))-x),&
H_{LR}&=p^6(q_p(1-q_p(x))-x),\\
H_{RL}&=p^6(q_p(q_p(1-x))-x),&
H_{RR}&=p^6(q_p(1-q_p(1-x))-x).
\end{aligned}
\]
Their discriminants with respect to \(x\) are, respectively,
\[
\begin{aligned}
\operatorname{disc}_x H_{LL}&=-p^{16}(p-2)^2(p+2)^3(3p-2)^3,\\
\operatorname{disc}_x H_{LR}&=\operatorname{disc}_x H_{RL}=-p^{19}J(p),\\
\operatorname{disc}_x H_{RR}&=-p^{20}(p+4)(3p-4)^3,
\end{aligned}
\]
where \(J(p)=27p^5+288p^3-288p^2+512p-256\). Since
\[
J'(p)=135p^4+864(p-1/3)^2+416>0,
\qquad J(1/2)=-1125/32<0,
\]
all four discriminants are nonzero for \(1/4\le p\le1/2\). Consequently no root can be born or die through a smooth double root. At \(x=0\), the fixed root is simple because \((F_p^2)'(0)=4/p^2>1\); \(x=1\) is never periodic since \(F_p^2(1)=0\). Thus the number of solutions of \(F_p^2(x)=x\) is constant on each open parameter interval cut out by \(\alpha,p_0,\beta\).

**3. Exact rational root counts between crossings.** For each row in the following table, rational Sturm isolation of each of the four branch polynomials, followed by the exact inequalities defining its corresponding branch, counts *all* solutions of \(F_p^2(x)=x\). The fixed points are counted separately from \(q_p(x)=x\) and \(q_p(1-x)=x\). The file `CHECK.py` reproduces the calculations using rational isolating intervals rather than floating-point root sampling.

| Parameter \(p\) | Branch root counts \((LL,LR,RL,RR)\) | Number fixed | Primitive two-cycles |
|---|---|---:|---:|
| \(1/4\) | \((4,4,4,4)\) | 4 | 6 |
| \(251/1000\) | \((4,4,4,4)\) | 4 | 6 |
| \(27/100\) | \((2,3,3,4)\) | 4 | 4 |
| \(1/3\) | \((1,2,2,3)\) | 2 | 3 |
| \(2/5\) | \((1,1,1,1)\) | 2 | 1 |
| \(1/2\) | \((1,1,1,1)\) | 2 | 1 |

For completeness, the fixed-point equation gives a left-hand nonzero fixed point \(2p-p^2\) exactly when \(p\le p_0\); the second admissible right-hand fixed point also reaches the corner at \(p_0\). Hence the number of distinct fixed points is 4 below \(p_0\), 3 at \(p_0\), and 2 above it, as independently follows from the explicit quadratic equations.

**4. The boundary counts.** At \(p=\alpha\), \(h(\alpha)<1/2\), and \(F_p^2(x)-x\) has a strict corner minimum at \(x=1/2\). The magnitude of the product of the one-sided corner slope and \(F_p'(h)\) exceeds 30 by the rational interval bound for \(\alpha\). Consequently the two neighboring roots (representing two primitive cycles) meet at the single cycle \(\{1/2,h(\alpha)\}\) and disappear across the threshold. Hence \(N_2(\alpha)=5\). At \(p=\beta\), \(h(\beta)>1/2\), and the corner is a strict maximum; the corresponding slope product exceeds 6 in magnitude. Again two cycles merge at \(\{1/2,h(\beta)\}\) and disappear, giving \(N_2(\beta)=2\). At \(p=p_0\), \(h(p_0)=1/2\), so the only seam orbit is a **fixed** point, not a primitive two-cycle; the extra two-cycle below \(p_0\) collapses into it, and the other three primitive cycles persist. Thus \(N_2(p_0)=3\). The nonzero branch discriminants and exclusion of other seam events make these local counts exhaustive, completing the proof.

## Verification
Run `python CHECK.py` with SymPy installed. The program verifies both exact quartic factor identities, all four discriminants, strict parameter brackets, and exact rational Sturm counts for six parameter values, including both endpoints. Because every possible parameter transition has already been classified analytically, these sample counts are a rigorous finite component of the parameter-uniform proof, not an extrapolation from numerical experiments. Root-isolation tolerances specify *rational* enclosures and are checked against exact branch inequalities.

## Relationship to prior work
Lawnik and Berezowski introduced the four-arm quadratic M-map and provided fixed-point calculations, numerical bifurcation plots, Lyapunov exponents and numerical invariant-density histograms. Their analysis does not supply an exact all-parameter census of primitive two-cycles. Standard kneading and piecewise-smooth bifurcation frameworks explain methods but do not by themselves specify the three algebraic thresholds or six-to-one cycle-count diagram for this particular family. An earlier exact first-critical-image Markov-parameter calculation for the same family determines selected entropy and lap-growth values; it does not imply this all-parameter primitive-two-cycle count. A different economic map also called an “M-map” is not equivalent to the present quadratic family.

## Limitations
The result counts period-two **orbits**, not the number of periodic points of every period. It does not characterize stability of these orbits, even though their count varies; no conclusion about absence of attracting cycles of other periods is implied. It does not prove that a numerical image-encryption method is secure, or that the model is mixing for every parameter. The novelty comparison is bounded by accessible indexed literature and prior mathematical records, not a claim that no unindexed proof exists. An independent audit has not been conducted.

## References
1. M. Lawnik and M. Berezowski, “New Chaotic System: M-Map and Its Application in Chaos-Based Cryptography,” *Symmetry* 14 (2022), 895, DOI: 10.3390/sym14050895. First public date reported by the journal: 2022-04-27. https://doi.org/10.3390/sym14050895
2. J. Milnor and W. Thurston, “On iterated maps of the interval,” *Lecture Notes in Mathematics* 1342 (1988), 465–563, DOI: 10.1007/BFb0082847.
3. C. K. Halse, M. E. Homer and M. di Bernardo, “C-bifurcations and period-adding in one-dimensional piecewise smooth maps,” *Chaos, Solitons & Fractals* 18 (2003), 953–976, DOI: 10.1016/S0960-0779(03)00066-3.
4. L. Gardini and I. Sushko, “Growing through chaos in the Matsuyama map via subcritical flip bifurcation and bistability,” *Chaos, Solitons & Fractals* 124 (2019), 52–67, DOI: 10.1016/j.chaos.2019.04.036. This paper concerns a different map with the same nickname.
