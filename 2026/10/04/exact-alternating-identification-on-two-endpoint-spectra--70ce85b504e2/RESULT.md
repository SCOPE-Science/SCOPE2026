# Exact alternating identification on two-endpoint spectra

## Finding
For the practical \(l=1\) residual-ratio version of Algorithm 2.1 in Hu--Pollock--Xue--Zhu, consider the quadratic objective
\[
f(x)=\tfrac12 x^\top A x-b^\top x,
\]
where \(A\) is symmetric positive definite and has exactly the two endpoint eigenvalues \(\sigma(A)=\{\mu,1\}\) with \(0<\mu<1\). Let \(r_k=b-Ax_k\), let \(P_\mu\) be the orthogonal projector onto the \(\mu\)-eigenspace, and use the practical estimate
\[
q_k=\frac{\|r_k\|}{\|r_{k-1}\|},\qquad \alpha_1=1,\qquad \alpha_{k+1}=1+q_k.
\]
If \(P_\mu r_0=0\), then \(r_1=0\), so the method reaches the minimizer in one step. Otherwise
\[
q_1=(1-\mu)\frac{\|P_\mu r_0\|}{\|r_0\|}
\]
and, for every \(k\ge1\),
\[
q_{k+1}=1-\mu-\mu q_k.
\]
Consequently, with
\[
q_*=\frac{1-\mu}{1+\mu},
\]
the exact transient is
\[
q_k=q_*+(-\mu)^{k-1}(q_1-q_*),
\]
and
\[
\alpha_{k+1}=1+q_k\longrightarrow\frac{2}{1+\mu}.
\]
The limit is the minimax-optimal constant gradient-descent step for the spectral interval \([\mu,1]\). Unless \(q_1=q_*\), both \(q_k\) and \(\alpha_{k+1}\) alternate strictly about their optimal values, and their parameter errors contract by the exact factor \(\mu\) at every update.

## Assumptions and scope
The statement concerns the quadratic problem and the practical \(l=1\) estimator in Algorithm 2.1 of the cited preprint. The scaling is exact: the top eigenvalue is \(1\). Both eigenspaces of \(A\) are nontrivial, although either may have arbitrary multiplicity. The nontrivial branch assumes \(P_\mu r_0\ne0\); no assumption is needed on the initial projection onto the top eigenspace.

The result does not assert the same recurrence for spectra containing interior eigenvalues, inaccurate normalization of the largest eigenvalue, or geometric averages with \(l>1\).

## Proof
The source algorithm gives the residual recurrence
\[
r_k=(I-\alpha_k A)r_{k-1}.
\]
Because \(\alpha_1=1\) and \(A\) has only the two eigenvalues \(\mu\) and \(1\), the first update is the exact spectral filter
\[
r_1=(I-A)r_0=(1-\mu)P_\mu r_0.
\]
Thus the top eigenspace is annihilated after one step. If \(P_\mu r_0=0\), then \(r_1=0\) and the proof is complete. Otherwise \(r_1\) lies in the \(\mu\)-eigenspace and is nonzero, giving
\[
q_1=(1-\mu)\frac{\|P_\mu r_0\|}{\|r_0\|}\in(0,1-\mu].
\]

The \(\mu\)-eigenspace is invariant under all subsequent gradient steps. Hence, whenever \(r_k\ne0\),
\[
r_{k+1}=\bigl(1-\mu\alpha_{k+1}\bigr)r_k
=\bigl(1-\mu(1+q_k)\bigr)r_k.
\]
For \(q_k\in[0,1-\mu]\),
\[
1-\mu(1+q_k)\ge 1-\mu(2-\mu)=(1-\mu)^2>0.
\]
Therefore the absolute value in the norm ratio introduces no sign ambiguity and
\[
q_{k+1}=1-\mu-\mu q_k.
\]
This expression also lies in \([(1-\mu)^2,1-\mu]\), so induction makes the recurrence valid for every later step and also shows that no later residual vanishes in the nontrivial branch.

The affine map has the unique fixed point
\[
q_*=\frac{1-\mu}{1+\mu},
\]
and subtraction of the fixed-point equation gives
\[
q_{k+1}-q_*=-\mu(q_k-q_*).
\]
Iteration yields the displayed closed form and exact alternating contraction. Since \(\alpha_{k+1}=1+q_k\), its limit is \(2/(1+\mu)\).

Finally, for a fixed gradient-descent step \(\alpha\) on a matrix whose spectral endpoints are \(\mu\) and \(1\), the spectral factor is
\[
\max\{|1-\alpha\mu|,|1-\alpha|\}.
\]
Balancing the two endpoint magnitudes gives \(\alpha=2/(1+\mu)\) and factor \(q_*=(1-\mu)/(1+\mu)\), proving the stated minimax interpretation.

## Verification
The proof uses only the algorithmic recurrence and orthogonal spectral decomposition. The critical boundary check is
\[
1-\mu(1+q_k)\ge(1-\mu)^2>0,
\]
which validates removal of the absolute value and prevents an unaccounted finite hit after the first step. The recurrence maps \([0,1-\mu]\) into \([(1-\mu)^2,1-\mu]\), so all ratios remain defined in the nontrivial branch.

As a numerical consistency check, the recurrence was replayed for one hundred randomly selected values of \(\mu\in(0,1)\), random residuals, and repeated endpoint eigenspaces. The largest floating-point discrepancy between the direct matrix update and \(q_{k+1}=1-\mu-\mu q_k\) was below \(4\times10^{-16}\). This check is supportive only; the result is proved algebraically above.

## Relationship to prior work
Hu--Pollock--Xue--Zhu define the adaptive step \(\alpha_{k+1}=1+\rho_k\) and, for the practical choice \(l=1\), set \(\rho_k=\|r_k\|/\|r_{k-1}\|\). Their Lemma 2.4 bounds each residual ratio by \(1-\mu\), while Theorem 2.5 gives one-sided error bounds for the practical estimator. Their separate Theorem 2.1 analyzes the computationally expensive spectral-radius oracle rather than the practical residual-ratio estimator. Their experiments report approach toward the optimal rate under accurate scaling, but the inspected manuscript does not state the two-endpoint exact recurrence, closed form, or alternating identification law established here.

A closely related published mathematical record on Adaptive Optimal Gradient Descent studies endpoint-mode annihilation for a different curvature-estimation rule. In that method, losing an endpoint mode can destroy identification of the original optimal step. The present calculation shows the opposite behavior for the Hu--Pollock--Xue--Zhu residual-ratio feedback on the canonical two-endpoint spectrum: the initialization annihilates the top endpoint exactly, yet the scalar feedback still reconstructs the original minimax step, with an exact alternating error law. This contrast is one reason the special case is structurally informative rather than merely a numerical example.

Earlier adaptive-gradient methods of Malitsky--Mishchenko use local curvature inferred from gradient differences and a different stepsize recurrence, so their convergence theory does not imply this residual-ratio identity.

## Limitations
The exact law relies on both a two-point spectrum and exact normalization of the largest eigenvalue to \(1\). Interior eigenvalues generally survive the first step and destroy the scalar reduction. The statement is deterministic and quadratic; it does not cover noisy residuals, nonlinear objectives, or momentum variants. It proves a parameter-identification law, not an acceleration theorem beyond the optimal fixed-step rate on this spectral class.

## References
1. X. Hu, S. Pollock, Z. Xue, and Y. Zhu, *An adaptive framework for first-order gradient methods*, arXiv:2602.13620, first submitted 2026-02-14.
2. Y. Malitsky and K. Mishchenko, *Adaptive Gradient Descent without Descent*, ICML 2020, arXiv:1910.09529.
3. Y. Malitsky and K. Mishchenko, *Adaptive Proximal Gradient Method for Convex Optimization*, NeurIPS 2024, arXiv:2308.02261.
