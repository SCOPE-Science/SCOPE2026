# Exact non-isochronous crossing annulus and sharp grazing in a four-sector relay oscillator

## Finding
For every \(k>0\), consider the four-sector relay oscillator
\[
\dot x=y,\qquad \dot y=-x-k\operatorname{sgn}(xy)
\]
away from the switching axes. The unique transverse Filippov solution from the positive-axis section point \((A,0)\) is a four-quadrant periodic orbit **if and only if** \(A>2k\). For these amplitudes, its first-return map and least period are exactly
\[
P(A)=A,\qquad
T(A)=2\arccos\!\left(-\frac{k}{A-k}\right)
       +2\arccos\!\left(\frac{k}{A+k}\right).
\]
Therefore the crossing periodic trajectories form a non-isolated open annulus; all have return multiplier \(P'(A)=1\). Their period is strictly decreasing and satisfies
\[
2\pi<T(A)<2\pi+2\arccos(1/3),\quad
\lim_{A\downarrow2k}T(A)=2\pi+2\arccos(1/3),\quad
\lim_{A\to\infty}T(A)=2\pi.
\]
The exact boundary \(A=2k\) is a grazing collision with the origin, not a transverse periodic orbit. In particular, vanishing first-order averaged drift for this symmetric perturbation conceals a non-isochronous annulus with a finite-amplitude crossing threshold.

## Assumptions and scope
The parameter \(k\) is any strictly positive real number. The oscillator is the specialization \(f=0\), \(m=4\), \(h\equiv k/\varepsilon\) of Jiang's equation (1.3), for \(\varepsilon>0\). As its Example 4.1 makes explicit, the four-sector switching function is \(g_4(x,y)=\operatorname{sgn}(xy)\) off the axes. The differential equation is understood in the Filippov sense on the switching axes. A **four-quadrant transverse periodic orbit** means a nonconstant closed trajectory meeting the four open quadrants in their cyclic order, crossing both axes with nonzero normal velocity and no sliding segment. The section is \(\Sigma_+=\{(A,0):A>0\}\), and \(A\) always denotes its positive-axis turning coordinate, not Euclidean radius elsewhere.

## Proof
**Conserved half-plane energies.** On \(y<0\), the acceleration is \(\dot y=-x+k\operatorname{sgn}(x)\). Hence
\[
E_- =\frac{x^2+y^2}{2}-k|x|
\]
is constant on every lower-half-plane arc, including its transverse crossing of \(x=0\), because the potential is continuous. Similarly, on \(y>0\),
\[
E_+=\frac{x^2+y^2}{2}+k|x|
\]
is constant. The two first integrals are used only within their respective half-planes; they are **not** asserted to be a single globally conserved energy through \(y=0\).

**The sharp crossing threshold.** Starting from \((A,0)\), a prospective downward lower-half-plane passage has \(E_-=A(A-2k)/2\). At \(x=0\) the same energy would equal \(y^2/2\), which is strictly positive at a transverse crossing. Thus \(A>2k\) is necessary. For \(A=2k\), the lower solution is \(x(t)=k+k\cos t\), \(y(t)=-k\sin t\) until it reaches \((0,0)\) at \(t=\pi\), so it is not a four-quadrant transverse cycle. For \(0<A<2k\) the required transverse crossing is impossible; on the subinterval where \(0<A\le k\), the Filippov field at the positive axis may instead slide, a behavior not claimed to be unique at every boundary point.

**Exact closed orbit above threshold.** Let \(A>2k\), and define
\[
\theta_- =\arccos\!\left(-\frac{k}{A-k}\right),\quad
v=\sqrt{A(A-2k)},\qquad
\theta_+ =\arccos\!\left(\frac{k}{A+k}\right),\quad
w=\sqrt{A(A+2k)}.
\]
On the first (positive-\(x\)) lower segment, the exact solution is
\[
x(t)=k+(A-k)\cos t,\quad y(t)=-(A-k)\sin t,
\quad 0\le t\le\theta_-.
\]
It reaches \((0,-v)\). The next lower segment, writing its new time as \(s\), obeys \(\ddot x+x=-k\) and has
\[
x(s)=-k+k\cos s-v\sin s,\quad
 y(s)=-k\sin s-v\cos s,\quad0\le s\le\theta_-.
\]
At \(s=\theta_-\), the state is exactly \((-A,0)\). Since the accelerations on both sides of \(y=0\) there are positive, this is a transverse crossing to \(y>0\). Starting at \((-A,0)\), the first upper segment is
\[
x(t)=k-(A+k)\cos t,\quad y(t)=(A+k)\sin t,
\quad 0\le t\le\theta_+.
\]
It arrives at \((0,w)\). The final upper segment obeys \(\ddot x+x=-k\), and has
\[
x(s)=-k+k\cos s+w\sin s,\quad
 y(s)=-k\sin s+w\cos s,\quad0\le s\le\theta_+.
\]
This reaches exactly \((A,0)\). All four axis crossings are transverse: at \(x=0\), \(\dot x=\pm v,\pm w\ne0\), and at \(y=0\), the two adjacent accelerations have the same nonzero sign because \(A>2k>k\). The orbit winds exactly once around the origin, so the first return is the least period. Its elapsed time is \(2\theta_-+2\theta_+\). The construction holds for each \(A>2k\) and gives the identity return map and a foliated open annulus.

**Strict twist and limits.** Direct differentiation on \(A>2k\) gives
\[
T'(A)=2k\left[\frac{1}{(A+k)\sqrt{A(A+2k)}}-
\frac{1}{(A-k)\sqrt{A(A-2k)}}\right]<0.
\]
The second denominator is strictly smaller than the first. Both endpoint limits follow directly from the arccosine expression, with the lower-amplitude endpoint omitted because its first axis crossing has zero velocity. Finally \(T(A)>2\pi\), since \(\theta_-=\pi/2+\arcsin(k/(A-k))\) and \(\theta_+=\pi/2-\arcsin(k/(A+k))\).

## Verification
The exact four harmonic pieces and their joining coordinates can be checked by substitution and the elementary identities \(\sin^2\theta_\pm+\cos^2\theta_\pm=1\). A standalone standard-library checker in `verify.py` replays the four event equations, sign/transversality tests, period formula, and derivative sign on a supplementary grid of parameter values; run `python3 verify.py`. The proof above, not a finite test grid, establishes the universal inequalities and periodicity for every real \(k>0\), \(A>2k\).

## Relationship to prior work
Jiang [1, equation (1.3), Proposition 3.3 and Remarks 3.1–3.2] analyzes the same four-sector family by **first-order averaging**, including the symmetry which makes the averaged contribution of a constant \(h\) vanish for \(m=4\). A zero first averaged function does not show that the actual finite-parameter return map is exactly the identity, nor determine which amplitudes encounter grazing, nor the period. This result supplies those nonperturbative statements in the degenerate constant-forcing subfamily. After the rotation \((X,Y)=(y,-x)\), the equation is \(\dot X=Y+k\operatorname{sgn}(XY),\ \dot Y=-X\), linking it to the discontinuous Liénard frameworks of Llibre–Teixeira [2] and Dong–Liu [3]. Their results on lower bounds for isolated limit cycles and averaged coefficients do not give the exact amplitude threshold or period law stated here.

## Limitations
The claim does not count isolated limit cycles under nonzero polynomial perturbations. It does not classify all sliding, escaping, or nonunique Filippov motions on the axes, or claim that every periodic Filippov trajectory must belong to the transverse annulus. The neutral multiplier applies to the smooth crossing return map, not to a sliding orbit. As with any literature comparison, absence from the inspected papers and searches is not a proof of absolute publication novelty. All calculations apply to the exact ideal relay law, not to regularizations, hysteresis, or noisy switching.

## References
[1] Ziguo Jiang, “Limit cycles in an m-piecewise discontinuous polynomial differential system,” *AIMS Mathematics* 9(2), 3613–3629 (first publicly available 2024-01-09), DOI: 10.3934/math.2024177. Full text: https://www.aimspress.com/aimspress-data/math/2024/2/PDF/math-09-02-177.pdf.

[2] Jaume Llibre and Marco A. Teixeira, “Limit cycles for m-piecewise discontinuous polynomial Liénard differential equations,” *Z. Angew. Math. Phys.* 66, 51–66 (2015), DOI: 10.1007/s00033-013-0393-2. Author preprint: https://www.ime.unicamp.br/sites/default/files/pesquisa/relatorios/rp-2013-2.pdf.

[3] Guangfeng Dong and Changjian Liu, “Note on limit cycles for m-piecewise discontinuous polynomial Liénard differential equations,” *Z. Angew. Math. Phys.* 68, Article 97 (2017), DOI: 10.1007/s00033-017-0844-2.
