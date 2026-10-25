# Exact linear-width positive factors for relaxed GADI Lyapunov iterates

## Finding
For the fixed-shift generalized alternating-direction implicit (GADI) iteration of the Lyapunov equation \(F^{\mathsf T}X+XF=C^{\mathsf T}C\), the published R-GADI factors have \((2^k-1)p\) columns after \(k\) steps. At every step, the **same matrix iterate** has an exact positive-semidefinite factor with at most \(kp\) columns. The factor is a binomially weighted rational Krylov sequence, and its column span gives the exact rank.

## Assumptions and scope
Let \(F\in\mathbb R^{n\times n}\) have eigenvalues of strictly positive real part, let \(C\in\mathbb R^{p\times n}\), and choose \(\alpha>0\), \(0\le\omega<2\). Set \(Q=C^{\mathsf T}C\) and \(X_0=0\). The iteration is precisely
\[
(\alpha I+F^{\mathsf T})X_{k+1/2}=X_k(\alpha I-F)+Q,
\]
\[
X_{k+1}(\alpha I+F)=X_k(F-(1-\omega)\alpha I)+(2-\omega)\alpha X_{k+1/2}.
\]
The shift is constant across steps. All statements concern real matrices in exact arithmetic and every integer \(k\ge1\). Define
\[
H=(\alpha I+F)^{-1},\qquad T=2\alpha H^{\mathsf T}-I,\qquad c=\omega/2,\qquad b=1-c,
\]
\[
E=\sqrt{2\alpha b}\,H^{\mathsf T}C^{\mathsf T}.
\]
For \(0\le j<k\), set
\[
w_{k,j}=b^j\sum_{r=j}^{k-1}\binom rj c^{r-j}.
\]
With \(c=0\), interpret \(0^0=1\) in the finite binomial formula. Every \(w_{k,j}>0\), including the boundary \(\omega=0\).

## Proof
**One-step identity.** Eliminate \(X_{k+1/2}\) from the source iteration, using the commutativity of \(F\) and \(H\). Simplification gives
\[
X_{k+1}=cX_k+bTX_kT^{\mathsf T}+EE^{\mathsf T}. \tag{1}
\]
One way to check all coefficients is to write the standard one-shift ADI update as \(X^{\rm ADI}=TX_kT^{\mathsf T}+2\alpha H^{\mathsf T}QH\): the stated update is exactly \(cX_k+bX^{\rm ADI}\). Direct substitution into the two original equations gives the same identity without invoking an external result.

**Binomial expansion.** On symmetric matrices define commuting operators \(\mathcal I(X)=X\) and \(\mathcal T(X)=TXT^{\mathsf T}\). By (1) and \(X_0=0\),
\[
X_k=\sum_{r=0}^{k-1}(c\mathcal I+b\mathcal T)^r(EE^{\mathsf T}).
\]
The binomial theorem yields
\[
X_k=\sum_{j=0}^{k-1}w_{k,j}(T^jE)(T^jE)^{\mathsf T}=Z_kZ_k^{\mathsf T},
\]
where
\[
Z_k=\big[\sqrt{w_{k,0}}E,\sqrt{w_{k,1}}TE,\dots,\sqrt{w_{k,k-1}}T^{k-1}E\big].
\]
Equivalently the weights are generated using only current and previous indices: \(w_{1,0}=1\), \(w_{k+1,0}=1+cw_{k,0}\), \(w_{k+1,j}=cw_{k,j}+bw_{k,j-1}\) for \(1\le j<k\), and \(w_{k+1,k}=bw_{k,k-1}\). All weights are strictly positive because \(b>0\). This proves positive semidefiniteness and a factor with precisely \(kp\) stored columns before dependence compression.

**Exact rank and sharpness.** Since \(w_{k,j}>0\),
\[
\operatorname{rank}X_k=\operatorname{rank}Z_k
=\dim\operatorname{span}\{E,TE,\ldots,T^{k-1}E\}\le\min(n,kp).
\]
Because \(T=2\alpha H^{\mathsf T}-I\) and \(E\) is a positive scalar multiple of \(H^{\mathsf T}C^{\mathsf T}\), the triangular polynomial changes of basis give the further exact description
\[
\operatorname{ran}X_k=\operatorname{span}\{H^{\mathsf T}C^{\mathsf T},\ldots,(H^{\mathsf T})^kC^{\mathsf T}\}.
\]
For \(p=1\), take \(F=\operatorname{diag}(f_1,\ldots,f_n)\) with distinct positive \(f_i\) and \(C=(1,\ldots,1)\). Then \(E_i\ne0\), while \(T\) has distinct diagonal entries \((\alpha-f_i)/(\alpha+f_i)\). The Vandermonde determinant shows the rank is exactly \(\min(k,n)\), establishing sharpness in every step before saturation. This does not assert full \(kp\) rank for arbitrary inputs.

## Verification
Run the complete standalone script `verify_rgadi.py` using Python 3 with NumPy. It independently forms the source two-stage dense iteration, constructs the weighted factor from a separate formula, verifies their agreement and symmetry/positive semidefiniteness for diagonal and nonsymmetric positive-stable examples, tests the weight recurrence against its binomial closed form, and checks the diagonal sharpness example. Numerical tests illustrate the theorem; its proof is the matrix identity, binomial expansion and Vandermonde argument above.

## Relationship to prior work
Zhang and Xun, *Low-rank generalized alternating direction implicit iteration method for solving matrix equations*, arXiv:2404.06034v1 (2024-04-09), Section 2.1, give the two-stage GADI recurrence as equation (12) and the \((2^k-1)p\)-column factors in equation (13). Their computational-complexity discussion explicitly uses this exponential column count. Their equation (7) already gives a \(kp\)-column factor for **ordinary**, unrelaxed one-shift ADI. The present identity supplies an exact \(kp\)-column **positive** factor for the nonzero-relaxation GADI variant as well, with explicit binomial weights and a rank characterization. The standard low-rank CF-ADI and rational Krylov constructions supply conceptual context but are not claimed as new here.

## Limitations
The conclusion is for the fixed-parameter Lyapunov inner iteration with zero initial matrix. It does not prove a faster numerical implementation in finite precision, accuracy of compressed factors after truncation, or an identical iteration when shifts or relaxation vary by step. The rank bound is a structural statement; numerical conditioning of the Krylov columns can still degrade. The comparison with prior literature is not an independent publication-priority certification.

## References
1. J. Zhang and W. Xun, *Low-rank generalized alternating direction implicit iteration method for solving matrix equations*, arXiv:2404.06034v1 (2024-04-09), especially equations (7), (12), (13) and Section 2.3. https://arxiv.org/abs/2404.06034
2. J.-R. Li and J. White, *Low rank solution of Lyapunov equations*, SIAM Journal on Matrix Analysis and Applications 24 (2002), 260–280, classical Cholesky-factor ADI and Krylov subspace context.
