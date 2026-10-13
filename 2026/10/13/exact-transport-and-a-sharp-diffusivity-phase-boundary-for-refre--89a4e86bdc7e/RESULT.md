# Exact transport and a sharp diffusivity phase boundary for refreshed arrow walks

## Finding
Fix an arrow bias \(a\in(0,1)\). In the independently refreshed two-sided arrow environment specified below, the annealed limiting speed and central-limit diffusivity are rational functions of the global refresh probability \(p\in(0,1]\). The speed has the explicit form
\[
v_a(p)=(2a-1)\left(1-\frac{2a(1-a)(1-p)^2}{(2-p)\{p+a(1-a)(1-p)^2\}}\right).
\]
It is strictly increasing in \(p\in(0,1)\) when \(a>1/2\), strictly decreasing when \(a<1/2\), and identically zero when \(a=1/2\).

**The global diffusivity dichotomy is sharp:** \(p\mapsto\Sigma_a(p)\) is strictly increasing on \((0,1)\) **if and only if** \(a=1/2\). In the balanced case its exact law is
\[
\Sigma_{1/2}(p)=\frac{p(3-p)^2}{(2-p)(1+p)^2}.
\]
For every \(a\ne1/2\) there is an interior global maximizer \(p_*\in(0,1)\) with \(\Sigma_a(p_*)>\Sigma_a(1)=4a(1-a)\). No uniqueness of \(p_*\) is asserted. A closed rational expression valid for all biases appears below.

## Assumptions and scope
At each integer site \(x\in\mathbb Z\), independently install a deterministic arrow pointing right with probability \(a\), otherwise left. Start a walker at \(X_0=0\). At each time \(n\ge0\), it follows the arrow at \(X_n\) and moves one unit in the indicated direction. Independently after this step, with probability \(p\in(0,1]\), replace **all** arrows at **all** sites by a newly sampled independent product field; otherwise keep every arrow unchanged. Initial arrows, resampling indicators, and all replacement fields are mutually independent. All statements concern the annealed law, averaging over environments and resampling.

The renewal construction proves that there exist a deterministic speed \(v_a(p)\) and a diffusivity \(\Sigma_a(p)>0\) such that
\[
\lim_{n\to\infty}\frac{X_n}{n}=v_a(p)\quad\text{almost surely},\qquad
\frac{X_n-nv_a(p)}{\sqrt n}\Longrightarrow N(0,\Sigma_a(p)).
\]
Define \(b=1-a\), \(z=1-p\), and for \(0\le z<1\)
\[
R_t(z)=\frac{1+tz}{(1-tz)(1-z^2)},\qquad
S_t(z)=\frac{(1+tz)^2}{(1-tz)^2(1-z^2)},
\]
\[
H_a(z)=aR_a(z)-bR_b(z),\qquad J_a(z)=aS_a(z)+bS_b(z).
\]
Then the exact diffusivity for the entire two-parameter region is
\[
\boxed{\displaystyle
\Sigma_a(p)=p^2J_a(z)-2p^2v_a(p)\{H_a(z)+zH_a'(z)\}
+\frac{2-p}{p}v_a(p)^2,\qquad z=1-p.}
\]
The prime denotes ordinary differentiation of the displayed rational function with respect to \(z\). This expression uses no unspecified moments or series; its denominators are nonzero in the stated domain.

## Proof
**1. Frozen-arrow paths.** Consider a new block with a frozen field, beginning at its origin. If the arrow at the origin points right, let \(K\ge1\) be the first site on the positive ray whose arrow points left. Conditional on the initial right arrow, \(\Pr(K=k)=(1-a)a^{k-1}\). The walker moves \(0,1,\ldots,K\) and then alternates between \(K\) and \(K-1\). Its positive displacement after \(m\ge1\) steps is therefore
\[
D_m^+=\min(m,K)-\mathbf1_{\{m>K,\;m-K\text{ odd}\}}.
\]
Conditional on a left arrow at the origin, the negative of the displacement has the same law with the continuation parameter \(a\) replaced by \(b=1-a\). These descriptions hold even though every unrefreshed trajectory ultimately becomes trapped in a two-cycle.

**2. First two frozen-block moment series.** For a generic continuation parameter \(t\in(0,1)\), \(\Pr(K=k)=(1-t)t^{k-1}\). For \(0\le z<1\), summing the minimum and the alternating correction gives
\[
\sum_{m\ge1}\mathbb E D_m^+\,z^{m-1}
=\frac1{(1-z)(1-tz)}-\frac{(1-t)z}{(1-tz)(1-z^2)}=R_t(z).
\]
For the square, \((\min(m,K))^2=\sum_{j\le\min(m,K)}(2j-1)\); the odd alternating correction is \(2K-1\). Consequently
\[
\sum_{m\ge1}\mathbb E(D_m^+)^2z^{m-1}
=\frac{1+tz}{(1-z)(1-tz)^2}
-\frac{(1-t)z(1+tz)}{(1-tz)^2(1-z^2)}=S_t(z).
\]
Averaging the two initial orientations yields, for the signed frozen displacement \(D_m\),
\[
\sum_{m\ge1}\mathbb ED_mz^{m-1}=H_a(z),\qquad
\sum_{m\ge1}\mathbb ED_m^2z^{m-1}=J_a(z).
\]
All exchanges of sums are justified by \(|D_m|\le m\) and \(z<1\).

**3. Random refresh blocks and limit theorems.** Let \(L\) be the number of steps until and including the next resampling, and let \(D=D_L\) be the signed block displacement. Then \(\Pr(L=m)=p(1-p)^{m-1}\), and the pairs \((L_j,D_j)\) from successive blocks are independent and identically distributed. Translating the freshly sampled product arrow field by the current walker location leaves its law unchanged. Since \(|D|\le L\), all block moments are finite. At \(z=1-p\),
\[
\mathbb ED=pH_a(z),\quad \mathbb ED^2=pJ_a(z),\quad
\mathbb E(LD)=p\{H_a(z)+zH_a'(z)\},
\]
\[
\mathbb EL=\frac1p,\qquad \mathbb EL^2=\frac{2-p}{p^2}.
\]
The renewal-reward strong law gives \(v_a(p)=\mathbb ED/\mathbb EL=p^2H_a(z)\). The renewal-reward central limit theorem (or the i.i.d. bivariate CLT plus renewal-time inversion) gives
\[
\Sigma_a(p)=\frac{\mathbb E[(D-v_a(p)L)^2]}{\mathbb EL}
=p\mathbb E[(D-v_a(p)L)^2].
\]
The terminal incomplete block is negligible on the \(\sqrt n\) scale because \(L\) has a geometric tail; expansion proves the stated rational expression. The variance is strictly positive because distinct nonproportional block outcomes occur with positive probability when \(0<a,p<1\); at \(p=1\) it equals \(4a(1-a)>0\).

**4. Exact speed and global speed monotonicity.** Substituting the definition of \(H_a\), and writing \(c=a(1-a)\), elementary simplification yields the displayed formula for \(v_a\). Its derivative is exactly
\[
\frac{dv_a}{dp}=(2a-1)\,
\frac{2c(1-p)\{2-c(1-p)^3\}}
{(2-p)^2\{p+c(1-p)^2\}^2}.
\]
All factors other than \(2a-1\) are strictly positive on \(0<p<1\), proving the speed statements.

**5. Balanced rate, and the asymmetric interior maximum.** When \(a=b=1/2\), \(H_a\equiv0\), so the variance formula simplifies to
\[
\Sigma_{1/2}(p)=\frac{p(3-p)^2}{(2-p)(1+p)^2},\qquad
\Sigma'_{1/2}(p)=\frac{6(3-p)(1-p)^2}{(2-p)^2(1+p)^3}>0
\]
for \(0<p<1\). For general \(a\in(0,1)\), differentiating the rational expression directly gives
\[
\Sigma_a(1)=4a(1-a),\qquad \Sigma_a'(1)=0,\qquad
\Sigma_a''(1)=24a(1-a)(2a-1)^2.
\]
(The last endpoint-curvature formula is also a specialization of a previously published general identity; it is not the novelty claim here.) Thus, if \(a\ne1/2\), \(\Sigma_a(p)>\Sigma_a(1)\) for every \(p<1\) sufficiently near 1. On the other hand, the rational block formula and \(a,b<1\) show \(\Sigma_a(p)=O(p)\to0\) as \(p\downarrow0\). Continuity therefore forces an interior global maximum whose height strictly exceeds the no-memory endpoint value. Consequently the diffusivity is not monotone; together with the balanced case this proves the claimed if-and-only-if classification.

## Verification
The independent exact-arithmetic checker `check.py` requires Python 3 and SymPy. Run `python check.py` in the directory containing it. The code checks the two frozen moment generating functions against exact finite-horizon arrow calculations, the algebraic formulas for speed and variance, the balanced derivative, all endpoint identities, and finite geometric-tail approximations to the renewal moments. It returned `PASS: 193 finite/exact checks; universal signs follow from the proof.` In particular, these checks do not replace the arguments establishing infinitely many time horizons and all real parameter values.

## Relationship to prior work
Avena and den Hollander (arXiv:1610.00641; original version 2016) introduced walks in globally resampled random environments with **deterministic** resampling schedules and obtained laws of large numbers and central limit theorems. Their principal one-dimensional static-environment assumptions take site transition probabilities in \((0,1)\), whereas the arrows here have probabilities only \(0\) and \(1\). Avena and da Costa (arXiv:2603.22652v1, first public 24 March 2026) survey and extend block decompositions for refreshed environments; Section 3 treats general non-cooling schedules but does not give the sharp Bernoulli-arrow diffusivity dichotomy above.

Martin and Nagel (arXiv:2610.11919v1, first public 8 October 2026) subsequently treated **geometrically** refreshed random environments in general, establishing the regenerative speed/variance identities used here and an endpoint-curvature identity. Those general formulas and the endpoint identity are credited, not claimed as novel. Their inspected manuscript does not evaluate the full arrow-field rational expressions or establish the global strict-increase-if-and-only-if-balanced dichotomy. The distinguishing contribution here is the exact two-cycle enumeration and resulting full refresh-rate phase classification for a singular spatial environment.

## Limitations
The model refreshes **all** arrows simultaneously, has i.i.d. arrows across space and independent geometric refresh blocks, and concerns the annealed law only. It excludes \(a=0,1\) and treats \(p=0\) only as a limit; no uniqueness of the asymmetric interior maximizer or extension to partially refreshed or elliptic environments is proved. As with any literature-based originality comparison, an unindexed equivalent result cannot be excluded. Independent scientific validation has not been performed.

## References
1. L. Avena and F. den Hollander, *Random walks in cooling random environments*, arXiv:1610.00641 (2016), https://arxiv.org/abs/1610.00641 .
2. L. Avena and C. da Costa, *A cohesive account on the ergodic behaviours and scaling limits of Random Walks in Cooling Random Environments*, arXiv:2603.22652v1 (24 March 2026), https://arxiv.org/abs/2603.22652 .
3. R. Martin and J. Nagel, *Random walk in a regenerating random environment*, arXiv:2610.11919v1 (8 October 2026), https://arxiv.org/abs/2610.11919 .
