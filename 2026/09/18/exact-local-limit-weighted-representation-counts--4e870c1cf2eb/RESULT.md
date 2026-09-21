# Exact local-limit asymptotics for weighted representation partitions

## Statement

For an integer \(k>1\), a set \(A\subseteq\mathbb N\), and \(n\ge0\), write
\[
D_A(n)=R_{1,k}(A,n)-R_{1,k}(\mathbb N\setminus A,n),
\]
where \(R_{1,k}(A,n)\) counts solutions of \(n=a_1+ka_2\) with \(a_1,a_2\in A\).
For an integer \(c\), define
\[
F_{k,c}(T)=\#\{A\subseteq\mathbb N:D_A(n)=c\text{ for every }n\ge T\}.
\]
Thus the function \(f_k(T)\) of Yang--Chen and Li--Xu--Yan is \(F_{k,0}(T)\).

**Theorem.** Fix \(k>1\), and let \(c_T\in\mathbb Z\) satisfy
\[
\frac{c_T}{\sqrt T}\longrightarrow \gamma\in\mathbb R.
\]
Then
\[
F_{k,c_T}(T)
\sim
\frac{(8k/\pi)^{k/2}}{\sqrt{k+3}}
\exp\!\left(-\frac{2k^2\gamma^2}{k+3}\right)
\frac{2^T}{T^{k/2}}.
\]
In particular, for every fixed integer \(c\),
\[
\boxed{
F_{k,c}(T)
\sim
C_k\frac{2^T}{T^{k/2}},\qquad
C_k=\frac{(8k/\pi)^{k/2}}{\sqrt{k+3}}.}
\]
Consequently
\[
f_k(T)\sim C_k\frac{2^T}{T^{k/2}}.
\]
For example,
\[
f_2(T)\sim \frac{16}{\pi\sqrt5}\frac{2^T}{T}.
\]
If \(1<k<\ell\), the comparison in Li--Xu--Yan sharpens to
\[
\frac{f_k(T)}{f_\ell(T)}
\sim
\frac{C_k}{C_\ell}T^{(\ell-k)/2}.
\]

## Context

Li, Xu and Yan proved in arXiv:2609.20385 (submitted 17 September 2026) that, for fixed \(k>1\) and fixed \(c\),
\[
F_{k,c}(T)\asymp_{k,c}\frac{2^T}{T^{k/2}}.
\]
Their result settles a problem of Yang and Chen by showing that \(f_k(T)\) and \(f_\ell(T)\) are not eventually equal when \(k\ne\ell\). The theorem above identifies the leading constant, shows that it is independent of every fixed \(c\), and gives the Gaussian profile when the prescribed eventual difference varies on the natural \(\sqrt T\) scale.

## Proof

Put
\[
\varepsilon_j=\begin{cases}1,&j\in A,\\-1,&j\notin A.\end{cases}
\]
If \(n=kq+s\), \(0\le s<k\), then the elementary identity
\[
2D_A(n)=\sum_{j=0}^{q}\varepsilon_j+\sum_{j=0}^{q}\varepsilon_{kj+s}
\tag{1}
\]
implies
\[
2D_A(n)-2D_A(n-k)=\varepsilon_{\lfloor n/k\rfloor}+\varepsilon_n.
\tag{2}
\]
For each residue \(s\), let \(n_s\) be the unique integer in \([T,T+k-1]\) congruent to \(s\pmod k\), and put \(q_s=(n_s-s)/k\). Equations (1)--(2) show that \(D_A(n)=c\) for all \(n\ge T\) if and only if the \(k\) boundary equations
\[
\sum_{j=0}^{q_s}\varepsilon_j+\sum_{j=0}^{q_s}\varepsilon_{kj+s}=2c,
\qquad 0\le s<k,
\tag{3}
\]
hold and
\[
\varepsilon_n=-\varepsilon_{\lfloor n/k\rfloor}\qquad(n\ge T+k).
\tag{4}
\]
Once \(\varepsilon_0,\ldots,\varepsilon_{T+k-1}\) are fixed, (4) uniquely determines every later sign. Hence \(F_{k,c}(T)\) is exactly the number of initial sign vectors satisfying (3).

Let \(\mathbf 1\in\mathbb R^k\) be the all-ones vector and \(e_0,\ldots,e_{k-1}\) the standard basis. For \(0\le x<T+k\), let \(v_x\in\mathbb Z^k\) be the coefficient vector of \(\varepsilon_x\) in (3):
\[
(v_x)_s=\mathbf 1_{x\le q_s}+\mathbf 1_{x\equiv s\pmod k}.
\tag{5}
\]
The second indicator in (5) needs no upper cutoff: among integers at most \(T+k-1\) having residue \(s\), the largest is precisely \(n_s\).

Write \(T=ka+b\) with \(0\le b<k\). Then
\[
q_s=\begin{cases}a+1,&s<b,\\a,&s\ge b.\end{cases}
\]
It follows that all but one column have one of two simple forms:
\[
v_x=\mathbf1+e_{x\bmod k}\quad(0\le x\le a),
\qquad
v_x=e_{x\bmod k}\quad(a+2\le x<T+k),
\tag{6}
\]
while \(x=a+1\) contributes one bounded exceptional column. Therefore, for every residue \(r\), the numbers of columns of the two types in (6) are respectively
\[
\frac{T}{k^2}+O_k(1),\qquad
\frac{(k-1)T}{k^2}+O_k(1).
\tag{7}
\]

Now take independent Rademacher signs \(\xi_x\). The normalized covariance matrix of
\(S_T=\sum_{x<T+k}\xi_xv_x\) has the limit
\[
\frac1T\sum_{x<T+k}v_xv_x^{\!t}\longrightarrow
\Sigma_k
=\frac1{k^2}\sum_{r=0}^{k-1}
\left((\mathbf1+e_r)(\mathbf1+e_r)^t+(k-1)e_re_r^t\right).
\]
Writing \(J=\mathbf1\mathbf1^t\), this simplifies to
\[
\Sigma_k=\frac{kI+(k+2)J}{k^2}.
\tag{8}
\]
Thus \(\Sigma_k\) has eigenvalue \(1/k\) with multiplicity \(k-1\) and eigenvalue \((k+3)/k\) in the \(\mathbf1\) direction. In particular,
\[
\det\Sigma_k=\frac{k+3}{k^k},
\qquad
\mathbf1^t\Sigma_k^{-1}\mathbf1=\frac{k^2}{k+3}.
\tag{9}
\]

It remains to take the lattice local limit. Fourier inversion gives, for \(t_T=2c_T\mathbf1\),
\[
\Pr(S_T=t_T)
=\frac1{(2\pi)^k}\int_{[-\pi,\pi]^k}
 e^{-it_T\cdot\theta}\prod_{x<T+k}\cos(v_x\cdot\theta)\,d\theta.
\tag{10}
\]
By (7), each coordinate column \(e_r\) occurs a positive proportion of the time. Hence away from the \(2^k\) torus points
\[
\theta\in\{0,\pi\}^k\pmod{2\pi}
\tag{11}
\]
the product in (10) is exponentially small. Near any point \(\pi\eta\) from (11),
\[
\cos(v_x\cdot(\pi\eta+z))
=(-1)^{v_x\cdot\eta}\cos(v_x\cdot z).
\]
For coordinate \(s\), the sum of all coefficients is \(2(q_s+1)\), so \(\sum_x(v_x)_s\) is even. Also \(t_T\) is coordinatewise even. Thus all \(2^k\) major arcs have the same phase and contribute equally.

On one major arc put \(z=y/\sqrt T\). Since the columns are uniformly bounded,
\[
\sum_x\log\cos(v_x\cdot z)
=-\frac12 y^t\left(\frac1T\sum_xv_xv_x^t\right)y+o(1)
\]
uniformly for bounded \(y\). The positive definiteness in (8), together with the repeated coordinate columns, supplies an integrable Gaussian majorant and makes the complement negligible. Since \(t_T/\sqrt T\to2\gamma\mathbf1\), (10) therefore yields
\[
\Pr(S_T=t_T)
\sim
\frac{2^k}{(2\pi T)^{k/2}\sqrt{\det\Sigma_k}}
\exp\!\left(-\frac12(2\gamma\mathbf1)^t\Sigma_k^{-1}(2\gamma\mathbf1)\right).
\]
Using (9),
\[
\Pr(S_T=t_T)
\sim
\frac{2^k k^{k/2}}{(2\pi T)^{k/2}\sqrt{k+3}}
\exp\!\left(-\frac{2k^2\gamma^2}{k+3}\right).
\tag{12}
\]
There are \(2^{T+k}\) initial sign vectors. Multiplying (12) by \(2^{T+k}\) gives the theorem.

## Verification

`artifacts/verify.py` independently constructs the boundary coefficient vectors from (3), checks their parity and limiting covariance determinant, and computes exact finite counts by integer dynamic programming for small and moderate \(k,T\). The reported normalized counts approach the constants in the theorem, including a nonzero \(c/\sqrt T\) check.

## Originality and limitations

To the best of our knowledge, the explicit constant \(C_k\), the exact asymptotic equivalence, and the \(c_T\asymp\sqrt T\) Gaussian profile are not in the prior literature located in the search. Li--Xu--Yan prove only two-sided order bounds, and their proof uses one-dimensional binomial estimates rather than a multivariate local limit. The earlier Yang--Chen line establishes structural and counting-order statements, and Yan--Shan gives exact formulas in a small-threshold regime rather than this large-\(T\) asymptotic.

The main residual originality risk is that the motivating preprint is extremely recent and a contemporaneous follow-up may not yet be indexed. The full text of the 2012 Yang--Chen paper was not independently inspected here; its relevant historical claims were checked through the 2026 paper and bibliographic records. The theorem above does not assert an error in any cited paper.

## References

1. S.-S. Li, Y.-T. Xu, X.-H. Yan, *A problem of Yang and Chen on weighted representation functions*, arXiv:2609.20385 (2026), https://arxiv.org/abs/2609.20385.
2. Q.-H. Yang, Y.-G. Chen, *Partitions of natural numbers with the same weighted representation functions*, Journal of Number Theory 132 (2012), 3047--3055.
3. X.-H. Yan, Y.-Q. Shan, *Partitions of the set of natural numbers and their weighted representation functions*, Ramanujan Journal 67 (2025), Article 53, https://doi.org/10.1007/s11139-025-01113-7.
4. Z. Qu, *A note on representation functions with different weights*, Colloquium Mathematicum 143 (2016), 105--112, https://doi.org/10.4064/cm6512-12-2015.
