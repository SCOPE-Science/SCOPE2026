# Poisson cusps and sharp alphabet growth for signed Hamming Schur multipliers

## Finding

For every pair of integers \(d\ge2\), \(q\ge2\), let \(H(d,q)\) be the Hamming graph on all words of length \(d\) over a \(q\)-letter alphabet. Let \(A_{d,q}\) be its adjacency matrix, \(J\) the all-one matrix, and \(M_{d,q}=J-2A_{d,q}\). Define \(s_{d,q}\) as the spectral-operator Schur multiplier norm of \(X\mapsto M_{d,q}\circ X\), on either real or complex square matrices of order \(q^d\). With \(k=\lfloor d/q\rfloor\), we have the exact closed expression

\[
s_{d,q}=1+4d\left(1-\frac1q\right)\left[\binom{d-1}{k}\frac{(q-1)^{d-1-k}}{q^{d-1}}-\frac1{q^{d-1}}\right].
\]

For every fixed \(d\ge2\), the sequence \(q\mapsto s_{d,q}\) is **strictly increasing**, with \(s_{d,q}<1+4d\) and
\[
\sup_{q\ge2}s_{d,q}=1+4d.
\]
The proportion of negative entries in \(M_{d,q}\) is \(d(q-1)/q^d\), which tends to zero at fixed \(d\) as \(q\to\infty\), even though the Schur norm tends to \(1+4d\).

For any integers \(d,q\to\infty\) with \(d/q\to\lambda\in(0,\infty)\), we have
\[
\frac{s_{d,q}-1}{4d}\longrightarrow
\Phi(\lambda):=e^{-\lambda}\frac{\lambda^{\lfloor\lambda\rfloor}}{\lfloor\lambda\rfloor!}.
\]
The function \(\Phi\) is continuous, analytic between consecutive positive integers, and not differentiable at **any** positive integer \(m\). Its one-sided derivatives there satisfy
\[
\Phi'_-(m)=-\frac{\Phi(m)}m,\qquad \Phi'_+(m)=0.
\]
For each fixed \(q\ge2\), there is the complementary Gaussian asymptotic
\[
s_{d,q}\sim\sqrt{\frac{8d(q-1)}\pi}\quad(d\to\infty).
\]

## Assumptions and scope

All graph edges have unit length, and adjacency means *Hamming distance exactly one*. The matrix \(J\) includes its positive diagonal; hence \(M_{d,q}\) has negative entries precisely on the ordered adjacent pairs. The matrix norm on the domain and codomain of the Schur map is the Euclidean spectral operator norm; it is **not** an entrywise norm or a Schatten-four norm. The dimension \(d\) and alphabet size \(q\) are integers at least two; \(\lambda\) in the coupled limit is any positive real number. No finite matrix size is kept fixed in that limit.

## Proof

**1. Exact Schur norm for a symmetric transitive symbol.** Put \(N=q^d\). The matrix \(M=M_{d,q}\) is real symmetric and is preserved by coordinatewise letter translations, a vertex-transitive permutation group. Therefore the diagonal entries of \(|M|=(M^2)^{1/2}\) are all equal to \(\tau=N^{-1}\operatorname{tr}|M|\). Spectrally factor \(M\) into row vectors \(u_i,v_j\) with \(M_{ij}=\langle u_i,v_j\rangle\) and \(\|u_i\|=\|v_j\|=\sqrt\tau\). The standard Hilbert-space row/column factorization gives \(\|S_M\|\le\tau\): explicitly, \(S_M(X)=U^*(X\otimes I)V\) for diagonal-vector maps \(U,V\) with \(\|U\|=\|V\|=\sqrt\tau\).

Conversely choose the real symmetric orthogonal matrix \(W\) which acts as \(+1\) on the nonnegative spectral subspace of \(M\) and \(-1\) on its negative subspace. Then \(MW=|M|\). With \(e=N^{-1/2}(1,\ldots,1)^T\),
\[
\|S_M\|\ge e^T(M\circ W)e=\frac1N\sum_{i,j}M_{ij}W_{ij}=\frac1N\operatorname{tr}(MW)=\tau.
\]
This witness is real, so the real and complex Schur norms coincide. The normalized-trace principle itself is classical (Mathias; Davidson–Donsig); we use a complete direct argument here to establish the normalization.

**2. Full Hamming spectrum.** Write the adjacency operator as a sum of \(d\) commuting operators \(J_q-I_q\), each acting in one coordinate. The constant coordinate mode has eigenvalue \(q-1\) and the \((q-1)\)-dimensional zero-sum coordinate space has eigenvalue \(-1\). Thus for each \(j=0,\ldots,d\), \(A_{d,q}\) has eigenvalue \(d(q-1)-qj\) with multiplicity \(\binom dj(q-1)^j\). Since \(J\) vanishes on every nonconstant tensor mode, \(M\) has eigenvalue \(N-2d(q-1)\) on constants and eigenvalue \(2(qj-d(q-1))\) on level \(j\ge1\).

For \(d,q\ge2\), \(N\ge2d(q-1)\); indeed \(q^d\ge 1+d(q-1)+\binom d2(q-1)^2\ge2d(q-1)\) for these parameters (the last inequality follows directly from the last term for \(d\ge3\), and equality may occur for \(d=q=2\); alternatively induction on \(d\) using \(q^{d+1}/(d+1)\ge q^d/d\)). Consequently, with \(Y\sim\mathrm{Binomial}(d,1/q)\), comparison with the spectrum of \(-2A\) gives
\[
s_{d,q}=1+2\,\mathbb E|d-qY|-\frac{4d(q-1)}{q^d}.
\]

**3. Binomial single-boundary reduction.** Let \(p=1/q\), let \(Z\sim\mathrm{Binomial}(d-1,p)\), and put \(k=\lfloor dp\rfloor\). Since \(Y-dp\) is centered,
\[
\mathbb E|Y-dp|=2\mathbb E[(Y-dp)_+]=2dp(1-p)\Pr\{Z=k\}.
\]
For completeness, expand the positive-part sum over \(y>dp\), use \(y\binom dy=d\binom{d-1}{y-1}\) and \((d-y)\binom dy=d\binom{d-1}y\), and telescope neighboring binomial probabilities. The equality also holds when \(dp\) is an integer. Multiplying by \(q=1/p\) gives
\[
\mathbb E|d-qY|=2d(1-p)\Pr\{Z=k\}.
\]
Substitution yields exactly the displayed expression, including the subtraction \(4d(q-1)/q^d\).

**4. Strict growth with the alphabet.** Regard the formula as a function of real \(0<p\le1/2\). With \(k=\lfloor dp\rfloor\), set
\[
F_k(p)=\binom{d-1}k p^k(1-p)^{d-k},\qquad G(p)=(1-p)p^{d-1}.
\]
The expression is \(s(p)=1+4d(F_k(p)-G(p))\). Within each open cell \(k<dp<k+1\),
\[
F_k'(p)=\frac{k-dp}{p(1-p)}F_k(p)<0,
\qquad
G'(p)=p^{d-2}((d-1)-dp)\ge0.
\]
Hence \(s'(p)<0\). If \(dp=m\) is an integer, the probabilities \(\Pr\{\mathrm{Binomial}(d-1,p)=m-1\}\) and \(\Pr\{\mathrm{Binomial}(d-1,p)=m\}\) coincide, so \(F_k\) is continuous across the cell boundary. It follows that \(s(p)\) strictly decreases with \(p\), which is the claimed strict increase with integer \(q=1/p\). The limit at \(p\downarrow0\) is \(1+4d\), approached strictly from below.

**5. Competing limits and cusps.** If \(d/q\to\lambda\in(0,\infty)\), the binomial boundary probability in Step 3 tends to \(e^{-\lambda}\lambda^k/k!\) for \(k=\lfloor\lambda\rfloor\); at integer \(\lambda=m\), the only potential subsequential indices \(m-1,m\) give the same Poisson probability. The correction \(q^{-(d-1)}\) vanishes and \(1-1/q\to1\), proving the coupled limit. For noninteger \(\lambda\), differentiating \(e^{-\lambda}\lambda^k/k!\) proves analyticity. At \(m\in\mathbb N\), the left branch uses \(k=m-1\), and the right branch \(k=m\), yielding the stated distinct one-sided derivatives.

For fixed \(q\), the local central limit estimate for a binomial point mass at \(k=\lfloor d/q\rfloor\) gives \(\Pr\{Z=k\}\sim[2\pi d(1/q)(1-1/q)]^{-1/2}\). The exponentially small term \(q^{-(d-1)}\) and constant \(1\) are negligible relative to \(\sqrt d\), yielding the Gaussian asymptotic.

## Verification

The accompanying standard-library program `check.py` independently constructs the tensor eigenmodes of the actual signed adjacency matrix for eleven small parameter pairs. It verifies every eigenvalue through integer matrix-vector multiplication, compares the resulting exact normalized trace with the binomial single-mass formula for a large finite grid, checks strict alphabet growth, and checks small exact examples. Its successful run prints `SIGNED_HAMMING_SCHUR_CHECK_OK`. These finite computations do not prove the infinite parameter claims; Steps 1–5 above do.

As convenient exact test values, \(s_{2,2}=1\), \(s_{2,3}=25/9\), \(s_{3,2}=5/2\), and \(s_{2,4}=4\).

## Relationship to prior work

Mathias' normalized-trace Schur-multiplier criterion (1993), and Davidson–Donsig's version for transitive group actions (2005), **already cover Step 1**. The tensor-product graph spectrum in Step 2 is also standard Hamming-scheme mathematics. Holbrook–Johnston–Schoch (first publicly posted June 6, 2022) provide the motivating modern study of real sign-matrix Schur norms. Hladnik's 1999 bicirculant treatment and the 2003 Hladnik–Holbrook–Serra Capizzano paper concern closely related Fourier/tensor techniques. This result is not claimed to introduce those general principles or any new graph eigenvalues.

The assessed contribution is their sharp specialization to the two-parameter signed Hamming family, the single-binomial-mass expression, strict global alphabet monotonicity with a sparse-negative limit, and the complete Poisson cusp law. The located primary material and published mathematical-record comparisons did not state this combined Hamming-specific classification; historical equivalence under other terminology remains possible.

## Limitations

The theorem is for the specific full sign symbol \(J-2A(H(d,q))\) and spectral Schur norms. It does not classify arbitrary signed matrices, general Hamming distance shells, heterogeneous alphabet products, or Schur norms on other Schatten spaces. The elementary limit function is a limit of norms and is not itself a finite-dimensional Schur multiplier. The 1999 bicirculant article's full text was not available for direct inspection in this investigation, so prior historical coverage cannot be ruled out solely from its abstract. Independent validation has not been performed.

## References

- R. Mathias, *The Hadamard Operator Norm of a Circulant and Applications*, SIAM J. Matrix Anal. Appl. 14 (1993), 1152–1167; DOI: https://doi.org/10.1137/0614080.
- K. R. Davidson and A. P. Donsig, *Norms of Schur Multipliers* (2005), https://arxiv.org/abs/math/0506073, especially Section 4 and Theorem 4.4.
- J. Holbrook, N. Johnston, J.-P. Schoch, *Real Schur norms and Hadamard matrices* (2022), https://arxiv.org/abs/2206.02863.
- E. Christensen, *Bilinear forms, Schur multipliers, complete boundedness and duality* (2023), https://arxiv.org/abs/2301.05005.
- M. Hladnik, *Schur norms of bicirculant matrices*, Linear Algebra Appl. 286 (1999), 261–272.
- M. Hladnik, J. Holbrook, and S. Serra Capizzano, *Fat Diagonals and Fourier Analysis*, SIAM J. Matrix Anal. Appl. 24 (2003), 1060–1070; DOI: https://doi.org/10.1137/S0895479802411742.
