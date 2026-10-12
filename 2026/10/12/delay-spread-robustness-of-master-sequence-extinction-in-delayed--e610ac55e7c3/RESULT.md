# Delay-spread robustness of master-sequence extinction in delayed quasispecies

## Finding

**Theorem (a delay-dispersion extinction criterion).** Fix any integer \(N\geq2\). In the constant-population quasispecies delay system defined below, suppose there is no mutation back into class \(0\), that the mutant classes are never less fit than class \(0\), and that the master self-copying probability has an upper bound \(0<q<1\). Let the replication delays range between \(a\) and \(b\), with \(0<a\leq b<\infty\). If
\[
q<\exp[-NM(b-a)],
\]
where \(M\) is a uniform upper bound on all replication rates, then **every nonnegative unit-simplex history generates a global solution whose master fraction decays exponentially**. More precisely, put \(c=\exp[-NM(b-a)]\), let \(m>0\) be a uniform lower bound on the master replication rate, and let \(\lambda>0\) be the unique solution of
\[
\lambda=m\bigl(c-q\exp(\lambda b)\bigr).
\]
Then, for all \(t\geq b\),
\[
0\leq x_0(t)\leq K\exp[-\lambda(t-b)],\qquad
K=\max_{0\leq s\leq b}\bigl\{x_0(s)\exp[\lambda(s-b)]\bigr\}.
\]
In particular, the system admits no entire, strictly positive periodic orbit, even if its coefficients and individual delays vary periodically. **Only the delay spread, rather than the common delay magnitude, enters the sufficient condition for extinction**; the common delay length still affects the exponential rate.

An explicit three-genotype example has three distinct replication delays exceeding \(100\), a delay spread of \(1/10\), seasonal fitness, and strictly one-way mutation. It satisfies the criterion and therefore exhibits extinction of the master fraction for every normalized nonnegative history. This example is beyond an equal-delay extinction hypothesis.

## Assumptions and scope

Let \(i,j\in\{0,1,\ldots,N-1\}\). For \(t\geq0\), consider
\[
\dot x_i(t)=\sum_{j=0}^{N-1}Q_{ji}(t)f_j(t)x_j(t-\tau_j(t))-x_i(t)\Phi(t),
\qquad
\Phi(t)=\sum_{j=0}^{N-1}f_j(t)x_j(t-\tau_j(t)).
\]
For every \(t\), the mutation matrix \(Q(t)\) is entrywise nonnegative and row-stochastic, \(\sum_iQ_{ji}(t)=1\). Each coefficient and delay is continuous; \(a\leq\tau_j(t)\leq b\) with \(a>0\); \(0<m\leq f_0(t)\leq f_j(t)\leq M\) for every class \(j\). There is no backward mutation into the master: \(Q_{j0}(t)=0\) whenever \(j\geq1\), and \(0\leq Q_{00}(t)\leq q<1\). Histories \(x_j(s)\) on \([-b,0]\) are continuous, nonnegative, and satisfy \(\sum_jx_j(s)=1\) for **each** history time \(s\). The conclusion is uniform across these histories, but the prefactor \(K\) depends on the realized solution over its first \(b\) units of time.

The criterion is sufficient, not asserted necessary or optimal. It is a statement about genotype **fractions** and not absolute population sizes. The continuous nonautonomous delay system need not admit any time-periodic coefficients.

## Proof

**1. Positive invariance and boundedness.** Summing the evolution equations gives, for \(S(t)=\sum_i x_i(t)\), the exact identity
\[
\dot S(t)=\Phi(t)\,[1-S(t)].
\]
As \(S(0)=1\), necessarily \(S(t)=1\). Each coordinate has a nonnegative birth term and a depletion term proportional to itself. Since \(a>0\), the method of steps and variation of constants preserve coordinate nonnegativity, starting from the nonnegative history, for all future times. Hence \(0\leq x_j(t)\leq1\) and the solution continues globally. Delayed coordinates also belong to \([0,1]\), so
\[
0\leq\Phi(t)\leq NM,\qquad
\dot x_j(t)\geq-NM x_j(t).
\]

**2. A lower bound on asynchronous delayed population mass.** The last inequality and integration imply, for \(u\geq v\geq0\),
\[
x_j(u)\geq x_j(v)\exp[-NM(u-v)].
\]
Set \(\Delta=b-a\) and \(c=\exp[-NM\Delta]\). For any \(t\geq b\), take \(u=t-\tau_j(t)\) and \(v=t-b\). Both times are nonnegative and \(0\leq u-v\leq\Delta\), whence
\[
x_j(t-\tau_j(t))\geq c\,x_j(t-b).
\]
Summing across the **different** delayed sampling times, and using normalization at the common time \(t-b\), gives the structural estimate
\[
\sum_{j=0}^{N-1}x_j(t-\tau_j(t))\geq c\sum_{j=0}^{N-1}x_j(t-b)=c.
\]
Therefore the fitness order implies
\[
\Phi(t)\geq f_0(t)\sum_j x_j(t-\tau_j(t))\geq c f_0(t).
\]
The distinction between separate delayed times and one common delayed time is the reason a mere direct application of the equal-delay normalization identity does not work.

**3. Scalar comparison and exponential decay.** Absence of backward mutation yields the exact master equation \(\dot x_0=f_0Q_{00}x_0(t-\tau_0)-\Phi x_0\), so for \(t\geq b\),
\[
\dot x_0(t)\leq f_0(t)\{q x_0(t-\tau_0(t))-c x_0(t)\}.
\]
Because \(0<q<c\) and \(b>0\), the continuous strictly decreasing function \(g(z)=m[c-q\exp(zb)]-z\) satisfies \(g(0)>0\), \(g(z)\to-\infty\), and has exactly one positive zero \(\lambda\). The function \(y(t)=K\exp[-\lambda(t-b)]\) dominates \(x_0\) on \([0,b]\). For every \(t\geq b\),
\[
\begin{aligned}
f_0(t)\{q y(t-\tau_0(t))-c y(t)\}
&=f_0(t)\{q\exp[\lambda\tau_0(t)]-c\}y(t)\\
&\leq f_0(t)\{q\exp(\lambda b)-c\}y(t)\\
&=-\frac{f_0(t)\lambda}{m}y(t)
\leq-\lambda y(t)=\dot y(t).
\end{aligned}
\]
The scalar retarded comparison principle applies because the delayed coefficient \(qf_0(t)\) is nonnegative: writing the difference \(x_0-y\), the negative-current, positive-delayed linear inequality propagates its nonpositivity from \([0,b]\) by steps of length at least \(a\). Thus \(0\leq x_0(t)\leq y(t)\) for every \(t\geq b\), proving the claim. Every strictly positive periodic master component would stay bounded away from zero, contrary to its exponential decay. \(\square\)

**Exact three-class certificate.** Choose
\[
\begin{gathered}
f_0(t)=1+\tfrac1{10}\sin t,\quad
f_1(t)=\tfrac65+\tfrac1{10}\sin t,\quad
f_2(t)=\tfrac{13}{10}+\tfrac1{10}\sin t,\\
Q=\begin{pmatrix}2/5&3/5&0\\0&1/2&1/2\\0&0&1\end{pmatrix},\qquad
(\tau_0,\tau_1,\tau_2)=(100,\,100+1/25,\,100+1/10).
\end{gathered}
\]
For this model \(N=3\), \(m=9/10\), \(M=7/5\), \(q=2/5\), \(b=1001/10\), and \(\Delta=1/10\). Thus \(NM\Delta=21/50\), and the elementary exponential inequality \(e^{-u}\geq1-u\) gives
\[
c=e^{-21/50}\geq29/50>2/5=q.
\]
All inequalities are exact, and the delays are strictly unequal. The exponential comparison bound applies for every allowable normalized history. This calculation does **not** claim the stated sufficient condition is sharp.

## Verification

The standalone standard-library script `verify.py` checks every rational inequality in the explicit certificate and proves strict applicability of the scalar-root condition through exact rational arithmetic. Execute `python3 verify.py` from the directory containing the script; expected output is `VERIFY_OK`. The analytic proof above establishes the infinite-time result. The script **does not** numerically approximate an infinite trajectory or substitute finite checking for the DDE comparison principle.

The critical mathematical checks are the simplex invariance, coordinatewise depletion bound \(NM\), the common-time lower bound \(c\), strict positivity of \(c-q\), existence and uniqueness of the scalar rate \(\lambda\), and the comparison inequality. The stated bounds require \(a>0\), strictly positive uniform \(m\), and continuous bounded coefficients. No assertion is made at equality \(q=c\).

## Relationship to prior work

Morales, Turner and Zapata (2026) introduce the three-class delayed quasispecies system. Their Theorem 3, as stated in the indexed article's nonexistence/error-threshold section, imposes **equal replication delays** and proves master extinction/no positive periodic solution under one-way mutation and dominated master fitness. The result here has a different logical domain: delays may differ among all classes, be time-dependent, and have arbitrarily large common magnitude, provided the explicit spread bound holds. It also supplies an exponential rate inequality not provided by the source's stated equal-delay conclusion. The article's publisher full-text access was unsuccessful during comparison; thus unindexed auxiliary statements or appendices remain a potential originality risk and are not represented as ruled out.

Turner, Crespo, Sardanyés and Morales (arXiv:2412.10475, 2024) fully analyze the corresponding two-class model, with equal delays in their principal stability theorem in Section 3.1.2. Their main extinction conclusions do not imply a three-class variable-delay spread bound. Morales and Turner (arXiv:2508.12424, 2025) allow variable delays in a generalized model but establish periodic existence results, especially for backward mutation, rather than the three-class master extinction estimate stated here. This theorem does not claim novelty for simplex invariance, scalar positive delay comparisons, or the general biological notion of an error threshold.

## Limitations

The condition \(q<e^{-NM(b-a)}\) is a **conservative sufficient** criterion. It can fail even when extinction holds. The decay rate \(\lambda\) deteriorates as the largest absolute delay increases; hence the theorem does not give a delay-magnitude-uniform convergence rate. There is no claim about frequencies of mutant classes beyond their sum approaching one, about mutations from other classes into the master, about stochastic finite populations, or about empirically calibrated viral replication delays. No comparison with all unpublished work is possible. Full access to the 2026 motivating paper was unavailable, leaving a documented residual literature risk.

## References

1. N. Morales, E. A. Turner and J. L. Zapata, *T-periodic dynamics in a 3D delayed quasispecies model*, Journal of Biological Dynamics 20 (2026), article 2631218; first public online 2026-02-23; DOI: 10.1080/17513758.2026.2631218. Its stated 2020 MSC primary code is 92D25.
2. E. A. Turner, F. Crespo, J. Sardanyés and N. Morales, *Quasispecies dynamics with time lags and periodic fluctuations in replication*, arXiv:2412.10475v1 (2024-12-13), full text, especially Section 3.1.2.
3. N. Morales and E. A. Turner, *Generalized Quasispecies Model with Time Delays and Periodic Fluctuations in Replication*, arXiv:2508.12424v1 (2025-08-17), full text, especially Sections 2–4.
