# Periodic rescue and random-switching extinction in a two-stage semelparous population

## Finding

A discrete two-stage semelparous population may decline in **each constant environment**, grow under **strict seasonal alternation**, yet decline at an exact, season-correlation-independent rate under **every nondegenerate symmetric random seasonal switching law**. For two positive fecundities \(b_i\) and two survival fractions \(s_i\), the random growth rate is
\[
\lambda_{\rm rand}=(b_1b_2s_1s_2)^{1/4}\qquad(0<q<1),
\]
where \(q\) is the probability of repeating the environmental state. Perfect alternation \(q=0\) instead gives
\[
\lambda_{\rm alt}=\sqrt{\max\{b_1s_2,b_2s_1\}},
\]
strictly larger whenever \(b_1s_2\ne b_2s_1\). Thus the typical growth rate is discontinuous at perfect alternation even though the transition probabilities converge.

For an exact biological parameter choice,
\[
A_1=\begin{pmatrix}0&4\\1/16&0\end{pmatrix},\qquad
A_2=\begin{pmatrix}0&1/4\\1&0\end{pmatrix},
\]
each constant season has population multiplier \(1/2\), deterministic alternation gives multiplier \(2\), and every \(0<q<1\) gives almost-sure multiplier \(1/2\). The expected total abundance has a different exact multiplier,
\[
\mu(q)=\frac{17(1-q)+\sqrt{225-450q+289q^2}}{16}.
\]
It grows exponentially exactly when \(0<q<7/13\), despite almost-sure extinction for those same switching probabilities; it is critical at \(q=7/13\) and decays for \(7/13<q<1\). All strict growth/decline inequalities persist under sufficiently small changes of the four demographic parameters.

## Assumptions and scope

The state \(z_t=(J_t,A_t)^T\in(0,\infty)^2\) consists of juvenile and adult abundances, with age-stage update \(z_t=A_{\eta_t}z_{t-1}\) and \(A_i=\begin{pmatrix}0&b_i\\s_i&0\end{pmatrix}\). Here \(b_i>0\) is per-adult juvenile production; \(0<s_i\le1\) is juvenile-to-adult survival. Neither age stage remains in its original stage for the next census, appropriate to two-stage semelparity. All asymptotic statements concern an arbitrary *strictly positive* initial vector and, for random switching, either starting environment. The two-state Markov chain \(\eta_t\) stays in its present state with probability \(q\) and flips with probability \(1-q\). Matrix entries are deterministic conditional on the season, with no individual-level demographic sampling. The norm is the total abundance \(\|z_t\|_1=J_t+A_t\); equivalent norms give the same exponential rate.

## Proof

**1. Exact typical rate.** Multiplication of any two consecutive demographic matrices yields
\[
A_jA_i=\operatorname{diag}(b_js_i,s_jb_i).
\]
Consequently, the first component of \(z_{2m}\) equals its positive initial value multiplied by \(\prod_{k=1}^{m}b_{\eta_{2k}}s_{\eta_{2k-1}}\); the second equals its positive initial value multiplied by \(\prod_{k=1}^{m}s_{\eta_{2k}}b_{\eta_{2k-1}}\). For \(0<q<1\), the finite-state environmental chain is irreducible and aperiodic, and its even-time and odd-time subsamples are ergodic with stationary distribution \((1/2,1/2)\). The ergodic theorem applied separately to both parity subsamples gives almost surely
\[
\lim_{m\to\infty}\frac{1}{2m}\log J_{2m}=
\lim_{m\to\infty}\frac{1}{2m}\log A_{2m}
=\frac14\log(b_1b_2s_1s_2).
\]
The same holds for the logarithm of the total abundance because both stage abundances are positive; an extra demographic update changes the log by a bounded amount, proving the full-time limit. This identifies the exact asymptotic multiplier for every \(0<q<1\), independently of \(q\).

For \(q=0\), environments alternate deterministically. Their two-step product is diagonal with diagonal entries \(b_2s_1\) and \(s_2b_1\), in one seasonal phase, and the diagonal entries are exchanged in the opposite phase. A strictly positive initial stage vector therefore has rate \(\sqrt{\max\{b_1s_2,b_2s_1\}}\). Writing \(X=b_1s_2\), \(Y=b_2s_1\), the random rate is \((XY)^{1/4}\) and the alternating rate is \(\max(X,Y)^{1/2}\), which is strictly greater when \(X\ne Y\). At \(q=1\) the environment stays fixed and the multiplier is \(\sqrt{b_is_i}\), dependent on the initial environmental state; it is not included in the random formula.

**2. Exact rescue/extinction example.** Both displayed demographic matrices square to \(I/4\), so each constant environment has spectral radius \(1/2\). But the order-2 product is \(A_2A_1=\operatorname{diag}(1/64,4)\), giving strictly positive populations alternating multiplier \(2\). The general formula yields \(\lambda_{\rm rand}=(4\cdot(1/4)\cdot(1/16)\cdot1)^{1/4}=1/2\) for every \(0<q<1\). The strict inequalities \(\max_i\sqrt{b_is_i}<1\), \(\lambda_{\rm alt}>1\), \(\lambda_{\rm rand}<1\) hold on a nonempty open subset of the admissible demographic parameter region by continuity.

**3. Mean abundance versus the typical trajectory.** Let \(u_t^{(i)}=\mathbb E[z_t\mathbf1_{\{\eta_t=i\}}]\). For \(0<q<1\) the combined conditional expectation \(u_t=(u_t^{(1)},u_t^{(2)})^T\) obeys \(u_t=M(q)u_{t-1}\), where
\[
M(q)=\begin{pmatrix}qA_1&(1-q)A_1\\(1-q)A_2&qA_2\end{pmatrix}.
\]
For the exact matrices, the characteristic polynomial factors as
\[
\det(xI-M(q))=\frac{(8x^2+17(1-q)x+2-4q)(8x^2-17(1-q)x+2-4q)}{64}.
\]
The matrix \(M(q)\) is irreducible and nonnegative for \(0<q<1\). Its Perron root is the larger positive root of the second quadratic, equal to \(\mu(q)\) above. A strictly positive left Perron eigenvector bounds \(\|u_t\|_1\) above and below by constant multiples of \(\mu(q)^t\), even if the initial environmental state is fixed. Thus \(\lim_{t\to\infty}(\mathbb E\|z_t\|_1)^{1/t}=\mu(q)\). The polynomial \(8x^2-17(1-q)x+2-4q\) evaluates to \(13q-7\) at \(x=1\), and its smaller root lies below one throughout \(0<q<1\). Hence its Perron root is greater than, equal to, or less than one exactly as \(q<7/13\), \(q=7/13\), or \(q>7/13\), respectively. At the critical equality \(\mu(q)=1\), the statement concerns the exponential rate, not any almost-sure survival claim.

## Verification

The included standalone Python 3/SymPy file `verify_exact.py` reconstructs the demographic products, checks the characteristic factorization and critical inequality with exact symbolic arithmetic, and compares the four-state expectation recursion against full rational enumeration of switching paths in \(48\) independent cases. It also samples long random trajectories as a non-probative diagnostic. The infinite-horizon assertions follow from the proved ergodic and Perron–Frobenius arguments, **not** from finite computations or simulations.

## Relationship to prior work

Sanz (2019) studies stochastic growth rates and extinction bounds for environment-dependent population projection matrices, including a two-stage rich/poor example. Its main estimates operate in a general positive demographic matrix framework; they do not yield the exact discontinuous boundary here or the analytic ensemble threshold \(7/13\) in this strictly semelparous (imprimitive) specialization. Chitour, Mazanti and Sigalotti (2018) characterize generic differences between deterministic and probabilistic matrix-product growth; the qualitative possibility of a gap is therefore established mathematical background, not claimed as newly discovered here. The specific population life cycle, the independence of the random Lyapunov rate from every interior Markov persistence parameter, and the contrasting rational ensemble threshold form the present quantitative claim. The continuous-time population growth models of Monmarché, Schreiber and Strickler (2024) have different evolution operators and positive-time flows, rather than the exact anti-diagonal discrete-time update used here.

## Limitations

These are density-independent real-valued population abundances, not stochastic finite-individual branching processes; “almost-sure extinction” means population *density* tends exponentially to zero along almost every seasonal path. The typical-rate identity uses strict positivity of both initial stage abundances; zero entries can select a different deterministic alternating eigen-branch. The jump occurs on the imprimitive zero-diagonal demographic boundary and is not asserted to survive arbitrary addition of positive stage-retention terms. The mean-growth threshold \(7/13\) is specific to the exact rational demographic example, not a universal ecological constant. Earlier literature on cyclic Leslie matrices and switching products might have equivalent formulas in different notation; no uniqueness or priority claim is made.

## References

1. L. Sanz, “Conditions for growth and extinction in matrix models with environmental stochasticity,” *Ecological Modelling* 411 (2019), 108797, doi:10.1016/j.ecolmodel.2019.108797; lawful open preprint arXiv:2402.03827.
2. Y. Chitour, G. Mazanti and M. Sigalotti, “On the gap between deterministic and probabilistic joint spectral radii for discrete-time linear systems,” arXiv:1812.08399 (2018).
3. P. Monmarché, S. J. Schreiber and É. Strickler, “Impacts of Tempo and Mode of Environmental Fluctuations on Population Growth,” arXiv:2408.11179 (2024).
4. A. Grant and T. G. Benton, “The Impact of Environmental Variation on Demographic Convergence of Leslie Matrix Population Models,” *Theoretical Population Biology* 50 (1996), 18–30, doi:10.1006/tpbi.1996.0021.
