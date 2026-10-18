# Complete four-leader phase diagram on unequal complete bipartite networks

## Finding

Let \(m\ge4\) be an integer. In the unit-conductance graph \(K_{2,m}\), designate exactly four vertices as noisy leaders with the same feedback gain \(\kappa>0\). For the resulting grounded Laplacian \(H_S=L(K_{2,m})+\kappa\operatorname{diag}(\mathbf1_S)\), minimize \(\operatorname{tr}(H_S^{-1})\) over all four-element leader sets \(S\). Write \(i\in\{0,1,2\}\) for the number of chosen vertices in the two-vertex part. The optimum depends only on \(i\), and its **complete global phase classification**, including all ties, is:

| Size of the other part | Optimal \(i\) as gain increases |
|---|---|
| \(4\le m\le6\) | \(0\) for every \(\kappa>0\) |
| \(m=7,8\) | \(2\) for \(0<\kappa<\gamma_m\), then \(0\) for \(\kappa>\gamma_m\) |
| \(m=9,10\) | \(2\) for \(0<\kappa<\gamma_m\), then \(0\) for \(\gamma_m<\kappa<\delta_m\), then \(1\) for \(\kappa>\delta_m\) |
| \(m\ge11\) | \(2\) for \(0<\kappa<\tau_m\), then \(1\) for \(\kappa>\tau_m\) |

At every indicated transition, **exactly the two adjacent values of \(i\) tie**; every four-element leader set with either indicated count is optimal. Away from transitions, precisely the sets with the single stated count are optimal. The transition values are as follows:

\[\begin{aligned}
\gamma_7 &: 13z^3+239z^2+888z-196=0,\\
\gamma_8 &: z^3+26z^2+112z-64=0,\\
\gamma_9 &: z^3+141z^2+800z-972=0,\\
\gamma_{10} &: -z^3+4z^2+72z-200=0,
\end{aligned}\]
where \(\gamma_7,\gamma_8,\gamma_9\) are the unique positive roots of their respective equations and \(\gamma_{10}\) is the **smaller** of two positive roots. Furthermore,
\[\delta_9=\frac{55+\sqrt{2785}}5,\qquad
\delta_{10}=\frac{77+\sqrt{2709}}{23}.\]
For every \(m\ge11\), \(\tau_m\) is the unique positive root of
\[\begin{aligned}
Q_m(z)={}&2z^4+(-m^2+13m-2)z^3\\
&+(-m^3+5m^2+60m-68)z^2\\
&+(-4m^3+36m^2+28m-88)z\\
&-4m^3+20m^2-8m.
\end{aligned}\]
In particular, **only \(m=9\) and \(m=10\) have three distinct optimal leader-count phases** in this complete four-leader family. For \(m=9\), the count undergoes the nonmonotone transition \(2\to0\to1\). Its transition gains are approximately \(1.0275490235\) and \(21.5546198416\).

## Assumptions and scope

There is one undirected edge of conductance one between each vertex of the two-vertex part \(A\) and each vertex of the \(m\)-vertex part \(B\), and no edges within a part. Every vertex has an independent unit-intensity Brownian disturbance. The linear consensus dynamics are \(dX_t=-H_SX_t\,dt+dW_t\). Because \(H_S\) is real symmetric positive definite, its stationary covariance is \(\frac12H_S^{-1}\). We compare \(\operatorname{tr}(H_S^{-1})\); dividing by two gives total stationary variance and leaves the optimizer unchanged. Every gain is finite and strictly positive. Leaders have identical gains; no claim is made about unequal gains, other bipartite part sizes, or variable leader budgets.

## Proof

**1. Exact reduction to three orbits.** Every four-element leader set selects \(i\in\{0,1,2\}\) vertices of \(A\) and \(j=4-i\) vertices of \(B\). Permutations within the two parts are graph automorphisms; thus all such sets have exactly the same objective \(F_i(m,\kappa)\). Write \(z=\kappa\), and define
\[\begin{aligned}
s_A&=\frac{2-i}{m}+\frac{i}{m+z},& t_A&=\frac{2-i}{m^2}+\frac{i}{(m+z)^2},\\
s_B&=\frac{m-j}{2}+\frac{j}{2+z},& t_B&=\frac{m-j}{4}+\frac{j}{(2+z)^2}.
\end{aligned}\]
Block inversion of the diagonal-degree matrix minus the two cross-part rank-one blocks gives
\[\boxed{F_i=s_A+s_B+\frac{s_Bt_A+s_At_B}{1-s_As_B}.}\]
For \(z>0\) and four selected vertices, \(0<s_As_B<1\). This also follows directly from strict positive definiteness: \(x^{\mathsf T}H_Sx=\sum_{uv\in E}(x_u-x_v)^2+z\sum_{u\in S}x_u^2>0\) for every nonzero \(x\). The formula is therefore valid on the entire asserted domain.

**2. Explicit comparison polynomials.** Put
\[\begin{aligned}
P_{20}(m,z)={}&(-m^2+10m-8)z^3+(-m^3+6m^2+48m-48)z^2\\
&+(-4m^3+44m^2+24m-64)z-4m^3+24m^2,\\
P_{01}(m,z)={}&(m^3-7m^2-14m+24)z^2\\
&+(4m^3-52m^2-8m+48)z+4m^3-28m^2-8m,\\
P_{21}(m,z)={}&2z^4+(-m^2+13m-2)z^3\\
&+(-m^3+5m^2+60m-68)z^2\\
&+(-4m^3+36m^2+28m-88)z-4m^3+20m^2-8m.
\end{aligned}\]
Direct substitution in the inverse-trace formula and clearing only strictly positive denominators yields the identities
\[\begin{aligned}
F_2-F_0 &=\frac{P_{20}(m,z)}{8m(z+2)(z+4)(z+m)},\\
F_0-F_1 &=\frac{P_{01}(m,z)}{8m(z+2)((m+3)z+8m)},\\
F_2-F_1 &=\frac{P_{21}(m,z)}{2(z+2)(z+4)(z+m)((m+3)z+8m)}.
\end{aligned}\]
The signs of these three polynomials, not comparisons of rounded numerical eigenvalues, therefore solve the full discrete optimization.

**3. Small part sizes.** At \(m=4,5,6\), simplification gives strictly positive \(F_2-F_0\) and strictly negative \(F_0-F_1\) for every \(z>0\). For the first difference, positive numerators after cancellation are respectively \(z^2+7z+2\), \(17z^3+217z^2+656z+100\), and \(z(z+5)(z+10)\); for the second, negative numerators are respectively \(-5z^2-35z-14\), \(-3(4z^2+33z+10)\), and \(-2z^2-21z-4\). Hence \(i=0\) is uniquely optimal.

For \(m=7\), \(F_0-F_1<0\) throughout and \(F_2-F_0\) has the sign of \(13z^3+239z^2+888z-196\). This cubic has one positive root by Descartes' rule, lying strictly between \(1/5\) and \(1/4\). Thus the optimal count switches exactly from \(2\) to \(0\).

For \(m=8\), \(F_2-F_0\) changes sign exactly once, at the root \(\gamma_8\in(1/2,3/5)\). The sign change of \(F_0-F_1\) is at a smaller root of \(z^2+54z-8\), lying in \((1/10,1/5)\). Meanwhile \(F_2-F_1\) has the sign of \(z^4+19z^3+110z^2+196z-416\), with its only positive root in \((1,6/5)\). These strict rational intervals show \(F_2\) is lowest below \(\gamma_8\), and \(F_0\) lowest above it. Descartes' rule gives uniqueness of each positive root.

For \(m=9\), the three difference numerators, after cancellation of positive factors, are
\[\begin{aligned}
F_2-F_0 &: z^3+141z^2+800z-972,\\
F_0-F_1 &: 5z^2-110z+48,\\
F_2-F_1 &: z^4+17z^3+74z^2+82z-684.
\end{aligned}\]
The unique positive roots of the first and third are in \((1,11/10)\) and \((2,9/4)\), respectively. The quadratic has two positive roots, in \((2/5,1/2)\) and \((21,22)\). Its larger root is \(\delta_9\). Reading the signs in these strictly ordered intervals gives exactly \(F_2<F_0,F_1\) before \(\gamma_9\), \(F_0<F_1,F_2\) between \(\gamma_9\) and \(\delta_9\), and \(F_1<F_0,F_2\) afterward.

For \(m=10\), the corresponding numerators are
\[\begin{aligned}
F_2-F_0 &: -z^3+4z^2+72z-200,\\
F_0-F_1 &: 23z^2-154z+140,\\
F_2-F_1 &: z^4+14z^3+16z^2-104z-1040.
\end{aligned}\]
The cubic has exactly two positive roots, in \((13/5,27/10)\) and \((93/10,19/2)\). The quadratic roots lie in \((1,11/10)\) and \((11/2,57/10)\); the larger is \(\delta_{10}\). The quartic has just one positive root in \((4,41/10)\). Descartes' rule, sign changes at the indicated rational endpoints, and the strict ordering of these intervals imply the optimal sequence \(2\to0\to1\). Although \(F_2-F_0\) becomes negative once more after the cubic's second root, \(F_2-F_1>0\) there; the last regime remains \(i=1\).

**4. All larger sizes.** For every integer \(m\ge11\), \(P_{01}(m,z)>0\) for all \(z>0\). Its quadratic, leading, and constant coefficients are positive. The middle coefficient is nonnegative when \(m\ge14\); in the only three remaining cases \(m=11,12,13\), the respective discriminants are \(-1600704\), \(-6024960\), and \(-13528512\), so positivity also holds there. Hence \(F_1<F_0\) and the count \(0\) is never optimal. In the quartic \(P_{21}\), the constant, linear, and quadratic coefficients are strictly negative for every \(m\ge11\), while the leading coefficient is \(2>0\). The cubic coefficient is positive at \(m=11,12\) and negative for \(m\ge13\). In descending degree there is exactly one sign change, so Descartes' rule and continuity force exactly one positive root \(\tau_m\). Below it, \(F_2<F_1\); above it, \(F_1<F_2\). This establishes the full classification and all ties.

## Verification

The included standard-library Python script `verify.py` constructs the grounded Laplacian and performs exact Gauss–Jordan inversion for 81 rational instances, independently verifying the block formula. It additionally checks three cleared-denominator identities over 96 parameter pairs, rational root brackets, representative optima in every phase, and sign-coefficient conditions at sizes 11 through 119. Run `python verify.py`; the expected terminal line begins with `VERIFY_OK`. The finite calculations are reproducibility checks, not substitutes for the all-integer sign proof given above.

## Relationship to prior work

Lin, Fardad, and Jovanović (arXiv:1302.0450; earliest version February 3, 2013) formulate finite-gain noisy leader selection as minimization of a grounded-Laplacian inverse trace and develop convex-relaxation and greedy methods. Their general framework contains the objective used here; it does not provide these exact \(K_{2,m}\) four-leader phase boundaries. Fitch and Leonard (arXiv:1407.1569, 2014) give a joint-centrality characterization for one or two noise-corrupted leaders and special path/cycle solutions. Patterson, Yi, and Zhang (arXiv:1708.06873, 2017) derive resistance-distance formulas for arbitrary noisy leader sets, but their explicit graph optimizers concern other graph types and leader regimes. The general inverse-trace objective, electrical interpretations, and orbit reduction are background; the assessed new statement is the complete gain-dependent optimizer on the stated infinite four-leader family, including its exceptional nonmonotone phases. No claim of exhaustive historical priority is made.

## Limitations

The result is exact for equal strictly positive feedback gains and exactly four leaders on the undirected, unit-conductance family \(K_{2,m}\), \(m\ge4\). It concerns stationary total variance, not convergence rate, transient error, or unequal noise intensities. It does not compare alternative graph topologies or allow added edges. Identifying an equivalent older theorem remains a residual literature risk; independent mathematical assessment has not been performed.

## References

1. F. Lin, M. Fardad, and M. R. Jovanović, *Algorithms for Leader Selection in Stochastically Forced Consensus Networks*, arXiv:1302.0450 (first public version February 3, 2013), https://arxiv.org/abs/1302.0450 .
2. K. E. Fitch and N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569 (first public version July 7, 2014), https://arxiv.org/abs/1407.1569 .
3. S. Patterson, Y. Yi, and Z. Zhang, *A Resistance Distance-Based Approach for Optimal Leader Selection in Noisy Consensus Networks*, arXiv:1708.06873 (first public version August 23, 2017), https://arxiv.org/abs/1708.06873 .
