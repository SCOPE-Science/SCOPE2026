# Sharp support-cap phases for two-summand small deviations

## Finding

Let \(L\geq 1\). Among all pairs of independent, not necessarily identically distributed random variables satisfying \(0\leq X,Y\leq L\) almost surely and \(\mathbb E X=\mathbb E Y=1\), define the maximal upper-tail probability
\[
F(L):=\sup\Pr\{X+Y\geq 3\}.
\]
Then the supremum is attained for every \(L\), and its exact value is
\[
F(L)=\begin{cases}
0,&1\leq L<\frac32,\\[2pt]
\displaystyle\frac{1}{L(3-L)},&\frac32\leq L\leq2,\\[5pt]
\displaystyle\frac12,&2\leq L\leq2+\frac1{\sqrt2},\\[5pt]
\displaystyle\frac{2(L-2)+3(L-2)^2}{(2L-3)^2},&2+\frac1{\sqrt2}\leq L\leq3,\\[5pt]
\displaystyle\frac59,&L\geq3.
\end{cases}
\]
Overlapping branch endpoints agree. Equivalently, the sharp lower bound on the strict small-deviation probability \(\Pr\{X+Y<3\}\) is \(1-F(L)\). The bound jumps from zero upper-tail mass below \(L=3/2\) to \(4/9\) at that support threshold, has an exact \(1/2\) plateau, and reaches the unrestricted upper-tail constant \(5/9\) precisely at \(L=3\).

## Assumptions and scope

Independence, nonnegativity, exact separate means equal to one, a common finite almost-sure upper support cap, and an inclusive event \(X+Y\geq3\) are essential to the stated optimization. Distributions may have atoms, including at the threshold, and need not be identical. The cap \(L\) ranges over all real numbers at least one; smaller caps cannot admit a mean-one law. At \(L=3/2\) the jump is caused by the event's inclusion of the equality case. No claims are made for other thresholds, three or more summands, or unequal means and caps.

## Proof

**1. Reduction to mean-one two-point distributions.** This standard moment-mixture reduction is explicitly available in Ling's Proposition 2.3 (2026), and the following formulas show its applicability with the support cap. Let \(\nu\) be any probability law supported in \([0,L]\) with mean one. If \(\nu=\delta_1\) there is nothing to prove. Otherwise put
\[
m=\int_{[0,1)}(1-a)\,\nu(da)=\int_{(1,L]}(b-1)\,\nu(db)>0.
\]
For \(0\leq a<1<b\leq L\), define the mean-one two-point probability law
\[
Q_{a,b}=\frac{b-1}{b-a}\delta_a+\frac{1-a}{b-a}\delta_b.
\]
Place mass \(\nu(\{1\})\) on the degenerate law \(\delta_1\) and use the positive mixing measure \((b-a)\nu(da)\nu(db)/m\) on pairs \((a,b)\). Its total mass is \(1-\nu(\{1\})\): indeed the integral of \(b-a=(b-1)+(1-a)\) separates into the two moment-balance integrals. Multiplying the two atoms' coefficients by the mixing density and integrating against any bounded Borel test function recovers exactly \(\nu\). Hence \(\nu\) is a probability mixture of mean-one laws with one or two support points in \([0,L]\). Applying this separately to the independent marginals and using Tonelli shows that any common upper bound for the success probability of all pairs of such elementary laws also holds for arbitrary admissible laws.

**2. Elementary success patterns.** If either variable is identically one, then success is exactly the event that the other is at least two; this has probability zero for \(L<2\), and Markov's inequality gives probability at most \(1/2\) for \(L\geq2\). For two nondegenerate elementary laws, write their respective supports as \(\{a,b\}\) and \(\{c,d\}\), with \(0\leq a,c<1<b,d\leq L\). Their high-atom probabilities are
\[
q=\frac{1-a}{b-a},\qquad r=\frac{1-c}{d-c}.
\]
The low-low outcome cannot reach three. If even the high-high outcome fails, success probability is zero. Otherwise the inclusion of each cross outcome \((b,c)\) or \((a,d)\) determines the other three possible patterns.

If neither cross outcome succeeds, success probability is \(qr\). Since \(b,d\geq1\) and \(a,c\geq0\),
\[
q\leq\frac1b,\quad r\leq\frac1d,\quad qr\leq\frac1{bd},\qquad b+d\geq3.
\]
For \(3/2\leq L\leq2\), minimizing \(bd\) on the compact segment \(1\leq b,d\leq L\), \(b+d\geq3\), gives \(bd\geq L(3-L)\): the minimum lies on \(b+d=3\), where the concave product \(b(3-b)\) is minimized at \(b=L\) or \(b=3-L\). For \(L\geq2\), the identity \((b-1)(d-1)\geq0\) gives \(bd\geq b+d-1\geq2\). If \(L<3/2\), no support pair reaches the threshold at all.

If exactly one cross outcome succeeds, success requires the corresponding high atom, so its probability is at most \(q\) or \(r\). For example, \(b+c\geq3\) implies \(b\geq2\), and thus \(q\leq1/b\leq1/2\); the other case is symmetric. These patterns are impossible if \(L<2\).

If **both** cross outcomes succeed, necessarily
\[
b\geq3-c,\qquad d\geq3-a.
\]
Success probability is \(q+r-qr\), increasing in \(q\) and \(r\). For fixed lower atoms \(a,c\), both high probabilities decrease as their corresponding upper atoms grow. Thus it suffices to replace \(b,d\) by their smallest admissible values, \(3-c,3-a\), which remain inside \([0,L]\) by the two cross-success inequalities. Set \(A=1-a\) and \(B=1-c\). Then
\[
0<A,B\leq t:=\min\{1,L-2\},\qquad q=\frac{A}{1+A+B},\quad r=\frac{B}{1+A+B}.
\]
Writing \(H(A,B)=q+r-qr\), direct differentiation gives
\[
\frac{\partial H}{\partial A}=\frac{(1-B)(1+A+B)+2AB}{(1+A+B)^3}\geq0,
\]
and the symmetric formula for \(\partial H/\partial B\). Since \(A,B\leq1\), both derivatives are nonnegative; therefore the maximum of this success pattern occurs at \(A=B=t\) and equals
\[
H(t,t)=\frac{2t+3t^2}{(1+2t)^2}.
\]
This final success pattern is possible only when \(L>2\). A comparison with the one-cross maximum is exact:
\[
H(t,t)-\frac12=\frac{2t^2-1}{2(1+2t)^2}.
\]
It dominates \(1/2\) exactly when \(t\geq1/\sqrt2\). Combined with the preceding exhaustive classification, this yields the claimed upper envelope on each support-cap interval.

**3. Attainment and boundary cases.** For \(L<3/2\), any admissible pair has zero success probability. For \(3/2\leq L\leq2\), let \(X\) have atoms \(0,L\) with respective probabilities \(1-1/L,1/L\); let \(Y\) have atoms \(0,3-L\) with probabilities \(1-1/(3-L),1/(3-L)\). Both means are one, each support is within \([0,L]\), and precisely the high-high outcome succeeds. At \(L=2\), the second variable is deterministic one.

For \(2\leq L\leq2+1/\sqrt2\), take \(X\equiv1\) and let \(Y\) be zero or two with probability one-half each. For \(2+1/\sqrt2\leq L\leq3\), take \(X,Y\) independent and identically distributed with atoms \(3-L,L\). Each has high probability \((L-2)/(2L-3)\), and at least one high outcome is exactly the success event. For \(L\geq3\), take independent laws with masses \(2/3,1/3\) at zero and three. All claimed bounds are therefore maxima and not merely suprema.

## Verification

The complete proof above is analytical. The standalone file `check.py` runs with the Python standard library and performs 32,397 exact-rational assertions covering finite grids of all mean-one two-atom marginal pairs, exact arithmetic for the displayed branch formula, and explicit extremizers across rational support caps. It checks the identity \(H(t,t)-1/2=(2t^2-1)/(2(1+2t)^2)\) at rational inputs; that identity and the derivative signs are independently verified algebraically in the proof. The finite grid cannot establish the infinite-dimensional inequality; the two-point mixture and pattern analysis do that.

## Relationship to prior work

Zhi Ling, *On Samuels' Conjecture* (arXiv:2608.18392v1, first publicly available 18 August 2026), proves the sharp **unrestricted** moment-only tail envelope for independent nonnegative summands; for two mean-one variables at threshold three, its value is \(5/9\). Ling's two-point decomposition is used here as a known reduction. Ling's theorem does not depend on a common upper support cap and does not supply the cap-dependent phases, including the jump, nontrivial \(1/2\) plateau, or internal transition \(2+1/\sqrt2\).

Fu, Han, Wang, Yan, Zhang and Zhou, *Sharp small-deviation inequalities for sums of independent nonnegative random variables* (arXiv:2607.23980v1), and Nie and Wei, *On Feige's conjecture* (arXiv:2607.24528v1), independently develop sharp uncapped moment inequalities at and around the unit slack. The latter also states the known sharp two-variable unrestricted lower-tail formula for arbitrary slack. These results do not produce the present support-cap classification. Loper and Regier, *A new tail bound for the sum of bounded independent random variables* (arXiv:2503.17594v1), optimize a Chernoff–Cramér **upper bound** under bounded supports; that optimized surrogate is not the exact extremal event probability determined here. Classical concentration and moment-set arguments support the reduction but do not constitute the new phase formula. This literature comparison cannot exclude an earlier, differently named exact cap-bound theorem.

## Limitations

The result treats exactly two independent nonnegative variables with equal specified means and a common almost-sure cap, and the inclusive threshold three. It does not characterize every optimizer, extend to more variables, or address arbitrary thresholds or dependent marginals. The jump at \(L=3/2\) would not survive unchanged if the event were strict. Priority remains subject to discovery of equivalent, differently indexed older literature; this is not an independently audited mathematical claim.

## References

- Z. Ling, *On Samuels' Conjecture*, arXiv:2608.18392v1, first public posting 18 August 2026, https://arxiv.org/html/2608.18392v1.
- W. Fu, Y. Han, G. Wang, J. Yan, P. Zhang and Z. Zhou, *Sharp small-deviation inequalities for sums of independent nonnegative random variables*, arXiv:2607.23980v1, first public posting 27 July 2026, https://arxiv.org/html/2607.23980v1.
- Z. Nie and J. Wei, *On Feige's conjecture*, arXiv:2607.24528v1, first public posting 27 July 2026, https://arxiv.org/html/2607.24528v1.
- J. Loper and J. Regier, *A new tail bound for the sum of bounded independent random variables*, arXiv:2503.17594v1, first public posting 22 March 2025, https://arxiv.org/html/2503.17594v1.
