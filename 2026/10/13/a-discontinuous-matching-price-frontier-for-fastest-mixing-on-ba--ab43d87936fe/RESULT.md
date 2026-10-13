# A discontinuous matching-price frontier for fastest mixing on balanced bicliques

## Finding
Fix an integer \(n\ge3\) and a price \(t>0\). Let \(G=K_{n,n}\), with vertex classes \(U=\{u_1,\ldots,u_n\}\) and \(V=\{v_1,\ldots,v_n\}\). The perfect-matching edges \(u_iv_i\) have unit-conductance price \(t\), and all other edges \(u_iv_j\), \(i\ne j\), have price \(1\). Among all individually chosen nonnegative conductances \(w_{ij}\) satisfying
\[
t\sum_{i=1}^n w_{ii}+\sum_{i\ne j}w_{ij}=1,
\]
maximize the second-smallest eigenvalue \(\lambda_2(L(w))\) of the weighted graph Laplacian, equivalently the spectral gap of the symmetric continuous-time Markov generator \(-L(w)\).

Set
\[
\tau_n=\frac{2(n-1)}{n-2}.
\]
The exact optimum is
\[
\boxed{\lambda_2^*(n,t)=
\begin{cases}
1/(t+n-1),&0<t\le\tau_n,\\
(n-2)/(n(n-1)),&t\ge\tau_n.
\end{cases}}
\]
At equality, the two formulas agree. The **entire set** of globally optimal edge allocations, without a symmetry assumption, is the following:

- If \(0<t<\tau_n\), the optimizer is unique and assigns \(w_{ij}=1/[n(t+n-1)]\) to **every** edge, even though matching edges have a different price.
- If \(t>\tau_n\), the optimizer is unique and assigns \(w_{ii}=0\), \(w_{ij}=1/[n(n-1)]\) for \(i\ne j\). The resulting crown graph remains connected.
- If \(t=\tau_n\), all and only the optimal allocations are \(w_{ii}=a\), \(w_{ij}=b\) for \(i\ne j\), where \(0\le a\le b\) and \(nt a+n(n-1)b=1\).

Thus the optimal matching-edge rate has a positive left limit and zero right limit at \(\tau_n\), while the optimal gap is continuous with a kink. The threshold decreases from \(4\) at \(n=3\) toward \(2\) as \(n\to\infty\). Just below the threshold, the matching edges consume a fraction tending to \(2/n\) of the unit budget.

## Assumptions and scope
All graph edges join different vertex classes. The matching is fixed but arbitrary; relabeling does not affect the conclusion. Rates may be zero, so the feasible family includes graphs with deleted edges; the optimizer always has positive spectral gap. The objective is the **continuous-time Laplacian gap**, not discrete-time second-largest eigenvalue modulus and not effective-resistance/Kirchhoff-index minimization. There are no individual upper bounds on conductances, and every price is strictly positive. The normalization is one unit of total price-weighted conductance.

## Proof
Write \(W=(w_{ij})_{1\le i,j\le n}\), and let \(A=\sum_iw_{ii}\) and \(B=\sum_{i\ne j}w_{ij}\). Then \(tA+B=1\), with \(A,B\ge0\). The Laplacian is
\[
L(W)=\begin{pmatrix}
\operatorname{diag}(W\mathbf 1)&-W\\
-W^{\mathsf T}&\operatorname{diag}(W^{\mathsf T}\mathbf1)
\end{pmatrix}.
\]
Introduce the two orthogonal subspaces of \(\mathbf1_{2n}^{\perp}\),
\[
E_+=\{(x,x):\mathbf1_n^{\mathsf T}x=0\},\qquad
E_-=\{(x,-x):\mathbf1_n^{\mathsf T}x=0\},
\]
each of dimension \(n-1\), and their orthogonal projectors \(P_+\) and \(P_-\). A matching-edge incidence vector has squared projection length \(0\) onto \(E_+\) and \(2(n-1)/n\) onto \(E_-\). For a nonmatching edge these squared lengths are \(1\) and \((n-2)/n\), respectively. Since every Rayleigh quotient on \(\mathbf1_{2n}^{\perp}\) is at least \(\lambda_2\), averaging the Rayleigh quotients over orthonormal bases of the two subspaces gives
\[
\lambda_2(L(W))\le
\min\left\{\frac{B}{n-1},
\frac{2(n-1)A+(n-2)B}{n(n-1)}\right\}.
\tag{1}
\]
This bound is valid for every individual allocation, not merely for symmetric weights.

Substitute \(B=1-tA\). The first expression in (1) decreases with \(A\), while the second has slope
\[
\frac{2(n-1)-(n-2)t}{n(n-1)}.
\]
When \(t<\tau_n\), this slope is positive and the maximum of the lower envelope occurs uniquely at \(A=1/(t+n-1)\), \(B=(n-1)/(t+n-1)\). When \(t>\tau_n\), both expressions are decreasing and their minimum is maximized only at \(A=0,B=1\). At \(t=\tau_n\), the second expression is constant, and the maximizing interval is \(0\le A\le1/(t+n-1)\), equivalently \(0\le a\le b\) after symmetry is established.

To prove attainment, assign conductance \(a\ge0\) to every matching edge and \(b>0\) to every nonmatching edge. The bipartite adjacency block is \((a-b)I+bJ\), and the common vertex degree is \(d=a+(n-1)b\). The complete Laplacian spectrum, with multiplicities, is
\[
\boxed{0\ (1),\quad 2d\ (1),\quad nb\ (n-1),\quad
[2a+(n-2)b]\ (n-1).}
\tag{2}
\]
Indeed, the four invariant orthogonal summands are the constant vector; \((\mathbf1_n,-\mathbf1_n)\); \(E_+\); and \(E_-\), respectively. For \(a\le b\), the gap is \(2a+(n-2)b\), equal to the second expression in (1). The allocations stated above have \(a\le b\), satisfy the budget, and attain their upper bounds; the formulas for the optimal value follow.

It remains to prove that **there are no asymmetric optimal allocations**. For every maximizing total \(A\) found above, the second trace bound in (1) equals the optimal gap. Since \(L-\lambda_2 I\) is positive semidefinite on \(\mathbf1_{2n}^{\perp}\), equality in the trace bound forces every vector in \(E_-\) to be a \(\lambda_2\)-eigenvector. Consequently, for all \(x\perp\mathbf1_n\),
\[
[\operatorname{diag}(W\mathbf1)+W]x=\lambda_2 x,
\qquad
[\operatorname{diag}(W^{\mathsf T}\mathbf1)+W^{\mathsf T}]x=\lambda_2 x.
\tag{3}
\]
Any matrix acting as \(\lambda_2 I\) on \(\mathbf1_n^{\perp}\) must have the form \(\lambda_2 I+v\mathbf1_n^{\mathsf T}\). Comparing the off-diagonal entries of the two matrices in (3) shows that \(w_{ij}=v_i=u_j\) whenever \(i\ne j\). The bipartite incidence relation \(i\ne j\) is connected for \(n\ge3\), so all nonmatching weights equal one common value \(b\). Comparing diagonal entries in (3) then gives \(2w_{ii}+(n-2)b=\lambda_2\), forcing all matching weights to equal one common value \(a\). The scalar optimization already established therefore exhausts **every** global optimizer.

At \(t<\tau_n\), \(a=b\), and the optimal gap has multiplicity \(2n-2\). At \(t>\tau_n\), \(a=0<b\), and the gap has multiplicity \(n-1\). On the critical optimal interval, the multiplicity is \(n-1\) except at its endpoint \(a=b\), where it is \(2n-2\).

## Verification
The standalone `verify_matching_spectral.py` uses Python's standard-library exact rational arithmetic. It verifies the explicit \(2n\)-vertex eigenbasis for the claimed family, the two projector trace bounds, budget normalization, feasible-allocation comparisons, and both endpoints and interior points of the critical interval. Running `python3 verify_matching_spectral.py` yielded:

`VERIFY_OK 693 exact eigenvector equations; 126 projector bounds; 1260 feasible-allocation certificates; 28 critical-family spectra`

These are finite consistency checks. The theorem for all integers \(n\ge3\), all real prices \(t>0\), and all real feasible conductances follows from the analytical proof above, including its equality case.

For illustration, at \(n=3,t=3\) the unique optimizer is \(a=b=1/15\) with gap \(1/5\); simply deleting the matching gives a lower gap \(1/6\). At \(t=4\), the entire family \(0\le a\le b\) with \(12a+6b=1\) is optimal.

## Relationship to prior work
Sun, Boyd, Xiao and Diaconis [1] established the general continuous-time fastest-mixing semidefinite optimization problem under price-weighted rate constraints, including its geometric dual, and analyzed paths and cycles. Their general framework includes this graph as an instance, but it does not state the present explicit full optimal-face classification and sharp matching-price threshold. Boyd, Diaconis, Parrilo and Xiao [2] used graph symmetries to solve discrete-time mixing problems and included complete bipartite graphs without a distinguished priced matching; their objective is the second-largest eigenvalue modulus and has different rate constraints. Triyani, Oktriyansa and Nurshiami [3] computed the unweighted crown-graph Laplacian spectrum, corresponding to the deleted-matching endpoint of (2); a fixed-graph spectrum does not select optimal conductances as prices vary.

The optimization proof here derives a new pair of global trace certificates for this two-price network, then uses equality-rigidity to classify individual optimal weights rather than only exhibiting an orbit-constant optimizer. The claimed contribution is the specialized exact classification, not the general semidefinite formulation, graph eigenvalue definitions, or the fixed-weight crown spectrum.

## Limitations
The conclusion does not treat \(n=2\), directed or discrete-time generators, unequal vertex stationary masses, price heterogeneity within either edge class, individual rate caps, or other objectives. A general optimization framework can recover optimal values algorithmically for finite graphs; the claim is the explicit all-size solution and optimizer classification. The literature comparison is limited to inspected sources and searches, not a proof that no equivalent theorem exists elsewhere. Independent validation has not been performed.

## References
[1] J. Sun, S. Boyd, L. Xiao, P. Diaconis, “The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem,” *SIAM Review* 48 (2006), 681–699, DOI: 10.1137/S0036144504443821; published electronically 2006-11-02. Public full text: https://stanford.edu/~boyd/papers/pdf/fmmp.pdf.

[2] S. Boyd, P. Diaconis, P. Parrilo, L. Xiao, “Fastest Mixing Markov Chain on Graphs with Symmetries,” *SIAM Journal on Optimization* 20 (2009), 792–819, DOI: 10.1137/070689413. Public full text: https://stanford.edu/~boyd/papers/pdf/fast_mix_symm.pdf.

[3] Triyani, R. Oktriyansa, S. R. Nurshiami, “Spektrum Laplace Graf Mahkota dan Graf Benteng,” *PYTHAGORAS* 19 (2024), 27–36, DOI: 10.21831/pythagoras.v19i1.60818. Public full text: https://journal.uny.ac.id/index.php/pythagoras/article/download/60818/pdf.
