# Sharp tracial crossed-Heinz stability for common two-point spectra

## Finding
Let \((\mathcal M,\tau)\) be a finite tracial von Neumann algebra with a faithful normal finite trace \(\tau\), let \(a>b>0\), let \(0<t<1\), and let \(P,Q\in\mathcal M\) be arbitrary orthogonal projections (not necessarily commuting). Set
\[
\delta=a-b,\quad A=b1+\delta P,\quad B=b1+\delta Q,\quad C_t=A^tB^{1-t}+B^tA^{1-t},
\]
\[
d_t=(a^t-b^t)(a^{1-t}-b^{1-t}),\qquad L=(\sqrt a+\sqrt b)^2.
\]
Then the **largest constant uniform over all finite tracial von Neumann algebras and their projection pairs** in the crossed-Heinz trace-deficit estimate is
\[
\boxed{\tau(A+B)-\|C_t\|_{1,\tau}\ \ge\ \Gamma_{\mathrm{tr}}(a,b,t)\|A-B\|_{2,\tau}^{2}},
\qquad \boxed{\Gamma_{\mathrm{tr}}(a,b,t)=\frac{\min\{d_t,L/2\}}{\delta^2}}.
\]
The conventions are \(\|Z\|_{1,\tau}=\tau(|Z|)\) and \(\|Z\|_{2,\tau}^2=\tau(Z^*Z)\). Every value of the constant is attained by rank-one projection pairs inside \(M_2(\mathbb C)\). In the regime \(d_t>L/2\), the sharp tracial constant is strictly larger than the sharp Loewner-order coefficient \(\min\{d_t,L-d_t\}/\delta^2\) obtained by Sababheh and Bourin.

## Assumptions and scope
No dimension, commutativity, rank, or spectral-gap assumption is imposed on \(P,Q\); \(\tau(1)<\infty\) guarantees that all trace expressions are finite. The constant is universal across algebras containing the test pair, not necessarily optimal within each fixed algebra (for example, an abelian algebra has a stronger constant). The classification is a tracial-norm result, not an improvement of the already-sharp Loewner inequality. At \(P=Q\), both sides vanish.

## Proof
**1. Polynomial reduction.** Put \(X=P+Q\), \(R=P-Q\), and \(u(X)=X(2- X)\). Projection identities give
\[
R^2=P+Q-PQ-QP=u(X),\qquad R(X-1)=-(X-1)R.
\]
Functional calculus for the two-point spectra of \(A,B\) yields
\[
A+B-C_t=(A^t-B^t)(A^{1-t}-B^{1-t})=d_t R^2.
\]
Thus \(C_t=s(X)-d_tu(X)\) is self-adjoint, where \(s(x)=2b+\delta x\), \(0\le x\le2\). The difference norm is \(\|A-B\|_{2,\tau}^{2}=\delta^2\tau(u(X))\). Also \(0<d_t<a+b\), since \(d_t=a+b-a^tb^{1-t}-a^{1-t}b^t\).

**2. Intrinsic spectral reflection.** Let \(E=1_{\{u(X)>0\}}\), and let \(U=\operatorname{sgn}(R)\), the polar sign of the self-adjoint operator \(R\). Since \(R^2=u(X)\), \(U^2=E\); \(U\) commutes with functions of \(u(X)\), and the anticommutation identity in Step 1 gives
\[
U(X-1)U=-(X-1)E,\qquad UXU=(2-X)E.
\]
Consequently \(\tau(E f(X))=\tau(E f(2-X))\) for every bounded Borel function \(f\) on \([0,2]\). This remains valid for continuous-spectrum pairs of projections; no discrete two-projection decomposition is required.

**3. Exact trace-deficit pairing.** For \(x\in[0,2]\) put
\[
h(x)=s(x)-|s(x)-d_tu(x)|,\quad x_{\mathrm{lo}}=1-|x-1|,\quad x_{\mathrm{hi}}=1+|x-1|.
\]
Because \(s(x_{\mathrm{hi}})\ge a+b>d_t\ge d_tu(x)\), the high branch is positive. Hence
\[
\frac{h(x)+h(2-x)}2=\min\{d_tu(x),\ s(x_{\mathrm{lo}})\}
=\min\{d_tu(x),\ a+b-\delta|x-1|\}.
\]
Outside \(E\), the spectrum of \(X\) is contained in \(\{0,2\}\), so both the trace defect and \(u(X)\) vanish. Averaging over \(E\) by Step 2 gives the exact identity
\[
\boxed{\tau(A+B)-\tau(|C_t|)=
\tau\!\left(\min\{d_tu(X),\ (a+b)1-\delta|X-1|\}\right).}
\]
Here \(\min\) is the pointwise functional-calculus minimum of two commuting self-adjoint functions of \(X\), not an arbitrary operator minimum.

**4. Sharp scalar lower bound.** Write \(L=(\sqrt a+\sqrt b)^2\). Direct expansion, valid on \([0,2]\), shows
\[
2s(x)-Lu(x)=\big((\sqrt a+\sqrt b)x-2\sqrt b\big)^2\ge0.
\]
Therefore \(s(x_{\mathrm{lo}})\ge(L/2)u(x)\). Applying this pointwise to Step 3 yields
\[
\tau(A+B)-\tau(|C_t|)\ge\min\{d_t,L/2\}\tau(u(X))
=\Gamma_{\mathrm{tr}}(a,b,t)\|A-B\|_{2,\tau}^2.
\]

**5. Attainment in both parameter regions.** Suppose \(d_t\le L/2\). In \(M_2(\mathbb C)\), take \(P=\operatorname{diag}(1,0)\) and \(Q=\operatorname{diag}(0,1)\). Then \(X=1\), \(u(X)=1\), and the ratio of the trace defect to \(\|A-B\|_2^2\) equals \(d_t/\delta^2\).

Suppose \(d_t>L/2\). Put
\[
r_*=(\sqrt a-\sqrt b)/(\sqrt a+\sqrt b),\qquad
P=\begin{pmatrix}1&0\\0&0\end{pmatrix},\quad
Q=vv^*,\quad v=(r_*,\sqrt{1-r_*^2})^T.
\]
The eigenvalues of \(X\) are \(1\pm r_*\), with common \(u=1-r_*^2\). The lower scalar branch is \(s(1-r_*)=2\sqrt{ab}=(L/2)u\), whereas the upper branch is positive. Therefore the ratio is exactly \(L/(2\delta^2)\). Both constructions have nonzero distance and prove the universal coefficient cannot increase. At \(d_t=L/2\) either construction suffices.

## Verification
An exact rational witness at \(a=100\), \(b=1\), \(t=1/2\) has \(d_t=81\), \(L=121\), and \(r_*=9/11\). Its two crossed-Heinz eigenvalues are \(-820/121\) and \(18782/121\); hence \(\operatorname{Tr}(A+B)-\|C_t\|_1=202-162=40\), while \(\|A-B\|_F^2=6480\). The attained quotient is \(1/162=\Gamma_{\mathrm{tr}}\), strictly above the Loewner coefficient \(40/9801\). The self-contained `verify_trace.py` checks this rational certificate, the low-contrast extremizer, the scalar square identity, and 15,000 deterministic numerical principal-angle cases. These finite checks only corroborate the analytic proof; they do not establish arbitrary-dimension or continuous-spectrum assertions.

## Relationship to prior work
Sababheh and Bourin, arXiv:2610.04567v1, Theorem 6.1 prove the stronger-in-order but numerically weaker-for-traces inequality \(|C_t|+\gamma_L(A-B)^2\preceq A+B\) for this two-point spectral class, with sharp \(\gamma_L=\min\{d_t,L-d_t\}/\delta^2\). Their Corollary 6.2 obtains a trace inequality with this same coefficient, while Remark 6.3 explicitly makes no claim of optimal trace coefficient. When \(d_t\le L/2\), that prior coefficient already matches the present tracial constant; the new improvement is the exact phase \(d_t>L/2\). When \(t=1/2\) and \(a/b\to\infty\), the ratio \(\Gamma_{\mathrm{tr}}/\gamma_L=L/(8\sqrt{ab})\to\infty\). Zhang, arXiv:2602.00358v1, proves crossed-Heinz bounds in noncommutative symmetric spaces but supplies no nonzero Frobenius-square remainder and hence does not imply the sharp constant. Earlier Bourin-related inequalities supply baseline comparisons, not the paired-spectrum coefficient obtained here.

## Limitations
The result assumes a finite trace and common two-point spectra with identical \(a,b\). No sharp constant is asserted for arbitrary positive \(A,B\), arbitrary unitarily invariant norms, nontracial states, or semifinite traces with infinite trace of the identity. The universal constant need not be sharp inside a single restricted algebra. Publication novelty cannot be certified solely by research-index searches; relevant unindexed or unpublished statements may exist. The numerical verifier is finite and is not a computer proof of the analytic assertions.

## References
1. M. Sababheh and J.-C. Bourin, *Crossed-Heinz Inequalities: The Two-Dimensional Threshold and Higher-Dimensional Stability*, arXiv:2610.04567v1 (first posted 2026-10-03), especially Theorem 6.1, Corollary 6.2, and Remark 6.3. https://arxiv.org/html/2610.04567v1
2. T. Zhang, *Bourin-type inequalities for \(\tau\)-measurable operators in fully symmetric spaces*, arXiv:2602.00358v1 (first posted 2026-01-30), Theorem 1.3 and Section 3. https://arxiv.org/html/2602.00358v1
3. F. Kittaneh and É. Ricard, *On a question of Bourin*, Linear Algebra Appl. 710 (2025), 356–362, DOI:10.1016/j.laa.2025.02.004 (baseline unitarily invariant norm comparison; full text not inspected).
