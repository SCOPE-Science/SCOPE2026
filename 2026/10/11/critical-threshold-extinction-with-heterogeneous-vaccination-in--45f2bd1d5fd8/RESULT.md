# Critical-threshold extinction with heterogeneous vaccination in multi-group SAIRS dynamics

## Finding

**Theorem.** For the model and assumptions below, at the exact threshold \(\mathcal R_0=1\), the unique disease-free equilibrium is globally asymptotically stable on the full invariant nonnegative population simplex, even for independent, nonzero vaccination rates in every group. Combining this endpoint with the strict-subcritical stability and supercritical instability established for this same model in [1] gives the sharp criterion \(\mathcal R_0\le1\) for global asymptotic stability of the disease-free equilibrium under the stated transmission assumptions.

The new assertion is the **vaccinated equality case**. The strict-subcritical and supercritical statements are background results of [1], not claimed here as new.

## Assumptions and scope

Fix an integer \(n\ge1\). For each group index \(i=1,\ldots,n\), let \(S_i,A_i,I_i,R_i\) denote susceptible, asymptomatically infectious, symptomatically infectious, and removed fractions. Suppose \(\mu_i>0\), \(\nu_i\ge0\), \(\alpha>0\), \(\delta_A>0\), \(\delta_I>0\), and \(\gamma\ge0\). Let \(B_A=(\beta^A_{ij})\) and \(B_I=(\beta^I_{ij})\) be nonnegative irreducible matrices with strictly positive diagonal entries. The force of infection is

\[
 f_i=\sum_{j=1}^n(\beta^A_{ij}A_j+\beta^I_{ij}I_j).
\]

The autonomous system is

\[
\begin{aligned}
\dot S_i&=\mu_i-S_if_i-(\mu_i+\nu_i)S_i+\gamma R_i,\\
\dot A_i&=S_if_i-(\alpha+\delta_A+\mu_i)A_i,\\
\dot I_i&=\alpha A_i-(\delta_I+\mu_i)I_i,\\
\dot R_i&=\delta_AA_i+\delta_II_i+\nu_iS_i-(\gamma+\mu_i)R_i.
\end{aligned}
\]

Initial data range over the complete nonnegative invariant phase space

\[
\Gamma=\{(S,A,I,R)\in\mathbb R_{\ge0}^{4n}:S_i+A_i+I_i+R_i=1\ \text{for all }i\}.
\]

The disease-free equilibrium has \(A_i=I_i=0\), \(S_i=s_i=(\mu_i+\gamma)/(\mu_i+\nu_i+\gamma)\), and \(R_i=1-s_i\). All \(s_i>0\). Write \(D_s=\operatorname{diag}(s_i)\), \(D_A=\operatorname{diag}(\alpha+\delta_A+\mu_i)\), and \(D_I=\operatorname{diag}(\delta_I+\mu_i)\), and define

\[
K=\bigl(D_sB_A+\alpha D_sB_I D_I^{-1}\bigr)D_A^{-1},\qquad \mathcal R_0=\rho(K).
\]

This definition is the nonzero spectral block of the usual next-generation matrix. Irreducibility and positivity imply \(K\) is irreducible with positive Perron left eigenvector at \(\rho(K)=1\).

## Proof

First, \(\Gamma\) is compact, forward invariant and positively complete. At each coordinate-zero boundary the corresponding derivative is nonnegative; direct summation gives \(\frac{d}{dt}(S_i+A_i+I_i+R_i)=\mu_i[1-(S_i+A_i+I_i+R_i)]\).

Assume \(\rho(K)=1\). Choose \(p_i>0\) such that \(p^{\mathsf T}K=p^{\mathsf T}\), and set

\[
 q^{\mathsf T}=p^{\mathsf T}D_sB_I D_I^{-1}>0.
\]

Multiplying the Perron identity by \(D_A\) yields the **exact cancellation equations**

\[
 p^{\mathsf T}(D_sB_A-D_A)+\alpha q^{\mathsf T}=0,
\quad p^{\mathsf T}D_sB_I-q^{\mathsf T}D_I=0.
\]

Consequently the weighted infection mass \(W=\sum_i(p_iA_i+q_iI_i)\) obeys

\[
\dot W=\sum_{i=1}^n p_i(S_i-s_i)f_i.
\tag{1}
\]

Set \(e_i=S_i-s_i\) and \(\kappa_i=\mu_i+\nu_i+\gamma>0\). The population identity eliminates \(R_i\) from the susceptible equation, giving

\[
 \dot e_i=-\kappa_i e_i-S_if_i-\gamma(A_i+I_i).
\tag{2}
\]

The additional susceptible *positive-excess* term

\[
 H=\sum_{i=1}^n p_i(e_i)_+,
 \qquad (u)_+=\max\{u,0\},
\]

makes \(\mathcal V=W+H\) nonnegative and locally Lipschitz throughout \(\Gamma\). At \(e_i=0\), equation (2) has \(\dot e_i\le0\); therefore the upper right derivative of \((e_i)_+\) is zero there. Using (1)-(2) in the remaining cases gives, along every forward solution and at every differentiability time,

\[
\boxed{\displaystyle
\dot{\mathcal V}=
\sum_{i:e_i<0}p_ie_if_i
-\sum_{i:e_i>0}p_i\bigl(s_if_i+\kappa_i e_i+\gamma(A_i+I_i)\bigr)\le0 .}
\tag{3}
\]

The same sign inequality holds for the upper right Dini derivative at switching instants, so \(\mathcal V\) is nonincreasing.

Consider a compact omega-limit orbit on which \(\mathcal V\) is constant. If any \(e_i>0\), equation (3) is strictly negative, impossible. If \(e_i<0\) and \(f_i>0\) for some index, it is also strictly negative. Suppose instead any infection persists at a point of this orbit. Because both transmission matrices have positive diagonal entries, there is an index \(j\) with \(f_j>0\). Constancy therefore forces \(e_j=0\). But (2) gives \(\dot e_j=-s_jf_j-\gamma(A_j+I_j)<0\), so for a short positive time \(e_j<0\) while \(f_j>0\) remains true by continuity. Equation (3) is then strictly negative, a contradiction. Thus every omega-limit point satisfies \(A_i=I_i=0\) for all groups.

It follows from compactness that every \(A_i(t),I_i(t)\to0\) and hence every \(f_i(t)\to0\). Variation of constants in (2) then yields \(e_i(t)\to0\); the conservation relation yields \(R_i(t)\to1-s_i\). This proves global attraction. For Lyapunov stability, \(W(t)\le\mathcal V(t)\le\mathcal V(0)\) controls every infected coordinate uniformly because \(p_i,q_i>0\). Equation (2), \(S_i\le1\), and \(f_i\le C\sum_j(A_j+I_j)\) bound \(\sup_{t\ge0}|e_i(t)|\) by \(|e_i(0)|+C'\mathcal V(0)\). Since \(\mathcal V(0)\) tends to zero with the initial distance to the disease-free state, all group coordinates stay uniformly close to that equilibrium. This establishes Lyapunov stability and concludes global asymptotic stability.

## Verification

The proof is valid for **all** \(n\ge1\) under the stated hypotheses. The standalone script `check_threshold.py` checks the Perron cancellations, the two sign branches of (3), and a rational two-group critical example without floating-point approximation; run `python3 check_threshold.py` from a directory containing that script. Its finite checks support arithmetic reproducibility but are not used as a substitute for the preceding all-dimensional proof.

For the illustrative parameter choice \(n=2\), \(\mu_i=\nu_i=\gamma=\alpha=\delta_A=\delta_I=1\), and \(B_A=B_I=\begin{pmatrix}2&1\\1&2\end{pmatrix}\), the threshold satisfies \(\rho(K)=1\), and \(p=q=(1,1)\) gives equation (3) exactly. This numerical specialization is not an assumption in the theorem.

## Relationship to prior work

Ottaviano, Sensi and Sottile [1] establish global asymptotic stability for vaccinated groups when \(\mathcal R_0<1\) and establish the critical equality only for **unvaccinated** groups. Their proof at equality relies on a nonnegative susceptible deficit which need not hold with vaccination: an initial state may have \(S_i>s_i\). The positive-excess term in (3) compensates for precisely that deficiency, without assuming identical vaccination rates or a reduced group count.

The general multistage extinction theorem of Guo, Li and Shuai [2] treats a **single susceptible variable** with an incidence dominance assumption relative to the disease-free susceptible state. It does not directly imply the present theorem for independently varying \(S_i\) with their allowed initial excess. Li and Zhang [3] study a different network epidemic structure with an additional exposed stage and particular mixing constraints, rather than the full arbitrary contact matrices and waning immunity here. The matrix-weighted infected mass is related to the classical Perron-vector Lyapunov method [4]; the crucial correction here is the susceptible positive-excess term.

## Limitations

No exact decay rate at the nonhyperbolic threshold is proved. No claim about endemic equilibria or stability above the threshold is new. The result assumes irreducible, nonnegative transmission matrices with strictly positive diagonals and fixed population fractions by group. Other population exchange structures, treatment delays, stochastic dynamics, and state-dependent vaccination are outside the theorem. A related 2018 multi-group SEIRS vaccination paper [5] was accessible only at the abstract level; its distinct exposed-versus-infectious compartment architecture makes direct coverage unclear rather than definitively excluded. The analytic argument above is self-contained; independent external validation has not been performed.

## References

[1] S. Ottaviano, M. Sensi, S. Sottile, *Global stability of multi-group SAIRS epidemic models*, arXiv:2202.02993 (public version dated 7 February 2022); Math. Methods Appl. Sci. (2023), doi:10.1002/mma.9303. https://arxiv.org/abs/2202.02993

[2] H. Guo, M. Y. Li, Z. Shuai, *Global dynamics of a general class of multistage models for infectious diseases*, SIAM J. Appl. Math. 72 (2012), 261–279, doi:10.1137/110827028. https://sites.ualberta.ca/~myli/research/ps_files/multistage_2012.pdf

[3] E. Li, Q. Zhang, *Global dynamics of an endemic disease model with vaccination: Analysis of the asymptomatic and symptomatic groups in complex networks*, Electron. Res. Arch. 31 (2023), 6481–6504, doi:10.3934/era.2023328. https://doi.org/10.3934/era.2023328

[4] Z. Shuai, P. van den Driessche, *Global Stability of Infectious Disease Models Using Lyapunov Functions*, SIAM J. Appl. Math. 73 (2013), 1513–1532, doi:10.1137/120876642. https://doi.org/10.1137/120876642

[5] D. Fan, P. Hao, D. Sun, J. Wei, *Global stability of multi-group SEIRS epidemic models with vaccination*, Int. J. Biomath. 11 (2018), 1850006, doi:10.1142/S1793524518500067. https://doi.org/10.1142/S1793524518500067
