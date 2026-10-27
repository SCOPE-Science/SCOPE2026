# Sharp peak splitting in symmetric binary-source gravitational microlensing

## Finding

For a single point-mass gravitational lens and two static, equal-flux, pointlike background sources with the same positive impact parameter, there is **exactly one** separation threshold between a one-peaked and a two-peaked ideal magnification curve. With impact parameter \(b>0\) and half the separation in peak times, measured in Einstein-crossing time units, denoted \(s\geq0\), this threshold is

\[
 s_*(b)=\left(\frac{\sqrt{9b^4+36b^2+16}-2b^2-4}{5}\right)^{1/2}.
\]

The sum is strictly single-peaked for \(0\leq s<s_*(b)\); at equality its unique central maximum is quartically degenerate; and for \(s>s_*(b)\) its central point becomes a strict local minimum and it has exactly two symmetric strict global maxima. No third local maximum or intermediate three-peak regime occurs for any \(b>0\). The physical time separation required for distinct maxima is strictly greater than \(2s_*(b)t_E\), where \(t_E\) is the Einstein crossing time.

The boundary also satisfies the sharp scale bounds

\[
 \frac{b}{\sqrt5}<s_*(b)<\frac{b}{\sqrt2},\qquad
 \lim_{b\to0^+}\frac{s_*(b)}b=\frac1{\sqrt2},\qquad
 \lim_{b\to\infty}\frac{s_*(b)}b=\frac1{\sqrt5}.
\]

At onset, if \(t_+(s)>0\) is the time of the newly formed positive peak, then, with \(D=2b^2+4\),

\[
 t_+(s)=\sqrt{\frac{18s_*(5s_*^2+D)}{5s_*^2+7D}}\;\sqrt{s-s_*}
 +O\big((s-s_*)^{3/2}\big)\quad(s\downarrow s_*).
\]

Here \(s_*\) abbreviates \(s_*(b)\). This is an exact bifurcation classification of the ideal curve, not a statistical detection guarantee.

## Assumptions and scope

The point-lens amplification is the standard Paczyński function

\[
 M(u)=\frac{u^2+2}{u\sqrt{u^2+4}},\qquad u>0.
\]

In dimensionless centered time \(t\in\mathbb R\), the two projected lens-source separations are \(u_\pm(t)=\sqrt{b^2+(t\mp s)^2}\). The non-orbiting sources have equal unlensed fluxes and positive common impact parameter \(b\); their common Einstein time is scaled to one. The normalized combined flux is

\[
 F_{b,s}(t)=\frac12\big[M(u_+(t))+M(u_-(t))\big].
\]

Constant additional blending does not alter peak locations as long as the source-flux scaling remains positive. Unequal brightnesses or impact parameters, source orbital motion, finite stellar radii, parallax and multiple lenses are not covered. All statements quantify over every real \(b>0\), every \(s\geq0\), and all real observation times \(t\).

## Proof

**1. Shape at the center.** Set \(B=b^2>0\), \(C=b^2+4>0\), \(D=B+C\) and \(Q(z)=(z^2+B)(z^2+C)\). Define \(g(z)=M(\sqrt{b^2+z^2})\). Direct differentiation gives

\[
 g'(z)=-\frac{8z}{Q(z)^{3/2}},\qquad
 g''(z)=\frac{8[5z^4+2Dz^2-BC]}{Q(z)^{5/2}}.
\]

The bracket is strictly increasing as a function of \(z^2\ge0\) and has one positive zero. Thus \(F''_{b,s}(0)=g''(s)\) changes from negative to positive only at \(s=s_*(b)\). Solving \(5s^4+2Ds^2-BC=0\) yields the stated radical. Its radicand is positive for every \(b>0\).

**2. Exhaustive stationary-point count.** For \(z\ge0\), let \(h(z)=z/Q(z)^{3/2}\). For \(0<t<s\),

\[
 F'_{b,s}(t)=4\{h(s-t)-h(s+t)\}.
\]

For \(t\ge s>0\), the derivative is strictly negative, so every noncentral stationary point is inside \((0,s)\) or its reflection. Within \((0,s)\), stationarity is equivalent to \(h(s-t)=h(s+t)\). Put \(w=((s+t)/(s-t))^{1/3}>1\), \(y=w+w^{-1}>2\), and \(x=s-t=2s/(1+w^3)\). Since \(h(x)=h(w^3x)\), raising positive quantities to the power \(2/3\), substituting \(Q\), and cancelling \(w^2-1\) gives exactly

\[
 16s^4\alpha(y)+4s^2D\beta(y)-BC=0,
\]

where

\[
 \alpha(y)=\frac{y^4-3y^2+1}{(y^3-3y+2)^2},\qquad
 \beta(y)=\frac{y}{y^3-3y+2}.
\]

These transformations are reversible for \(0<t<s\): in particular, every \(y>2\) determines exactly one \(w>1\), hence one \(t\in(0,s)\). Differentiation yields

\[
 \beta'(y)=-\frac{2(y^2+y+1)}{(y-1)^3(y+2)^2}<0,
\]

and

\[
 \alpha'(y)=-\frac{2P(y)}{(y-1)^5(y+2)^3}<0,
\]

with \(P(y)=y^5+y^4-2y^3-6y^2-3y+3\). Writing \(v=y-2>0\) gives the positive-coefficient expansion

\[
 P(y)=v^5+11v^4+46v^3+86v^2+61v+5>0.
\]

Therefore the stationary-point equation has a strictly decreasing left-minus-right side on \((2,\infty)\). Its value at \(y=2\) is \(5s^4+2Ds^2-BC\) and its limit as \(y\to\infty\) is \(-BC\). It has exactly one solution \(y>2\) if \(s>s_*\), and none if \(s\le s_*\). Because \(F'(t)<0\) for \(t\ge s\), and the curve is even, this exhausts all stationary points.

**3. Mode classification and critical equality.** For \(s<s_*\), the center has negative second derivative and no other stationary point, hence is the unique strict global maximum. For \(s>s_*\), it has positive second derivative, and the unique positive stationary point must change the derivative from positive to negative: it is a strict global maximum, as is its reflection. At \(s=s_*\), the center has vanishing second derivative. Writing \(r=s_*\) and using \(Q(r)=3r^2(2r^2+D)\), direct differentiation gives

\[
 g^{(4)}(r)=-\frac{32r^2(2r^2+D)(5r^2+7D)}{Q(r)^{7/2}}<0.
\]

Thus the center is a quartically degenerate but strict global maximum at equality. The decay \(F_{b,s}(t)\to1\) at \(|t|\to\infty\) confirms the global classification.

**4. Square-root opening.** At criticality \(g'''(r)=32r(5r^2+D)/Q(r)^{5/2}>0\). Taylor expansion of \(F'_{b,s}(t)/t\) at \((t^2,s)=(0,r)\) gives \(g'''(r)(s-r)+g^{(4)}(r)t^2/6+O((s-r)^2+|s-r|t^2+t^4)\). Its simple zero in \(t^2\) yields

\[
 t_+^2=\frac{18r(5r^2+D)}{5r^2+7D}(s-r)+O((s-r)^2),
\]

which gives the stated expansion after taking the positive square root.

**5. Sharp impact-parameter bounds.** Put \(z=s_*^2/b^2\), \(B=b^2\). The critical equation is equivalent to

\[
 B(5z^2+4z-1)+4(2z-1)=0.
\]

The left side is negative at \(z=1/5\), positive at \(z=1/2\), and strictly increasing for \(z>0\). Therefore \(1/5<z<1/2\). Taking \(B\to0^+\) and \(B\to\infty\) yields the respective sharp limiting values.

## Verification

Run `python verify.py` using Python 3 and the standard library. The file checks the two rational derivative identities exactly at 199 distinct rational arguments, samples 180,000 derivative/brightness comparisons across 1,200 randomly selected positive geometries, and verifies the analytic benchmark and onset coefficient. All checks passed when run from the complete package. These finite tests are consistency checks, not the proof of the universal quantifiers.

For example, at \(b=1\), \(s_* =\sqrt{(\sqrt{61}-6)/5}\approx0.601705854369\). If \(s=0.8\), the two peak times are approximately \(t=\pm0.630876026959\); the peak flux is \(1.210408120976\) and the central flux is \(1.196850505712\). At \(s=0.5\), there is one central maximum. The exact boundary corresponds to a separation of approximately \(1.203411708737\) Einstein times.

## Relationship to prior work

Han and Jeong (1998, original public preprint 1998-04-26) give the same point-lens amplification and two-source superposition formula in their equations (1), (3), (4), and study source-separation effects using realistic detection simulations. Their analysis discusses close sources mimicking one event, but does not state this ideal equal-flux, equal-impact, global mode-count threshold or critical square-root law. Skowron, Wyrzykowski, Mao and Jaroszyński (2009) fit binary-source sums to actual repeating microlensing light curves; their Section 4 uses the corresponding two-component model, rather than a universal analytical one-/two-peak classifier. Rattenbury (2008) studies deformed close binary source profiles, not the present ideal symmetric peak splitting.

The earlier Griest–Hu (1992) binary-source analysis is especially relevant historically: it classifies double-peaked events and their detection frequencies. The complete original paper was not available for direct full-text comparison here, so an unrecognized earlier special-case threshold remains a historical-priority risk. The claim of novelty is restricted to this explicit complete analytic classification and onset law, not to binary-source microlensing, superposition, or the possibility of double peaks.

## Limitations

This is a theorem about continuous, noiseless, point-source, equal-brightness, equal-impact, static binary-source curves. A mathematical pair of maxima need not be distinguishable with finite cadence or signal-to-noise. Projection to unequal impact parameters or source fluxes is not addressed. A broader theorem about modes of equal translates of rational scale mixtures may subsume some qualitative assertions; no such exact implication was established in the inspected sources. The original 1992 full text was inaccessible, so historical originality is provisional. No empirical event is newly fitted or classified.

## References

1. Han, C., and Jeong, Y. (1998), *Where Are the Binary Source Gravitational Microlensing Events? II*, arXiv:astro-ph/9804273v1, first public 1998-04-26, https://arxiv.org/abs/astro-ph/9804273 . Full 10-page original preprint inspected, especially pages 3–7.
2. Skowron, J., Wyrzykowski, Ł., Mao, S., and Jaroszyński, M. (2009), *Repeating microlensing events in the OGLE data*, MNRAS 393, 999–1009, https://doi.org/10.1111/j.1365-2966.2008.14245.x . Full accessible HTML inspected, especially Sections 1, 4, 5.
3. Rattenbury, N. J. (2008), *Microlensing of close binary stars*, MNRAS 392, 439–447, https://doi.org/10.1111/j.1365-2966.2008.14074.x . Accessible HTML inspected, especially model assumptions and Section 3.
4. Griest, K., and Hu, W. (1992), *Effect of Binary Sources on the Search for Massive Astrophysical Compact Halo Objects via Microlensing*, ApJ 397, 362–380, https://doi.org/10.1086/171793 . Abstract and subsequent primary-work descriptions checked; original full text not inspected.
