# Exact six-class central-section law for right regular pentagonal prisms

## Finding

Let \(P\subset\mathbb R^2\) be a regular pentagon of circumradius \(R>0\), centered at the origin, and let \(K=P\times[-h,h]\), where \(h>0\). For a Haar-uniform unoriented plane through the origin, let \(N\) be the number of sides of the generic polygon \(K\cap U^\perp\), and let \(J\) be the number of its sides lying in the two pentagonal cap faces of \(K\). Set \(q=h/R\), \(\alpha=\pi/5\), and
\[
G_q(t)=\arcsin\!\left(\frac{\sin t}{\sqrt{1+q^2}}\right),\qquad 0\le t\le\frac\pi2.
\]
Define the following five explicitly evaluable numbers:
\[
\begin{aligned}
C_0&=\frac2\alpha G_q(\alpha/2),\\
C_1&=\frac2\alpha\bigl[G_q(\alpha)-G_q(\alpha/2)\bigr],\\
C_2&=\frac2\alpha\bigl[G_q(3\alpha/2)-G_q(\alpha)\bigr],\\
C_3&=\frac2\alpha\bigl[G_q(2\alpha)-G_q(3\alpha/2)\bigr],\\
C_4&=\frac2\alpha\bigl[G_q(5\alpha/2)-G_q(2\alpha)\bigr].
\end{aligned}
\]
**The complete joint law consists of exactly six positive-probability cases, for every \(q>0\):**

| \(N\) | \(J\) | Exact probability |
|---:|---:|---|
| 5 | 0 | \(1-C_0\) |
| 6 | 1 | \(C_0-C_1\) |
| 7 | 2 | \(C_1-C_2\) |
| 6 | 2 | \(C_2-C_3\) |
| 5 | 2 | \(C_3-C_4\) |
| 4 | 2 | \(C_4\) |

In particular, \(N\in\{4,5,6,7\}\) almost surely, all four possibilities have positive probability, and the marginal law is
\[
\begin{aligned}
\Pr(N=4)&=C_4,\\
\Pr(N=5)&=1-C_0+C_3-C_4,\\
\Pr(N=6)&=C_0-C_1+C_2-C_3,\\
\Pr(N=7)&=C_1-C_2.
\end{aligned}
\]
For the **uniform pentagonal prism** (all fifteen edges equal), \(q=\sin(\pi/5)\), and the probabilities in increasing order of \(N=4,5,6,7\) are approximately \(0.248771890074\), \(0.495782910558\), \(0.187721122486\), and \(0.067724076883\), respectively.

## Assumptions and scope

The word *random* refers solely to Haar-uniform **orientation** of a plane constrained to pass through the prism center; no random translational offset is sampled. The cap faces are the two regular pentagons at heights \(\pm h\), and \(J\) counts those met by the section in nonzero-length line segments. Orientations containing a prism vertex or producing other degeneracies form a spherical null set and are excluded from the word *generic*. Scaling \(R,h\) together does not change the law, so only \(q>0\) enters. These statements do not concern all affine planes, oblique prisms, or nonregular pentagonal bases.

## Proof

1. Parameterize one representative of each unoriented plane by the upper-hemisphere unit normal \(n=(\sin\theta\cos\phi,\sin\theta\sin\phi,\cos\theta)\), with \(0<\theta<\pi/2\). Then \(z=\cos\theta\) is uniform on \((0,1)\), independent of uniformly distributed \(\phi\). The plane equation at projected pentagon point \(x\in P\) is \(z_{\mathrm{height}}=-\tan\theta(\cos\phi,\sin\phi)\cdot x\). Therefore the projection of the section is exactly the strip-clipped pentagon
\[
\{x\in P: |(\cos\phi,\sin\phi)\cdot x|\le h\cot\theta\}.
\]
Write the normalized strip threshold \(t=(h/R)\cot\theta\). Its distribution satisfies, for every \(a\ge0\),
\[
\Pr(t\le a)=\frac{a}{\sqrt{q^2+a^2}}=:F_q(a).
\]

2. The dihedral symmetries of the regular pentagon, together with the replacement of a horizontal normal by its opposite (which swaps the two cap faces without changing \(N\) or \(J\)), reduce the azimuth to \(0\le\phi\le\alpha/2\), with uniform density \(2/\alpha\). The signed projections of its five unit-radius vertices are \(b_j=\cos(2j\alpha-\phi)\), \(j=0,1,2,3,4\). For \(0<\phi<\alpha/2\), the three positive projections have indices \(0,1,4\), the two negative projections indices \(2,3\), and their absolute magnitudes have strict decreasing order
\[
\underbrace{\cos\phi}_{j=0}>
\underbrace{\cos(\alpha-\phi)}_{j=3}>
\underbrace{\cos(\alpha+\phi)}_{j=2}>
\underbrace{\cos(2\alpha-\phi)}_{j=1}>
\underbrace{\cos(2\alpha+\phi)}_{j=4}>0.
\]
The inequalities follow because cosine is strictly decreasing on \([0,\pi/2]\) and the displayed five arguments are strictly ordered there.

3. Let \(m_+(t)\) and \(m_-(t)\) be the number of pentagon vertices with projected scalar coordinates greater than \(t\) and less than \(-t\), respectively. The outside vertices on each side of the strip form a consecutive proper run around the convex pentagon's boundary. A run of \(m\ge1\) outside vertices removes exactly \(m-1\) lateral pentagon edges from the strip-clipped polygon, while giving exactly one intersected cap face. Hence
\[
N=5-m_+-m_-+2\bigl({\bf1}_{m_+>0}+{\bf1}_{m_->0}\bigr),\qquad
J={\bf1}_{m_+>0}+{\bf1}_{m_->0}.
\]
As \(t\) decreases past the five ordered absolute vertex projections, the pairs \((m_+,m_-)\) are successively \((0,0),(1,0),(1,1),(1,2),(2,2),(3,2)\), giving \((N,J)=(5,0),(6,1),(7,2),(6,2),(5,2),(4,2)\), respectively. Their conditional probabilities are the differences of \(F_q\) at consecutive thresholds, including the top and bottom tails.

4. Since
\[
\frac{d}{ds}G_q(s)=\frac{\cos s}{\sqrt{q^2+\cos^2s}}=F_q(\cos s),\qquad 0\le s\le\pi/2,
\]
we integrate each conditional threshold probability over the fundamental azimuth wedge. The averaged values of the five descending thresholds are exactly \(C_0,C_1,C_2,C_3,C_4\). Subtracting successive averages and the two tails gives the six table entries. Their sum telescopes to one. Every probability is strictly positive because its corresponding open \((\phi,t)\) region is nonempty and the Haar density is everywhere positive. This proves the full law for all \(q>0\).

5. In a uniform pentagonal prism the base-edge length is \(2R\sin\alpha\), equal to the height \(2h\), whence \(q=\sin\alpha\). Substitution gives the stated numerical probabilities.

## Verification

The accompanying standalone `pentagonal_prism_checker.py` implements the exact functions and compares them with (i) explicit crossing counts for all fifteen three-dimensional prism edges under 180,000 independently sampled normals for each of three aspect ratios, and (ii) independent 20,000-slice midpoint quadrature integrating projection-threshold intervals without the closed-form antiderivative. All tests passed. The largest observed absolute quadrature error was less than \(1.2\times10^{-10}\); the largest Monte Carlo discrepancy was less than \(0.0015\). These finite calculations are checks, not a substitute for the all-orientation argument above.

## Relationship to prior work

Classical stereology studies random affine plane sections of polyhedra and polygon-type frequencies, often integrating over both orientation and translation; conditioning every sampled plane to pass through a fixed center is a different probability law. Socha's freely available six-page article develops a random-section **angle** distribution using isotropic uniform planes, not the present joint cap-incidence/side-count law. Voss's 1982 abstract reports exact polygon-frequency formulas for some simple polyhedra, and Ohser–Mücklich's 1995 abstract treats regular prisms in stationary isotropic ensembles. Both remain substantial historical-priority comparisons because their full texts were unavailable for direct inspection; no claim that their full texts fail to cover this theorem is made. Hug–Schneider's work on spherical/conical tessellations concerns a different random-cone model. A separate published exact central hexagon law for **rectangular boxes** has a different body and no mechanism implying the odd-prism six-class law. Likewise, a mean-square-width formula for regular prisms does not determine central section side counts.

## Limitations

The law is for center-anchored planes only. The classification is generic (measure-zero vertex-containing planes may have other combinatorics). The dimension is three and the planar bases must be regular pentagons. Historical uniqueness has not been independently certified; full texts of Voss (1982) and Ohser–Mücklich (1995), and older stereological numerical tables, pose residual priority risks. The standalone numerical verifier is not an independent audit.

## References

1. D. Hug and R. Schneider, *Random conical tessellations*, arXiv:1508.07768 (public preprint dated 2015-08-31), https://arxiv.org/abs/1508.07768.
2. P. Socha, *Random plane section of a polyhedron*, Acta Stereologica 7 (1988), 41–46, https://www.ias-iss.org/acta/ActaStereologica_pdf/Vol.1.2.5.7.8/VOL%207/NO%201/AS_7_n1_41_SOC.pdf.
3. K. Voss, *Frequencies of n-polygons in planar sections of polyhedrons*, Journal of Microscopy 128 (1982), 111–120, https://doi.org/10.1111/j.1365-2818.1982.tb00443.x.
4. J. Ohser and F. Mücklich, *Stereology for some classes of polyhedrons*, Advances in Applied Probability 27 (1995), 384–396, https://doi.org/10.2307/1427832.
