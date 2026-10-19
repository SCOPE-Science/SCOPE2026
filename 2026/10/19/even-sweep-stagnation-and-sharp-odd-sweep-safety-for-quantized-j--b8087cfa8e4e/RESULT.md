# Even-sweep stagnation and sharp odd-sweep safety for quantized Jacobi refinement

## Finding

Let \(P\) be any real symmetric \(n\)-by-\(n\) contraction (\(\|P\|_2\le 1\)) with a nonzero fixed vector \(u\), and take \(0<r<1\). Define the strictly positive-definite target \(A=I+rP\). Consider residual-refreshed Jacobi corrections computed using the different stored coupling \(P\): at each outer iterate \(x\), form the **exact target residual** \(v=b-Ax\), initialize \(y_0=0\), execute exactly \(k\ge1\) inner updates \(y_{j+1}=v-Py_j\), and set \(x^+=x+y_k\). All arithmetic after coefficient storage is exact.

Put \(\delta=1-r\) and \(\kappa=(1+r)/(1-r)\). Then:

1. For **every even** \(k\), the outer error operator has eigenvalue \(1\) on \(u\); hence it does not converge to the correct solution from all initial states. For \(b=Au\) and \(x_0=0\), every outer iterate remains exactly zero.
2. For **every odd** \(k\le\kappa\), the exact induced Euclidean error contraction factor is \(\boxed{\|E_k\|_2=r}\). The bound is attained at \(u\), independently of dimension or the other eigenvalues of \(P\). No such additional inner steps improve the worst-case per-outer-cycle rate over one inner step.
3. Every odd \(k\) with \(k\delta<2\) yields strict convergence for all initial states. If \(P\) also has an eigenvalue \(-1\), this condition is necessary as well: \(k\delta=2\) gives a nondecaying sign-alternating error mode, while \(k\delta>2\) gives exponentially growing error in that mode. For odd \(k>\kappa\), that mode also forces \(\|E_k\|_2>r\).

These statements occur with **literal binary round-to-nearest storage**, not only an arbitrary perturbation. For every precision \(p\ge2\), every connected undirected simple regular graph whose degree \(d\) is a power of two, and every \(r\in[1-2^{-(p+1)},1)\), let \(P\) be its normalized adjacency matrix. Storing just the off-diagonal entries of \(A=I+rP\) in binary \(p\)-significand-digit nearest-even arithmetic (with sufficient exponent range), while keeping its diagonal equal to one, replaces the off-diagonal coupling \(rP\) by exactly \(P\). The graph matrix meets all the spectral hypotheses. Connected bipartite regular graphs attain both critical modes, so all three conclusions apply with a sharp odd-sweep convergence threshold.

For the natural dyadic example \(r=1-2^{-(p+2)}\) on an even cycle (degree two) or a complete balanced bipartite graph of power-of-two degree, \(\kappa=2^{p+3}-1\). **Every even** inner sweep count stalls a nonzero mode; **every odd** \(k\le2^{p+3}-1\) has exactly the same worst-case outer contraction \(r\); and **every odd** \(k\ge2^{p+3}+1\) has an exponentially growing mode. The source system is positive definite throughout.

## Assumptions and scope

All matrices and vectors are real and finite-dimensional. The one parameter \(r\) lies strictly between zero and one. The matrix \(P\) is symmetric, \(\|P\|_2\le1\), and has eigenvalue one. For the sharp failure threshold in part 3, eigenvalue minus one is additionally assumed. Each outer step uses the original matrix \(A\) in the residual and the stored coupling \(P\) in each inner Jacobi step; the inner initial guess is reset to zero. The number of inner steps \(k\) is fixed between outer steps. The binary-storage corollary uses normalized binary arithmetic with a \(p\)-bit significand, round-to-nearest/ties-to-even, sufficient exponent range and no further arithmetic rounding. No claim is made about a literal implementation whose inner dot products, residuals, or updates also incur rounding.

## Proof

**Exact residual-to-error polynomial.** For \(k\ge1\) define \(C_k=\sum_{j=0}^{k-1}(-P)^j\). The recurrence gives \(y_k=C_kv\). Hence, if \(e=x-x_\star\), with \(Ax_\star=b\), then \(e^+=E_ke\) where
\[
E_k=I-C_k(I+rP).
\]
Because \(P\) is symmetric, \(E_k\) has the real eigenvalue \(g_k(\lambda)=1-(1+r\lambda)\sum_{j=0}^{k-1}(-\lambda)^j\) on a \(P\)-eigenvector with eigenvalue \(\lambda\in[-1,1]\). At the endpoints,
\[
g_k(1)=\begin{cases}1,&k\text{ even},\\-r,&k\text{ odd},\end{cases}
\qquad g_k(-1)=1-k(1-r).
\]
The first formula proves even-sweep stagnation. For \(b=Au\) and \(x_0=0\), the residual stays \((1+r)u\) and every even-sweep correction vanishes, proving the explicit frozen trajectory.

**A sharp uniform bound for safe odd counts.** Write \(\delta=1-r\), and suppose \(k\) odd with \(\delta(k+1)\le2\). At \(k=1\), the formula reduces to \(g_1(\lambda)=-r\lambda\), so \(\|E_1\|_2=r\). For odd \(k\ge3\), note that \(\delta\le1/2\).

For \(0\le\lambda\le1\), set \(S=(1+\lambda^k)/(1+\lambda)\). Direct division yields
\[
g_k(\lambda)=-\lambda^k+\delta\lambda S.
\]
Since \(\lambda^k\le\lambda\), \(S\le1\), so \(g_k(\lambda)\le\delta\le r\). Moreover
\[
g_k(\lambda)+r
=(1-\lambda^k)-\delta\frac{1-\lambda^{k+1}}{1+\lambda}
\ge r(1-\lambda^k)\ge0,
\]
where the first inequality uses \(1-\lambda^{k+1}\le(1+\lambda)(1-\lambda^k)\), equivalent to \(\lambda^k\le\lambda\).

For \(-1\le\lambda\le0\), put \(t=-\lambda\in[0,1]\). Then
\[
g_k(-t)=t^k-\delta\sum_{j=1}^kt^j\le rt^k\le r.
\]
Convexity of \(s\mapsto t^s\) (with the endpoints treated by continuity) gives the discrete chord inequality
\[
\sum_{j=0}^kt^j\le\frac{k+1}{2}(1+t^k).
\]
Consequently,
\[
g_k(-t)+r=1+t^k-\delta\sum_{j=0}^kt^j
\ge(1+t^k)\left(1-\frac{\delta(k+1)}2\right)\ge0.
\]
Thus \(|g_k(\lambda)|\le r\) for the full spectrum. The vector \(u\) has eigenvalue \(-r\), proving equality \(\|E_k\|_2=r\). The condition \(\delta(k+1)\le2\) is precisely \(k\le\kappa\).

**Strict convergence and the sharp bipartite boundary.** Let \(k\) be odd and \(k\delta<2\). For \(\lambda\in[0,1]\), \(g_k(\lambda)\le\delta\lambda S<1\), and \(g_k(\lambda)>-1\) (strict at \(\lambda=1\) because \(r<1\)). For \(\lambda=-t\in[-1,0]\), the upper bound \(g_k(-t)\le rt^k<1\) holds. Subtracting the \(j=0\) term from the chord inequality and using \(t^k\le1\) gives
\[
\sum_{j=1}^kt^j\le\frac{k}{2}(1+t^k).
\]
Hence
\[
g_k(-t)\ge\left(1-\frac{k\delta}{2}\right)t^k-\frac{k\delta}{2}>-1.
\]
Since \(E_k\) is real symmetric, all its eigenvalues are strictly within the unit disk, and the outer iteration converges for every initial error. If \(-1\) is an eigenvalue of \(P\), the exact value \(1-k\delta\) supplies the converse and the stated boundary behavior. For odd \(k>\kappa\), it also satisfies \(1-k\delta<-r\), proving strict deterioration in the operator norm.

**Binary realization.** For a connected \(d\)-regular undirected simple graph, \(P=\mathrm{Adj}/d\) is a symmetric stochastic matrix with \(\|P\|_2=1\) and \(P\mathbf1=\mathbf1\). A bipartite graph also has \(P\sigma=-\sigma\) for its alternating-sign vector. If \(d\) is a power of two, \(1/d\) is representable. In a binary \(p\)-significand-digit format, the value immediately below \(1/d\) is \((1-2^{-p})/d\), with midpoint \((1-2^{-(p+1)})/d\). Thus exactly when \(1-2^{-(p+1)}\le r<1\), rounding \(r/d\) to nearest-even gives \(1/d\). The tie goes upward because the significand of \(1/d\) is even at its least significant bit. Every nonedge remains zero and the diagonal one remains exact. The target eigenvalues are \(1+r\lambda(P)\ge1-r>0\). In the dyadic example, \(\delta=2^{-(p+2)}\) yields \(\kappa=(2-\delta)/\delta=2^{p+3}-1\). Since this \(\kappa\) is odd and \(\kappa+1\) is even, the next odd \(k\) exceeds \(2/\delta\), yielding the asserted three-way classification.

## Verification

A standalone exact-rational checker, `verify_quantized_jacobi.py`, is included. Running `python verify_quantized_jacobi.py` prints `FINAL PASS 29781 exact rational checks`. It directly forms the graph matrices and correction operators for multiple precisions and sizes, checks the rounding midpoints, compares all resulting matrices to their eigenprojector representation, replays the inner recurrence, and tests scalar bounds at rational points across the complete spectral interval. It includes a connected nonbipartite graph. The mathematical proof above, not the finite testing, establishes the results for every stated dimension, precision, and inner count.

## Relationship to prior work

Lindquist, Appelhans, Jackson, and Derlaga's 2026 paper introduces mixed-precision matrix-splitting storage and restarted stationary corrections. Their exact-iteration restart equivalence assumes the same operator in the residual and inner recurrence; the two operators differ here specifically because of coefficient quantization. This finding does not question their stated estimates under their assumptions. Tamstorf, Benzaken, and McCormick established that quantization can change definiteness and that suitably chosen multigrid correction cycles may remain effective. The present theorem treats the different, fixed-length Jacobi corrector and gives a parity-specific complete boundary. Suzuki and Iwashita studied limited low-precision inner iterations in a nested Krylov architecture, not this polynomial restart with its Perron-mode obstruction. Zhang and Trogdon studied Neumann-series iteration under strict spectral contraction, not the endpoint-quantized mismatch with high-precision residuals. The Neumann polynomial, elementary graph eigenvectors, and rounding midpoint facts themselves are standard; the new claim is their combined sharp restarted-Jacobi consequence and the uniform odd-sweep inequality.

## Limitations

This is a deterministic, post-storage exact-arithmetic model and does not model roundoff in subsequent inner products or vector updates, finite exponent-range effects, stochastic rounding, adaptive restart lengths, floating-point stopping tests, or Krylov acceleration. It makes no wall-clock performance claim. The frozen example occurs at a near-singular low-precision conditioning boundary; it does not imply failure of the 2026 method for well-conditioned systems. Earlier equivalent specializations in general polynomial-preconditioning literature remain a bibliographic possibility. A full independent validation has not been performed.

## References

1. N. Lindquist, D. Appelhans, C. W. Jackson, and J. M. Derlaga, *A Mixed-Precision Model for Matrix-Splitting Methods*, arXiv:2610.06414 (first version dated 2026-10-05), especially Section 2.1 and Algorithm 2.1. https://arxiv.org/abs/2610.06414
2. R. Tamstorf, J. Benzaken, and S. F. McCormick, *Discretization-Error-Accurate Mixed-Precision Multigrid Solvers*, arXiv:2007.06628 (2020), especially Sections 1 and 3–4. https://arxiv.org/abs/2007.06628
3. K. Suzuki and T. Iwashita, *A Nested Krylov Method Using Half-Precision Arithmetic*, arXiv:2505.20719 (2025), Sections 3–4. https://arxiv.org/abs/2505.20719
4. Y. Zhang and T. Trogdon, *A Probabilistic Analysis of the Neumann Series Iteration*, arXiv:1909.07506 (2019), Sections 1–3. https://arxiv.org/abs/1909.07506
