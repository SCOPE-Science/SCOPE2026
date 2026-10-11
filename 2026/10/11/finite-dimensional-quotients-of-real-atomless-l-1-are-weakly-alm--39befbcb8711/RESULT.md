# Finite-dimensional quotients of real atomless \(L^1\) are weakly almost square

## Finding
Let \((\Omega,\Sigma,\mu)\) be an arbitrary nonzero finite atomless measure space, and \(Z\subset L^1(\mu;\mathbb R)\) an arbitrary finite-dimensional subspace. If \(r_n\) are Rademacher-type measurable signs, then for every \(f\in L^1(\mu)\),
\[
 \boxed{\displaystyle \lim_{n\to\infty}\inf_{z\in Z}\|r_nf-z\|_1=\|f\|_1.}
\tag{1}
\]
In particular, the quotient \(X=L^1(\mu;\mathbb R)/Z\) is **weakly almost square (WASQ)**: for every \(x\in S_X\) there exist \(y_n\in B_X\) such that
\[
 y_n\rightharpoonup0,\qquad\|y_n\|\to1,\qquad \|x+y_n\|\to1,\qquad\|x-y_n\|\to1.
\]
The exact limit in (1), valid for all finite-dimensional kernels rather than just an explicitly selected one, is part of the assertion. It is independent of the dimension or choice of \(Z\).

## Assumptions and scope
Everything is real-scalar. The finite measure \(\mu\) is nonzero and nonatomic. A Rademacher-type sequence is a sequence of \(\{-1,1\}\)-valued measurable functions \(r_n\) for which \(\int h r_n\,d\mu\to0\) holds for every \(h\in L^1(\mu)\); such sequences exist on all finite atomless measure spaces (Rodríguez--Rueda Zoca, Lemma 2.1). The quotient map \(q:L^1(\mu)\to X\) has the exact quotient norm
\[
 \|q(f)\|=\inf_{z\in Z}\|f-z\|_1.
\]
The WASQ property requires witnesses for **every** unit vector, not just a norm-dense subset.

## Proof
**1. Atomless signs.** For every finite atomless measure space there exist measurable signs \(r_n:\Omega\to\{-1,1\}\) such that
\[
 \int_\Omega h r_n\,d\mu\longrightarrow0
 \quad\text{for every }h\in L^1(\mu).
\]
This is the Rademacher-type sign lemma, for example Rodríguez--Rueda Zoca (2023), Lemma 2.1. It gives \(r_nf\rightharpoonup0\) in \(L^1(\mu)\) for each fixed \(f\in L^1(\mu)\).

**2. A quotient-norm lemma, including uniformity over a finite-dimensional kernel.** For every \(f\in L^1(\mu)\),
\[
 \lim_{n\to\infty}\inf_{z\in Z}\|r_nf-z\|_1=\|f\|_1.
\tag{1}
\]
For a *fixed* \(z\in Z\), the sign identity gives
\[
 \begin{aligned}
 \|r_nf-z\|_1
 &=\tfrac12\left(\|f-z\|_1+\|f+z\|_1\right)\\
 &\quad+\tfrac12\int_\Omega r_n\bigl(|f-z|-|f+z|\bigr)\,d\mu\\
 &\longrightarrow \int_\Omega\max\{|f|,|z|\}\,d\mu\ \geq\ \|f\|_1.
 \end{aligned}
\tag{2}
\]
The equality in the limit uses \((|a-b|+|a+b|)/2=\max\{|a|,|b|\}\) for real numbers. To justify the infimum in (1), suppose a subsequence has distance at most \(\|f\|_1-\varepsilon\). Choose nearly minimizing \(z_n\in Z\). Since \(\|z_n\|_1\leq\|r_nf-z_n\|_1+\|f\|_1\), these vectors are bounded. Finite dimensionality permits a convergent subsequence \(z_n\to z\in Z\); the \(L^1\)-norm is Lipschitz continuous in \(z\), contradicting (2). The upper bound in (1) follows by choosing \(z=0\). This step does not follow merely from pointwise convergence in (2) without the finite-dimensional compactness argument.

**3. WASQ for the quotient.** Fix \(x\in S_X\). In its coset choose \(f\in L^1(\mu)\) with \(q(f)=x\) and \(\|f\|_1=1\). Such a representative exists because minimizing \(\|f_0-z\|_1\) over the finite-dimensional space \(Z\) is a coercive continuous finite-dimensional optimization problem. Define \(y_n=q(r_nf)\). Then \(y_n\rightharpoonup0\), because quotienting is bounded linear and \(r_nf\rightharpoonup0\). By (1), \(\|y_n\|\to1\), while \(\|y_n\|\leq1\). Moreover
\[
 \begin{aligned}
 \|x\pm y_n\|
 &\leq\|(1\pm r_n)f\|_1
 =\int_\Omega |f|(1\pm r_n)\,d\mu\\
 &=1\pm\int_\Omega |f|r_n\,d\mu\longrightarrow1.
 \end{aligned}
\]
On the other hand, \(x\pm y_n\rightharpoonup x\), so weak lower semicontinuity of the norm gives \(\liminf_n\|x\pm y_n\|\geq\|x\|=1\). All required limits follow.


**4. Exactness and independence of auxiliary choices.** The limit (1) is valid for each \(f\), including non-minimizing representatives, and every Rademacher-type sign sequence, because the proof uses solely the weak-null sign property and compactness of bounded sets of \(Z\). The theorem does not require a special basis of \(Z\), a countably generated sigma-algebra or separability of \(L^1(\mu)\).

## Verification
The nonstandard point is passage from fixed-\(z\) convergence to convergence of the infimum: norm-bounded approximate minimizers have convergent subsequences **because \(Z\) is finite-dimensional**. Equation (2) above shows this limit cannot drop below \(\|f\|_1\), and choosing \(z=0\) gives the reverse inequality. The WASQ witnesses are explicitly \(q(r_nf)\), where \(f\) minimizes the quotient norm in its coset. All three limits and weak nullness are individually proved. No finite computation is used in place of the analytic argument.

## Relationship to prior work
Rodríguez--Rueda Zoca (2023) proves WASQ for atomless \(L^1\)-type spaces **before taking any quotient** and supplies the Rademacher-type sign lemma. Their proof does not assert (1) or control the quotient distance to an arbitrary finite-dimensional subspace. Since WASQ is norm-dependent, simple linear isomorphism or stability intuition cannot replace the exact quotient-norm argument.

One geometric motivation for investigating finite-dimensional quotients is that a finite compact **metric graph with all its edge points** has an isometric model as \(L^1\) of the disjoint edge intervals modulo the finite-dimensional space of cycle flows. A spanning tree identifies its fundamental cycles, and edgewise differentiation identifies \(\operatorname{Lip}_0\) with the annihilator of their signed edge indicators. The quotient theorem therefore provides a direct cycle-flow method for verifying WASQ in these spaces. **The metric-graph conclusion is not asserted as an independently novel claim:** the first version of Kaasik--Veeorg (2022), Theorem 3.1, explicitly claimed a stronger statement for all geodesic metric spaces. Its proof began with a reduction to finitely supported vectors; the later complete version (2023), Proposition 3.2, instead establishes only the finitely supported case and explicitly presents the general question as open. This revision means a stronger claim existed in the historical record, notwithstanding its later narrowing. The present finding is the arbitrary finite-dimensional \(L^1\)-quotient theorem and exact distance limit, which neither version states or implies. Freeman--Gartland's isomorphic \(L^1\) results do not control an arbitrary quotient norm and are not equivalent formulations of (1).

## Limitations
No claim is made for infinite-dimensional quotient kernels, spaces with atoms, the complex scalar field, arbitrary quasi-Banach spaces, or all geodesic metric spaces. The statement is **not** an assertion of priority over the geodesic-space theorem claimed in the 2022 first preprint. The proof relies on the real scalar identity \((|a-b|+|a+b|)/2=\max(|a|,|b|)\). Although targeted literature comparisons reveal no covering finite-dimensional quotient theorem, an unindexed equivalent may exist; no independent mathematical audit has been performed.

## References
1. J. Rodríguez and A. Rueda Zoca, *On weakly almost square Banach spaces*, arXiv:2301.07943 (first public 2023-01-19), especially Lemma 2.1 and Section 2, https://arxiv.org/html/2301.07943v1 .
2. J. K. Kaasik and T. Veeorg, *Weakly almost square Lipschitz-free spaces*, arXiv:2210.09158, **v1 first published 2022-10-17** and **v2 revised 2023-04-21**; compare v1 Theorem 3.1 with v2 Proposition 3.2 and Problem 1, https://arxiv.org/html/2210.09158v1 and https://arxiv.org/html/2210.09158v2 .
3. D. M. Freeman and C. Gartland, *Lipschitz Functions on Unions and Quotients of Metric Spaces*, arXiv:2212.08707 (first public 2022-12-16), Theorem A, https://arxiv.org/html/2212.08707v2 .
