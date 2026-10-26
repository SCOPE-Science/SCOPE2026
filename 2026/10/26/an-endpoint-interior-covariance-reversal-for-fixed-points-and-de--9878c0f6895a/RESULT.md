# An endpoint–interior covariance reversal for fixed points and descents in Ewens permutations

## Finding

For an Ewens random permutation of \([n]\), \(n\ge4\), with parameter \(\theta>0\), the covariance between the indicator that a *specified* label is fixed and the total number of descents depends on whether that label is an endpoint. All interior labels have the same covariance, which is positive for \(0<\theta<1\), zero for \(\theta=1\), and negative for \(\theta>1\). Both endpoint covariances are strictly negative for every \(\theta>0\).

Precisely, write \(D=\sum_{j=1}^{n-1}\mathbf1_{\{\pi(j)>\pi(j+1)\}}\), \(B_i=\mathbf1_{\{\pi(i)=i\}}\), \(F=\sum_i B_i\), and put

\[
H=(\theta+n-3)(\theta+n-2)(\theta+n-1)^2,
\qquad P=(n-1)(n-3)+2\theta(n-2),
\]
\[
Q=u(u+1)(u+2)+\theta u(3u+5)+\theta^2(4u+6),\qquad u=n-3.
\]

Then

\[
\operatorname{Cov}(B_i,D)=\begin{cases}
-\dfrac{\theta Q}{2H},&i\in\{1,n\},\\[4pt]
-\dfrac{\theta(\theta-1)P}{H},&2\le i\le n-1,
\end{cases}
\]

and

\[
\operatorname{Cov}(F,D)=-\frac{\theta^2(n-1)[n^2-4n+2+2\theta(n-1)]}{H}<0.
\]

The endpoint and interior effects have different orders: for each fixed \(\theta>0\),

\[
\lim_{n\to\infty}n\operatorname{Cov}(B_1,D)=-\theta/2,
\quad \lim_{n\to\infty}n^2\operatorname{Cov}(B_i,D)=-\theta(\theta-1)
\quad(2\le i\le n-1),
\]

uniformly over the interior indices, and \(\lim_{n\to\infty}n\operatorname{Cov}(F,D)=-\theta^2\). Thus an interior fixed point can be positively associated with descents even while the *total* fixed-point count remains negatively associated.

## Assumptions and scope

Fix an integer \(n\ge4\) and a real parameter \(\theta>0\). For each permutation \(\pi\in S_n\), let \(c(\pi)\) be its number of cycles and assign probability

\[
\mathbb P_\theta(\pi)=\frac{\theta^{c(\pi)}}{\theta(\theta+1)\cdots(\theta+n-1)}.
\]

A fixed-point indicator \(B_i\) concerns the *specified label* \(i\), not the total number of fixed points. Descents are ordinary, noncyclic adjacent comparisons in one-line notation; there is no comparison between the last and first entries. There is no large-sample assumption in the finite formulas. The asymptotics hold for fixed \(\theta\) only.

## Proof

**Two-arrow probability and adjacent descents.** Prescribe two distinct source labels \(a,b\) and distinct target labels \(c,d\), corresponding to the two directed arrows \(a\mapsto c\), \(b\mapsto d\). Contract all directed paths thereby prescribed and remove their completed directed cycles. By Ewens weighted cycle enumeration on the remaining free vertices, the sum of \(\theta^{c(\pi)}\) over completing permutations, divided by the full Ewens normalizer, equals

\[
\frac{\theta^{h}}{(\theta+n-1)(\theta+n-2)},
\]

where \(h\in\{0,1,2\}\) is the number of cycles already closed by the prescribed arrows. Indeed each closed prescribed cycle contributes one factor \(\theta\), and each of the \(n-2\) remaining unconstrained linkages has total weight \(\theta(\theta+1)\cdots(\theta+n-3)\); contraction is a weight-preserving bijection between those linkages and the completions.

For adjacent \(a=j,b=j+1\), summing this expression over distinct image targets with \(c>d\), the weighted numerator is \(\theta\) for the transposition \(a\leftrightarrow b\), plus \(\theta(n-2)\) from configurations with exactly one of the two sources fixed, plus \((n-1)(n-2)/2\) from the remaining no-closed-cycle image pairs. Hence the total numerator is \((n-1)(\theta+(n-2)/2)\), independently of \(j\). Equivalently the common descent probability is

\[
q_n=\mathbb P_\theta(\pi(j)>\pi(j+1))
=\frac12+\frac{\theta(1-\theta)}{2(\theta+n-2)(\theta+n-1)}.
\]

[An equivalent expression for the marginal adjacent inversion probability follows from the general pair-inversion theorem of Pinsky–Schickentanz (2025); no novelty is claimed for this marginal.]

**Conditioning on a specified fixed point.** Ewens consistency gives

\[
\mathbb P(B_i=1)=\frac{\theta}{\theta+n-1}=:p_n.
\]

Conditional on \(B_i=1\), after deleting \(i\) and closing the gap in the ordered alphabet, the permutation on the remaining \(n-1\) labels has the Ewens law with the same parameter. If \(i=1\) or \(i=n\), the one comparison adjacent to \(i\) cannot be a descent, while each of the \(n-2\) surviving comparisons is a usual adjacent descent in the smaller Ewens permutation. Therefore

\[
\mathbb E[D\mid B_i=1]=(n-2)q_{n-1}\quad(i\in\{1,n\}).
\]

If \(2\le i\le n-1\), only \(n-3\) comparisons remain genuinely adjacent after deleting \(i\). The two comparisons meeting \(i\) have probabilities \((n-i)/(\theta+n-2)\) and \((i-1)/(\theta+n-2)\): for either other source, its own label has image weight \(\theta\), while each of the \(n-2\) other possible image labels has weight one; count the labels respectively greater and smaller than \(i\). Thus

\[
\mathbb E[D\mid B_i=1]=(n-3)q_{n-1}+\frac{n-1}{\theta+n-2}
\quad(2\le i\le n-1).
\]

In either case \(\mathbb E[D]=(n-1)q_n\), and the elementary identity

\[
\operatorname{Cov}(B_i,D)
=p_n\big(\mathbb E[D\mid B_i=1]-(n-1)q_n\big)
\]

gives the two stated rational formulas by expansion and factorization. (All denominators are positive.) For \(n\ge4\), \(P>0\), and with \(u=n-3\ge1\), each coefficient in \(Q\) is positive. This proves the asserted endpoint sign and exact interior phase change.

**Aggregation and scaling.** Summing the two endpoint formulas and the \(n-2\) equal interior formulas yields the displayed covariance with \(F\). Its numerator factor \(n^2-4n+2+2\theta(n-1)\) is positive for \(n\ge4\) since \(n^2-4n+2\ge2\) there. Finally, divide numerator and denominator of these rational formulas by the leading powers of \(n\) to obtain the three stated asymptotic limits.

## Verification

The supplied standalone `verify.py` enumerates all permutations of sizes \(4\) through \(8\), each under five exact rational concentrations \(\theta\in\{1/3,1/2,1,2,5\}\). For every stratum it independently calculates cycle weights, the total descent mean, each positional fixed-point covariance, and the total covariance as rational numbers, comparing with the formulas above. It uses no sampling. Reproduce with `python3 verify.py`. Exhaustive finite computation corroborates but does not prove the unrestricted formulas; that proof is given above.

## Relationship to prior work

Kammoun (2018) establishes large-sample behavior of descent processes under conjugation-invariant measures including Ewens measures; it does not state this exact finite specified-position fixed-point regression. Féray and Kammoun (first publicly posted December 14, 2023) study asymptotic normality of vincular pattern counts in conjugacy classes, with primary MSC2020 \(60C05\); their fixed-point and descent context motivates distinguishing fixed marked labels from global permutation patterns. Pinsky and Schickentanz (2025) give exact unconditioned pair-inversion probabilities and formulas conditioned on the **number** of fixed points. Their exact one-comparison marginal is an ingredient already covered by prior work, but conditioning on the number of fixed points does not itself determine the dependence with an *individual labelled fixed-point event*.

A publicly indexed result on the uniform-permutation case (2026, *Boundary localization of fixed-point–descent dependence in a uniform permutation*) gives the \(\theta=1\) interior cancellation and boundary effects. The present finite Ewens analysis incorporates that special case and distinguishes the opposite interior signs on the two sides of \(\theta=1\). This comparison is based on its publicly available indexed description, not an inspection of its full text.

## Limitations

The classification is for the standard Ewens measure with fixed positive \(\theta\) on finite permutations and noncyclic descents; it does not assert analogous results for arbitrary conjugation-invariant laws, conditioned cycle types, or when \(\theta\) varies with \(n\). The asymptotic statements only hold for fixed concentration. Although the compared works do not display the specified-position covariance phase diagram in the material inspected, historical priority over every possible equivalent treatment is not established; the 2025 conditioned-inversion formulas are the closest general source and warrant particular attention. This is a direct analytical proof with finite exact checks, not an independent audit.

## References

1. M. S. Kammoun, *Monotonous subsequences and the descent process of invariant random permutations*, arXiv:1805.05253 (initial public posting 2018-05-14), https://arxiv.org/abs/1805.05253.
2. V. Féray and M. S. Kammoun, *Asymptotic normality of pattern counts in conjugacy classes*, arXiv:2312.08756 (initial public posting 2023-12-14), https://arxiv.org/abs/2312.08756.
3. R. G. Pinsky and D. T. Schickentanz, *Inversions in Random Permutations Under the Ewens Sampling Distribution With and Without a Prescribed Number of Fixed Points*, arXiv:2510.20654v2 (2025), https://arxiv.org/abs/2510.20654.
4. *Boundary localization of fixed-point–descent dependence in a uniform permutation*, indexed finding (2026), https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-boundary-localization-of-fixed-point-descent-dependence-in-a-uni--6e228e1e9495.
