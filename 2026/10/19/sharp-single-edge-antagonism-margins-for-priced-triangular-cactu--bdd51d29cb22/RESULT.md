# Sharp single-edge antagonism margins for priced triangular cactus networks

## Finding

A *triangular cactus* here means a finite connected simple graph whose blocks are triangles or individual bridge edges; at least one triangle is present. In each triangle \(i\), designate a corner \(h_i\). The two edges incident with \(h_i\) each have unit conductance price, and the opposite (backup) edge has price \(t_i>0\). Each bridge \(j\) has price \(c_j>0\). All conductances on the admissible edges are chosen **independently**, are nonnegative, and have total linear expenditure \(B>0\); the positive-conductance support must be connected.

For each admissible edge \(e=uv\), an adversary may subtract a conductance of magnitude \(\delta\geq0\) at precisely this edge, including an edge assigned nominal conductance zero. Write \(L\) for the nominal weighted Laplacian, \(b_e=\mathbf e_u-\mathbf e_v\), and \(R_e=b_e^{\mathsf T}L^+b_e\). The supremum single-edge antagonism magnitude preserving *strict consensus decay on* \(\mathbf1^\perp\) against every location is \(\gamma(w)=1/\max_{e\in E}R_e\) (at equality the worst perturbation creates an extra zero mode).

Define the explicit block-cost coefficient
\[
 k(t)=\begin{cases}
 1+\frac12\sqrt{t(4-t)},&0<t<\frac25,\\[3pt]
 \frac{2(2+t)}3,&\frac25\leq t\leq4,\\[3pt]
 4,&t\geq4.
 \end{cases}
\]
(The coincident endpoint formulas agree.) Put \(K=\sum_i k(t_i)+\sum_j c_j\). Then the **unrestricted global optimum** is
\[
\boxed{\max_{\substack{w_e\geq0,\;\sum_e p_e w_e=B\\\text{connected support}}}\gamma(w)=\frac B K,\qquad
\min_w\max_{e\in E}R_e=\frac K B.}
\]
Every global optimizer puts bridge conductance \(w_j=B/K\) on each bridge. On triangle \(i\), both designated spokes have a common positive conductance \(a_i\), and its backup edge has conductance \(b_i=r_i a_i\), with
\[
 a_i=\frac{B\,k(t_i)}{K(2+t_i r_i)},\qquad
r_i\in\begin{cases}
\left\{\frac{\sqrt{(4-t_i)/t_i}-1}{2}\right\},&0<t_i<\frac25,\\
\{1\},&\frac25\leq t_i<4,\\
[0,1],&t_i=4,\\
\{0\},&t_i>4.
\end{cases}
\]
Thus the optimal allocation is unique unless at least one triangle has price \(t_i=4\); each such triangle supplies one independent closed interval of optimal ratios. In particular, equal conductances on all three triangle edges are forced throughout the nontrivial price plateau \(2/5\leq t_i<4\), even though prices differ. For \(t_i>4\), the optimally omitted backup edge remains a permitted antagonistic attack location.

## Assumptions and scope

Graphs are finite, undirected, simple, and connected as topological candidate networks; no two cyclic blocks share an edge, but triangle blocks may meet at cut vertices. Each block is exactly a single bridge or a triangle, not a larger cycle. The triangle cost pattern requires *two equal-price spokes*, normalized to price one, and a possibly differently priced third edge. The budget is spent exactly and can be redistributed before, but not after, an attack. An attack subtracts conductance on **one** candidate edge at a time; this is neither a simultaneous-edge robustness theorem nor a theorem about stochastic link failure. Connected positive support is required to avoid interpreting a disconnected zero-cost design as a stable consensus network. At the strict stability boundary \(\delta=\gamma(w)\), only positive semidefiniteness remains and asymptotic average consensus is generally lost.

## Proof

**1. Exact link between antagonism and effective resistance.** On \(\mathbf1^\perp\), a connected nominal Laplacian is positive definite. The Cauchy--Schwarz inequality in its energy inner product implies
\[
L-\delta b_e b_e^{\mathsf T}\succ0\text{ on }\mathbf1^\perp
\quad\Longleftrightarrow\quad
\delta\,b_e^{\mathsf T}L^+b_e<1.
\]
At equality, choosing the vector proportional to \(L^+b_e\) makes the perturbed quadratic form vanish. Hence \(\gamma(w)=1/\max_eR_e\) exactly, without small-gain approximations.

**2. Block separation.** The block-cut incidence graph of a cactus is a tree. For unit current driven between endpoints of an edge in one block, any component joined to that block at a single cut vertex carries no current: its harmonic potential is constant. Consequently the effective resistance of those endpoints is exactly what it would be in their own isolated block. A bridge of conductance \(w\) therefore has resistance \(1/w\), independently of the rest of the cactus.

**3. The unrestricted triangle problem.** Label a triangle \(h,u,v\), let its two spoke conductances be \(x,y\) and its backup conductance be \(z\). With \(D=xy+z(x+y)>0\), elementary parallel/series reduction gives
\[
R_{hu}=\frac{y+z}{D},\quad
R_{hv}=\frac{x+z}{D},\quad
R_{uv}=\frac{x+y}{D}.
\]
Set \(a=(x+y)/2\). Since \(xy\leq a^2\), the largest of the three resistances is at least
\[
\max\left\{\frac{a+z}{a^2+2az},\frac{2a}{a^2+2az}\right\},
\]
which is exactly the worst-edge resistance after replacing \(x,y\) by \(a,a\). Equality forces \(x=y\): for \(x\ne y\) the denominator is strictly smaller and at least one displayed numerator is positive. This does *not* assume symmetry of feasible allocations. A finite-cost connected triangle requires \(a>0\), even if \(z=0\).

At fixed triangle expenditure \(C=2a+tz\), put \(r=z/a\geq0\). Its worst-edge resistance is \(f_t(r)/C\), where
\[
f_t(r)=\begin{cases}
\dfrac{2(2+tr)}{1+2r},&0\leq r\leq1,\\[6pt]
\dfrac{(2+tr)(1+r)}{1+2r},&r\geq1.
\end{cases}
\]
On the first interval the derivative is \(2(t-4)/(1+2r)^2\). On the second it is
\[
f_t'(r)=\frac{t(2r^2+2r+1)-2}{(1+2r)^2}.
\]
The second numerator is strictly increasing for \(r\geq1\); it is negative at \(r=1\) precisely when \(t<2/5\). Its unique root in that case is \(r=(\sqrt{(4-t)/t}-1)/2\). For \(2/5\leq t<4\), the first branch decreases up to \(r=1\) and the second increases from there, forcing \(r=1\). At \(t=4\) the first branch is identically \(4\), and the second increases for \(r>1\). At \(t>4\) both branches attain their minimum only at \(r=0\). Substitution gives exactly \(\min_{r\geq0}f_t(r)=k(t)\), with the optimizer ratios listed above.

**4. Global sharpness and completeness of optimizers.** Let \(M=\max_{e\in E}R_e\). For triangle \(i\), its edge-resistance constraints force expenditure at least \(k(t_i)/M\) by the preceding homogeneous local solution. For bridge \(j\), resistance at most \(M\) forces conductance at least \(1/M\), costing at least \(c_j/M\). Summing gives
\[
B\geq\frac{\sum_i k(t_i)+\sum_jc_j}{M}=\frac K M,
\]
so \(M\geq K/B\). Equality is attained by assigning each bridge \(B/K\), and each triangle expenditure \(Bk(t_i)/K\) with the locally minimizing ratio. Since the sum of all blockwise lower bounds then *equals* the whole budget, every global minimizer must saturate every blockwise inequality. The strict spoke symmetrization and complete scalar minimizer classification prove the claimed characterization and uniqueness statement.

## Verification

Run the accompanying `VERIFY.py` with Python 3; it uses only standard-library exact rational arithmetic. It tests arbitrary asymmetric triangle allocations, the low/equal/high-price formulae, the flat price-four optimal family, and full grounded-Laplacian resistances on a three-triangle cactus joined by a bridge. The example has respective backup-edge prices \(2/13\), \(2\), and \(5\), and bridge price \(3/2\). At budget \(B=18/13+8/3+4+3/2\), the proof predicts and direct exact matrix inversion confirms worst edge resistance \(1\). Additional exact rational competitor allocations satisfy the lower bound. The finite checks verify implemented formulas, not the quantified theorem; the argument above proves the theorem for every admissible graph and positive real parameter.

## Relationship to prior work

The single-negative-edge effective-resistance stability criterion is a known fact, established in work of Zelazo and Bürger; it is used as the starting point, not claimed as new. Their cactus discussion concerns signed-Laplacian definiteness with separated negative cycles; it does not optimize priced conductances or classify optimal supports. Ghosh, Boyd, and Saberi study sums of resistance distances and discuss general convex formulations for maximum pairwise resistance, rather than this *edge-endpoint* minimax price classification. Suliman and Weinstein link unit-budget maximum-edge-resistance minimization to infinite Lewis weights; this does not supply the priced cactus closed-form law or the two sharp price thresholds. In a different recent model, Tovar and collaborators identify a triangle edge-deletion threshold \(t=3\) when optimizing *mean pairwise* resistance, not worst admissible-edge resistance. A separate triangular-bouquet design calculation of the all-pairs sum also has a different objective and a size-dependent deletion threshold. The present statement is the exact all-optimizer solution of a distinct cost-sensitive worst-edge stability-margin problem.

## Limitations

This result applies only to a single antagonistic attack, which may target an admissible edge even when its designed conductance is zero. Changing this attack convention, allowing simultaneous attacks, varying both spoke prices independently, or including nontriangular biconnected blocks changes the problem. A numerical test cannot establish novelty; equivalent results may exist under optimal experimental design or graph reweighting terminology. The result does not establish a universal design theorem for arbitrary cacti or graph topologies. Independent scientific validation has not been performed.

## References

- D. Zelazo and M. Bürger, *On the Definiteness of the Weighted Laplacian and its Connection to Effective Resistance*, arXiv:1408.2187v1 (public 10 August 2014), especially Theorems III.3--III.4. https://arxiv.org/abs/1408.2187
- D. Zelazo and M. Bürger, *On the Robustness of Uncertain Consensus Networks*, arXiv:1408.4471v1 (public 19 August 2014), especially Sections IV--V. https://arxiv.org/abs/1408.4471
- A. Ghosh, S. Boyd, and A. Saberi, *Minimizing Effective Resistance of a Graph*, proceedings version 2006; SIAM Review 50 (2008), 37--66. https://web.stanford.edu/~boyd/papers/eff_res.html
- A. Suliman and O. Weinstein, *Infinite Lewis Weights in Spectral Graph Theory*, arXiv:2302.05966v1 (2023), especially Sections 1 and 3. https://arxiv.org/abs/2302.05966
- H. Tovar et al., *Cost convexity controls the architecture of resistance-optimal networks*, arXiv:2610.03627v1 (2026), especially the priced-triangle all-pairs example. https://arxiv.org/abs/2610.03627
