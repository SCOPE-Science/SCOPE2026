# A path-square law for sign crossings and energy on Gaussian trees

## Finding

In a finite centered unit-variance Gaussian Markov tree, the covariance between the event that an edge's endpoint values have opposite signs and the squared value at any vertex is an exact negative edge-correlation multiple of the **squared correlation along the remaining path**. In particular, on every tree whose edge correlations are all strictly positive, any nontrivially nonnegative weighted number of sign-disagreement edges is strictly negatively correlated with any nontrivially nonnegative weighted sum of vertex squares. If all edge correlations are strictly negative, the covariance is strictly positive.

More precisely, let \(T=(V,E)\) be a finite tree with at least one edge. Give each edge \(e\) a number \(r_e\in(-1,1)\). Choose any root, take mutually independent standard normal variables \((\varepsilon_v)_{v\in V}\), put \(X_{\mathrm{root}}=\varepsilon_{\mathrm{root}}\), and, for each nonroot vertex \(v\) with parent \(p(v)\), set
\[
 X_v=r_{\{p(v),v\}}X_{p(v)}+\sqrt{1-r_{\{p(v),v\}}^2}\,\varepsilon_v.
\]
All \(X_v\) have variance one. For \(e=\{u,v\}\), define \(B_e=\mathbf1\{X_uX_v<0\}\). For \(z\in V\), let \(b_e(z)\in\{u,v\}\) be the unique endpoint of \(e\) nearest to \(z\), and define
\[
 \eta_{z,e}=\prod_{f\in P(z,b_e(z))}r_f,
\]
where \(P\) is the edge set of the indicated unique tree path and the empty product equals one. Then, simultaneously for **every** edge \(e\) and vertex \(z\),
\[
\boxed{\operatorname{Cov}(B_e,X_z^2)=-\frac{r_e\sqrt{1-r_e^2}}{\pi}\,\eta_{z,e}^{2}.}
\]
Consequently for any fixed weights \(w_e\ge0\) and \(a_z\ge0\),
\[
\boxed{\operatorname{Cov}\!\left(\sum_{e\in E}w_eB_e,\sum_{z\in V}a_zX_z^2\right)
=-\frac1\pi\sum_{e\in E}w_e r_e\sqrt{1-r_e^2}\sum_{z\in V}a_z\eta_{z,e}^{2}.}
\]
If every \(r_e\) has the same nonzero sign, at least one \(w_e\) is positive, and at least one \(a_z\) is positive, the resulting covariance has the strict **opposite** sign to the correlations.

For a stationary Gaussian autoregressive chain of length \(n\ge2\) with \(\mathbb E[X_iX_j]=\rho^{|i-j|}\), \(|\rho|<1\), put \(C_n=\sum_{i=1}^{n-1}\mathbf1\{X_iX_{i+1}<0\}\) and \(E_n=\sum_{i=1}^{n}X_i^2\). The exact finite-sample specialization is
\[
\boxed{\operatorname{Cov}(C_n,E_n)
=-\frac{2\rho\sqrt{1-\rho^2}}{\pi}\sum_{h=0}^{n-2}(n-1-h)\rho^{2h}.}
\]
At fixed \(|\rho|<1\),
\[
\lim_{n\to\infty}\frac{\operatorname{Cov}(C_n,E_n)}n
=-\frac{2\rho}{\pi\sqrt{1-\rho^2}}.
\]

The tree hypothesis is substantive, not merely notation: a centered Gaussian triple with correlations \(\mathbb E[UV]=1/2\), \(\mathbb E[ZU]=4/5\), and \(\mathbb E[ZV]=1/10\) has covariance-matrix determinant \(9/50>0\), yet its sign–square covariance is
\[
 \operatorname{Cov}(\mathbf1\{UV<0\},Z^2)=\frac{33}{100\pi\sqrt3}>0.
\]
Thus even three *positive* pairwise Gaussian correlations do not suffice for the tree's negative-dependence conclusion without its Markov path factorization.

## Assumptions and scope

The tree is finite and connected, has at least two vertices, and has edge correlations in the *open* interval \((-1,1)\). The Gaussian model is centered with unit marginal variance and independent innovations as defined above. Zero correlations are permitted in the identity, but strict sign assertions require all edge correlations to be nonzero and of the same sign. A sign at the exact value zero has probability zero, so the strict crossing event is unambiguous. The edge and vertex weights are deterministic and nonnegative. For the chain corollary, sample size \(n\ge2\) and the autoregressive correlation \(\rho\in(-1,1)\) are arbitrary.

## Proof

**Step 1 (three-Gaussian sign–square identity).** Let \((U,V,Z)\) be centered jointly Gaussian with unit marginal variances, \(\mathbb E[UV]=r\in(-1,1)\), \(\mathbb E[ZU]=a\), \(\mathbb E[ZV]=b\), and put \(I=\mathbf1\{UV<0\}\). We establish
\[
\operatorname{Cov}(I,Z^2)=\frac{r(a^2+b^2)-2ab}{\pi\sqrt{1-r^2}}.
\]
Let \(s=\sqrt{1-r^2}\). The familiar bivariate normal sign integral gives \(\mathbb E I=\arccos(r)/\pi\). Conditional on \(U=x>0\), the probability of a sign disagreement is \(\Phi(-rx/s)\). By symmetry and a one-variable Gaussian integration by parts,
\[
\mathbb E[U^2I]=2\int_0^\infty x^2\varphi(x)\Phi(-rx/s)\,dx
=\frac{\arccos(r)-rs}{\pi}.
\]
The last equality follows by writing \((x^2-1)\varphi(x)=(-x\varphi(x))'\) and using \(\int_0^\infty x\varphi(x)\varphi(rx/s)\,dx=s^2/(2\pi)\). Thus
\[\operatorname{Cov}(U^2,I)=\operatorname{Cov}(V^2,I)=-rs/\pi.\]
Also \(\mathbb E|UV|=2(s+r\arcsin r)/\pi\). Indeed, with \(\phi=\arccos r\), represent \(U=R\cos\Theta\) and \(V=R\cos(\Theta-\phi)\), where \(\Theta\) is uniform on \([0,2\pi)\), independent of \(R\), and \(\mathbb E R^2=2\). Directly splitting the angle integral where the cosine factors change sign gives
\[
\mathbb E|UV|=\frac1\pi\int_0^{2\pi}|\cos t\cos(t-\phi)|\,dt
=\frac2\pi\left(\sin\phi+(\pi/2-\phi)\cos\phi\right),
\]
which is the stated expression. Since \(UV\mathbf1\{UV<0\}=(UV-|UV|)/2\),
\[\operatorname{Cov}(UV,I)=-s/\pi.\]
Regress \(Z=\alpha U+\beta V+\xi\), with \(\xi\) independent of \((U,V)\), where
\[
\alpha=\frac{a-rb}{1-r^2},\qquad\beta=\frac{b-ra}{1-r^2}.
\]
Centering and independence give
\[
\operatorname{Cov}(Z^2,I)=-\frac{s}{\pi}\bigl[r(\alpha^2+\beta^2)+2\alpha\beta\bigr].
\]
Substitution and simplification gives the boxed three-Gaussian identity. All displayed integrals are convergent for \(|r|<1\); hence no limiting interchange at singular correlations is needed.

**Step 2 (tree geometry).** Along a tree path, independent innovations imply
\[
 \mathbb E[X_xX_y]=\prod_{f\in P(x,y)}r_f.
\]
For \(e=\{u,v\}\) and \(z\) on the \(u\)-side of the edge, write \(\eta=\eta_{z,e}\). The same path formula yields
\[
\mathbb E[X_zX_u]=\eta,\qquad \mathbb E[X_zX_v]=r_e\eta.
\]
Apply Step 1 with \(a=\eta\), \(b=r_e\eta\), \(r=r_e\); its numerator reduces to \(-r_e(1-r_e^2)\eta^2\). This proves the local law. Interchanging \(u\) and \(v\) covers the other side. Bilinearity of covariance proves the weighted formula. If all edge correlations are nonzero, each \(\eta_{z,e}^2>0\), giving strictness of the sign when both weight families are nontrivial.

**Step 3 (chain and limit).** In the chain the nearest-endpoint path has \(d(z,e)\) edges, so \(\eta_{z,e}^2=\rho^{2d(z,e)}\). Summing first over vertices and then edges gives the elementary identity
\[
 \sum_{i=1}^{n-1}\sum_{z=1}^{n}\rho^{2d(z,\{i,i+1\})}
 =2\sum_{h=0}^{n-2}(n-1-h)\rho^{2h}.
\]
This proves the finite-sample formula. Divide the sum by \(n\) and use geometric-series convergence for \(|\rho|<1\) to obtain the limit.

## Verification

A standalone standard-Python checker, `verify.py`, tests the algebraic reduction of Step 1 over exact rational triples; independently integrates the conditional-normal formula for nine correlations; checks the chain's two summation organizations using exact rationals through length 25; checks path products on a branching tree; and compares a seeded Gaussian-tree simulation against all local covariance predictions. It reports 446 passed finite checks. These checks corroborate the identities and are **not** the proof for arbitrary tree size, which is given above.

Run with `python3 verify.py` in the directory containing `RESULT.md` and `verify.py`.

## Relationship to prior work

Kratz and León (2006) establish second-moment finiteness conditions for crossings of differentiable continuous-time stationary Gaussian processes; their inspected full text does not assert the discrete tree sign-event/squared-amplitude cross-covariance above. Sinn and Keller (2011) analyze pairwise covariances of discrete-time Gaussian zero-crossing indicators, including AR(1); only accessible abstract, metadata and keywords were inspected, not its inaccessible full paper, so possible unobserved overlapping formulas remain a priority risk. Classical Price/McMahon Gaussian integration methods, and the later general formulation of Voigtlaender (2020), provide machinery for Gaussian nonlinear expectations; no novelty is claimed for those methods, Gaussian regression, or the bivariate normal moments. The assessed claim is the exact tree-path-square mixed-covariance law and its common-sign consequence.

## Limitations

The theorem concerns Gaussian Markov trees with unit marginal variances and nonsingular edge transitions. It does not establish analogous sign claims for non-Gaussian tree models, Gaussian graphs with cycles, arbitrary Gaussian covariance matrices, or weighted models containing both positive and negative edge correlations. A covariance sign does not imply stochastic ordering or independence. The chain asymptotic fixes \(\rho\) before taking \(n\to\infty\), and is not uniform at \(|\rho|=1\). The literature comparison is not proof of historical uniqueness, particularly because the full Sinn–Keller paper was inaccessible. Independent audit is not performed.

## References

- M. F. Kratz and J. R. León, *On the second moment of the number of crossings by a stationary Gaussian process*, Annals of Probability **34** (2006), 1601–1607, DOI: 10.1214/009117906000000142; arXiv:math/0609682 (first posted 2006-09-25). https://arxiv.org/abs/math/0609682
- M. Sinn and K. Keller, *Covariances of Zero Crossings in Gaussian Processes*, Theory of Probability and Its Applications **55** (2011), 485–504, DOI: 10.1137/S0040585X97984991. https://doi.org/10.1137/S0040585X97984991
- R. Price, *A Useful Theorem for Nonlinear Devices Having Gaussian Inputs*, IRE Transactions on Information Theory **4** (1958), 69–72, DOI: 10.1109/TIT.1958.1057444. https://doi.org/10.1109/TIT.1958.1057444
- F. Voigtlaender, *A General Version of Price’s Theorem*, Journal of Theoretical Probability **34** (2021), 1474–1485, first published 2020-06-26, DOI: 10.1007/s10959-020-01017-w. https://link.springer.com/article/10.1007/s10959-020-01017-w
