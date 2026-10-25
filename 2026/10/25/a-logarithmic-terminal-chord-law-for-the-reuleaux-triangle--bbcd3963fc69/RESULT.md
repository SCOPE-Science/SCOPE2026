# A logarithmic terminal chord law for the Reuleaux triangle

## Finding

Let \(C_0=(0,0)\), \(C_1=(1,0)\), and \(C_2=(1/2,\sqrt3/2)\). Let \(K=\bigcap_{j=0}^{2}\overline B(C_j,1)\) be the width-one Reuleaux triangle. Choose an unoriented affine line \(\lambda u_\phi+t v_\phi\) with \(\phi\in[0,\pi)\), where \(u_\phi=(\cos\phi,\sin\phi)\) and \(v_\phi=(-\sin\phi,\cos\phi)\), from the invariant measure \(d\phi\,dt\) conditioned on intersecting \(K\). Let \(L\) be the length of its chord of \(K\). Then, as \(\varepsilon\downarrow0\),

\[
\Pr(L>1-\varepsilon)=\frac{3}{\pi}\varepsilon\log(1/\varepsilon)+O(\varepsilon).
\]

In particular the limiting ratio \(\Pr(L>1-\varepsilon)/(\varepsilon\log(1/\varepsilon))\) is \(3/\pi\). The terminal law has an explicit logarithmic enhancement relative to a linear endpoint tail, despite the body having constant width.

## Assumptions and scope

The three generating disks are closed Euclidean unit disks, their centers forming an equilateral triangle of side one. The line measure is uniform in normal angle and offset, not selected by joining random interior or boundary points. Conditioning is on a positive-length intersection with \(K\). Since \(K\) has constant width one, the total unnormalized measure of intersecting lines over \(0\le\phi<\pi\) is exactly \(\pi\). The maximum chord length is the diameter one. The asymptotic constant and remainder refer to this precise probability model.

## Proof

**1. Exact chord intervals and symmetry.** For fixed \(\phi,t\), put \(a_j=C_j\cdot u_\phi\) and \(b_j=C_j\cdot v_\phi\). The intersection of the line with disk \(j\) is, if \(|t-b_j|\le1\), the interval

\[
I_j(\phi,t)=\left[a_j-\sqrt{1-(t-b_j)^2},\ a_j+\sqrt{1-(t-b_j)^2}\right].
\]

Otherwise the chord is empty. The Reuleaux chord is the intersection of these three intervals, with length \(\ell_\phi(t)=\max\{0,\min_j\sup I_j-\max_j\inf I_j\}\). Threefold rotational and reflection symmetry makes the normal angle interval \([0,\pi)\) the union of three equivalent sectors of length \(\pi/3\). In the reference sector \(0\le\phi\le\pi/3\), the line with \(t=0\) contains the unit segment \([0,u_\phi]\) and hence \(\ell_\phi(0)=1\).

**2. Only a narrow offset layer matters.** For \(t\ge0\), the left disk endpoint associated with \(C_1\) is

\[
\cos\phi-\sqrt{1-(t+\sin\phi)^2}\ge0
\]

whenever this disk intersects the line; at \(t=0\) equality holds, and the expression is nondecreasing in \(t\ge0\). For \(t\le0\) the analogous left endpoint for \(C_2\), with \(\beta=\pi/3-\phi\), is

\[
\cos\beta-\sqrt{1-(t-\sin\beta)^2}\ge0.
\]

The disk at the origin bounds the right endpoint by \(\sqrt{1-t^2}\). Thus throughout this angular sector \(\ell_\phi(t)\le\sqrt{1-t^2}\); if \(\ell_\phi(t)>1-\varepsilon\), necessarily \(|t|\le\sqrt{2\varepsilon-\varepsilon^2}\). Consequently an angular boundary strip of width \(O(\sqrt\varepsilon)\) contributes only \(O(\varepsilon)\) to the line measure.

**3. Identify the local active disks.** Fix a sufficiently large constant \(M\). On the angular interior

\[
M\sqrt\varepsilon\le\phi\le\pi/3-M\sqrt\varepsilon,
\]

the right endpoints of the disks centered at \(C_1,C_2\) exceed that of the disk at \(C_0\) at offset zero by quantities bounded below by a positive constant times \(\min\{\phi,\pi/3-\phi\}\). Endpoint derivatives in \(t\) are bounded uniformly for \(|t|\le\sqrt{2\varepsilon}\) in this angular sector, so increasing \(M\) ensures that the right endpoint stays the \(C_0\) endpoint at all relevant offsets. The maximal left endpoint for \(t>0\) is the \(C_1\) endpoint (its first-order slope is \(\tan\phi>0\), while those of \(C_0,C_2\) are respectively zero and negative), and for \(t<0\) it is the \(C_2\) endpoint. Thus for \(s\ge0\) and the relevant \(s\le\sqrt{2\varepsilon}\), the positive-offset chord has length

\[
\ell_\phi(s)=\sqrt{1-s^2}-\cos\phi+\sqrt{1-(s+\sin\phi)^2},
\]

while the negative-offset chord has the same formula with \(\phi\) replaced by \(\beta=\pi/3-\phi\). Convexity of \(K\) implies chord length is concave in the offset; its superlevel set at \(1-\varepsilon\) therefore is an interval containing zero. For fixed \(\alpha\in(0,\pi/3]\), let \(q_\varepsilon(\alpha)\) denote the positive endpoint from the displayed formula, i.e. the root at which the chord length equals \(1-\varepsilon\).

**4. Uniform root expansion and logarithmic integration.** A Taylor expansion with derivatives bounded uniformly on the relevant compact angular and small-offset region gives

\[
1-\left[\sqrt{1-s^2}-\cos\alpha+\sqrt{1-(s+\sin\alpha)^2}\right]
=s\tan\alpha+O(s^2).
\]

For \(\alpha\ge M\sqrt\varepsilon\), the positive root satisfies

\[
q_\varepsilon(\alpha)=\varepsilon\cot\alpha
+O\!\left(\varepsilon^2\cot^3\alpha\right),
\]

uniformly, after taking \(M\) sufficiently large. Indeed the loss is increasing and at least \(s\tan\alpha\), hence \(q_\varepsilon\le\varepsilon\cot\alpha\); substituting this estimate in the uniform quadratic remainder gives the stated bound. The integrated error is

\[
O\!\left(\varepsilon^2\int_{M\sqrt\varepsilon}^{\pi/3}\cot^3\alpha\,d\alpha\right)=O(\varepsilon).
\]

The two offset signs exchange \(\alpha\) and \(\pi/3-\alpha\). Including the previously bounded boundary strips, the total length measure in one angular sector therefore is

\[
\begin{aligned}
\int_0^{\pi/3}\!|\{t:\ell_\phi(t)>1-\varepsilon\}|\,d\phi
&=2\varepsilon\int_{M\sqrt\varepsilon}^{\pi/3-M\sqrt\varepsilon}\cot\alpha\,d\alpha+O(\varepsilon)\\
&=\varepsilon\log(1/\varepsilon)+O(\varepsilon).
\end{aligned}
\]

There are three congruent sectors. Dividing three times this sector measure by the total invariant line measure \(\pi\) proves the asserted law. All bounds above hold uniformly for sufficiently small positive \(\varepsilon\), with absolute constants once \(M\) is fixed.

## Verification

The included standalone `verify_reuleaux_tail.py` builds the three exact disk intervals independently and numerically integrates the superlevel width using bisection and adaptive quadrature. Its numerical test estimates the logarithmic coefficient through the finite-scale difference \((10P(\varepsilon/10)-P(\varepsilon))/(\varepsilon\log10)\), which cancels the subleading linear term in the claimed expansion. At \(\varepsilon=10^{-3}\) and \(10^{-4}\), those estimates were respectively \(0.95426385\) and \(0.95484264\), approaching \(3/\pi\simeq0.95492966\). The numerical checker corroborates, but does not substitute for, the uniform proof above.

## Relationship to prior work

Harutyunyan and Ohanyan (2009) and Bäsel (2012) derive random-chord distributions for ordinary regular polygons under invariant lines. Their objects have straight edges, whereas the present object is the intersection of three disks and the claim concerns its sharp terminal probability. Gates (1987) studies general geometric chord distributions and is potentially relevant, but its full article could not be inspected through available access. In particular, literature priority is not independently certified. The present result is not a consequence of the known terminal laws for disks or ordinary regular polygons through any established reduction in the inspected sources.

## Limitations

This is an asymptotic result only at the maximal chord endpoint; it does not give the entire Reuleaux chord-length distribution, nor a pointwise density expansion. It applies specifically to invariantly sampled affine lines of the planar unit-width Reuleaux triangle; different chord-sampling schemes generally have different laws. The numerical code requires NumPy and SciPy. The closest general 1987 work was available by abstract, not full text, so historical priority remains provisional. Independent peer verification has not been performed.

## References

1. U. Bäsel, *Random chords and point distances in regular polygons*, arXiv:1204.2707 (first publicly posted 12 April 2012), https://arxiv.org/abs/1204.2707.
2. H. S. Harutyunyan and V. K. Ohanyan, *The chord length distribution function for regular polygons*, *Advances in Applied Probability* **41** (2009), 358–366, https://doi.org/10.1239/aap/1246886615.
3. J. Gates, *Some properties of chord length distributions*, *Journal of Applied Probability* **24** (1987), 863–874, https://doi.org/10.2307/3214211 (abstract inspected; full article unavailable during this study).
