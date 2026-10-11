# Sharp minor-axis logarithmic obstruction and two-sided logarithmic law for equal-length ellipse coverings

## Finding
For a noncircular ellipse \(E=\{(x,y):(x/a)^2+(y/b)^2\le1\}\), with \(a>b>0\), let \(N_E(\varepsilon)\) be the least number of translates \(E-h\), with **each** \(\lVert h\rVert_2=\varepsilon\), whose union covers \(E\). Let \(J_E(\varepsilon)\) be the analogous minimum when only its minor-axis segment \(\{(0,y):|y|\le b\}\) must be covered. These numbers may be infinite.

Put \(\kappa=b/a\in(0,1)\), \(\eta=1-(\varepsilon/a)^2\), and \(\Lambda=\log((1+\kappa)/(1-\kappa))\). Then, as \(\varepsilon\uparrow a\),
\[
\lim\frac{J_E(\varepsilon)}{\log(1/\eta)}=\frac1\Lambda,
\qquad
\frac1\Lambda\le\liminf\frac{N_E(\varepsilon)}{\log(1/\eta)}\le\limsup\frac{N_E(\varepsilon)}{\log(1/\eta)}\le\frac2{\log(1+\kappa/8)}.
\]
Thus the global equal-length covering number has *exact logarithmic order*, and the canonical minor-axis obstruction has an exact leading constant. In addition, both numbers are finite when \(0<\varepsilon<a\), and infinite when \(\varepsilon\ge a\).

The upper bound for the global number is a constructive estimate, not an assertion that its coefficient is optimal. All asymptotics fix the eccentricity parameter \(\kappa\) while \(\varepsilon\uparrow a\).

## Assumptions and scope
The covering definition uses Euclidean translation lengths measured **before** affine normalization, without allowing shorter or unequal steps. Translate signs are immaterial because the collection of all admissible displacement vectors is centrally symmetric. The ellipse is compact, and covering includes its boundary. For \(\varepsilon=a\), translations tangent to the center are allowed, but infinitely many are needed.

Normalize via \((X,Y)=(x/a,y/b)\), taking \(E\) to the closed unit disk \(D\). A physical translation becomes a vector \(w=(u,v)\) obeying
\[
u^2+\kappa^2 v^2=\delta^2,\qquad \delta=\varepsilon/a=\sqrt{1-\eta}.
\]
A normalized point \(z\) belongs to \(D-w\) precisely when \(\lVert z+w\rVert_2\le1\). In particular, unlike an affine-invariant covering problem, the length constraint remains elliptical after normalization.

## Proof
**1. Exact one-dimensional trace intervals.** A positive-axis point \(z=(0,t)\) is covered by a displacement \(w=(u,-s)\), with \(s\in(0,\delta/\kappa]\), if and only if
\[
(t-s)^2+\delta^2-\kappa^2s^2\le1
\quad\Longleftrightarrow\quad
 t\in I_\eta(s):=[s-\sqrt{\kappa^2s^2+\eta},\;s+\sqrt{\kappa^2s^2+\eta}].
\]
If \(t>\sqrt\eta\), any covering displacement must have a strictly negative vertical component: with a nonnegative component the squared translated norm is at least \(t^2+\delta^2>1\). The corresponding observation holds for the negative axis, with the signs reversed. A single displacement therefore cannot serve both far-positive and far-negative portions of this segment.

**2. Sharp trace lower bound.** Fix \(0<\theta<1/2\) and a fixed \(T\in(0,1)\). On the positive trace interval \([\eta^{1/2-\theta},T]\), every contributing \(s\) satisfies
\[
s\ge\frac{t-\sqrt\eta}{1+\kappa}\ \ge C_\kappa\eta^{1/2-\theta}.
\]
Indeed, \(t\le s+\sqrt{\kappa^2s^2+\eta}\le(1+\kappa)s+\sqrt\eta\). Uniformly over these \(s\), the ratio of the positive endpoints of \(I_\eta(s)\) is at most
\[
\frac{1+\sqrt{\kappa^2+C_\kappa^{-2}\eta^{2\theta}}}{1-\sqrt{\kappa^2+C_\kappa^{-2}\eta^{2\theta}}}
\longrightarrow\frac{1+\kappa}{1-\kappa}.
\]
Consequently, each such interval covers at most \(\Lambda+o(1)\) units of logarithmic axis length. The positive trace has logarithmic length \((1/2-\theta)\log(1/\eta)+O(1)\), so it needs at least this length divided by \(\Lambda+o(1)\) displacements. The negative trace needs a disjoint set of displacements. Letting \(\theta\downarrow0\) gives
\[
\liminf_{\eta\downarrow0}\frac{J_E(\varepsilon)}{\log(1/\eta)}\ge\frac1\Lambda.
\]
The same lower bound follows for the full ellipse because \(N_E(\varepsilon)\ge J_E(\varepsilon)\).

**3. Matching trace construction.** Write \(c=1-\kappa^2\), \(\gamma=(1+\kappa)/(1-\kappa)\), and fix \(T=\min\{(1-\kappa)/(8\kappa),1/8\}\). For sufficiently small \(\eta\), put \(s_0=\sqrt\eta/c\), \(s_j=s_0\gamma^j\), and let \(j_*\) be the smallest nonnegative integer with \((1+\kappa)s_{j_*}\ge T\). Each \(s_j\), \(0\le j\le j_*\), satisfies \(s_j\le\delta/\kappa\) for all sufficiently small \(\eta\). Use the single displacement \((\delta,0)\), and the two displacements
\[
w_j^\pm=(\sqrt{\delta^2-\kappa^2s_j^2},\,\pm s_j),\qquad 0\le j\le j_*.
\]
The horizontal displacement covers \(|t|\le\sqrt\eta\); the initial trace interval meets this range because \(s_0-\sqrt{\kappa^2s_0^2+\eta}\le\sqrt\eta\). Successive trace intervals overlap since
\[
s_{j+1}-\sqrt{\kappa^2s_{j+1}^2+\eta}\le (1-\kappa)s_{j+1}=(1+\kappa)s_j\le s_j+\sqrt{\kappa^2s_j^2+\eta}.
\]
The last interval reaches \(T\). Thus \(|t|\le T\) is covered by \(1+2(j_*+1)\) displacements, where
\[
j_* =\frac{\log(1/\eta)}{2\log\gamma}+O_\kappa(1).
\]
The fixed compact part \(\{(0,t):T\le |t|\le1\}\) can be covered by a number of displacements bounded as \(\varepsilon\uparrow a\), by the compactness lemma in Step 5 below. This yields the reverse inequality and the exact trace limit.

**4. A logarithmic-size covering of the central square.** Put
\[
q=1+\kappa/8,\quad \tau=\min\{\kappa/(8q^2),\;c/(4\kappa),\;1/16\},\quad t_0=\sqrt\eta/2.
\]
Assume \(\delta\ge1/2\) and \(t_0<\tau/q\). Choose \(t_j=t_0q^j\) for \(0\le j\le j_*\), where \(j_*\) is the first index with \(qt_{j_*}\ge\tau\). Besides the two horizontal vectors \((\pm\delta,0)\), take the four vectors
\[
w_{j,\sigma,\rho}=\left(\sigma\sqrt{\delta^2-\kappa^2(t_j/c)^2},\ \rho t_j/c\right),
\qquad\sigma,\rho\in\{-1,1\}.
\]
All of them have the required physical displacement length because \(t_j\le\tau\le c/(4\kappa)\). They cover every \((s,t)\) in the square \(|s|,|t|\le\tau\), as follows. If \(|s|\ge t^2/\delta\), the horizontal vector of sign opposite to \(s\) gives
\[
\lVert(s,t)+w\rVert^2-1\le t^2-\eta-\delta|s|\le0,
\]
using \(|s|\le\tau<\delta\). If instead \(|s|<t^2/\delta\) and \(|t|\le t_0\), the same choice gives a norm excess at most \(s^2+t^2-\eta<0\), since \(\delta\ge1/2\) and \(t_0^2=\eta/4\).

In the remaining case \(|t|>t_0\), choose an index with \(r=|t|/t_j\in[1/q,q]\) and a four-vector whose signs oppose those of \(s,t\). Direct expansion, dropping the nonpositive cross term involving \(|s|\), yields
\[
\lVert(s,t)+w\rVert^2-1\le s^2-\eta+t_j^2
\left(r-\frac1{1+\kappa}\right)\left(r-\frac1{1-\kappa}\right).
\]
For \(r\in[1/q,q]\), the two factors have opposite signs and absolute values at least \(\kappa/4\), so the product is at most \(-\kappa^2/16\). Meanwhile
\[
s^2<\frac{t^4}{\delta^2}\le\frac{q^4t_j^4}{\delta^2}\le\frac{\kappa^2t_j^2}{16}
\]
by the definitions of \(\tau\) and \(\delta\). Therefore the norm excess is at most \(-\eta<0\). The square is covered by at most \(2+4(j_*+1)\) shifts. Since
\[
j_* =\frac{\log(1/\eta)}{2\log q}+O_\kappa(1),
\]
its leading covering coefficient is \(2/\log q\).

**5. Uniform covering away from the origin.** We use the standard interior-translate compactness mechanism also employed by Martini–Richter–Spirova in the proof of their endpoint theorem (2013). Here is the explicit ellipse version: for every fixed neighborhood \(U\) of the origin, \(E\setminus U\) can be covered by a number \(M(U)<\infty\) of length-\(\varepsilon\) translations, independent of \(\varepsilon\) sufficiently close to \(a\) from below. For each nonzero \(x\in E\), take the farther of the two major-axis endpoints \(\pm(a,0)\). Its distance from \(x\) is strictly greater than \(a\), since \(\max\{|x-(a,0)|^2,|x+(a,0)|^2\}\ge a^2+|x|^2\). The line segment from \(x\) toward that farther endpoint contains an interior point \(y\in\operatorname{int}E\) at distance exactly \(a\) from \(x\) (if \(x\) is on the boundary, every strictly intermediate point lies in the interior by strict convexity; the same holds for interior \(x\)). Then \(h=y-x\) has length \(a\), with \(x+h\in\operatorname{int}E\). Rotating or rescaling this chosen vector slightly makes its length \(\varepsilon\) near \(a\) while keeping \(x+h\) interior, and this covering is stable on a neighborhood of \(x\). Finitely many such neighborhoods cover the compact set \(E\setminus U\).

Apply this lemma outside the open central normalized square \(\{|s|<\tau, |t|<\tau\}\). Combining with Step 4 gives \(N_E(\varepsilon)\le 2+4(j_*+1)+M\), proving the global logarithmic upper estimate. The lemma also gives finiteness of \(N_E(\varepsilon)\) for every fixed \(0<\varepsilon<a\), by choosing for each \(x\in E\) a farther endpoint at distance at least \(a>\varepsilon\) and a suitable interior point at exactly distance \(\varepsilon\).

**6. Endpoint divergence and obstruction.** If \(\varepsilon>a\), the center of \(E\) cannot lie in any length-\(\varepsilon\) translate: every point of \(E\) has Euclidean norm at most \(a\). At \(\varepsilon=a\), the only vectors covering the center are \((\pm a,0)\), which cover no nonzero minor-axis point. Any other fixed admissible vector covering positive minor-axis points has a negative normalized vertical component \(-s\), with its eligible positive ordinates confined to \([(1-\kappa)s,(1+\kappa)s]\); the left endpoint is strictly positive. No finite family can cover all sufficiently small positive ordinates. Thus \(J_E(a)=N_E(a)=\infty\), completing the claim.

## Verification
The attached pure-Python file `verify_ellipse.py` independently constructs the explicit central-square and minor-axis displacement families. It checks physical-length constraints and randomly sampled normalized points for five aspect ratios, two small values of \(\eta\), and 38,000 finite numerical comparisons. Execute from any directory using `python3 verify_ellipse.py`; expected message: `VERIFY_OK: 38000 randomized finite checks`. The analytical interval identities, compactness argument, inequalities and limits above, not the sampling, establish the theorem.

## Relationship to prior work
Martini–Richter–Spirova, *Illuminating and covering convex bodies* (arXiv:1308.0791v1, first public 2013-08-04), introduce fixed-equal-length illumination/covering quantities, prove basic comparison results, identify the circumradius endpoint obstruction, and give the standard compactness mechanism used here away from the center. This result gives a quantitative endpoint scale for every noncircular ellipse and an exact leading constant for the minor-axis covering obstruction, neither furnished by the inspected paper. Lassak–Martini–Spirova, *On translative coverings of convex bodies* (2014), treat unrestricted translation coverings and related constants; they do not impose one fixed nonzero Euclidean displacement length, so their finite planar illumination number does not subsume the above divergence.

## Limitations
The coefficient of \(\log(1/\eta)\) for **the full ellipse** is bounded above and below, but its optimal constant is not determined. Constants are not uniform as \(\kappa\to0\) or \(\kappa\to1\); the circular case \(\kappa=1\) behaves differently. Numerical tests are finite evidence, not a proof of the quantified covering statements. Earlier equivalent endpoint estimates under alternate terminology remain possible and have not been exhaustively ruled out.

## References
1. H. Martini, C. Richter, M. Spirova, *Illuminating and covering convex bodies*, arXiv:1308.0791v1 (2013-08-04), https://arxiv.org/abs/1308.0791 .
2. M. Lassak, H. Martini, M. Spirova, *On translative coverings of convex bodies*, Rocky Mountain J. Math. 44 (2014), 1281–1299, https://doi.org/10.1216/RMJ-2014-44-4-1281 .
