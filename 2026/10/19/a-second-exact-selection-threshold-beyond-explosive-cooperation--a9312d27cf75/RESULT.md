# A second, exact selection threshold beyond explosive-cooperation onset

## Finding

A deterministic cooperative equilibrium can be attracting while rare-mutation stationary behavior still concentrates on full defection. For the nonlinear payoff difference from the higher-order cooperation model of Civilini et al., an independently defined well-mixed Fermi birth–death closure with symmetric exploration probability \(\mu_N=N^{-2}\) has **two distinct sharp thresholds**: an interior fixed-point birth at
\[
C_{\mathrm{fold}}=(\sqrt A+\sqrt B)^2,
\]
and a stationary-selection switch at
\[
C_{\mathrm{sel}}=\bigl(2\sqrt{A/3}+\sqrt{B+A/3}\bigr)^2>C_{\mathrm{fold}}.
\]
Here \(A=-S>0\), \(B=T-1>0\), and \(C=(2(G-W)+T-S-1)\delta\). The upper deterministic fixed point is \(r_+(C)\). For fixed \(0\le C\le 2(G-W)+T-S-1\), the unique stationary distribution \(\pi_N^C\), pushed forward to cooperation frequencies \(k/N\), obeys
\[
\pi_N^C\Longrightarrow
\begin{cases}
\delta_0,&C\le C_{\mathrm{sel}},\\
\delta_{r_+(C)},&C>C_{\mathrm{sel}}.
\end{cases}
\]
The first line includes exact equality: the mutation scale \(N^{-2}\) selects the defective boundary even when the two large-deviation heights are equal. If \(C_{\mathrm{sel}}\) exceeds the physical maximum of \(C\), a stationary-selection switch is not physically accessible.

For the payoff-symmetric class \(A=B\), the ratio of the sharp thresholds is exactly \(C_{\mathrm{sel}}/C_{\mathrm{fold}}=4/3\). At \(T=3/2\), \(S=-1/2\), \(2(G-W)=5\), the corresponding synergy parameters are \(\delta_{\mathrm{fold}}=1/3\) and \(\delta_{\mathrm{sel}}=4/9\). At the latter, \(r_-=1/4\), \(r_+=3/4\). Hence for \(1/3<\delta\le4/9\), an attracting cooperative deterministic equilibrium coexists with stationary defection selection.

## Assumptions and scope

Fix payoff parameters \(T>1\), \(S<0\), \(a=2(G-W)>0\), \(b=T-S-1>0\), \(c=a+b\), \(0\le\delta\le1\), and selection strength \(w>0\). Set \(A=-S>0\), \(B=T-1>0\), and \(C=c\delta\). Let
\[
D_C(x)=-A+(C+A-B)x-Cx^2,
\qquad 0\le x\le1.
\]
This is the well-mixed payoff difference of the 2023 higher-order social-dilemma model. It is **not** asserted that the stochastic finite-graph process of that paper is identical to the chain below.

For each integer \(N\ge2\), let \(K_t\in\{0,1,\ldots,N\}\) be the continuous-time birth–death chain with total upward and downward transition rates at state \(k\), \(x=k/N\):
\[
q^+_{N,k}=x(1-x)\sigma(wD_C(x))+\mu_N(1-x),
\quad q^-_{N,k}=x(1-x)\sigma(-wD_C(x))+\mu_N x,
\]
where \(\sigma(z)=1/(1+e^{-z})\) and \(\mu_N=N^{-2}\). The endpoint rates are interpreted directly from these expressions. Symmetric mutations make the finite chain irreducible, so it has a unique stationary distribution \(\pi_N^C\). The deterministic imitation drift in the zero-mutation limit is \(x(1-x)\tanh(wD_C(x)/2)\). The limits concern fixed game parameters as \(N\to\infty\); they are not uniform over parameters approaching either threshold.

## Proof

**1. Deterministic threshold.** For \(0<x<1\), \(\partial_C D_C(x)=x(1-x)>0\); also \(D_C(0)=-A\), \(D_C(1)=-B\). The first appearance of nonnegative interior payoff difference occurs when \(D_C\) has a double root. Solving \(D_C(r)=\partial_xD_C(r)=0\) gives \(C_{\mathrm{fold}}=(\sqrt A+\sqrt B)^2\) at \(r=\sqrt A/(\sqrt A+\sqrt B)\). For \(C>C_{\mathrm{fold}}\) there are exactly two simple interior roots \(0<r_-<r_+<1\); the drift signs are negative, positive, negative in the three intervals. Thus \(r_-\) is repelling and \(r_+\) attracting, as is boundary zero.

**2. Potential crossing.** Define
\[
\Psi_C(x)=w\int_0^xD_C(t)\,dt
=w\left[-Ax+\frac{C+A-B}{2}x^2-\frac C3x^3\right].
\]
For \(C>C_{\mathrm{fold}}\), factor \(D_C(t)=-C(t-r_-)(t-r_+)\). Since \(D_C(r_+)=0\), integration and the root identity yield
\[
\frac{\Psi_C(r_+)}w=\frac{Cr_+^2}{6}(r_+-3r_-).
\]
The height \(\Psi_C(r_+)\) strictly increases with \(C\), because
\[
\frac{d}{dC}\frac{\Psi_C(r_+)}w
=\int_0^{r_+}t(1-t)\,dt>0.
\]
At the fold, the height is negative; at large \(C\), it is positive. The crossing is therefore unique. At that crossing \(r_+=3r_-\). Vieta's relations give \(Cr_-r_+=A\) and \(C(r_-+r_+)=C+A-B\). Hence \(r_-=\sqrt{A/(3C)}\) and \(C+A-B=4\sqrt{AC/3}\); solving for the root above the fold gives the asserted \(C_{\mathrm{sel}}\). This root exceeds \(C_{\mathrm{fold}}\), as the crossing must occur strictly after a negative-height fold. The only global maximizers of \(\Psi_C\) on \([0,1]\) are zero below this crossing, \(r_+\) above it, and both exactly at the crossing. Since \(\Psi_C'(1)=-wB<0\), the right endpoint never supplies a competing maximum.

**3. Finite-chain stationary law.** Detailed balance gives
\[
\pi_N(k)=\pi_N(0)\prod_{j=0}^{k-1}\frac{q^+_{N,j}}{q^-_{N,j+1}}.
\]
Using the exact logistic identity \(\sigma(z)/\sigma(-z)=e^z\), telescoping the factors \((j/N)(1-j/N)\), and bounding the \(\mu_N\)-corrections by \(O((\log N)/N)\) in logarithmic products, one obtains a constant \(K\ge1\), depending only on fixed parameters, such that for \(1\le k\le N-1\), \(x=k/N\),
\[
K^{-1}\frac{\mu_N}{x(1-x)}e^{N\Psi_C(x)}
\le \frac{\pi_N(k)}{\pi_N(0)}
\le K\frac{\mu_N}{x(1-x)}e^{N\Psi_C(x)}.
\]
The uniform bounded factors include the initial boundary jump, the Riemann-sum error in \(\sum_j wD_C(j/N)\), and the one-step mismatch between the two logistic arguments. The endpoint \(k=N\) has an extra polynomial factor relative to \(k=N-1\), hence cannot change the exponential maximizers because \(\Psi_C(1)<\max\Psi_C\). Compactness and these bounds imply concentration on the unique global maximizer whenever it is unique.

**4. Exact selection at equal height.** At \(C=C_{\mathrm{sel}}\), the potential has a strict one-sided maximum at zero with \(\Psi_C'(0)=-wA<0\), and a nondegenerate quadratic maximum at \(r_+\). For sufficiently small disjoint neighborhoods there are positive constants \(\eta_0,\eta_1\) such that \(\Psi_C(x)\le-\eta_0x\) near zero and \(\Psi_C(x)\le-\eta_1(x-r_+)^2\) near \(r_+\). Away from both, the potential is strictly negative. The relative total weights are bounded by a geometric-harmonic boundary sum of order \(O(\mu_N N)\), a Gaussian interior sum of order \(O(\mu_N\sqrt N)\), and exponentially small residual terms. With \(\mu_N=N^{-2}\), all vanish; thus \(\pi_N(0)\to1\) even at equal potential heights. This finishes the weak-limit classification.

**5. Symmetric payoff example.** Substituting \(A=B\) gives \(C_{\mathrm{fold}}=4A\) and \(C_{\mathrm{sel}}=16A/3\). With \(A=B=1/2\) and \(c=6\), this yields \(\delta=1/3\), \(4/9\) and the stated interior roots.

## Verification

Run `python3 VERIFY.py` with the Python standard library. It checks the potential crossing polynomial and integral identities with exact rational arithmetic, uses separately coded finite birth–death detailed-balance reconstruction, and checks stationary concentration trends for finite sample sizes. The standalone program printed `PASS: 787 exact and numeric assertions`. These tests supplement rather than replace the analytic argument; no finite computation certifies the infinite-population limit.

## Relationship to prior work

Civilini, Sadekar, Battiston, Gómez-Gardeñes and Latora (arXiv:2303.11475, first posted March 20, 2023) derive the nonlinear payoff-difference polynomial and deterministic saddle-node criterion for explosive cooperation. Their supplementary Eq. S12 supplies the polynomial; their Eq. S14 identifies the deterministic threshold. The distinct stationary large-population selection threshold, including the asymptotic boundary selection at the equal-height point for \(N^{-2}\) mutation, is the present result. The paper discusses stochastic realizations and quasistationary peaks but not this particular rare-mutation stationary regularization. Nałęcz-Jawecki and Miękisz discuss general mean-potential laws in evolutionary games: the present use of potential methods is not claimed as new. Sandholm and Staudigl discuss generic large-deviation methods for evolutionary dynamics; the particular thresholds are not inferred merely from the title or abstract of that source.

## Limitations

The result applies to the explicitly defined well-mixed birth–death chain, not to stochastic higher-order hypergraph dynamics without further derivation. Mutation must scale as \(N^{-2}\) for the equality selection statement; other mutation regimes can change the polynomial prefactor at the equal-height crossing. Neither mixing times nor finite-size metastable switching rates are characterized. Experimental stochastic stationarity may take longer than practical observation windows. All thresholds refer to fixed positive selection strength and fixed payoffs, and a formally computed threshold may lie outside the physically permitted synergy interval. Novelty is a best-knowledge literature comparison, not a claim of exhaustive priority verification.

## References

1. A. Civilini, O. Sadekar, F. Battiston, J. Gómez-Gardeñes, and V. Latora, “Explosive cooperation in social dilemmas on higher-order networks,” arXiv:2303.11475v1 (2023-03-20); *Physical Review Letters* 132, 167401 (2024), DOI:10.1103/PhysRevLett.132.167401.
2. M. Nałęcz-Jawecki and J. Miękisz, “Mean-potential law in evolutionary games,” arXiv:1801.08010 (2018).
3. W. H. Sandholm and M. Staudigl, “Sample Path Large Deviations for Stochastic Evolutionary Game Dynamics,” *Mathematics of Operations Research* (2018), DOI:10.1287/moor.2017.0908.
