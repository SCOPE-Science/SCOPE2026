# A sharp one-band seasonal instability threshold in a two-species ecological feedback model

## Finding
Consider two populations with positive common coexistence equilibrium \(E=(1,1)\), alternating between one-way facilitation and one-way inhibition. Although **both frozen seasons and every duty-weighted average Jacobian are Hurwitz**, the coexistence state is linearly unstable for some intermediate periods. The **complete** period-and-duty-cycle classification is
\[
\text{unstable}\quad\Longleftrightarrow\quad
bc\,\vartheta(1-\vartheta)T^2>4\cosh^2(aT/2).
\]
Strict reversal gives local exponential stability. Equality has a simple multiplier \(-1\) and a second multiplier \(-e^{-2aT}\); no nonlinear stability assertion is made there.

For fixed duty share \(0<\vartheta<1\), put \(\nu=\sqrt{bc\,\vartheta(1-\vartheta)}\). There is an **unstable open interval of periods** if and only if
\[
\frac{a}{\nu}< H_*:=\frac{w_*}{\cosh w_*},\qquad
w_*>0,\quad w_*\tanh w_*=1.
\]
The scalar \(w_*\) exists uniquely and \(H_*=0.66274341934918158\ldots\). If \(a/\nu=H_*\), one isolated period \(T=2w_*/a\) is neutral and all other periods are exponentially stable. If \(a/\nu>H_*\), every period is exponentially stable. When the interval exists, its two endpoints are the only two positive solutions of \(\nu T=2\cosh(aT/2)\).

At any fixed period, the unstable duty shares, if any, constitute exactly **one interval symmetric about one half**. In particular, equal-duration seasons are most destabilizing, while sufficiently unbalanced durations are always stabilizing.

## Assumptions and scope
All parameters \(a,b,c,T\) are strictly positive and the duty share satisfies \(0<\vartheta<1\). In each period of length \(T\), the population state \((x,y)\in(0,\infty)^2\) follows season A for duration \(\vartheta T\):
\[
\dot x=x\,[a(1-x)+b(y-1)],\qquad
\dot y=a y(1-y).
\]
It then follows season B for duration \((1-\vartheta)T\):
\[
\dot x=a x(1-x),\qquad
\dot y=y\,[a(1-y)-c(x-1)].
\]
Repeat periodically, with continuous states across switches. Each season uses logistic self-regulation, and only one cross-species feedback direction is active at a time. The positive quadrant is forward invariant. Indeed, throughout both seasons \(\dot y\le y[(a+c)-ay]\), hence \(y\) is bounded above by \(Y=\max\{y(0),1+c/a\}\). Consequently \(\dot x\le x[a+bY-ax]\) in season A, and \(\dot x\le ax(1-x)\) in season B. All positive solutions therefore exist globally and remain bounded. The equilibrium \(E\) exists in both seasons, so it is a period-\(T\) solution.

The claim is a *local* Floquet stability classification of this exact nonlinear ecological system. It does not assert that every unstable parameter produces a periodic orbit, or that every locally stable equilibrium attracts all positive initial data.

## Proof
**Step 1: seasonal linearizations and the monodromy.** At \(E\) the seasonal Jacobians are
\[
J_A=\begin{pmatrix}-a&b\\0&-a\end{pmatrix},\qquad
J_B=\begin{pmatrix}-a&0\\-c&-a\end{pmatrix}.
\]
Each has two eigenvalues \(-a\). Their duty-weighted mean is
\[
\vartheta J_A+(1-\vartheta)J_B
=\begin{pmatrix}-a&\vartheta b\\-(1-\vartheta)c&-a\end{pmatrix}
\]
with eigenvalues \(-a\pm i\sqrt{bc\,\vartheta(1-\vartheta)}\). Thus neither instantaneous instability nor instability of the averaged matrix accounts for the result. The exact monodromy, with season B after A, is
\[
M=e^{J_B(1-\vartheta)T}e^{J_A\vartheta T}
=e^{-aT}\begin{pmatrix}
1&b\vartheta T\\
-c(1-\vartheta)T&1-bc\,\vartheta(1-\vartheta)T^2
\end{pmatrix}.
\]
Put \(z=T\sqrt{bc\,\vartheta(1-\vartheta)}\). The matrix \(Q=e^{aT}M\) has \(\operatorname{tr}Q=2-z^2\), \(\det Q=1\). For \(z\le2\), \(\rho(Q)=1\), including the defective endpoint \(z=2\). For \(z>2\), the eigenvalues of \(Q\) are \(-e^{2u}\) and \(-e^{-2u}\), where \(u=\operatorname{arcosh}(z/2)\); this follows from \(2-z^2=-2\cosh(2u)\). Therefore the maximal real Floquet exponent is exactly
\[
\Lambda(T,\vartheta)=-a+
\begin{cases}
0,&z\le2,\\[2pt]
2\operatorname{arcosh}(z/2)/T,&z>2.
\end{cases}
\]
Since \(a>0\), the condition \(\Lambda>0\) is equivalent to \(z>2\cosh(aT/2)\), proving the displayed sharp inequality. Equality forces the eigenvalues of \(M\) to be \(-1\) and \(-e^{-2aT}\), the former simple. Standard linearization of the smooth period map gives local exponential stability for \(\Lambda<0\) and nonlinear local instability for \(\Lambda>0\).

**Step 2: exactly one period band.** At fixed \(\vartheta\), the instability criterion is \(F(T)>1\) for
\[
F(T)=\frac{\nu T}{2\cosh(aT/2)}
=\frac{\nu}{a}\frac{w}{\cosh w},\qquad w=aT/2.
\]
For positive \(w\), the derivative of \(w/\cosh w\) has the sign of \(1-w\tanh w\). The product \(w\tanh w\) strictly increases from zero to infinity, so there is exactly one maximizing \(w_*\). Moreover \(F(T)\to0\) as \(T\downarrow0\) and as \(T\to\infty\). Hence the trichotomy and uniqueness of the two instability endpoints follow, including the isolated tangency case.

**Step 3: duty-cycle interval.** At fixed \(T\), write \(C_T=4\cosh^2(aT/2)/(bcT^2)\). The unstable shares solve \(\vartheta(1-\vartheta)>C_T\). None exist when \(C_T\ge1/4\). Otherwise the exact open interval is
\[
\frac{1-\sqrt{1-4C_T}}{2}<\vartheta<
\frac{1+\sqrt{1-4C_T}}{2}.
\]
The maximum \(\vartheta(1-\vartheta)=1/4\) occurs only at equal season durations; this gives the claimed optimality and a complete duty-cycle phase diagram.

## Verification
For \(a=1\), \(b=c=4\) and \(\vartheta=1/2\), the instability condition becomes \(T>\cosh(T/2)\). There are exactly two positive crossings,
\[
T_-=1.1787755269387010\ldots,\qquad
T_+=4.2535997853565131\ldots .
\]
Thus \(T=0.4\) and \(T=8\) give locally exponentially stable coexistence, whereas \(T=2\) gives a positive exponent \(0.3169578969248167\ldots\) and local instability. At \(T=2\), the unstable duty interval is \((0.1819097853538457\ldots,0.8180902146461543\ldots)\).

The supplied standalone `check.py` uses rational arithmetic for all nilpotent-shear matrix-product identities (25 rational cases), then independently compares high-precision eigenvalues of the period matrix with the hyperbolic formula for 1,600 parameter sets. It also checks the universal critical constant, two period crossings, duty boundaries, and one stable–unstable–stable example. Run it with `python check.py` using the Python standard library. This computational replay is supporting verification; the all-parameter result follows from the preceding exact proof.

## Relationship to prior work
Swailem and Rucklidge (arXiv:2511.03521, first publicly posted 2025-11-05) investigate sinusoidally driven predator–prey dynamics and obtain resonance tongues by numerical Floquet integration in a different nonlinear model. Their equations (1), (2), and (9), and the discussion of the subharmonic tongue, do not provide the present two-season triangular ecological model or its sharp one-band duty-and-period classification.

Gökçek (2004) establishes the *general* product-of-matrix-exponentials Floquet test for periodically switched linear systems (Theorem 3.1), as well as fast- and slow-switching sufficient stability results. Those general foundations are used here and not claimed as new. In particular, the pointwise monodromy calculation is standard; the new object and the globally sharp analytic partition of its joint biological season-length and duty parameters, including the universal unique-band threshold, are the substantive specialization. His Examples 4.1 and 4.2 use different matrices and do not classify this biological family.

Cima, Gasull and Mañosa (arXiv:1911.12245, 2019; *Nonlinear Dynamics*, 2020) already prove that alternation of two stable planar polynomial vector fields can reverse equilibrium stability (a continuous-seasonal form of Parrondo’s paradox). **The occurrence of that qualitative paradox is therefore prior knowledge**, not a new claim here. Their Theorem 1 gives existence using prescribed nonhyperbolic elliptic normal forms and fixed unit-duration seasons; it does not furnish this positive, logistic, hyperbolic two-species ecological family, the critical monotone equation, the exact two-end period band, or the duty-share interval. Their proof in Section 3 is structurally different from the present exact eigenvalue calculation.

Ji and Strugarek (arXiv:1804.07641, 2018) establish sharp duty-share thresholds for **cooperative**, concave seasonal population models, including a juvenile/adult ecological system. Their Theorems 1–3 require monotone cooperative dynamics and exploit Perron–Frobenius order; the present season B has negative cross-species derivative and is not cooperative, so their monotonicity threshold is not applicable. The present instability is centered at intermediate duty shares, whereas their studied persistence/extinction dichotomy has a one-sided seasonal threshold.

Chowdhury (arXiv:2608.14081, posted 2026-08-14) studies frequency-dependent ecological-network resilience, including high-frequency stabilization for large random network interaction matrices. The accessible abstract does not present this finite-dimensional exact classification; the full preprint could not be inspected and remains a literature-overlap risk, rather than evidence of absence.

## Limitations
Only local stability around the common coexistence equilibrium is asserted. A multiplier exactly \(-1\) does not by itself establish a nonlinear flip bifurcation or neutral nonlinear stability. The model idealizes alternating one-way species interaction and does not describe demographic stochasticity, migration, or finite environmental adjustment time. There is no claim that the general Floquet product theorem is new. Although direct searches identified no prior exact one-band duty-cycle threshold for this particular ecological family, unindexed switched-systems literature and inaccessible full texts remain possible sources of stronger coverage.

## References
- M. Swailem and A. M. Rucklidge, *Parametric resonance, chaos and spatial structure in the Lotka–Volterra model*, arXiv:2511.03521v2 (first submission 2025-11-05). https://arxiv.org/html/2511.03521v2
- C. Gökçek, *Stability analysis of periodically switched linear systems using Floquet theory*, Mathematical Problems in Engineering 2004, Article 521989, doi:10.1155/S1024123X04401069. https://onlinelibrary.wiley.com/doi/pdf/10.1155/S1024123X04401069
- A. Cima, A. Gasull and V. Mañosa, *A dynamic Parrondo’s paradox for continuous seasonal systems*, arXiv:1911.12245v1 (2019), *Nonlinear Dynamics* **102** (2020), 1033–1043. https://arxiv.org/pdf/1911.12245
- H. Ji and M. Strugarek, *Sharp seasonal threshold property for cooperative population dynamics with concave nonlinearities*, arXiv:1804.07641v1 (2018), *Bulletin des Sciences Mathématiques* **147** (2018), 58–82. https://arxiv.org/pdf/1804.07641
- S. N. Chowdhury, *Periodic Environmental Forcing Shapes the Stability of Complex Ecological Networks*, arXiv:2608.14081 (first submission 2026-08-14). https://arxiv.org/abs/2608.14081
