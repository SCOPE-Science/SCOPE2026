# Sharp positivity transition for quadratic fastest-mixing kernels on complete bipartite graphs

## Finding
Let \(2\le p\le q\) be integers, \(G=K_{p,q}\), \(L\) its unweighted combinatorial Laplacian, and
\[
P_{\alpha,\beta}=I-\alpha L+\beta L^2.
\]
Among all real \(\alpha,\beta\) for which \(P_{\alpha,\beta}\) is entrywise nonnegative, the *unique* pair minimizing the second-largest eigenvalue modulus (SLEM) of \(P_{\alpha,\beta}\) is as follows. Define the positivity threshold
\[
q_c(p)=\frac{p^2}{p-2}\qquad(p\ge3).
\]
In the alternating-spectrum regime \(p=2\), or \(p\ge3\) with \(q\le q_c(p)\), the answer is
\[
\beta_* =\frac{2}{p(p+3q)},\qquad
\alpha_* =\frac{2(2p+q)}{p(p+3q)},\qquad
\mu_* =\frac{q-p}{p+3q}.
\]
For \(p\ge3\) and \(q\ge q_c(p)\), the answer is
\[
\beta_* =\frac{1}{q(2p-1)},\qquad
\alpha_* =\frac{q+2p}{q(2p-1)},\qquad
\mu_* =\frac{(p-1)q-p^2}{q(2p-1)}.
\]
The two prescriptions coincide at equality. At strictly larger \(q\) the holding probability at every vertex in the \(p\)-vertex (higher-degree) part is zero; at smaller \(q\) it is positive. The optimal kernel is symmetric and doubly stochastic in either regime. The spectral unconstrained formula in the first regime follows from established second-order polynomial minimax theory; the added conclusion is the exact *entrywise-stochasticity boundary* and its distinct optimal formula beyond that boundary.

For fixed \(p\ge3\), as \(q\to\infty\),
\[
\mu_*\longrightarrow \frac{p-1}{2p-1}<\frac12.
\]
By contrast, if the kernel must be a product of two individually nonnegative one-hop matrices \((I-\gamma_2 L)(I-\gamma_1 L)\), its SLEM is at least \((1-p/q)^2\to1\). Thus enforcing positivity only on the *combined* two-hop filter is quantitatively different from enforcing it at both intermediate steps.

## Assumptions and scope
The graph is simple, unweighted and connected; both parts have at least two vertices, and \(p\le q\). The design class consists *only* of quadratic polynomials in this fixed Laplacian, with constant term one; the decision variables \(\alpha,\beta\) are real and otherwise unrestricted. Entrywise nonnegativity is imposed on the completed polynomial kernel, not on a hypothetical intermediate factor. Because \(L\mathbf1=0\), all such kernels have row sums one; symmetry then gives column sums one. No assertion is made that this kernel is optimal among all stochastic kernels on the squared graph (that broader class contains the all-ones averaging kernel and may attain zero SLEM).

The SLEM is the largest modulus among eigenvalues on the subspace orthogonal to \(\mathbf1\). The condition \(p,q\ge2\) ensures all three positive Laplacian eigenvalues occur, except that two coincide when \(p=q\). At \(p=q\), \(\mu_*=0\) and the unique optimum is exactly the uniform averaging kernel \(\mathbf1\mathbf1^T/(2p)\).

## Proof
**Spectrum and positivity.** In block order with \(p\) vertices first, the Laplacian and its square have blocks
\[
L=\begin{pmatrix}qI_p&-J_{p\times q}\\-J_{q\times p}&pI_q\end{pmatrix},\quad
L^2=\begin{pmatrix}q^2I_p+qJ_p&-(p+q)J_{p\times q}\\-(p+q)J_{q\times p}&p^2I_q+pJ_q\end{pmatrix}.
\]
The positive Laplacian eigenvalues are \(p\) (multiplicity \(q-1\)), \(q\) (multiplicity \(p-1\)), and \(N=p+q\) (multiplicity one). Writing \(f(t)=1-\alpha t+\beta t^2\), we consequently minimize
\[
\mu(\alpha,\beta)=\max\{|f(p)|,|f(q)|,|f(N)|\}.
\]
All off-diagonal entries and both diagonal types are nonnegative exactly when
\[
\beta\ge0,\quad \alpha\ge N\beta,\quad
1-q\alpha+q(q+1)\beta\ge0,\quad
1-p\alpha+p(p+1)\beta\ge0.\tag{1}
\]
Necessity follows from within-part off-diagonals \(q\beta,p\beta\), cross-part entries \(\alpha-N\beta\), and the two diagonal types. Sufficiency follows by exhaustion of the entry types.

**Unconstrained minimax and its feasible range.** For \(p<q\), the unconstrained minimax of a quadratic \(f\) with \(f(0)=1\) on \(\{p,q,N\}\) equioscillates:
\[
f(p)=f(N)=\mu_0,\qquad f(q)=-\mu_0.
\]
Solving the three linear equations gives
\[
\beta_0=\frac2{p(p+3q)},\quad \alpha_0=(N+p)\beta_0,\quad
\mu_0=\frac{q-p}{p+3q}.
\]
For completeness, optimality and uniqueness do not require invoking a black-box approximation theorem: if a competing polynomial had all three absolute values at most \(\mu_0\), its difference \(h\) from this candidate would obey \(h(p)\le0\), \(h(q)\ge0\), \(h(N)\le0\). But \(h(t)/t\) is affine, so it cannot have the stated weak sign pattern at three strictly ordered points unless it vanishes identically. Thus the candidate is the unique unconstrained minimizer. When \(p=q\), two distinct positive spectral values are simultaneously annihilated, giving the same stated coefficients and unique zero-SLEM polynomial.

For the candidate, the cross-part entry equals \(p\beta_0>0\), the low-degree holding probability is \((q-p+2)/(p+3q)>0\), and the high-degree holding probability is
\[
1-\frac{2q(2p-1)}{p(p+3q)}.
\]
This last number is nonnegative if and only if \((p-2)q\le p^2\); that inequality is automatic when \(p=2\). The unconstrained minimizer is hence feasible precisely in the first regime and is then also the unique constrained minimizer.

**Saturation and sharp optimality beyond the threshold.** Suppose \(p\ge3\) and \((p-2)q>p^2\). Set
\[
\beta_s=\frac1{q(2p-1)},\qquad \alpha_s=(N+p)\beta_s.
\]
The high-degree diagonal is zero, the low-degree diagonal is \((p-1)(q-p)/[q(2p-1)]>0\), and the cross-part entry is \(p\beta_s>0\). The three nontrivial eigenvalues of the kernel are
\[
f(p)=f(N)=\mu_s=\frac{(p-1)q-p^2}{q(2p-1)},
\qquad f(q)=-\frac1{2p-1}.
\]
The assumed strict inequality is equivalent to \(\mu_s>1/(2p-1)\), so its SLEM is exactly \(\mu_s\).

For a feasible competitor write \(\alpha=\alpha_s+u\), \(\beta=\beta_s+v\). The high-degree holding inequality (1), active at the candidate, forces \(u\le(q+1)v\). If \(v>0\), then
\[
f(N)-\mu_s=N(-u+Nv)\ge N(p-1)v>0.
\]
If \(v<0\), then
\[
f(p)-\mu_s=p(-u+pv)\ge p(p-q-1)v>0,
\]
using \(q\ge p\). If \(v=0\), feasibility forces \(u\le0\), and \(f(p)\ge\mu_s\) with equality only if \(u=0\). Therefore every different feasible pair has SLEM *strictly greater* than \(\mu_s\). This establishes sharp optimality and uniqueness on the second branch, including the matching formulas at the shared threshold.

**Two individually stochastic steps.** A first-order factor \(I-\gamma L\) is nonnegative exactly for \(0\le\gamma\le1/q\). Its eigenvalue on the \(p\)-eigenspace is \(1-\gamma p\). For any two such factors their product has a \(p\)-eigenvalue at least \((1-p/q)^2\), hence that lower bound holds for SLEM. For fixed \(p\ge3\), the second-branch formula tends to \((p-1)/(2p-1)\). The claimed strict asymptotic separation follows.

## Verification
Run `python verify_quadratic_biclique.py` with Python 3, NumPy and SciPy. The supplied program evaluates the rational formulas and all entrywise constraints across 1,547 parameter pairs, compares with an independently constructed three-variable linear program, constructs full matrices for smaller graphs, and tests the two-factor barrier. During preparation it passed **14,188 checks**. Exact rational identities corroborate the algebra and matrix/optimization tests detect implementation errors; finite testing is not the proof of the theorem for all \(p,q\).

## Relationship to prior work
Boyd, Diaconis and Xiao develop semidefinite formulations for fastest-mixing *one-hop* Markov chains. Boyd, Diaconis, Parrilo and Xiao give explicit formulas for the standard one-hop problem on \(K_{p,q}\), but their admissible matrices do not incorporate the within-part two-hop entries of the present polynomial. Apers and Sarlette establish the unconstrained second-order polynomial filtering framework and discuss \(K_{p,q}\); their Section 2 assumes polynomial filters without entrywise Markov positivity. The first branch's unconstrained minimax behavior is therefore known in broader form, and **is not claimed as new**. The result here determines the *exact positivity boundary* at which that known polynomial ceases to be Markov, and proves the distinct constrained optimum, uniqueness, zero-holding transition and two-stochastic-factor separation beyond that boundary. No inspected source supplies that combined constrained classification.

## Limitations
The result does not optimize arbitrary stochastic transition matrices supported by the squared graph, does not assert a gain from nonnegative intermediate updates, and does not address nonuniform edge weighting or robustness to link deletion. A two-hop polynomial kernel can require signed intermediate computations even while its completed transition matrix is nonnegative. The known unconstrained result gives much of the first regime; bibliographic coverage of the exact constrained specialization is not exhaustive, so an unindexed equivalent remains possible. Independent scientific audit has not been performed.

## References
1. S. Apers and A. Sarlette, *Accelerating Consensus by Spectral Clustering and Polynomial Filters*, arXiv:1503.01269v1, 4 March 2015, especially Sections 1, 2, 2.1, 3 and 4. https://arxiv.org/abs/1503.01269
2. S. Boyd, P. Diaconis and L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667–689, DOI:10.1137/S0036144503423264. https://web.stanford.edu/~boyd/papers/pdf/fmmc.pdf
3. S. Boyd, P. Diaconis, P. Parrilo and L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, arXiv:0709.0955v1, 6 September 2007, especially Sections 3.1.2 and 5.3.1. https://arxiv.org/abs/0709.0955
