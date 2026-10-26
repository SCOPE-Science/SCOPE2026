# Deterministic spectral dominance of funNyström for fractional matrix powers

## Finding

Let \(A\) be any real symmetric positive-definite \(n\times n\) matrix, let \(1\le k\le n\), let \(\Omega\in\mathbb R^{n\times k}\) have full column rank, and let \(q\ge1\) be an integer. For every symmetric positive-definite \(B\), define the power-Nyström matrix
\[
\mathcal N_q(B;\Omega)=B^q\Omega(\Omega^{\mathsf T}B^{2q-1}\Omega)^{-1}\Omega^{\mathsf T}B^q.
\]
Write the \(k\) positive eigenvalues of this rank-\(k\) matrix in descending order. For every exponent \(0<p<1\), and every \(1\le j\le k\),
\[
\boxed{\lambda_j\bigl(\mathcal N_q(A^p;\Omega)\bigr)\le\lambda_j\bigl(\mathcal N_q(A;\Omega)\bigr)^p.}
\]
For \(p>1\), the inequality is reversed; at \(p=1\) there is equality. In the concave-power regime, this implies a deterministic, same-sketch nuclear-norm residual inequality:
\[
\boxed{\|A^p-\mathcal N_q(A;\Omega)^p\|_*\le\|A^p-\mathcal N_q(A^p;\Omega)\|_* .}
\]
Thus applying a fractional power *after* the Nyström approximation always gives at least as large a captured trace as Nyström approximation of that matrix power using the identical sketch and iteration count. The comparison is independent of the distribution of \(\Omega\).

The advantage can be arbitrarily large. At \(p=1/2\), \(q=k=1\), let \(L>1\),
\[
A_L=\begin{pmatrix}L&0\\0&1\end{pmatrix},\qquad
\Omega_L=\begin{pmatrix}L^{-3/8}\\1\end{pmatrix}.
\]
Then the nonzero eigenvalues of \(\mathcal N_1(A_L;\Omega_L)\) and \(\mathcal N_1(A_L^{1/2};\Omega_L)\) respectively equal
\[
\alpha_L=\frac{L^{5/4}+1}{L^{1/4}+1},\qquad \beta_L=L^{1/4}.
\]
Their nuclear-norm residuals for approximating \(A_L^{1/2}\) are, respectively,
\[
E_{\rm fun}(L)=L^{1/2}+1-\sqrt{\alpha_L}\sim\tfrac12 L^{1/4},\qquad
E_{\rm direct}(L)=L^{1/2}+1-L^{1/4}\sim L^{1/2},
\]
so \(E_{\rm direct}(L)/E_{\rm fun}(L)\sim2L^{1/4}\to\infty\).

## Assumptions and scope

All matrix powers mean the spectral functional calculus of real symmetric positive-definite matrices. A real nonnegative symmetric matrix has its usual nonnegative spectral power; zero eigenvalues stay zero. All inverses above exist by positive definiteness and full column rank of the sketch. The statement holds for every dimension, every full-rank deterministic sketch, every integer \(q\ge1\), and every real exponent \(p>0\), with the residual comparison restricted to \(0<p<1\). The source algorithm permits random Gaussian sketches, but randomness is not an assumption here. The same \(\Omega\) and the same \(q\) must be used in both alternatives.

## Proof

**1. Generalized Ritz values.** For \(t\ge0\) write \(M_t=\Omega^{\mathsf T}A^t\Omega\). For each \(p>0\), \(M_{p(2q-1)}\) is positive definite, and the nonzero eigenvalues of \(\mathcal N_q(A^p;\Omega)\) are precisely the generalized eigenvalues of the symmetric-definite pencil
\[
\bigl(M_{2pq},M_{(2q-1)p}\bigr).
\]
Indeed, factor the Nyström matrix as \(XX^{\mathsf T}\), where \(X=A^{pq}\Omega M_{(2q-1)p}^{-1/2}\). The nonzero eigenvalues of \(XX^{\mathsf T}\) are those of \(X^{\mathsf T}X\). Consequently, if \(v\ne0\) and \(w=\Omega v\ne0\), the associated generalized Rayleigh quotient equals
\[
R_p(v)=\frac{w^{\mathsf T}A^{2pq}w}{w^{\mathsf T}A^{(2q-1)p}w}.
\]

**2. Log-convex spectral moments.** For every \(w\ne0\), set \(m_w(t)=w^{\mathsf T}A^t w\), \(g_w(t)=\log m_w(t)\). In an orthonormal eigenbasis of \(A\),
\[
m_w(t)=\sum_{i=1}^{n}|c_i|^2e^{t\log a_i},\qquad a_i>0.
\]
Therefore \(g_w\) is twice differentiable and
\[
g_w''(t)=\operatorname{Var}_{\pi_t}(\log a_i)\ge0,\qquad
\pi_{t,i}=\frac{|c_i|^2a_i^t}{m_w(t)}.
\]
Thus \(g_w'\) is nondecreasing. Writing \(R_1(v)=m_w(2q)/m_w(2q-1)\), for \(0<p<1\),
\[
\log R_p(v)=p\int_{2q-1}^{2q}g_w'(pt)\,dt
\le p\int_{2q-1}^{2q}g_w'(t)\,dt
=p\log R_1(v),
\]
because \(t\ge2q-1\ge1>0\). Exponentiation gives \(R_p(v)\le R_1(v)^p\). For \(p>1\), the monotonicity of \(g'_w\) reverses that inequality. Applying generalized Courant–Fischer max-min to the two positive-definite pencils, on the same coefficient-space \(\mathbb R^k\), and using that \(x\mapsto x^p\) is increasing, gives the asserted comparison of each ordered eigenvalue. For \(p=1\) the pencils coincide.

**3. Trace residuals.** For every positive-definite \(B\), with \(Y=B^{q-1/2}\Omega\),
\[
\mathcal N_q(B;\Omega)=B^{1/2}Y(Y^{\mathsf T}Y)^{-1}Y^{\mathsf T}B^{1/2}.
\]
The middle factor is an orthogonal projector, so \(0\preceq\mathcal N_q(B;\Omega)\preceq B\). For \(0<p<1\), the Löwner–Heinz inequality gives \(\mathcal N_q(A;\Omega)^p\preceq A^p\); applying the projector formula to \(B=A^p\) gives \(\mathcal N_q(A^p;\Omega)\preceq A^p\). Both residuals are positive semidefinite and hence their nuclear norms equal their traces. Summing the eigenvalue comparison from Step 2 shows
\[
\operatorname{tr}\mathcal N_q(A^p;\Omega)\le\operatorname{tr}\mathcal N_q(A;\Omega)^p.
\]
Subtract these traces from \(\operatorname{tr}A^p\) to obtain the residual inequality. Neither an ordering between the two low-rank matrices nor a bound on their Frobenius/operator-norm residuals has been asserted.

**4. Unbounded separation.** With the stated two-by-two matrices and \(q=1\), the only positive eigenvalue of \(\mathcal N_1(B;\Omega)\) is
\[
\frac{\Omega^{\mathsf T}B^2\Omega}{\Omega^{\mathsf T}B\Omega}.
\]
Direct substitution gives \(\alpha_L\) and \(\beta_L\). Set \(u=L^{1/4}\). Long division yields the *exact* polynomial identity
\[
\alpha_L=\frac{u^5+1}{u+1}=u^4-u^3+u^2-u+1.
\]
Hence \(\sqrt{\alpha_L}=u^2-\tfrac12u+O(1)\) and the two residuals are \(\tfrac12u+O(1)\) and \(u^2-u+1\). Their ratio is \(2u(1+o(1))\), proving the unbounded gap.

## Verification

The included standalone script `verify.py` checks the exact two-by-two rational identities using symbolic arithmetic, verifies the asymptotic ratio numerically over increasing \(L\), and stress-tests the matrix-pencil eigenvalue inequalities and trace residuals on positive-definite randomly rotated matrices for several dimensions, sketch ranks, power counts, and exponents. Execute with `python verify.py` after installing `requirements.txt`. Finite stress tests only corroborate; the all-dimensional claim is proved above.

## Relationship to prior work

Persson and Kressner [1] define funNyström by taking a matrix function of the power-Nyström approximation (their formula (3) and Algorithm 1), prove randomized nuclear/Frobenius/operator error bounds, and numerically compare the method to approximating the matrix function directly. Their Lemma 3.2 and nuclear-norm analysis give a projection-based comparison rather than the same-sketch eigenvalue-by-eigenvalue comparison here. Section 4.3 specifically reports empirical evidence that funNyström is not worse than directly sketching the matrix function in its test problems; this theorem proves a precise all-sketch trace inequality for fractional powers. Persson, Meyer, and Musco [2] prove that a good approximation to a positive matrix transfers to a good approximation of its operator-monotone function, independently of the underlying algorithm, but do not state the deterministic paired-algorithm spectral comparison or unbounded trace-residual separation. Classical log-convexity of matrix spectral moments, generalized min-max, and Löwner–Heinz are used as standard ingredients, not claimed as new. This finding addresses a more specific *relative* performance question, with neither randomization nor approximation-optimality assumptions.

## Limitations

The theorem requires positive definiteness and a full-column-rank common sketch; it does not directly address singular matrices with pseudoinverses. For concave fractional powers it concerns the trace/nuclear-norm residual, not Frobenius or operator norms. For \(p>1\), only the eigenvalue inequality is claimed, because functional calculus need not preserve Löwner order at those exponents. The adversarial sketch in the unbounded-gap family depends on its matrix parameter, so the gap is not a typical-case Gaussian expectation bound. Arithmetic is exact and no finite-precision stability claim is made. The originality assessment is limited to the cited works and searchable mathematical records, not an exhaustive historical proof of novelty.

## References

[1] D. Persson and D. Kressner, *Randomized low-rank approximation of monotone matrix functions*, arXiv:2209.11023, first public 2022-09-22; SIAM J. Matrix Anal. Appl. 44 (2023), 894–918. https://arxiv.org/abs/2209.11023

[2] D. Persson, R. A. Meyer, and C. Musco, *Algorithm-agnostic low-rank approximation of operator monotone matrix functions*, arXiv:2311.14023, first public 2023-11-23; SIAM J. Matrix Anal. Appl. 46 (2025), 1–21. https://arxiv.org/abs/2311.14023

[3] R. Bhatia, *Matrix Analysis*, Springer (1997), standard Löwner–Heinz and generalized variational matrix analysis background.
