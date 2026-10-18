# A sharp core-edge price threshold for fastest diffusion on a pendant clique

## Finding
Let \(m\ge2\) be an integer. Attach one pendant vertex to a distinguished vertex of the complete graph \(K_{m+1}\). Give each of the \(\binom m2\) edges not touching the distinguished vertex a linear conductance price \(t>0\); give all \(m\) edges from that vertex to the other clique vertices, and the pendant edge, unit price. Fix a total conductance expenditure \(B>0\). All conductances may be optimized **independently**, subject to nonnegativity.

Write \(\lambda_2\) for the second-smallest eigenvalue of the combinatorial weighted Laplacian. The unique maximizer has a sharp core-edge deletion threshold
\[
\tau_m=\frac{2(m+1)}m.
\]
For \(0<t<\tau_m\), set
\[
q=\sqrt{1-\frac{t(m-1)}{2m}},\qquad
C=m+1-\frac{(mq-1)^2}{m+2},
\]
and set
\[
x_0=\frac{2+q^{-1}}{m+2},\quad
y_0=\frac{m-q^{-1}}{m(m+2)},\quad
z_0=\frac{m+1+mq}{m+2}.
\]
The uniquely optimal conductances are \(\frac BC x_0\) on each distinguished-to-clique edge, \(\frac BC y_0\) on each edge inside the remaining clique, and \(\frac BC z_0\) on the pendant edge; the maximum spectral gap is \(B/C\). All three weights are strictly positive.

For \(t\ge\tau_m\), the unique optimum puts weight \(B/(m+1)\) on each of the \(m+1\) edges incident with the distinguished vertex, zero weight on every edge between other clique vertices, and has gap \(B/(m+1)\). **Uniqueness holds at equality** \(t=\tau_m\), unlike the flat optimal faces possible in other priced spectral-gap problems. In particular \(\tau_m\downarrow2\) as \(m\to\infty\).

## Assumptions and scope
Label the distinguished vertex \(h\), pendant vertex \(\ell\), and ordinary clique vertices \(v_1,\ldots,v_m\). The edge set is exactly \(h\ell\), \(hv_i\), and \(v_iv_j\) for \(1\le i<j\le m\); in particular, \(\ell v_i\) is never an edge. For edge conductances \(w_e\ge0\), define \(L(w)=\sum_e w_e(e_i-e_j)(e_i-e_j)^\mathsf T\). The budget equation is
\[
 w_{h\ell}+\sum_i w_{hv_i}+t\sum_{i<j}w_{v_iv_j}=B.
\]
The problem maximizes \(\lambda_2(L(w))\) over these weights. It is continuous-time, symmetric, unnormalized Laplacian diffusion, not discrete-time stochastic-matrix modulus minimization. No restriction to invariant weights is made in the optimization.

## Proof
**Step 1: A positive-semidefinite global cost certificate.** Write \(N=m+2\) and \(\Pi=I-\mathbf1\mathbf1^\mathsf T/N\). Let \(P_U\) be the orthogonal projection onto the subspace supported on the \(v_i\) coordinates with their sum zero: its clique block is \(I_m-\mathbf1_m\mathbf1_m^\mathsf T/m\), and all other entries vanish. Define
\[
(q,\alpha)=
\begin{cases}
\left(\sqrt{1-t(m-1)/(2m)},\ t/2\right),&0<t<\tau_m,\\
\left(1/m,\ (m+1)/m\right),&t\ge\tau_m,
\end{cases}
\]
and the vector, in the order \(h,v_1,\ldots,v_m,\ell\),
\[
u=(1-mq,\ \underbrace{1+2q,\ldots,1+2q}_{m\ \mathrm{entries}},\ -(m+1+mq)).
\]
Then \(u\perp\mathbf1\), \(u\perp\operatorname{ran}P_U\), and
\[
Y=\alpha P_U+\frac{uu^\mathsf T}{(m+2)^2}\succeq0,
\qquad Y\mathbf1=0,\qquad \operatorname{rank}Y=m.
\]
Its exact squared edge lengths, \((e_i-e_j)^\mathsf T Y(e_i-e_j)\), are \(1\) for \(h\ell\), \(1\) for each \(hv_i\), and \(2\alpha\) for each \(v_iv_j\). The last number equals \(t\) in the mixed regime and equals \(\tau_m\le t\) in the deleted-core regime. (For the second type, the identity is \(\alpha(m-1)/m+q^2=1\).)

If \(\lambda_2(L(w))\ge1\), then \(L(w)-\Pi\succeq0\), so
\[
\text{expenditure}\ \ge\operatorname{tr}(YL(w))
\ge\operatorname{tr}Y.
\]
Direct evaluation yields \(\operatorname{tr}Y=C\) when \(t<\tau_m\), and \(\operatorname{tr}Y=m+1\) otherwise. By homogeneity, every budget-\(B\) design has \(\lambda_2\le B/\operatorname{tr}Y\).

**Step 2: Attainment and exact spectrum.** For \(t<\tau_m\), give each \(hv_i\), \(v_iv_j\), \(h\ell\) weight respectively \(x_0,y_0,z_0\). The \(m-1\)-dimensional ordinary-clique transverse subspace has eigenvalue \(x_0+m y_0=1\). The remaining three-dimensional invariant subspace (constant on the ordinary clique) has eigenvalues \(0,1,(m+2)x_0z_0\). Here \(q\in(1/m,1)\), \(x_0\ge3/(m+2)\), and \(z_0\ge1\), so the last eigenvalue exceeds \(1\). Thus \(\lambda_2=1\). Their expenditure is exactly
\[
m x_0+\binom m2 t y_0+z_0=C.
\]
For \(t\ge\tau_m\), the unit-weight star on \(m+1\) leaves has Laplacian eigenvalues \(0\), \(1\) (multiplicity \(m\)), and \(m+2\), with expenditure \(m+1\). Scaling both constructions by \(B/\operatorname{tr}Y\) attains the bound.

**Step 3: Global uniqueness, including the boundary.** In either construction let \(E\) be the \(m\)-dimensional eigenspace for eigenvalue \(1\). The certificate \(Y\) is positive definite on \(E\), with \(\operatorname{ran}Y=E\). For any other cost-normalized optimal Laplacian \(\widetilde L\) with \(\lambda_2(\widetilde L)=1\), equality in the two certificate inequalities implies
\[
(\widetilde L-\Pi)v=0\quad\hbox{for every }v\in E.
\]
Therefore \(\Delta=\widetilde L-L_*\) annihilates both \(E\) and \(\mathbf1\), a subspace of codimension one, so \(\Delta\) is a scalar multiple of \(gg^\mathsf T\), where \(g\) is a nonzero eigenvector for the single upper eigenvalue of \(L_*\). Both its pendant coordinate and all its ordinary-clique coordinates are nonzero: if either were zero, the eigenvector equations across the positive edges \(h\ell\) and \(hv_i\) would force every coordinate to vanish. But \(\Delta_{\ell,v_i}=0\), since those are nonedges in **both** admissible Laplacians. Hence the scalar is zero, and \(\widetilde L=L_*\). Individual edge weights are identifiable from off-diagonal Laplacian entries, proving unique global allocation.

## Verification
Run `python verify_pendant_clique.py` with Python 3, SymPy, and NumPy. The standalone checker completes 1,960 assertions, using exact rational matrix spectra and certificate identities for \(2\le m\le11\), and independent random nonuniform weighted-Laplacian competitors for \(2\le m\le9\). The analytical certificate and equality argument above prove the all-order and all-real-parameter result; the finite checks alone do not.

## Relationship to prior work
Sun, Boyd, Xiao, and Diaconis formulate the general fastest-mixing continuous-time process as a semidefinite optimization problem, derive the maximum-variance-unfolding dual, and explicitly solve path/cycle examples [1]. The present \(K_{m+1}\)-plus-one-leaf topology with three edge-price classes and its sharp price threshold are not among those identified examples. Boyd, Diaconis, Parrilo, and Xiao study symmetry reduction and discrete-time stochastic-matrix modulus minimization, including two cliques joined by a bridge [2]; that is neither this graph nor this objective. Fiedler's exact absolute-algebraic-connectivity results for trees [3] cover tree-only optimization principles relevant to the high-price star regime, but not the mixed regime on a clique with a pendant edge. The new contribution claimed here is the explicit all-order priced transition and global optimizer rigidity, **not** semidefinite duality, eigenvalue concavity, or symmetry averaging themselves.

## Limitations
This theorem applies only to one leaf attached to a clique, unit prices on spokes and the pendant edge, and a single positive price on edges inside the ordinary clique. It does not solve multiple-leaf pineapple graphs, arbitrary prices, nonsymmetric Markov generators, or discrete-time SLEM optimization. An equivalent unindexed specialization of general semidefinite eigenvalue optimization may exist; literature searches and inspected relevant statements cannot prove publication-level uniqueness. No independent validation has been performed.

## References
[1] J. Sun, S. Boyd, L. Xiao, P. Diaconis, “The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem,” *SIAM Review* 48 (2006), 681–699, DOI: 10.1137/S0036144504443821; published electronically 2006-11-02. Lawful public copy: https://web.stanford.edu/~boyd/papers/pdf/fmmp.pdf.

[2] S. Boyd, P. Diaconis, P. Parrilo, L. Xiao, “Fastest Mixing Markov Chain on Graphs with Symmetries,” *SIAM J. Optimization* 20 (2009), 792–819; original open preprint arXiv:0709.0955v1, https://arxiv.org/pdf/0709.0955.

[3] M. Fiedler, “Absolute Algebraic Connectivity of Trees,” *Linear and Multilinear Algebra* 26 (1990), 85–106, DOI: 10.1080/03081089008817967.
