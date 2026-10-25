# A third-order Gaussian mean-width transition in partial permutohedra

## Finding

Let \(m\ge2\) and \(k\ge1\) be integers, and let the (standard-coordinate) partial permutohedron be
\[
\mathcal P(m,k)=\operatorname{conv}\{x\in\{0,1,\ldots,k\}^{m}:\text{nonzero coordinates of }x\text{ are distinct}\}.
\]
For a uniformly random unit vector \(U\in S^{m-1}\), put \(W_{m,k}(U)=h_{\mathcal P(m,k)}(U)+h_{\mathcal P(m,k)}(-U)\), and denote its mean by \(\overline W_{m,k}\). If \(k=k_m\) and \(k_m/m\to\alpha\in(0,\infty)\), then
\[
\frac{W_{m,k_m}(U)}{m^{3/2}}\xrightarrow{\Pr}2H(\alpha),\qquad
\frac{\overline W_{m,k_m}}{m^{3/2}}\longrightarrow2H(\alpha),
\]
where \(\Phi,\phi\) are the standard Gaussian CDF and density and
\[
H(\alpha)=\begin{cases}
\displaystyle\frac{\operatorname{erfc}(\Phi^{-1}(1-\alpha))}{4\sqrt\pi},&0<\alpha\le\tfrac12,\\[4pt]
\displaystyle\frac{\alpha-1/2}{\sqrt{2\pi}}+\frac1{4\sqrt\pi},&\alpha\ge\tfrac12.
\end{cases}
\]
The function \(H\) is twice continuously differentiable at \(1/2\), but not three times differentiable there: its third derivatives have one-sided limits \(-\sqrt{2\pi}\) and \(0\), respectively. Thus the leading Euclidean mean width has a sharp third-order transition at \(k/m=1/2\).

There are exact finite-dimensional companion identities. For \(G\sim N(0,I_m)\), let \(G_{[1]}>\cdots>G_{[m]}\) be the descending order statistics (almost surely). Then
\[
h_{\mathcal P(m,k)}(G)=\sum_{j=1}^{\min(m,k)}(k-j+1)(G_{[j]})_+.
\]
If \(k\ge m\), the Gaussian support mean has the closed formula
\[
\mathbb E h_{\mathcal P(m,k)}(G)=\frac{km}{\sqrt{2\pi}}-
\binom m2\left(\frac1{\sqrt{2\pi}}-\frac1{2\sqrt\pi}\right),
\]
and for every \(m,k\), \(\overline W_{m,k}=2\mathbb E h_{\mathcal P(m,k)}(G)/\mathbb E\|G\|_2\), where \(\mathbb E\|G\|_2=\sqrt2\,\Gamma((m+1)/2)/\Gamma(m/2)\).

The geometric mechanism is an exact angular stratification. For \(0\le r\le\min(m,k)\), there are \((m)_r=m!/(m-r)!\) vertices with precisely \(r\) nonzero coordinates. Their common spherical exterior angle is
\[
\omega_{m,k,r}=\begin{cases}
\displaystyle\frac1{2^m r!},&0\le r<k,\\[4pt]
\displaystyle\frac{\Pr\{\operatorname{Bin}(m,1/2)\ge k\}}{(m)_k},&r=k\le m.
\end{cases}
\]
When \(r<k\), the full conic intrinsic-volume polynomial of the normal cone is
\[
\sum_{j=0}^{m}v_j(N_r)t^j=
\frac{(1+t)^{m-r}}{2^{m-r}}\;
\frac{\prod_{a=1}^{r}(t+2a-1)}{2^r r!}.
\]
This last polynomial uses the established type-B Weyl-chamber formula; the new claim does not assert novelty of that general chamber formula or of the known vertex classification. The *complete geometric evaluation here* is the combined finite-rank angular law and its explicit mean-width phase profile.

If \(R_m\) is the number of nonzero coordinates of the vertex exposed by \(G\), then exactly
\[
R_m\overset d=\min\{k,\operatorname{Bin}(m,1/2)\}.
\]
If \(k=m/2+\tau\sqrt m+o(\sqrt m)\) (integer-valued) for fixed real \(\tau\), then
\[
\frac{R_m-m/2}{\sqrt m}\Longrightarrow\min\{\tau,Z/2\},\qquad
\Pr\{R_m=k\}\longrightarrow1-\Phi(2\tau),
\]
with \(Z\sim N(0,1)\). This clipped-normal angular crossover occurs at the same ratio as the third-order mean-width transition.

## Assumptions and scope

The polytope uses the ordinary Euclidean inner product in \(\mathbb R^m\). Every statement is for integer \(m\ge2,k\ge1\); asymptotic claims require \(k/m\to\alpha\in(0,\infty)\) and no other relation. The spherical direction is uniform on the **ambient** unit sphere, not on an affine-hull quotient (the polytope is full-dimensional). A Gaussian exterior angle means the probability that an isotropic Gaussian direction selects a prescribed vertex. Conic intrinsic volumes \(v_j\) follow the standard Euclidean cone convention; their generating polynomial is the ordinary polynomial \(\sum_jv_jt^j\).

The vertex-stratification identities remain exact when \(k>m\): only ranks \(r\le m\) exist, all satisfy \(r<k\), and the second case in the angle formula is absent. The phase function concerns ratios tending to positive finite \(\alpha\); no fixed-\(k\) extreme-value asymptotic is claimed.

## Proof

**1. Support maximization and vertices.** For a vector with pairwise distinct, nonzero objective coordinates, a maximizing feasible word cannot use a positive label on a negative objective coordinate, and it must use the largest available labels on the largest positive objective coordinates. If it has \(r\) selected coordinates, those labels are exactly \(k,k-1,\ldots,k-r+1\), and \(r=\min\{k,\#\{i:G_i>0\}\}\). This follows by swapping any two misordered labels and by adding or deleting a strictly beneficial or detrimental coordinate. In particular every such word is uniquely exposed by some objective vector, so it is a vertex; other generating words are not vertices because their support cannot be uniquely optimized. This proves the stated support formula and the vertex multiplicities. The vertex description itself is prior work (Heuer–Striker, Proposition 5.7).

**2. Exact solid angles and conic volumes.** Fix a rank-\(r\) vertex with active coordinates \(i_1,\ldots,i_r\), labeled by \(k,k-1,\ldots,k-r+1\) in that order. If \(r<k\), its normal cone is exactly
\[
\{g:g_{i_1}\ge\cdots\ge g_{i_r}\ge0,\quad g_j\le0\ (j\notin\{i_1,\ldots,i_r\})\}.
\]
The two coordinate blocks are orthogonal, so this is the Cartesian product of a type-B Weyl chamber of rank \(r\) and a negative orthant of dimension \(m-r\). A Gaussian has exactly the prescribed sign pattern with probability \(2^{-m}\), and its \(r\) positive entries have any of the \(r!\) orders equiprobably, proving \(\omega_{m,k,r}=1/(2^m r!)\). The classical type-B formula \(\prod_{a=1}^r(t+2a-1)/(2^r r!)\) and the orthant polynomial \(((1+t)/2)^{m-r}\), with conic-product convolution, give the displayed generating function.

For \(r=k\le m\), the specified \(k\) active indices must be the indices of the \(k\) largest Gaussian coordinates and all must be positive. By permutation exchangeability, conditional on \(B=\#\{i:G_i>0\}\ge k\), each of the \((m)_k\) ordered active-index strings is equally likely. Hence its angle is \(\Pr(B\ge k)/(m)_k\). These angles sum to one because \(\sum_{r<k}\binom mr2^{-m}=\Pr(B<k)\). The binomial law and its central limit theorem yield the exact exposed-rank distribution and clipped-normal critical law.

**3. Mean width under linear parameter scaling.** Let \(k_m/m\to\alpha>0\), and let \(Q_m(t)\) be the descending empirical quantile function of \(m\) standard Gaussian variables. The exact support identity is the right-endpoint Riemann sum
\[
\frac{h(G)}{m^2}=
\frac1m\sum_{j=1}^{m}\left(\frac{k_m-j+1}{m}\right)_+(G_{[j]})_+.
\]
The empirical Gaussian distribution converges in first Wasserstein distance, so the descending quantile functions converge in \(L^1(0,1)\). The weights in this sum converge uniformly to the bounded Lipschitz function \((\alpha-t)_+\). The Gaussian quantile is nonnegative precisely on \(0<t\le1/2\), so
\[
\frac{h(G)}{m^2}\longrightarrow
\int_0^{\min(\alpha,1/2)}(\alpha-t)\Phi^{-1}(1-t)\,dt=H(\alpha)
\]
in probability and in mean. For the mean conclusion, use the uniform-integrability bound \(0\le h(G)/m^2\le(k_m/m)(m^{-1}\sum_i|G_i|)\), whose squared expectations are uniformly bounded.

For the explicit evaluation write \(b=\min(\alpha,1/2)\) and \(z=\Phi^{-1}(1-b)\). Substituting \(t=1-\Phi(u)\) and integrating by parts gives
\[
H(\alpha)=(\alpha-b)\phi(z)+\int_z^\infty\phi(u)^2\,du.
\]
The integral equals \(\operatorname{erfc}(z)/(4\sqrt\pi)\), while \(z=0\) when \(\alpha\ge1/2\). The piecewise formula follows. Below the boundary \(H'(\alpha)=\phi(\Phi^{-1}(1-\alpha))\), \(H''(\alpha)=\Phi^{-1}(1-\alpha)\), and \(H'''(\alpha)=-1/\phi(\Phi^{-1}(1-\alpha))\); above it \(H\) is affine. These derivatives prove the exact differentiability assertion.

For concentration, the support function is \(L_{m,k}\)-Lipschitz with
\[
L_{m,k}^2\le\sum_{j=1}^{\min(m,k)}(k-j+1)^2=O(m^3),
\]
since \(k/m\) stays bounded. Gaussian Poincaré therefore yields \(\operatorname{Var}h(G)=O(m^3)\). Combining this with the mean limit gives \(h(G)/m^2\to H(\alpha)\) in \(L^2\). Apply the same estimate to \(-G\) and use \(\|G\|_2/\sqrt m\to1\) in probability to obtain the directional-width convergence. The Gaussian radius and direction are independent, and support is positively homogeneous, whence \(\mathbb E W(U)=2\mathbb Eh(G)/\mathbb E\|G\|_2\). Since \(\mathbb E\|G\|_2\sim\sqrt m\), this proves the mean-width limit.

**4. Exact saturated finite-size mean.** For \(k\ge m\), let \(Y_i=(G_i)_+\). For descending positive entries, \(\sum_{j\ge1}(j-1)Y_{[j]}=\sum_{i<j}\min(Y_i,Y_j)\). Therefore
\[
h(G)=k\sum_i Y_i-\sum_{i<j}\min(Y_i,Y_j).
\]
Integration of the independent Gaussian tail gives
\[
\mathbb EY_i=\frac1{\sqrt{2\pi}},\qquad
\mathbb E\min(Y_i,Y_j)=\int_0^\infty(1-\Phi(t))^2dt=\frac1{\sqrt{2\pi}}-\frac1{2\sqrt\pi}.
\]
Taking expectations proves the exact finite-dimensional formula.

## Verification

The included standalone checker `verify_geometry.py` independently enumerates all generating vertices for \(2\le m\le5\), \(1\le k\le5\), and compares direct linear maximization with sorted-score support on 700 random Gaussian objectives. It also checks all normal-angle orbit probabilities sum to one; evaluates the Gaussian-minimum integral independently; checks the closed \(H\) formula by numerical quantile integration; tests Gaussian support means through dimensions 50, 200, and 800; and verifies the type-B/orthant coefficient product (including its highest-degree solid angle) through dimension nine. It finishes with `VERIFY_OK`.

The general theorems rely on the preceding proofs and the cited established Weyl-chamber formula, not on finite numerical checks. Monte Carlo diagnostics are not proofs of limits or novelty.

## Relationship to prior work

Heuer and Striker define the partial permutohedra and identify their vertices, facets, and face structure. Behrend and collaborators extend their face-lattice, volume and Ehrhart theory. These sources supply the *objects* and their already-known discrete geometry, not a Gaussian mean-width phase profile. The type-B conic intrinsic-volume polynomial is established by Godland and Kabluchko; here its product with an orthant is applied to a particular family of normal cones, so that ingredient alone is not claimed to be new. General Gaussian-width and order-statistics tools provide the analytic language, but do not by themselves evaluate the explicitly displayed \(\operatorname{erfc}\)-profile and its third-derivative transition for this family. The proposed contribution is the quantitative relationship among the spherical width, angular orbit saturation, and the sharp differentiability boundary.

## Limitations

The phase law assumes a finite, strictly positive limit of \(k/m\). It does not cover fixed \(k\), superlinear \(k\), or second-order central limit fluctuations of widths. The full conic intrinsic-volume polynomial is given only at the lower-rank vertices \(r<k\); for the saturated orbit \(r=k\le m\), only its top conic volume (solid angle) is evaluated. The known type-B chamber formula and vertex classification are cited as inputs. No claim of independent mathematical auditing or uniqueness within all possible equivalent formulations in the literature is made.

## References

1. D. Heuer and J. Striker, *Partial permutation and alternating sign matrix polytopes*, arXiv:2012.09901, first posted 17 December 2020, especially Section 5 and Proposition 5.7. https://arxiv.org/abs/2012.09901
2. R. E. Behrend, F. Castillo, A. Chavez, A. Diaz-Lopez, L. Escobar, P. E. Harris, and E. Insko, *Partial permutohedra*, arXiv:2207.14253, first posted 28 July 2022, especially Sections 1, 3–6. https://arxiv.org/abs/2207.14253
3. T. Godland and Z. Kabluchko, *Conic intrinsic volumes of Weyl chambers*, arXiv:2005.06205, first posted 13 May 2020, Theorem 1.1 (type B). https://arxiv.org/abs/2005.06205
4. Z. Kabluchko, A. E. Litvak, and D. Zaporozhets, *Mean width of regular polytopes and expected maxima of correlated Gaussian variables*, arXiv:1511.08479 (background on the Gaussian-support approach; not a partial-permutohedron phase theorem). https://arxiv.org/abs/1511.08479
