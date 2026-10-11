# Sharp three-leaf star extension constants for real \(p\)-Banach targets

## Finding

Let \(N=\{u_0,u_1,u_2\}\) carry the equilateral metric \(d(u_i,u_j)=2\) for distinct leaves, and let \(M=N\cup\{o\}\) be the metric star with \(d(o,u_i)=1\). For \(0<p\leq1\), let \(\mathfrak t_p(N,M)\) denote the least constant \(C\) such that every Lipschitz map from \(N\) to every real \(p\)-Banach space extends to \(M\) with Lipschitz constant at most \(C\) times the original one. Then

\[
\boxed{\mathfrak t_p(N,M)=\min\left\{2,\frac{2^{1+1/p}}{3}\right\}.}
\]

Write \(p_0=\log 2/\log 3\). For the canonical isometric triple in the real free \(p\)-Banach space \(\mathcal F_p(N)\), all minimizing images of the new center are classified: for \(0<p<p_0\) they are precisely the three leaf images; at \(p=p_0\) they are those three images and their arithmetic barycenter; and for \(p_0<p\leq1\) the barycenter is the unique minimizer. Thus the optimal center changes discontinuously at the sharp threshold, while the optimal constant is continuous.

## Assumptions and scope

A real \(p\)-Banach space \(Z\) is a complete real vector space with a positive homogeneous \(p\)-norm satisfying \(\|v+w\|^p\leq\|v\|^p+\|w\|^p\). Its Lipschitz constant is defined using the norm distance \(\|f(x)-f(y)\|\) and the stated ordinary metric on the domain. The universal constant allows an arbitrary target \(Z\) and arbitrary map \(f:N\to Z\); no finite-dimensionality or locally convexity of \(Z\) is assumed. The free space \(\mathcal F_p(N)\), with any leaf designated as basepoint, has canonical isometric embedding \(\delta:N\to\mathcal F_p(N)\) and the universal linearization property. We use the concrete finite norm representation from Cúth and Raunig [2], not an unproved identification with a Banach norm when \(p<1\).

The extra point \(o\) is not a fourth equilateral point: its distance to each leaf is exactly one. Multiplying all distances by a common positive factor does not change the extension constant.

## Proof

**1. Universal upper estimate.** Let \(L=\operatorname{Lip}(f)\). Taking the extension value at \(o\) to be one of the leaf values gives \(\|f(o)-f(u_i)\|\leq2L\), so \(\mathfrak t_p\leq2\). Alternatively set
\[
y=\frac{f(u_0)+f(u_1)+f(u_2)}{3}.
\]
For distinct \(i,j,k\), the \(p\)-triangle inequality gives
\[
\|y-f(u_i)\|^p
=3^{-p}\|(f(u_j)-f(u_i))+(f(u_k)-f(u_i))\|^p
\leq2(2L/3)^p.
\]
Since \(d(o,u_i)=1\) and all original leaf-leaf Lipschitz bounds remain unchanged, this is an extension with constant at most \(2^{1+1/p}/3\). For the whole range \(0<p\leq1\), this candidate constant is at least \(4/3>1\); therefore the original leaf-leaf pairs never spoil the claimed upper estimate.

**2. Exact free-space norm.** Designate \(u_0\) as basepoint and put \(e_1=\delta(u_1)\), \(e_2=\delta(u_2)\), \(\delta(u_0)=0\). The three spanning trees of the equilateral three-point metric, or equivalently [2, Corollary 2.7], give for every real \(s,t\)
\[
\|se_1+te_2\|_{\mathcal F_p(N)}
=2\min\left\{
(|s|^p+|t|^p)^{1/p},
(|s+t|^p+|s|^p)^{1/p},
(|s+t|^p+|t|^p)^{1/p}
\right\}.
\tag{1}
\]
The reason this finite formula is exhaustive is that the free \(p\)-norm takes its minimum over spanning-tree presentations of the molecule, and there are exactly three unoriented spanning trees on three vertices. Their edges all have length two. This is a precise use of the known tree formula, not an appeal to numerical enumeration as an infinite proof.

**3. Reduction to a probability simplex.** A potential center \(z=se_1+te_2\) has unique affine coefficients
\[
\lambda_0=1-s-t,\qquad\lambda_1=s,\qquad\lambda_2=t,
\qquad \lambda_0+\lambda_1+\lambda_2=1,
\]
meaning \(z=\sum_i\lambda_i\delta(u_i)\). The canonical map from \(\mathcal F_p(N)\) to its Banach envelope \(\mathcal F_1(N)\) is contractive: this follows directly because every \(p\)-sum of edge coefficients dominates their ordinary absolute sum. For an equilateral triple of side two, the Banach free-space norm of a zero-total-mass molecule \(\sum_i\mu_i\delta(u_i)\) equals \(\sum_i|\mu_i|\), by sending positive mass directly to negative mass along edges of cost two. Hence, if any \(\lambda_i<0\),
\[
\|z-\delta(u_i)\|_{\mathcal F_p(N)}
\geq\sum_j|\lambda_j-\mathbf1_{\{j=i\}}|
\geq 2(1-\lambda_i)>2.
\]
At least one leaf image gives radius two, so no minimizer can have a negative affine coefficient. It suffices to minimize over the closed simplex \(\lambda_i\geq0\).

**4. Radii on the simplex.** For every simplex point and every \(i\), let \(\{i,j,k\}=\{0,1,2\}\). Formula (1), expressed relative to leaf \(i\), simplifies to
\[
\|z-\delta(u_i)\|=2(\lambda_j^p+\lambda_k^p)^{1/p}.
\tag{2}
\]
Indeed the spanning-tree star based at \(i\) gives that value. Each alternative spanning tree replaces one of the nonnegative coefficients by its sum with another nonnegative coefficient and cannot be smaller. By permuting indices write \(0\leq a\leq b\leq c\), \(a+b+c=1\). The largest of the three radii (2) is exactly
\[
R_p(z)=2(b^p+c^p)^{1/p}.
\tag{3}
\]

**5. Global minimization and all equality cases.** Fix \(a\in[0,1/3]\) and take \(b\in[a,(1-a)/2]\), \(c=1-a-b\). For \(0<p<1\), the function \(b\mapsto b^p+(1-a-b)^p\) is strictly concave, so its minimum on that interval occurs at one of its two endpoints. The \(b=a\) endpoint yields \(a^p+(1-2a)^p\), a strictly concave function of \(a\) whose minimum occurs at \(a=0\) or \(a=1/3\), giving respectively \(1\) and \(2/3^p\). The \(b=c=(1-a)/2\) endpoint yields \(2((1-a)/2)^p\), strictly decreasing in \(a\); it is minimized only at \(a=1/3\), giving \(2/3^p\). Therefore
\[
\inf_z R_p(z)
=2\left(\min\{1,2/3^p\}\right)^{1/p}
=\min\{2,2^{1+1/p}/3\}.
\]
All minimizers for \(p<1\) follow from strictness: a permutation of \((0,0,1)\) when \(3^p<2\), the balanced triple \((1/3,1/3,1/3)\) when \(3^p>2\), and those four points when \(3^p=2\). For \(p=1\), equation (3) becomes \(R_1=2(b+c)=2(1-a)\), whose unique minimum is at \(a=b=c=1/3\) with value \(4/3\). The separating equality \(3^p=2\) is equivalent to \(p=p_0\).

**6. Sharpness for arbitrary targets.** Set \(Z=\mathcal F_p(N)\) and \(f(u_i)=\delta(u_i)\), which has Lipschitz constant exactly one. Every extension value \(z\in Z\) must obey the lower bound just proved. Coupled with step 1, this establishes the *universal* optimal extension constant, not merely a calculation for one target.

## Verification

The standalone `verification/check.py` uses only the Python standard library. Running `python verification/check.py` checks the complete three-spanning-tree formula on selected rational coordinates, the exact \(p=1\) minimax lower bound on an extended rational affine grid, and all \(4,960\) points of a degree-30 simplex grid at ten exponent values including the transition exponent. It also checks both explicit extremizer types. Reproducible output is recorded in `VERIFICATION.md`. Those finite tests do **not** establish the global theorem or equality classification; the analytic argument in steps 1–6 does.

## Relationship to prior work

Bíma [1] introduced relevant free \(p\)-space techniques for Lipschitz maps and finite-dimensional subsets, with primary MSC 46A16. Cúth and Raunig [2, Theorem 2.2 and Corollary 2.7] provide the spanning-tree norm computation used in step 2; their work on three-point isometric \(p\)-amenability addresses inclusions and linearizations, not this one-point extension minimax law. Bíma [3, Proposition 26] connects universal Lipschitz extension to the canonical free-space image. His Theorem 30 studies a *different* metric: \(\{0,1,2\}\subset\mathbb R\) with the added point \(3/2\), where the Banach endpoint extension constant is one, and proves only the quasi-Banach inequality and limit as \(p\downarrow0\). Here the leaf distances are all two, the new point is equally distant from every leaf, the Banach endpoint is \(4/3\), and the entire optimal-center phase diagram is determined. Thus the prior finite norm algorithm and free-space reduction are acknowledged as inputs, while the explicit star-geometry minimax/equality classification is the additional conclusion.

## Limitations

This is a result for this natural four-point metric star and all real \(p\)-Banach targets; it does not assert a sharp constant for every three-point metric, arbitrary graphs, or complex \(p\)-Banach targets. The optimal-center classification is for the canonical free-space triple, not an assertion of uniqueness of extensions for every target. No independent audit has been performed. Equivalent presentations under alternative terminology in unindexed literature remain possible.

## References

[1] J. Bíma, *Lipschitz Free Spaces and Subsets of Finite-Dimensional Spaces*, arXiv:2303.03265 (first public version 6 March 2023), https://arxiv.org/abs/2303.03265.

[2] M. Cúth and T. Raunig, *Canonical embedding of Lipschitz-free p-spaces*, arXiv:2311.02920v1 (6 November 2023), Theorem 2.2 and Corollary 2.7, https://arxiv.org/html/2311.02920v1.

[3] J. Bíma, *Nagata Dimension and Lipschitz Extensions Into Quasi-Banach Spaces*, arXiv:2402.03189v1 (5 February 2024), Proposition 26 and Theorem 30, https://arxiv.org/html/2402.03189v1.
