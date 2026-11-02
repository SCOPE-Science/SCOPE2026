# A sharp long-arm extinction threshold for Banach-valued Lipschitz extensions on stars

## Finding
Fix an integer \(m\ge3\) and a real number \(R\ge1\). Let \(M_{m,R}\) be a tree metric with hub \(o\), \(m\) short leaves \(u_1,\ldots,u_m\) each at distance one from \(o\), and one long leaf \(v\) at distance \(R\) from \(o\). Thus \(d(u_i,u_j)=2\) for \(i\ne j\) and \(d(u_i,v)=R+1\). Put \(N_{m,R}=M_{m,R}\setminus\{o\}\). Let \(\mathfrak t_1(N_{m,R},M_{m,R})\) be the least \(C\) such that every Lipschitz map \(f:N_{m,R}\to Y\) into any real Banach space \(Y\) extends across \(o\) with Lipschitz constant at most \(C\operatorname{Lip}(f)\). Then
\[
\boxed{\mathfrak t_1(N_{m,R},M_{m,R})=
\begin{cases}
\dfrac{m(R+1)^2}{mR^2+2R+m},&1\le R\le \dfrac{m}{m-2},\\[6pt]
2-\dfrac2m,&R\ge\dfrac{m}{m-2}.
\end{cases}}
\]
For every Banach-valued boundary map an optimal universal linear center prescription is
\[
\widetilde f(o)=a\sum_{i=1}^{m}f(u_i)+(1-ma)f(v),\qquad
a=\begin{cases}\dfrac{R(R+1)}{mR^2+2R+m},&R\le\dfrac{m}{m-2},\\[5pt]
\dfrac1m,&R\ge\dfrac{m}{m-2}.
\end{cases}
\]
Among center prescriptions invariant under every permutation of the short leaves, this one is unique. The coefficient of \(f(v)\) is strictly positive below the critical ratio \(R=m/(m-2)\) and vanishes from that ratio onward. For any fixed \(R>1\), all integers \(m\ge \max\{3,\lceil2R/(R-1)\rceil\}\) lie in the zero-long-leaf regime.

## Assumptions and scope
All target Banach spaces are real, and the Lipschitz constant is the usual maximum ratio of norm differences to metric distances. The metric on \(N_{m,R}\) is induced by the stated weighted tree; all \(m+1\) leaves remain distinct for finite \(R\). An extension may depend on the map and on the Banach target; our universal prescription is a particularly strong linear choice. The assertion does not apply to arbitrary asymmetric trees, to \(R<1\), or to \(p\)-Banach targets with \(p<1\). Uniqueness is asserted only in the permutation-invariant affine class.

## Proof
**Weighted-tree zero-mass norm.** Give the leaves the lengths \(\ell_i=1\) for \(1\le i\le m\) and \(\ell_{m+1}=R\). For any real coefficients \(c_j\) summing to zero, the exact norm of the corresponding molecule in the real free Banach space over \(N_{m,R}\) is
\[
\left\|\sum_j c_j\delta_{v_j}\right\|_{\mathcal F(N_{m,R})}=\sum_j\ell_j|c_j|.\tag{1}
\]
For the upper bound, transport positive mass to negative mass along leaf-to-leaf paths through the hub; every transport plan has cost equal to the right-hand side since every such path has length \(\ell_i+\ell_j\). For the lower bound use the real scalar potential \(g(v_j)=\ell_j\operatorname{sgn}(c_j)\); it is one-Lipschitz on the leaves because \(|g(v_i)-g(v_j)|\le\ell_i+\ell_j=d(v_i,v_j)\), and its pairing with the molecule equals the right-hand side. This proves (1) directly, without relying on a computer enumeration.

**A universal center rule and its sharpness.** An affine center rule has coefficients \(w_j\in\mathbb R\), \(\sum_j w_j=1\), and sends any boundary map to \(\sum_jw_j f(v_j)\). By (1) and the universal linearization of Lipschitz maps, its sharp norm is
\[
\Lambda(w)=\max\left\{1,\max_i \frac1{\ell_i}\sum_j\ell_j\left|\mathbf1_{\{i=j\}}-w_j\right|\right\}.\tag{2}
\]
Indeed the stated expression is an upper bound for every Banach target. It is attained when the target is the free Banach space \(\mathcal F(N_{m,R})\) and \(f(v_j)=\delta_{v_j}\), whose Lipschitz constant is one. Moreover, every possible extension value in that finite-dimensional target has a unique affine representation \(\sum_jw_j\delta_{v_j}\) with coefficients summing to one. Thus minimizing (2) over all real affine coefficients computes the *universal* extension constant, not merely the best norm of a predetermined extension operator.

**Symmetry reduction.** Permutations of the \(m\) short leaves act isometrically on \(\mathcal F(N_{m,R})\) and preserve the set of \(m+1\) extremal distance requirements in (2). Averaging any candidate center over this finite isometry group cannot increase their maximum, by convexity of the Banach norm. We may therefore take all short-leaf weights equal to \(a\in\mathbb R\), and the long-leaf weight \(b=1-ma\). Formula (2) becomes the exact one-variable minimax
\[
\Lambda(a)=\max\{1,\ F(a),\ G(a)\},\quad
F(a)=|1-a|+(m-1)|a|+R|1-ma|,\quad
G(a)=m(1+R^{-1})|a|.\tag{3}
\]
If \(a<0\), then \(F(a)>1+R=F(0)\). If \(a\ge1/m\), both \(F\) and \(G\) are nondecreasing (strictly increasing after the endpoint), since \(m\ge3\) and \(R\ge1\). Thus a minimizer lies in \([0,1/m]\). On that interval,
\[
F(a)=1+R+(m-2-mR)a,\qquad G(a)=m(1+R^{-1})a.\tag{4}
\]
Here \(F\) decreases strictly and \(G\) increases strictly. At \(a=1/m\) their values are \(2-2/m\) and \(1+1/R\). They cross inside the interval exactly when \(R\le m/(m-2)\). The crossing is unique and solves
\[
a=\frac{R(R+1)}{mR^2+2R+m},\qquad
\Lambda(a)=\frac{m(R+1)^2}{mR^2+2R+m}.\tag{5}
\]
If \(R\ge m/(m-2)\), \(F\) remains the larger term all the way to the boundary, and the unique minimizing symmetric coefficient is \(a=1/m\), giving \(\Lambda=2-2/m\). The values agree at the breakpoint. For all allowed parameters the minimum is above one; hence the initial \(1\) in (3) does not affect the optimization. This proves the claimed sharp formula and symmetric uniqueness.

**Support transition.** In the crossing regime the long-leaf coefficient simplifies to
\[
1-ma=\frac{m-(m-2)R}{mR^2+2R+m},
\]
which is positive below, and zero exactly at, the critical ratio. Above that ratio the optimal symmetric center is the arithmetic mean of the short-leaf values and ignores the long leaf. Solving \(R\ge m/(m-2)\) for fixed \(R>1\) gives the final dimension threshold.

## Verification
The companion `CHECK.py` uses Python standard-library `fractions.Fraction` exclusively. It verifies the exact weighted-tree dual norm independently against all \(2^{m+1}\) signed endpoint potentials at both geometrically different leaf orbits, checks the closed expression and support transition for \(m=3,\ldots,8\) and a set of rational \(R\) values including every exact breakpoint, and compares each predicted minimum against 81 further rational symmetric prescriptions. It reports 4,674 exact-rational checks. These are finite corroborations only; the all-dimensions theorem is established by equations (1)–(5).

## Relationship to prior work
The one-point trace is the established extension invariant studied by Bíma (2024), whose general bounds do not give the weighted-star exact value. Basso (2017) gives universal finite-point extension bounds, not the length-ratio threshold. Albiac, Ansorena, Cúth and Doucha (2020) treat complementability and Lipschitz extension constructions, without this finite sharp classification. The published equilateral-star computation *Sharp leaf-count transitions in one-point \(p\)-Banach Lipschitz extensions* gives exactly the \(R=1\), \(p=1\) endpoint \(2m/(m+1)\), and the published three-leaf calculation gives its lower-dimensional counterpart; neither implies the anisotropic \(R>1\) phase boundary or zero-long-leaf plateau. The arguments here concern the canonical Banach endpoint rather than any claim of novelty for those previously known endpoints.

## Limitations
The proof establishes the universal sharp *real Banach-valued* one-hub extension constant for precisely the two-arm-length family \(m\ge3\), \(R\ge1\); it does not classify all optimal nonsymmetric centers or solve general unequal-arm star metrics, quasi-Banach targets, or other graph extensions. The sharp formula may have an earlier equivalent presentation in unindexed interpolation or free-space projection literature. No independent scientific audit has been performed.

## References
1. J. Bíma, *Nagata Dimension and Lipschitz Extensions Into Quasi-Banach Spaces*, arXiv:2402.03189v1 (first public 2024-02-05), especially Definition 2 and the finite-subset discussion: https://arxiv.org/html/2402.03189v1.
2. G. Basso, *Lipschitz extensions to finitely many points*, arXiv:1707.06593v1 (first public 2017-07-20), Sections 1 and 4: https://arxiv.org/html/1707.06593v3.
3. F. Albiac, J. L. Ansorena, M. Cúth and M. Doucha, *Lipschitz free spaces isomorphic to their infinite sums and geometric applications*, arXiv:2005.06555v1 (first public 2020-05-13), Sections 1–3: https://arxiv.org/html/2005.06555v2.
4. *Sharp leaf-count transitions in one-point \(p\)-Banach Lipschitz extensions*, public research record (2026-10-11), especially its Finding and Proof, accessible via the published-finding corpus research index.
5. *Sharp three-leaf star extension constants for real \(p\)-Banach targets*, public research record (2026-10-11), especially its Finding and Proof, accessible via the published-finding corpus research index.
