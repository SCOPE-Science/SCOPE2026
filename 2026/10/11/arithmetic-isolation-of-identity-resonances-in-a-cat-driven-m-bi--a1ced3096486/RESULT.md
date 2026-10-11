# Arithmetic isolation of identity resonances in a cat-driven Möbius map

## Finding

Consider the three-torus skew diffeomorphism of Chigarev, Kazakov and Pikovsky on the symmetric parameter slice \(c=\alpha=0\), with \(0<\varepsilon<1\) and \(\mu\geq0\):
\[
(t,s,x)\longmapsto\left(2t+s,\ t+s,\ x+\mu\sin(2\pi t)-\frac1\pi\arctan\frac{\varepsilon\sin(2\pi x)}{1+\varepsilon\cos(2\pi x)}\right)\pmod1.
\]
Put \(\sigma_j=\sin(2\pi j/5)>0\), \(j\in\{1,2\}\), and define the disjoint discrete sets
\[
\mathcal R_j=\left\{\frac{k+1/2}{\sigma_j}: k=0,1,2,\ldots\right\}.
\]
If \(\mu\notin\mathcal R_1\cup\mathcal R_2\), this map has **exactly four primitive period-two orbits**. If \(\mu\in\mathcal R_j\), it has exactly two isolated primitive period-two orbits above the other base two-cycle, together with a circle's worth of primitive period-two orbits above the resonant base two-cycle. These are all the primitive period-two orbits. There is no parameter for which both base two-cycles have identity fiber return, because \(\sigma_1/\sigma_2=(1+\sqrt5)/2\) is irrational.

For the two nonresonant period-two orbits above base two-cycle \(j\), the fiber Lyapunov exponents per single iteration are respectively \(\pm\chi_j(\mu)\), where the **exact** positive exponent magnitude is
\[
\chi_j(\mu)=2\operatorname{arsinh}\!\left(\frac{\varepsilon|\cos(\pi\mu\sigma_j)|}{\sqrt{1-\varepsilon^2}}\right).
\]
At every \(\mu_*\in\mathcal R_j\), this vanishes linearly:
\[
\chi_j(\mu)=\frac{2\pi\varepsilon\sigma_j}{\sqrt{1-\varepsilon^2}}|\mu-\mu_*|+O_{\varepsilon,j}(|\mu-\mu_*|^3).
\]
Thus a two-point hyperbolic fiber configuration does not pass through an ordinary isolated parabolic point: at each resonance, the full fiber return becomes the **identity** and all its points are periodic. The other primitive base two-cycle cannot undergo this degeneracy simultaneously.

## Assumptions and scope

The phase space is \(\mathbb T^3\), with \(\mathbb T=\mathbb R/\mathbb Z\); all maps act modulo one in each coordinate. The forcing amplitude \(\mu\) is any nonnegative real number, and \(\varepsilon\) lies strictly between zero and one. The parameters \(c\) and \(\alpha\) are both zero. A primitive period-two orbit consists of two distinct phase-space points interchanged by the map. "Isolated" refers to the period-two set, not to any attracting set. The exponents above are fiber-direction exponents; the base directions retain the Anosov exponents. No statement is made about periods greater than two, invariant measures of generic chaotic trajectories, or persistence when \(c\) or \(\alpha\) is perturbed.

## Proof

**All possible base itineraries.** The linear cat matrix is \(A=\bigl(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\bigr)\). Its only fixed point on \(\mathbb T^2\) is \((0,0)\), because \(\det(A-I)=-1\). Since \(\det(A^2-I)=-5\), its second iterate has exactly five fixed points. The four nonzero points split into exactly two primitive two-cycles:
\[
(1/5,2/5)\leftrightarrow(4/5,3/5),\qquad
(2/5,4/5)\leftrightarrow(3/5,1/5).
\]
These are exhaustive, by the determinant count. Along base orbit \(j\), the two successive forcing shifts in the fiber are \(+\delta_j\) and \(-\delta_j\), with \(\delta_j=\mu\sigma_j\).

**Exact Möbius return.** Write \(z=e^{2\pi i x}\) and let \(H_\varepsilon(z)=(z+\varepsilon)/(1+\varepsilon z)\) and \(R_\delta(z)=e^{2\pi i\delta}z\). Since \(1+\varepsilon\cos(2\pi x)>0\), the arctangent uses a globally unambiguous continuous argument, and the given fiber map at shift \(\delta\) is \(F_\delta=R_\delta\circ H_\varepsilon\). The second return over base orbit \(j\) is
\[
T_j=F_{-\delta_j}\circ F_{\delta_j}=R_{-\delta_j}\circ H_\varepsilon\circ R_{\delta_j}\circ H_\varepsilon.
\]
Use determinant-one matrices
\[
B=\frac{1}{\sqrt{1-\varepsilon^2}}
\begin{pmatrix}1&\varepsilon\\\varepsilon&1\end{pmatrix},\qquad
U_\delta=\begin{pmatrix}e^{i\pi\delta}&0\\0&e^{-i\pi\delta}\end{pmatrix}.
\]
A determinant-one representative of \(T_j\) is \(P_j=U_{-\delta_j}BU_{\delta_j}B\), whose trace is
\[
\operatorname{tr} P_j=2\frac{1+\varepsilon^2\cos(2\pi\delta_j)}{1-\varepsilon^2}
=2+\frac{4\varepsilon^2\cos^2(\pi\delta_j)}{1-\varepsilon^2}.
\]
For \(\delta_j\notin\mathbb Z+1/2\), this trace exceeds two, so the circle Möbius return has exactly two fixed points, one attracting and one repelling. When \(\delta_j\in\mathbb Z+1/2\), conjugation by \(U_{\delta_j}\) changes the sign of the off-diagonal entries of \(B\); hence \(U_{-\delta_j}BU_{\delta_j}=B^{-1}\), so **\(P_j=I\)**, not merely a parabolic matrix. Every circle point then returns after two steps. Because each underlying base itinerary has primitive period two, every one of these full-system orbits has exact period two.

**Exponent and sharp resonance order.** Away from resonance, write the two matrix eigenvalues as \(e^{\pm\chi_j}\) using \(\cosh\chi_j=\tfrac12\operatorname{tr}P_j\). An attracting projective fixed point has multiplier \(e^{-2\chi_j}\) over two iterations, and the repelling one has multiplier \(e^{2\chi_j}\). Using \(\cosh(2\operatorname{arsinh} u)=1+2u^2\) gives the stated \(\chi_j\). At \(\delta_j=k+1/2\), Taylor expansion of \(\cos(\pi\delta_j)\) yields the claimed linear absolute-value law and cubic remainder.

**No simultaneous resonance.** Elementary trigonometry gives \(\sigma_1/\sigma_2=2\cos(\pi/5)=(1+\sqrt5)/2\). A common member of \(\mathcal R_1\) and \(\mathcal R_2\) would make this irrational ratio equal to \((2k+1)/(2\ell+1)\), a rational number, impossible.

**Exclusion of all other primitive two-cycles.** Every full-map period-two point projects to a fixed point of \(A^2\), which was exhausted above. Over its sole fixed base point \((0,0)\), the fiber shift vanishes and the first-step map is \(H_\varepsilon\), conjugate to a real dilation with two fixed points; it has no nontrivial two-cycles. Over each primitive two-cycle of \(A\), the preceding trace calculation exhausts the two-iterate fiber fixed points. Counting the corresponding full two-cycles proves the assertion.

## Verification

The standalone file `verify.py` enumerates exactly the five cat-map second-iterate fixed points using modular integer arithmetic, checks both base itineraries, and independently evaluates the determinant-one matrix trace and identity-return criterion at sample resonant and nonresonant parameters. Its numerical tests are consistency checks, **not** a proof of the infinite quantifiers; those follow from the exact matrix identity, determinant count and irrationality argument above. Run `python3 verify.py` to obtain `CHECK_OK`.

## Relationship to prior work

Chigarev–Kazakov–Pikovsky (2023), equations (1), Section IV.A, and Appendix A establish the original cat-driven Möbius map, the general Möbius composition rule, and the use of periodic-driver returns in studying attractor–repeller collisions. Their plotted bifurcations and general stable/unstable or rotational alternatives do not state this complete primitive-period-two census on \(c=\alpha=0\), the exact identity (rather than generic parabolic) resonances, their arithmetic mutual exclusion, or the exact exponent formula and linear vanishing. The earlier Chigarev–Kazakov–Pikovsky (2021) paper studies relative dimensions and mutual singularities for Anosov–Möbius models; its Section IV.A is concerned with a different map construction and does not provide this census. The calculation uses the known Möbius composition principle as a starting point, rather than claiming that principle as new.

## Limitations

The claims are exact only on the symmetry slice \(c=\alpha=0\) with \(\mu\ge0\), \(0<\varepsilon<1\). The resonances are nongeneric and need not persist under symmetry breaking. The theorem does not classify higher-period points or chaotic attractors. Although the primary two papers were materially compared, unlocated equivalent computations in other Möbius cocycle literature remain a publication-priority uncertainty. No independent mathematical audit has been carried out.

## References

1. V. Chigarev, A. Kazakov, A. Pikovsky, *Attractor-repeller collision and the heterodimensional dynamics*, arXiv:2305.18172v1 (first public 2023-05-29), *Chaos* 33, 063113 (2023), DOI: 10.1063/5.0144672. Open preprint: https://ar5iv.labs.arxiv.org/html/2305.18172 .
2. V. Chigarev, A. Kazakov, A. Pikovsky, *Mutual singularities of overlapping attractor and repeller*, *Chaos* 31, 083127 (2021), DOI: 10.1063/5.0056891.
3. *Mathematics Subject Classification 2020*, class 37C25, American Mathematical Society: https://mathscinet.ams.org/mathscinet/msc/msc2020.html .
