# Nonlinear six-season resonance selection in the delayed Beverton--Holt map

## Finding

Consider the positive delayed Beverton--Holt recurrence
\[
 x_{n+1}=\frac{\lambda x_n}{1+(\lambda-1)x_{n-1}/K_n},\qquad
 K_n=\exp\!\left(\frac{\eta}{\lambda}\cos\frac{\pi n}{3}\right),
 \quad \lambda>1,
\]
with a fixed real forcing amplitude \(\eta\). Let \(x_{j,\lambda}^{*}>0\), \(j\in\mathbb Z/6\mathbb Z\), denote its unique positive six-periodic orbit, in its forcing-indexed phase. Such an orbit exists and attracts all positive initial states for every finite \(\lambda>1\), by the global-attraction theorem cited below.

**Theorem (nonlinear resonance selection).** There is exactly one real \(q=q(\eta)\) satisfying
\[
 \frac23\left(\sinh q+\sinh\frac q2\right)=\eta.
\]
For each fixed \(\eta\in\mathbb R\), as \(\lambda\to\infty\),
\[
 \boxed{\quad
 \log x_{j,\lambda}^{*}
 =-q(\eta)\cos\left(\frac{\pi(j+1)}3\right)
 +O_{\eta}(\lambda^{-1}),\quad j=0,\ldots,5.\quad}
\]
The error is uniform across the six phases; it is also locally uniform as \(\eta\) ranges over any fixed compact interval. Consequently, the environmental modulation \(K_n-1=O_\eta(\lambda^{-1})\) vanishes while the attracting population cycle retains a finite, nonconstant profile whenever \(\eta\ne0\). The selected amplitude satisfies
\[
 q(\eta)=\eta-\frac{\eta^3}{8}+O(\eta^5)
 \quad(\eta\to0),\qquad
 q(\eta)=\operatorname{sgn}(\eta)\bigl[\log(3|\eta|)+o(1)\bigr]
 \quad(|\eta|\to\infty).
\]
In particular, the nonlinearly selected response grows only logarithmically at large scaled forcing.

For context, differentiating the finite-\(\lambda\) positive cycle at zero forcing gives the *exact* linear susceptibility
\[
 \left.\frac{\partial\log x_{j,\lambda}^{*}}{\partial\eta}\right|_{\eta=0}
 =-\left(1-\frac1\lambda\right)\cos\left(\frac{\pi(j+1)}3\right).
\]
Equivalently, differentiation with respect to the actual log-carrying-capacity amplitude \(\varepsilon=\eta/\lambda\) has magnitude \(\lambda-1\). The nonlinear law above resolves this diverging susceptibility on its natural \(\varepsilon\asymp\lambda^{-1}\) scale.

## Assumptions and scope

The theorem concerns the positive, phase-labelled attracting orbit of the explicitly given second-order, nonautonomous smooth recurrence. The growth factor satisfies \(\lambda>1\); the forcing parameter \(\eta\) is fixed before taking \(\lambda\to\infty\), although it may have either sign. The baseline carrying capacity equals one; a positive constant baseline \(K\) is restored by multiplying every population value by \(K\). No joint limit with \(|\eta|\to\infty\) is claimed. The associated map acts on the positive quadrant by \((u,v)\mapsto(v,\lambda v/[1+(\lambda-1)u/K_n])\), making this a problem about the attracting periodic orbit of a nonautonomous planar dynamical system (MSC2020 \(37C60\)).

## Proof

**1. Existence and uniqueness of the finite-growth cycle.** Write the recurrence as \(x_{n+1}=x_n f_n(x_{n-1})\), where
\[
 f_n(t)=\frac{\lambda}{1+(\lambda-1)t/K_n}.
\]
For \(\lambda>1\) and \(K_n>0\), each \(f_n\) is positive, bounded, continuous, strictly decreasing, and \(t f_n(t)\) is strictly increasing for \(t\ge0\). Also \(\prod_{n=0}^5f_n(0)=\lambda^6>1\) and \(\lim_{t\to\infty}\prod_{n=0}^5f_n(t)=0\). Theorem 1.1 and Corollary 6.1 of Ishihara--Nakata (2010) therefore give a globally attracting positive six-periodic solution. It is unique: a different positive six-periodic solution would constitute an initial state unable to converge to the first one.

**2. The singular periodic problem.** Put \(\delta=\lambda^{-1}\) and \(z_j=\log x_{j,\lambda}^{*}\). Indices are cyclic modulo six. Let \(h_j=\cos(\pi j/3)\). The six periodic equations are exactly
\[
 F_j(z,\delta,\eta):=z_{j+1}-z_j+
 \log\!\left[\delta+(1-\delta)
 \exp(z_{j-1}-\delta\eta h_j)\right]=0.
\]
The expression is real analytic near every finite \((z,0,\eta)\). Taylor expansion in \(\delta\), locally uniform in the six coordinates, yields
\[
 F_j=(Lz)_j+\delta\bigl[e^{-z_{j-1}}-1-\eta h_j\bigr]
 +O(\delta^2),\qquad
 (Lz)_j=z_{j+1}-z_j+z_{j-1}.
\]
On six-periodic sequences the real symmetric cyclic matrix \(L\) has Fourier eigenvalues \(2\cos(\pi m/3)-1\), \(m=0,\ldots,5\). Thus \(\ker L=E\), the two-dimensional span of \(\cos(\pi j/3)\) and \(\sin(\pi j/3)\); \(L\) is invertible on \(E^\perp\).

**3. Lyapunov--Schmidt reduction with a nonzero selected amplitude.** Let \(P\) be orthogonal projection onto \(E\), and \(Q=1-P\). Decompose \(z=v+w\), with \(v\in E\) and \(w\in E^\perp\). By the analytic implicit-function theorem, \(QF(v+w,\delta,\eta)=0\) determines a unique analytic \(w=W(v,\delta,\eta)\) near any fixed \((v,0,\eta)\), with \(W(v,0,\eta)=0\). Dividing the remaining \(P F\) equation by \(\delta\) has an analytic extension to \(\delta=0\), where it becomes
\[
 R(v,\eta):=P\bigl(e^{-v_{j-1}}-1-\eta h_j\bigr)=0.
\]
The vector \(v_j=-q\cos(\pi(j+1)/3)\) has \(v_{j-1}=-q h_j\). Reflection symmetry makes the sine coefficient of \(e^{q h_j}\) vanish, and its cosine coefficient is exactly
\[
 \frac13\sum_{j=0}^{5}e^{q h_j}h_j
 =\frac23\left(\sinh q+\sinh\frac q2\right).
\]
Hence \(R(v,\eta)=0\) precisely when \(q\) solves the displayed amplitude equation. The right side has strictly positive derivative \((2/3)[\cosh q+(1/2)\cosh(q/2)]\), ranges over the full real line, and determines a unique real \(q\).

For the nondegeneracy required by the second implicit-function theorem, differentiate \(R\) in the \(v\) variable. Up to sign, the derivative is \(P D S^{-1}|_E\), where \((S^{-1}u)_j=u_{j-1}\) and \(D\) is the strictly positive diagonal multiplication \((Du)_j=e^{-v_{j-1}}u_j\). The cyclic shift \(S^{-1}\) is an isomorphism of \(E\), while \(P D|_E\) is positive definite, since \(\langle u,P Du\rangle=\sum_j e^{-v_{j-1}}u_j^2>0\) for all \(0\ne u\in E\). Therefore \(D_vR\) is invertible. The analytic implicit-function theorem supplies a six-periodic solution \(z(\delta,\eta)=v(\eta)+O_\eta(\delta)\) for all sufficiently small positive \(\delta\). Its six exponentials are positive. By Step 1 this must be the globally attracting positive orbit. Analytic dependence on \(\eta\), compact covering, and uniqueness give the stated locally uniform error.

**4. Explicit amplitude limits and susceptibility.** Expanding the hyperbolic sines gives \(\eta=q+q^3/8+O(q^5)\), whose local inverse is \(q=\eta-\eta^3/8+O(\eta^5)\). For \(q\to+\infty\) the right side is asymptotic to \(e^q/3\); oddness handles negative \(q\). Finally, at \(\eta=0\), the finite-\(\lambda\) periodic orbit is identically one. Linearization in \(\eta\) gives
\[
 u_{j+1}-u_j+\left(1-\frac1\lambda\right)u_{j-1}
 =\frac{1-\lambda^{-1}}{\lambda}h_j,
 \quad u_j=\left.\frac{\partial z_j}{\partial\eta}\right|_{0}.
\]
The cosine identity \(h_{j+2}-h_{j+1}=-h_j\) verifies the unique periodic solution \(u_j=-(1-\lambda^{-1})h_{j+1}\), completing the proof.

## Verification

Run `python3 verify.py` with Python 3 from the directory containing this document. The standalone checker verifies the six-cycle Fourier nullspace by exact rational elimination, checks the first-harmonic hyperbolic-sine identity, solves the actual positive six-periodic equations numerically for several forcing values and growth rates, and checks the exact finite-\(\lambda\) susceptibility by centered differences. It reports `VERIFY_OK` on successful completion. These finite computations are auxiliary consistency tests; the infinite-parameter assertion follows from the analytical implicit-function argument above.

## Relationship to prior work

Ishihara and Nakata (2010, arXiv:1006.3379, initially public 2010-06-17) prove global attraction for a class of periodically forced delayed Pielou recurrences and explicitly include the delayed Beverton--Holt specialization. This supplies Step 1; the high-growth sixth-root singular limit and nonlinear phase-selection formula are additional claims. Kocic (2009/2010) investigates geometric-mean attenuance with delay; it does not, in the examined accessible sections, provide the finite nonzero response under vanishing six-season forcing. Haskell, Yang and Sacker (2012 online/2013 print) study resonance/attenuation in the **one-step**, non-delayed Beverton--Holt recurrence and hence do not imply the delayed, two-dimensional six-root mechanism. The broader periodic-forcing and delay literature makes independent priority assessment appropriate; the result is not presented as externally certified.

## Limitations

The theorem is for the forcing-indexed positive six-cycle and fixed scaled \(\eta\); no uniformity is claimed when \(\eta\) grows with \(\lambda\). It does not give a global rate of convergence of arbitrary initial states to that orbit as \(\lambda\to\infty\), nor a theorem for general forcing waveforms or non-six periods. The argument uses an established global-attraction theorem, with its hypotheses explicitly checked. Two relevant papers on delayed geometric-mean attenuance were not accessible as continuous full text in the present source inspection; therefore independent bibliographic priority verification remains a residual risk.

## References

1. K. Ishihara and Y. Nakata, *On a generalization of the global attractivity for a periodically forced Pielou's equation* (first arXiv version 2010-06-17), arXiv:1006.3379. https://arxiv.org/abs/1006.3379
2. V. L. Kocic, *A note on the nonautonomous delay Beverton--Holt model*, Journal of Biological Dynamics 4 (2010), 131--139, first online 2009-04-17. https://doi.org/10.1080/17513750902803588
3. V. L. Kocic, *Generalized attenuant cycles in some discrete periodically forced delay population models*, Journal of Difference Equations and Applications 16 (2010), 1141--1149. https://doi.org/10.1080/10236190902766850
4. Y. Yang, R. J. Sacker, with appendix by C. Haskell, *Resonance and attenuation in the n-periodic Beverton--Holt equation*, Journal of Difference Equations and Applications 19 (2013), 1174--1191, online 2012-10-09. https://doi.org/10.1080/10236198.2012.726988
