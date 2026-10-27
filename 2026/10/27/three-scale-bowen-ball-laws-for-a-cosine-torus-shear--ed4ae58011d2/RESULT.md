# Three-scale Bowen-ball laws for a cosine torus shear

## Finding
For the smooth, Haar-preserving torus map
\[
F_a(x,y)=(x,y+a\cos(2\pi x))\pmod1,
\qquad 0<a<\tfrac18,
\]
there are three distinct exact scales of orbit proximity. Equip \(\mathbb T^2\) with the maximum of circular distances and normalized Haar area \(\lambda\). For fixed \(0<\varepsilon<1/8\), write
\[
B_n(z,\varepsilon)=\{w:\max_{0\le j\le n}d_\infty(F_a^jz,F_a^jw)<\varepsilon\},\quad
\mathcal C_n(\varepsilon)=\int_{\mathbb T^2}\lambda(B_n(z,\varepsilon))\,d\lambda(z).
\]
For every \(x\in\mathbb T\) with \(\sin(2\pi x)\ne0\) and \(\|2x\|_{\mathbb T}\ne\varepsilon\), uniformly in the fiber coordinate \(y\),
\[
\boxed{\lim_{n\to\infty}n\lambda(B_n((x,y),\varepsilon))
=\frac{2\varepsilon^2}{\pi a|\sin(2\pi x)|}
\bigl(1+\mathbf1_{\{\|2x\|_{\mathbb T}<\varepsilon\}}\bigr).}
\]
At the two critical base points \(x=0,\tfrac12\), the different exponent is
\[
\boxed{\lim_{n\to\infty}\sqrt n\,\lambda(B_n((x,y),\varepsilon))
=\frac{8\varepsilon^{3/2}}{3\pi\sqrt a}.}
\]
Nevertheless the spatial average has a sharp logarithmic enhancement:
\[
\boxed{\mathcal C_n(\varepsilon)
=\frac{4\varepsilon^2}{a\pi^2}\frac{\log n}{n}
+O_{a,\varepsilon}(n^{-1}).}
\]
Thus typical centers have Bowen mass of order \(n^{-1}\), the two extrema have order \(n^{-1/2}\), and the two-point orbit-proximity probability has order \((\log n)/n\), with an explicit coefficient. This is a metric-and-measure-specific quantitative result, not an assertion that the already known polynomial-entropy exponent is new.

## Assumptions and scope
Here \(\mathbb T=\mathbb R/\mathbb Z\) and \(\|u\|_{\mathbb T}=\min_{k\in\mathbb Z}|u-k|\). The product metric is \(d_\infty((x,y),(x',y'))=\max(\|x-x'\|_{\mathbb T},\|y-y'\|_{\mathbb T})\). The parameter \(a\) and radius \(\varepsilon\) are fixed as \(n\to\infty\); the stated error constant is allowed to depend on them. The time window is precisely all integer observations \(0,1,\ldots,n\). Circle Haar area is probability normalized. The indicator and exclusion of the finitely many equality cases in the regular-center law are intentional. Every statement applies to either strict or nonstrict Bowen inequalities as far as area is concerned.

## Proof
**1. An exact two-point reduction.** Lift the initial base difference to \(h\in(-\varepsilon,\varepsilon)\) and the initial fiber difference to \(\eta\in(-\varepsilon,\varepsilon)\). Set \(\phi(x)=a\cos(2\pi x)\) and \(\Delta=\phi(x+h)-\phi(x)\). The lifted fiber difference after \(j\) iterates is \(\eta+j\Delta\). Since \(|\Delta|\le2a<1/4\), whereas distinct radius-\(\varepsilon\) integer neighborhoods are separated by \(1-2\varepsilon>3/4\), a trajectory of fiber differences initially within \(\varepsilon\) of zero and remaining within \(\varepsilon\) modulo one cannot switch its nearest integer. Hence the Bowen conditions are exactly \(|h|<\varepsilon\) and \(|\eta+j\Delta|<\varepsilon\) as *real* inequalities for all observed \(j\). The maximum of the absolute value of an affine function on \([0,n]\) is at an endpoint, so integrating over \(\eta\) yields
\[
\lambda(B_n((x,y),\varepsilon))
=\int_{-\varepsilon}^{\varepsilon}
\bigl(2\varepsilon-n|\phi(x+h)-\phi(x)|\bigr)_+\,dh.\tag{1}
\]
The expression is independent of \(y\). The identity
\[
\phi(x+h)-\phi(x)=-2a\sin(\pi h)\sin(2\pi x+\pi h)\tag{2}
\]
will also be used below.

**2. Pointwise regular centers.** For fixed \(x\) with \(\sin(2\pi x)\ne0\), solutions of \(\phi(x+h)=\phi(x)\) on \((-\varepsilon,\varepsilon)\) are \(h=0\) and, if \(\|2x\|_{\mathbb T}<\varepsilon\), the unique representative of \(-2x\pmod1\) in that interval. At noncritical \(x\) these roots are simple, and \(|\phi'(x+h)|=2\pi a|\sin(2\pi x)|\) at both. For a simple root \(h_0\), the change of variable \(u=n(\phi(x+h)-\phi(x))\), localized to a small fixed neighborhood, shows
\[
\lim_{n\to\infty}n\int_{\text{near }h_0}
(2\varepsilon-n|\phi(x+h)-\phi(x)|)_+\,dh
=\frac1{|\phi'(x+h_0)|}
\int_{-2\varepsilon}^{2\varepsilon}(2\varepsilon-|u|)\,du
=\frac{4\varepsilon^2}{|\phi'(x+h_0)|}.
\]
The integrand vanishes outside neighborhoods of these roots for all sufficiently large \(n\). Summing their contributions proves the displayed pointwise law. When \(\|2x\|_{\mathbb T}=\varepsilon\), a root lies on the boundary and the full-root formula is not asserted.

**3. Critical centers.** At \(x=0\) or \(x=1/2\), the only root in \((-\varepsilon,\varepsilon)\) is \(h=0\), and
\[
|\phi(x+h)-\phi(x)|=a(1-\cos(2\pi h))=2a\pi^2h^2+O_a(h^4).
\]
Putting \(h=t/\sqrt n\) in (1), the support is uniformly bounded in the \(t\)-variable for all sufficiently large \(n\), by the quadratic lower bound near zero. Dominated convergence gives
\[
\lim_{n\to\infty}\sqrt n\,\lambda(B_n((x,y),\varepsilon))
=\int_{\mathbb R}(2\varepsilon-2a\pi^2t^2)_+\,dt
=\frac{8\varepsilon^{3/2}}{3\pi\sqrt a}.
\]

**4. Exact arcsine integral for the spatial average.** Substitute \(m=x+h/2\) in (2); modulo one the map \((x,h)\mapsto(m,h)\) preserves area. For \(B\ge0\) let
\[
K(B)=\int_0^1(2\varepsilon-B|\sin(2\pi m)|)_+\,dm.
\]
The distribution of \(|\sin(2\pi m)|\) for uniform \(m\) has distribution function \(2\arcsin(s)/\pi\) on \([0,1]\). Direct integration gives the exact formulas
\[
K(B)=\begin{cases}
2\varepsilon-2B/\pi,&0\le B\le2\varepsilon,\\[2mm]
\dfrac2\pi\left(2\varepsilon\arcsin\dfrac{2\varepsilon}{B}
-B\left(1-\sqrt{1-\dfrac{4\varepsilon^2}{B^2}}\right)\right),&B>2\varepsilon.
\end{cases}\tag{3}
\]
Therefore
\[
\mathcal C_n(\varepsilon)=2\int_0^{\varepsilon}K(2an\sin(\pi h))\,dh.\tag{4}
\]

**5. The logarithmic coefficient and controlled remainder.** For sufficiently large \(n\), put \(h_n=\pi^{-1}\arcsin(2\varepsilon/(an))\). On \([0,h_n]\) the integral in (4) is \(O_{a,\varepsilon}(n^{-1})\) because \(0\le K\le2\varepsilon\) and \(h_n=O(n^{-1})\). For \(h\in[h_n,\varepsilon]\), one has \(2an\sin(\pi h)\ge4\varepsilon\). Taylor's theorem applied to (3), uniformly on this range, gives
\[
K(B)=\frac{4\varepsilon^2}{\pi B}
+O_\varepsilon(B^{-3}).\tag{5}
\]
As \(\sin(\pi h)\ge2h\) for \(0\le h\le1/2\), the integral of the remainder in (5) is bounded by
\[
O_{a,\varepsilon}\left(n^{-3}\int_{h_n}^{\varepsilon}h^{-3}\,dh\right)
=O_{a,\varepsilon}(n^{-1}).
\]
Equations (4)--(5) now yield
\[
\mathcal C_n(\varepsilon)=\frac{4\varepsilon^2}{a\pi n}
\int_{h_n}^{\varepsilon}\frac{dh}{\sin(\pi h)}
+O_{a,\varepsilon}(n^{-1}).
\]
Finally, the antiderivative \(\pi^{-1}\log\tan(\pi h/2)\) and \(h_n\asymp n^{-1}\) give
\[
\int_{h_n}^{\varepsilon}\frac{dh}{\sin(\pi h)}
=\frac{\log n}{\pi}+O_{a,\varepsilon}(1),
\]
proving the claimed sharp average asymptotic.

## Verification
Run `python3 verify_bowen.py` in a standard Python 3 environment. It checks 1,640 independent cosine-difference identities, sampled modular lifting/endpoint equivalences, the analytic arcsine integral against independent circle quadrature, and the finite-\(n\) exact one-dimensional integral against its logarithmic coefficient at several observation lengths. The corresponding actual output is in `verify_bowen_output.txt`. These numerical checks do not replace the analytical proof of any limit, error bound, or statement for every parameter.

## Relationship to prior work
Corrêa, *Polynomial entropy and rotation sets* (first public version verified 12 September 2026), defines Bowen balls and establishes a lower polynomial-entropy bound for torus maps with nontrivial rotation sets; its Section 5 studies frozen-base skew translations at the level of polynomial entropy. The published result does not give the Haar-averaged two-point Bowen correlation, the critical-center \(n^{-1/2}\) law, or their exact constants. The previously published published-finding corpus analysis *Polynomial entropy equals velocity-image box dimension for frozen-base torus translations* establishes the general entropy exponent from the velocity image, but its inspected proof concerns covering and separated sets, not averaged Bowen-ball volumes. The published-finding corpus results *Universal Bowen-ball volume law for irrational skew Dehn twists* and *Sharp Haar Bowen-ball constants for unipotent Jordan toral dynamics* establish different sharp local laws respectively for a nonzero-degree irrational-base skew system and a linear unipotent map; neither applies to a degree-zero frozen-base cosine shear or implies the nonuniform three-scale law above. Classical arcsine and cosine-product identities are used as known elementary facts, not claimed new.

## Limitations
These are quantitative metric-dependent laws for this explicit cosine shear and product maximum metric; they are not conjugacy-invariant constants. Neither topological entropy zero nor polynomial entropy one is newly asserted here; those are consequences of prior general results. The conclusions do not treat arbitrary nonlinear shears, non-Haar reference measures, shrinking \(\varepsilon\) jointly with \(n\), or uniformity as \(a\downarrow0\). The exact regular-center formula omits the specified exceptional base points where a root meets the boundary; at the critical points a separate law is proved. A historically broader correlation-integral theorem could subsume the result despite the targeted comparisons. No independent mathematical audit has been performed.

## References
1. H. Corrêa, *Polynomial entropy and rotation sets*, Archiv der Mathematik, first publicly verified 12 September 2026, https://doi.org/10.1007/s00013-026-02286-3 (especially Sections 2 and 5).
2. *Polynomial entropy equals velocity-image box dimension for frozen-base torus translations*, published published-finding corpus mathematical record (11 October 2026), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-polynomial-entropy-equals-velocity-image-box-dimension-for-froze--2c91fbb3a44a.
3. *Universal Bowen-ball volume law for irrational skew Dehn twists*, published published-finding corpus mathematical record (11 October 2026), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-universal-bowen-ball-volume-law-for-irrational-skew-dehn-twists--9c651d44a4c2.
4. *Sharp Haar Bowen-ball constants for unipotent Jordan toral dynamics*, published published-finding corpus mathematical record (11 October 2026), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-sharp-haar-bowen-ball-constants-for-unipotent-jordan-toral-dynam--ab1c4e92842d.
