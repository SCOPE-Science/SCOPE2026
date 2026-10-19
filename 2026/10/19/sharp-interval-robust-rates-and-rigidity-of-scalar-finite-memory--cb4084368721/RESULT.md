# Sharp interval-robust rates and rigidity of scalar finite-memory feedback

## Finding

Consider the discrete-time scalar plants with uncertain but time-invariant drift \(a\in[c-t,c+t]\), where \(c\in\mathbb R\) and \(t>0\). The same finite-memory state-feedback coefficients must be used for every plant. For feedback length \(H\geq1\), define the smallest possible *worst-case closed-loop spectral radius* as

\[
\mathcal R_H(c,t)=\inf_{k\in\mathbb R^H}\ \max_{a\in[c-t,c+t]}\rho(T_H(a,k)).
\]

Then the exact minimax value, for every finite memory length, is

\[
\boxed{\mathcal R_1(c,t)=t,\qquad \mathcal R_H(c,t)=t/2\quad(H\geq2).}
\]

The optimizer is **unique** in each class: for \(H=1\), it is \(k_0=-c\); for every \(H\geq2\), it is

\[
\boxed{k_0=-c,\quad k_1=-t^2/4,\quad k_j=0\ (2\leq j<H).}
\]

Thus one past-state tap halves the exact interval-worst spectral rate; no additional finite memory can improve it. A common Schur-stabilizing controller exists for all drifts in the *entire closed interval* exactly when \(t<1\) in the static class or \(t<2\) in any class with at least one past-state tap. These strict criteria correspond to interval widths below \(2\) and \(4\), respectively.

## Assumptions and scope

For each fixed real \(a\), the controlled scalar system is

\[
x_{n+1}=a x_n+u_n,\qquad u_n=\sum_{j=0}^{H-1}k_j x_{n-j}.
\]

The gain vector \(k=(k_0,\ldots,k_{H-1})\in\mathbb R^H\) is fixed, independent of both \(a\) and time; the unknown drift is fixed along each trajectory and ranges over the entire interval, not just its endpoints. The \(H\)-state companion matrix \(T_H(a,k)\) is the standard shift realization of the history vector. Its monic characteristic polynomial is

\[
p_a(z)=z^H-(a+k_0)z^{H-1}-\sum_{j=1}^{H-1}k_j z^{H-1-j}.
\]

The quantity \(\rho\) is the maximum modulus of the polynomial zeros. No positivity, small-uncertainty, or initial-stability hypothesis is imposed. The optional addition of square-integrable additive disturbance does not change the Schur-stability criterion, although it changes stationary costs; no optimal-LQR-cost or policy-gradient guarantee is claimed.

The degenerate case \(t=0\) is excluded from the proof for the conformal map but has minimax value zero for every \(H\), attained by exact static pole cancellation.

## Proof

**1. Static feedback.** If \(H=1\), the only pole is \(a+k_0\). For real gains,

\[
\max_{a\in[c-t,c+t]}|a+k_0|=t+|c+k_0|.
\]

It follows that \(\mathcal R_1=t\), attained only when \(k_0=-c\).

**2. A two-tap upper bound for all larger memory lengths.** Set \(k_0=-c\), \(k_1=-t^2/4\), and all remaining coefficients to zero. For \(H\geq2\),

\[
p_a(z)=z^{H-2}\left(z^2-(a-c)z+t^2/4\right).
\]

Since \(|a-c|\leq t\), the quadratic discriminant \((a-c)^2-t^2\) is nonpositive. The roots are complex conjugates of common modulus \(t/2\) in the interior, and coincident real roots of modulus \(t/2\) at the two endpoints. The additional \(H-2\) roots are zero. Hence \(\rho(T_H(a,k))=t/2\) for **every** allowed drift, showing \(\mathcal R_H\leq t/2\).

**3. Lower bound for arbitrary finite memory.** Fix any \(H\geq1\) and any gains. Introduce the Laurent polynomial

\[
L(z)=z-\sum_{j=0}^{H-1}k_jz^{-j},\qquad p_a(z)=z^{H-1}(L(z)-a)\quad(z\ne0).
\]

Write \(r=\max_{a\in[c-t,c+t]}\rho(T_H(a,k))\). Suppose for contradiction that \(r<t/2\), and choose any \(R\) satisfying \(r<R<t/2\). No polynomial \(p_a\), with \(a\) in the interval, has a zero with \(|z|\geq R\). Therefore \(L(z)\) avoids the whole slit \([c-t,c+t]\) whenever \(|z|\geq R\).

The classical Joukowski inverse

\[
\Phi(w)=\frac{w-c+\sqrt{(w-c)^2-t^2}}{t},
\]

where the analytic square-root branch satisfies \(\sqrt{(w-c)^2-t^2}\sim w-c\) at infinity, maps \(\mathbb C\setminus[c-t,c+t]\) conformally onto \(\{\xi:|\xi|>1\}\). Consider

\[
g(\zeta)=\frac{1}{\Phi(L(R/\zeta))},\qquad |\zeta|<1.
\]

Because \(L(R/\zeta)\) avoids the slit, this is holomorphic away from \(\zeta=0\), has modulus strictly below one, and extends holomorphically across zero. The asymptotics \(L(z)=z+O(1)\) and \(\Phi(w)=2(w-c)/t+O(w^{-1})\) give

\[
g(0)=0,\qquad g'(0)=\frac{t}{2R}>1.
\]

Schwarz's lemma contradicts this derivative. Thus every fixed finite-memory controller satisfies \(r\geq t/2\). Together with step 2, this proves the sharp value for \(H\geq2\).

**4. Rigidity of the optimum.** Suppose a controller of length \(H\geq2\) actually attains \(r=t/2\). The same argument defines \(g\) on the open disk with \(R=t/2\), because all roots are of modulus at most \(R\); its derivative at zero is exactly one. The equality case of Schwarz's lemma forces \(g(\zeta)=\zeta\). Hence, for \(|z|>R\),

\[
\Phi(L(z))=\frac{2z}{t},\qquad
L(z)=c+\frac t2\left(\frac{2z}{t}+\frac{t}{2z}\right)=c+z+\frac{t^2}{4z}.
\]

Comparison with the Laurent expansion defining \(L\) forces \(k_0=-c\), \(k_1=-t^2/4\), and every later coefficient to vanish. The minimax optimizer is therefore unique for every \(H\geq2\). The unique static optimizer was established in step 1.

**5. Strict stabilization threshold.** All companion eigenvalues have modulus strictly below one if and only if each plant is Schur stable. By the exact minimax values and their attainment, simultaneous Schur stabilization for the complete interval holds if and only if \(t<1\) for \(H=1\) or \(t<2\) for \(H\geq2\). At equality the constructed worst-case endpoints possess roots on the unit circle; the lower bound precludes any different strictly stable controller.

## Verification

The accompanying `verify.py` (Python 3 and NumPy) checks companion eigenvalues on multiple interval grids, exact-rational quadratic discriminants and polynomial coefficients, and the Joukowski inverse identity. Run it from the package directory using `python verify.py`; successful execution prints a PASS line and a deterministic check count. The program is supplementary: the lower bound and uniqueness are infinite-family assertions proved by the Schwarz-lemma argument, not established by sampling.

For example, for \(c=0\), \(t=1.1\), every static controller has worst-case pole modulus at least \(1.1\); the two-tap controller \((k_0,k_1)=(0,-0.3025)\) has worst-case modulus exactly \(0.55\) for every drift in \([-1.1,1.1]\).

## Relationship to prior work

Fujinami, Lee, Tsiamis, Matni and Pappas (2026), Section II, motivate finite impulse response state-feedback by an explicit two-plant scalar example with drifts \(\pm1.1\) that cannot be simultaneously stabilized statically but can with one lag. They study policy-gradient convergence and a memory-expansion curriculum under heterogeneity hypotheses; the complete-interval minimax spectral radius, rigidity across every feedback length, and exact interval-width threshold are not statements of their analysis.

Classical robust Schur-stability theory for interval plants (Katbab--Jury, 1990) offers general coefficient-family stability criteria and is directly relevant background. Its accessible abstract does not resolve whether it contains the present specialized exact minimax formula; the full paper was not accessible for a decisive comparison. Likewise, broader simultaneous-stabilization and fixed-order Schur-stability theory study related problems but do not, in the materials inspected, supply this explicit scalar feedback-memory rigidity statement. The Joukowski map and Schwarz lemma are standard complex-analysis tools, not claimed as new.

## Limitations

This is a **spectral-radius** minimax theorem for a *fixed, real, scalar, unit-input-gain, finite-tap state-feedback law* and a drift fixed within each trajectory. It does not cover arbitrary switching of the drift at successive steps, uncertain input gains, general rational dynamic controllers with internal feedback states, multidimensional plants, nonstationary policies, finite-sample randomization alone, or optimization of LQR cost. At the interval endpoints the optimal quadratic may have a repeated root: although the spectral radius is exactly \(t/2\), a uniform bound with pure factor \((t/2)^n\) and no polynomial prefactor is not asserted. For \(t<2\), any slightly larger exponential factor below one is possible uniformly for the fixed compact uncertainty family.

The literature comparison is subject to a genuine residual risk from inaccessible full text in classical interval Schur-stability work and from equivalent formulations in complex-analytic simultaneous-stabilization theory. The available bibliographic comparison is not exhaustive.

## References

1. T. Fujinami, B. D. Lee, A. Tsiamis, N. Matni and G. J. Pappas, *Policy Gradient over History-Dependent Policy Classes for LQR with Domain Randomization*, arXiv:2609.16300v1, first public 2026-09-14. https://arxiv.org/abs/2609.16300
2. A. Katbab and E. I. Jury, *Robust Schur-stability of control systems with interval plants*, International Journal of Control 51 (1990), 1343–1352, https://doi.org/10.1080/00207179008934138.
3. C. Fonte, *Conditions for the Simultaneous Stabilizability of a Segment of Systems*, American Control Conference (2008), https://skoge.folk.ntnu.no/prost/proceedings/acc08/data/papers/0199.pdf.
4. T. Büyükköroğlu, *Fixed Order Controller for Schur Stability*, Mathematical and Computational Applications 21 (2016), Article 25, https://doi.org/10.3390/mca21020025.
