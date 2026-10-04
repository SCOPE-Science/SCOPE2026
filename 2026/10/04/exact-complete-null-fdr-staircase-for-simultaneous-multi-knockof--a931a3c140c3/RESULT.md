# Exact complete-null FDR staircase for simultaneous multi-knockoffs
## Finding
Consider the simultaneous multi-knockoff selection rule with \(\kappa\ge 2\) knockoff copies, \(d\ge1\) features, and target level
\[
q=\frac{1}{\kappa r},\qquad r\in\{1,2,\ldots\}.
\]
Under the complete null and the source exchangeability assumptions, suppose the gap statistics are almost surely positive and pairwise distinct. Then the exact false discovery rate is
\[
\operatorname{FDR}_{d,\kappa,r}
=
\sum_{b=0}^{\left\lfloor (d-r)/(r+1)\right\rfloor}
\frac{r}{(r+1)b+r}\binom{(r+1)b+r}{b}
\frac{\kappa^b}{(\kappa+1)^{(r+1)b+r}},
\]
where the sum is zero when \(d<r\). The finite-sample FDR therefore changes only when the feature count reaches \(d=(r+1)b+r\).

Let \(f_{\kappa,r}\in(0,1)\) be the smaller root of
\[
f=\frac{1}{\kappa+1}+\frac{\kappa}{\kappa+1}f^{r+1}.
\]
Then
\[
\lim_{d\to\infty}\operatorname{FDR}_{d,\kappa,r}=f_{\kappa,r}^r.
\]
When \(r=1\), \(f_{\kappa,1}=1/\kappa\), so the limiting FDR equals \(q=1/\kappa\). When \(r\ge2\), the limiting FDR is strictly smaller than \(q=1/(\kappa r)\).

At the common nominal level \(q=0.1\), three admissible choices illustrate the calibration effect of the detection threshold:
\[
(\kappa,r)=(10,1):\ 0.1000000000,\qquad
(5,2):\ 0.02917960675,\qquad
(2,5):\ 0.00417294930.
\]
Thus the one-discovery calibration uses essentially the entire global-null FDR budget, whereas larger detection thresholds remain substantially conservative even with arbitrarily many features.

## Assumptions and scope
The complete null means every feature is null. The source multi-knockoff exchangeability conditions imply that, conditional on the gap statistics, the winner labels are iid uniform on \(\{0,1,\ldots,\kappa}\). Label \(0\) means that the original feature wins; labels \(1,\ldots,\kappa\) mean that a knockoff wins.

The gap statistics are assumed almost surely positive and pairwise distinct. This makes every decreasing-gap prefix attainable by a positive threshold. With tied gaps, a threshold adds an entire tied block at once and the displayed finite-\(d\) formula need not apply without a specified tie rule. No claim is made for non-null mixtures, misspecified knockoff distributions, or data-dependent choices of \(q\), \(\kappa\), or \(r\).

## Proof
Condition on the ordered gap statistics and list features in decreasing gap order. For the first \(j\) features, let \(A_j\) be the number of original wins and \(B_j=j-A_j\) the number of knockoff wins. The published multi-knockoff FDP estimate is
\[
\frac{\kappa^{-1}+\kappa^{-1}B_j}{A_j\vee1}.
\]
At \(q=1/(\kappa r)\), a nonempty prefix satisfies the threshold inequality exactly when
\[
r(1+B_j)\le A_j,
\]
or equivalently
\[
S_j:=A_j-rB_j\ge r.
\]
Under the complete null, conditional on the gaps, the increments of \(S_j\) are iid: an original win contributes \(+1\) with probability \(1/(\kappa+1)\), while a knockoff win contributes \(-r\) with probability \(\kappa/(\kappa+1)\). Because upward jumps have size one, the first crossing of level \(r\) hits level \(r\) exactly.

If the first hit uses \(b\) knockoff wins, it uses \(r(b+1)\) original wins and therefore occurs at
\[
n_b=(r+1)b+r.
\]
Reverse a path that first hits \(r\) at \(n_b\). Its reversed partial sums are \(r-S_{n_b-j}>0\) for \(1\le j<n_b\), so reversal bijects first-hit paths with sequences of the same multiset of increments whose every partial sum is positive. Raney's cycle lemma then says that exactly \(r\) of the \(n_b\) cyclic starting positions are positive, yielding the exact count
\[
N_{r,b}=\frac{r}{(r+1)b+r}\binom{(r+1)b+r}{b}.
\]
This also supplies the needed first-passage lemma rather than treating the ballot count as a computational observation.
Each such path has probability
\[
\left(\frac{1}{\kappa+1}\right)^{r(b+1)}
\left(\frac{\kappa}{\kappa+1}\right)^b
=
\frac{\kappa^b}{(\kappa+1)^{(r+1)b+r}}.
\]
Under the complete null, the false discovery proportion is one exactly when the procedure makes at least one selection and zero otherwise. Summing the disjoint first-passage events with \(n_b\le d\) proves the finite formula.

For the infinite-feature limit, write \(p=1/(\kappa+1)\) and \(s=\kappa/(\kappa+1)\). Let \(h(x)\) be the probability, starting from state \(x<r\), of ever reaching \(r\). The negative drift and upward skip-free structure give the bounded solution vanishing as \(x\to-\infty\). With \(h(x)=f^{r-x}\), the harmonic equation
\[
h(x)=p\,h(x+1)+s\,h(x-r)
\]
reduces to
\[
f=p+s f^{r+1}.
\]
The convex polynomial has one root at \(1\) and exactly one smaller root \(f_{\kappa,r}\in(0,1)\); hence \(h(0)=f_{\kappa,r}^r\).

For \(r=1\), the smaller root is \(1/\kappa\), yielding the nominal level. For \(r\ge2\), put \(a=(\kappa r)^{-1/r}\). The polynomial is negative at \(a\) because
\[
a\left(\kappa+1-\frac1r\right)>1.
\]
Indeed, \((\kappa+1-1/r)^r>\kappa r\): the logarithm of the left-to-right ratio is increasing for real \(r\ge2\), and at \(r=2\) the inequality reduces to \((\kappa+1/2)^2>2\kappa\). Therefore \(f_{\kappa,r}<a\), so \(f_{\kappa,r}^r<1/(\kappa r)\).

## Verification
The bundled `verify.py` performs exact rational exhaustive checks of the finite formula against all binary winner-patterns for several \((\kappa,r,d)\) combinations, checks the first-passage count against direct enumeration, checks the staircase locations, and numerically solves the smaller-root equation for the displayed examples. Running it produces `VERIFY_OK`.

The proof itself is symbolic and does not depend on finite enumeration. The computation is a replay check for arithmetic and boundary cases.

## Relationship to prior work
Gimenez and Zou introduce simultaneous multi-knockoffs, prove that the null winner labels are conditionally iid uniform on \(\{0,1,\ldots,\kappa}\), define the FDP threshold used above, and prove FDR control at level \(q\). They also identify the detection threshold \(\lceil1/(q\kappa)\rceil\). Their main paper and supplementary proof do not state the complete-null finite-feature FDR distribution, the Raney-number staircase, or the limiting root law derived here.

Barber and Candès supply the Selective SeqStep+ mechanism underlying knockoff FDR control. Emery and Keich study a different multiple-knockoff construction and finite-sample FDR-control framework. Searches over the simultaneous multi-knockoff, multiple-knockoff, Selective SeqStep+, complete-null, first-passage, Catalan, Raney, and exact-FDR formulations located control theorems and related competition procedures, but no statement equivalent to the formula above.

The result is not a restatement of the generic FDR bound: at the same nominal level it distinguishes calibration regimes. For example, at \(q=0.1\), the limiting global-null FDR ranges from \(0.1\) at detection threshold one to approximately \(0.00417\) for the admissible pair \((\kappa,r)=(2,5)\).

## Limitations
The formula requires the complete null and tie-free positive gap statistics. It describes the exact probability of any false selection, not power under alternatives and not the FDR for mixtures of null and non-null features. The originality conclusion is literature-search based rather than a proof that no equivalent result exists under different terminology; competition-based multiple-testing literature is the main residual risk.

## References
1. J. Roquero Gimenez and J. Zou, “Improving the Stability of the Knockoff Procedure: Multiple Simultaneous Knockoffs and Entropy Maximization,” arXiv:1810.11378v1, first public 2018-10-26; AISTATS 2019, PMLR 89:2184–2192.
2. R. Foygel Barber and E. J. Candès, “Controlling the False Discovery Rate via Knockoffs,” arXiv:1404.5609; Annals of Statistics 43(5), 2015.
3. K. Emery and U. Keich, “Controlling the FDR in Variable Selection via Multiple Knockoffs,” arXiv:1911.09442, 2019.
