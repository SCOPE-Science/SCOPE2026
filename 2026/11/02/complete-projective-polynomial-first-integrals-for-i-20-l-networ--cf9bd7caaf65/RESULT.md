# Complete projective–polynomial first integrals for \(I_{20}^{(L)}\) networks

## Finding

For every integer \(L\ge1\) and \(N\ge L+2\), a common-coefficient \(N\)-particle flow of the imprimitive Lie family \(I_{20}^{(L)}\) has an explicit and **complete generic family** of \(2N-L-5\) independent rational first integrals. These involve ordinary projective cross-ratios of the \(x\)-coordinates and previously unrecorded, in the inspected work, normalized order-\(L+1\) divided differences of the \(y\)-coordinates. The sign of one distinguished divided difference and the labeled order of the \(x\)-coordinates complete the real connected-orbit classification.

More precisely, take distinct \(x_1,\ldots,x_N\) and, for every subset \(S\) of size \(L+2\), put
\[
\Delta_S=\sum_{i\in S}\frac{y_i}{\prod_{j\in S\setminus\{i\}}(x_i-x_j)}.
\]
Let \(S_0=\{1,\ldots,L+2\}\) and \(S_i=\{1,\ldots,L+1,i\}\) for \(i=L+3,\ldots,N\). On the open region \(\Delta_{S_0}\ne0\), define
\[
K_i=\frac{(x_i-x_1)(x_2-x_3)}{(x_i-x_3)(x_2-x_1)},
\quad i=4,\ldots,N,
\]
\[
J_i=\frac{\Delta_{S_i}}{\Delta_{S_0}}\frac{x_i-x_1}{x_{L+2}-x_1},
\quad i=L+3,\ldots,N.
\]
Empty index ranges contribute no invariants. All \(K_i,J_i\) are constant along every regular solution with common coefficients, even when those coefficients depend on the entire population state. They are independent, number exactly \(2N-L-5\), and separate all positive-denominator projective–polynomial group orbits once labeled \(x\)-order and \(\operatorname{sgn}\Delta_{S_0}\) agree.

The stronger exact relative-invariant law is
\[
\boxed{\dot\Delta_S=\bigl(D-(L+1)B-C\sum_{i\in S}x_i\bigr)\Delta_S.}
\]

## Assumptions and scope

The number of nodes \(N\) and polynomial degree \(L\) are integers satisfying \(L\ge1\) and \(N\ge L+2\). For each \(i=1,\ldots,N\), consider
\[
\begin{aligned}
\dot x_i&=A(t,\mathbf x,\mathbf y)+B(t,\mathbf x,\mathbf y)x_i+C(t,\mathbf x,\mathbf y)x_i^2,\\
\dot y_i&=[D(t,\mathbf x,\mathbf y)+L C(t,\mathbf x,\mathbf y)x_i]y_i
 +\sum_{k=0}^{L}E_k(t,\mathbf x,\mathbf y)x_i^k.
\end{aligned}
\]
All coefficients are shared by all nodes at any fixed time, are continuous in time and locally Lipschitz in the full state, and allow the ordinary solution to exist on the time interval under consideration. No particular mean-field formula, autonomy, periodicity, or small-coupling hypothesis is required. Initial \(x_i\) are pairwise distinct and \(\Delta_{S_0}\ne0\). Statements are restricted to finite real portions of the solution; no crossing of a projective infinity chart is asserted.

A *positive-denominator projective–polynomial transformation* is a transformation on a specified finite configuration of the form
\[
x\mapsto\frac{a x+b}{c x+d},\qquad
 y\mapsto\frac{\lambda y+Q(x)}{(cx+d)^L},
\]
where \(ad-bc=1\), \(\lambda>0\), \(\deg Q\le L\), and \(cx_i+d>0\) at every labeled node. This is a pole-free component of the action in the source's \(I_{20}^{(L)}\) normal form. The completeness assertion is about these transformations, not arbitrary disconnected projective continuations.

## Proof

**1. Preservation of distinctness and the difference law.** For any \(i\ne j\), cancellation of the common coefficient \(A\) gives
\[
\frac{d}{dt}(x_i-x_j)=[B+C(x_i+x_j)](x_i-x_j).
\]
Thus a nonzero difference cannot vanish during a finite regular flow, and the labeled order of the \(x_i\) remains fixed. In particular, all displayed rational quantities stay well-defined if their initial denominators are nonzero.

**2. Relative-invariant evolution.** Fix \(S\) with \(|S|=L+2\), and set \(w_i=\prod_{j\in S\setminus\{i\}}(x_i-x_j)^{-1}\). Differentiating the differences yields
\[
\frac{\dot w_i}{w_i}=-(L+1)B-C\left(L x_i+\sum_{j\in S}x_j\right).
\]
Consequently
\[
\frac{d}{dt}(w_i y_i)
=\left(D-(L+1)B-C\sum_{j\in S}x_j\right)w_i y_i
 +w_i\sum_{k=0}^{L}E_kx_i^k.
\]
For any polynomial \(P\) of degree at most \(L\), the coefficient of degree \(L+1\) in its interpolation polynomial on the \(L+2\) distinct abscissae is zero, so
\[
\sum_{i\in S}w_i P(x_i)=0.
\]
Summing the preceding identity proves the stated exact equation for \(\Delta_S\). It also proves \(\Delta_{S_0}(t)=\Delta_{S_0}(0)\exp\!\left(\int_0^t [D-(L+1)B-C\sum_{j\in S_0}x_j]ds\right)\); hence its sign cannot change or pass through zero on a regular solution.

**3. All rational first integrals.** Applying the logarithmic difference law in Step 1 to the four factors defining \(K_i\) shows that all terms involving \(B\) and \(C\) cancel. For a fiber invariant, Step 2 gives
\[
\frac{d}{dt}\left(\frac{\Delta_{S_i}}{\Delta_{S_0}}\right)
=-C(x_i-x_{L+2})\frac{\Delta_{S_i}}{\Delta_{S_0}}.
\]
Step 1 also gives
\[
\frac{d}{dt}\left(\frac{x_i-x_1}{x_{L+2}-x_1}\right)
=C(x_i-x_{L+2})\frac{x_i-x_1}{x_{L+2}-x_1}.
\]
Multiplication proves \(\dot J_i=0\), including when \(\Delta_{S_i}=0\), without taking logarithms of a possibly zero quantity. These calculations remain valid for arbitrary shared state-dependent coefficients.

**4. Covariance under the full finite transformation.** Write \(H_i=cx_i+d>0\). Since \(ad-bc=1\), transformed differences satisfy
\[
x'_i-x'_j=\frac{x_i-x_j}{H_iH_j}.
\]
For every \(|S|=L+2\), the weight denominator in the divided difference therefore acquires \(H_i^{L}\prod_{j\in S}H_j\), cancelling the \(H_i^{-L}\) in \(y'_i\). The polynomial \(Q\) drops out by the interpolation identity from Step 2, yielding
\[
\Delta'_S=\lambda\left(\prod_{j\in S}H_j\right)\Delta_S.
\]
The same difference relation preserves each cross-ratio \(K_i\); in the normalized \(J_i\), the ratio \(H_i/H_{L+2}\) from the two divided differences cancels the inverse ratio from \((x'_i-x'_1)/(x'_{L+2}-x'_1)\). Thus all invariants and the sign of \(\Delta_{S_0}\) are preserved under positive-denominator transformations.

**5. Converse orbit separation.** Consider two configurations satisfying the assumptions, with identical labeled \(x\)-order, identical \(K_i\), identical \(J_i\), and the same sign of \(\Delta_{S_0}\). There is a unique fractional-linear map carrying the first three distinct \(x\)-abscissae to their targets; equality of all \(K_i\) forces it to carry every other abscissa to its target. Because every labeled pair has the same order in both configurations and the determinant is positive, its denominators at the nodes all have the same sign. Choose the determinant-one matrix representative with positive denominators \(H_i\).

Define
\[
\lambda=\frac{\Delta'_{S_0}}{\Delta_{S_0}\prod_{j\in S_0}H_j}>0.
\]
For \(i=1,\ldots,L+1\), interpolate the unique polynomial \(Q\) of degree at most \(L\) through the prescribed values
\[
Q(x_i)=H_i^L y'_i-\lambda y_i.
\]
The covariance equation for \(S_0\) forces the transformed \(y_{L+2}\) to equal its target, since that variable has a nonzero coefficient in \(\Delta_{S_0}\). For each \(i>L+2\), equality of \(J_i\), with the already-matched abscissae and \(\Delta_{S_0}\), forces equality of \(\Delta_{S_i}\) and hence equality of transformed \(y_i\). Thus the constructed transformation maps the entire first configuration to the second. Conversely, Step 4 proves necessity. This is an *if and only if* classification for the stated regular group component.

**6. Independence, exact count and reconstruction.** Use the \(3\) coordinates \(x_1,x_2,x_3\), the \(L+2\) coordinates \(y_1,\ldots,y_{L+2}\), and all \(K_i,J_i\) as a new coordinate system. Each remaining \(x_i\) is rationally recovered from \(K_i\) and the first three abscissae. Then \(\Delta_{S_0}\) is known, and each \(J_i\) determines \(\Delta_{S_i}\), whose only still-unknown ordinate is \(y_i\) with nonzero coefficient \(\prod_{j=1}^{L+1}(x_i-x_j)^{-1}\). Thus the coordinate change is rationally invertible on its domain. The \(K_i,J_i\) are functionally independent, numbering
\[
(N-3)+(N-L-2)=2N-L-5.
\]
The remaining \(3+(L+2)=L+5\) coordinates parametrize the positive-denominator group orbit, confirming completeness. This remains valid for \(N=L+2\), when the \(J\)-family is empty.

## Verification

The standalone `verify_invariants.py` uses only Python's standard library and exact rational arithmetic. From the accompanying package, run `python3 verify_invariants.py`. It performs 100 finite transformation checks over degrees \(L=1,\ldots,5\), verifies cross-ratio and normalized divided-difference invariance and the exact covariance multiplier, performs centered finite-difference dynamical checks for \(L=1,2,3\), and checks 240 exact rational instances of the differentiated divided-difference identity for \(L=1,\ldots,6\). Successful execution prints three PASS lines.

These experiments are finite diagnostics; the identity, complete orbit separation, and independence for all \(N,L\) are proved analytically in Steps 1–6. No computer-assisted infinite certificate or external validation is claimed.

For a small explicit example, set \(L=1\), \(N=4\), \(x=(0,1,2,3)\), and \(y=(0,0,1,1)\). Then \(\Delta_{\{1,2,3\}}=1/2\), \(K_4=-3\) and \(J_4=1/2\). The second invariant records information not determined by the projective \(x\)-cross-ratio alone.

## Relationship to prior work

Tokunaga's 2026 classification supplies the \(I_{20}^{(L)}\) normal form, its finite group action and the group dimension \(L+5\); those facts are foundational, not claimed as new here [1]. Martens and Dharmavaram supply the general mean-field Lie–Scheffers reduction and explicit constants for scalar Riccati, quasi-linear and Bernoulli examples, including classical cross-ratios [2]. Campoamor-Stursberg and coauthors establish general methods for mixed superposition rules and imprimitive Lie systems [3]. The present contribution is the explicit, *full and separating* many-node rational invariant family for the two-variable projective–polynomial normal form: its nontrivial divided-difference component, exact relative-invariant law, real sign/order conditions, and elementary reconstruction. The inspected prior texts do not state this specific theorem; standard interpolation and projective identities remain acknowledged ingredients. Independent historical-priority verification is outstanding.

## Limitations

Only the open subset with pairwise distinct \(x_i\) and \(\Delta_{S_0}\ne0\) is classified. Collision strata, the algebraic hypersurface \(\Delta_{S_0}=0\), and other projective charts need separate analysis. These first integrals do not by themselves solve the remaining \(L+5\)-dimensional group equations or guarantee global existence. The real orbit separation uses positive-denominator transformations (the component accessible without crossing a pole), not arbitrary disconnected continuations of the projective action. The result does not imply any global attracting or chaotic behavior. Originality remains subject to independent expert scrutiny, particularly against older specialized invariant-theory literature.

## References

[1] K. Tokunaga, *Low-Dimensional Reduction of Mean-Field Coupled Dynamical Systems with Units Described by Two Real Variables: Classification and Applications*, arXiv:2610.28715v1, first posted 2026-10-20. https://arxiv.org/html/2610.28715v1

[2] E. A. Martens and S. Dharmavaram, *Lie Meets Network Dynamics: Exact Macroscopic Reductions (Finite Systems)*, arXiv:2607.12210v1, first posted 2026-07-13. https://arxiv.org/html/2607.12210v1

[3] R. Campoamor-Stursberg, O. Carballal, F. J. Herranz and J. de Lucas, *Mixed Superposition Rules for Lie Systems and Compatible Geometric Structures*, arXiv:2511.01063v1, first posted 2025-11-02. https://arxiv.org/html/2511.01063v1

[4] A. González-López, N. Kamran and P. J. Olver, *Lie Algebras of Vector Fields in the Real Plane*, Proc. London Math. Soc. 64 (1992), 339–368, DOI:10.1112/plms/s3-64.2.339. The classification is background; full text was not obtained for this comparison.
