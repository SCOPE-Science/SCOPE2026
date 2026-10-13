# A bridge-price phase transition for fastest mixing on asymmetric double stars

## Finding

Let \(T_{k,\ell}\) be the tree consisting of two adjacent hubs, with \(k\) leaves at one hub and \(\ell\) at the other, where integers \(k\ge\ell\ge1\). Put a nonnegative symmetric continuous-time transition rate \(w_e\) on every tree edge, assign unit price to each pendant edge, and price \(t>0\) to the hub-to-hub bridge. The normalized budget is \(\sum_{e\ \mathrm{pendant}} w_e+t w_{\mathrm{bridge}}=1\). Let \(L(w)\) be the weighted Laplacian, and maximize its second-smallest eigenvalue \(\lambda_2(L(w))\), the exponential convergence rate of the symmetric continuous-time Markov process to its uniform equilibrium.

Set \(q=\sqrt t\), \(N=k+\ell+2\), \(h=(2k\ell+k+\ell)/N\), and \(q_c=(k-\ell)/(\ell+1)\). Then the optimum is attained by a **unique** assignment of rates and equals \(1/Z\), where

\[
Z=2h(1+q)+\frac{h+1}{2}q^2+\frac{\big((k-\ell)-(\ell+1)q\big)_+^2}{N},\qquad (a)_+=\max\{a,0\}.
\]

For \(k>\ell\) and \(0<q\le q_c\), this simplifies to \(Z=k+\ell+2\ell q+(\ell+1)q^2\). In that regime the unique rates on, respectively, each of the \(k\) left spokes, each of the \(\ell\) right spokes, and the bridge are

\[
\frac{1}{Z},\qquad \frac{1+q}{Z},\qquad \frac{1+\ell+\ell/q}{Z}.
\]

For \(q>q_c\) (including all \(q>0\) when \(k=\ell\)), put \(A=1+q/2\). The corresponding three optimal rates are

\[
\frac{2(\ell+1)A}{NZ},\qquad
\frac{2(k+1)A}{NZ},\qquad
\frac{h/q+(h+1)/2}{Z}.
\]

Both rate formulas agree at \(q=q_c>0\). For \(k>\ell\), the eigenvalue \(\lambda_2\) has multiplicity \(k\) when \(q\le q_c\), and multiplicity one when \(q>q_c\). Thus the transition at the sharp bridge-price boundary \(t_c=((k-\ell)/(\ell+1))^2\) changes the eigenspace dimension. As a function of \(q\), the optimal inverse gap \(Z\) is continuously differentiable but not twice continuously differentiable there, with the second derivative changing by \(2(\ell+1)^2/N\). For the balanced case \(k=\ell\), there is no positive-price transition.

For example, \((k,\ell,t)=(4,1,1)\) is below its threshold \(t_c=9/4\); the unique rates are \(1/9\) on each of the four left spokes, \(2/9\) on the right spoke, and \(1/3\) on the bridge. The sharp mixing spectral gap is \(1/9\).

## Assumptions and scope

All vertices have unit stationary significance (the Markov generator is \(-L\), so the uniform distribution is invariant); the budget prices are the squares of allowed Euclidean edge lengths. Rates can be chosen independently and continuously on the fixed double-star topology, with no individual upper bounds. The result covers every integer pair \(k\ge\ell\ge1\) and every finite \(t>0\). Relabeling the two sides extends it to arbitrary positive leaf counts. The budget equality is without loss since the optimum has positive gap and the objective is positively homogeneous.

For verification of normalization, write \((x,y,z)\) for the **unscaled** conductances on the left spokes, right spokes, and bridge; the final conductances equal \((x,y,z)/Z\), where \(Z=kx+\ell y+q^2z\). The explicit formulas above use this convention.

## Proof

**Universal spectral upper certificate.** For any points \(X_v\) in a Euclidean space with \(\sum_v X_v=0\) and \(\|X_i-X_j\|^2\le c_{ij}\) on every tree edge, the Rayleigh principle gives

\[
\lambda_2(L(w))\sum_v\|X_v\|^2
\le\sum_{ij\in E}w_{ij}\|X_i-X_j\|^2
\le\sum_{ij\in E}c_{ij}w_{ij}=1.
\]

It suffices to construct centered points of squared-norm sum \(Z\) with all edge-length constraints tight and a positive unscaled Laplacian \(L_0\) satisfying \(L_0 X=X\) and \(\lambda_2(L_0)=1\). With its budget \(Z\), the normalized Laplacian \(L_0/Z\) saturates the upper certificate.

**Regime \(0<q\le q_c\), requiring \(k>\ell\).** Let \(\alpha=(\ell+(\ell+1)q)/k\in(0,1]\), and select vectors \(u_1,\ldots,u_k\) in a Euclidean subspace perpendicular to a unit vector \(e\), with \(\sum_i u_i=0\) and \(\|u_i\|^2=1-\alpha^2\), whose Gram matrix is a scaled regular simplex. Set the \(k\) left-leaf points to \(\alpha e+u_i\), the left hub to \(0\), the right hub to \(-qe\), and each right leaf to \(-(q+1)e\). The centering identity is \(k\alpha=\ell+(\ell+1)q\). Every pendant squared distance is \(1\), the bridge squared distance is \(q^2\), and direct expansion yields

\[
\sum_v\|X_v\|^2=k+\ell+2\ell q+(\ell+1)q^2=Z.
\]

Take \(x=1\), \(y=1+q\), and \(z=1+\ell+\ell/q\). For each leaf, \(L_0X=X\) follows from its pendant edge difference; at the left hub it is \(-k\alpha+zq=0\), and at the right hub it is \(\ell(1+q)-zq=-q\). The unscaled rate cost equals the displayed \(Z\).

To certify **that this eigenvalue is the second**, consider \(L_0-I\) and delete the row and column of the left hub. The remaining principal matrix is the direct sum of \(k\) zero entries and a grounded right star. The latter has leaf diagonal \(y-1=q>0\) and its one-dimensional Schur complement at the right hub equals

\[
z-1-\ell\frac{y}{y-1}=0.
\]

Thus the principal minor is positive semidefinite. Cauchy interlacing implies \(L_0-I\) has at most one negative eigenvalue. Since \(L_0\mathbf1=0\) it has exactly one; because \(L_0X=X\ne0\), the second eigenvalue of \(L_0\) equals \(1\). For any \(q\le q_c\), the nullspace of \(L_0-I\) has dimension \(k\): its left-leaf equations force the left-hub coordinate to zero, while the right-leaf and hub equations leave one linear constraint among the \(k\) left-leaf coordinates and the right-hub coordinate.

**Regime \(q>q_c\).** Put \(A=1+q/2\), \(m=(k-\ell)A/N\), \(U=q/2-m>0\), and \(V=-q/2-m<0\). Embed all \(k\) left leaves at the scalar \(A-m\), the left hub at \(U\), the right hub at \(V\), and all \(\ell\) right leaves at \(-A-m\). Their sum is zero, the two pendant lengths are \(1\), and the hub distance is \(q\). Their squared-norm sum is

\[
Z=2h(1+q)+\frac{h+1}{2}q^2.
\]

Take \(x=A-m=2(\ell+1)A/N\), \(y=A+m=2(k+1)A/N\), and \(z=h/q+(h+1)/2\). Direct substitution verifies \(L_0X=X\) at all vertices, and \(kx+\ell y+q^2z=Z\). Here \(x-1=U>0\), \(y-1=-V>0\). Eliminate the \(k+\ell\) positive leaf-diagonal pivots in \(L_0-I\); the remaining symmetric \(2\times2\) Schur matrix has off-diagonal \(-z\), has nullvector \((U,V)\), and therefore has diagonal entries \(zV/U<0\) and \(zU/V<0\). It has exactly one negative and one zero eigenvalue. Hence \(L_0-I\) has exactly one negative and one zero eigenvalue, proving \(\lambda_2(L_0)=1\) **simply**.

**Joining the branches.** Elementary algebra gives

\[
\big[k+\ell+2\ell q+(\ell+1)q^2\big]
-\big[2h(1+q)+(h+1)q^2/2\big]
=\frac{((k-\ell)-(\ell+1)q)^2}{N}.
\]

Thus the two expressions meet with the same first derivative at \(q_c\), and the positive-part formula follows. At equality the high-branch rate expressions reduce to the low-branch ones. The second derivative difference is \(2(\ell+1)^2/N\) when \(k>\ell\).

**Uniqueness among all (including nonsymmetric) allocations.** Fix the corresponding witness points. If another budget-one Laplacian attained the same \(\lambda_2=1/Z\), equality in the spectral upper certificate forces every coordinate column of \(X\) to be a \(\lambda_2\)-eigenvector of the competing Laplacian. Every leaf position differs nontrivially from its hub, so its eigenvector row identity fixes that leaf's individual edge rate to its displayed value. The remaining bridge rate is then fixed by the exact budget. Thus every optimal edge rate is unique; no symmetry hypothesis was imposed on competing designs.

## Verification

The provided `checker.py` performs exact-rational Gram-matrix construction (including the transverse simplex), edge-length and centroid checks, budget and Laplacian eigenvector identities, exact-rational ranks of \(L_0-I\), and both regime-specific Schur identities for \(299\) sampled integer-pair and rational-price cases. It returns `VERIFY_OK 299 exact rational cases; 97 low-price and 202 high-price; Gram eigenrelations, budgets, ranks and Schur certificates`. The infinite family is proved by the preceding algebra and inertia argument, **not** by finite checking.

## Relationship to prior work

Sun, Boyd, Xiao, and Diaconis [1] formulated continuous-time fastest mixing with arbitrary positive edge costs as a semidefinite program and its Euclidean-embedding dual. Fiedler's absolute algebraic connectivity of trees [2] and Richter–Rocha's double-broom formula and eigenvectors [3] already cover important uniform-price cases, including the all-unit-price specialization of a double star. Wappler [4] developed general edge-length embedding and structural theory. The contribution here is only the explicit **continuous bridge-price-dependent** double-star optimizer, its complete normalized edge-rate formulas, and its sharp eigenvalue-multiplicity transition. This is not a claim of novelty for spectral duality, general graph optimization, uniform-price double-star mixing, or the geometric proof technique.

## Limitations

The theorem concerns symmetric continuous-time chains with a **uniform** invariant distribution and a prescribed fixed double-star topology. It does not solve discrete-time transition optimization, node-weighted stationary distributions, arbitrary trees, or stochastic time-dependent edge rates. The mixing-rate convention is the Laplacian spectral gap, not a mixing-time identity. Existing work already treats the unit-price case and general algorithms. A specialized equivalent bridge-price formula in older literature cannot be ruled out without broader historical full-text comparison; an accessible repository record of Wappler's relevant thesis was checked, but its PDF attachment did not resolve during retrieval. Independent validation has not been performed.

## References

[1] J. Sun, S. Boyd, L. Xiao, and P. Diaconis, *The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem*, SIAM Review 48 (2006), 681–699, doi:10.1137/S0036144504443821. First verified electronic publication: 2006-11-02. Open full text: https://web.stanford.edu/~boyd/papers/pdf/fmmp.pdf.

[2] M. Fiedler, *Absolute algebraic connectivity of trees*, Linear and Multilinear Algebra 26 (1990), 85–106, doi:10.1080/03081089008817967.

[3] S. Richter and I. Rocha, *Absolute algebraic connectivity of double brooms*, 2014 research preprint, https://www.tu-chemnitz.de/mathematik/preprint/2014/PREPRINT_10.pdf; later expanded as *Absolute algebraic connectivity of double brooms and trees*, Discrete Applied Mathematics 201 (2016), doi:10.1016/j.dam.2015.08.009.

[4] M. Wappler, *On Graph Embeddings and a new Minor Monotone Graph Parameter associated with the Algebraic Connectivity of a Graph*, doctoral thesis, TU Chemnitz, public repository record dated 2013-06-07, urn:nbn:de:bsz:ch1-qucosa-115518, https://monarch.qucosa.de/landing-page/?tx_dlf%5Bid%5D=https%3A%2F%2Fmonarch.qucosa.de%2Fapi%2Fqucosa%253A19916%2Fmets.
