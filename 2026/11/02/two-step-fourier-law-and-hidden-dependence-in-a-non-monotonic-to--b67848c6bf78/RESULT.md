# Two-step Fourier law and hidden dependence in a non-monotonic toral shear

## Finding

For the Lebesgue-stationary toral shear family of Myers Hill, Sturman and Wilson, the first-coordinate observations at times zero and one are independent Haar-uniform variables, and their circular displacement at time two is also exactly Haar-uniform. Nevertheless, the first-coordinate observations at times zero and two are dependent for **every** positive shear-fold parameter in the family. A complete, explicitly factorized formula for **all** two-time Fourier coefficients establishes these assertions, quantifies their departure from the linear cat-map endpoint and separates two otherwise easily confused mixing diagnostics.

Write \(\mathbb T=\mathbb R/\mathbb Z\), let \(0<\eta<1/2\), and define
\[
f_\eta(y)=\begin{cases}y/(1-\eta),&0\le y\le1-\eta,\\ (1-y)/\eta,&1-\eta<y<1,\end{cases}
\qquad H_\eta(x,y)=(x+f_\eta(y),\ y+x+f_\eta(y))\pmod1.
\]
For a Haar-distributed initial point \((X_0,Y_0)\in\mathbb T^2\), write \((X_j,Y_j)=H_\eta^j(X_0,Y_0)\) and, for every pair of integers \(k,\ell\), define
\[
C_\eta(k,\ell)=\mathbb E\,e^{2\pi i(kX_2-\ell X_0)}.
\]
Let \(E(t)=\int_0^1e^{2\pi itz}\,dz\) for real \(t\), with \(E(0)=1\), and set
\[
J_\eta(m,r)=(1-\eta)E(r+m(1-\eta))+\eta E(r-m\eta).
\]
Then, for all \(k,\ell\in\mathbb Z\),
\[
\boxed{C_\eta(k,\ell)=J_\eta(k-\ell,k)J_\eta(\ell-k,\ell).}
\]
The removable-singularity-safe definition above applies at every integer frequency and every permitted parameter. In particular, for each nonzero integer \(k\),
\[
\boxed{C_\eta(k,k)=0,\qquad C_\eta(k,-k)=|J_\eta(2k,k)|^2.}
\]
Consequently \(X_2-X_0\pmod1\) is uniform, while
\[
\boxed{\mathbb E\,e^{2\pi i(X_2+X_0)}
=\frac{\sin^2(2\pi\eta)}{\pi^2(3-2\eta)^2(1-2\eta)^2}>0.}
\]
A low-order unequal-frequency mixed moment is also explicit:
\[
\boxed{\mathbb E\,e^{2\pi i(X_2-2X_0)}
=-\frac{2\sin^2(\pi\eta)}{\pi^2\eta(1+\eta)(2-\eta)(3-\eta)}
=-\frac\eta3+O(\eta^2)\quad(\eta\downarrow0).}
\]
Thus the joint law of \((X_0,X_2)\) is not Haar product for any \(0<\eta<1/2\), even though both marginals are Haar and their circular difference is uniform. At the endpoint \(\eta=0\), interpreted as the cat map, \((X_0,X_2)\) **is** independent Haar; hence independence of these two observations holds if and only if \(\eta=0\) on the half-closed parameter range \([0,1/2)\). Moreover,
\[
d_{\mathrm{TV}}\!\left(\mathcal L(X_0,X_2),\lambda_{\mathbb T}\otimes\lambda_{\mathbb T}\right)
\ge \frac{\sin^2(\pi\eta)}{\pi^2\eta(1+\eta)(2-\eta)(3-\eta)}
=\frac\eta6+O(\eta^2).
\]
Here total variation is the supremum of the absolute difference of probabilities over measurable sets.

## Assumptions and scope

The state space is \(\mathbb T^2\) with normalized Haar (Lebesgue) probability measure. Initial coordinates are jointly Haar, not prescribed deterministically; all expectations are with respect to this measure. Frequencies \(k,\ell,m,r\) are integers unless \(E(t)\) is evaluated at real \(t\). The two-time result is at the fixed horizon of exactly two iterations, for every \(0<\eta<1/2\), including parameters where long-time mixing has not been established. The endpoint \(\eta=0\) is treated separately by its linear cat-map definition. No claim about all time lags, exponential mixing, or a central limit theorem is made.

The two component maps are invertible Haar-preserving shears, so their composition \(H_\eta\) preserves Haar measure; no hyperbolicity argument is needed here. The tent shear \(f_\eta\) pushes uniform Lebesgue measure on \([0,1]\) to uniform Lebesgue measure: each \(t\in(0,1)\) has two inverse images, contributing Jacobian weights \(1-\eta\) and \(\eta\).

## Proof

**Step 1: independent shear coordinates.** Put \(x=X_0\), \(y=Y_0\), \(u=X_1=x+f_\eta(y)\pmod1\), and \(v=Y_1=y+u\pmod1\). Conditional on \(y\), translation \(x\mapsto u\) preserves Haar, so \(y,u\) are independent Haar. Then \((y,v)=(y,y+u)\) is also independent Haar. In these independent coordinates,
\[
X_0=u-f_\eta(y)=v-y-f_\eta(y)\pmod1,\qquad
X_2=u+f_\eta(v)=v-y+f_\eta(v)\pmod1.
\]
In particular, \(X_1=X_0+f_\eta(Y_0)\pmod1\). As \(X_0\) and \(f_\eta(Y_0)\) are independent Haar, \(X_0\) and \(X_1\) are independent Haar.

**Step 2: factorization of the complete two-time spectrum.** For any integers \(k,\ell\), characters ignore integer choices of representatives, and
\[
kX_2-\ell X_0\equiv (k-\ell)v+k f_\eta(v)
+(\ell-k)y+\ell f_\eta(y)\pmod1.
\]
Independence of \(y\) and \(v\) factors its exponential expectation into
\[
C_\eta(k,\ell)
=\left(\int_0^1e^{2\pi i((k-\ell)t+k f_\eta(t))}\,dt\right)
\left(\int_0^1e^{2\pi i((\ell-k)t+\ell f_\eta(t))}\,dt\right).
\]
Splitting each integral at \(1-\eta\), substituting \(t=(1-\eta)z\) on the first branch and \(t=1-\eta z\) on the second, gives
\[
\int_0^1e^{2\pi i(mt+r f_\eta(t))}\,dt
=(1-\eta)E(r+m(1-\eta))+\eta E(r-m\eta)=J_\eta(m,r).
\]
This proves the formula for every integer pair, including exceptional frequencies at which individual rational denominators would vanish.

**Step 3: explicit rational-trigonometric form.** For integer \(m,r\) whenever both bracketed factors below are nonzero, use \(e^{2\pi im}=e^{2\pi ir}=1\) to rewrite
\[
J_\eta(m,r)=
\frac{r(e^{-2\pi i m\eta}-1)}
{2\pi i\,[r+m(1-\eta)]\,[r-m\eta]}.
\]
Indeed the common-denominator numerator is exactly
\[
(1-\eta)(r-m\eta)+\eta(r+m(1-\eta))=r.
\]
The earlier integral representation, not this quotient, defines its values at removable singularities.

**Step 4: uniform displacement versus hidden dependence.** For nonzero \(k\), \(J_\eta(0,k)=\int_0^1e^{2\pi ik f_\eta(t)}dt=0\) because \(f_\eta\) pushes Haar to Haar. Therefore \(C_\eta(k,k)=J_\eta(0,k)^2=0\). All nonzero Fourier coefficients of the law of \(X_2-X_0\) vanish, which by uniqueness of Fourier coefficients of finite measures on the circle makes that difference exactly Haar-uniform.

For opposite frequencies, the reality of \(f_\eta\) gives \(J_\eta(-2k,-k)=\overline{J_\eta(2k,k)}\), and thus \(C_\eta(k,-k)=|J_\eta(2k,k)|^2\). Taking \(k=1\), where neither denominator vanishes when \(0<\eta<1/2\), yields
\[
J_\eta(2,1)=\frac{e^{-4\pi i\eta}-1}{2\pi i(3-2\eta)(1-2\eta)},
\quad |J_\eta(2,1)|^2=\frac{\sin^2(2\pi\eta)}{\pi^2(3-2\eta)^2(1-2\eta)^2}>0.
\]
If \(X_0\) and \(X_2\) were independent uniform, this mixed moment would vanish; hence they are not independent. Likewise evaluating the factorization at \((k,\ell)=(1,2)\) gives the displayed negative real coefficient and its Taylor expansion \(-\eta/3+O(\eta^2)\).

**Step 5: cat endpoint and distance bound.** At \(\eta=0\), \(H_0(x,y)=(x+y,x+2y)\pmod1\), so \(X_2=2X_0+3Y_0\pmod1\). Conditional on \(X_0\), the variable \(3Y_0\pmod1\) is Haar, establishing independence of \(X_0\) and \(X_2\) at this endpoint. Finally, for any complex-valued test function of modulus at most one, the expectation difference between two laws has modulus at most twice their total variation distance. Apply this to \(e^{2\pi i(X_2-2X_0)}\), whose Haar-product expectation is zero, and divide the explicit modulus by two. This gives the stated strict total-variation lower bound and its small-parameter expansion.

## Verification

The accompanying standalone `verification_checker.py` compares the exact coefficient formula against a separately implemented finite-grid integration over the **original** coordinates \((X_0,Y_0)\). It checks rational algebraic denominator identities, the two explicit low-frequency expressions, diagonal cancellation, three rational parameters and multiple positive, negative and unequal harmonics, and the leading linear asymptotic near \(\eta=0\). In the supplied environment the checker completed **398 comparisons**, with no discrepancies. This is supporting reproducibility evidence; the all-parameter, all-frequency theorem is the analytic argument above, not an extrapolation from grid samples.

Reproduction command: `python3 verification_checker.py` (Python standard library only). Grid comparisons have the explicit absolute tolerance `0.002`; the small-parameter ratio comparison has tolerance `0.004`. The reported theoretical exact formulas do not depend on these tolerances.

## Relationship to prior work

Myers Hill, Sturman and Wilson introduced the one-parameter family of non-monotonic toral shears and proved the Bernoulli property in two explicit parameter windows. Their preprint first appeared on 14 December 2021, followed by the open-access 2022 journal article. Their principal theorems concern asymptotic mixing, invariant cones and stable/unstable manifolds, not the full two-step coordinate Fourier law above. The existing cat-map and Cerbelli–Giona endpoint structures are used here only as established model context.

Related work of the same authors on **two** non-monotonic orthogonal shears, and on the orthogonal-tents endpoint, concerns different maps and long-time mixing rates; it does not by itself imply this exact interior-parameter two-time joint law. Exact transfer-operator, character-integration and shear-change-of-variables methods are standard; the specific parameter-uniform joint-spectrum identity and hidden-dependence classification are the mathematical assertions presented here. The absence of an identified identical statement in inspected literature is not a proof of exhaustive publication priority.

## Limitations

Only the two-step coordinate joint law is classified. Uniform circular displacement is weaker than independence, and neither claim determines asymptotic decay of correlations. The strict positivity and explicit lower bound hold throughout \(0<\eta<1/2\); the endpoint \(\eta=1/2\) is not part of the theorem statement. The total-variation estimate is a lower bound, not a claim of an optimal constant or an upper bound. The small-parameter \(O(\eta^2)\) concerns one specified Fourier coefficient, not the entire joint distribution. The underlying parameter family and long-time Bernoulli/mixing results are previously published. Independent mathematical audit and definitive publication-priority determination have not been performed.

## References

1. J. Myers Hill, R. Sturman, M. C. T. Wilson, *A Continuous Family of Non-Monotonic Toral Mixing Maps*, arXiv:2112.07346v1, first posted 14 December 2021. https://arxiv.org/abs/2112.07346
2. J. Myers Hill, R. Sturman, M. C. T. Wilson, *A Family of Non-Monotonic Toral Mixing Maps*, Journal of Nonlinear Science **32**, article 31 (2022). https://doi.org/10.1007/s00332-022-09790-0
3. S. Cerbelli and M. Giona, *A Continuous Archetype of Nonuniform Chaos in Area-Preserving Dynamical Systems*, Journal of Nonlinear Science **15** (2005), 387–421, as cited in [2]; background on the symmetric endpoint only.
