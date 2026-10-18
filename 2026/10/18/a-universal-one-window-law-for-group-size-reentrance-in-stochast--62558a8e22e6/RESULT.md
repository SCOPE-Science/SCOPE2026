# A universal one-window law for group-size reentrance in stochastic public goods

## Finding

**Theorem (one unfavorable group-size interval).** Fix a multiplication factor \(r>1\), a selection strength \(s>0\), and a probability distribution \(\mu\) of positive geometric return factors \(\omega\). Suppose \(\mu\) has compact support in \((0,\infty)\), does not change with group size, and assigns positive probability to \(\omega>1\). For every integer group size \(G>r\), put
\[
Q_G=\frac rG\int\omega^{G-1}\,d\mu(\omega).
\]
For the well-mixed, infinite-population Fermi dynamics defined below, precisely two possibilities arise:

* If \(Q_G\le1\), every initial cooperation frequency \(x(0)\in(0,1)\) converges to full defection \(x=0\).
* If \(Q_G>1\), full defection and full cooperation are both attracting. Exactly one interior equilibrium \(x_G^*\in(0,1)\) separates their basins: trajectories below it converge to \(0\), and trajectories above it converge to \(1\).

The sequence \((Q_G)\) is strictly log-convex in its integer index and tends to infinity. **Consequently the set of group sizes for which every interior trajectory defects is either empty or one finite consecutive interval of integers.** Thus increasing group size can destroy cooperation's attraction and later restore it, but it cannot produce multiple separated unfavorable bands under these assumptions.

This behavior occurs in the original two-environment model, not only in a generalized return law. For
\[
r=\frac92,\qquad
\mu=\frac45\delta_{11/10}+\frac15\delta_{9/10},
\]
the complete classification for all integer \(G\ge5\) is **bistability at \(G=5,6\)**, **universal interior defection at \(7\le G\le17\)**, and **bistability at every \(G\ge18\)**. The three regimes persist after sufficiently small perturbations of these numerical parameters.

## Assumptions and scope

In a group of size \(G\), exactly \(k\) individuals contribute one unit each. Conditional on a positive random geometric return factor \(\omega\), the per-capita public return is
\[
\frac rG\sum_{j=0}^{k-1}\omega^j,
\]
where an empty sum is zero and \(\omega=1\) has its continuous linear-return interpretation. Cooperators also incur unit cost; defectors do not. The return factor is independently drawn for each group and is independent of group composition, with the same distribution \(\mu\) for every group size. A well-mixed infinite population has cooperator frequency \(x\in[0,1]\), and the number of cooperative co-players is binomial with parameters \(G-1\) and \(x\). The deterministic mean-field dynamics follow pairwise Fermi imitation of average payoffs, at any \(s>0\).

This extends the two-point environment in Zhu et al. (2024) to an arbitrary **fixed compactly supported** positive return-factor law. It does not model finite-population stochastic fixation or environments that change with frequency or group size.

## Proof

**1. Exact payoff difference and dynamics.** If the tagged player faces \(k\) cooperative co-players, the payoff of switching from defection to cooperation changes by
\[
\frac rG\left(\sum_{j=0}^{k}\omega^j-\sum_{j=0}^{k-1}\omega^j\right)-1
=\frac rG\omega^k-1.
\]
Taking the binomial and environmental expectations gives the cooperator-minus-defector average payoff
\[
F_G(x)=\frac rG\int\bigl(1+(\omega-1)x\bigr)^{G-1}\,d\mu(\omega)-1.
\]
The flow is
\[
\dot x=x(1-x)\tanh\!\left(\frac s2F_G(x)\right).
\]
Thus the interior direction of motion is exactly the sign of \(F_G\). For \(G>r\),
\[
F_G(0)=\frac rG-1<0,\qquad F_G(1)=Q_G-1.
\]
For \(G\ge3\), differentiating twice under the finite-moment integral yields
\[
F_G''(x)=\frac{r(G-1)(G-2)}G
\int(\omega-1)^2\bigl(1+(\omega-1)x\bigr)^{G-3}\,d\mu(\omega)\ge0.
\]
For \(G=2\), \(F_G\) is affine and hence also convex. Therefore, if \(Q_G\le1\), convexity puts \(F_G(x)<0\) throughout \(0\le x<1\). Every strictly interior solution decreases and its only possible limit is \(0\). At equality, \(x=1\) is still an equilibrium, but it attracts no strictly interior solution. If \(Q_G>1\), continuity supplies a root between the negative left endpoint and positive right endpoint. Convexity and \(F_G(0)<0\) imply uniqueness: were \(0<a<b\le1\) both roots, convexity would give \(F_G(a)\le (1-a/b)F_G(0)+(a/b)F_G(b)<0\). The signs therefore cross from negative to positive at this unique root. The scalar flow gives exactly the basins stated above and local attraction of both boundary equilibria.

**2. The one-window law.** Set \(M_G=\int\omega^{G-1}\,d\mu(\omega)>0\). Cauchy--Schwarz applied to consecutive powers gives
\[
M_G^2\le M_{G-1}M_{G+1}.
\]
Since \(Q_G=rM_G/G\), for each integer \(G\ge2\),
\[
\frac{Q_G^2}{Q_{G-1}Q_{G+1}}
=\frac{M_G^2}{M_{G-1}M_{G+1}}\,
\frac{(G-1)(G+1)}{G^2}<1.
\]
Hence \(\log Q_G\) is strictly convex on the integer index: any group size between two with \(Q\le1\) also has \(Q\le1\). Thus the unfavorable group sizes form a consecutive integer set. To show it is finite, positive mass above \(1\) supplies some \(\epsilon>0\) and \(c>0\) with \(\mu([1+\epsilon,\infty))\ge c\). Consequently
\[
Q_G\ge\frac{rc}{G}(1+\epsilon)^{G-1}\longrightarrow\infty.
\]
The unfavorable set is therefore a finite interval or empty. Strict convexity also makes the adjacent ratios \(Q_{G+1}/Q_G\) strictly increasing.

**3. Exact reentrance and robustness.** For the displayed two-atom law, elementary substitution yields
\[
Q_G=\frac{9\bigl(4\cdot11^{G-1}+9^{G-1}\bigr)}{G\,10^G}.
\]
The exact integer differences between numerator and denominator at \(G=5,6,7,17,18\), in that order, are
\[
86125,\quad329277,\quad-1440835,\quad
-29132543211735635,\quad346187661271574877.
\]
Thus \(Q_5,Q_6>1\), \(Q_7,Q_{17}<1\), and \(Q_{18}>1\). Strict log-convexity forces \(Q_G<1\) for all integers \(7\le G\le17\). Since \(Q_{18}>Q_{17}\), increasing adjacent ratios force \(Q_G>1\) for every integer \(G\ge18\). This proves the complete classification. All five finite inequalities and \(4<r<5\) are strict, so their signs persist on an open neighborhood of the given return-law parameters; the same log-convex argument then preserves the entire infinite-index classification.

## Verification

Run `python3 verify.py` with Python 3. The standalone standard-library script recomputes the exact rational differences, tests the payoff's binomial-moment identity at several group sizes and rational frequencies, and checks sampled strict log-convex inequalities. The program's finite checks supplement, rather than replace, the all-size Cauchy--Schwarz argument. The script must be considered alongside the proof, since neither finite enumeration nor numerical trajectories establishes an infinite classification.

## Relationship to prior work

Zhu et al. (2024, arXiv:2408.02042v1) define the stochastic two-point synergy/discounting game. Their main Eq. (6), Supplementary Note 1, and Supplementary Note 4 supply its fixed-size evolutionary law, its equilibrium regimes, and a qualitative group-size aggregation dilemma. The present result keeps the paper's dynamics but proves a **cross-group-size** structural constraint for *every* compactly supported return-factor distribution, together with a complete rational example having two separated bistable size ranges.

Hauert et al. (2006) derive the geometric synergy/discounting payoff and fixed-size phase diagrams; they do not establish this distribution-independent one-window law. Hauert and McAvoy (2024) analyze a different quadratic-return mechanism and group-size effects. Peña (2012) examines *random group sizes*, not the present fixed group size with a random return factor. The log-convexity argument uses a classical moment inequality but its dynamical consequence and the all-integer reentrance certification are not contained in those fixed-size classifications.

## Limitations

The proof concerns infinite-population deterministic mean-field Fermi imitation, not pathwise fixation in a finite random population. It assumes the same bounded positive return-factor distribution for every group size, group-independent environmental draws, and fixed \(r>1\). If the return law or multiplication factor changes with group size, the one-window conclusion need not hold. The example describes attraction only within the scalar well-mixed model. Search-based comparisons do not certify global literature uniqueness; specialist or inaccessible work may contain related results.

## References

1. W. Zhu et al., *Evolutionary dynamics in stochastic nonlinear public goods games*, arXiv:2408.02042v1 (first posted 2024-08-04), *Communications Physics* **7**, 377 (2024). https://arxiv.org/abs/2408.02042 ; DOI:10.1038/s42005-024-01865-6.
2. C. Hauert, F. Michor, M. A. Nowak, M. Doebeli, *Synergy and discounting of cooperation in social dilemmas*, *Journal of Theoretical Biology* **239**, 195–202 (2006). DOI:10.1016/j.jtbi.2005.08.040; https://personal.math.ubc.ca/~hauert/publications/reprints/hauert_jtb06.pdf.
3. C. Hauert and A. McAvoy, *Frequency-dependent returns in nonlinear public goods games*, arXiv:2404.13728 (first posted 2024-04-21), *Journal of the Royal Society Interface* **21**, 20240334 (2024). https://arxiv.org/abs/2404.13728.
4. J. Peña, *Group-size diversity in public goods games*, *Evolution* **66**, 623–636 (2012). DOI:10.1111/j.1558-5646.2011.01504.x.
5. Y. Jiang et al., *Nonlinear Public Goods Game in Dynamical Environments*, arXiv:2510.10259v1 (2025), a related but dynamically varying-environment model. https://arxiv.org/abs/2510.10259.
