# The sharp all-height Steiner real-rootedness threshold for planar-base right prisms

## Finding
Let \(B\subset\mathbb R^2\) be any compact convex body of positive area \(A\) and perimeter \(P\). For a height \(h>0\), put \(K_h=B\times[0,h]\). The Euclidean Steiner polynomial of \(K_h\) has **three real negative roots for every positive height** (multiplicities counted) if and only if
\[
q:=\frac{4\pi A}{P^2}\le q_*:=15\pi-\frac94\pi^2-24=0.917279901395841\ldots.
\]
The roots are simple for all heights if \(q<q_*\). At \(q=q_*\), there is exactly one height yielding a double root; it is \(h=\ell u_*\), where
\[
\ell=\frac{P}{2\pi},\qquad
u_*=-\frac{3(\pi-4)(5\pi-16)}{2(3\pi-10)}=0.653712286170932\ldots.
\]
For every \(q>q_*\), the **same** height \(h=\ell u_*\) yields one real negative root and two nonreal conjugate roots. Thus the threshold is sharp even with a base-independent witness after perimeter normalization.

For a regular \(m\)-gon base, \(q_m=\pi/[m\tan(\pi/m)]\) is strictly increasing with \(m\). Direct certified trigonometric bounds give \(q_6<q_*<q_7\). Consequently, all-height real-rootedness holds for the regular prisms with \(3\le m\le6\) sides and fails (at \(h=\ell u_*\)) for every \(m\ge7\).

## Assumptions and scope
The base \(B\) can be smooth or nonsmooth; only convexity, compactness, positive area and finite perimeter are assumed. The height \(h\) is strictly positive. The cubic is the **ordinary** outer-parallel-body Steiner polynomial, with \(\mathbb B_3\) the unit Euclidean three-ball, not an Ehrhart or relative Steiner polynomial. Real-rooted means three real roots counted with algebraic multiplicity; negative excludes zero.

## Proof
**1. Exact polynomial.** Set \(\ell=P/(2\pi)\), \(u=h/\ell\) and \(z=t/\ell\). The planar Steiner formula gives
\[
\operatorname{Area}(B+s\mathbb B_2)=A+Ps+\pi s^2\quad(s\ge0).
\]
A horizontal slice of \(K_h+t\mathbb B_3\) at height in \([0,h]\) has area \(A+Pt+\pi t^2\); in either end cap its area is \(A+P\sqrt{t^2-s^2}+\pi(t^2-s^2)\) for \(0\le s\le t\). Integrating and using \(\int_0^t\sqrt{t^2-s^2}\,ds=\pi t^2/4\) yields
\[
\operatorname{Vol}_3(K_h+t\mathbb B_3)
=hA+(hP+2A)t+\left(\pi h+\frac{\pi P}{2}\right)t^2+\frac{4\pi}{3}t^3.
\]
Because \(A=\pi\ell^2q\), division by \(\pi\ell^3\) reduces the zeros to those of
\[
F_{q,u}(z)=\frac43z^3+(u+\pi)z^2+2(u+q)z+qu
=A_q(z)+uB_q(z),
\]
where \(A_q(z)=\frac43z^3+\pi z^2+2qz\) and \(B_q(z)=z^2+2z+q\). Planar isoperimetry gives \(0<q\le1\).

**2. Subcritical strict interlacing.** Put \(r=\frac32(\pi-4)\), so \(-2<r<-1\), and \(q_*=-r^2-2r\). For \(0<q<q_*\), the two negative zeros \(\beta_1=-1-\sqrt{1-q}\) and \(\beta_2=-1+\sqrt{1-q}\) of \(B_q\) satisfy \(\beta_1<r<\beta_2<0\). Evaluating at these zeros eliminates the height parameter:
\[
F_{q,u}(\beta_j)=A_q(\beta_j)
=-\frac23\beta_j^2(\beta_j-r).
\]
Thus \(F(\beta_1)>0\), \(F(\beta_2)<0\), while \(F(-\infty)<0\) and \(F(0)=qu>0\). The intermediate-value theorem forces one root in each of the three disjoint intervals \(( -\infty,\beta_1)\), \((\beta_1,\beta_2)\), and \((\beta_2,0)\); their total degree proves exactly three distinct negative roots.

**3. Exact boundary.** At \(q=q_*\), \(r\) is a root of \(B_q\) and \(A_q\) and hence of \(F\) for every \(u\). Polynomial division gives
\[
F_{q_*,u}(z)=(z-r)\left[\frac43z^2+(u+3\pi-8)z+u\left(\frac32\pi-4\right)\right].
\]
The bracket's discriminant is
\[
\left(u-\pi+\frac83\right)^2+\frac89(3\pi-8)^2>0.
\]
Both bracket roots are negative by positivity of its two nonleading coefficients for \(u>0\). The bracket takes value zero at \(z=r\) precisely when \(u=u_*\); its positive discriminant ensures that the coincident root has multiplicity exactly two, not three.

**4. A single witness for every supercritical base.** For \(\delta=q-q_*>0\), the cubic discriminant \(\operatorname{Disc}_zF_{q,u_*}\) is the exact polynomial
\[
C_1\delta+C_2\delta^2-\frac{128}{3}\delta^3,
\]
where
\[
C_1=-\frac{3(\pi-4)^2(27\pi^2-176\pi+288)^3}{4(3\pi-10)^4}<0,
\]
\[
C_2=\frac{1593\pi^4-21888\pi^3+112768\pi^2-258048\pi+221184}{(3\pi-10)^2}<0.
\]
For the first sign note that \(27x^2-176x+288\) has negative discriminant \(-128\) and positive leading coefficient. For the second sign set \(Q(x)=1593x^4-21888x^3+112768x^2-258048x+221184\). Exact rational arithmetic shows \(Q(3.141592)<-14\) and \(\lvert Q'(x)\rvert<3{,}000{,}000\) on \([3,4]\); since \(3.141592<\pi<3.141593\), it follows that \(Q(\pi)<-11<0\). The rational enclosure of \(\pi\) is certified by Machin's arctangent formula and alternating-series bounds in the standalone checker. Consequently the cubic discriminant is strictly negative for **every** \(q>q_*\) at \(u=u_*\). It has one real negative root and one nonreal conjugate pair there. This proves both directions of the equivalence and the sharp witness.

**5. Regular-polygon cutoff.** A regular \(m\)-gon has \(q_m=\pi/[m\tan(\pi/m)]\), increasing strictly with \(m\ge3\), because \(x\mapsto\tan x/x\) increases on \((0,\pi/2)\). Rational alternating-series bounds for sine, cosine and \(\pi\) (implemented in the checker) verify \(q_6<q_*<q_7\). The claimed side-count dichotomy follows.

## Verification
The included standalone `verify.py` uses symbolic polynomial identities, an exact-rational Machin enclosure of \(\pi\), a rational sign certificate for the quartic \(Q\), exact rational bracketing of the regular hexagon and heptagon, and numerical root tests across the threshold (including both extreme and near-critical shapes). It does not treat floating-point root tests as a substitute for the all-parameter analytical proof. Run with `python verify.py` after installing `sympy` and `numpy`.

## Relationship to prior work
Katsnelson (2008), Section 12, developed general Steiner-polynomial product calculus; the exact prism coefficient formula is therefore not presented as a new general product principle. Henk and Hernández Cifre (2008) studied general constraints on Steiner roots. Saorín Gómez (2008, Example 1.3) determined the circular-cylinder real-root threshold, which covers the special case \(q=1\) but does not identify the all-base all-height critical isoperimetric quotient, the common witness height, or the regular-six-to-seven polygonal transition. Henk, Hernández Cifre and Saorín (2012) treated general relative-root cones rather than the prism-specific shape classification. The claim is restricted to the new exact all-height criterion and its sharp boundary/witness consequences.

## Limitations
No assertion is made about the full height-dependent number of real roots for each supercritical quotient \(q\); the proof guarantees at least one explicitly given failing height. The result does not claim a novel circular-cylinder threshold or a new planar Steiner formula. Bibliographic searches and comparisons cannot exclude earlier independently derived or unindexed equivalent classifications. Independent external validation and historical-priority certification have not been performed.

## References
1. V. Katsnelson, *On H. Weyl and J. Steiner Polynomials*, arXiv:0803.2346v1, first public 2008-03-16, Section 12. https://arxiv.org/pdf/0803.2346
2. M. Henk and M. A. Hernández Cifre, *Notes on the roots of Steiner polynomials*, Revista Matemática Iberoamericana **24** (2008), 631–644. https://ems.press/content/serial-article-files/38249?nt=1
3. E. Saorín Gómez, *On Inner Parallel Bodies: From the Steiner Polynomial to Poincaré Inequality* (2008 doctoral thesis), Example 1.3. https://webs.um.es/beca/Investigacion/SaorinGomez.pdf
4. M. Henk, M. A. Hernández Cifre and E. Saorín, *Steiner Polynomials via Ultra-logconcave Sequences*, *Communications in Contemporary Mathematics* **14** (2012). https://webs.um.es/mhcifre/preprints/henk_saorin%20steiner_log.pdf
