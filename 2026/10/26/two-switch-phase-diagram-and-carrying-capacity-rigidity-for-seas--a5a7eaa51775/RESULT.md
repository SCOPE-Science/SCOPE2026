# Two-switch phase diagram and carrying-capacity rigidity for seasonal Ricker recruitment

## Finding

For two seasonal recruitment maps \(F_1(x)=R_1 x e^{-a x}\) and \(F_2(x)=R_2 x e^{-b x}\), suppose \(0<a<b\) and \(R_1,R_2>0\). Compare the abundance after the season with coefficient \(a\) followed by the season with coefficient \(b\), namely \(F_2(F_1(x))\), to the reverse order \(F_1(F_2(x))\), at each positive initial abundance \(x>0\).

The two sequences have **exactly two distinct positive equality abundances**, with opposite preferred order between them, if and only if
\[
\boxed{R_1>1,\qquad 1+\frac ba(R_1-1)<R_2<R_1^{b/a}.}
\]
In this regime there are \(0<x_-<x_+\) such that \(F_2(F_1(x))>F_1(F_2(x))\) for \(0<x<x_-\) and \(x>x_+\), whereas the inequality reverses strictly for \(x_-<x<x_+\). For all positive parameters (with \(a\ne b\)), there are at most two positive equality abundances. The allowed two-switch interval is nonempty for every \(R_1>1\), because \(u^{b/a}>1+(b/a)(u-1)\) for \(u>1\).

When both seasonal maps have the same positive carrying capacity \(K\), namely \(R_1=e^{aK}\) and \(R_2=e^{bK}\), there are **no strict ordering reversals**:
\[
\boxed{F_2(F_1(x))\ge F_1(F_2(x))\quad(x>0),}
\]
with equality if and only if \(x=K\). Thus the common-equilibrium boundary is a tangency, not a third open phase.

There is an explicit square-root opening of the two crossovers. Fix \(a,b,R_1\) satisfying the first assumptions and \(R_1>1\), put \(K=(\log R_1)/a\) and vary \(R_2=R_1^{b/a}e^{-\delta}\) with \(\delta\downarrow0\). The two positive crossovers satisfy
\[
x_\pm=K-\frac{\delta}{b-a}\ \pm\ \sqrt{\frac{2\delta}{b(b-a)}}+O(\delta).
\]

An exact witness is \(a=1\), \(b=2\), \(R_1=2\), \(R_2=7/2\). Its two equality abundances are
\[
\boxed{x_-=\log\frac7{4+\sqrt2},\qquad x_+=\log\frac7{4-\sqrt2}.}
\]

## Assumptions and scope

The maps act on strictly positive real abundances, without stochasticity, migration, harvesting or saturation beyond the standard Ricker exponential density dependence. The symbols \(R_i\) denote positive low-density recruitment multipliers, and \(a,b\) are positive crowding coefficients. The order of composition is read from right to left. Since interchanging seasons interchanges the two comparisons, fixing \(a<b\) entails no loss for distinct crowding coefficients; the equal-crowding case is not part of the two-switch criterion. The statement compares outputs after **exactly two updates**, not asymptotic cycles, stochastic averages or steady states.

## Proof

**Step 1 (exact log-ratio identity).** Direct substitution gives
\[
\begin{aligned}
F_2(F_1(x))&=R_1R_2x\exp\{-ax-bR_1xe^{-ax}\},\\
F_1(F_2(x))&=R_1R_2x\exp\{-bx-aR_2xe^{-bx}\}.
\end{aligned}
\]
All factors are positive. Therefore the log ratio divided by \(x\), which has exactly the same sign as the output difference, is
\[
g(x):=\frac1x\log\frac{F_2(F_1(x))}{F_1(F_2(x))}
=(b-a)+aR_2e^{-bx}-bR_1e^{-ax}.
\]
Its derivative is
\[
g'(x)=ab\big(R_1e^{-ax}-R_2e^{-bx}\big).
\]
The equation \(g'(x)=0\) has at most one real root, and \(g(x)\to b-a>0\) as \(x\to\infty\). If \(R_2>R_1\), the only positive stationary point is the strict minimum
\[
x_* =\frac{\log(R_2/R_1)}{b-a}>0,
\qquad g(x_*)=(b-a)\left[1-R_1\left(\frac{R_1}{R_2}\right)^{a/(b-a)}\right].
\]
If \(R_2\le R_1\), then \(g'(x)>0\) for \(x>0\) and two positive zeros are impossible. In either case at most two positive zeros are possible.

**Step 2 (complete two-switch criterion).** Exactly two positive simple zeros occur precisely when the strict interior minimum exists and is negative, \(g(0)>0\), and the positive limiting value is retained. These conditions are
\[
R_2>R_1,\quad R_2<R_1^{b/a},\quad R_2>1+\frac ba(R_1-1).
\]
The first two inequalities force \(R_1>1\); then the third implies \(R_2>R_1\). Hence they are equivalent to the boxed criterion. Monotonicity on either side of \(x_*\) establishes the ordering signs, with strict inequalities on open intervals and equality exactly at the two roots. The lower boundary \(g(0)=0\) does not add a positive zero at \(x=0\), since the domain is \(x>0\); at the upper boundary \(g(x_*)=0\) the two zeros merge tangentially.

**Step 3 (common carrying-capacity rigidity).** If \(R_1=e^{aK}\), \(R_2=e^{bK}\) with \(K>0\), set \(u=e^{-a(x-K)}>0\) and \(c=b/a>1\). Then
\[
\frac{g(x)}a=(c-1)+u^c-cu.
\]
Strict convexity of \(u\mapsto u^c\) gives \(u^c\ge1+c(u-1)\), with equality only for \(u=1\), equivalently \(x=K\). Since the log-ratio sign is the output-difference sign, this proves the claimed global inequality and exact equality set. The same identity proves that the upper two-switch boundary consists of a tangency for \(R_1>1\).

**Step 4 (sharp local onset).** Write \(R_c=R_1^{b/a}\) and \(R_2=R_ce^{-\delta}\). For sufficiently small \(\delta>0\), the two-switch criterion holds. The unique minimum is exactly \(x_*(\delta)=K-\delta/(b-a)\), and
\[
g(x_*)=(b-a)\left[1-e^{a\delta/(b-a)}\right]=-a\delta+O(\delta^2),
\qquad g''(x_*(\delta))=ab(b-a)e^{a\delta/(b-a)}.
\]
Taylor expansion at this nondegenerate minimum, uniformly in a fixed neighborhood of \(K\), shows that the two zeros are located a distance \(\sqrt{2\delta/[b(b-a)]}+O(\delta)\) on either side of \(x_*(\delta)\), proving the stated onset. This controls the actual positive roots for all sufficiently small positive \(\delta\), since Step 1 excludes additional zeros.

**Step 5 (exact witness).** For the indicated rational parameters, \(g(x)=1+(7/2)e^{-2x}-4e^{-x}\). With \(y=e^{-x}\), its zero equation is \(7y^2-8y+2=0\), whose roots \((4\pm\sqrt2)/7\) are distinct and both in \((0,1)\). The stated logarithms are therefore the only two positive equality abundances. Their signs follow from Step 2.

## Verification

The standalone standard-library Python file `verify.py` recomputes the exact analytic identities and witness via independent evaluation of both compositions, checks randomized interior and exterior two-switch configurations, common-equilibrium inequalities, and the near-boundary square-root scaling. All numerical tests are finite checks; the universal root count and parameter classification follow from the preceding analytic proof, not the tests.

## Relationship to prior work

The Ricker recruitment law and periodically forced variants are established. Syta and Litak (public 2006 preprint) analyze time-series chaos of a static Ricker map; Sacker (2007) studies periodic compositions \(x\mapsto xe^{p_n-x}\) with common crowding coefficient and proves stable periodic responses in a specified regime; Yang and Sacker (2014) study modified \(\lambda\)-Ricker maps exhibiting an Allee threshold, common-shape semigroup properties and periodic attracting states. None of the inspected results gives the present two-positive-crossover criterion for distinct crowding coefficients, common-carrying-capacity rigidity and square-root onset. A full related-result comparison is included in the scientific review. A separate earlier result concerning when a multiplicative harvest is applied to Ricker maps compares different compositions and does not imply this environment-order phase diagram.

## Limitations

This is a two-update deterministic model; no long-term stability, noisy population forecasts, environmental feedback or field measurement claim follows. The final literature search did not exhaust every possible translated-exponential or unimodal-map theorem. General two-exponential root-count techniques are classical; the proposed contribution is the application-specific sharp parameter classification, its rigidity boundary, and onset scaling. Potential coverage by broader map-ordering theory remains a historical-priority risk. The cited 2022 analysis of the proper periodic Ricker model could not be inspected in full, so absence of related material there is not asserted. Independent scientific validation has not been performed.

## References

1. A. Syta and G. Litak, *Stochastic description of the deterministic Ricker's population model*, arXiv:nlin/0610019v1, public October 9, 2006, https://arxiv.org/abs/nlin/0610019.
2. R. J. Sacker, *A note on periodic Ricker maps*, Journal of Difference Equations and Applications 13 (2007), 89–92, doi:10.1080/10236190601008752; author-uploaded public full text at https://www.researchgate.net/publication/233166868_A_note_on_periodic_Ricker_maps.
3. Y. Yang and R. J. Sacker, *Periodic unimodal Allee maps, the semigroup property and the \(\lambda\)-Ricker map with Allee effect*, Discrete and Continuous Dynamical Systems B 19 (2014), 589–606, doi:10.3934/dcdsb.2014.19.589; lawful author copy at https://dornsife.usc.edu/robert-sacker/wp-content/uploads/sites/256/2023/06/Yang-Lambda_Ricker.pdf.
4. A. Cánovas, *On the proper periodic Ricker model*, Chaos (2022), doi:10.1063/5.0085571. Abstract available; complete text not inspected.
