# A logarithmic near-circle crossover for nearly diametral chords of ellipse boundaries

## Finding

Let \(a>0\), \(0<b\le a\), and let \(X,Y\) be independent random points uniformly distributed by normalized arclength on the boundary of the ellipse
\[
\mathcal E_{a,b}=\{(a\cos\theta,b\sin\theta):0\le\theta<2\pi\}.
\]
Put \(D=\|X-Y\|_2\), \(\delta=1-b^2/a^2\in[0,1)\), and
\(F_{a,\delta}(\varepsilon)=\Pr(D>2a-\varepsilon)\). Define the parameter-convention complete elliptic integrals
\[
E(m)=\int_0^{\pi/2}\sqrt{1-m\sin^2 t}\,dt,
\qquad
K(m)=\int_0^{\pi/2}\frac{dt}{\sqrt{1-m\sin^2 t}},\quad 0\le m<1,
\]
with \(E(1)=1\). The ellipse perimeter is \(P_{a,\delta}=4aE(\delta)\).

**Theorem.** The following statements hold for the same arclength-uniform, independent-endpoint model:

1. For each *fixed* \(0<\delta<1\), as \(\varepsilon\downarrow0\),
   \[
   F_{a,\delta}(\varepsilon)
   =\frac{4\pi a^2(1-\delta)}{aP_{a,\delta}^2\sqrt\delta}\,\varepsilon+o_{a,\delta}(\varepsilon)
   =\frac{\pi(1-\delta)}{4aE(\delta)^2\sqrt\delta}\,\varepsilon+o_{a,\delta}(\varepsilon).
   \]
2. For the circle \(\delta=0\) and \(0<\varepsilon<2a\), the known exact formula is
   \[
   F_{a,0}(\varepsilon)=\frac2\pi\arccos\left(1-\frac{\varepsilon}{2a}\right)
   \sim\frac2\pi\sqrt{\frac\varepsilon a}.
   \]
3. For any family \(\delta_\varepsilon\in[0,1)\) with \(\delta_\varepsilon/(\varepsilon/a)\to\lambda\in[0,\infty)\),
   \[
   \lim_{\varepsilon\downarrow0}
   \frac{F_{a,\delta_\varepsilon}(\varepsilon)}{\sqrt{\varepsilon/a}}
   =H(\lambda):=\frac1{\pi^2}\int_0^{2\pi}
       \sqrt{\bigl(1-\lambda\sin^2\phi\bigr)_+}\,d\phi,
   \quad (z)_+:=\max\{z,0\}.
   \]
   More explicitly,
   \[
   H(\lambda)=\begin{cases}
      \dfrac4{\pi^2}E(\lambda), & 0\le\lambda\le1,\\[5pt]
      \dfrac{4\sqrt\lambda}{\pi^2}
        \left[E(1/\lambda)-(1-1/\lambda)K(1/\lambda)\right],&\lambda>1.
   \end{cases}
   \]
   This function is positive, continuous, and strictly decreasing, with \(H(0)=2/\pi\), \(H(1)=4/\pi^2\), and \(H(\lambda)\sim1/(\pi\sqrt\lambda)\) as \(\lambda\to\infty\).
4. The transition function has the **logarithmic cusp**
   \[
   \pi^2H(1+h)=4+h\log|h|+(1-\log16)h
     +O\!\left(h^2|\log|h||\right),\qquad h\to0,\ h\ne0.
   \]
   In particular, \(H'(\lambda)\to-\infty\) as \(\lambda\to1\) from either side. This distinguishes the critical shape scale \(1-b^2/a^2\asymp\varepsilon/a\) and the subthreshold/superthreshold portions of the crossover.

## Assumptions and scope

The ellipse is a filled planar convex body's **boundary**, not its interior; the two endpoints are independently **uniform by Euclidean arclength**, not uniformly distributed in the ellipse parameter and not produced by an invariant random line. The diameter is \(2a\). The fixed-eccentricity limit has \(a>0\), \(\delta\in(0,1)\) fixed, whereas in the joint limit \(a>0\) is fixed and \(\delta\) varies with \(\varepsilon\). Both limits use \(\varepsilon\downarrow0\) with strict probability event \(D>2a-\varepsilon\), whose boundary has probability zero. The normalized crossover variable is \(\lambda=\lim a\delta_\varepsilon/\varepsilon\). The asymptotic for fixed \(\delta\) is not claimed to be uniform as \(\delta\downarrow0\).

## Proof

**Exact two-angle reduction.** The speed of the standard ellipse parameterization is
\[
g_\delta(\theta)=a\sqrt{1-\delta\cos^2\theta},\qquad
P_{a,\delta}=\int_0^{2\pi}g_\delta(\theta)d\theta=4aE(\delta).
\]
Use the antipodal coordinates \(\theta_1=\phi-v/2\), \(\theta_2=\phi+\pi+v/2\), with \(\phi\) taken modulo \(2\pi\) and \(-\pi\le v<\pi\). They give a measure-preserving parameterization (Jacobian absolute value one) of the ordered angle-pair torus; periodicity allows the displayed fundamental domain. Direct subtraction of the two ellipse points gives the **exact identity**
\[
D=2a\cos(v/2)\sqrt{1-\delta\sin^2\phi}.
\]
The ordered joint angle density, including the arclength Jacobians, is
\[
\frac{g_\delta(\phi-v/2)g_\delta(\phi+v/2)}{P_{a,\delta}^2}
\,d\phi\,dv.
\]
Consequently the probability in the theorem is exactly the integral of this density over the region
\[
\cos(v/2)\sqrt{1-\delta\sin^2\phi}>1-\frac\varepsilon{2a}.
\tag{1}
\]
All subsequent limits follow from this identity, not from approximating the endpoint law by uniform parameter angles.

**Fixed noncircular ellipse.** If \(\delta>0\) is fixed, equality \(D=2a\) occurs only at the two ordered diametral configurations \((\phi,v)=(0,0),(\pi,0)\) on this fundamental domain. Near either configuration, writing \(s\) for \(\phi\) or \(\phi-\pi\), Taylor expansion yields
\[
2a-D=a\delta s^2+\frac a4v^2+O_{a,\delta}\!\left((|s|+|v|)^4\right).
\]
The limiting density is \(g_\delta(0)^2/P_{a,\delta}^2=b^2/P_{a,\delta}^2\). Rescale \(s=\sqrt{\varepsilon/(a\delta)}\,u\), \(v=2\sqrt{\varepsilon/a}\,w\). At each pole the indicator approaches \({\bf1}\{u^2+w^2<1\}\). The Jacobian contributes \(2\varepsilon/(a\sqrt\delta)\), so the area contribution of each pole is \(2\pi\varepsilon/(a\sqrt\delta)\). There are two ordered poles. Localization follows because the continuous exact distance has no other maximizers, and the quadratic form is positive definite. Dominated convergence after rescaling gives
\[
F_{a,\delta}(\varepsilon)\sim
 2\frac{b^2}{P_{a,\delta}^2}\frac{2\pi\varepsilon}{a\sqrt\delta}
 =\frac{4\pi b^2}{aP_{a,\delta}^2\sqrt\delta}\varepsilon,
\]
which is assertion 1.

**The circle.** At \(\delta=0\), \(g_0=a\) and \(D=2a\cos(v/2)\) are independent of \(\phi\). Since \(v\) is uniformly distributed modulo \(2\pi\), the event in (1) has normalized \(v\)-length \(2\arccos(1-\varepsilon/(2a))/\pi\), proving assertion 2.

**Crossover.** Write \(t=\varepsilon/a\) and suppose \(\delta_\varepsilon/t\to\lambda\in[0,\infty)\). The event in (1) forces \(v=O(\sqrt t)\). Substitute \(v=2\sqrt t\,u\). For bounded \(u\), uniformly in \(\phi\),
\[
\frac{2a-D}{\varepsilon}=u^2+\frac{\delta_\varepsilon}{t}\sin^2\phi+o(1)
 \longrightarrow u^2+\lambda\sin^2\phi.
\]
Moreover \(g_{\delta_\varepsilon}(\phi\pm v/2)/P_{a,\delta_\varepsilon}\to1/(2\pi)\) uniformly. The rescaled indicators are dominated by a bounded \(u\)-strip; the limiting equality set has two-dimensional Lebesgue measure zero. Dominated convergence in the probability integral yields
\[
\lim_{\varepsilon\to0}\frac{F}{\sqrt{\varepsilon/a}}
 =\frac1{2\pi^2}\int_0^{2\pi}\int_{\mathbb R}
 {\bf1}\{u^2+\lambda\sin^2\phi<1\}\,du\,d\phi
 =\frac1{\pi^2}\int_0^{2\pi}\sqrt{(1-\lambda\sin^2\phi)_+}\,d\phi.
\]
Symmetry gives \(4E(\lambda)\) for the integral when \(\lambda\le1\). For \(\lambda>1\), set \(m=1/\lambda\) and substitute \(\sin\phi=\sqrt m\sin t\) on each support arc. The integral becomes \(4\sqrt\lambda\,[E(m)-(1-m)K(m)]\), proving the piecewise formula.

**Monotonicity, matching, and cusp.** The integral defining \(H\) is strictly decreasing in \(\lambda\ge0\) because its integrand decreases strictly on a set of positive measure; dominated convergence proves continuity and the values at zero and one. As \(\lambda\to\infty\), the support shrinks toward the two zeros of \(\sin\phi\); rescaling \(s=\sqrt\lambda\,\phi\) at each zero gives total integral \(\pi/\sqrt\lambda+o(\lambda^{-1/2})\). This also matches the small-\(\delta\) limit of the fixed-eccentricity coefficient: \(P_{a,\delta}\to2\pi a\).

To evaluate the singularity at \(\lambda=1\), use the standard complete-elliptic-integral expansions, with \(r\downarrow0\),
\[
K(1-r)=\log\frac4{\sqrt r}+O\bigl(r|\log r|\bigr),\qquad
E(1-r)=1+\frac r2\left(\log\frac4{\sqrt r}-\frac12\right)
 +O\bigl(r^2|\log r|\bigr).
\]
These follow, for example, from the convergent endpoint series of NIST DLMF §19.12. Substitute \(r=1-\lambda\) for \(\lambda<1\), or \(r=1-1/\lambda\) and multiply by \(\sqrt\lambda\) for \(\lambda>1\). In both cases one obtains
\[
\pi^2 H(1+h)=4+h\log|h|+(1-\log16)h+O(h^2|\log|h||).
\]
The derivative of the leading nonanalytic term tends to negative infinity, and the differentiable remainders from the displayed convergent series are of smaller derivative order. This proves assertions 3 and 4.

## Verification

The standalone artifact `check_ellipse.py` numerically integrates the **exact** two-angle probability from (1), with the correct arclength weights, and compares it against the fixed-eccentricity and crossover limits. The program also evaluates the complete elliptic integrals on both sides of the cusp. Run `python check_ellipse.py` with Python 3 and NumPy/SciPy installed. It prints `VERIFY_OK cases= 15` when all assertions hold. The checks cover nine crossover parameters \(\lambda\in\{0,0.2,0.5,0.9,1,1.1,1.5,3,10\}\), three fixed eccentricities \(\delta\in\{0.1,0.36,0.75\}\), and three one-sided cusp scales. The numerical errors are bounded by the tolerances in the code; numerical quadrature is corroboration rather than a proof of any asymptotic assertion.

## Relationship to prior work

The new content is the **arclength-endpoint ellipse-tail coefficient**, the *joint near-circle scaling law* and its explicit *logarithmic nonanalyticity*. The elementary circle distribution and the standard special-function endpoint expansions are prior mathematical knowledge, not newly claimed discoveries.

Gečiauskas (1966) studies the interpoint distance for **interior-uniform points** of an oval and derives a general relation using Crofton's differential equation. Gečiauskas (1967) studies **random-line/directional chords** and their relationships to interior sampling; the first point may be selected from the contour, but the second endpoint is determined by a random chord direction rather than independently uniform on the contour. Neither sampling measure is the product of normalized boundary arclength measures used here. The first page and relevant theorem/model definitions of both full articles were checked.

Mayer and Molchanov (2006) prove maximal-sample-distance limits for radial distributions on the unit ball, including uniform points **on the circle/sphere**; their circle tail is consistent with assertion 2. Their rotational symmetry assumption does not imply the eccentric ellipse or the critical double-scaling formula. Schrempp (2015) studies the largest sample distance for planar supports with a unique diameter, explicitly assuming a **two-dimensional Lebesgue density** for the point law (Section 2), thereby excluding boundary arclength sampling. Its fixed-shape results also do not analyze a simultaneous approach to a circle. These full-text hypothesis and conclusion comparisons delimit the claim; no general priority conclusion is inferred merely from differing titles.

## Limitations

The result is a single-pair geometric probability theorem, **not** a limit law for the maximum among \(n\) sampled points. It assumes independent normalized arclength sampling and axis-aligned (up to rigid motion) Euclidean ellipses. The fixed-eccentricity and joint limits have distinct quantifiers: the first is not uniform in a vanishing eccentricity; the second applies when the ratio \(a\delta_\varepsilon/\varepsilon\) tends to a **finite** value. Although \(H(\lambda)\sim1/(\pi\sqrt\lambda)\), this large-\(\lambda\) limit cannot be substituted into the joint theorem without establishing a separate uniform remainder. The proof does not cover arbitrary smooth curves, higher-dimensional ellipsoids or finite-sample inference. Historical priority remains provisional pending broader expert assessment; the available literature search cannot prove uniqueness of publication history.

## References

1. E. Gečiauskas, *Distribution function of a distance between two random points in an oval*, Lithuanian Mathematical Journal 6 (1966), 245–248. Public publisher date 1966-06-15. DOI: `10.15388/LMJ.1966.19722`. Primary full text examined, especially definitions and theorem.
2. E. Gečiauskas, *The distribution function of the chord length of oval and ovaloid and its relation to distribution of a distance in an oval and ovaloid*, Lithuanian Mathematical Journal 7 (1967), 409–412. DOI: `10.15388/LMJ.1967.19983`. Primary full text examined for the two random-chord models and moment relation.
3. M. Mayer and I. Molchanov, *A limit theorem for the maximal interpoint distance of a random sample in the unit ball*, arXiv:`math/0605289`, first posted 2006-05-11; full 2006 manuscript examined for boundary sphere/circle specialization.
4. M. Schrempp, *The limit distribution of the largest interpoint distance for distributions supported by an ellipse and generalizations*, arXiv:`1505.01597`, first posted 2015-05-07. The full 2015 preprint was inspected for the Lebesgue-density hypotheses and main statements.
5. NIST Digital Library of Mathematical Functions, §19.12, *Asymptotic Approximations* for Legendre elliptic integrals, equations (19.12.1)–(19.12.3), https://dlmf.nist.gov/19.12 .
