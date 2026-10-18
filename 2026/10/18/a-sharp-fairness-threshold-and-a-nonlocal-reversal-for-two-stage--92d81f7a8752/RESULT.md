# A sharp fairness threshold and a nonlocal reversal for two-stage vaccination renewal

## Finding

For a two-group, fixed-dose-rate recurrent-vaccination model with Erlang-2 booster intervals and step-function waning immunity, equal allocation can be a **strict local minimizer** of the disease-free next-generation spectral factor yet fail even to beat a completely concentrated allocation. The local transition is governed by an exact contact-assortativity threshold, and a fully explicit example proves the local/global discrepancy. In contrast, exponential booster intervals with the same mean-dose-rate constraint always make equal allocation globally optimal for all non-perfectly disassortative mixing.

Specifically, let \(c>0\), \(0<\alpha\leq 2\), and \(-1\leq x\leq1\). Put
\[
F(y)=(1+y)e^{-2y},\qquad
s_1=F(c(1+x)),\quad s_2=F(c(1-x)),
\]
\[
K_\alpha=\begin{pmatrix}1-\alpha/2&\alpha/2\\\alpha/2&1-\alpha/2\end{pmatrix},
\qquad
R_2(x)=\rho\big(K_\alpha\operatorname{diag}(s_1,s_2)\big).
\]
Here \(\rho\) denotes spectral radius. Then the equal split is stationary and
\[
R_2''(0)=c^2 e^{-2c}\left(4c+\frac{2(1-\alpha)}{\alpha}\frac{(1+2c)^2}{1+c}\right).
\]
Consequently equal allocation is a strict local **minimum** when
\[
0<\alpha<\alpha_c(c):=2-\frac{1}{1+2c+2c^2},
\]
and a strict local **maximum** when \(\alpha_c(c)<\alpha\leq2\). At equality the quadratic test is degenerate and no local classification is asserted. For any fixed \(1<\alpha<2\), the transition occurs precisely at
\[
c=\frac{\sqrt{\alpha/(2-\alpha)}-1}{2}.
\]
For \(\alpha=3/2\) and \(c=3/8\), equal allocation is a strict local minimum, but
\[
R_2(1)<R_2(0)=\frac{11}{8}e^{-3/4}.
\]
Thus the local minimum is **not** a global minimum. This statement does not claim that \(x=1\) is a global minimizer.

For comparison, if the boosters are exponential rather than Erlang-2, keeping exactly the same per-group mean booster rates and step immunity, then
\[
R_1(x)=e^{-c}\left[(1-\alpha/2)\cosh(cx)+\sqrt{\frac{\alpha^2}{4}+(1-\alpha/2)^2\sinh^2(cx)}\right].
\]
For every \(c>0\) and \(0<\alpha<2\), \(R_1\) is strictly increasing in \(|x|\) and the equal split is the unique global minimizer; for \(\alpha=2\), \(R_1(x)\equiv e^{-c}\). For Erlang-2 at \(\alpha=2\), on the other hand,
\[
R_2(x)=e^{-2c}\sqrt{(1+c)^2-c^2x^2},
\]
which is strictly decreasing in \(|x|\).

## Assumptions and scope

The two population groups each have mass \(1/2\), equal epidemiological activity and symmetric contact mixing. The original contact parameter \(\alpha\) runs from assortative to perfectly cross-group contact as \(\alpha\) increases from zero to two; the theorem excludes \(\alpha=0\). Let the common perfect-immunity duration following each vaccine be \(\tau>0\). In group \(i\), i.i.d. inter-booster times are Erlang with shape two and rate \(2\nu_i\), so \(\mathbb E[T_i]=1/\nu_i\). Each booster resets the susceptibility age to zero and susceptibility becomes one at age \(\tau\), remaining one until another booster. The total vaccine-administration rate per population member is fixed at \(\nu>0\): with parameter \(x\),
\[
\nu_1=\nu(1+x),\qquad \nu_2=\nu(1-x),\qquad c=\nu\tau.
\]
The endpoints \(x=\pm1\) are interpreted as the natural limit where one group receives no boosters and has susceptibility one. The optimization criterion is only the positive disease-free next-generation spectral factor \(R_j\); if all other disease parameters are fixed, lowering it raises the model's endemicity threshold. No claim is made about infection trajectories, vaccine logistics, individual wellbeing, stochastic outbreak probability or global epidemic extinction dynamics.

The originating model and the spectral-factor/cost reduction are given in Foutel-Rodier, Charpentier and Guérin [1], especially Section 5, the two-group matrix and the fixed per-capita dose-rate constraint. We introduce the Erlang-2/step-immunity specialization and establish the allocation phase boundary and the explicit local/global counterexample.

## Proof

**1. Renewal susceptibility.** For a booster interval \(T\) and the stated susceptibility-at-age function, the fraction of its cycle spent susceptible equals \((T-\tau)_+/T\). By renewal reward, the stationary mean is
\[
\Sigma=\frac{\mathbb E[(T-\tau)_+]}{\mathbb E[T]}=\frac{\int_\tau^\infty\mathbb P(T>u)\,du}{\mathbb E[T]}.
\]
For Erlang-2 with rate \(2\nu_i\), the survival function is \(e^{-2\nu_i u}(1+2\nu_i u)\); integration gives \(\mathbb E[(T-\tau)_+]=e^{-2\nu_i\tau}(\tau+1/\nu_i)\). Thus \(\Sigma_i=F(\nu_i\tau)\) with \(F(y)=(1+y)e^{-2y}\), including its continuous extension \(F(0)=1\). For exponential intervals of rate \(\nu_i\), the same calculation gives \(\Sigma_i=e^{-\nu_i\tau}\).

**2. Exact spectral factor and local threshold.** Set \(t=\alpha/2\), \(m(x)=(s_1+s_2)/2\), and \(d(x)=(s_1-s_2)/2\). Directly taking the characteristic polynomial of the two-by-two nonnegative matrix yields
\[
R_2(x)=(1-t)m(x)+\sqrt{t^2m(x)^2+(1-2t)d(x)^2}.
\]
The expression is real and positive for the stated domain, with a smooth branch near \(x=0\) since \(t>0\). Since \(m(0)=F(c)\), \(d(0)=0\), and the two groups interchange under \(x\mapsto-x\), this proves stationarity at zero and \(R_2(0)=F(c)\). The Taylor expansions
\[
m(x)=F(c)+\frac{c^2}{2}F''(c)x^2+O(x^4),\qquad
 d(x)=cF'(c)x+O(x^3)
\]
give
\[
R_2''(0)=c^2\left(F''(c)+\frac{2(1-\alpha)}{\alpha}\frac{F'(c)^2}{F(c)}\right).
\]
Substituting \(F'(c)=-(1+2c)e^{-2c}\) and \(F''(c)=4ce^{-2c}\) proves the displayed derivative. Multiplying its sign expression by the strictly positive \(\alpha(1+c)/2\) reduces the condition \(R_2''(0)>0\) to
\[
\alpha(1+2c+2c^2)<1+4c+4c^2.
\]
Equivalently \(\alpha<2-1/(1+2c+2c^2)\). Strict second-derivative signs give the corresponding local extremum assertions. The boundary function rises strictly from one toward two as \(c\) rises; solving its equality for fixed \(\alpha\in(1,2)\) gives the stated critical rate \(c\).

**3. Explicit strict local minimum that is not global.** With \(\alpha=3/2\), \(c=3/8\), the threshold is \(\alpha_c=98/65>3/2\) and the exact second derivative is \(3e^{-3/4}/1408>0\), so zero is a strict local minimum. Let \(a=e^{-3/4}\). At the concentrated allocation \(x=1\), the two susceptibilities are \(s_1=(7/4)a^2\) and \(s_2=1\). The Perron root is the unique positive root of
\[
P(z)=z^2-\frac{1+(7/4)a^2}{4}z-\frac78a^2.
\]
At the fair value \(z_0=(11/8)a\), direct algebra gives
\[
P(z_0)=\frac{a}{128}\left(130a-44-77a^2\right).
\]
For a rational, non-numerical sign proof, the alternating series for \(e^{-3/4}\) through degree five implies \(a>19339/40960>47/100\); the first three terms of the positive exponential series show \(e^{3/4}>2\), hence \(a<1/2\). The quadratic \(g(a)=130a-44-77a^2\) has \(g'(a)=130-154a>0\) on this interval and \(g(47/100)=907/10000>0\), so \(P(z_0)>0\). Since \(P\) has exactly one positive root and its positive region begins after that root, \(R_2(1)<z_0=R_2(0)\). This is a strict comparison of feasible allocations under the *same* mean dose-rate budget.

**4. Memoryless renewal contrast.** Using \(s_i=e^{-c(1\pm x)}\) in the same characteristic formula, write \(m=e^{-c}\cosh(cx)\), \(d=-e^{-c}\sinh(cx)\) and obtain the displayed \(R_1(x)\). When \(0<t<1\), the nonconstant coefficient \(1-t\) is positive; \(\cosh(cx)\) strictly increases and \(\sinh^2(cx)\) strictly increases with \(|x|>0\), showing the unique global minimum at zero. When \(t=1\), the expression reduces identically to \(e^{-c}\). When boosters are Erlang-2 and \(t=1\), the matrix is off-diagonal, so its Perron root is \(\sqrt{s_1s_2}\). The identity \(s_1s_2=e^{-4c}((1+c)^2-c^2x^2)\) proves the final strict decreasing formula. No extrapolation to other Erlang shapes is made.

## Verification

The accompanying standalone `verify.py` reconstructs the matrix and its characteristic polynomial, checks renewal survival and derivative identities using symbolic algebra, verifies the exact Hessian at the example, certifies the polynomial inequality using rational arithmetic, and compares high-precision Perron eigenvalues and dose-rate budgets. It additionally checks the exponential-clock formula and the perfectly cross-group Erlang-2 identity. The analytical inequalities above, not numerical sampling, prove the general assertions.

Execute from the directory containing the file with `python verify.py`; dependencies are Python 3, SymPy and mpmath. The output ends with a count of passed assertions.

## Relationship to prior work

Foutel-Rodier, Charpentier and Guérin [1] introduce renewal vaccination, the fixed-dose-rate constraint, and the two-group next-generation matrix. Their Proposition 6 proves fair allocation optimal for \(0\leq\alpha\leq1\), and Figure 6 explores selected nonassortative cases numerically. Neither their matrix formula alone nor their assortative proposition states the exact Erlang-2 curvature boundary or the strict nonlocal counterexample given here.

Delmas, Dronnier and Zitt [2, Section 4] already establish important results about disassortative optimal vaccination and spectral-radius concavity **when the cost is linear in effective susceptible fractions** for perfect or single-shot vaccine coverage. That work rules out novelty claims based solely on the idea that concentrated vaccination can beat fair vaccination under cross-group mixing. The present fixed *recurrent dose-rate* constraint has a nonlinear map from rates to susceptibility; in fact the explicit example has strict local curvature opposite to a naive concentration heuristic. The difference in cost coordinates prevents the published concavity statement from implying the present local/global result.

Duijzer and collaborators [3] study dose-optimal vaccination for separate SIR populations and final epidemic size, not this interacting-renewal next-generation spectral factor. These distinctions do not establish publication priority against every possible broader optimization theorem.

## Limitations

All claims refer to the stated symmetric two-group model, a sharp immunity-loss age, fixed positive budget, and one of the two explicitly specified renewal laws. Strict local/global nonconvexity is proved only for the displayed concrete parameters; it does **not** characterize the globally optimal allocation for every disassortative model. The equality \(\alpha=\alpha_c(c)\) has a vanishing second derivative and is left unclassified. Endpoint no-vaccination regimes are limiting renewal policies. The effect of epidemic stochasticity, vaccination uptake, side effects, differing costs, unequal population sizes, other immunity curves and dynamic outbreak severity is not treated. Full publication priority requires independent scrutiny of wider vaccination optimization literature.

## References

[1] F. Foutel-Rodier, A. Charpentier and H. Guérin, *Optimal Vaccination Policy to Prevent Endemicity: A Stochastic Model*, arXiv:2306.13633 (first public 23 June 2023), Section 5 and Proposition 6; Journal of Mathematical Biology 90, 10 (2025), DOI:10.1007/s00285-024-02171-z. https://arxiv.org/html/2306.13633v3

[2] J.-F. Delmas, D. Dronnier and P.-A. Zitt, *Optimal vaccination: Various (counter) intuitive examples*, arXiv:2112.08756 (2021), Section 4, especially Proposition 4.1. https://arxiv.org/html/2112.08756v1

[3] L. E. Duijzer, W. L. van Jaarsveld, J. Wallinga and R. Dekker, *Dose-Optimal Vaccine Allocation over Multiple Populations*, Production and Operations Management 27 (2018), 143–159, DOI:10.1111/poms.12788.
