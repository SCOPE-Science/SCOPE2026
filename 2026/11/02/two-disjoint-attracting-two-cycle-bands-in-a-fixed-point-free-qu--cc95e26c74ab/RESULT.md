# Two disjoint attracting two-cycle bands in a fixed-point-free quadratic map

## Finding

Consider the real-plane map
\[
F_c(x,y)=\left(x+y,\ y-\frac1{100}|y|-xy+\frac1{10}x^2-cy^2+\frac1{10}\right),\qquad c>0.
\]
This is the one-parameter slice \((a,b,d)=(1/100,1/10,1/10)\) used in the numerical bifurcation study of Huynh et al. (2019), with \(c\) free. Write
\[
K=\frac{521}{605},\quad c_\infty=\frac{21}{40},\quad
c_{\mathrm f}=\frac{1093979}{2084000}.
\]
The number \(N_2(c)\) of geometrically distinct primitive period-two orbits **in the entire real plane** is exactly
\[
N_2(c)=\begin{cases}
0,&0<c<c_{\mathrm f},\\
1,&c=c_{\mathrm f},\\
2,&c_{\mathrm f}<c<c_\infty,\\
1,&c\ge c_\infty.
\end{cases}
\]
At \(c=c_{\mathrm f}\), two distant orbits merge at a unit-multiplier fold. One of the two branches escapes to infinity as \(c\uparrow c_\infty\): its positive vertical amplitude is
\[
t_{\mathrm{far}}(c)=\frac{1/100}{c_\infty-c}+O(1).
\]
The surviving finite orbit has **two, and only two, disjoint open intervals of local exponential attraction**.

To specify them exactly, put
\[
W(t)=\frac{521}{605t}-\frac1{100},\quad
H(t)=\frac{11t}{20},\quad
V(t)=W(t)-H(t),\quad
C(t)=\frac{21}{40}+\frac{521}{1210t^2}-\frac1{100t}.
\]
Let \(r_1<r_2\) be the two positive roots of
\[
P(t)=44289025t^4-350885359t^2-2521640t+108576400=0,
\]
and let \(q_1<q_2\) be the unique positive solutions of
\[
V(q_1)=\frac{4\sqrt3}{11},\qquad V(q_2)=-\frac{4\sqrt3}{11}.
\]
They obey \(r_1<q_1<q_2<r_2\). Define four exact parameters
\[
c_1=C(r_2),\quad c_2=C(q_2),\quad
c_3=C(q_1),\quad c_4=C(r_1).
\]
Numerically, for orientation only,
\[
(c_1,c_2,c_3,c_4)\approx
(0.577872326737,\ 0.634736417925,\ 1.188264592301,\ 1.860616595223).
\]
**A locally exponentially attracting primitive two-cycle exists (and is unique) if and only if**
\[
\boxed{\ c\in(c_1,c_2)\ \cup\ (c_3,c_4).\ }
\]
At \(c_1,c_4\) its two-step derivative has an eigenvalue \(-1\); at \(c_2,c_3\) the two multipliers form a nonreal conjugate pair of modulus one. No claim is made about nonlinear attraction precisely at these nonhyperbolic boundary parameters.

## Assumptions and scope

All coordinates and parameters are real, \(c>0\), and the phase space is all of \(\mathbb R^2\). A primitive two-cycle means an unordered orbit \(\{p,F_c(p)\}\) with \(F_c^2(p)=p\) but \(F_c(p)\ne p\). We count such unordered cycles once and allow unbounded coordinate values. Local exponential attraction means the two eigenvalues of the two-step Jacobian have modulus strictly below one, equivalently the orbit has a locally exponentially attracting neighborhood (the map is smooth near both cycle points because their vertical coordinates are nonzero).

The underlying map has no fixed point: a fixed point would require \(y=0\) and then \(x^2/10+1/10=0\). The earlier quadratic NEM1 of Panahi, Sprott and Jafari (2018) is the related \(a=0\) limiting map; the present claim concerns the strictly positive absolute-value coefficient in the 2019 example.

## Proof

**1. Exhaustive period-two reduction.** It is convenient first to write the larger family as
\[
F_{a,b,c,d}(x,y)=(x+y,\ y-a|y|-xy+bx^2-cy^2+d),\quad a,b,c,d>0.
\]
If \((x,y)\) has period two, its successive vertical coordinates sum to zero, hence are \(t,-t\) with \(t>0\), after choosing the starting point with positive vertical coordinate. The same first-coordinate equation forces the two points to be \((X-t/2,t)\) and \((X+t/2,-t)\) for some \(X\). Substitution into the two second-coordinate equations, adding and subtracting, yields exactly
\[
X=\frac{2}{1+b},\qquad
L t^2-2at+K=0,\qquad
L=1+\frac b2-2c,\quad K=\frac{8b}{(1+b)^2}+2d.
\]
Conversely every positive solution of this quadratic produces the two displayed points and direct substitution verifies the two-step return. No other period-two itinerary is possible. Since no fixed point exists, every solution gives a primitive two-cycle, and distinct positive roots yield distinct geometric orbits.

On the stated slice, \(K=521/605\), \(L=2(c_\infty-c)\), and the discriminant divided by four is \(a^2-LK\), with \(a=1/100\). The equality \(a^2-LK=0\) occurs at \(c_{\mathrm f}=1093979/2084000>0\). For \(L>0\), the quadratic has respectively zero, one positive double, or two distinct positive roots as its discriminant is negative, zero, or positive. For \(L=0\) it has the sole root \(K/(2a)\). For \(L<0\) its two roots have opposite signs, hence exactly one is positive. This proves every entry of the displayed census. Near the fold, with \(\varepsilon=c-c_{\mathrm f}\downarrow0\), the roots separate as
\[
t_\pm=\frac Ka\pm \frac{K\sqrt{2K}}{a^2}\sqrt{\varepsilon}+O(\varepsilon).
\]
As \(c\uparrow c_\infty\) from below, the larger root is
\(t_{\mathrm{far}}=2a/L+O(1)=a/(c_\infty-c)+O(1)\), establishing the claimed escape law. There is no finite loss of the remaining orbit at \(c_\infty\).

**2. Two-step Jacobian identities.** At a point with nonzero vertical coordinate,
\[
DF_{a,b,c,d}(x,y)=
\begin{pmatrix}1&1\\-y+2bx&1-a\operatorname{sgn}(y)-x-2cy\end{pmatrix}.
\]
For a positive root \(t\), define \(W=K/t-a\) and \(H=(1+b)t/2\). Multiplication of the two exact Jacobians at \((2/(1+b)-t/2,t)\) and \((2/(1+b)+t/2,-t)\) gives
\[
\begin{aligned}
\operatorname{tr}(DF^2)&=1+\frac{8b}{1+b}+\left(\frac{b-1}{b+1}\right)^2-(W+H)^2,\\
\det(DF^2)&=\left(\frac{1+3b}{1+b}\right)^2-(W-H)^2,\\
1-\operatorname{tr}(DF^2)+\det(DF^2)&=2(1+b)(K-at).
\end{aligned}
\]
The identities hold at every two-cycle, not merely numerical samples. On the displayed parameter slice they simplify to
\[
T(t)=\frac{290}{121}-(W(t)+H(t))^2,\quad
D(t)=\frac{169}{121}-(W(t)-H(t))^2.
\]
The quadratic Schur criterion for a real two-by-two matrix gives strict spectral radius below one precisely when
\[
1-T+D>0,\quad 1+T+D>0,\quad 1-D>0.
\]
Thus the three necessary and sufficient conditions are
\[
K-at>0,\qquad W(t)^2+H(t)^2<\frac{290}{121},\qquad
|V(t)|>\frac{4\sqrt3}{11}.
\]

**3. Exact isolation and exhaustiveness of the two attraction bands.** The middle inequality is \(P(t)<0\) after multiplication by the positive factor \(146410000t^2\). The coefficient signs of \(P\) in descending order are \(+,-,-,+\); Descartes' rule gives at most two positive roots. Exact integer arithmetic yields
\[
P(564/1000)>0>P(565/1000),\quad
P(2760/1000)<0<P(2761/1000).
\]
Therefore there are exactly two positive roots, isolated by
\[
0.564<r_1<0.565,\qquad 2.760<r_2<2.761,
\]
and \(P(t)<0\) exactly for \(r_1<t<r_2\).

The function \(V(t)=K/t-a-11t/20\) is strictly decreasing from \(+\infty\) to \(-\infty\). Comparing its sign and its square to \(48/121\) at rational endpoints proves
\[
0.798<q_1<0.799,\qquad1.935<q_2<1.937.
\]
Consequently \(|V(t)|>4\sqrt3/11\) exactly for \(t<q_1\) or \(t>q_2\). The isolation intervals give the strict interleaving \(r_1<q_1<q_2<r_2\). Every \(t\) in \((r_1,r_2)\) also satisfies \(t<K/a\), so the first Schur inequality is automatic there. The full interval of Schur-stable positive amplitudes is hence exactly
\[
(r_1,q_1)\cup(q_2,r_2).
\]
An orbit with \(c<c_\infty\) cannot enter these bands: its smaller root satisfies \(t\ge K/(2a)=5210/121>43\), whereas \(r_2<3\); its larger root, if present, is still larger. For \(c>c_\infty\), its unique amplitude lies in \((0,K/(2a))\), and
\[
c=C(t)=c_\infty+\frac{K}{2t^2}-\frac at,
\qquad C'(t)=\frac{at-K}{t^3}<0.
\]
The decreasing parameterization reverses the amplitude-band order, giving exactly the two asserted \(c\)-intervals. At \(r_1,r_2\), \(1+T+D=0\) while the other Schur conditions hold, so one multiplier is \(-1\). At \(q_1,q_2\), \(D=1\) and \(-2<T<2\), so the multipliers form a nonreal unit-modulus conjugate pair. At all remaining parameters the spectral radius is not strictly below one. This completes the exhaustive classification.

## Verification

The standalone script `verify_period_two.py` uses only Python's standard-library exact rational numbers. It checks fifteen independent parameterized two-step orbit returns, all associated Jacobian identities, the exact polynomial identity and its positive-root sign isolations, the two unit-circle root isolations, five Schur-sector witnesses and six orbit-count witnesses. Run: `python3 verify_period_two.py`. The script checks finite algebraic certificates; the exhaustive real-root and parameter statements are proved by the analytic Descartes, monotonicity, and quadratic arguments above, not by sampling. Exact decimal brackets provide certified labels; displayed floating-point approximations do not define the theorem.

## Relationship to prior work

Huynh, Ouannas, Wang, Pham, Nguyen and Alsaadi (2019) introduce precisely the map studied here (their Eq. 1), with \((a,b,d)=(0.01,0.1,0.1)\) and a numerical bifurcation diagram varying \(c\) (Sec. 2.1). They report an initial period-two phase and subsequent period doublings but do not give an exhaustive real-plane primitive-two-cycle count, exact sink parameter bands, or the distant-orbit escape boundary. Their stabilization and synchronization calculations concern controlled systems, not the untreated map's entire two-cycle spectrum.

Panahi, Sprott and Jafari (2018, Secs. 2–4 and Table 1) give an antecedent map with the same quadratic skeleton but no \(-a|y|\) term; their NEM1 therefore corresponds to the limit \(a=0\) with \(b=d=0.1\) in the current notation. They present numerical bifurcation and Lyapunov plots, not an implication covering the strictly positive-\(a\) four-threshold classification. Their construction is acknowledged rather than claimed new. García-Grimaldo and Campos-Cantón (2022) review maps without fixed points using numerical diagnostics; the complete chapter was not accessible, so exact overlap cannot be excluded on the basis of its abstract. Standard Jury stability and Descartes' rule are used as tools, not represented as new mathematics.

## Limitations

The result concerns only primitive period-two orbits in the real plane. It makes no claim about higher-period orbits, global attraction basins, invariant chaotic sets or security properties. At the four nonhyperbolic boundary parameters, nonlinear attraction and bifurcation criticality coefficients are not classified. The comparison with the 2022 review is limited by lack of full-text access; unindexed publications may still contain equivalent results. The numerical thresholds are given to orient the reader; the root equations and rational isolations specify them exactly. No independent mathematical audit has been performed.

## References

1. V. V. Huynh, A. Ouannas, X. Wang, V.-T. Pham, X. Q. Nguyen, F. E. Alsaadi, “Chaotic Map with No Fixed Points: Entropy, Implementation and Control,” *Entropy* **21** (2019), 279, first published 14 March 2019. DOI: 10.3390/e21030279. Full text: https://www.researchgate.net/publication/331784411_Chaotic_Map_with_No_Fixed_Points_Entropy_Implementation_and_Control .
2. S. Panahi, J. C. Sprott, S. Jafari, “Two Simplest Quadratic Chaotic Maps Without Equilibrium,” *International Journal of Bifurcation and Chaos* **28** (2018), 1850144. DOI: 10.1142/S0218127418501444. Author-hosted full text: https://sprott.physics.wisc.edu/pubs/paper500.pdf .
3. C. García-Grimaldo, E. Campos-Cantón, “Comparative Analysis of Chaotic Features of Maps Without Fixed Points,” in *Complex Systems and Their Applications* (2022), pp. 151–176. DOI: 10.1007/978-3-031-02472-6_8 (abstract available; full chapter not inspected).
