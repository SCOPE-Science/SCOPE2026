# Three weak-resetting reversals in a layered reversible diffusion

## Finding

There exists a uniformly elliptic, one-dimensional reversible diffusion on the unit interval, absorbed at \(0\) and reflected at \(1\), for which the first-order effect of Poisson resetting to the starting point changes sign **exactly three times** as the reset point traverses \((0,1)\). More precisely, write \(H_x\) for the unreset first hitting time of \(0\), and \(T_r(x)\) for its mean under independent Poisson resets to \(x\) at rate \(r\). The piecewise-constant three-layer model below has three simple interior zeros of

\[
J(x)=\left.\frac{dT_r(x)}{dr}\right|_{r=0+}=
\frac{\bigl(\mathbb EH_x\bigr)^2-\operatorname{Var}(H_x)}{2}.
\]

The signs from left to right are \((- ,+ ,- ,+)\). Thus arbitrarily weak resetting reduces the mean search time in two separated launch-position intervals, but increases it in the two intervening regions. There also exist **smooth positive scale and speed densities**, hence smooth uniformly elliptic reversible diffusions, exhibiting *at least* three such sign changes.

## Assumptions and scope

On \([0,1]\), take the killed diffusion whose backward generator is

\[
\mathcal L f(x)=\frac{1}{m(x)}\frac{d}{dx}
\left(\frac{f'(x)}{s(x)}\right),\qquad
f(0)=0,\quad f'(1)=0.
\]

The domain consists of functions continuous at the internal interfaces and with continuous flux \(f'/s\). The strictly positive, piecewise constant scale density \(s\) and speed density \(m\) are, respectively,

\[
(s,m)=\begin{cases}
(1,1),&0<x<1/3,\\
(1,1/32),&1/3<x<2/3,\\
(128,1/32),&2/3<x<1.
\end{cases}
\]

In each layer the local diffusivity is \(D=(sm)^{-1}\), hence \(1,32,1/4\), respectively. The conservative interface conditions are essential: the example has independently changing scale and speed, not merely a single spatial diffusion coefficient under a fixed stochastic calculus convention. For \(x\in(0,1)\), reset to the *same* initial point \(x\) at exponentially distributed times, independently of the diffusion. Only the derivative at zero reset rate is classified; a positive derivative does **not** rule out improvement at a larger reset rate.

## Proof

**1. Exact moment reduction.** Set \(M(x)=\int_x^1m(y)\,dy\). From the killed boundary equations \(\mathcal Lu=-1\) and \(\mathcal Lw=-2u\), for \(u(x)=\mathbb EH_x\) and \(w(x)=\mathbb EH_x^2\), we have

\[
u'(x)=s(x)M(x),\qquad
v'(x)=2s(x)\int_x^1s(y)M(y)^2\,dy,
\quad v=w-u^2,
\]

with \(u(0)=v(0)=0\). The second formula follows by subtracting \(2uu'\) from \(w'\), changing integration order, and using \(u(y)-u(x)=\int_x^ys(z)M(z)\,dz\). Both identities hold on every open layer and join continuously at the interfaces. The right-tail values of \(M\) at \(0,1/3,2/3,1\) are \(17/48,1/48,1/96,0\); those of \(K(x)=\int_x^1s(y)M(y)^2\,dy\) are \(1363/82944,5/3072,1/648,0\). Consequently, for \(F(x)=u(x)^2-v(x)\), exact rational integration gives

\[
F(x)=\begin{cases}
\dfrac{x(17280x^3-24480x^2+10404x-1363)}{41472},&0\le x\le1/3,\\[5pt]
\dfrac{405x^4-1620x^3+270x^2-348x+341}{995328},&1/3\le x\le2/3,\\[5pt]
\dfrac{6635520x^4-26542080x^3+38658816x^2-24233472x+5527381}{995328},&2/3\le x\le1.
\end{cases}
\]

**2. Restart derivative.** The renewal identity for resetting to the original point, with \(\phi_x(r)=\mathbb E[e^{-rH_x}]\), is

\[
T_r(x)=\frac{1-\phi_x(r)}{r\phi_x(r)}.
\]

The bounded reflecting–absorbing interval gives finite hitting-time moments. Expanding \(\phi_x(r)=1-r u(x)+r^2w(x)/2+O(r^3)\) yields \(T_r(x)=u(x)+r[u(x)^2-w(x)/2]+O(r^2)\), so \(J(x)=F(x)/2\) exactly.

**3. Exactly three changes.** On the first layer, the cubic factor \(P(x)=17280x^3-24480x^2+10404x-1363\) satisfies \(P(0)=-1363\), \(P(1/3)=25\), and its two derivative zeros are \(17/36\pm17\sqrt{10}/360\). Only the smaller one lies in \([0,1/3]\); it is a local maximum. Thus \(P\) crosses zero once in this layer. On the middle layer,

\[
F'(x)=\frac{135x^3-405x^2+45x-29}{82944}<0
\quad(1/3\le x\le2/3),
\]

and \(F(1/3)=25/124416>0\), \(F(2/3)=-19/110592<0\), so there is exactly one middle crossing. On the last layer,

\[
F'(x)=\frac{(x-1)[1920(x-1)^2-167]}{72}.
\]

It decreases until \(x=1-\sqrt{167/1920}\) and then increases. Since \(F(2/3)<0\) and \(F(1)=46165/995328>0\), it has exactly one zero on this layer. The three interior zeros are approximately \(0.2683588852\), \(0.5490460495\), and \(0.7503621537\). The boundary value \(F(0)=0\) is excluded from the interior count. Every crossing is transversal. In particular, the exact sign witnesses are

\[
\begin{array}{c|cccc}
x&1/4&2/5&7/10&4/5\\\hline
F(x)&-11/82944&18961/124416000&-496831/124416000&1326209/124416000.
\end{array}
\]

**4. Smooth robustness.** Take smooth strictly positive \(s_\varepsilon,m_\varepsilon\) converging in \(L^1[0,1]\) to the piecewise constants while remaining within fixed common positive upper/lower bounds. The displayed integral expressions for \(u,v\) converge uniformly on \([0,1]\), hence so does \(F\). The four rational signs above persist for all sufficiently small \(\varepsilon\), and the intermediate value theorem gives at least three distinct sign changes. For smooth densities the generator is \(D(x)f''(x)+b(x)f'(x)\), with \(D=1/(sm)>0\) and \(b=-s'/(s^2m)\), a smooth uniformly elliptic reversible diffusion. The argument does not establish *exactly* three for every smoothing.

## Verification

The accompanying `verify.py` uses only Python's standard library. It evaluates all layer integrals using exact rational arithmetic, compares first and second moments to an independent three-layer Laplace-transfer calculation, checks the stated rational polynomial formulas and endpoint signs, and bisects each of the three roots. Run `python3 verify.py` after extracting this file. The number of roots is established by the monotonicity proof above rather than by finite sampling or numerical root-finding.

## Relationship to prior work

Menon Jr. and Anteneodo (2024) derive small-reset-rate and heterogeneous-diffusivity formulas in a fixed stochastic-calculus interpretation, analyze monotone and oscillatory diffusion profiles, and report spatial resetting phase diagrams. The present example differs in its independently specified scale and speed densities and supplies an explicit, exact, three-reversal theorem plus smooth stability. Their general weak-rate perturbation framework does not by itself imply the existence, specific count, or signs of this example. Ray (2020) studies a linear space-dependent diffusivity with constant drift and a single resetting transition parameter. Julián-Salgado, Dagdug, and Boyer (2023) obtain discontinuous optimal-reset-rate transitions when resets occur to **two** sites; here there is exactly one reset site at each launch point and the result concerns the infinitesimal-rate derivative. Méndez and collaborators (2022) treat another heterogeneous setting with different absorbing boundary conditions and do not give this three-layer sign classification. None of these comparisons establishes global historical uniqueness.

## Limitations

Only first-order weak-resetting behavior is proved; full global minimizers of \(r\mapsto T_r(x)\) are not classified. For the discontinuous model there are exactly three interior changes; for arbitrary sufficiently close smooth approximations the proof ensures at least three. No claim is made that three layers are minimal, that all reversible diffusions have a bounded number of changes, or that a broader published scale–speed classification cannot imply the specific construction. The source-priority assessment is provisional pending independent review.

## References

1. L. Menon Jr. and C. Anteneodo, “Random search with resetting in heterogeneous environments,” arXiv:2408.04726v1 (2024-08-08), https://arxiv.org/html/2408.04726v1.
2. S. Ray, “Space-dependent diffusion with stochastic resetting: A first-passage study,” arXiv:2010.14237v2, https://arxiv.org/html/2010.14237v2.
3. P. Julián-Salgado, L. Dagdug, and D. Boyer, “Diffusion with two resetting points,” arXiv:2311.11897v4, https://arxiv.org/html/2311.11897v4.
4. V. Méndez, A. Masó-Puigdellosas, and D. Campos, “Nonstandard diffusion under Markovian resetting in bounded domains,” *Physical Review E* **105**, 054118 (2022), https://doi.org/10.1103/PhysRevE.105.054118.
