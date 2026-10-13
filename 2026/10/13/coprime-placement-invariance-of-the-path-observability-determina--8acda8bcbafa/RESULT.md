# Coprime placement invariance of the path observability determinant

## Finding
For an integer \(n\geq2\), let \(J_n\in\mathbb R^{n\times n}\) be the symmetric nearest-neighbor path adjacency matrix: \((J_n)_{i,i+1}=(J_n)_{i+1,i}=1\) and all other entries are zero. Let
\[
A=\alpha I_n+\beta J_n,\qquad \alpha\in\mathbb R,\quad\beta\in\mathbb R\setminus\{0\}.
\]
For a single coordinate observation at node \(j\in\{1,\ldots,n\}\), define the finite-horizon observability Gramian
\[
W_H(j)=\sum_{t=0}^{H-1}A^t e_j e_j^{\mathsf T}A^t,
\qquad H\in\mathbb Z,\quad H\ge n.
\]
Because \(A\) is symmetric, this is also the controllability Gramian for the same coordinate input. Write \(m=n+1\), \(g=\gcd(j,m)\), and
\[
\lambda_k=\alpha+2\beta\cos\!\left(\frac{k\pi}{m}\right),
\qquad k=1,\ldots,n.
\]
Then the following is an exact, all-dimensional classification.

1. The rank of \(W_H(j)\) equals \(n-g+1\). Its determinant vanishes exactly when \(g>1\).
2. Every coordinate with \(\gcd(j,n+1)=1\) has the **same strictly positive determinant**, for every \(H\ge n\), every real \(\alpha\), and every nonzero real \(\beta\). These and only these coordinates maximize the determinant over all single-coordinate sensor placements.
3. At the smallest full horizon the common determinant has the universal closed form
\[
\boxed{\det W_n(j)=\beta^{n(n-1)}\quad\text{if }\gcd(j,n+1)=1.}
\]
4. If additionally \(\max_k|\lambda_k|<1\), the infinite-horizon Gramian \(W_\infty(j)=\sum_{t=0}^\infty A^te_je_j^{\mathsf T}A^t\) exists and has the same rank and optimizer classification. At every coprime coordinate,
\[
\boxed{
\det W_\infty(j)
=\frac{\beta^{n(n-1)}}{\displaystyle\prod_{k=1}^n\prod_{\ell=1}^n(1-\lambda_k\lambda_\ell)}.
}
\]
The denominator is strictly positive under the stated stability assumption. In particular, the set of determinant-optimal positions is independent of the observation horizon and of the scalar diagonal and edge parameters.

## Assumptions and scope
All states, matrices, and sensors are real. The index \(j\) is one-based. Every path edge has the **same** nonzero symmetric coupling \(\beta\), and every diagonal entry of \(A\) is \(\alpha\); these Toeplitz hypotheses are essential. For finite horizons there is no stability requirement, and \(\beta\) may be negative. Infinite horizons require the strict Schur-stability inequality \(\max_k|\lambda_k|<1\). The information-volume or D-optimality criterion is \(\det W_H(j)\), not the trace, condition number, or smallest eigenvalue. Sensor inputs have equal unit coordinate magnitude, and there is exactly one sensor.

The same statement describes a heat discretization with Dirichlet boundary values at two exterior nodes: setting \(A=I-\eta T_n\), where \(T_n=2I-J_n\) and \(\eta>0\), gives \(\alpha=1-2\eta\), \(\beta=\eta\). This Dirichlet model is not the degree-corrected (Neumann) path graph Laplacian.

## Proof
**1. Distinct spectral modes and their sensor weights.** The standard discrete sine eigenbasis for \(J_n\) is
\[
U_{ik}=\sqrt{\frac{2}{m}}\sin\!\left(\frac{ik\pi}{m}\right),
\quad\lambda_k=\alpha+2\beta\cos\!\left(\frac{k\pi}{m}\right).
\]
The eigenvalues \(\lambda_1,\ldots,\lambda_n\) are distinct because \(\beta\ne0\) and cosine is strictly decreasing on \((0,\pi)\). Set \(d_k(j)=U_{jk}\) and
\[
K_H(k,\ell)=\sum_{t=0}^{H-1}\lambda_k^t\lambda_\ell^t.
\]
Then
\[
U^{\mathsf T}W_H(j)U
=\operatorname{diag}(d_k(j))K_H\operatorname{diag}(d_k(j)),
\]
so \(\det W_H(j)=(\prod_k d_k(j)^2)\det K_H\). The \(n\times H\) Vandermonde-type matrix with entries \(\lambda_k^t\), \(0\le t<H\), has full row rank when \(H\ge n\). Consequently \(K_H\) is positive definite and its determinant is strictly positive, independently of the sensor location.

**2. Exact arithmetic rank and determinant classification.** Put \(g=\gcd(j,m)\). The sine coefficient \(d_k(j)\) is zero precisely when \(m\mid jk\). These indices among \(1\le k\le m-1\) are exactly \(k=r m/g\) for \(r=1,\ldots,g-1\). Therefore exactly \(g-1\) spectral directions vanish at node \(j\), and the rank of the Gramian is \(n-(g-1)=n-g+1\).

If \(g=1\), multiplication by \(j\) permutes all nonzero residue classes modulo \(m\), and the absolute sine is invariant under reduction modulo \(m\). Thus
\[
\prod_{k=1}^n|\sin(jk\pi/m)|
=\prod_{k=1}^n\sin(k\pi/m)
=\frac{m}{2^n}.
\]
The last equality follows from the roots-of-unity product \(\prod_{k=1}^{m-1}|1-e^{2\pi i k/m}|=m\) and \(|1-e^{2\pi i k/m}|=2\sin(k\pi/m)\). Hence
\[
\prod_{k=1}^n d_k(j)^2=
\begin{cases}
2^{-n}m^{2-n},&\gcd(j,m)=1,\\
0,&\gcd(j,m)>1.
\end{cases}
\]
This proves the horizon-independent determinant equality and the complete set of maximizers, since \(\det K_H>0\).

**3. Universal minimal-horizon value.** The \(n\)-step coordinate controllability matrix is
\[
C_n(j)=[e_j,Ae_j,\ldots,A^{n-1}e_j],
\quad W_n(j)=C_n(j)C_n(j)^{\mathsf T}.
\]
At the endpoint \(j=1\), column \(t+1\) of \(C_n(1)\) has support only on coordinates \(1,\ldots,t+1\), and its entry at coordinate \(t+1\) is \(\beta^t\) (the unique \(t\)-step nearest-neighbor route). Therefore \(C_n(1)\) is triangular with determinant \(\beta^{0+1+\cdots+(n-1)}=\beta^{n(n-1)/2}\), so
\[
\det W_n(1)=\beta^{n(n-1)}.
\]
Since the endpoint is coprime to \(m\), the determinant equality proved in Step 2 gives exactly the same value at every coprime sensor, and zero at every other sensor.

**4. Infinite-horizon value.** Under strict Schur stability, \(K_\infty(k,\ell)=1/(1-\lambda_k\lambda_\ell)\). The Cauchy double-alternant identity (the polynomial identity extends by continuity to zero eigenvalues) gives
\[
\det K_\infty
=\frac{\displaystyle\prod_{1\le k<\ell\le n}(\lambda_k-\lambda_\ell)^2}
{\displaystyle\prod_{k,\ell=1}^n(1-\lambda_k\lambda_\ell)}.
\]
For \(H=n\), \(K_n\) is the Vandermonde Gram matrix and hence \(\det K_n=\prod_{k<\ell}(\lambda_k-\lambda_\ell)^2\). Combining Step 3 with \(\det W_n(1)=2^{-n}m^{2-n}\det K_n\) yields
\[
2^{-n}m^{2-n}\prod_{k<\ell}(\lambda_k-\lambda_\ell)^2
=\beta^{n(n-1)}.
\]
Substitution into the infinite-horizon identity proves the formula in the Finding. Every factor \(1-\lambda_k\lambda_\ell\) is positive because all eigenvalues are real with modulus less than one. Rank and optimizer statements follow exactly as in Steps 1–2 using the infinite geometric-sequence Gram matrix, whose principal \(n\times n\) truncation already has full rank.

## Verification
The standalone `checker.py` uses only Python's standard-library rational arithmetic. Run `python3 checker.py`. Its result is:

```
VERIFY_OK 630 exact-rational finite tests; 630 determinants; 630 ranks; n=4 trace contrast.
```

It checks all positions at dimensions \(2\le n\le8\), three exact rational values of \(\alpha\), two nonzero exact rational values of \(\beta\), and the three horizons \(H=n,n+1,n+2\). For every case it independently computes the Gramian, its exact rational determinant, and exact rank; checks all determinant ties and singularities; and checks the universal \(n\)-step value. These finite tests do **not** constitute a proof for every dimension or all real coefficients; Steps 1–4 provide that proof.

An exact example shows why the determinant result does not imply other sensor metrics tie. For \(n=4\), \(A=(3/5)I+(1/5)J_4\), and \(H=4\), both end sensor \(j=1\) and interior sensor \(j=2\) have determinant \(5^{-12}\), yet
\[
\operatorname{tr} W_4(1)=\frac{27519}{15625}
\quad\text{and}\quad
\operatorname{tr}W_4(2)=\frac{31197}{15625}.
\]
The larger interior trace is not a larger determinant.

## Relationship to prior work
Parlangeli and Notarstefano (arXiv:1109.3556, 2011) classify reachability and observability of consensus dynamics on ordinary path and cycle graph Laplacians and explicitly give the eigenvectors of the related Dirichlet tridiagonal Toeplitz matrix in their spectral section and appendix. That published spectral data and the general PBH criterion are prior art. Their path-graph model has endpoint degrees one, whereas the present Dirichlet matrix has diagonal two at its endpoints. The novel statement assessed here is **not** the sine basis or a generic rank criterion, but the exact all-horizon determinant equality, its universal shortest-horizon value, and its complete D-optimal classification.

Pasqualetti, Zampieri, and Bullo (arXiv:1308.1201, 2013) discuss quantitative controllability Gramians and metrics including determinant and control-energy volume; their work does not assert this Dirichlet-path arithmetic invariance. Summers and Lygeros (arXiv:1306.2491, 2013) establish modularity for trace-based sensor/actuator placement; their paper explicitly focuses on trace, not on the determinant-optimal node family derived here. Standard discrete-sine formulas and the Cauchy determinant identity are used as established mathematical tools rather than being claimed as original.

## Limitations
Only a uniform symmetric Toeplitz path, a single unit coordinate sensor, and determinant optimality are classified. The result does not cover the Neumann path Laplacian, heterogeneous edge weights, multiple simultaneous sensors, arbitrary weighted observation vectors, nor minimizers of worst-case estimation error or condition number. Finite-horizon statements do not assert asymptotic stability. The rank condition alone is not presented as a novel result. A closely matching unpublished or less discoverable D-optimal path-placement theorem could exist; literature searches do not prove global priority. No independent audit has been performed.

## References
1. G. Parlangeli and G. Notarstefano, *On the reachability and observability of path and cycle graphs*, first arXiv posting 2011-09-16, arXiv:1109.3556, https://arxiv.org/abs/1109.3556 .
2. F. Pasqualetti, S. Zampieri, and F. Bullo, *Controllability Metrics, Limitations and Algorithms for Complex Networks*, first arXiv posting 2013-08-06, arXiv:1308.1201, https://arxiv.org/abs/1308.1201 .
3. T. H. Summers and J. Lygeros, *Optimal Sensor and Actuator Placement in Complex Dynamical Networks*, first arXiv posting 2013-06-11, arXiv:1306.2491, https://arxiv.org/abs/1306.2491 .
