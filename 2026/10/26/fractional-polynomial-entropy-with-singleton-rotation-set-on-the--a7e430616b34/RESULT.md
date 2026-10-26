# Fractional polynomial entropy with singleton rotation set on the two-torus

## Finding
For **every** real parameter \(0<\beta<1\), there is an explicit orientation-preserving homeomorphism \(F_\beta:\mathbb T^2\to\mathbb T^2\), isotopic to the identity, with
\[
\boxed{\rho(\widetilde F_\beta)=\{(0,0)\},\qquad h_{\mathrm{top}}(F_\beta)=0,\qquad h_{\mathrm{pol}}(F_\beta)=2-\beta.}
\]
Here the specified lift fixes the horizontal coordinate at two fixed base points; every other lift has a singleton rotation set shifted by an integral vector. Consequently every polynomial-entropy value strictly between one and two occurs among zero-topological-entropy two-torus pseudo-rotations. The nonwandering set of the example is exactly two circles, fixed pointwise.

## Assumptions and scope
Write \(\mathbb T=\mathbb R/\mathbb Z\) and use the maximum product metric on \(\mathbb T^2\). Polynomial entropy means
\[
h_{\mathrm{pol}}(F)=\lim_{\varepsilon\downarrow0}\limsup_{n\to\infty}\frac{\log s_F(n,\varepsilon)}{\log n},
\]
where \(s_F(n,\varepsilon)\) is the maximal cardinality of a set separated by the Bowen metric \(d_n(z,z')=\max_{0\le r<n}d(F^r z,F^r z')\). The corresponding minimal spanning cardinality gives the same exponent.

Let the marked base-circle points be \(r=0\) and \(a=1/2\). Parametrize the two complementary arcs using
\[
h_+(t)=\tfrac14(1+\tanh t)\pmod1,\qquad h_-(t)=\tfrac34-\tfrac14\tanh t\pmod1,\quad t\in\mathbb R.
\]
Thus both arcs approach \(r\) as \(t\to-\infty\) and \(a\) as \(t\to+\infty\). Define an orientation-preserving circle homeomorphism \(g\) by \(g(h_\pm(t))=h_\pm(t+1)\), \(g(r)=r\), and \(g(a)=a\).

For the specified \(\beta\), define the continuous, piecewise differentiable nonnegative amplitude
\[
 a_\beta(t)=\begin{cases}
(1-t)^{-\beta},&t\le-1,\\
2^{-\beta}(-t),&-1\le t\le0,\\
0,&t\ge0.
\end{cases}
\]
On the first open arc put \(\phi_\beta(h_+(t))=a_\beta(t)\sin(2\pi t)\). Put \(\phi_\beta=0\) on the second arc and at both marked points. The limits of the first expression at both ends are zero, so \(\phi_\beta:\mathbb T\to\mathbb R\) is continuous. The promised map is
\[
\boxed{F_\beta(x,y)=(g(x),\ y+\phi_\beta(x)\pmod1).}
\]
No differentiability of \(F_\beta\) at \(r\) is claimed.

## Proof
**Construction, topology, and rotation set.** The two formulas for \(h_\pm\) conjugate translation on \(\mathbb R\) to the same north–south motion on their arcs. The map \(g\) is orientation-preserving and fixes \(r,a\). The displayed \(F_\beta\) is a homeomorphism with inverse \((x,y)\mapsto(g^{-1}x,y-\phi_\beta(g^{-1}x))\). It is isotopic to the identity by replacing translation \(t\mapsto t+1\) in the base by \(t\mapsto t+u\) and the fiber displacement by \(u\phi_\beta\), for \(0\le u\le1\). Since both open arcs are wandering under \(g\), points above them are wandering under \(F_\beta\). Both boundary fibers are fixed pointwise, proving the assertion about the nonwandering set.

The chosen horizontal lift of \(g\) fixes \(0,1/2,1\). Its iterated displacement is therefore bounded by one, uniformly in the base point. On the positive arc, write the initial base point as \(h_+(s)\). Its vertical lift displacement at time \(k\) is
\[
B_k(s)=\sum_{j=0}^{k-1}a_\beta(s+j)\sin(2\pi(s+j))
=\sin(2\pi s)\sum_{j=0}^{k-1}a_\beta(s+j).
\]
For all real \(s\) and integers \(k\ge1\), a consecutive-unit-mesh sum through the decaying tail satisfies
\[
\sum_{j=0}^{k-1}a_\beta(s+j)\le C_\beta k^{1-\beta}.
\tag{1}
\]
Indeed the summands vanish on the nonnegative half-line, are uniformly bounded on the compact cutoff region, and on the negative tail are bounded, after ordering by distance from its right endpoint, by a constant times \(1,2^{-\beta},\ldots,k^{-\beta}\). Thus \(|B_k(s)|\le C_\beta k^{1-\beta}\), uniformly in \(s\), while it vanishes on the other arc. Every normalized lift displacement tends uniformly to \((0,0)\); this proves the singleton Misiurewicz–Ziemian rotation set.

**Upper polynomial-entropy bound.** A second uniform consequence of the same tail estimate is
\[
\sup_{s\in\mathbb R}\sum_{j=0}^{n-1}\left(a_\beta(s+j)+|a'_\beta(s+j)|\right)\le C_\beta n^{1-\beta},
\tag{2}
\]
where the derivative is interpreted one-sidedly at the two breakpoints. The derivative is bounded on \([-1,0]\) and decays as \((1-t)^{-1-\beta}\) for \(t<-1\). Since \(\phi_\beta(h_+(s+j))=a_\beta(s+j)\sin(2\pi s)\), (2) implies that each partial sum \(B_k(s)\), \(0\le k\le n\), is \(C_\beta n^{1-\beta}\)-Lipschitz in the fractional coordinate \(u\) when \(s=m+u\) with fixed integer \(m\) and \(0\le u\le1\).

Fix \(\varepsilon>0\). Uniform continuity of \(h_+\) lets us use a mesh of \(O_\varepsilon(n^{1-\beta})\) values of \(u\) within each integer strip \(s=m+u\), so that both base positions at every time and all partial vertical sums are \(\varepsilon/4\)-close. The \(O(n)\) strips meeting \([-2n,2n]\) consequently require \(O_{\beta,\varepsilon}(n^{2-\beta})\) Bowen representatives, with an additional fixed \(\varepsilon\)-net in the initial vertical circle.

For the far-left tail write \(s=-j+u\) with \(j\ge2n\) an integer. The base trajectories remain uniformly close to \(r\). For fixed \(u\), the amplitudes \(a_\beta(-j+u+i)\) decrease monotonically as \(j\) increases, throughout \(0\le i<n\). Therefore
\[
\max_{0\le k\le n}|B_k(-j+u)-B_k(-j'+u)|
=|B_n(-j+u)-B_n(-j'+u)|
\]
for \(j,j'\ge2n\). The endpoint values lie in an interval of length at most \(C_\beta n^{1-\beta}\), since \(n\,a_\beta(-2n+n)\le C_\beta n^{1-\beta}\). Quantizing this interval into bins of length \(\varepsilon/4\) requires \(O_{\beta,\varepsilon}(n^{1-\beta})\) choices of \(j\) for each of the \(O_{\beta,\varepsilon}(n^{1-\beta})\) fractional-coordinate representatives. Thus the far-left tail costs only \(O(n^{2-2\beta})\) representatives. For \(s\ge2n\), the cocycle is zero and all base trajectories are close to \(a\), so a fixed vertical net suffices. The second arc has zero cocycle and an elementary \(O_\varepsilon(n)\) spanning cover: use unit strips in a length-\(O(n)\) central window and one representative for each end tail. The fixed fibers require a constant number. In total,
\[
 g_{F_\beta}(n,\varepsilon)\le C_{\beta,\varepsilon} n^{2-\beta}.
\tag{3}
\]
It follows that \(h_{\mathrm{pol}}(F_\beta)\le2-\beta\); (3) also proves \(h_{\mathrm{top}}(F_\beta)=0\).

**Matching lower bound.** Fix a sufficiently small \(0<\varepsilon_0<1/20\) and a sufficiently large fixed integer \(L\). For each large \(n\), choose \(\asymp n\) integers \(j\) in \([n/3,2n/3]\), separated by at least \(L\). For each such \(j\), choose \(\asymp n^{1-\beta}\) fractional coordinates \(u\in[0,1/8]\), separated by \(K n^{\beta-1}\), where \(K>0\) is a sufficiently large constant. Take the initial points \((h_+(-j+u),0)\).

For a fixed \(j\), let \(k=\lfloor j/2\rfloor\). All sampled arguments \(-j+u+i\), \(0\le i<k\), lie below \(-1\) for large \(n\). On \([0,1/8]\), both \(\sin(2\pi u)\) and the negative-tail amplitude are increasing functions of \(u\). Differentiation gives
\[
\frac{\partial}{\partial u} B_k(-j+u)
=\sum_{i=0}^{k-1}\left[2\pi\cos(2\pi u)a_\beta(-j+u+i)
+\sin(2\pi u)a'_\beta(-j+u+i)\right]
\ge c_\beta n^{1-\beta}.
\tag{4}
\]
This follows from \(k\asymp n\), \(\cos(2\pi u)\ge2^{-1/2}\), and \(a_\beta(-j+u+i)\ge(1+j)^{-\beta}\). With the specified mesh, the unwrapped fiber-phase difference at time \(k\) between any two distinct \(u\)-values exceeds \(4\varepsilon_0\). It starts at zero, grows monotonically with the time index up to \(k\), and each one-step increment is at most \(C_\beta n^{-\beta}<\varepsilon_0\) for large \(n\). Hence at some time its value lies between \(\varepsilon_0\) and \(2\varepsilon_0\); the two points are separated in the fiber **modulo one**. This first-crossing argument is essential: the final unwrapped difference alone would not imply separation on a circle.

If \(j\ne j'\), at time \(j\) the first base coordinate is \(h_+(u)\) with \(u\in[0,1/8]\), whereas the second is \(h_+(j-j'+u')\). Taking \(L\) large makes their base-circle distance bounded below by a positive constant independent of \(n,j,j',u,u'\). Shrinking \(\varepsilon_0\) if necessary makes the two points Bowen-separated. Therefore
\[
 s_{F_\beta}(n,\varepsilon_0)\ge c_\beta n\cdot n^{1-\beta}=c_\beta n^{2-\beta}
\tag{5}
\]
for all sufficiently large \(n\). Combining (3) and (5) proves \(h_{\mathrm{pol}}(F_\beta)=2-\beta\).

## Verification
The standalone standard-library script `verify_fractional_torus.py` checks sampled numerical Birkhoff sums, positive monotonicity on lower-bound strips, and first-crossing separation for several \(\beta\) and finite horizons; its output is `VERIFY_OK` when all checks pass. These numerical checks are illustrative only. Equations (1)–(5) and the topological construction constitute the general proof, with no claim of independent formal certification.

## Relationship to prior work
Corrêa's *Polynomial entropy and rotation sets* (2026), Section 5.1, explicitly asks which values \(\alpha\ge1\) are realizable by zero-topological-entropy torus homeomorphisms isotopic to the identity with a singleton rotation set. The family above realizes the entire open interval \((1,2)\) within that question, but does not resolve its other values or its separate minimality problem.

The published frozen-base velocity-image theorem determines polynomial entropy by upper box dimension for systems \((b,y)\mapsto(b,y+v(b))\), and obtains a fractional example on \(\mathbb T^3\) with a non-singleton rotation set. It does not cover a moving north–south base on \(\mathbb T^2\) with singleton rotation set. The published rational-base scalar-skew zero–one theorem similarly requires periodic base rotation and therefore does not cover the present nonperiodic base. Hauseux–Le Roux's gap for fixed-point-free planar Brouwer homeomorphisms does not apply to a compact torus map with two fixed circles. Correa–de Paula's integer-entropy theorem requires a Morse–Smale diffeomorphism with finite hyperbolic nonwandering set, unlike the present continuous map with non-isolated fixed circles. These distinctions concern actual hypotheses and implications rather than title matching.

## Limitations
The construction is only topological: its oscillatory cocycle approaches a fixed circle too slowly to claim Hölder or differentiable regularity there. The entropy result concerns the given two-torus maps and does not establish minimality, area preservation, realizations at \(\alpha\ge2\), or corresponding smooth examples. The originality comparison is limited to the specifically inspected papers and searched records; possible older formulations using slow entropy, parabolic skew extensions, or surface wandering dynamics remain a bibliographic risk. Independent scientific audit has not been performed.

## References
1. H. Corrêa, *Polynomial entropy and rotation sets*, *Archiv der Mathematik*, first verified public publication 12 September 2026, https://doi.org/10.1007/s00013-026-02286-3, Section 5.1 and Problem 1.
2. J. Correa and H. de Paula, *Polynomial entropy of Morse-Smale diffeomorphisms on surfaces*, arXiv:2203.08336v2 (2022), https://arxiv.org/html/2203.08336v2, Theorem 1 and Introduction.
3. L. Hauseux and F. Le Roux, *Polynomial entropy of Brouwer homeomorphisms*, arXiv:1712.01502 (2017), https://arxiv.org/abs/1712.01502.
4. *Polynomial entropy equals velocity-image box dimension for frozen-base torus translations*, public published-finding corpus mathematical finding, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-polynomial-entropy-equals-velocity-image-box-dimension-for-froze--2c91fbb3a44a/RESULT.md.
5. *A zero-one polynomial entropy law for continuous rational skew products*, public published-finding corpus mathematical finding, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-a-zero-one-polynomial-entropy-law-for-continuous-rational-skew-p--66b278bf390d/RESULT.md.
