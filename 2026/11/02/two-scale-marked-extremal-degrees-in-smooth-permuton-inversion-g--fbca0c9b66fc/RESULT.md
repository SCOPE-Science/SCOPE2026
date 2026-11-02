# Two-scale marked extremal degrees in smooth permuton inversion graphs

## Finding

Let \(\mu\) be a permuton with a continuous density \(f\) on \([0,1]^2\), uniformly bounded below by a positive constant. Write \(a=f(0,0)\), \(b=f(1,1)\), and \(F=a+b\). Independently sample \(n\) points \((X_i,Y_i)\) from \(\mu\), and join vertices \(i,j\) precisely when \((X_i-X_j)(Y_i-Y_j)<0\). Let \(D_i\) be vertex \(i\)'s degree.

For a point \((x,y)\), define its corner label \(C=0\) if \(x+y\le1\) and \(C=1\) otherwise, and define its local coordinates by
\[
(U,V)=\begin{cases}(\sqrt n x,\sqrt n y),&C=0,\\(\sqrt n(1-x),\sqrt n(1-y)),&C=1.\end{cases}
\]
Order the vertices by increasing \(D_i\), breaking ties by original sample index, and denote the \(j\)-th vertex's associated quantities by \(C_{n,j},U_{n,j},V_{n,j},D_{n,j}\). Set
\[
H_{n,j}=\frac{D_{n,j}-\sqrt n(U_{n,j}+V_{n,j})}{n^{1/4}}.
\]

**Theorem.** For every fixed positive integer \(k\), the joint array \((C_{n,j},U_{n,j},V_{n,j},D_{n,j}/\sqrt n,H_{n,j})_{j=1}^k\) converges in distribution to
\[
\big(C_j,U_j,V_j,S_j,G_j\big)_{j=1}^k.
\]
Here \(\Pi_0,\Pi_1\) are independent planar Poisson point processes on \([0,\infty)^2\) with intensity measures \(a\,du\,dv\) and \(b\,du\,dv\), respectively. The pairs \((C_j,U_j,V_j)\) are the points of their disjoint labeled union, ordered by \(S_j=U_j+V_j\). Independently of both Poisson processes, \(W_{0X},W_{0Y},W_{1X},W_{1Y}\) are four independent standard Brownian motions, and
\[
G_j=W_{C_jX}(U_j)+W_{C_jY}(V_j).
\]
In particular, conditional on the entire limiting Poisson configuration,
\[
\operatorname{Cov}(G_i,G_j\mid\Pi_0,\Pi_1)=
\begin{cases}
\min(U_i,U_j)+\min(V_i,V_j),&C_i=C_j,\\
0,&C_i\ne C_j.
\end{cases}
\]
The limiting low-degree vertices are therefore not generally independent at their second fluctuation scale.

The exact first-scale ranks and geometric marks are explicit: \(F S_j^2/2\) are the successive arrival times of a unit-rate Poisson process, so \(F S_j^2/2\sim\operatorname{Gamma}(j,1)\). Independently across ranks and independently of the radial arrival process, the corner labels have \(\Pr(C_j=0)=a/F\) and the angular fractions \(R_j=U_j/(U_j+V_j)\) are uniform on \([0,1]\). For any one rank, \(G_j/\sqrt{S_j}\) is standard normal conditional on its geometric marks. This one-dimensional normality does **not** assert independence across ranks.

## Assumptions and scope

The random points are independent and identically distributed. The word *permuton* requires both coordinate marginals to be uniform on \([0,1]\). Assume \(f\in C([0,1]^2)\) and \(f(x,y)\ge c>0\) for all coordinates, which implies an upper bound \(f\le C<\infty\). The constants \(a,b,F\) are strictly positive. The integer \(k\) is fixed as \(n\to\infty\); all four Brownian motions start at zero and have covariance \(\min(s,t)\). Convergence is joint, including every listed vertex coordinate, degree, and second-scale fluctuation. The theorem applies in particular to uniformly random permutations, obtained from independently sampled uniform coordinates and their order rankings.

## Proof

**1. Exact degree identity.** For a fixed sampled point \((x,y)\), let \(N_X^-(x)\) count *other* points with \(X<x\), let \(N_Y^-(y)\) count *other* points with \(Y<y\), and let \(N_{--}(x,y)\) count *other* points with both inequalities. Partitioning the inversion partners into northwest and southeast regions gives the identity
\[
D=N_X^-(x)+N_Y^-(y)-2N_{--}(x,y).
\]
Upon replacing both coordinates by their complements, exactly the analogous identity holds at the top-right corner with upper-tail marginal counts and their overlap.

**2. Rare corner configurations.** For any bounded rectangle \(A\subset[0,\infty)^2\), continuity at the two diagonal corners implies
\[
n\Pr\big((\sqrt nX,\sqrt nY)\in A\big)\longrightarrow a\,|A|,
\qquad
n\Pr\big((\sqrt n(1-X),\sqrt n(1-Y))\in A\big)\longrightarrow b\,|A|.
\]
For sufficiently large \(n\), the two corresponding corner sets are disjoint. Multinomial rare-event convergence, or the joint Laplace functional of the binomial point process, therefore gives two independent Poisson point processes of the stated intensities. This is a *point-process* convergence for bounded planar windows, not merely convergence of one minimum.

**3. Four boundary empirical-process limits.** For \(t\ge0\), write
\[
B_{n,X-}(t)=n^{-1/4}\left(\sum_{i=1}^n\mathbf1\{X_i\le t/\sqrt n\}-t\sqrt n\right),
\]
and define \(B_{n,X+},B_{n,Y-},B_{n,Y+}\) analogously from upper and lower marginal strips. On each compact interval of \(t\), these processes converge jointly to four independent standard Brownian motions, independently of the two diagonal-corner Poisson processes.

Here is a direct justification of the simultaneous independence assertion. First Poissonize the sample size to \(N\sim\operatorname{Pois}(n)\). On a fixed compact range \([0,R]\), remove the four \(R/\sqrt n\)-by-\(R/\sqrt n\) corner squares from all four boundary strips. The total number of removed points is tight because \(f\) is bounded and each square has area \(R^2/n\); after dividing strip counts by \(n^{1/4}\), this removal is negligible uniformly in \(t\le R\). The four remaining strip regions are disjoint, so their Poisson counting processes have independent increments and are mutually independent and independent of the diagonal-corner point processes. Their integrated intensities over thresholds \(t/\sqrt n\) equal \(t\sqrt n+O_R(1)\), uniformly in \(t\), because both marginals are uniform and only four small squares were removed. The centered Poisson functional central limit theorem, whose jumps are \(n^{-1/4}\) and whose quadratic variation converges uniformly to \(t\), yields four independent Brownian motions. For de-Poissonization, couple the Poissonized and fixed samples by one iid sequence. Since \(|N-n|=O_{\Pr}(\sqrt n)\), the number of additionally included or excluded points in any width-\(R/\sqrt n\) strip is \(O_{\Pr}(1)\), and in either fixed diagonal-corner square is \(o_{\Pr}(1)\). Thus both the normalized boundary processes and the rare corner configurations have the same joint limit for exactly \(n\) points.

**4. Convert boundary fluctuations into local degree marks.** At any selected corner point with \(U,V\le R\), the overlap count in the exact identity is dominated by the number of sample points in the corresponding \(R/\sqrt n\) corner square, hence is \(O_{\Pr}(1)\) simultaneously for all such points. The difference between strict and non-strict marginal counts is at most one per threshold almost surely. Consequently, uniformly over corner points in a bounded window,
\[
\frac{D-\sqrt n(U+V)}{n^{1/4}}=
B_{n,CX}(U)+B_{n,CY}(V)+o_{\Pr}(1).
\]
The joint convergence in Steps 2–3 and the continuous mapping theorem, with continuous Brownian limiting paths, establish convergence of the entire bounded-window configuration with these Gaussian marks. No independence of different Gaussian marks at the same corner is presumed: they evaluate the same pair of Brownian paths.

**5. Rule out hidden low-degree points.** For a generic point \((x,y)\), its conditional edge probability against an independent point is
\[
h(x,y)=\Pr((X-x)(Y-y)<0)=x+y-2\Pr(X\le x,Y\le y).
\]
By \(f\ge c\),
\[
h(x,y)\ge c\bigl(x(1-y)+(1-x)y\bigr)
\ge \frac c2\min(x+y,2-x-y).
\]
Conditional on its position, its degree is \(\operatorname{Bin}(n-1,h(x,y))\). Fix \(t>0\) and choose \(R>4t/c\). Outside the two corner regions where \(\min(x+y,2-x-y)\le R/\sqrt n\), a binomial lower-tail Chernoff estimate followed by a union bound over all \(n\) vertices shows
\[
\Pr\big(\exists i: D_i\le t\sqrt n,
\ \min(X_i+Y_i,2-X_i-Y_i)>R/\sqrt n\big)=o(1).
\]
On the other hand, the diagonal-corner Poisson processes have arbitrarily many points as the corner radius grows, and Step 4 makes their scaled degrees asymptotically \(U+V\). Thus the \(k\) smallest-degree vertices lie, with probability arbitrarily close to one, in a fixed bounded pair of corner windows. The limiting sums \(U+V\) are almost surely distinct, so sorting by the actual degrees, including the stated finite tie convention, preserves the limiting order. This proves the asserted joint convergence for every fixed \(k\).

**6. Explicit rank and covariance consequences.** The change of variables \((u,v)=(sr,s(1-r))\), with \(s>0\) and \(0<r<1\), has Jacobian \(s\). The union of the corner Poisson processes therefore has intensity \(Fs\,ds\), with independent labels of probabilities \(a/F,b/F\) and independent uniform angular fractions. The map \(z=Fs^2/2\) turns this into a unit-rate Poisson process, yielding the gamma arrival-time law. Conditional on the corner configurations, Brownian covariance is \(\min\) along each shared boundary coordinate and zero between independent corners, giving the displayed covariance formula. In particular, the conditional variance of \(G_j\) equals \(U_j+V_j=S_j\), proving the final one-rank normal statement.

## Verification

The standalone file `verify.py` enumerates every permutation of orders two through eight and verifies the exact inversion-degree identity for every vertex. It separately checks an asymmetric positive permuton with unequal diagonal-corner intensities, evaluates exact rational boundary-count covariance identities, and reports seeded finite-sample diagnostics for the two first degree ranks, corner labels, angles and centered fluctuations. The included `verify_output.txt` records the command's actual output. These checks address normalization and signs but are **not** proofs of the Poisson limit, Gaussian functional limit, or localization argument; those are justified analytically above. Reproduce with `python3 verify.py` using Python 3.10 or later.

## Relationship to prior work

Benoît Corsini, *Minimal inversion of a permuton sample*, arXiv:2607.28992 (first public July 31, 2026), proves a generalized-Rayleigh limit for the **single minimum degree**, with more general corner regularity; its corner counting estimates motivate the first-scale analysis. Bhattacharya and Mukherjee, *Degree Sequence of Random Permutation Graphs*, arXiv:1503.03582 (2015), prove the Rayleigh minimum for the uniform permutation graph and study finite-dimensional degree proportions at macroscopic vertex labels. Neither result states the present jointly ranked locations and shared-Brownian \(n^{1/4}\)-scale fluctuation law. The first-scale gamma/angle consequences naturally extend their corner arguments; the joint Gaussian marks and their conditional covariance require an additional boundary empirical-process limit. Historical priority is not independently certified.

## Limitations

The assumptions require a positive continuous density and uniform coordinate marginals. Degenerate or singular permutons, vanishing corner densities, non-uniform marginals, growing rank \(k\), and quantitative convergence rates are not covered. The second-scale Gaussian variables at different ranks can be dependent despite independent corner labels and angular marks. Finite computations provide only corroboration. The result is analytically argued and self-reviewed, not independently audited.

## References

1. B. Corsini, *Minimal inversion of a permuton sample*, arXiv:2607.28992v1, July 31, 2026, https://arxiv.org/abs/2607.28992 .
2. B. B. Bhattacharya and S. Mukherjee, *Degree Sequence of Random Permutation Graphs*, arXiv:1503.03582v1, March 12, 2015, https://arxiv.org/abs/1503.03582 .
