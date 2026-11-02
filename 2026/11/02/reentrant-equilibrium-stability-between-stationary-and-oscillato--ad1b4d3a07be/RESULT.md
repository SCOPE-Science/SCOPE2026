# Reentrant equilibrium stability between stationary and oscillatory spatial instabilities in a two-signal predator–prey system

## Finding
For a fully specified positive-parameter four-component reaction–diffusion system on a smooth disk, the homogeneous coexistence equilibrium is locally exponentially stable, then unstable, then **stable again**, and finally unstable as the common signal-production rate increases. The complete classification has three **exact** transition strengths:
\[
 h_-:=\frac{11-\sqrt{17}}2,\qquad
 h_+:=\frac{11+\sqrt{17}}2,\qquad
 h_{\mathrm{osc}}:=\frac{148}{\sqrt{377}},
 \qquad 0<h_-<h_+<h_{\mathrm{osc}}.
\]
The positive equilibrium is locally exponentially stable if and only if
\[
 0<h<h_-\quad\hbox{or}\quad h_+<h<h_{\mathrm{osc}}.
\]
It is linearly unstable for \(h_-<h<h_+\) and for \(h>h_{\mathrm{osc}}\). At the first two thresholds a real spatial eigenvalue crosses zero, and at the last threshold a nonzero imaginary conjugate pair crosses into the unstable half-plane. Each critical eigenvalue is doubled by the angular degeneracy of the first Neumann eigenspace. No nonlinear bifurcation branch is asserted at any critical point.

## Assumptions and scope
Let \(\Omega\subset\mathbb R^2\) be the open disk of radius \(R=j'_{1,1}\), where \(j'_{m,1}\) denotes the first strictly positive zero of the derivative of the Bessel function \(J_m\). Impose homogeneous Neumann boundary conditions on all four fields. For every real \(h>0\), consider
\[
\begin{aligned}
 \partial_t u_1&=\Delta u_1+\Delta v_1
     +u_1\bigl(\tfrac12-u_1+\tfrac12u_2\bigr),\\
 \partial_t u_2&=\Delta u_2-\Delta v_2
     +u_2(6-u_2-5u_1),\\
 \partial_t v_1&=\Delta v_1+h u_2-v_1,\\
 \partial_t v_2&=\Delta v_2+h u_1-v_2.
\end{aligned}
\]
All biological source-model parameters are strictly positive. The self-diffusion, signal-diffusion and two cross-diffusion magnitudes equal one, so the stated sufficient coefficient conditions \(4d_{11}d_3>d_{12}^2\) and \(4d_{21}d_4>d_{22}^2\) are satisfied. The constant positive equilibrium is
\[
 E_h=(u_1,u_2,v_1,v_2)=(1,1,h,h).
\]
In this statement, 'locally exponentially stable' means convergence for all sufficiently small smooth perturbations in a fixed sufficiently regular Sobolev or Hölder phase space. 'Linearly unstable' means the linearization has an eigenvalue with strictly positive real part; standard semilinear parabolic linearized instability gives local nonlinear instability in the corresponding regular phase space. The theorem is not a claim about solutions started far from \(E_h\).

## Proof
**1. Exact modal characteristic polynomial.** Let \(\kappa\ge0\) be an eigenvalue of the scalar Neumann operator \(-\Delta\). Linearization at \(E_h\), on one associated spatial eigenfunction, is the real matrix
\[
 M_\kappa(h)=
 \begin{pmatrix}
 -1-\kappa&1/2&-\kappa&0\\
 -5&-1-\kappa&0&\kappa\\
 0&h&-1-\kappa&0\\
 h&0&0&-1-\kappa
 \end{pmatrix}.
\]
Set \(t=1+\kappa\), \(g=h\kappa\), \(P=5/2\), \(S=11/2\). Direct determinant expansion, or elimination of the chemical variables, yields
\[
 p_\kappa(z)=\det(zI-M_\kappa)
 =(z+t)^4+P(z+t)^2-Sg(z+t)+g^2.
\]
At \(\kappa=0\) the four eigenvalues are \(-1,-1,-1\pm i\sqrt{5/2}\), independently of \(h\).

**2. Exact Hurwitz test.** Write \(p_\kappa(z)=z^4+a_1z^3+a_2z^2+a_3z+a_4\). Expansion gives
\[
\begin{aligned}
 a_1&=4t, & a_2&=6t^2+P,\\
 a_3&=4t^3+2Pt-Sg, &a_4&=t^4+Pt^2-Sgt+g^2.
\end{aligned}
\]
The second and third Hurwitz determinants are exactly
\[
\begin{aligned}
 \Delta_2&=a_1a_2-a_3=20t^3+2Pt+Sg>0,\\
 \Delta_3&=a_1a_2a_3-a_3^2-a_1^2a_4\\
 &=4t^2(P+4t^2)^2-(S^2+16t^2)g^2.
\end{aligned}
\]
Because \(a_1,a_2,\Delta_2>0\), the quartic is Hurwitz **if and only if** \(a_4>0\) and \(\Delta_3>0\). Indeed, these two inequalities force \(a_3>0\) via \(\Delta_3=a_3\Delta_2-a_1^2a_4\); the usual quartic Routh–Hurwitz conditions then hold.

**3. First spatial eigenvalue.** Classical separation of variables for the Neumann disk gives first nonzero eigenvalue \(\kappa_1=(j'_{1,1}/R)^2=1\), of real multiplicity two. The next distinct eigenvalue is
\[
 \kappa_2=(j'_{2,1}/j'_{1,1})^2>25/16>5/4.
\]
This separation can be established without treating rounded Bessel zeros as rigorous bounds. The alternating series for \(J_1'\) gives \(J_1'(2)<1/2-3/4+5/24<0\), hence \(j'_{1,1}<2\). Meanwhile the series for \(J_1(x)/(x/2)\) is positive for \(0<x\le5/2\), because its first two alternating terms already exceed \(1-x^2/8\ge7/32>0\). For \(J_2'\), the first four alternating terms, after dividing by \(x/2\), give the rigorous lower bound \(1/2-x^2/12+x^4/256-x^6/11520>0\) on the same interval (this polynomial decreases to a strictly positive endpoint value). Thus \(j'_{2,1}>5/2\). Standard interlacing of Bessel zeros and monotonicity in the order then show that every positive Neumann derivative zero other than \(j'_{1,1}\) exceeds \(5/2\). As \(R=j'_{1,1}<2\), the stated lower bound follows. The numerical ratio is approximately \(2.751764\), but no numerical Bessel bound is needed for the theorem.

For \(\kappa=1\), put \(g=h\), \(t=2\). The characteristic polynomial specializes to
\[
 p_1(z)=z^4+8z^3+\tfrac{53}2z^2
 +(42-\tfrac{11}2h)z+(h^2-11h+26),
\]
with
\[
 a_4=(h-h_-)(h-h_+),\qquad
 \Delta_3=5476-\tfrac{377}{4}h^2.
\]
The exact strict ordering \(h_+<h_{\mathrm{osc}}\) follows, for example, from \(\sqrt{17}<413/100\), \(\sqrt{377}<389/20\) and \(2960/389>1513/200\). The Hurwitz test therefore gives the two disjoint first-mode stability intervals as stated. For \(h_-<h<h_+\), the negative constant term gives a positive real eigenvalue; for \(h>h_{\mathrm{osc}}\), \(\Delta_3<0\) gives right-half-plane instability. At \(h_\pm\), \(a_4=0\) and \(a_3>0\), giving a simple zero eigenvalue of the modal matrix; its crossing speed has sign \(-a_4'(h_\pm)/a_3(h_\pm)\). At \(h=h_{\mathrm{osc}}\), \(a_4>0\) and \(\Delta_3=0\). The modal polynomial factors into a strictly Hurwitz quadratic and a quadratic \(z^2+\omega^2\) with
\[
 \omega^2=\frac{42-(11/2)h_{\mathrm{osc}}}{8}>0.
\]
The crossing is transverse because \(\Delta_3'(h_{\mathrm{osc}})=-(377/2)h_{\mathrm{osc}}<0\); alternatively direct implicit differentiation of \(p_1(i\omega)=0\) gives strictly positive real eigenvalue speed.

**4. Exclusion of all higher spatial instabilities.** Completing the square gives
\[
 a_4=\left(g-\frac{St}{2}\right)^2
 +t^2\left(t^2-\frac{81}{16}\right).
\]
Every higher nonzero disk mode satisfies \(\kappa\ge\kappa_2>5/4\), hence \(t>9/4\) and \(a_4>0\) for every \(h\). The condition \(\Delta_3>0\) is exactly
\[
 h<F(t):=\frac{2t(P+4t^2)}{(t-1)\sqrt{S^2+16t^2}}.
\]
The function \(F\) is strictly increasing for all \(t\ge2\). Indeed its derivative has the sign of
\[
 512t^5-1024t^4+1616t^3-2904t^2-605
 =512t^4(t-2)+t^2(1616t-2904)-605>0
\]
when \(t\ge2\). Consequently every higher mode remains Hurwitz whenever \(h<h_{\mathrm{osc}}=F(2)\). The constant mode is always Hurwitz. For \(h>h_{\mathrm{osc}}\), the first mode is already unstable, so no assertion about higher modes is needed.

**5. Full-system conclusion and robustness.** The diffusion matrix has only positive eigenvalues, so the constant-coefficient semilinear system has a sectorial linearization and its Neumann modes decompose as above. For fixed \(h\), sufficiently high modes have real parts tending to \(-\infty\) (the common \(-\kappa\) damping dominates the cross-coupling eigenvalues of order \(\sqrt{h\kappa}\)); the strict modal Hurwitz inequalities therefore give a genuine spectral gap. The semilinear parabolic principle of linearized stability/instability yields the local conclusions. Choosing the four interior sample values \(h=1,5,759/100,8\) proves in addition that the stable–unstable–stable–unstable sequence persists for all sufficiently small positive-parameter perturbations of the reaction, transport and production coefficients on the same disk: the spectral gap and unstable eigenvalues at these four samples persist continuously.

## Verification
Run the packaged `verification.py` using Python with SymPy, NumPy and SciPy. It independently reconstructs the four-by-four determinant, expands the Hurwitz determinants, verifies the exact threshold algebra and strict ordering, and checks the monotonic higher-mode threshold identity. It also confirms standard disk Neumann eigenvalue brackets and samples representative spectra. **No finite mode sampling is used to prove the all-mode statement**; that conclusion follows from the analytic monotonicity and Bessel eigenvalue separation.

The three approximate thresholds are \(h_-\approx3.438447187191\), \(h_+\approx7.561552812809\), and \(h_{\mathrm{osc}}\approx7.622387798844\). The recovered stability window is narrow but nonempty and persists under small coefficient perturbations.

## Relationship to prior work
Shanmugasundaram, Saha, Makinde and Chattopadhyay's 2026 two-signal model is the exact source of these equations; their Section 6 states the general quartic dispersion relation, uses a negative constant coefficient as a sufficient stationary-instability test, and relies on numerical pattern diagrams. The present contribution is a full bounded-domain modal Hurwitz classification for a positive-parameter specialization, including **restabilization** followed by a later oscillatory loss. This does not claim that general quartic Routh–Hurwitz theory or Turing/Hopf mechanisms are new.

Shi, Liu and Xu (2019) provide a two-parameter Turing–Hopf analysis of a **different two-field ratio-dependent reaction–diffusion model**, so their stability-region theorem does not imply this four-field result. Gaffney, Krause, Maini and Wang (2022) analyze localization of Turing conditions in spatially heterogeneous cross-diffusion systems using WKB asymptotics, not the present homogeneous-disk three-transition exact gain diagram. Wang and collaborators (2014) discuss reentrant **pattern branches** in a Brusselator simulation, which does not establish recovered stability of this four-field homogeneous equilibrium. Existing general instability theory supplies the methods, not these model-specific exact thresholds and mode exclusion.

## Limitations
All stability statements are local to the positive homogeneous equilibrium. The theorem does not assert existence, nonlinear stability or uniqueness of patterned equilibria, periodic spatial waves or global attractors. Each first-mode neutral eigenvalue is doubled by disk rotational symmetry, so the boundary events are not claimed to be simple-eigenvalue scalar bifurcations. The source model's physical interpretation and all-solution positivity far from equilibrium are not re-established. Numerical Bessel evaluations in the reproducer corroborate classical eigenvalue ordering but are not substituted for the established spectral theorem for a Neumann disk. The restricted rational parameter family illustrates an open reentrant mechanism; no all-parameter classification is asserted.

## References
1. G. Shanmugasundaram, J. Saha, O. D. Makinde and J. Chattopadhyay, *Asymptotic stability and diffusion-driven pattern formation in a predator-prey system with two chemicals*, arXiv:2604.18129v1 (first public April 20, 2026), especially equations (2.7), (6.7) and Section 6.
2. Q. Shi, M. Liu and X. Xu, *Turing–Hopf bifurcation of a ratio-dependent predator-prey model with diffusion*, Advances in Difference Equations 2019, 310, DOI:10.1186/s13662-019-2123-3.
3. E. A. Gaffney, A. L. Krause, P. K. Maini and C. Wang, *Spatial Heterogeneity Localizes Turing Patterns in Reaction-Cross-Diffusion Systems*, arXiv:2210.10155.
4. K. Wang et al., *Simulations of pattern dynamics for reaction-diffusion systems via SIMULINK*, BMC Systems Biology 8, 45 (2014), DOI:10.1186/1752-0509-8-45.
5. Classical Neumann disk spectrum: separation of variables with zeros of \(J_m'\), as tabulated in the NIST Digital Library of Mathematical Functions, Chapter 10.
