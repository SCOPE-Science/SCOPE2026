# Two exact sign reversals in the third joint cumulant of Ewens small-block counts

## Finding
Let \(C_1,C_2,C_3\) be the numbers of singleton, doubleton, and tripleton blocks in an Ewens partition of \(\{1,\ldots,n\}\), with \(n\ge6\) and \(\theta>0\). Define \(W_k=\prod_{i=0}^{k-1}(n-i)/(n+\theta-1-i)\), including \(W_0=1\). Their third mixed cumulant is
\[
\kappa_n(\theta)=\frac{\theta^3}{6}\bigl(W_6-W_3^2-W_4W_2-W_5W_1+2W_1W_2W_3\bigr).
\]
Write
\[
Q_n(\theta)=(5n-10)\theta^3+(8n^2-53n+60)\theta^2+(n^3-29n^2+128n-110)\theta-2n^4+14n^3-12n^2-60n+60.
\]
For every integer \(n\ge6\), there is a unique \(\theta_n^*>2\) with \(Q_n(\theta_n^*)=0\), and
\[
\operatorname{sgn}\kappa_n(\theta)=\operatorname{sgn}((\theta-1)Q_n(\theta)).
\]
Thus the cumulant is positive for \(0<\theta<1\), negative for \(1<\theta<\theta_n^*\), and positive for \(\theta>\theta_n^*\), with precisely two zeros. Here \(\theta_6^*=3\); for \(n\ge7\), \(\theta_n^*>3\), and
\[
\theta_n^*=\frac25n+\frac{24}{35}+O(n^{-1}).
\]

## Assumptions and scope
The Ewens sampling formula gives the probability of nonnegative block counts \(c_j\) satisfying \(\sum_j jc_j=n\):
\[
\Pr(C_j=c_j\text{ for all }j)=\frac{n!}{\theta^{\overline n}}\prod_{j=1}^n\frac{(\theta/j)^{c_j}}{c_j!},\qquad \theta^{\overline n}=\prod_{i=0}^{n-1}(\theta+i).
\]
The result concerns the three **distinct** counts \(C_1,C_2,C_3\), under this exact finite-sample law, for every integer \(n\ge6\) and every real \(\theta>0\). It does not claim corresponding sign diagrams for arbitrary block-size triples.

## Proof
The standard factorial-moment extraction from the Ewens formula gives, for pairwise distinct positive sizes \(j_1,\dots,j_r\) whose sum \(k\le n\),
\[
\mathbb E\prod_{s=1}^rC_{j_s}=\frac{\theta^r}{\prod_sj_s}\frac{(n)_{\underline{k}}}{(n+\theta-k)^{\overline{k}}}=\frac{\theta^r}{\prod_sj_s}W_k.
\]
Indeed multiplying the block-count formula by \(\prod c_{j_s}\), shifting each selected count down by one, and summing the remaining Ewens weights on \(n-k\) labels gives this identity. Substitution into the third-cumulant formula proves the displayed \(\kappa_n\) expression.

A direct common-denominator calculation yields the **exact polynomial identity**
\[
W_6-W_3^2-W_4W_2-W_5W_1+2W_1W_2W_3
=\frac{6n(n-1)(n-2)(\theta-1)Q_n(\theta)}{(n+\theta-6)(n+\theta-5)(n+\theta-4)(n+\theta-3)^2(n+\theta-2)^2(n+\theta-1)^3}.
\]
All denominator factors are strictly positive on the stated domain. Consequently the cumulant sign reduces to that of \((\theta-1)Q_n(\theta)\).

To count positive roots, note
\[
Q_n(0)=-2(n-1)(n^3-6n^2+30)<0,\quad
Q_n(2)=-2n(n-4)(n-3)(n-1)<0,
\]
for \(n\ge6\), and \(Q_n''(\theta)=6(5n-10)\theta+2(8n^2-53n+60)>0\) for \(\theta\ge0\). The last constant is positive at \(n=6\) and increases thereafter. Strict convexity puts \(Q_n<0\) throughout \([0,2]\). Also \(Q_n'(2)=n^3+3n^2-24n+10>0\) and the cubic coefficient is positive, so \(Q_n\) increases from a negative value at 2 to infinity, crossing zero exactly once. The factorization \(Q_n(3)=-n(n-6)(n-3)(2n+1)\) settles the stated lower bound.

For the root location, write \(\theta=cn\) and divide the cubic by \(n^4\). Its leading polynomial is \((c+1)^2(5c-2)\), with unique positive simple root \(c=2/5\). The root cannot tend to infinity relative to \(n\) because of the positive cubic coefficient and the negative constant term; comparison at any fixed \(c\) on either side of \(2/5\) shows convergence. Expanding \(Q_n(2n/5+d)\) gives the \(n^3\) coefficient \(49d/5-168/25\). Since the root is simple, solving the next-order implicit equation gives \(d=24/35\) and error \(O(n^{-1})\), completing the proof.

## Verification
Run `python verify_ewens_cumulant.py` with SymPy installed. It independently sums the Ewens sampling formula over all integer partitions for \(6\le n\le12\) at seven rational parameter values; compares 49 exact cumulants with the factorial-moment expression; checks the polynomial factorization, the root-boundary identities and asymptotic coefficients symbolically. Exact finite enumerations corroborate but do not replace the proof for arbitrary parameters.

## Relationship to prior work
The Ewens sampling formula and its factorial moments are classical. Ewens (1972) gives the underlying distribution. Arratia, Barbour, and Tavaré (1992) analyze Poisson-process approximations to the component counts. Crane (2016) surveys the formula and its probabilistic meaning. These sources provide the input law, not an explicitly reported all-sample-size, two-transition classification for the third mixed cumulant of the smallest three block-size counts in the material inspected. In contrast to pairwise sign behavior, the additional root is at a parameter of linear order in sample size. This is a claim about an explicitly solved dependence phase diagram, not the novelty of the Ewens formula itself.

## Limitations
Originality is assessed against accessible material, not independently certified. Earlier work could have the phase diagram implicitly through general generating functions or omitted appendices. The positive-root statement is restricted to singleton, doubleton and tripleton counts; analogous assertions for other triples remain unproved. The numerical checks are finite and cannot establish the general result. No independent audit has been performed.

## References
- W. J. Ewens, “The sampling theory for some alleles in a selectively neutral population” (1972).
- R. Arratia, A. D. Barbour, and S. Tavaré, “Poisson Process Approximations for the Ewens Sampling Formula” (1992).
- H. Crane, “The Ubiquitous Ewens Sampling Formula” (2016), available as full-text HTML at https://studylib.net/doc/27695943/the-ubiqutous-ewens-sampling-formula.
