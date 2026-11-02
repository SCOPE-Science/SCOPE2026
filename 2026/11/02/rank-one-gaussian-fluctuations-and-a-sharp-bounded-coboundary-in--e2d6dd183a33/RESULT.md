# Rank-one Gaussian fluctuations and a sharp bounded coboundary in the triangular tent map

## Finding
Let \(T:\Omega\to\Omega\) be the full-branch two-dimensional tent map defined below, and let \(\mu\) be normalized area. For the stationary centered coordinate process \(Q_j=(X_j-1,Y_j-1/3)^\mathsf T\), where \((X_j,Y_j)=T^j(X_0,Y_0)\), \((X_0,Y_0)\sim\mu\), its entire lag-covariance sequence is, for every integer \(k\geq1\),
\[
\Gamma_k=\mathbb E[Q_0Q_k^\mathsf T]
=\begin{pmatrix}0&0\\(-1/2)^{k-1}/12&(-1/2)^k/18\end{pmatrix},
\qquad
\Gamma_0=\begin{pmatrix}1/6&0\\0&1/18\end{pmatrix}.
\]
Consequently, the Green--Kubo covariance matrix exists and equals
\[
\Sigma=\lim_{n\to\infty}\frac1n\operatorname{Cov}\left(\sum_{j=0}^{n-1}Q_j\right)
=\begin{pmatrix}1/6&1/18\\1/18&1/54\end{pmatrix}
=\frac16\begin{pmatrix}1\\1/3\end{pmatrix}\begin{pmatrix}1&1/3\end{pmatrix}.
\]
There is a rank-one bivariate central limit theorem
\[
\frac1{\sqrt n}\sum_{j=0}^{n-1}Q_j\ \Longrightarrow\ (Z,Z/3)^\mathsf T,
\qquad Z\sim N(0,1/6).
\]
Among all centered real linear-coordinate observables \(f_{a,b}=a(X-1)+b(Y-1/3)\), the asymptotic variance is exactly \((a+b/3)^2/6\). It vanishes if and only if \((a,b)\) is proportional to \((1,-3)\). In that unique null direction, every orbit (including points on the switching boundary) satisfies the **sharp global bound**
\[
\sup_{z\in\Omega}\sup_{n\geq1}\left|\sum_{j=0}^{n-1}(X_j(z)-3Y_j(z))\right|=2.
\]

## Assumptions and scope
The compact triangle is
\[
\Omega=\{(x,y):0\leq x\leq1,\ 0\leq y\leq x\}\cup
\{(x,y):1\leq x\leq2,\ 0\leq y\leq2-x\}.
\]
It has Euclidean area \(1\). The deterministic map is
\[
T(x,y)=\begin{cases}(x+y,x-y),&0\leq x\leq1,\\
(2-x+y,2-x-y),&1\leq x\leq2.
\end{cases}
\]
Both formulas agree at \(x=1\). This is the canonical parameter \(t=1\) member of the planar tent family of Alves--Etubi (arXiv:2409.18805). All claims concern the fixed map \(T\), the normalized Lebesgue measure \(\mu\) on \(\Omega\), and the specified coordinate observables. No perturbation claim for \(t<1\) is made.

## Proof
**Full branches and invariant law.** Writing a target point as \((u,v)\), the two inverse branches are
\[
A(u,v)=((u+v)/2,(u-v)/2),\qquad
B(u,v)=(2-(u+v)/2,(u-v)/2).
\]
Each maps \(\Omega\) into its respective half triangle. Both branch Jacobians of \(T\) have absolute determinant \(2\), and each inverse branch contracts Euclidean distances by \(2^{-1/2}\). Therefore the normalized area is invariant: the Perron--Frobenius operator is
\[
(Pf)(u,v)=\tfrac12(f(A(u,v))+f(B(u,v))).
\]
Iterated inverse-branch cylinders have diameter tending to zero and measure \(2^{-n}\); their symbol process is the fair Bernoulli shift. Thus \((T,\mu)\) is mixing, in particular ergodic. Exact integration over the two half triangles gives \(\mathbb E X=1\), \(\mathbb E Y=1/3\), \(\operatorname{Var}(X)=1/6\), \(\operatorname{Var}(Y)=1/18\), and \(\operatorname{Cov}(X,Y)=0\).

**Transfer calculation.** Define \(q_x=x-1\) and \(q_y=y-1/3\). Direct substitution yields
\[
Pq_x=0,\qquad Pq_y=\tfrac12(q_x-q_y),
\qquad P^kq_y=\frac{(-1/2)^{k-1}}2(q_x-q_y)\quad(k\geq1).
\]
For \(\Gamma_k\) with the *initial coordinate indexing the row*, Perron--Koopman duality gives \((\Gamma_k)_{ij}=\langle P^k q_i,q_j\rangle_{L^2(\mu)}\). The stated formula follows from the initial moments. The entries form absolutely summable geometric series. Adding \(\Gamma_0+\sum_{k\geq1}(\Gamma_k+\Gamma_k^\mathsf T)\) gives the displayed \(\Sigma\), so the covariance-limit formula follows from the usual finite-sum identity by dominated convergence. In particular, the one-dimensional asymptotic variance equals \((a+b/3)^2/6\).

**Sharp coboundary and degenerate central limit.** Put \(H(x,y)=x-y\). Both branches satisfy \(T_1(x,y)-T_2(x,y)=2y\), so for every point
\[
x-3y=H(x,y)-H(T(x,y)).
\]
Every \((x,y)\in\Omega\) has \(0\leq H(x,y)\leq2\). Thus the sum telescopes and has absolute value at most \(2\). Equality occurs already at \(n=1\) and \((x,y)=(2,0)\), proving sharpness. Centering is automatic because \(\mathbb E[x-3y]=0\).

Now set \(D_j=q_x\circ T^j\), \(\mathcal F_j=T^{-j}\mathcal B\), a decreasing filtration. Since \(Pq_x=0\), \(\mathbb E[D_j\mid\mathcal F_{j+1}]=0\). Therefore the finite triangular arrays obtained by reversing \(D_0,\ldots,D_{n-1}\) are bounded martingale-difference arrays. Their conditional variance sum is
\[
\frac1n\sum_{j=0}^{n-1}(Pq_x^2)\circ T^{j+1}\ \longrightarrow\ \int q_x^2\,d\mu=\frac16
\]
almost surely by the ergodic theorem. Uniform boundedness gives the conditional Lindeberg condition. The martingale central limit theorem gives \(n^{-1/2}\sum_jD_j\Rightarrow N(0,1/6)\). Finally, the telescoping identity implies
\[
3\sum_{j=0}^{n-1}q_y\circ T^j=\sum_{j=0}^{n-1}q_x\circ T^j-(H-H\circ T^n),
\]
with last term uniformly bounded, proving the bivariate limit by Slutsky's theorem. This also identifies the only null direction independently of the covariance summation.

## Verification
The accompanying `checker.py` is a reproducible exact-arithmetic SymPy program. It checks branch inverses, determinants, invariant polynomial moments, the Perron images, 24 successive lag-covariance matrices, the Green--Kubo matrix and its null vector, and the coboundary identity on both branches. It was executed successfully. These finite algebraic checks corroborate the formulas; the mixing, infinite-series and martingale-limit conclusions follow from the arguments above, not from finite computation.

## Relationship to prior work
The original triangular map and its perturbative invariant-density and entropy analysis appear in Alves--Etubi, arXiv:2409.18805, first publicly posted 2024-09-27; its later revised version also identifies the two full branches. Alves--Pumariño, arXiv:1806.01095, provides the earlier entropy and measure-theoretic context and describes symbolic coding for this canonical map. These works establish background that is **not** claimed as new. The present claim concerns instead the full coordinate lag-covariance law, its degenerate Gaussian limit, the exact linear nullspace of asymptotic variance and a sharp all-orbit discrepancy bound.

González-Koda--Gutiérrez--Pérez-Espigares, arXiv:2507.10663 (2025), develops a large-deviation tilt construction for observables of a two-dimensional tent map. Its abstract is relevant, but the full mathematical paper was inaccessible during this comparison; no assertion is made that its statements exclude or imply the present result. The 2015 original dynamics paper of Pumariño and collaborators was available only in partial preview. These are explicit publication-priority risks, not independent verification.

## Limitations
The theorem treats only \(t=1\), not the entire parameter family. The Gaussian limit may be degenerate and does not imply independent coordinates. A functional CLT, parameter perturbation law, higher-order cumulants and a complete publication-priority search are not asserted. The two cited closely related papers without complete full-text access remain residual originality uncertainties. Independent mathematical audit has not been performed.

## References
1. J. F. Alves and O. R. Etubi, *Hölder continuity of invariant density and entropy for piecewise expanding maps*, arXiv:2409.18805v1 (2024-09-27); revised as *Modulus of continuity of invariant densities and entropies for piecewise expanding maps*, arXiv:2409.18805v2 (2025-02-25). https://arxiv.org/abs/2409.18805
2. J. F. Alves and A. Pumariño, *Entropy formula and continuity of entropy for piecewise expanding maps*, arXiv:1806.01095 (2018); *Ann. Inst. H. Poincaré Anal. Non Linéaire* **38** (2021), 91--108. https://arxiv.org/abs/1806.01095
3. A. Pumariño, J. Á. Rodríguez, J. C. Tatjer, and E. Vigil, *Chaotic dynamics for two-dimensional tent maps*, *Nonlinearity* **28** (2015), 407--434, DOI:10.1088/0951-7715/28/2/407.
4. Y. K. González-Koda, R. Gutiérrez, and C. Pérez-Espigares, *Making rare events typical in \(d\)-dimensional chaotic maps*, arXiv:2507.10663 (2025). https://arxiv.org/abs/2507.10663
