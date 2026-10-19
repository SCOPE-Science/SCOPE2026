# Three-way short-period fold ordering in an Anosov-driven Möbius map

## Finding

For the three-torus skew map introduced by Chigarev, Kazakov and Pikovsky [1], fix the Möbius strength \(\varepsilon=2/5\), let \(0<\mu\le 1/10\), and vary the forcing phase \(-\pi/2\le\alpha\le\pi/2\) and positive drift \(c\) upward from zero. Its unique fixed base orbit and its two distinct primitive period-two base orbits each initially carry a pair of hyperbolic fiber-fixed or fiber-period-two states. Let \(c_0,c_1,c_2\) denote their respective **first positive nonidentity parabolic thresholds**. They are exact elementary functions of \(\mu,\alpha\):
\[
 h_0=\frac{1}{\pi}\arcsin(2/5),\quad
 q_j=\cos(2\pi j/5),\quad s_j=\sin(2\pi j/5),
\]
\[
 c_0(\alpha)=h_0-\mu\sin\alpha,\qquad
 c_j(\alpha)=-\mu q_j\sin\alpha+
 \frac1\pi\arcsin\left(\frac25\cos(\pi\mu s_j\cos\alpha)\right),\quad j=1,2.
\]
All three thresholds are positive. There are **exactly two** phase values
\[ -\pi/2<\alpha_-(\mu)<0<\alpha_+(\mu)<\pi/2\]
at which the *earliest* of these three short-period folds changes identity. Specifically the first fold is the base \(j=2\) period-two fold for \(\alpha<\alpha_-\), the base \(j=1\) period-two fold for \(\alpha_-<\alpha<\alpha_+\), and the fixed-base fold for \(\alpha>\alpha_+\). At the two transition phases the indicated neighboring folds occur simultaneously (at different base orbits). No other crossing changes the identity of the earliest fold in the stated phase interval. The switching phases are uniquely specified by
\[
 c_2(\alpha_-)=c_1(\alpha_-),\qquad c_1(\alpha_+)=c_0(\alpha_+).
\]
Their weak-forcing limits are sharp:
\[
 \alpha_-(\mu)=-\frac{\varepsilon\pi}{4\sqrt{1-\varepsilon^2}}\mu+O(\mu^3),\qquad
 \alpha_+(\mu)=\frac{\varepsilon\pi(1+\cos(2\pi/5))}{2\sqrt{1-\varepsilon^2}}\mu+O(\mu^3),\quad\varepsilon=2/5.
\]
The claim ranks **only the folds supplied by base periods one and two**. It does not identify the first bifurcation over all possible periods or a global attractor–repeller collision boundary.

## Assumptions and scope

Let \(\mathbb T=\mathbb R/\mathbb Z\). The original model [1, Eq. (1)] is the diffeomorphism \(F\colon\mathbb T^3\to\mathbb T^3\)
\[
 \begin{aligned}
 t'&=2t+s\pmod1,\\
 s'&=t+s\pmod1,\\
 x'&=x+c+\mu\sin(2\pi t+\alpha)
 -\frac1\pi\arctan\!\left(\frac{\varepsilon\sin(2\pi x)}{1+\varepsilon\cos(2\pi x)}\right)\pmod1.
 \end{aligned}
\]
Here \(\varepsilon=2/5\), \(0<\mu\le1/10\), and \(-\pi/2\le\alpha\le\pi/2\). Since \(1+\varepsilon\cos(2\pi x)>0\), the arctangent has its ordinary continuous meaning. A *fiber pair* above a base orbit of period \(p\in\{1,2\}\) consists of the attracting and repelling fixed points of its \(p\)-step fiber Möbius return. Hyperbolicity, parabolicity and attraction here refer to the fiber derivative, not to the full three-dimensional dynamics (which also has one stable and one unstable Anosov direction). A fold threshold is the first \(c>0\) at which that return loses its two distinct hyperbolic circle fixed points; the parabolic return has a single circle fixed point and is not the identity. At the upper fold, the associated hyperbolic fiber pair coalesces. Only \(c\) in the initial windows containing \(c=0\) is compared. All derivatives and maps are real/complex smooth, with no numerical discretization.

## Proof

**1. Exhaustion of base periods at most two.** The driving cat matrix is \(A=\left(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\right)\). Since \(|\det(A-I)|=1\), the only fixed torus point is \((0,0)\). Since \(|\det(A^2-I)|=5\), the complete \(A^2\)-fixed set is \((0,0)\) and the four points
\[
 (1/5,2/5)\leftrightarrow(4/5,3/5),\qquad
 (2/5,4/5)\leftrightarrow(3/5,1/5).
\]
These are the two base primitive period-two orbits, indexed by \(j=1,2\). Their successive forcing shifts are \(d_{\pm}=c+\mu\sin(\alpha\pm2\pi j/5)\).

**2. Exact return discriminants.** Set \(z=e^{2\pi ix}\). For shift \(d\) the circle fiber is the disk-preserving Möbius map
\[
 M_d(z)=e^{2\pi i d}\frac{z+\varepsilon}{1+\varepsilon z}.
\]
Use the determinant-one \(\mathrm{SU}(1,1)\) representatives
\[
 U_d=\operatorname{diag}(e^{i\pi d},e^{-i\pi d}),\qquad
 B=(1-\varepsilon^2)^{-1/2}\left(\begin{smallmatrix}1&\varepsilon\\\varepsilon&1\end{smallmatrix}\right).
\]
The two-step fiber return over base orbit \(j\) is represented by \(U_{d_-}BU_{d_+}B\), with real trace
\[
 \operatorname{tr} P_j=\frac{2}{1-\varepsilon^2}
 \left[\cos\bigl(2\pi(c+\mu q_j\sin\alpha)\bigr)
 +\varepsilon^2\cos(2\pi\mu s_j\cos\alpha)\right].
\]
A disk-preserving Möbius transformation has two distinct hyperbolic circle fixed points for \(|\operatorname{tr}P|>2\), a nonidentity parabolic point when \(|\operatorname{tr}P|=2\), and no circle fixed point for \(|\operatorname{tr}P|<2\). For the **positive-trace component** containing \(c=0\), the strict inequality \(\operatorname{tr}P_j>2\) becomes
\[
 |\sin\bigl(\pi(c+\mu q_j\sin\alpha)\bigr)|
 <\varepsilon\cos(\pi\mu s_j\cos\alpha).
\]
The cosine on the right is strictly positive since \(\pi\mu s_j\le\pi/10\). The first positive endpoint is precisely \(c_j\) in the finding. The fixed-base fiber has shift \(d=c+\mu\sin\alpha\) and exactly the hyperbolic window \(|\sin(\pi d)|<\varepsilon\), giving \(c_0\).

**3. All three start hyperbolic and their folds are genuine.** Put \(h_j=\pi^{-1}\arcsin(\varepsilon\cos(\pi\mu s_j\cos\alpha))\). Using \(\arcsin r\ge r\), \(\cos v\ge1-v^2/2\), and \(\mu\le1/10\),
\[
 h_j\ge \frac{2}{5\pi}\cos(\pi/10)>\frac1{10}\ge\mu|q_j|.
\]
Also \(h_0>1/10\). Thus the three initial hyperbolic windows contain \(c=0\), and their first positive endpoints are strictly positive. Every endpoint is at most \(h_0+1/10<1/4\), so throughout these first windows \(-1/10\le d_\pm<h_0+1/5<1/2\). The off-diagonal entry of \(U_{d_-}BU_{d_+}B\) is a nonzero scalar multiple of \(\cos(\pi d_+)\), hence its value at trace \(+2\) cannot be an identity return. The corresponding fold is genuinely parabolic. There is no intervening second hyperbolic component along the initial window.

**4. Strict ordering and the two unique switches.** Let \(h_j(\alpha)\) be as above. The exact identities
\[
 q_1-q_2=\sqrt5/2,\quad 0<q_1<1,\quad q_2<0,
 \quad s_1>s_2>0,\quad s_1^2+s_2^2=5/4
\]
imply \(h_2(0)>h_1(0)\) and \(h_1(\alpha)\le h_0\). Define
\[
 \Delta_{21}=c_2-c_1=\mu(q_1-q_2)\sin\alpha+h_2-h_1,
 \qquad \Delta_{10}=c_1-c_0=\mu(1-q_1)\sin\alpha+h_1-h_0.
\]
Differentiating gives
\[
 h_j'(\alpha)=\frac{\varepsilon\mu s_j\sin(\pi\mu s_j\cos\alpha)\sin\alpha}{\sqrt{1-\varepsilon^2\cos^2(\pi\mu s_j\cos\alpha)}};
 \qquad |h_j'|\le\frac{\varepsilon\pi\mu^2s_j^2}{\sqrt{1-\varepsilon^2}}|\sin\alpha\cos\alpha|.
\]
In the open phase interval \((-\pi/2,\pi/2)\),
\[
 \Delta_{21}'\ge \mu\cos\alpha\left(\frac{\sqrt5}{2}
 -\frac{5\varepsilon\pi\mu}{4\sqrt{1-\varepsilon^2}}\right)>0.
\]
The last strict inequality follows for \(\varepsilon=2/5\), \(\mu\le1/10\): its subtracted term is at most \(\pi/(4\sqrt{21})<1/4\), whereas \(\sqrt5/2>1\). Now \(\Delta_{21}(-\pi/2)=-\mu\sqrt5/2<0\) while \(\Delta_{21}(0)=h_2(0)-h_1(0)>0\). Hence exactly one \(\alpha_-\in(-\pi/2,0)\) satisfies \(c_2=c_1\). For \(\alpha\le0\), \(\Delta_{10}<0\) (apart from no possible zero), so the fixed-base fold cannot be earliest there. On \((0,\pi/2)\), \(h_1'>0\) and
\[
 \Delta_{10}'=\mu(1-q_1)\cos\alpha+h_1'(\alpha)>0.
\]
Since \(\Delta_{10}(0)=h_1(0)-h_0<0\) and \(\Delta_{10}(\pi/2)=\mu(1-q_1)>0\), there is exactly one \(\alpha_+\in(0,\pi/2)\) with \(c_1=c_0\). Because \(\Delta_{21}>0\) for every \(\alpha\ge0\), no other competitor becomes earliest. This proves the full three-way ranking including both simultaneous transitions.

**5. Weak-forcing asymptotics.** Uniformly in \(\alpha\in[-\pi/2,\pi/2]\),
\[
 h_j(\alpha)=h_0-\frac{\varepsilon\pi\mu^2s_j^2\cos^2\alpha}{2\sqrt{1-\varepsilon^2}}+O(\mu^4).
\]
The unique root equations above force \(\alpha_\pm=O(\mu)\). Substitution into the root equations, using \(s_1^2-s_2^2=\sqrt5/4\) and \(s_1^2=(1-q_1)(1+q_1)\), yields the two announced coefficients and \(O(\mu^3)\) remainder. Analyticity of the right-hand sides near \(\mu=0\) after division by \(\mu\) justifies the uniform local expansions.

## Verification

The standalone `verify.py` independently enumerates all five \(A^2\)-fixed base points, verifies the golden-ratio trigonometric identities symbolically, composes the actual complex \(\mathrm{SU}(1,1)\) matrices, and compares their traces against the closed expressions at parameter-grid points and exact fold boundaries. It also solves the two switch equations to high precision and checks the claimed ordering on both sides. The code reported `CHECK_OK` after 519 assertions/consistency tests. For \(\mu=1/10\), the switch phases are approximately
\[
 \alpha_-=-0.03370194797518050324915709496,\quad
 \alpha_+=0.08814153511561806720774144410.
\]
These finite checks do not establish uniqueness for all parameters: the analytic derivative bounds in Step 4 do.

## Relationship to prior work

Chigarev–Kazakov–Pikovsky [1] give the exact skew map, the Möbius composition property, periodic-driver fold mechanism, and numerical fold curves for driver periods up to seven (especially their Section IV.A and Figure 5). They do not give this closed short-period three-curve ordering, strict uniqueness of the two switching phases, or their weak-forcing constants. The published related result [2] concerns complete primitive period-two counting and identity-resonance arithmetic only on the **different zero-phase, zero-drift slice** \(c=\alpha=0\), with no variable-phase or positive-drift fold competition. Thus [2] neither states nor implies the order transition between the fixed base orbit and the two different primitive period-two base orbits as \(\alpha\) changes. Both the general Möbius matrix method [1] and the base-period arithmetic in [2] are acknowledged rather than claimed as new. The 2021 study [3] investigates measures and relative singularities for related models, not the present fold-ordering classification.

## Limitations

The result concerns the first **three specified driver orbits** (base period at most two), not all driver periods; higher-period driver folds may precede all three. The work does not determine the actual global collision threshold, persistence of heterodimensional cycles, or invariant measures. The fixed strength \(\varepsilon=2/5\) and small-forcing strip \(0<\mu\le1/10\) are selected because they include the numerical benchmark parameters used in [1] and allow a rigorous single-valued phase ordering. The proof does not assert the same ordering outside the phase interval. Undiscovered equivalent analytical calculations in the wider Möbius-cocycle literature remain a novelty risk.

## References

1. V. Chigarev, A. Kazakov, A. Pikovsky, *Attractor-repeller collision and the heterodimensional dynamics*, arXiv:2305.18172v1, first posted 2023-05-29, *Chaos* 33, 063113 (2023), DOI 10.1063/5.0144672. Accessible full text: https://arxiv.org/html/2305.18172v1 .
2. *Arithmetic isolation of identity resonances in a cat-driven Möbius map*, 2026 public mathematical finding, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-arithmetic-isolation-of-identity-resonances-in-a-cat-driven-m-bi--a1ced3096486 .
3. V. Chigarev, A. Kazakov, A. Pikovsky, *Mutual singularities of overlapping attractor and repeller*, *Chaos* 31, 083127 (2021), DOI 10.1063/5.0056891.
