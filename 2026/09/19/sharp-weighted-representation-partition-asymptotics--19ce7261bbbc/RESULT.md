# Sharp asymptotics and a Gaussian profile for weighted-representation partitions

## Result

Fix an integer \(k\ge 2\). For \(A\subseteq\mathbb N\), let
\[
R_{1,k}(A,n)=\#\{(a_1,a_2)\in A^2:n=a_1+ka_2\}
\]
and
\[
D_A(n)=R_{1,k}(A,n)-R_{1,k}(\mathbb N\setminus A,n).
\]
For an integer \(c\) and \(T\ge1\), define
\[
F_{k,c}(T)=\#\{A\subseteq\mathbb N:D_A(n)=c\text{ for every }n\ge T\}.
\]
The recent theorem of Li--Xu--Yan proves, for fixed \(k\) and fixed \(c\),
\[
F_{k,c}(T)\asymp_{k,c}\frac{2^T}{T^{k/2}}.
\]
The estimate can be sharpened to an explicit local-limit asymptotic.

**Theorem.** Let \(c_T\in\mathbb Z\) satisfy
\[
\frac{c_T}{\sqrt T}\longrightarrow \lambda\in\mathbb R.
\]
Then
\[
F_{k,c_T}(T)
\sim
C_k\exp\!\left(-\frac{2k^2\lambda^2}{k+3}\right)
\frac{2^T}{T^{k/2}},
\]
where
\[
\boxed{\displaystyle
C_k=\frac{(8k/\pi)^{k/2}}{\sqrt{k+3}}.}
\]
In particular, for every fixed integer \(c\),
\[
\boxed{\displaystyle
F_{k,c}(T)\sim C_k\frac{2^T}{T^{k/2}},}
\]
so the leading constant is independent of the fixed eventual difference \(c\).

Writing \(f_k(T)=F_{k,0}(T)\), one obtains
\[
\boxed{\displaystyle
f_k(T)\sim \frac{(8k/\pi)^{k/2}}{\sqrt{k+3}}\frac{2^T}{T^{k/2}}.}
\]
Consequently, if \(1<k<\ell\), then
\[
\frac{f_k(T)}{f_\ell(T)}
\sim
\frac{C_k}{C_\ell}T^{(\ell-k)/2}.
\]

## Finite sign reduction

Write \(\varepsilon_j=1\) if \(j\in A\) and \(\varepsilon_j=-1\) otherwise. Li--Xu--Yan prove that if \(n=kq+s\), \(0\le s<k\), then
\[
2D_A(n)=\sum_{j=0}^{q}\varepsilon_j+\sum_{j=0}^{q}\varepsilon_{kj+s},
\]
and that \(D_A(n)=c\) for all \(n\ge T\) is equivalent to the \(k\) boundary equalities
\[
D_A(n)=c\qquad(T\le n\le T+k-1)
\]
together with
\[
\varepsilon_n=-\varepsilon_{\lfloor n/k\rfloor}\qquad(n\ge T+k).
\]
Thus every choice of the first \(T+k\) signs has at most one infinite extension.

For each \(0\le s<k\), let \(n_s\) be the unique integer in \([T,T+k-1]\) congruent to \(s\pmod k\), and write \(n_s=kq_s+s\). Define
\[
L_s=\sum_{j=0}^{q_s}\varepsilon_j+
\sum_{j=0}^{q_s}\varepsilon_{kj+s}.
\]
Then
\[
F_{k,c}(T)=
\#\{\varepsilon\in\{-1,1\}^{T+k}:L_s=2c\text{ for every }s\}.
\]
Let \(v_x\in\mathbb Z^k\) be the coefficient vector of \(\varepsilon_x\) in \((L_0,\dots,L_{k-1})\). Under independent uniform signs,
\[
L=(L_0,\dots,L_{k-1})=\sum_{x=0}^{T+k-1}v_x\varepsilon_x,
\]
and
\[
F_{k,c}(T)=2^{T+k}\Pr(L=2c\mathbf 1).
\]

## Covariance

Let
\[
\Sigma_T=\sum_x v_xv_x^{\mathsf T}.
\]
Since \(q_s=T/k+O_k(1)\) and \(n_s=T+O_k(1)\), direct intersection counts between the two sums defining each \(L_s\) give
\[
\Sigma_T=T B_k+O_k(1)
\]
entrywise, with
\[
B_k=\frac1k I_k+\frac{k+2}{k^2}J_k,
\]
where \(J_k\) is the all-ones matrix. Equivalently,
\[
(B_k)_{ss}=\frac{2(k+1)}{k^2},\qquad
(B_k)_{st}=\frac{k+2}{k^2}\quad(s\ne t).
\]
The eigenvalues of \(B_k\) are
\[
\frac1k\quad\text{with multiplicity }k-1,
\qquad
\frac{k+3}{k}\quad\text{on }\mathbb R\mathbf1,
\]
so
\[
\det B_k=\frac{k+3}{k^k}.
\]

## Lattice local limit

Fourier inversion gives, for an attainable \(y\in(2\mathbb Z)^k\),
\[
\Pr(L=y)=\frac1{(2\pi)^k}
\int_{[-\pi,\pi]^k}
 e^{-i\theta\cdot y}
 \prod_x\cos(\theta\cdot v_x)\,d\theta.
\]
Set \(Q=\max_s q_s\) and
\[
P_s=\{x:Q<x\le n_s,\ x\equiv s\pmod k\}.
\]
For \(x\in P_s\), one has \(v_x=e_s\), and Li--Xu--Yan's count gives
\[
|P_s|=\frac{k-1}{k^2}T+O_k(1).
\]
Hence the only points of the Fourier torus where the integrand has modulus one are
\[
\pi\eta,\qquad \eta\in\{0,1\}^k.
\]
All \(2^k\) peaks contribute with the same sign: each coordinate coefficient sum equals \(2(q_s+1)\), and the target coordinates \(2c_T\) are even.

Near any peak, writing \(\theta=\pi\eta+h\),
\[
\sum_x\log\cos(h\cdot v_x)
=-\frac12h^{\mathsf T}\Sigma_T h+O_k(T\|h\|^4).
\]
Taking \(\|h\|\le T^{-2/5}\) and then \(h=z/\sqrt T\) gives the Gaussian integral with covariance \(B_k\). Outside these shrinking peak neighborhoods, the coordinate-only blocks \(P_s\) give exponential decay. Therefore, whenever \(c_T/\sqrt T\to\lambda\),
\[
\Pr(L=2c_T\mathbf1)
\sim
\frac{2^k}{(2\pi T)^{k/2}\sqrt{\det B_k}}
\exp\!\left[
-\frac1{2T}(2c_T\mathbf1)^{\mathsf T}
B_k^{-1}(2c_T\mathbf1)
\right].
\]
Since
\[
B_k^{-1}\mathbf1=\frac{k}{k+3}\mathbf1,
\]
the exponent tends to
\[
-\frac{2k^2\lambda^2}{k+3}.
\]
Multiplying by \(2^{T+k}\), using \(\det B_k=(k+3)/k^k\), yields exactly
\[
C_k=\frac{(8k/\pi)^{k/2}}{\sqrt{k+3}}.
\]

## Checks

The accompanying verification program independently constructs the finite coefficient vectors, counts the relevant sign solutions exactly for moderate \(T\), checks the covariance determinant, and compares fixed-\(c\) and \(c\asymp\sqrt T\) counts with the predicted constants. For example,
\[
C_2=2.277640138934967\ldots,\qquad
C_3=8.620181862007996\ldots.
\]
At \(k=2,T=120,c=0\), the normalized exact count is \(2.219102919464\); at \(k=3,T=90,c=0\), it is \(7.980166004492\). The slower finite-size convergence for \(k=3\) is consistent with the theorem and does not enter the proof.

## Literature context and originality boundary

Li--Xu--Yan (2026) prove only the two-sided order estimate \(F_{k,c}(T)\asymp 2^T/T^{k/2}\) for fixed \(c\); their proof uses coordinate blocks and binomial bounds but does not state a leading constant or a square-root-scale profile. Yan--Shan (2025) give exact formulas for a related counting function only in the small-threshold range \(t\le k\). Earlier weighted-representation papers address structural existence, finite-group analogues, or lower bounds for the representation function itself rather than the large-\(T\) enumeration considered here.

To the best of our knowledge, no prior source located in the searches states the explicit constant \(C_k\), the fixed-\(c\) asymptotic above, or the Gaussian \(c_T/\sqrt T\) profile. The 2012 Yang--Chen paper was not fully inspected; the 2026 primary source reports its relevant counting result as finiteness plus a much coarser exponential-scale statement. Because the motivating preprint is very recent, unindexed concurrent work remains a residual originality risk.

## Limitations

The theorem keeps \(k\) fixed and assumes \(c_T=O(\sqrt T)\) with a limiting ratio. No uniformity for growing \(k\), no moderate- or large-deviation theorem beyond this scale, and no optimized error term are claimed. The verification is finite computation supporting the formulas, not a substitute for the Fourier proof. No independent validation or formal proof-assistant verification is asserted.

## References

1. S.-S. Li, Y.-T. Xu, X.-H. Yan, *A problem of Yang and Chen on weighted representation functions*, arXiv:2609.20385 (2026). https://arxiv.org/abs/2609.20385
2. X.-H. Yan, Y.-Q. Shan, *Partitions of the set of natural numbers and their weighted representation functions*, Ramanujan J. 67 (2025), Article 53. https://doi.org/10.1007/s11139-025-01113-7
3. S.-S. Li, Y.-Q. Shan, X.-H. Yan, *Partitions of natural numbers and their weighted representation functions*, Bull. Aust. Math. Soc. 110 (2024), 12--18. https://doi.org/10.1017/S0004972723001053
4. S.-Q. Chen, Y. Ding, X. Lü, Y. Zhang, *Correct order on some certain weighted representation functions*, C. R. Math. 362 (2024), 547--552. https://doi.org/10.5802/crmath.573
5. Q.-H. Yang, Y.-G. Chen, *Partitions of natural numbers with the same weighted representation functions*, J. Number Theory 132 (2012), 3047--3055.
