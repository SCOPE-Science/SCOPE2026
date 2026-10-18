# Critical capture-time crossover for two-interval affine circle maps

## Finding

Consider the Gaivão–Laurent–Nogueira two-interval map on \([0,1)\), with its invariant interval \(J=[c,b)\). A near-identity degeneration of its exterior right branch has an exact microscopic overshoot law and a sharp macroscopic first-entry limit. The two limits describe different aspects of the same first-entry event.

Fix \(0<c<b<1\), \(0<\lambda<1\), and \(1-b<\lambda(1-c)\). Fix a real \(\kappa<(1-\lambda)/(b-c)\). For sufficiently small \(\delta>0\), put
\[
\eta_\delta=c+\delta,\quad s_\delta=1+\kappa\delta,\quad
\mu_\delta=s_\delta/\lambda,\quad a_\delta=b-\lambda(c+\delta),
\]
and define
\[
f_\delta(x)=\begin{cases}
\lambda x+a_\delta,&0\le x<\eta_\delta,\\
s_\delta(x-\eta_\delta)+c,&\eta_\delta\le x<1.
\end{cases}
\]
These parameters lie in the admissible domain of the originating article. Let \(\tau_\delta(x)=\min\{n\ge0:f_\delta^n(x)\in J\}\). Set \(B=b-c\), \(L=1-b\), \(\alpha=1-\kappa B>0\), and \(\Delta_\delta=\delta(\alpha+\kappa\delta)>0\).

**Exact finite-parameter first-entry structure.** For every integer \(n\ge1\), the Lebesgue measure of right-exterior points surviving at least \(n\) iterates is
\[
\operatorname{Leb}\{x\in[b,1):\tau_\delta(x)\ge n\}
=\left[L-\Delta_\delta\sum_{j=1}^{n-1}s_\delta^{-j}\right]_+.
\]
For a uniform initial point in \([b,1)\), define the normalized first-entry undershoot
\[
R_\delta(x)=\frac{b-f_\delta^{\tau_\delta(x)}(x)}{\Delta_\delta}.
\]
Except possibly for the final, truncated first-entry-time cell, the conditional distribution of \(R_\delta\) at each exact entry time is **exactly uniform on \([0,1]\)**. The total-variation distance, conditional on \(x\in[b,1)\), between the joint law of \((\tau_\delta,R_\delta)\) and the product of its discrete time marginal with a uniform \([0,1]\) law is \(O(\delta)\).

**Critical scaling limit.** Define, for \(t\ge0\),
\[
H_\kappa(t)=\begin{cases}
\alpha(1-e^{-\kappa t})/\kappa,&\kappa\ne0,\\
t,&\kappa=0,
\end{cases}
\quad
T_\kappa=\begin{cases}
\kappa^{-1}\log\dfrac{1-\kappa B}{1-\kappa(1-c)},&\kappa\ne0,\\
L,&\kappa=0.
\end{cases}
\]
Both \(H_\kappa\) and \(T_\kappa\) are well-defined, with \(H_\kappa(T_\kappa)=L\). If \(U\) is uniform on \([0,1)\), then
\[
\delta\tau_\delta(U)\ \Longrightarrow\ \nu_\kappa
=b\,\delta_0+\alpha e^{-\kappa t}\mathbf1_{(0,T_\kappa)}(t)\,dt.
\]
In particular, the rescaled positive first-entry times have a truncated increasing exponential density for \(\kappa<0\), a uniform density for \(\kappa=0\), and a truncated decreasing exponential density for \(\kappa>0\). The remaining mass \(b\) is an atom at zero. Conditional on starting in \([b,1)\), the rescaled first-entry time and \(R_\delta\) converge jointly to **independent** random variables, the first with density \(\alpha e^{-\kappa t}/L\) on \((0,T_\kappa)\) and the second uniform on \([0,1]\).

More strongly, there are finite positive constants \(C\) and \(\delta_0\), depending only on the fixed parameters, such that for \(0<\delta<\delta_0\),
\[
c\delta\ \le\ W_1\bigl(\mathcal L(\delta\tau_\delta(U)),\nu_\kappa\bigr)\ \le\ C\delta.
\]
Thus the order of the Wasserstein convergence rate is sharp when \(c>0\).

## Assumptions and scope

The branch break \(\eta_\delta\) is strictly inside \(J\), and all maps are considered on the half-open interval \([0,1)\). The parameter condition \(1-b<\lambda(1-c)\) permits both contracting and expanding perturbations \(s_\delta\) about one. The strict condition on \(\kappa\) ensures admissible disjoint branch images within \(J\) and transverse first entry from the right. All limits hold for fixed \(b,c,\lambda,\kappa\) as \(\delta\downarrow0\). The probability statements use normalized Lebesgue measure on the initial domain specified in each statement.

The first public version of the originating map is arXiv:2212.10944, dated 2022-12-21, with primary dynamical classification 37E05.

## Proof

**1. Admissibility and trapping.** The originating parameter conditions require \(0<\lambda<1\), \(\mu>0\), \(0\le c<b\le1\), a branch break in \((c,b)\), the disjoint-image inequality \(f(c)>f(b)\), and the stated endpoint constraint when the second slope exceeds one. For the parameters here, \(\eta_\delta=c+\delta\in(c,b)\), while
\[
f_\delta(c)-f_\delta(b)
=\delta\bigl[(1-\lambda)-\kappa(b-c)+\kappa\delta\bigr]>0.
\]
If \(\kappa>0\), the remaining parameter restriction \(\mu_\delta(1-b)\le1-c\) holds for all sufficiently small \(\delta\) because \(1-b<\lambda(1-c)\). For \(\kappa\le0\), \(s_\delta\le1\) handles the alternative condition. The originating map therefore sends \([0,1)\) into itself and \(J\) into itself. More directly, \(f_\delta([0,c))\subset[0,b)\), \(f_\delta([b,1))\subset[c,1)\), and neither exterior component can jump across \(J\) during its first entry.

For \(x<c\), the iterates before entry follow \(x\mapsto\lambda x+a_\delta\), with attracting affine fixed point \(a_\delta/(1-\lambda)\to c+(b-c)/(1-\lambda)>c\). Hence every left-exterior orbit enters \(J\) within a number of steps bounded uniformly in \(x\) and sufficiently small \(\delta\).

**2. Exact right-exterior cells.** Write \(x=b+u\), with \(0\le u<L\). Until first entry, the exact recurrence is
\[
u_{m+1}=s_\delta u_m-\Delta_\delta,\qquad
\Delta_\delta=b-f_\delta(b)=(1-s_\delta)(b-c)+s_\delta\delta
=\delta(\alpha+\kappa\delta).
\]
For \(n\ge1\), set
\[
h_{\delta,n}=\Delta_\delta\sum_{j=1}^{n-1}s_\delta^{-j},\qquad h_{\delta,1}=0.
\]
As \(s_\delta>0\), \(u_m\ge0\) for every \(m<n\) precisely when \(u\ge h_{\delta,n}\). Thus \(\tau_\delta=n\) on \([h_{\delta,n},h_{\delta,n+1})\cap[0,L)\), proving the survivor-measure identity. On a complete cell, whose length is \(w_{\delta,n}=\Delta_\delta s_\delta^{-n}\), direct substitution gives
\[
R_\delta(b+u)=1-\frac{u-h_{\delta,n}}{w_{\delta,n}}.
\]
Uniform initial position therefore gives exactly uniform undershoot on every complete cell. Since \(h_{\delta,n}\) is strictly increasing and eventually exceeds \(L\), there is at most one truncated terminal cell. The width of any cell is \(O(\delta)\) uniformly over the possible entry times (by Step 3). Its conditional probability is \(O(\delta)\), proving the total-variation product bound.

**3. Uniform limiting entrance profile.** The Riemann-sum expansion \(\log s_\delta=\kappa\delta+O(\delta^2)\) gives, uniformly whenever \(n\delta\) remains in a fixed compact interval,
\[
h_{\delta,n}=H_\kappa((n-1)\delta)+O(\delta).
\]
The hypotheses imply \(\alpha-\kappa L=1-\kappa(1-c)>0\), so \(H_\kappa\) increases strictly through \(L\) at the finite time \(T_\kappa\). It follows that all right-exterior entry times are at most \((T_\kappa+1)/\delta\) for small \(\delta\). Since \(H_\kappa'(t)=\alpha e^{-\kappa t}\) has a positive lower bound on this compact time interval, inversion of the adjacent cell thresholds yields
\[
\sup_{0\le u<L}\left|\delta\tau_\delta(b+u)-H_\kappa^{-1}(u)\right|\le C_1\delta.
\]
Here \(H_\kappa^{-1}(u)=-\kappa^{-1}\log(1-\kappa u/\alpha)\) for \(\kappa\ne0\), and equals \(u\) for \(\kappa=0\). With the uniform left-exterior bound of Step 1 and \(\tau_\delta=0\) on \(J\), this proves a deterministic \(O(\delta)\) coupling to the limit \(T(U)\), which is zero for \(U<b\) and \(H_\kappa^{-1}(U-b)\) for \(U\ge b\).

**4. Law and optimal rate.** Under uniform \(U\), \(T(U)=0\) with probability \(b\). On the remaining interval, the change of variables \(u=H_\kappa(t)\) yields density \(H_\kappa'(t)=\alpha e^{-\kappa t}\), supported on \((0,T_\kappa)\), of total mass \(L\). The deterministic coupling proves the \(W_1\) upper bound. For \(0\le t<\delta\), the prelimit scaled time has cumulative distribution \(b-c\), because its only mass below \(\delta\) is the initial mass in \(J\). The limiting cumulative distribution is at least \(b\) throughout that interval. The one-dimensional integral formula \(W_1=\int|F-G|\) therefore gives the lower bound \(c\delta\).

**5. Joint limit.** For right-exterior initial positions, all except a set of conditional probability \(O(\delta)\) lie in complete cells, on each of which the undershoot is uniform independently of the integer cell label. Consequently the total-variation dependence bound of Step 2 holds. Combining it with convergence of the discrete scaled time marginal to its absolutely continuous limit proves the claimed weak product limit. No total-variation convergence to the continuous-time law is asserted or possible for the discrete time variable.

## Verification

A standalone Python 3 standard-library checker is supplied as `capture_verify.py`. It reconstructs admissible rational parameter choices, verifies the exact preimage thresholds against iterated rational trajectories, checks the uniform-undershoot affine identity at rational fractions of complete cells, and tests finite-parameter approximations to the limiting profile and affine slow flow. The checker outputs `ALL_CHECKS_OK` when these finite assertions pass. These finite tests are not a proof of the limits; Steps 1–5 give the analytical proof.

## Relationship to prior work

Gaivão, Laurent, and Nogueira establish the invariant interval \(J=[c,b)\), eventual entrance of every orbit (Lemma 4.1), rotation numbers, and the conjugate dynamics on \(J\) (Theorems 5.2 and 5.5 and Section 6). The present result retains their map and adds the **full finite first-entry cell geometry and the two-scale limiting capture-and-undershoot law**, which concern the exterior portions discarded by conjugation to \(J\). The earlier Laurent–Nogueira model already lives on the normalized trapping interval, so its rotation-number description does not specify this exterior law. Related work on piecewise increasing contractions emphasizes long-time attractors and periodic cycles, not the particular first-entry distribution here.

## Limitations

The limit fixes \(\kappa\) and the other geometric parameters; it does not give uniform estimates as \(\kappa\) approaches its admissible boundary or as \(c\downarrow0\). The initial distribution is uniform Lebesgue, and the exact uniform undershoot applies to complete right-entry cells (not to an arbitrary nonuniform initial density or the final truncated cell). The scaled time converges weakly and in \(W_1\), not in total variation to its continuous component. This theorem does not classify invariant measures or rotation numbers inside \(J\), already addressed by prior work. An independently published equivalent critical entrance law has not been ruled out conclusively.

## References

1. J. P. Gaivão, M. Laurent, and A. Nogueira, *Rotation number of 2-interval piecewise affine maps*, arXiv:2212.10944 (first public version 2022-12-21); *Aequationes Mathematicae* 99 (2025), 511–530, DOI: 10.1007/s00010-024-01064-2. Open full text: https://link.springer.com/article/10.1007/s00010-024-01064-2.
2. M. Laurent and A. Nogueira, *Dynamics of 2-interval piecewise affine maps and Hecke–Mahler series*, *Journal of Modern Dynamics* 17 (2021), 33–63, DOI: 10.3934/jmd.2021002; arXiv:1907.08655.
3. J. P. Gaivão and A. Nogueira, *Dynamics of piecewise increasing contractions*, *Bulletin of the London Mathematical Society* 54 (2022), 482–500, DOI: 10.1112/blms.12577.
