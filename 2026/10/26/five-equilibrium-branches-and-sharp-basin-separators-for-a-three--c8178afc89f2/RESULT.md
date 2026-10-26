# Five equilibrium branches and sharp basin separators for a three-agent sigmoidal confidence model

## Finding
For every fixed confidence parameter \(1<\delta<4\), there is a finite \(\Gamma(\delta)\) such that every steepness \(\gamma>\Gamma(\delta)\) produces exactly five equilibria in the three-agent sigmoidal bounded-confidence model described below. In increasing order they are \(-v_\gamma,-u_\gamma,0,u_\gamma,v_\gamma\), with \(0<u_\gamma<v_\gamma<1\). The equilibria \(-v_\gamma,0,v_\gamma\) are asymptotically stable; \(\pm u_\gamma\) are unstable. Each solution in \([-1,1]\) converges to one of these five equilibria. The unstable equilibria are the exact basin boundaries: initial opinions in \((-u_\gamma,u_\gamma)\) tend to \(0\); those in \((u_\gamma,1]\) tend to \(v_\gamma\); those in \([-1,-u_\gamma)\) tend to \(-v_\gamma\); and an initial opinion precisely at an equilibrium stays there.

Let \(h=\sqrt{\delta}-1\in(0,1)\). The separators and polarized attractors have the quantitative limits
\[
u_\gamma=h+\frac{\log(2h/(1-h))}{2\sqrt{\delta}\,\gamma}+O_\delta(\gamma^{-2}),\qquad
1-v_\gamma=2e^{-\gamma(4-\delta)}\left[1+O_\delta\!\left(\gamma e^{-\gamma(4-\delta)}+e^{-\gamma\delta}\right)\right].
\]
Thus the limiting basin boundary lies at the geometric confidence-crossing opinion \(\sqrt{\delta}-1\), not at the center of the opinion interval. The statement is a fixed-\(\delta\), large-\(\gamma\) theorem: it makes no assertion of a uniform steepness threshold as \(\delta\) approaches \(1\) or \(4\).

## Assumptions and scope
The connected three-vertex path has two fixed-opinion endpoints (zealots) with opinions \(-1\) and \(1\), and one persuadable central vertex with time-dependent opinion \(x(t)\). The endpoints are not adjacent to each other. The original continuous-time sigmoidal bounded-confidence rule of Brooks--Chodrow--Porter weights a difference \(z\) by \(w(z)=[1+\exp\{\gamma(z^2-\delta)\}]^{-1}\), with \(\gamma>0\). Put
\[
w_+(x)=\frac1{1+e^{\gamma((1-x)^2-\delta)}},\qquad
w_-(x)=\frac1{1+e^{\gamma((1+x)^2-\delta)}}.
\]
The persuadable agent obeys the autonomous equation
\[
\dot x=f_\gamma(x)=\frac{(1-x)w_+(x)-(1+x)w_-(x)}{w_+(x)+w_-(x)}.
\]
All statements quantify over every fixed real \(\delta\in(1,4)\) and all sufficiently large real \(\gamma\), and over every initial \(x(0)\in[-1,1]\). The exponential weights are strictly positive for every finite \(\gamma\).

## Proof
**1. Exact scalar equilibrium function.** Define
\[
F_\gamma(x)=(1-x)e^{\gamma((1+x)^2-\delta)}-(1+x)e^{\gamma((1-x)^2-\delta)}-2x.
\]
Multiplication of the numerator of \(f_\gamma\) by the positive product of its two logistic denominators shows that \(\operatorname{sgn} f_\gamma(x)=\operatorname{sgn}F_\gamma(x)\), including equality. This reduction requires no asymptotic approximation. The function \(F_\gamma\) is odd, so it suffices to classify positive roots. Also
\[
F_\gamma'(0)=2\big((2\gamma-1)e^{-\gamma(\delta-1)}-1\big)<0
\]
for all sufficiently large \(\gamma\). Thus the central equilibrium is attracting.

**2. Exclusion of roots away from two transition layers.** Fix \(h=\sqrt\delta-1\) and choose \(\eta>0\) sufficiently small that \(0<h-\eta<h+\eta<1-\eta<1\) and \((2-\eta)^2>\delta\). Write \(A(x)=(1-x)e^{\gamma((1+x)^2-\delta)}\) and \(B(x)=(1+x)e^{\gamma((1-x)^2-\delta)}\), so \(F=A-B-2x\). On \([0,h-\eta]\), both exponentials and their first derivatives tend uniformly to zero, because \((1+x)^2-\delta\) and \((1-x)^2-\delta\) are bounded strictly below zero. Hence \(F_\gamma'\to-2\) uniformly there, implying \(F_\gamma(x)<0\) for all \(x\in(0,h-\eta]\).

On \([h+\eta,1-\eta]\), \((1+x)^2-\delta\) is bounded strictly above zero, while \((1-x)^2-\delta\le 1-\delta<0\). Also \(1-x\ge\eta\). Thus \(A\to+\infty\) uniformly, \(B\to0\) uniformly and \(F_\gamma>0\) throughout this interval for large \(\gamma\).

**3. Precisely one separator near \(h\).** Direct differentiation gives
\[
A''=e^{\gamma((1+x)^2-\delta)}\{4\gamma^2(1-x)(1+x)^2-2\gamma(1+3x)\},
\]
\[
B''=e^{\gamma((1-x)^2-\delta)}\{4\gamma^2(1+x)(1-x)^2+2\gamma(3x-1)\}.
\]
On the fixed interval \([h-\eta,h+\eta]\), the leading positive term of \(A''\) dominates the term from \(B''\) because their exponent difference is \(4\gamma x\), uniformly bounded below by \(4\gamma(h-\eta)>0\). Therefore \(F_\gamma''>0\) there for all large \(\gamma\). With negative sign at the left endpoint and positive sign at the right endpoint, strict convexity gives precisely one root \(u_\gamma\) in this interval; at this root \(F_\gamma'(u_\gamma)>0\), so it is repelling.

**4. Precisely one attracting outer root.** Fix any \(\kappa\in(0,1/4)\). On \([1-\eta,1-\kappa/\gamma]\), \(A\) is uniformly larger than \((\kappa/\gamma)e^{\gamma((2-\eta)^2-\delta)}\), while \(B\) is uniformly exponentially small. Consequently \(F_\gamma>0\) there. On the final interval \([1-\kappa/\gamma,1]\),
\[
A'=e^{\gamma((1+x)^2-\delta)}[-1+2\gamma(1-x^2)]<0
\]
because \(2\gamma(1-x^2)\le4\kappa<1\). The derivative \(B'\) is exponentially small on that interval, so \(F_\gamma'=A'-B'-2<0\) there for large \(\gamma\). As \(F_\gamma(1)=-2-2e^{-\gamma\delta}<0\), there is exactly one root \(v_\gamma\) in the final interval; it is attracting. Steps 1--4 exhaust \((0,1)\), and oddness gives the other two nonzero equilibria. Positivity of \(w_\pm\) and the strict inward pointing field at \(\pm1\) imply invariance of \([-1,1]\). Alternating signs between the five simple equilibria give their stability and all stated basins. One-dimensional uniqueness and monotonicity imply convergence of each orbit.

**5. Separator and attractor asymptotics.** At the separator, the exact root equation is
\[
\gamma((1+u_\gamma)^2-\delta)
=\log\frac{2u_\gamma}{1-u_\gamma}
+\log\!\left(1+\frac{1+u_\gamma}{2u_\gamma}e^{\gamma((1-u_\gamma)^2-\delta)}\right).
\]
Step 3 shows \(u_\gamma\to h>0\), and \((1-h)^2-\delta=-4h<0\). The last logarithm is exponentially small in \(\gamma\), uniformly in a small neighborhood of \(h\). The identity first yields \(u_\gamma-h=O_\delta(\gamma^{-1})\), and a first-order Taylor expansion then gives the displayed \(1/\gamma\) correction with remainder \(O_\delta(\gamma^{-2})\).

For the outer root set \(\varepsilon_\gamma=1-v_\gamma\). Step 4 gives \(\varepsilon_\gamma\to0\), and its exact equation becomes
\[
\varepsilon_\gamma e^{\gamma(4-\delta-4\varepsilon_\gamma+\varepsilon_\gamma^2)}
=2(1-\varepsilon_\gamma)+(2-\varepsilon_\gamma)e^{\gamma(\varepsilon_\gamma^2-\delta)}.
\]
The right-hand side is bounded above and below by positive constants for large \(\gamma\), forcing \(\varepsilon_\gamma=O_\delta(e^{-\gamma(4-\delta)})\) after using the unique outer-layer root and its monotone equation; substituting this bound back and expanding the exponential yields the displayed relative error. This proves both asymptotic statements.

## Verification
`verify.py` uses only Python's standard-library `decimal` arithmetic. It reconstructs the exact equilibrium function and derivative, isolates both positive roots independently by sign-bracket bisection for several rational values of \(\delta\) and integer steepness values, verifies all five equilibrium stabilities by analytic derivatives, checks the alternating vector-field signs and confirms the two leading asymptotic regimes numerically. These are finite diagnostics only; the global counts, basins and asymptotic error estimates follow from the analytical proof above, not from the sampling.

## Relationship to prior work
Brooks, Chodrow and Porter define this sigmoidal bounded-confidence flow, prove general statements relating its steep-confidence limit to Hegselmann--Krause dynamics, and give the balanced-exposure criterion for **linear stability of the harmonic equilibrium** (published Theorem 6). They also examine numerical stable branches on larger two-community networks and formulate a general conjecture about approximating discontinuous-model equilibrium interaction patterns (published Conjecture 1). Those statements do not give an exact equilibrium census, global scalar basins, or quantitative separator and attractor asymptotics for the present three-vertex path. In particular, harmonic linear stability by itself cannot determine the existence or location of other attracting branches. The present result is a special, explicitly solved regime, not a proof of their general conjecture.

Other nonlinear zealot-voter models, including Mobilia's \(q\)-voter process, employ stochastic discrete opinions and different update laws. General hard-threshold bounded-confidence convergence results concern discontinuous rather than finite-\(\gamma\) logistic weights. No general uniqueness of the present theorem in the literature is asserted.

## Limitations
The classification holds for each fixed \(\delta\in(1,4)\) once \(\gamma\) is sufficiently large; no explicit optimal finite \(\Gamma(\delta)\) is given. The endpoints \(\delta=1\) and \(\delta=4\), different confidence kernels, stochastic perturbations, asymmetric zealots, and networks with more persuadable individuals are outside the claim. The theorem is one-dimensional and must not be extrapolated to general network bifurcation structure. No independent validation has been performed.

## References
1. H. Z. Brooks, P. S. Chodrow, and M. A. Porter, *Emergence of polarization in a sigmoidal bounded-confidence model of opinion dynamics*, first public arXiv version 2022-09-15, arXiv:2209.07004; SIAM Journal on Applied Dynamical Systems 23 (2024), 1442--1470, DOI 10.1137/22M1527258. https://arxiv.org/abs/2209.07004
2. M. Mobilia, *Nonlinear q-voter model with inflexible zealots*, Physical Review E 92 (2015), 012803, DOI 10.1103/PhysRevE.92.012803 (distinct stochastic model).
3. C. Bernardo, C. Altafini, A. Proskurnikov, and F. Vasca, *Bounded confidence opinion dynamics: A survey*, Automatica 159 (2024), 111302, DOI 10.1016/j.automatica.2023.111302 (background on hard-threshold models).
