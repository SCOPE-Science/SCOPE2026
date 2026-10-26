# Exponential-memory queue reflection: sharp uniform moduli and a local \(J_1\) boundary

## Finding
The one-sided memory-reflection map arising from exponential service times has an exact weighted-running-supremum formula. Its occupancy and cumulative-loss coordinates have **sharp, horizon-independent or linearly horizon-dependent uniform Lipschitz moduli**, respectively. Both coordinates are locally Lipschitz for the Skorokhod \(J_1\) topology; neither is globally \(J_1\)-Lipschitz when the exponential decay rate is positive. The latter boundary contrasts with the uniform-norm estimates and supplies a precise restricted answer to the \(J_1\) question raised in Remark 3.11 of Wang--Chakraborty (2026).

## Assumptions and scope
Fix \(T>0\) and \(\beta\ge0\). All inputs \(\rho:[0,T]\to\mathbb R\) are real-valued càdlàg and satisfy \(\rho(0)\le1\). Set \(K_\beta(t)=e^{-\beta t}\), the survival kernel of an exponential service law when \(\beta>0\). A solution is a pair of càdlàg paths \(y,\eta\) with \(\eta\) nondecreasing, \(\eta(0)=0\),
\[y(t)=\rho(t)-\int_{(0,t]}e^{-\beta(t-s)}\,d\eta(s)\le1,\qquad \int_{(0,T]}\mathbf 1_{\{y(s)<1\}}\,d\eta(s)=0.\]
Here \((x)_+=\max\{0,x\}\), \(\|f\|_T=\sup_{0\le t\le T}|f(t)|\). No regularity of input besides càdlàg is assumed; in particular, jumps are admitted. For \(J_1\) take the usual increasing homeomorphism time changes fixing \(0\) and \(T\), with metric given by the infimum over time changes of the maximum of time-shift and path-error suprema. Product-space comparisons use the same time change for both outputs.

## Proof
**1. Explicit solution and complementarity.** Let \(m(t)=\int_{(0,t]}e^{-\beta(t-s)}d\eta(s)\). Multiplying by \(e^{\beta t}\) gives the nondecreasing process
\[z(t)=e^{\beta t}m(t)=\int_{(0,t]}e^{\beta s}\,d\eta(s),\qquad z(0)=0.\]
The obstacle \(y\le1\) becomes \(z(t)\ge e^{\beta t}(\rho(t)-1)\). The support of \(dz=e^{\beta t}d\eta\) is confined to equality of this obstacle, since \(y=1\) there. Therefore \(z\) solves the ordinary one-sided Skorokhod problem at a time-varying obstacle and necessarily equals
\[z(t)=\sup_{0\le s\le t}\bigl[e^{\beta s}(\rho(s)-1)\bigr]_+.\]
This running supremum is a nondecreasing càdlàg function (a downward jump in the obstacle does not undo its preceding supremum). Conversely, this formula produces a nondecreasing \(z\); its Stieltjes measure increases only when the current obstacle equals \(z\), so the associated \(\eta(t)=\int_{(0,t]}e^{-\beta s}dz(s)\) satisfies complementarity. Integration by parts in \(m(t)=e^{-\beta t}z(t)\) gives
\[\eta(t)=m(t)+\beta\int_0^t m(s)\,ds,\]
which also proves uniqueness. The stated formulas follow.

**2. Sharp uniform bounds.** For any two inputs define \(d=\|\rho_1-\rho_2\|_T\). The positive-part map, exponential weights \(0<K_\beta\le1\), and supremum imply \(\|m_1-m_2\|_T\le d\). Consequently,
\[\|y_1-y_2\|_T\le2d,\qquad \|\eta_1-\eta_2\|_T\le(1+\beta T)d.\]
To see the occupancy constant is optimal, compare the fixed input \(\rho_0\equiv1\) with a second path equal to \(1\) before a time \(a>0\), equal to \(1+d\) during \([a,a+h)\), and equal to \(1-d\) thereafter. At the downward jump the second occupancy equals \(1-d-d\), because continuous reflection keeps the memory at \(d\) throughout the elevated plateau. Its distance from \(\rho_0\) is exactly \(2d\), for every \(h>0\). For the regulator, compare \(\rho_0\) with the path equal to \(1+d\) on \([a,T]\), and \(1\) before \(a\). Its regulator at \(T\) is \(d[1+\beta(T-a)]\); letting \(a\downarrow0\) attains the optimal Lipschitz constant as a supremum. This also covers \(\beta=0\).

**3. A quantitative \(J_1\) bound.** Suppose both inputs have absolute supremum at most \(M\), and set \(B=(M-1)_+\). For an increasing homeomorphism \(\lambda\), put \(\epsilon=\|\lambda-\mathrm{id}\|_T\) and \(\delta=\|\rho_1-\rho_2\circ\lambda\|_T\). Compare the two weighted suprema by changing variables \(s'=\lambda(s)\); the two exponential factors differ by at most \(2\beta\epsilon\) because
\[|(\lambda(t)-\lambda(s))-(t-s)|\le2\epsilon.\]
As positive obstacles are at most \(B\), we obtain
\[\|m_1-m_2\circ\lambda\|_T\le a,\qquad a:=\delta+2\beta B\epsilon,\]
then \(\|y_1-y_2\circ\lambda\|_T\le\delta+a\).

The regulator estimate requires control of a time-changed integral. Every memory path \(m\) satisfies \(0\le m\le B\), and, because \(dm=-\beta m\,dt+d\eta\) as signed measures,
\[\eta(T)=m(T)+\beta\int_0^T m(s)ds\le B(1+\beta T),\quad\operatorname{TV}_{[0,T]}(m)\le B(1+2\beta T).\]
For any càdlàg bounded-variation \(f\) and increasing homeomorphism \(\lambda\), Stieltjes integration by parts yields
\[\left|\int_0^t f(\lambda(s))ds-\int_0^{\lambda(t)}f(u)du\right|\le\epsilon\bigl(\|f\|_T+\operatorname{TV}_{[0,T]}(f)\bigr).\]
Apply this with \(f=m_2\), and split the difference of the two regulator formulas into memory difference, aligned integral difference, and clock distortion:
\[\|\eta_1-\eta_2\circ\lambda\|_T\le a+\beta\bigl(Ta+2B(1+\beta T)\epsilon\bigr)=(1+\beta T)(\delta+4\beta B\epsilon).\]
These estimates hold for each \(\lambda\). Taking the infimum over clock changes gives local Lipschitz continuity of the single-output and paired-output maps in \(J_1\) on every uniformly bounded input class. Since a convergent \(J_1\) sequence is uniformly bounded, both maps are \(J_1\)-continuous on the entire domain.

**4. Failure of global \(J_1\)-Lipschitz control when \(\beta>0\).** Fix \(0<a<b<b+h<T\), with \(h>0\). For amplitude \(H>0\), set \(\rho_H(t)=(1+H)\mathbf1_{[a,b)}(t)\) and \(\widetilde\rho_H(t)=(1+H)\mathbf1_{[a+h,b+h)}(t)\). A piecewise-linear increasing homeomorphism mapping \(a\) to \(a+h\) and \(b\) to \(b+h\) aligns the two input paths exactly with maximal time error \(h\). Thus their \(J_1\) distance is at most \(h\), independent of \(H\).

Reflection holds \(m=H\) while each pulse is present; after its downward jump at the pulse endpoint, memory decays exponentially. Therefore
\[m_{\rho_H}(T)=H e^{-\beta(T-b)},\qquad m_{\widetilde\rho_H}(T)=He^{-\beta(T-b-h)}.\]
At \(T\), both original inputs vanish, and every allowable time change fixes \(T\). The output occupancy \(J_1\)-distance is at least \(H e^{-\beta(T-b)}(e^{\beta h}-1)\), which diverges as \(H\to\infty\). Regulator values differ at \(T\) as well: each pulse causes a jump of \(H\), followed by regulator growth at rate \(\beta H\) until its end, giving \(\eta_{\rho_H}(T)=H[1+\beta(b-a)]\), exactly the **same** terminal regulator as the shifted pulse, so this example by itself does NOT prove a global \(J_1\) failure for the regulator. To establish it, instead compare the same rectangular pulse with one stretched from \([a,b)\) to \([a,b+h)\). The inputs can again be aligned by a homeomorphism within \(h\), while their terminal regulators differ by \(\beta Hh\). This proves failure of a global \(J_1\)-Lipschitz constant for the regulator. (For \(\beta=0\), the map commutes with time changes and global bounds hold.)

## Verification
The self-contained standard-library file `verification.py` independently evaluates exponential-memory reflection for right-continuous finite-step inputs using an event recursion and compares its memory with a separately evaluated weighted-supremum formula. It also checks the two sharp uniform-modulus examples and the shifted-pulse occupancy obstruction. The program's finite computations are diagnostic only. The arbitrary-input existence, uniqueness, Lipschitz inequalities and unbounded-amplitude \(J_1\) obstruction are proved analytically above.

## Relationship to prior work
Wang and Chakraborty, arXiv:2610.22607v1 (2026), Definition 3.2 and Theorem 3.5 establish the general Volterra-Skorokhod model; Proposition 3.10 and Proposition 3.13 establish unspecified uniform Lipschitz constants for arbitrary admissible kernels. Remark 3.11 explicitly leaves the \(J_1\) question open. The present theorem resolves it quantitatively for the important exponential-service subclass and gives **sharp** uniform constants; it does not answer the question for all kernels. Reed, Ward, and Zhan (2013), Theorem 2.1, provide a related supremum representation for a generalized drift Skorokhod problem, but that theorem neither states these kernel-reflection constants nor their \(J_1\) boundary. Kruk et al. (2007) treat instantaneous classical reflection, whose time-change equivariance differs from exponential memory. Wang and Chakraborty (2025), arXiv:2511.07650v2, develop queue fluid limits through Volterra equations, not these pathwise sharp bounds. Literature equivalence with a differently formulated reflected-linear-drift estimate is a remaining originality risk.

## Limitations
No general \(J_1\) assertion is made for nonexponential service survival kernels. The negative global \(J_1\) conclusion requires \(\beta>0\) and unbounded input amplitudes; the map is locally Lipschitz on uniformly bounded classes. The two optimal uniform moduli are operator supremums; the regulator constant may be approached only in a vanishing initial waiting-time limit. No stochastic limit theorem is asserted without separate input tightness/convergence hypotheses. The analytical estimates require no further input regularity than the conditions stated above.

## References
1. M. Wang and P. Chakraborty (2026), *Volterra-Skorokhod Reflection and Fluid Limits of Loss Queues*, arXiv:2610.22607v1, submitted 15 October 2026, Sections 3.2--3.3 (especially Remark 3.11).
2. M. Wang and P. Chakraborty (2025), *Fluid Limits for Time-Varying Many-Server Loss Systems via Discontinuous Volterra Equations*, arXiv:2511.07650v2.
3. J. Reed, A. Ward, and D. Zhan (2013), *On the generalized drift Skorokhod problem in one dimension*, Journal of Applied Probability 50, 16--28, Theorem 2.1, doi:10.1239/jap/1363784421.
4. Ł. Kruk, J. Lehoczky, K. Ramanan, and S. Shreve (2007), *An explicit formula for the Skorokhod map on [0,a]*, Annals of Probability 35, 1740--1768, arXiv:0710.2977.
