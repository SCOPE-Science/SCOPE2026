# Denominator-mod-four resonance for alternating islands of rational piecewise rotations

## Finding

For the symmetric two-branch planar isometry \(F_\lambda(z)=\lambda(z-H(z))\), every rational rotation with even reduced denominator \(q\ge4\) and rotation angle strictly between zero and \(\pi\) has a unique primitive two-cycle. The two regular-set components containing its points are congruent open regular polygons, but their number of sides depends sharply on \(q\bmod4\):
\[
N(q)=\begin{cases}q,&q\equiv0\pmod4,\\ q/2,&q\equiv2\pmod4.\end{cases}
\]
Both polygons have inradius \(h=\tfrac12\tan(\pi p/q)\), each has area \(N(q)h^2\tan(\pi/N(q))\), and every point in either component except its center has least period \(q\). Thus the total area of the two alternating components is exactly \(2N(q)h^2\tan(\pi/N(q))\). In particular, the first even-denominator case beyond the previously classified low angles with \(q\equiv2\pmod4\), namely \(q=10\), has regular pentagonal rather than decagonal alternating islands.

## Assumptions and scope

Let \(q\ge4\) be **even** and let integers \(p,q\) satisfy \(1\le p<q/2\) and \(\gcd(p,q)=1\). Set \(\lambda=\exp(2\pi i p/q)\), \(\theta=2\pi p/q\), and
\[
H(z)=\begin{cases}1,&\operatorname{Im}z\ge0,\\-1,&\operatorname{Im}z<0.\end{cases}
\]
Consider \(F_\lambda:\mathbb C\to\mathbb C\) given by \(F_\lambda(z)=\lambda(z-H(z))\). Let \(\mathcal C=\bigcup_{n\ge0}F_\lambda^{-n}(\mathbb R)\), and let the regular set be \(U=\mathbb C\setminus\overline{\mathcal C}\). We classify the two components of \(U\) whose symbols alternate strictly between upper and lower half-planes, including their centers, exact shape, area, and pointwise periods. No claim is made that these two components exhaust \(U\) or its periodic islands.

Define \(h=\frac12\tan(\theta/2)>0\) and \(u=\frac{\lambda}{1+\lambda}=\frac12+ih\). For \(\delta\in\mathbb C\) set
\[
P_+=\left\{u+\delta:\ \operatorname{Im}(\lambda^{2j}\delta)>-h,\quad
\operatorname{Im}(\lambda^{2j+1}\delta)<h\quad(0\le j<q/2)\right\},\qquad P_-=-P_+.
\]
All inequalities are strict; polygon boundaries belong to the excluded critical set or its closure, and boundary orbit periods are not classified here.

## Proof

**1. Unique primitive two-cycle.** As \(\lambda^2\ne1\), a prescribed two-symbol itinerary has at most one solution to \(F_\lambda^2(z)=z\). A constant \(+,+\) or \(-,-\) itinerary would be a fixed point of its corresponding one-branch rotation and therefore cannot be primitive period two. Direct substitution yields
\[
F_\lambda(u)=\lambda(u-1)=-u,\qquad F_\lambda(-u)=\lambda(-u+1)=u.
\]
Since \(\operatorname{Im}u=h>0\), these are the admissible \(+,-\) and \(-,+\) solutions; thus \(\{u,-u\}\) is the unique primitive two-cycle.

**2. Exact maximal alternating cells.** Suppose \(z=u+\delta\) follows the strict alternating itinerary \((+,-,+,-,\ldots)\). The affine branch equations and the two-cycle identities give, by induction,
\[
F_\lambda^{2j}(z)=u+\lambda^{2j}\delta,\qquad
F_\lambda^{2j+1}(z)=-u+\lambda^{2j+1}\delta.
\]
The required signs are precisely the defining inequalities for \(P_+\). Conversely, those inequalities imply inductively that each iterate uses the stipulated branch. The conditions repeat every \(q\) steps; the intersection of the listed \(q\) open half-planes therefore gives **all**, not merely some, points with this itinerary. It is a nonempty bounded convex open polygon containing \(u\). The opposite itinerary gives \(P_-\), and odd symmetry of \(F_\lambda\) away from the real axis gives \(F_\lambda(P_+)=P_-\) and \(F_\lambda(P_-)=P_+\).

Every point in \(P_+\cup P_-\) has a finite orbit disjoint from \(\mathbb R\), hence lies in the regular set \(U\). Each connected component of \(U\) has constant itinerary, because no iterate can cross \(\mathbb R\) continuously within that component. Consequently \(P_+\) and \(P_-\), already the complete strict alternating itinerary cells, are exactly two connected components of \(U\).

**3. Arithmetic normal-direction dichotomy.** Writing \(\operatorname{Im}(a\delta)=\operatorname{Re}(\overline{(i\overline a)}\delta)\) for \(|a|=1\), each defining half-plane is an inward supporting half-plane at distance \(h\) from \(u\). The outward unit normals, in displacement coordinates, are
\[
\mathcal N_0=\{-i\overline\lambda^{2j}:0\le j<q/2\},\qquad
\mathcal N_1=\{i\overline\lambda^{2j+1}:0\le j<q/2\}.
\]
Since \(\gcd(p,q)=1\), the even powers of \(\lambda\) traverse all \(q/2\)-th roots of unity. If \(4\mid q\), the two sets of outward normals are disjoint and their union consists of all \(q\) equally spaced unit directions. If \(q\equiv2\pmod4\), then \(-1=\lambda^{q/2}\) is an **odd** power of \(\lambda\), so \(\mathcal N_0=\mathcal N_1\); there are precisely \(q/2\) equally spaced directions. Thus \(P_+\) is the open regular \(N(q)\)-gon of inradius \(h\); \(P_-\) is its half-turn image. The area formula for a regular \(N\)-gon of inradius \(h\) is \(Nh^2\tan(\pi/N)\), proving the asserted individual and total areas.

**4. Exact periods.** For every \(z=u+\delta\in P_+\), the two-step return acts as \(F_\lambda^2(z)=u+\lambda^2\delta\). The multiplier \(\lambda^2\) has exact order \(q/2\). If \(\delta\ne0\), the least period under this return is \(q/2\). Since \(F_\lambda\) exchanges the disjoint sets \(P_+\) and \(P_-\), a return under \(F_\lambda\) can only occur at an even iterate. Its least period is therefore exactly \(q\); at \(\delta=0\) it is two.

## Verification

The companion `verify.py` checks the exact itinerary formula numerically for every coprime pair \((p,q)\) with even \(4\le q\le34\) and \(1\le p<q/2\). For each pair it constructs the supporting directions, counts distinct normals, computes the polygon area by vertices, and verifies period-\(q\) sample returns and strict alternating signs. It also verifies the two-cycle identities. The proof above, not the finite tests, establishes all even denominators.

## Relationship to prior work

Cima, Gasull, Mañosa, and Mañosas established the global regular-set periodicity theorem and the \(q\)-side upper bound for even-denominator rational piecewise rotations, along with a regular \(q\)-gon result when the component-cycle period is coprime to \(q\). Our alternating cells have component period **two**, which is never coprime to even \(q\). The proof resolves their otherwise uncovered case explicitly, and its \(q/2\)-side branch does not follow from that coprime-period theorem. Goetz and Quas gave an earlier polygon classification under the same coprimality condition (Lemma 11); it likewise does not imply the even-denominator period-two branch. Cima and collaborators classified specific low-angle examples, including \(\pi/2\) and \(\pi/3\), for which the square and triangle cases were already known. The present claim is the uniform infinite-denominator law and its area/period profile, particularly the pentagon and higher odd polygons at \(q\equiv2\pmod4\); it does not claim those two classical examples as new.

## Limitations

No classification is asserted for irregular components, nonalternating symbolic itineraries, critical-line points, irrational rotations, or denominators that are odd. The result does not improve the general \(q\)-side upper bound for arbitrary components; it identifies an exact natural subfamily. Equivalent formulations in unindexed literature, including work on outer billiards or discrete bang-bang recurrences, remain a priority risk. No independent scientific audit has occurred.

## References

1. A. Cima, A. Gasull, V. Mañosa, F. Mañosas, *On some rational piecewise linear rotations*, arXiv:2306.17543 (first public 2023-06-30); *Journal of Difference Equations and Applications* 30 (2024), 1577–1589, DOI:10.1080/10236198.2023.2260898. Author-archived full text: https://ddd.uab.cat/pub/artpub/2024/307719/CimGasManMan2023a-Postprint.pdf.
2. A. Goetz and A. Quas, *Global properties of a family of piecewise isometries*, *Ergodic Theory and Dynamical Systems* 29 (2009), 545–568, DOI:10.1017/S0143385708080280. Author full text: https://web.uvic.ca/~aquas/papers/paper28.pdf; especially Lemma 11.
3. A. Cima, A. Gasull, V. Mañosa, F. Mañosas, *Pointwise periodic maps with quantized first integrals*, arXiv:2010.12901, published in *Communications in Nonlinear Science and Numerical Simulation* 108 (2022), 106150.
