# Sharp shape-regularity rarity and volume decoupling for uniformly tagged random-split cells

## Finding
Fix an integer \(d\ge2\), a real \(\beta>1\), and let \(X\) be uniform on \([0,1]^d\), independent of all cuts. In a depth-\(N\) uniform random partition, follow the unique rectangular cell containing \(X\) through \(N\) cuts. At each cut choose a coordinate independently uniformly among \(\{1,\ldots,d\}\) and a cut fraction independently uniformly on \((0,1)\). Let \(h_{N,j}\) be the final side length in direction \(j\), \(V_N=\prod_j h_{N,j}\), and \(R_N=(\max_j h_{N,j})/(\min_j h_{N,j})\).

**Theorem (tagged-cell sharp law and rare-event volume decoupling).** The retained one-step length fractions are independent \(\mathrm{Beta}(2,1)\) variables; hence \(-\log V_N\sim\mathrm{Gamma}(N,2)\), with shape \(N\) and rate \(2\), exactly for every \(N\ge1\). For every fixed \(\beta>1\),
\[
\lim_{N\to\infty}N^{(d-1)/2}\Pr(R_N\le\beta)=\sqrt d\left(\frac d\pi\right)^{(d-1)/2}(\log\beta)^{d-1}.
\]
Furthermore, in the same fixed-\(d\) limit,
\[
\mathcal L\left(\frac{2(-\log V_N-N/2)}{\sqrt N}\,\middle|\,R_N\le\beta\right)\Longrightarrow\mathcal N(0,1).
\]
Unconditionally,
\[
\left(\frac{\log R_N}{\sqrt N},\frac{2(-\log V_N-N/2)}{\sqrt N}\right)\Longrightarrow\left(\max_j G_j-\min_jG_j,Z\right),
\]
where the \(G_j\) are independent \(\mathcal N(0,1/(2d))\), and \(Z\sim\mathcal N(0,1)\) is independent of all the \(G_j\). No statement of independence of volume and shape for finite \(N\) is made.

## Assumptions and scope
A complete depth-\(N\) tree with independent uniform coordinate/relative-position cuts has the same tagged-path law as directly constructing cuts in the current cell containing \(X\). The point \(X\) is drawn independently uniformly from the original cube and is averaged over in the displayed probability. The dimension \(d\) and threshold \(\beta\) remain fixed as \(N\to\infty\). There are no restrictions on the side lengths of the unselected child cells. Ties of the longest or shortest side have probability zero at sufficiently large depth, and do not affect the formulas.

## Proof
**1. Length bias from a uniform query.** Before a cut, write \(x\in(0,1)\) for the selected coordinate of the *normalized* query in the current cell and \(t\in(0,1)\) for the independent cut position. Both are uniform and independent. The retained side fraction and new normalized query coordinate are
\[
(u,r)=\begin{cases}(t,x/t),&x<t,\\(1-t,(x-t)/(1-t)),&x>t.\end{cases}
\]
For the left-child branch, the change of variables \((x,t)\mapsto(u,r)\) has absolute Jacobian \(u\). The right branch has the same absolute Jacobian \(u\). Their densities add to \(2u\,du\,dr\) on \((0,1)^2\). Therefore \(u\) has density \(2u\), \(r\) is uniform, and they are independent. The other normalized query coordinates remain independent uniforms, while the next cut coordinate and cut fraction are fresh independent draws. Induction proves that all successive tagged length fractions \(U_i\) are iid \(\mathrm{Beta}(2,1)\) and independent of the coordinate choices \(J_i\).

Consequently \(E_i=-\log U_i\) are iid exponential variables of rate \(2\), independent of iid uniform \(J_i\in\{1,\ldots,d\}\). Write
\[
L_{N,j}=-\log h_{N,j}=\sum_{i=1}^N E_i\mathbf1_{\{J_i=j\}},\quad S_N=\sum_jL_{N,j}=\sum_{i=1}^NE_i=-\log V_N.
\]
The gamma assertion follows immediately.

**2. Covariance and Gaussian limit.** The iid increment vectors \(W_i=E_i e_{J_i}\) have mean \(\mu=(1/(2d))\mathbf1_d\) and covariance
\[
\Sigma=\frac1{2d}I_d-\frac1{4d^2}\mathbf1_d\mathbf1_d^{\mathsf T}.
\]
For the difference vector \(D_N=(L_{N,1}-L_{N,d},\ldots,L_{N,d-1}-L_{N,d})\), its one-step covariance is
\[
\Omega=\frac1{2d}(I_{d-1}+\mathbf1_{d-1}\mathbf1_{d-1}^{\mathsf T}),\qquad \det\Omega=\frac d{(2d)^{d-1}}.
\]
Also \(\operatorname{Var}(S_N)=N/4\) and \(\operatorname{Cov}(S_N,D_N)=0\) *exactly*. The multivariate central limit theorem gives a joint Gaussian limit with independent total-sum and difference components. The centered difference components have the same Gaussian law as \((G_1-G_d,\ldots,G_{d-1}-G_d)\) with iid \(G_j\sim\mathcal N(0,1/(2d))\). Taking the range of the \(d\) coordinates proves the claimed unconditional joint limit.

**3. Sharp bounded-shape probability.** Set \(b=\log\beta>0\) and define the compact full-dimensional polytope
\[
C_b=\{z\in\mathbb R^{d-1}:\max(0,z_1,\ldots,z_{d-1})-\min(0,z_1,\ldots,z_{d-1})\le b\}.
\]
Then \(\{R_N\le\beta\}=\{D_N\in C_b\}\), since \(\log R_N=\max_jL_{N,j}-\min_jL_{N,j}\). Partition \(C_b\), up to null boundaries, by which of its \(d\) associated coordinates \((z_1,\ldots,z_{d-1},0)\) is the minimum. If the last coordinate is minimum, the region is \([0,b]^{d-1}\), of volume \(b^{d-1}\). If coordinate \(k<d\) is minimum, let \(z_k\in[-b,0]\); each other nonzero coordinate lies in \([z_k,z_k+b]\), also giving volume \(b^{d-1}\). Hence
\[
\operatorname{Vol}_{d-1}(C_b)=d b^{d-1}.
\]
The one-step difference increment law is nondegenerate, nonlattice and spread out: a sum of sufficiently many increments has a nonzero absolutely continuous component, because the \(d\) possible direction vectors \(e_1,\ldots,e_{d-1},-\mathbf1_{d-1}\) span \(\mathbb R^{d-1}\), each chosen with positive probability, and the corresponding exponential lengths have densities. The characteristic function equals the average of \(2/(2-i\langle t,v_j\rangle)\) over those directions, so no nonzero frequency has unit modulus. Thus the multivariate nonlattice local limit theorem (Stone, 1965) applies to fixed bounded Jordan-measurable sets. With the covariance \(\Omega\), it yields
\[
\Pr(D_N\in C_b)\sim\frac{\operatorname{Vol}(C_b)}{(2\pi N)^{(d-1)/2}\sqrt{\det\Omega}}.
\]
Inserting the preceding determinant and polytope volume and simplifying gives precisely the displayed constant. The singular probability that some coordinate has never been selected is at most \(d(1-1/d)^N\) and is harmless in this local limit.

**4. Conditional log-volume law.** Apply the same \(d\)-dimensional local limit theorem to the full nondegenerate vector \((S_N,D_N)\). Its one-step covariance is block diagonal with blocks \(1/4\) and \(\Omega\); its step law is spread out because the \(d\) vectors \((1,e_j)\) for \(j<d\), where \(e_j\in\mathbb R^{d-1}\), and \((1,-\mathbf1_{d-1})\) for \(j=d\) are linearly independent and the exponential lengths are continuous. The standard uniform translated-box form of Stone's theorem, summed over boxes spanning an interval of length \(O(\sqrt N)\) along the first coordinate, gives, for every finite \(a<c\),
\[
\lim_{N\to\infty}N^{(d-1)/2}\Pr\!\left(D_N\in C_b,\ a\le\frac{2(S_N-N/2)}{\sqrt N}\le c\right)
=K_{d,b}\bigl(\Phi(c)-\Phi(a)\bigr),
\]
where \(K_{d,b}=\sqrt d(d/\pi)^{(d-1)/2}b^{d-1}\) and \(\Phi\) is the standard Gaussian distribution function. The result in Step 3 says that the total mass of this scaled subprobability is \(K_{d,b}\). Taking \(a\downarrow-\infty\) and \(c\uparrow\infty\), the matching total mass yields conditional tightness. Dividing by \(\Pr(D_N\in C_b)\) proves the conditional Gaussian limit.

## Verification
A standalone checker `verify.py` exercises the one-step length-bias identities by reproducible Monte Carlo, tests the covariance matrices and determinant formula against rational computations, checks the exact two-dimensional local-density identity using Fourier inversion, and verifies the geometry of the three-dimensional shape polytope. In dimension \(d=2\), the difference increment is a symmetric exponential with characteristic function \(4/(4+t^2)\); its \(N\)-step density at zero is exactly \(\Gamma(N-1/2)/(\sqrt\pi\,\Gamma(N))\), consistent with the predicted \(N^{-1/2}\) constant. Execution of the checker passed. These checks do not replace the local limit theorem, which is the proof of the infinite-limit assertions.

## Relationship to prior work
Bettinger, Portier, and Saumard (2026, arXiv:2608.08360) establish loss of shape regularity for centered and uniformly split regression trees, including a positive-probability stretched-cell result, and analyze fixed query points using upper and lower bounds. The theorem here changes the quantifier to an **independently uniform query**, proves an exact size-biased one-step law, and obtains both a sharp polynomial probability with constant and a conditional central limit theorem for volume. Their positive-probability elongation theorem does not imply either local probability or conditional fluctuation statement. The authors' earlier arXiv:2606.28641 treats broader random-split assumptions and nonregularity via coarser lower bounds rather than this tagged-uniform model's exact rarity. Stone's local limit theorem is an established tool, not a new contribution; the application and exact geometric constants are the new claim.

## Limitations
All probability statements average over the independent uniform query as well as cut randomness. No uniform-in-query or almost-sure-in-tree shape-regularity claim follows. The dimension and shape threshold are fixed; growing dimension or a threshold depending on depth requires separate analysis. The conditional volume law describes one tagged cell, not the entire set of leaf cells. Finite checks support intermediate identities but do not prove the asymptotic. Priority relative to unindexed, earlier random-partition and split-tree literature requires independent verification.

## References
1. J. Bettinger, F. Portier, A. Saumard, “Pointwise convergence of purely random partition estimators: from random trees to prototype rules,” arXiv:2608.08360 (first public version August 8, 2026), especially Section 3.3 and its proof appendix. https://arxiv.org/abs/2608.08360
2. J. Bettinger, F. Portier, A. Saumard, “Revisiting local regression: shape regularity, uniform rates, and the limits of random splits,” arXiv:2606.28641 (2026), Section 5.2. https://arxiv.org/abs/2606.28641
3. C. Stone, “A Local Limit Theorem for Nonlattice Multi-Dimensional Distribution Functions,” Annals of Mathematical Statistics **36** (1965), 546–551. https://doi.org/10.1214/aoms/1177700165
