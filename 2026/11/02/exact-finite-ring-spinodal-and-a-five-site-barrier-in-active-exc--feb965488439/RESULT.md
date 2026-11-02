# Exact finite-ring spinodal and a five-site barrier in active exclusion mean fields

## Finding

Consider the periodic one-dimensional, two-orientation active-exclusion mean-field dynamics defined below. Its spatially homogeneous state has a growing nonconstant linear mode **if and only if**

\[
C_N a^2-L_N a-H_N>0,
\]

where, with \(s_N=\sin^2(\pi/N)\),

\[
\begin{aligned}
C_N&=(1-\phi)(2\phi\cos^2(\pi/N)-1),\\
L_N&=r+4(1-\phi)d\,s_N,\\
H_N&=2rd+4(1-\phi)d^2s_N.
\end{aligned}
\]

Here \(N\ge3\) is the number of ring sites, \(\phi\in(0,1)\) is the uniform occupancy, \(a>0\) the persistent hopping rate, \(d\ge0\) the unbiased hopping rate per neighboring direction, and \(r>0\) the orientation reversal rate. At equality there is an additional zero eigenvalue rather than exponential instability; below the boundary every nonconstant linear mode decays.

Consequently, at fixed \(N,\phi,d,r\), an instability can occur for **some** positive activity \(a\) precisely when

\[
\phi>\phi_*(N):=\frac{1}{2\cos^2(\pi/N)}.
\]

If this holds, the exact activity threshold is the unique positive root

\[
a_*(N)=\frac{L_N+\sqrt{L_N^2+4C_NH_N}}{2C_N},
\qquad \text{and instability holds exactly when }a>a_*(N).
\]

No ring of three or four sites can undergo this mean-field linear instability at any allowed density or activity. Five sites are the smallest possible, with the sharp density barrier

\[
\phi_*(5)=3-\sqrt5.
\]

For instance, the five-site ring at \(\phi=4/5\), \(d=0\), \(r=1\) is unstable exactly when \(a>25(2+\sqrt5)\). In contrast, at \(N=5\), \(\phi=3/4\), \(d=0\), \(r=1\), every activity is finite-ring stable even though the infinite-ring long-wavelength criterion predicts instability for \(a>8\).

For any fixed \(\phi>1/2\) and fixed \(d\ge0,r>0\), the finite-ring threshold decreases to the infinite-ring threshold \(a_\infty\), where

\[
(1-\phi)(2\phi-1)a_\infty^2=r(a_\infty+2d),
\]

and the finite-size shift is sharp:

\[
a_*(N)-a_\infty
=\frac{(1-\phi)[(a_\infty+2d)^2+(2\phi-1)a_\infty^2]}
{2(1-\phi)(2\phi-1)a_\infty-r}
\frac{\pi^2}{N^2}+O(N^{-4}).
\]

These assertions concern the exact linearization of the specified *deterministic mean-field equations*, not phase separation of the finite stochastic exclusion process or nonlinear existence and stability of spatially inhomogeneous solutions.

## Assumptions and scope

At each ring site \(i\in\mathbb Z/N\mathbb Z\) let \(p_{i,+}\) and \(p_{i,-}\) be the two orientation densities, and put \(P_i=p_{i,+}+p_{i,-}\). For \(s\in\{+1,-1\}\) define

\[
\begin{aligned}
\dot p_{i,s}={}&a\big[p_{i-s,s}(1-P_i)-p_{i,s}(1-P_{i+s})\big]\\
&+d\sum_{h=\pm1}\big[p_{i-h,s}(1-P_i)-p_{i,s}(1-P_{i+h})\big]\\
&+r(p_{i,-s}-p_{i,s}).
\end{aligned}
\]

All indices are taken modulo \(N\). Hops are suppressed by destination occupancy in the mean-field factorization; orientations reverse independently. Fix \(N\ge3\), \(a>0\), \(d\ge0\), \(r>0\), and \(0<\phi<1\). The homogeneous state \(p_{i,+}=p_{i,-}=\phi/2\) is an equilibrium. Total occupancy \(\sum_iP_i\) is conserved. Linear stability refers to nonconstant Fourier modes, with the single uniform conserved-density zero eigenvalue removed. At a threshold, “stable” below means strict spectral decay on this fixed-density subspace; equality is marginal, not strictly stable.

## Proof

**1. Exact Bloch reduction.** Linearize at the homogeneous state and denote the total-density perturbation by \(U_i=\delta p_{i,+}+\delta p_{i,-}\), and orientation imbalance by \(V_i=\delta p_{i,+}-\delta p_{i,-}\). The ansatz \((U_i,V_i)=(U,V)e^{\mathrm ik i}\), for \(k=2\pi m/N\), reduces the linearized system to \(\dot{(U,V)}=J(k)(U,V)\), where, writing \(q=1-\cos k\) and \(t=a+2d\),

\[
J(k)=\begin{pmatrix}
-tq&-\mathrm i a(1-\phi)\sin k\\
-\mathrm i a(1-2\phi)\sin k&-2r-(1-\phi)tq
\end{pmatrix}.
\]

For example, the active contribution to the total-density equation is \(a[(\cos k-1)U-\mathrm i(1-\phi)\sin k\,V]\), and that to the imbalance equation is \(a[(1-\phi)(\cos k-1)V-\mathrm i(1-2\phi)\sin k\,U]\). The unbiased hopping contributes \(-2dqU\) and \(-2d(1-\phi)qV\); reversal contributes \(-2rV\). Thus the displayed matrix is an exact derivative of the full nonlinear mean-field dynamics for every allowed \(N\) and discrete wave number, not a small-wave-number approximation.

**2. Sign of the growth exponent.** Every nonzero wave number has \(q>0\), with

\[
\operatorname{tr}J(k)=-2r-(2-\phi)tq<0.
\]

The characteristic polynomial has real coefficients, and its determinant is

\[
\begin{aligned}
\det J(k)
&=tq\,[2r+(1-\phi)tq]+a^2(1-\phi)(1-2\phi)\sin^2k\\
&=q\big[2(rt-a^2(1-\phi)(2\phi-1))
+q(1-\phi)(t^2+a^2(2\phi-1))\big].
\end{aligned}
\]

Because the trace is negative and the determinant real, a positive-real-part eigenvalue occurs precisely when the determinant is negative. If \(\phi\le1/2\), the first determinant expression is strictly positive. If \(\phi>1/2\), the bracket in the second expression is strictly increasing as a function of \(q\), since \((1-\phi)(t^2+a^2(2\phi-1))>0\). Among nonzero discrete wave numbers its minimum occurs at \(m=1\) and \(m=N-1\), where \(q_1=2\sin^2(\pi/N)\). Hence instability occurs if and only if

\[
a^2(1-\phi)(2\phi-1)>rt+(1-\phi)\sin^2(\pi/N)\,[t^2+a^2(2\phi-1)].
\]

This equivalence is valid for \(\phi>1/2\); its rearranged criterion below also excludes instability automatically when \(\phi\le1/2\).

**3. Exact finite-ring classification.** Expanding \(t=a+2d\) in the preceding inequality gives exactly \(C_Na^2-L_Na-H_N>0\), with the coefficients from the finding. If \(C_N\le0\), this cannot hold for \(a>0\), because \(L_N>0\), \(H_N\ge0\). If \(C_N>0\), the quadratic has one positive root and is positive precisely above it. The quadratic formula gives \(a_*(N)\). Thus the existence of any active-rate-induced instability is equivalent to \(2\phi\cos^2(\pi/N)>1\). All other Fourier modes are then initially more stable than \(m=\pm1\). The exact unstable band for a given parameter set can also be read from the determinant: when \(\phi>1/2\), a nonzero Fourier mode \(m\) grows exactly if

\[
1-\cos(2\pi m/N)<
\frac{2[a^2(1-\phi)(2\phi-1)-rt]}
{(1-\phi)[t^2+a^2(2\phi-1)]}.
\]

**4. Sharp minimum size and contrasting examples.** For \(N=3\), \(\cos^2(\pi/N)=1/4\); for \(N=4\), it equals \(1/2\). Thus \(C_N<0\) whenever \(3\le N\le4\) and \(0<\phi<1\). For \(N=5\), \(\cos^2(\pi/5)=(3+\sqrt5)/8\) and \(\phi_*(5)=3-\sqrt5<1\), proving both exclusion for smaller sizes and attainment of the first possible size. At \(\phi=4/5\), \(d=0\), \(r=1\), one has \(C_5=(\sqrt5-2)/25\), \(L_5=1\), \(H_5=0\), so \(a_*(5)=25(2+\sqrt5)\). At \(\phi=3/4\), the infinite-volume coefficient \((1-\phi)(2\phi-1)=1/8\) makes the infinite-volume long-wave threshold \(a>8\) for \(d=0,r=1\), whereas \(C_5\le0\), giving the claimed finite-versus-infinite contrast.

**5. Sharp large-ring correction.** Set \(c=1-\phi\) and \(h=2\phi-1>0\). For \(N\to\infty\), the exact threshold equation is

\[
ch a^2-r(a+2d)-c\sin^2(\pi/N)[(a+2d)^2+h a^2]=0.
\]

Its unique positive root at zero sine factor is \(a_\infty\). The derivative of \(ch a^2-r(a+2d)\) at that root is \(2ch a_\infty-r=\sqrt{r^2+8chrd}>0\). The implicit-function theorem followed by \(\sin^2(\pi/N)=\pi^2N^{-2}+O(N^{-4})\) yields the stated positive \(N^{-2}\) correction. No claim about a nonlinear bifurcation or the stochastic finite-particle stationary distribution is used.

## Verification

Run `python3 verify.py` in a directory containing the accompanying standalone checker. It performs direct finite-difference differentiation of the nonlinear mean-field equations (using complex Fourier perturbations), compares each resulting Bloch symbol with the claimed matrix, checks trace and determinant identities across seeded parameter grids, compares instability signs against the full discrete Fourier spectrum, and checks the small-ring no-go and analytic activity thresholds. The executed script returned `PASS 4917 deterministic consistency assertions`.

The program's sampled checks are supportive reproducibility evidence only. The infinite parameter-range theorem and exact threshold rely on the algebraic proof above, not finite enumeration. The source code uses only the Python standard library.

## Relationship to prior work

Hawthorne, Woellner and Freire (2026) introduced the relevant active lattice mean-field framework, its general Bloch Jacobian, and infinite-lattice long-wavelength spinodal formulas, including the linear lattice. Their accessible supporting-information sections give the perturbative machinery, and an indexed main-text excerpt says that finite-lattice stability is handled numerically. Those results are prior work. The additional result here is the all-wave-number **closed-form finite-ring criterion**, the exact activity threshold, its finite-size shift, and the sharp five-site/density barrier; it is not a new derivation of the continuum spinodal.

Dandekar, Chakraborti and Rajesh (2020) studied a related one-dimensional hard-core run-and-tumble lattice process and its hydrodynamic transport coefficients. Mason, Erignoux, Jack and Bruna (2023) analyzed an active-exclusion hydrodynamic limit and phase separation. Their models and continuum results do not, on the inspected material, provide the stated exact discrete finite-ring mean-field threshold. Yao and Jack (2025) investigate fluctuations in a two-dimensional active lattice gas with continuous orientations, rather than this two-orientation finite-ring Jacobian. These comparisons are subject to the source-access limitations below.

## Limitations

The conclusion is **linear** stability or instability of a deterministic factorized mean-field equation at uniform occupancy. It does not imply an actual phase transition in a finite stochastic system, a nonlinear cluster state, a binodal, or a globally stable steady pattern. No claim of independent mathematical validation is made. The motivating 2026 paper's complete main text could not be obtained in this review, although its abstract, supporting-information material and indexed main-text portions were examined; additional implicit finite-volume coverage cannot be ruled out. Several other relevant articles were inspected only through abstracts or accessible portions. The result should therefore be regarded as a proved mathematical statement with **qualified best-knowledge originality**, not a certified publication-priority determination.

## References

- F. Hawthorne, C. F. Woellner and J. A. Freire, *Exact mean-field phase diagram for self-avoiding active particles in a lattice*, arXiv:2606.07823, first publicly submitted June 5, 2026. https://arxiv.org/abs/2606.07823
- R. Dandekar, S. Chakraborti and R. Rajesh, *Hard core run and tumble particles on a one-dimensional lattice*, Physical Review E 102, 062111 (2020). https://doi.org/10.1103/PhysRevE.102.062111
- J. Mason, C. Erignoux, R. L. Jack and M. Bruna, *Exact hydrodynamics and onset of phase separation for an active exclusion process*, Proceedings of the Royal Society A 479 (2023). https://doi.org/10.1098/rspa.2023.0524
- L. Yao and R. L. Jack, *Interfacial and density fluctuations in a lattice model of motility-induced phase separation*, Journal of Chemical Physics (2025). https://doi.org/10.1063/5.0253530
