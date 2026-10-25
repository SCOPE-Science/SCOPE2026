# The complete Haar central-section polygon law of a regular pentagonal prism

## Finding

Let \(h>0\), and let the right regular pentagonal prism of circumradius one and half-height \(h\) be
\[
K_h=\operatorname{conv}\left\{\left(\cos\frac{2\pi j}{5},\sin\frac{2\pi j}{5},\pm h\right):j=0,1,2,3,4\right\}.
\]
Choose a plane through the origin with its unoriented normal distributed according to the rotation-invariant probability measure, and let \(N_h\) denote the number of edges of the resulting section. Set \(\delta=\pi/10\),
\[
F_h(\theta)=\arcsin\left(\frac{\sin\theta}{\sqrt{1+h^2}}\right),\qquad
\Delta_j=F_h(j\delta)-F_h((j-1)\delta),\quad 1\le j\le5.
\]
**Theorem.** For every \(h>0\), the section is almost surely a quadrilateral, pentagon, hexagon, or heptagon, and the complete probabilities are
\[
\boxed{\begin{aligned}
\Pr(N_h=4)&=\frac{\Delta_5}{\delta},\\
\Pr(N_h=5)&=1+\frac{\Delta_4-\Delta_5-\Delta_1}{\delta},\\
\Pr(N_h=6)&=\frac{\Delta_3-\Delta_4+\Delta_1-\Delta_2}{\delta},\\
\Pr(N_h=7)&=\frac{\Delta_2-\Delta_3}{\delta}.
\end{aligned}}
\]
Each of these four probabilities is strictly positive. In particular, for the *uniform* pentagonal prism (all edges equal), \(h=\sin(\pi/5)\), they are, in side-count order \(4,5,6,7\),
\[
(0.2487718900737403\ldots,\ 0.4957829105575425\ldots,\ 0.1877211224861567\ldots,\ 0.0677240768825605\ldots).
\]
The expected number of sides is also exactly
\[
\boxed{\mathbb E N_h=\frac{10}{\pi}\left[\arctan h+
\arccos\left(\frac{h^2+\cos(2\pi/5)}{1+h^2}\right)\right].}
\]
There is a sharp, nonmonotone aspect dependence of the heptagon probability. With \(\delta=\pi/10\),
\[
\Pr(N_h=7)=\frac{\tan\delta+\tan3\delta-2\tan2\delta}{2\delta}\,h^2+O(h^4)
\quad(h\downarrow0),
\]
and
\[
\Pr(N_h=7)=\frac{2\sin2\delta-\sin\delta-\sin3\delta}{\delta h}
+O(h^{-3})\quad(h\to\infty).
\]
The leading coefficients are respectively \(0.395048925916\ldots\) and \(0.183144418069\ldots\), both positive.

## Assumptions and scope

The distribution is on *central* planes, not affine planes chosen with random offset. Orientations are Haar-uniform on the Grassmannian of two-dimensional linear subspaces of \(\mathbb R^3\). Degenerate planes passing through prism vertices or containing prism edges form a measure-zero set. The central plane is not required to cut the prism into equal-volume pieces: a regular pentagonal prism is not centrally symmetric. All side counts refer to the section polygon, not to the prism's faces. The arbitrary positive parameter \(h\) permits all positive aspect ratios, but the base remains a regular pentagon.

## Proof

**1. Independently count crossing edges.** A generic section vertex lies on exactly one prism edge. Represent a plane by a normal \(u=(r\cos\phi,r\sin\phi,z)\) with \(z\ge0\), \(r=\sqrt{1-z^2}\), and put \(t=hz/r\). Define \(s_j=\cos(\phi-2\pi j/5)\). The vertex values of the plane functional at the upper and lower pentagons are \(r(s_j+t)\) and \(r(s_j-t)\). The \(j\)-th vertical edge is crossed exactly when \(|s_j|<t\). Each horizontal pentagonal cap has either zero or two of its five edges crossed, since a generic line meets the boundary of a convex pentagon in zero or two points. The upper cap is crossed precisely when \(\min_j s_j<-t\) (its maximum is positive), and the lower cap is crossed precisely when \(\max_j s_j>t\) (its minimum is negative). Consequently,
\[
N_h=\sum_{j=0}^{4}{\bf1}_{\{|s_j|<t\}}
+2{\bf1}_{\{\max s_j>t\}}
+2{\bf1}_{\{-\min s_j>t\}}.
\tag{1}
\]
This identity directly counts all fifteen prism edges, without invoking a special section-type classification.

**2. Reduce the azimuth to one short sector.** A regular-pentagon rotation relabels the \(s_j\), reflection reverses their order, and the azimuthal shift \(\phi\mapsto\phi+\pi\) changes their signs, swapping the two cap indicators in (1). Thus \(N_h\) is invariant under the resulting order-ten dihedral action on azimuths. It suffices to take \(\phi\) uniform on \((0,\delta)\), where \(\delta=\pi/10\). In this sector the five positive thresholds are strictly ordered:
\[
0<E=\cos(4\delta+\phi)
<C=\cos(4\delta-\phi)
<D=\cos(2\delta+\phi)
<B=\cos(2\delta-\phi)
<M=\cos\phi.
\tag{2}
\]
The last two thresholds \(B,M\) are respectively \(-\min s_j\) and \(\max s_j\); the five thresholds \(E,C,D,B,M\) together are the sorted \(|s_j|\). Equation (1) therefore gives the six interval values
\[
\begin{array}{c|cccccc}
t&(0,E)&(E,C)&(C,D)&(D,B)&(B,M)&(M,\infty)\\\hline
N_h&4&5&6&7&6&5.
\end{array}
\tag{3}
\]
The strict threshold order proves that every claimed polygon type occurs on a region of positive spherical measure and that no other type does.

**3. Haar probability and exact integration.** Under uniform spherical orientation, \(z=|u_3|\) is uniform on \([0,1]\) and independent of azimuth. Hence, at fixed \(\phi\),
\[
\Pr(t\le q\mid\phi)=\Pr\left(\frac{hz}{\sqrt{1-z^2}}\le q\right)
=\frac{q}{\sqrt{h^2+q^2}}=:S_h(q),\qquad q\ge0.
\tag{4}
\]
Integrating the six intervals in (3) yields the conditional masses
\[
\begin{aligned}
p_4(\phi)&=S_h(E),\\
p_5(\phi)&=S_h(C)-S_h(E)+1-S_h(M),\\
p_6(\phi)&=S_h(D)-S_h(C)+S_h(M)-S_h(B),\\
p_7(\phi)&=S_h(B)-S_h(D).
\end{aligned}
\tag{5}
\]
For \(\theta\in[0,\pi/2]\),
\[
\frac{d}{d\theta}F_h(\theta)
=\frac{\cos\theta}{\sqrt{h^2+\cos^2\theta}}
=S_h(\cos\theta).
\tag{6}
\]
Averaging (5) over the uniform sector \((0,\delta)\) and using the substitutions \(\theta=4\delta\pm\phi\), \(2\delta\pm\phi\), and \(\phi\) gives exactly the four boxed formulas in the Finding. They are normalized because (5) sums to one for every \(\phi\), and positive because each relevant interval in (3) has positive conditional probability.

**4. Independent mean calculation.** For a line segment with endpoint vectors \(v,w\) relative to the origin, the Haar probability that the central plane crosses its interior equals the spherical angle \(\arccos(v\cdot w/(\|v\|\|w\|))\) divided by \(\pi\). The prism has five vertical edges with endpoint angle \(2\arctan h\) and ten horizontal edges with angle
\[
\arccos\left(\frac{h^2+\cos(2\pi/5)}{1+h^2}\right).
\]
Summing these independent *expectations* by linearity proves the mean identity and supplies a check unrelated to the chamber integration.

**5. Heptagon aspect limits.** From the exact law,
\[
p_7(h)=\frac{2F_h(2\delta)-F_h(\delta)-F_h(3\delta)}{\delta}.
\]
For fixed \(0<\theta<\pi/2\), the Taylor expansions are
\[
F_h(\theta)=\theta-\frac{h^2}{2}\tan\theta+O(h^4)
\quad(h\downarrow0),
\qquad
F_h(\theta)=\frac{\sin\theta}{h}+O(h^{-3})
\quad(h\to\infty).
\]
Substituting yields both asymptotic coefficients. Strict convexity of tangent on \((0,\pi/2)\) and strict concavity of sine on this interval establish their positivity. Since \(p_7(h)>0\) for every finite positive \(h\) and tends to zero at both extremes, it also has a positive interior global maximum, without asserting a unique optimizer. This completes the proof.

## Verification

The included standalone Python 3 file `verification/verify_pentagonal_prism.py` uses only the standard library. From independently constructed coordinates of all ten vertices and all fifteen original prism edges, it computes the section side count for a normal independently of the chamber formula. For five aspect ratios it checks each of the six threshold intervals at 200 azimuths, compares exact probabilities against a separate numerical quadrature of (5), and checks the exact expected side count via endpoint angles. A fixed-seed Haar simulation of 240,000 normals checks the four masses for the uniform pentagonal prism. Additional numerical checks target the two endpoint constants. The code prints `ALL_PENTAGONAL_PRISM_SECTION_CHECKS_OK` if all tests pass.

These finite tests do not prove the theorem, the strict positivity for all \(h>0\), or the endpoint asymptotics. Those assertions rest on steps 1–5 above. In particular the quadrature and simulation are corroborative, not exhaustive certificates for infinitely many orientations or aspect ratios.

## Relationship to prior work

Lonke's study of random **central cube** sections motivates exact Haar section statistics but does not imply the present law for a pentagonal prism. Published mean-square width calculations for uniform regular prisms use the same family of solids but concern the **width of the solid**, rather than the face number of its central planar section. A published exact section-type law for rectangular boxes concerns another polytope family, and cannot supply the fivefold threshold order (2) or the four masses above.

Voss investigated planar-section polygon frequencies of polyhedra (1982), and Ohser and Mücklich studied stereological sections of random polyhedral ensembles (1995). The accessible abstracts concern more general or random-offset stereological sampling. Their full papers were not available for complete statement-by-statement inspection; potential historical equivalents under alternative sampling conventions remain an explicit priority risk. A readable discussion of random affine sections of prisms by Gulbin (2008) uses translated/stationary sampling: for example, it records triangular cube sections, whereas a central cube section cannot be triangular. Thus its model is demonstrably different, even though related integral-geometric methods are relevant. We do not claim that generic spherical-integration techniques are new; the substantive contribution is the complete pentagonal-prism law and its sharp aspect behavior.

## Limitations

The prism must be right with a regular pentagonal base, its section plane must pass through the origin, and its normal must be Haar-uniform. The law need not hold for translated cutting planes, nonregular bases, or nonuniform orientation distributions. Only the first moments of the resulting discrete side counts are treated; no area or perimeter distribution is asserted. The heptagon probability is proved to attain some maximum, but its maximizing aspect ratio is not classified. Historical priority is provisional because two potentially relevant older stereological full texts were inaccessible; these do not support an assertion of uniqueness in the mathematical literature. No independent mathematical validation has been performed.

## References

1. Y. Lonke, *On Random Sections of the Cube*, arXiv:math/9812123v1 (first public version 21 December 1998), https://arxiv.org/abs/math/9812123.
2. K. Voss, *Frequencies of n-polygons in planar sections of polyhedrons*, *Journal of Microscopy* 128 (1982), 111–120, DOI:10.1111/j.1365-2818.1982.tb00443.x (abstract inspected; full text unavailable).
3. J. Ohser and F. Mücklich, *Stereology for some classes of polyhedrons*, *Advances in Applied Probability* 27 (1995), 384–396, DOI:10.2307/1427832 (abstract inspected; full text unavailable).
4. I. Gulbin, *On estimation and hypothesis testing of the grain size distribution by the Saltykov method*, *Image Analysis & Stereology* 27 (2008), 163–174, section on stereology of prisms.
5. *Exact mean-square width of every uniform regular prism*, published mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-mean-square-width-of-every-uniform-regular-prism--eb371b3be549.
6. *Exact Haar hexagon law and cubic rigidity for central sections of rectangular boxes*, published mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-haar-hexagon-law-and-cubic-rigidity-for-central-sections-o--45d2a55425d4.
