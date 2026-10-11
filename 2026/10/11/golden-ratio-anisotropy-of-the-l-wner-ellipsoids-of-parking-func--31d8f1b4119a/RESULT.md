# Golden-ratio anisotropy of the Löwner ellipsoids of parking-function polytopes

## Finding
Let \(\mathsf{PF}_n\subset\mathbb R^n\) be the convex hull of the classical parking functions of length \(n\), for each integer \(n\ge2\), with its **standard coordinate Euclidean metric**. Let \(\mathcal E_n\) be its unique minimum-volume enclosing (Löwner) ellipsoid. By permutation invariance there are unique \(t_n\in\mathbb R\) and \(A_n,B_n>0\) such that
\[
\mathcal E_n=\left\{x:\frac{\|(I-H_n)(x-t_n\mathbf1)\|^2}{A_n}+\frac{\|H_n(x-t_n\mathbf1)\|^2}{B_n}\le1\right\},\qquad H_n=\frac{\mathbf1\mathbf1^{\mathsf T}}n.
\]
Set
\[
u=\frac{3-\sqrt5}{2},\qquad h_*=\frac{\sqrt5-1}{4},\qquad v_*=\frac{5(3-\sqrt5)}{24}.
\]
Then the three *exact limiting shape constants* are
\[
\boxed{\lim_{n\to\infty}\frac{t_n}{n}=h_*,\qquad
\lim_{n\to\infty}\frac{A_n}{n^3}=v_*,\qquad
\lim_{n\to\infty}\frac{B_n}{n^3}=h_*^2=\frac{3-\sqrt5}{8}.}
\]
In particular the limiting **squared axial-to-transverse semiaxis ratio** is \(\lim B_n/A_n=3/5\); the semiaxis ratio is \(\sqrt{3/5}\), not \(1\). Furthermore, classify a vertex by its number \(k\) of coordinates strictly above \(1\). If \(\mathcal K_n\) is the nonempty set of integers \(k\) for which at least one vertex of that layer lies on \(\partial\mathcal E_n\), then
\[
\boxed{\lim_{n\to\infty}\max_{k\in\mathcal K_n}\min\left\{\frac{k}{n},\left|\frac{k}{n}-u\right|\right\}=0.}
\]
Thus all ellipsoid-contact vertex layers asymptotically concentrate at the all-one layer or the proportion \(u\) of non-one entries. No assertion is made that both layers occur for every finite \(n\), or that contact is restricted to exactly three layers for each \(n\). As a volume corollary, writing \(\kappa_n\) for the Euclidean unit \(n\)-ball volume,
\[\lim_{n\to\infty}\frac{1}{n^{3/2}}\left(\frac{\operatorname{vol}_n(\mathcal E_n)}{\kappa_n}\right)^{1/n}=\sqrt{v_*}.\]

## Assumptions and scope
A parking function \((x_1,\ldots,x_n)\) is a positive integer vector whose nondecreasing rearrangement \((x'_1,\ldots,x'_n)\) satisfies \(x'_i\le i\). The vertices, as established in the cited primary literature, are the permutations of \((1,\ldots,1,n-k+1,\ldots,n)\) for \(k=0,1,\ldots,n-1\); the \(k=0\) vector is all ones. Translating by \(-\mathbf1\), the corresponding orbit representative has \(n-k\) zero coordinates and the remaining entries \(n-k,n-k+1,\ldots,n-1\). All ellipsoids and eigenvalues are measured in the unscaled standard Euclidean coordinates, and the claim is asymptotic as integer \(n\to\infty\). It does **not** give exact finite-dimensional ellipsoid coefficients or an exact finite-dimensional contact count.

## Proof
**1. An exact finite-dimensional optimization identity.** For \(0\le k\le n-1\), define
\[
S_{n,k}=\sum_{j=n-k}^{n-1}j=\frac{k(2n-k-1)}2,\quad
T_{n,k}=\sum_{j=n-k}^{n-1}j^2,\quad
V_{n,k}=T_{n,k}-\frac{S_{n,k}^2}{n}.
\]
Let \(w=(w_0,\ldots,w_{n-1})\) be any probability vector giving the total mass on each vertex orbit, uniformly within that orbit. The covariance of the translated vertex distribution has eigenvalue \(\sum_k w_k V_{n,k}/(n-1)\) on \(\mathbf1^\perp\), and eigenvalue \(\operatorname{Var}_w(S_{n,k})/n\) on \(\mathbb R\mathbf1\). Put
\[
h_{n,k}=\frac{S_{n,k}}{n^2},\qquad v_{n,k}=\frac{V_{n,k}}{n^2(n-1)},\qquad
\alpha(w)=\sum_k w_kv_{n,k},\quad \beta(w)=n\operatorname{Var}_w(h_{n,k}).
\]
The shape matrix of the optimal Löwner ellipsoid is \(n\) times a maximal-determinant covariance. Hence \(\alpha_n=A_n/n^3\) and \(\beta_n=B_n/n^3\) maximize
\[J_n(w)=\alpha(w)^{n-1}\beta(w).\]
Its center is \(t_n=1+n\tau_n\), where \(\tau_n=\sum_k w_kh_{n,k}\).

For completeness, the covariance principle requires no unproved optimization oracle. For any full-rank probability measure on a finite vertex set, the directional derivative of \(\log\det\operatorname{Cov}(w)\) when mixing toward a vertex \(x\) equals \((x-\mu)^{\mathsf T}\operatorname{Cov}(w)^{-1}(x-\mu)-n\). Concavity of log determinant of covariance shows that at a maximizing measure every vertex satisfies this expression \(\le0\); thus the ellipsoid with center \(\mu\) and shape \(n\operatorname{Cov}(w)\) contains every vertex. Conversely, any enclosing ellipsoid with shape \(Q\) has \(\operatorname{tr}(\operatorname{Cov}(w)Q^{-1})\le1\), so arithmetic-geometric mean gives \(\det Q\ge n^n\det\operatorname{Cov}(w)\). These inequalities prove optimality, and uniqueness of the Löwner ellipsoid is standard. Symmetrizing a maximizing measure over coordinate permutations does not decrease its covariance determinant (covariance of a mixture dominates the mixture of covariances, followed by log-det concavity). Thus it suffices to maximize \(J_n\) over orbit masses.

**2. The limiting orbital polynomials and their sharp quadratic gap.** Write \(s=k/n\). Exact summation yields
\[
h_{n,k}=h(s)-\frac{s}{2n},\quad
v_{n,k}=\frac{v(s)+n^{-1}v_1(s)+n^{-2}v_2(s)}{1-1/n},
\]
where
\[
\begin{aligned}
h(s)&=s-\frac{s^2}{2},&
 v(s)&=s-2s^2+\frac43s^3-\frac14s^4,\\
v_1(s)&=-s+\frac32s^2-\frac12s^3,&
 v_2(s)&=\frac{s}{6}-\frac{s^2}{4}.
\end{aligned}
\]
The derivative \(v'(s)=(1-s)(1-3s+s^2)\) shows that \(v\) has the unique maximum \(v_*\) on \([0,1]\), at \(u=(3-\sqrt5)/2\). Write \(h_*=h(u)\). Crucially, direct expansion gives the **exact polynomial identity**
\[
\boxed{v_*-v(s)-\frac53\bigl(h(s)-h_*\bigr)^2=\frac{s(s-u)^2(\sqrt5-1-s)}6\ge0,\quad0\le s\le1.}\tag{1}
\]
Equality holds only at \(s=0\) and \(s=u\). The coefficient \(5/3=v_*/h_*^2\). Both sides can be checked by arithmetic in \(\mathbb Q(\sqrt5)[s]\).

**3. A determinant lower benchmark.** Let \(M_n=\max_k v_{n,k}\), and choose \(k_n\) attaining it. Smooth polynomial perturbation of the strict nondegenerate maximizer yields \(M_n=v_*+O(n^{-1})\) and \(k_n/n=u+O(n^{-1})\). In the orbit measure that puts weight \(1/(n+1)\) on \(k=0\) and \(n/(n+1)\) on \(k=k_n\),
\[
\alpha=\frac{n}{n+1}M_n,\qquad
\beta=\frac{n^2}{(n+1)^2}h_{n,k_n}^2\longrightarrow h_*^2.
\]
Consequently the *optimal* objective obeys
\[\liminf_{n\to\infty}\frac{J_n}{M_n^{n-1}}\ge\frac{h_*^2}{e}.\tag{2}\]
This benchmark is a dual vertex distribution, not a claim that its associated ellipsoid already contains the polytope.

**4. Concentration and the sharp determinant upper bound.** Write \(\delta_n=M_n-\alpha_n\ge0\). Uniform polynomial convergence and strict maximality of \(v\) imply constants \(c,C>0\), independent of \(n\), such that
\[M_n-v_{n,k}\ge c(k/n-u)^2-C/n.\]
Since \(h_{n,k}\) is uniformly Lipschitz in \(k/n\), this gives \(\beta_n\le C(n\delta_n+1)\). Combining it with (2) and \(J_n\le M_n^{n-1}\exp[-(n-1)\delta_n/M_n]\,C(n\delta_n+1)\) forces \(n\delta_n=O(1)\). It follows that
\[\alpha_n\to v_*,\quad \beta_n=O(1),\quad
\sum_k w_k(k/n-u)^2=O(n^{-1}),\quad\tau_n\to h_*.\tag{3}\]

We now need the *sharp* version of the variance-loss bound. Let \(s_n=k_n/n\) and
\[q_{n,k}=M_n-v_{n,k}-\frac53\bigl(h_{n,k}-h_{n,k_n}\bigr)^2.\]
The exact expansions in Step 2 and identity (1) imply the following elementary uniform bounds for fixed sufficiently small disjoint neighborhoods \(N_0\) of \(0\) and \(N_u\) of \(u\): (a) \(q_{n,k}\ge-C/n\) for \(k/n\in N_0\); (b) \(q_{n,k}\ge-C/n^2\) for \(k/n\in N_u\); (c) \(q_{n,k}\ge0\) outside these neighborhoods for all large \(n\). To see (b) quantitatively, \(q_{n,k_n}=0\), its first derivative in the continuous interpolation variable is \(O(n^{-1})\), and the quadratic coefficient at \(u\) is
\[-\tfrac12v''(u)-\tfrac53h'(u)^2=\frac{7\sqrt5}{12}-\frac54>0;\]
complete the square. In (c), identity (1) is strictly positive on the compact complement. The total optimal mass on \(N_0\) is \(O(n^{-1})\), since \(v_* -v(s)\) is bounded below by a positive constant there and \(\delta_n=O(n^{-1})\). Therefore \(\sum_k w_kq_{n,k}\ge-o(n^{-1})\). As variance is at most the mean squared distance to any reference point,
\[
 n\delta_n\ge\frac53 n\sum_k w_k(h_{n,k}-h_{n,k_n})^2-o(1)
 \ge\frac53\beta_n-o(1).\tag{4}
\]
Since \(M_n\to v_*\), (4) and the determinant upper bound now yield
\[\limsup_{n\to\infty}\frac{J_n}{M_n^{n-1}}\le\limsup_{n\to\infty}\beta_n\exp\!\left(-\frac{\beta_n}{h_*^2}\right)\le\frac{h_*^2}{e}.\]
Comparing with (2), the **unique** maximizer of \(b\mapsto b\exp(-b/h_*^2)\), for \(b>0\), forces \(\beta_n\to h_*^2\). This and (3) prove all three shape limits.

**5. Every contact-layer accumulation point.** The exact optimal ellipsoid satisfies for every vertex orbit \(k\)
\[\frac{n-1}{n}\frac{v_{n,k}}{\alpha_n}+\frac{(h_{n,k}-\tau_n)^2}{\beta_n}\le1,\]
with equality precisely for contacting vertex orbits. If a sequence of contacts has \(k/n\to s\), passing to the limit yields \(v(s)/v_*+(h(s)-h_*)^2/h_*^2=1\). Identity (1) forces \(s\in\{0,u\}\). Compactness upgrades this subsequential statement to the displayed uniform maximum-distance conclusion. Finally, \(\operatorname{vol}(\mathcal E_n)=\kappa_n A_n^{(n-1)/2}B_n^{1/2}\), giving the stated volume limit.

## Verification
The included pure-standard-library `verify.py` checks identity (1) **coefficient-by-coefficient in** \(\mathbb Q(\sqrt5)[s]\), finite orbit moments/covariances using independent explicit permutations for \(n=2,\ldots,7\) (27 orbit instances), and the two-orbit benchmark at six larger dimensions. The verifier additionally gives exact finite-dimensional covariance/contact certificates for \(n=2,3,4\). Its larger-dimensional numerical benchmarks are feasible dual probability distributions, **not** certificates of exact finite-dimensional optimal ellipsoids. The proof of the asymptotic statement is the analytic argument above; no finite computation substitutes for the limit or for the covariance variational principle. Reproduce with `python3 verify.py` from the unpacked package directory; no external modules or input files are required.

## Relationship to prior work
Amanbayeva and Wang introduced the classical parking-function polytope and its vertex/facet and enumeration theory [1]. Hanada, Lentfer and Vindas-Meléndez developed the generalized parking-function polytopes and their volumes [2]. Bayer and collaborators subsequently proved broad combinatorial and polymatroid descriptions [3]. These contributions determine the vertex orbits used as input but do not themselves compute the Löwner ellipsoid or its limiting anisotropy/contact distribution. A minimum-enclosing-**ball** radius, even when available, would not by itself determine the minimum-volume *anisotropic* ellipsoid: a radius and contact layers for a ball do not determine the two independent semiaxes of the Löwner ellipsoid. Classical minimum-volume-ellipsoid theory supplies the covariance determinant principle, but neither the polynomial identity (1) nor the resulting constants for this polytope without an additional calculation. The literature comparison remains limited by the possibility of an equivalent presentation in optimal-design terminology.

## Limitations
This is a leading-order asymptotic theorem for the classical case; it does not supply finite-\(n\) exact coefficients, finite-\(n\) contact multiplicities, higher-order asymptotics, or the full generalized \((a,b,\ldots,b)\) family. The convergence proof is self-contained conditional on the standard vertex description cited in [1], and the standard existence/uniqueness of the Löwner ellipsoid. No independent external mathematical validation is claimed. No absence-of-publication search establishes absolute novelty.

## References
[1] A. Amanbayeva and D. Wang, *The Convex Hull of Parking Functions of Length n*, arXiv:2104.08454 (first public posting 2021-04-17), 2022 journal version, https://ar5iv.labs.arxiv.org/html/2104.08454.

[2] M. Hanada, J. Lentfer and A. R. Vindas-Meléndez, *Generalized Parking Function Polytopes*, arXiv:2212.06885 (first posted 2022-12-13), *Annals of Combinatorics* 28 (2024), 575–613, https://link.springer.com/article/10.1007/s00026-023-00671-1.

[3] M. M. Bayer et al., *Combinatorics of Generalized Parking-Function Polytopes*, arXiv:2403.07387 (first posted 2024-03-12), https://arxiv.org/abs/2403.07387.

[4] Standard Löwner ellipsoid contact/covariance determinant characterization; e.g. the Löwner–John theorem, used here with an explicit finite-dimensional derivation.
