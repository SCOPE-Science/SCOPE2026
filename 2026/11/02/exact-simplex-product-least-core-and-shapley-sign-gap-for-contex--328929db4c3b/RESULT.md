# Exact simplex-product least core and Shapley sign gap for contextual distractors

## Finding
For a contextual-distractor cooperative game with \(u\ge1\) useful players, \(d\ge1\) distractors, additive useful credits \(m_i\ge0\), distractor baseline \(a>0\), and exceptional bonus \(b>0\) earned by precisely the coalition of all useful players, the exact least-core excess is \(\varepsilon^*=b/2\). The least-core payoff set is a translated product of scaled simplices, has affine dimension \(u+d-2\), and has exactly \(ud\) vertices. Its unique nucleolus and Euclidean minimum-norm point admit explicit formulas.

Let \(C=\binom{u+d}{u}\). Each distractor's Shapley value is \(a-b/(dC)\), whereas the total distractor credit of **every** least-core payoff vector is \(da-b/2\). Consequently, all distractors receive positive Shapley credit although at least one receives negative credit at **every** least-core point if and only if
\[
2ad<b<ad\binom{u+d}{u}.
\]
This interval is nonempty precisely when \(\binom{u+d}{u}>2\). At a vertex, exactly one distractor is negative in this regime; the nucleolus and minimum-norm selector assign negative credit to all distractors.

## Assumptions and scope
Let \(U\) and \(D\) be disjoint labeled player sets, \(|U|=u\ge1\), \(|D|=d\ge1\), and \(N=U\cup D\). For \(m_i\ge0\), \(a>0\), and \(b>0\), set
\[
v(S)=\sum_{i\in S\cap U}m_i+a|S\cap D|+b\mathbf{1}_{\{S=U\}},\qquad S\subseteq N.
\]
The term \(b\) represents the valuable context requiring every useful player and no distractor. The characteristic function has \(v(\varnothing)=0\). Define the excess \(e_S(x)=v(S)-\sum_{i\in S}x_i\). An admissible payoff is any **signed**, efficient vector \(x\in\mathbb R^{u+d}\) satisfying \(x(N)=v(N)\); negative credits are allowed. Minimize \(\max_{\varnothing\ne S\subsetneq N}e_S(x)\), without an additional individual-rationality or nonnegativity restriction. The nucleolus is the unique lexicographic minimizer of the sorted proper-coalition excesses among efficient payoffs; the minimum-norm selector minimizes \(\|x\|_2\) over the least core.

Write \(c_i=m_i\) for \(i\in U\), \(c_j=a\) for \(j\in D\), \(y=x-c\), and \(T=b/2\). Then the **entire** least core is
\[
\left\{x=c+y:\quad y_i\ge0\ (i\in U),\quad \sum_{i\in U}y_i=T,\quad y_j\le0\ (j\in D),\quad \sum_{j\in D}y_j=-T\right\}.
\]
The two factors are \(T\Delta_{u-1}\) and \(-T\Delta_{d-1}\), including the zero-dimensional simplex when a group has one member. Its vertices correspond to choosing one useful player to receive all \(T\) and one distractor to surrender all \(T\).

## Proof
**Optimal excess and geometry.** Efficiency gives \(\sum_{i\in N}y_i=0\). Let \(t=\sum_{i\in U}y_i=-\sum_{j\in D}y_j\). The nonempty proper complementary coalitions \(U\) and \(D\) have excesses \(b-t\) and \(t\), hence \(\varepsilon\ge\max(b-t,t)\ge b/2=T\). Set \(y_i=T/u\) on \(U\) and \(y_j=-T/d\) on \(D\). Then \(e_U=T\), while for each other nonempty proper coalition \(S\), \(e_S=-y(S)\le T\) because all the negative residual contributions sum to \(-T\). Thus \(\varepsilon^*=T\), and at every least-core point \(y(U)=T\), \(y(D)=-T\).

For any proper nonempty \(S\ne U\), the optimal excess constraint says \(y(S)\ge-T\). Taking complements shows \(y(S)\le T\) for every subset \(S\): for \(S=D\) this follows from \(y(D)=-T\), for \(S=\varnothing,N\) it is immediate, and all other subsets have a proper complement other than \(U\). Let \(P=\{i:y_i>0\}\); then \(y(P)\le T\). But \(y(U)=T\), so the sum of positive contributions is at least \(T\). Equality forces no negative useful contributions and no positive distractor contributions. Conversely, those signs together with the two group sums imply \(-y(S)\le T\) for \(S\ne U\), proving the exact product description, dimension, and \(ud\) vertices.

**Nucleolus.** Subtracting the additive baseline \(c\) translates efficient payoffs and leaves every coalition excess unchanged. The residual game \(w(S)=b\mathbf1_{\{S=U\}}\) is invariant under permutations within \(U\) and within \(D\). Uniqueness of the prenucleolus forces its residual vector to be constant on each of these two groups. Since every least-core point has group sums \(T\) and \(-T\), the only possibility is
\[
x_i^{\mathrm{nuc}}=m_i+\frac{b}{2u}\quad(i\in U),\qquad x_j^{\mathrm{nuc}}=a-\frac{b}{2d}\quad(j\in D).
\]

**Minimum Euclidean norm.** On the product of simplices, the distractor squared-norm sum is uniquely minimized at equal residual charges \(y_j=-T/d\). For useful players, minimize \(\sum_{i\in U}(m_i+y_i)^2\) subject to \(y_i\ge0\) and \(\sum y_i=T\). Strict convexity and the Karush–Kuhn–Tucker equations give
\[
x_i^{\min}=\max\{m_i,\theta\},\quad\sum_{i\in U}\max\{0,\theta-m_i\}=T;
\qquad x_j^{\min}=a-\frac{T}{d}\quad(j\in D),
\]
where the scalar \(\theta\) solving the displayed equation is unique because \(T>0\). If \(\theta\ge\max_i m_i\), all useful payoffs are equal, unlike the nucleolus when the baselines differ.

**Shapley attribution.** The additive baseline contributes exactly \(c\). For a useful player \(i\), the bonus is gained in a random permutation exactly when the predecessor set is \(U\setminus\{i\}\), probability \((u-1)!d!/(u+d)!=1/(uC)\). For a distractor \(j\), the bonus is lost exactly when the predecessor set is \(U\), probability \(u!(d-1)!/(u+d)!=1/(dC)\). Hence
\[
\phi_i=m_i+\frac{b}{uC},\qquad \phi_j=a-\frac{b}{dC}.
\]
All distractor Shapley credits are positive iff \(b<adC\). The total distractor least-core credit is \(da-T\). If \(b>2ad\), this total is negative and every least-core point includes a negative distractor. If \(b\le2ad\), the symmetric point has every distractor credit nonnegative, so the stronger universal-negative statement fails. At each vertex there is one distractor with \(y=-T\), all others have \(y=0\); when \(T>ad\), that one credit is negative and the others equal \(a>0\). The nucleolus and minimum-norm credits on \(D\) are \(a-T/d<0\). This proves the if-and-only-if gap.

## Verification
Run `python verify_contextual.py` with Python, NumPy and SciPy. The standalone checker enumerates **every proper coalition** in 72 small parameter instances, independently optimizes each least-core LP, exactly evaluates Shapley permutation weights, checks all 360 asserted simplex-product vertices and performs four numerical minimum-norm projection comparisons. The recorded output is `VERIFY_OK cases=72 coalitional_constraints=2376 simplex_vertices=360 min_norm_cases=4`. Rational enumeration supports, but does not replace, the all-size analytical proof above.

In the motivating \(u=4,d=2,a=5,b=60\) example, \(C=15\). The least-core excess is \(30\), the product has \(8\) vertices, the Shapley distractor credit is \(3\), and the nucleolus/minimum-norm distractor credit is \(-10\), agreeing with the published numerical example.

## Relationship to prior work
Kera, Yamauchi and Nagarajan (2026) introduce the contextual-distractor instance in their Section 3.3 and compare LP, minimum-norm, nucleolus, entropic least-core, and Shapley allocations, including numerical examples and sampling experiments. Their work motivates the exact family analyzed here but does not state the parametric simplex-product least-core description, the all-parameter minimum-norm formula, or the exact sign-gap interval in the inspected full text. The nucleolus and Shapley operators are classical, so their general definitions and uniqueness are not new. Nagarajan et al. (2026) investigate attribution differences caused by contextual distractors; their full primary paper was not accessible for complete implication comparison, leaving a specific priority risk.

## Limitations
These formulas concern the stipulated one-exceptional-coalition additive game, not arbitrary contextual-distractor models or empirical machine-learning performance. The least-core convention allows signed efficient allocations, and results may differ under nonnegative-payment or individual-rationality constraints. This is a self-review, not independent certification. A related inaccessible primary paper may contain equivalent special-case formulas; unindexed literature also remains a risk. Computational tests cover finite instances only.

## References
Kera, H., Yamauchi, T., and Nagarajan, S. G. (2026). *Rethinking Least-Core Computation in Contextual-Distractor Games*. arXiv:2610.06087v1, publicly posted 5 October 2026. https://arxiv.org/html/2610.06087v1

Nagarajan, S. G., et al. (2026). *Seeing Through Distractions: Stable Attribution via the Core*. As cited by Kera et al. (2026), Sections 1–2; complete text not inspected.

Schmeidler, D. (1969). The nucleolus of a characteristic function game. *SIAM Journal on Applied Mathematics*, 17, 1163–1170.
