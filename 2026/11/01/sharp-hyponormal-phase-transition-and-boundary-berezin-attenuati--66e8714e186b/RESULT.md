# Sharp hyponormal phase transition and boundary Berezin attenuation for oscillatory Bergman Toeplitz shifts

## Finding
Let \(A^2(\mathbb D)\) be the analytic Bergman Hilbert space with normalized area measure, let \(k\in\mathbb N\) with \(k\ge1\), and let \(\tau\in\mathbb R\). Define
\[
T_{k,\tau}=P\bigl(z^k(1-|z|^2)^{i\tau}\,\cdot\bigr),\quad
L_\tau=|\Gamma(1+i\tau)|,\quad
B_\tau=|\Gamma(1+i\tau)\Gamma(2-i\tau)|.
\]
Then
\[
\|T_{k,\tau}\|_{\mathrm{ess}}=L_\tau,\qquad
T_{k,\tau}\text{ hyponormal}\ \Longleftrightarrow\ \tau^2\le k
\ \Longleftrightarrow\ \|T_{k,\tau}\|=L_\tau.
\]
For the normalized Bergman reproducing kernel \(\kappa_z\), the Berezin transform \(\widetilde T_{k,\tau}(z)=\langle T_{k,\tau}\kappa_z,\kappa_z\rangle\) satisfies, uniformly in \(|\zeta|=1\),
\[
\lim_{r\uparrow1}\frac{\widetilde T_{k,\tau}(r\zeta)}{\zeta^k(1-r^2)^{i\tau}}
=\Gamma(1+i\tau)\Gamma(2-i\tau).
\]
In particular, \(\lim_{r\uparrow1}|\widetilde T_{k,\tau}(r\zeta)|=B_\tau\), and the exact boundary-Berezin attenuation ratio is
\[
\frac{B_\tau}{\|T_{k,\tau}\|_{\mathrm{ess}}}
=\sqrt{1+\tau^2}\,|\Gamma(1+i\tau)|
=\prod_{j=2}^{\infty}\left(1+\frac{\tau^2}{j^2}\right)^{-1/2}.
\]
This ratio is strictly below one for \(\tau\ne0\), independent of angular degree \(k\). Along \(\tau=\sqrt{k}\), all these operators are hyponormal, with \(\|T_{k,\sqrt{k}}\|=\|T_{k,\sqrt{k}}\|_{\mathrm{ess}}\) but
\[
\frac{B_{\sqrt{k}}}{\|T_{k,\sqrt{k}}\|_{\mathrm{ess}}}
\sim\sqrt{2\pi}\,k^{3/4}e^{-\pi\sqrt{k}/2}\longrightarrow0.
\]
Consequently there is no positive universal lower bound on normalized **boundary** Berezin modulus even within this norm-essential-norm-matching hyponormal Toeplitz family.

## Assumptions and scope
The area measure is \(dA=\pi^{-1}dx\,dy\), \(P\) is Bergman orthogonal projection, and \(\{e_n=\sqrt{n+1}z^n:n\ge0\}\) is the orthonormal monomial basis. On \(\mathbb D\), the phase \((1-|z|^2)^{i\tau}\) uses the ordinary real logarithm; it has modulus one. Assigning any boundary values does not affect the operator. Hyponormal means \(T^*T-TT^*\ge0\). The essential norm is distance to the compact operators, and the Berezin transform uses normalized kernels. The comparison is with the **boundary** modulus; no claim is made that the global Berezin number \(\sup_{z\in\mathbb D}|\widetilde T(z)|\) has the same small ratio.

## Proof
**1. Exact weighted shift.** Angular orthogonality and the beta integral yield \(T_{k,\tau}e_n=a_ne_{n+k}\), where
\[
a_n=\sqrt{\frac{n+1}{n+k+1}}\,
\frac{\Gamma(1+i\tau)\Gamma(n+k+2)}{\Gamma(n+k+2+i\tau)},
\qquad
|a_n|^2=\frac{n+1}{n+k+1}
\prod_{j=1}^{n+k+1}\frac{j^2}{j^2+\tau^2}.
\]
The Euler product gives \(\lim_{n\to\infty}|a_n|=L_\tau\). Multiplying the basis by unimodular factors eliminates all phases of the nonzero \(a_n\); alternatively the shift has the same essential norm as its positive-weight version. The difference between that version and \(L_\tau S^k\) is a compact weighted shift, since its weights tend to zero. The essential norm of \(S^k\) is one (its action on an infinite orthonormal sequence precludes compact approximation below one), so \(\|T_{k,\tau}\|_{\mathrm{ess}}=L_\tau\).

**2. Sharp hyponormal transition.** The exact adjacent weight ratio is
\[
\frac{|a_{n+1}|^2}{|a_n|^2}
=\frac{(n+2)(n+k+1)(n+k+2)}{(n+1)((n+k+2)^2+\tau^2)}.
\]
Consequently
\[
|a_{n+1}|\ge|a_n|
\quad\Longleftrightarrow\quad k(n+k+2)\ge(n+1)\tau^2.
\]
For \(\tau^2\le k\), the right-hand inequality holds at every \(n\), so weights increase. The self-commutator is diagonal:
\[
(T^*T-TT^*)e_n=(|a_n|^2-|a_{n-k}|^2)e_n,
\]
where \(a_j=0\) for \(j<0\). Thus the operator is hyponormal. The weight supremum is its limit \(L_\tau\), hence \(\|T\|=L_\tau\). Conversely, if \(\tau^2>k\), the inequality reverses for all sufficiently large \(n\); then \(|a_{n+k}|<|a_n|\) eventually, making the self-commutator negative on infinitely many basis vectors. The eventually strictly decreasing weights converge to \(L_\tau\) from above, hence \(\|T\|>L_\tau\). This proves both equivalences, including the equality boundary \(\tau^2=k\).

**3. Exact boundary Berezin factor.** Write \(\kappa_z(w)=(1-|z|^2)/(1-\bar zw)^2\). For fixed \(z=r\zeta\), the disk automorphism \(w=(z-v)/(1-\bar zv)\) transports the measure \(|\kappa_z(w)|^2dA(w)\) exactly to normalized \(dA(v)\). Also
\[
1-|w|^2=(1-r^2)\frac{1-|v|^2}{|1-r\bar\zeta v|^2}.
\]
Upon division by \(\zeta^k(1-r^2)^{i\tau}\), the Berezin integrand has absolute value at most one and tends almost everywhere to \(((1-|v|^2)/|1-\bar\zeta v|^2)^{i\tau}\). Dominated convergence gives a limit independent of \(\zeta\):
\[
I_\tau=\int_\mathbb D\left(\frac{1-|v|^2}{|1-v|^2}\right)^{i\tau}\,dA(v).
\]
Expanding the two binomial factors and integrating angular and radial variables gives the absolutely convergent Gauss series
\[
I_\tau=\frac1{1+i\tau}\,{}_2F_1(i\tau,i\tau;2+i\tau;1).
\]
Gauss summation applies because \(\operatorname{Re}(2+i\tau-2i\tau)=2>0\) and yields
\[
I_\tau=\Gamma(1+i\tau)\Gamma(2-i\tau).
\]
Rotational covariance makes the convergence uniform in \(\zeta\), since the normalized ratio in the displayed limit is in fact independent of \(\zeta\) for every \(r\).

**4. Attenuation and critical asymptotics.** The identity \(\Gamma(2-i\tau)=(1-i\tau)\Gamma(1-i\tau)\) yields \(B_\tau=\sqrt{1+\tau^2}L_\tau^2\). The Euler product for \(\sinh\) gives \(L_\tau^2=\pi|\tau|/\sinh(\pi|\tau|)\) (continuous at zero), hence the infinite product in the finding, strictly below one when \(\tau\ne0\). With \(\tau=\sqrt{k}\), the exact hyponormal criterion is met and the standard \(\sinh\)-asymptotic gives \(\sqrt{2\pi}k^{3/4}e^{-\pi\sqrt{k}/2}(1+o(1))\), completing the proof.

## Verification
The accompanying `phase_toeplitz_check.py` tests the exact shift weights against independent gamma-function evaluations, adjacent-weight inequalities across both sides of the threshold, the Gauss constant, the strict attenuation inequality, and finite-radius Berezin series convergence. It reports 472 passed finite assertions with Python and SciPy; these are supplementary checks, not proofs of limits, infinite products, or global operator properties. Run with `python phase_toeplitz_check.py` after installing `requirements.txt`.

## Relationship to prior work
Looi (2026), Sections 3.1–3.3 (particularly Propositions 3.3–3.4 and Remark 3.7), establishes the distinct diagonal-versus-Berezin oscillatory attenuation mechanism for **real-valued radial** Bergman Toeplitz symbols, and supplies a parametrized oscillation frequency. The gamma attenuation mechanism is therefore not claimed new in isolation. Le and Simanek (2020) study hyponormality for weighted shifts with diagonal perturbations, and Kim and Lee (2022) examine nonharmonic polynomial symbols. The result here is the combined **nonradial complex-power family**, its exact sharp \(\tau^2=k\) hyponormality threshold, the equivalent norm/essential-norm transition, and the vanishing normalized boundary-Berezin ratio **inside the hyponormal class**. Classical quasihomogeneous Bergman Toeplitz beta/Mellin methods underlie the shift calculation. Searches and source inspections did not identify a prior statement implying this combined theorem; that is a best-knowledge claim, not proof of publication priority.

## Limitations
Only the standard one-variable unweighted Bergman Hilbert space and positive integer angular degrees are addressed. No assertion concerns a uniform bound on the entire Berezin number, positivity of the self-adjoint real part, higher-dimensional balls, or arbitrary symbols. The limit concerns modulus at the boundary, and the symbol is not boundary-continuous when \(\tau\ne0\). Unindexed or inaccessible literature could contain an equivalent formulation. No independent audit has been performed.

## References
- Sam Looi, *The Berezin liminf criterion fails for radial Toeplitz operators*, arXiv:2603.10879 (first posted March 11, 2026), Sections 3.1–3.3. https://arxiv.org/abs/2603.10879
- Trieu Le and Brian Simanek, *Hyponormal Toeplitz Operators on Weighted Bergman Spaces*, arXiv:2003.07330 (first posted March 16, 2020). https://arxiv.org/abs/2003.07330
- Sumin Kim and Jongrak Lee, *Hyponormal Toeplitz operators with non-harmonic symbols on the weighted Bergman spaces*, Annals of Functional Analysis 14 (2023), article 14; online December 4, 2022. https://doi.org/10.1007/s43034-022-00241-1
- *Toeplitz Operators with Quasihomogeneous Symbols on the Bergman Space of the Unit Ball* (2012). https://doi.org/10.1155/2012/414201
