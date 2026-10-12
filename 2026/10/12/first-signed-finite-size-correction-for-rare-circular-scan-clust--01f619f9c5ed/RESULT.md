# First signed finite-size correction for rare circular scan clusters

## Finding
For each fixed integer \(k\ge4\) and each fixed real \(t>0\), place \(N\) independent uniform points on the unit circle. Let \(W_{N,k}\) be the shortest clockwise circular arc spanning \(k\) consecutive points, defined by the sum of the \(k-1\) intervening circular spacings. Put \(\lambda=t^{k-1}/(k-1)!\). Then, as integers \(N\to\infty\),
\[
\Pr\{N^{k/(k-1)}W_{N,k}\le t\}
=1-e^{-\lambda}-e^{-\lambda}\frac{(k+1)t^k}{k!}N^{-1/(k-1)}+o\bigl(N^{-1/(k-1)}\bigr).
\]
In particular, the first finite-size correction to the Weibull-type rare-cluster limit is strictly negative and its coefficient is explicit.

## Assumptions and scope
All \(N\ge k\) points are independent and uniform on a circle of circumference one; ties have probability zero. The integer \(k\ge4\) and number \(t>0\) are fixed before \(N\to\infty\). Let the sorted points be \(0\le U_{(1)}<\cdots<U_{(N)}<1\), with circular gaps \(G_i\) (indices modulo \(N\)). Then \(W_{N,k}=\min_{1\le i\le N}\sum_{j=0}^{k-2}G_{i+j}\). The event in the formula is the existence of a clockwise arc of length at most \(tN^{-k/(k-1)}\) spanning at least \(k\) sample points.

## Proof
**Exponential representation.** Let \(E_1,\ldots,E_N\) be independent unit exponential variables, \(T_N=\sum_iE_i\). The circular gap vector has the same law as \((E_1/T_N,\ldots,E_N/T_N)\). Set \(\epsilon_N=N^{-1/(k-1)}\) and \(q=t\epsilon_N\). Define \(J_i(q)=\mathbf1\{E_i+\cdots+E_{i+k-2}\le q\}\) cyclically and define a new-cluster indicator \(K_i(q)=J_i(q)(1-J_{i-1}(q))\). For sufficiently large \(N\), distinct variables in each window are distinct.

**Exact local expansion.** A Gamma\((k-1,1)\) distribution at the origin has expansion
\[
\Pr(J_i(q)=1)=\frac{q^{k-1}}{(k-1)!}-\frac{(k-1)q^k}{k!}+O_k(q^{k+1}).
\]
For adjacent windows, integrate over the sum \(s\) of their \(k-2\) shared exponentials. The joint probability is exactly
\[
\Pr(J_{i-1}(q)=J_i(q)=1)
=\int_0^q\frac{e^{-s}s^{k-3}}{(k-3)!}\bigl(1-e^{-(q-s)}\bigr)^2\,ds
=\frac{2q^k}{k!}+O_k(q^{k+1}).
\]
The last identity uses the beta integral \(\int_0^q s^{k-3}(q-s)^2ds=2(k-3)!q^k/k!\). Hence
\[
\mu_N:=\mathbb E\sum_{i=1}^N K_i(q)
=N\left(\frac{q^{k-1}}{(k-1)!}-\frac{(k+1)q^k}{k!}+O_k(q^{k+1})\right)
=\lambda-\frac{(k+1)t^k}{k!}\epsilon_N+O_{k,t}(\epsilon_N^2).
\]

**Poisson approximation at the required precision.** Each \(K_i\) depends only on \(k\) consecutive exponentials, so it has at most \(2k-2\) other potentially dependent indicators. For \(2\le d\le k-2\), simultaneous occurrence of \(K_i\) and \(K_{i+d}\) implies both \(J_i=J_{i+d}=1\); in turn, the sum of all \(k-1+d\ge k+1\) distinct exponentials covered by the two overlapping windows is at most \(2q\). Its probability is \(O_k(q^{k+1})\). At separation \(d=k-1\), the underlying \(J\)-windows are disjoint, so the joint probability is at most \(O_k(q^{2k-2})=O_k(q^{k+1})\). The cases \(d=\pm1\) give \(K_iK_{i+d}=0\). The same argument applies in the opposite circular direction. The dependency-graph Poisson approximation of Arratia, Goldstein and Gordon therefore yields
\[
d_{\mathrm{TV}}\left(\mathcal L\left(\sum_i K_i\right),\operatorname{Poisson}(\mu_N)\right)
\le C_k\left(Nq^{2k-2}+Nq^{k+1}\right)
=O_{k,t}(N^{-1}+\epsilon_N^2)=o(\epsilon_N).
\]
Here the neighborhood bound follows by summing single-indicator products and joint probabilities; indicators outside the neighborhoods use disjoint exponentials and are independent.

If some \(J_i\) occurs but no \(K_i\) occurs, all \(N\) cyclic \(J_i\) occur. This implies \((k-1)T_N\le Nq\), because the sum of their \(N\) window sums is \((k-1)T_N\). For \(q\to0\), the Chernoff bound \(\Pr\{T_N\le Nq/(k-1)\}\le (eq/(k-1))^N=o(\epsilon_N)\) removes this exceptional event. Thus
\[
\Pr\{\min_i\sum_{j=0}^{k-2}E_{i+j}\le q\}
=1-e^{-\lambda}-e^{-\lambda}\frac{(k+1)t^k}{k!}\epsilon_N+o(\epsilon_N).
\]

**Removing the random normalization.** The desired uniform-spacing event has exponential threshold \(qT_N/N\), rather than \(q\). Since \(k\ge4\), select \(a\) strictly between \(1/(k-1)\) and \(1/2\), and put \(\delta_N=N^{-a}=o(\epsilon_N)\). Gamma concentration yields \(\Pr\{|T_N/N-1|>\delta_N\}\le2\exp(-cN\delta_N^2)=o(\epsilon_N)\). On the complementary event sandwich the normalized event between the two deterministic exponential-window events with thresholds \(q(1-\delta_N)\) and \(q(1+\delta_N)\). The preceding Poisson expansion holds with either threshold, while varying \(t\) by the factor \(1\pm\delta_N\) changes its leading term by \(O_{k,t}(\delta_N)=o(\epsilon_N)\). The two bounds have the same displayed expansion. This proves the theorem.

## Verification
The included standalone `verify_rare_scan.py` checks the local Gamma coefficients, exact beta-integral identity and resulting cluster intensity for integers \(4\le k\le32\), using exact rational arithmetic. These finite computations are supplemental checks of the algebra. The universal result follows from the analytic simplex expansions, the dependency-graph Poisson approximation and the exponential-normalization sandwich given above.

## Relationship to prior work
Yuan [1] gives exact finite-\(N\) circular scan formulas for \(k=3\) and \(k=N-1\), but does not identify this first signed large-\(N\) correction for fixed \(k\ge4\). Exact finite scan procedures and conditional Bonferroni inequalities predate [1] [2,3]; they are not claimed as new. The dependency-graph Poisson estimate used in the proof is classical [4], and the contribution is the explicit local cluster-start expansion combined with a sharp normalization-scale comparison. Established Poisson limit and approximation results for ordered spacings are distinct from an evaluated signed first-error coefficient [5].

## Limitations
The limit is pointwise for fixed \(k\ge4\) and fixed \(t>0\); no uniformity in \(t\) or growing-\(k\) expansion is asserted. The case \(k=3\) is deliberately excluded because exponential normalization fluctuates on the same scale as the proposed correction. No extension to nonuniform circle sampling is asserted. Earlier exact scan formulae could implicitly encode this coefficient without stating it, and the full text of some older scan-statistics literature was not available for priority comparison; independent scientific audit has not been performed.

## References
[1] H. Yuan, *Exact Closed-Form Formulae for Linear and Circular Continuous Scan Statistics: P_c(N-1;N,w), P_c(3;N,w), and P(3;N,w)*, arXiv:2604.25360v1 (2026-04-28), https://arxiv.org/abs/2604.25360.

[2] J. Glaz, J. Naus, S. Wallenstein, *Scan Statistics*, Springer, 2001, chapter "Scanning N uniform distributed points: Exact results", pp. 113–140.

[3] J. Chen, J. Glaz, J. Naus, S. Wallenstein, *Bonferroni-type inequalities for conditional scan statistics*, Statistics & Probability Letters **53** (2001), 67–77, doi:10.1016/S0167-7152(01)00034-7.

[4] R. Arratia, L. Goldstein, L. Gordon, *Two moments suffice for Poisson approximations: the Chen–Stein method*, Annals of Probability **17** (1989), 9–25.

[5] J. Glaz, J. Naus, M. Roos, S. Wallenstein, *Poisson approximations for the distribution and moments of ordered m-spacings*, Journal of Applied Probability.
