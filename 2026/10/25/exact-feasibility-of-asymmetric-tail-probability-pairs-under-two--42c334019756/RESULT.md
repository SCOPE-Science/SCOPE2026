# Exact feasibility of asymmetric tail-probability pairs under two moments

## Finding

Fix real thresholds \(u,v>0\). Among all real random variables \(Z\) satisfying \(\mathbb E Z=0\) and \(\mathbb E Z^2=1\), this result characterizes exactly the attainable ordered pairs
\[
a=\Pr(Z\le -u),\qquad b=\Pr(Z\ge v).
\]
The middle event is the open interval \((-u,v)\), with mass \(c=1-a-b\). The strict inequalities below are essential: an atom at either endpoint belongs to a tail, not to the middle event.

Every feasible pair has \(a,b\ge0\) and \(a+b\le1\). Its remaining conditions are as follows.

1. **No tail mass.** If \(a=b=0\), feasibility holds exactly when \(uv>1\).

2. **No middle mass.** If \(c=0\), feasibility holds exactly when \(a,b>0\) and
   \[
   \max\left\{\frac{au^2}{b},\frac{bv^2}{a}\right\}\le1.
   \]

3. **Only the upper tail is occupied.** If \(c>0\), \(a=0<b\), feasibility holds exactly when
   \[
   b<\frac{u}{u+v},\qquad \frac{bv^2}{c}\le1.
   \]

4. **Only the lower tail is occupied.** If \(c>0\), \(b=0<a\), feasibility holds exactly when
   \[
   a<\frac{v}{u+v},\qquad \frac{au^2}{c}\le1.
   \]

5. **Both tails and the middle are occupied.** If \(a,b,c>0\), define \(m\) by
   \[
   m(a,b;u,v)=
   \begin{cases}
   au^2+bv^2+\dfrac{(au-bv)^2}{c},
       & a\le \dfrac{v}{u+v},\ b\le \dfrac{u}{u+v},\\
   \dfrac{(cu-bv)^2}{a}+bv^2+cu^2,
       & b>\dfrac{u}{u+v},\\
   au^2+\dfrac{(au-cv)^2}{b}+cv^2,
       & a>\dfrac{v}{u+v}.
   \end{cases}
   \]
   At most one of the last two cases can occur. Feasibility holds exactly when \(m<1\), or when \(m=1\) and both
   \[
   a<\frac{v}{u+v},\qquad b<\frac{u}{u+v}
   \]
   hold. Thus the equality case is excluded when the minimizing middle-group mean would sit at an endpoint.

This is a joint feasibility statement, not merely an upper bound on the sum \(a+b\).

## Assumptions and scope

Only the first two moments are fixed: the mean is zero and the second moment is one. No density, symmetry, unimodality, independence, or bounded-support assumption is imposed. Thresholds \(u\) and \(v\) are arbitrary positive real numbers. Probabilities are exact, not asymptotic. The events are \((-\infty,-u]\), \([v,\infty)\), and the strictly open interval \((-u,v)\).

## Proof

Write \(c=1-a-b\). When all three groups have positive mass, let \(x,z,y\) be their conditional means in the lower tail, middle interval, and upper tail, respectively. They satisfy
\[
x\le -u,\qquad -u<z<v,\qquad y\ge v,\qquad ax+cz+by=0.
\]
Conditional Jensen gives
\[
\mathbb E Z^2\ge ax^2+cz^2+by^2.
\]
Consequently the least possible second moment for the prescribed group masses is the infimum of this weighted quadratic expression under the displayed mean and interval constraints.

For \(a,b,c>0\), the minimizing lower and upper means begin at \(-u\) and \(v\). The mean constraint then requires \(z=(au-bv)/c\). This value lies in the closed middle interval precisely when \(a\le v/(u+v)\) and \(b\le u/(u+v)\), giving the first formula for \(m\). If \(b>u/(u+v)\), the middle mean is constrained at \(-u\), the upper mean is \(v\), and the lower mean must be \(x=(cu-bv)/a\); substitution gives the second formula. If \(a>v/(u+v)\), the middle mean is \(v\), the lower mean is \(-u\), and the upper mean is \(y=(au-cv)/b\); substitution gives the third formula. These cases exhaust the convex quadratic minimization. The infimum is attained by valid conditional means exactly when the middle mean is strictly inside \((-u,v)\); equality at either endpoint is not allowed in the middle group.

If \(c>0\) and only the upper tail has positive mass, the mean constraint and \(y\ge v\) require \(b<u/(u+v)\). Jensen gives the minimum \(bv^2/c\), attained by upper-tail value \(v\) and middle mean \(-bv/c\), which is strictly greater than \(-u\) exactly under that threshold condition. The lower-tail-only case is symmetric and yields \(au^2/c\) with \(a<v/(u+v)\).

If \(c=0\), both tails must have positive mass. Set the lower-tail mean to \(-t\); the mean constraint forces the upper-tail mean to \(at/b\). The constraints require \(t\ge\max\{u,bv/a\}\), so the least second moment is
\[
\frac{a}{b}\max\left\{u,\frac{bv}{a}\right\}^2
=\max\left\{\frac{au^2}{b},\frac{bv^2}{a}\right\}.
\]
This minimum is attained.

When at least one tail has positive mass, a minimum below one can be moved slightly into the open middle interval if necessary while keeping the second moment below one. One can then increase the conditional variance of a positive-mass tail group without changing that group’s probability or mean: a two-point distribution on the relevant half-line realizes any prescribed nonnegative conditional variance once its mean is strictly beyond the threshold. Choosing that variance to supply the remaining second moment produces \(\mathbb E Z^2=1\). If the minimum equals one, feasibility therefore requires the minimum to be attained, giving exactly the strict-boundary conditions above. Conversely, Jensen proves that a minimum above one is impossible, and a nonattained infimum equal to one cannot be reached.

Finally, if \(a=b=0\), then \(-u<Z<v\) almost surely and
\[
(Z+u)(v-Z)>0\quad\text{almost surely}.
\]
Taking expectations and using \(\mathbb E Z=0\) gives \(uv-\mathbb E Z^2>0\), so \(uv>1\) is necessary. If \(uv>1\), choose \(p\in(1/v,u)\) and set \(q=1/p\in(0,v)\). The two-point law supported at \(-p\) and \(q\), with probabilities \(q/(p+q)\) and \(p/(p+q)\), has mean zero, second moment \(pq=1\), and no mass in either tail. This proves sufficiency and completes the classification.

## Verification

The proof is analytic and covers all positive thresholds and all admissible probability pairs, including zero-mass and equality boundaries. The accompanying standard-library checker uses exact rational arithmetic to verify four explicit witnesses, all three positive-mass minimization regimes, the nonattained equality boundary, and eight representative boundary/feasibility predicates. Those finite checks are reproducibility aids, not a substitute for the proof. The equality-boundary distinction follows from the open middle interval and is explicitly included in the theorem.

## Relationship to prior work

Ion, Klaassen, and van den Heuvel give sharp bounds for the probability outside an asymmetric interval; their Theorem 2.2 bounds the scalar sum \(a+b\), with explicit extremizers. Their article does not state the full attainable set of ordered pairs \((a,b)\) or the strict feasibility boundary for a prescribed pair. Bertsimas and Popescu develop a general moment-optimization framework that can encode probability-bound problems, so a general optimization reduction is a genuine conceptual predecessor; the present statement supplies a closed-form univariate pair-feasibility classification. Ogasawara’s work on multiple Cantelli inequalities is relevant to multi-event probability bounds, but the accessible abstract does not establish this same univariate feasible-region formula. Search failure is not proof of priority.

## Limitations

The result is limited to one real random variable with fixed mean zero and second moment one and to two one-sided threshold events. It does not impose or characterize extra constraints such as integer support, symmetry, unimodality, higher moments, or a specified density. A general moment-optimization framework may recover equivalent statements by further specialization; exhaustive priority is not claimed. The full text of the multiple-Cantelli paper was not accessible in the inspected sources, so that comparison remains a documented residual risk. Independent review has not been performed.

## References

1. R. A. Ion, C. A. J. Klaassen, and E. R. van den Heuvel, “Sharp inequalities of Bienaymé–Chebyshev and Gauß type for possibly asymmetric intervals around the mean,” *TEST* 32 (2023), 566–601. DOI: 10.1007/s11749-022-00844-9. Published online 24 January 2023.
2. D. Bertsimas and I. Popescu, “Optimal inequalities in probability theory: A convex optimization approach,” *SIAM Journal on Optimization* 15 (2005), 780–804. DOI: 10.1137/S1052623401399903.
3. H. Ogasawara, “The multiple Cantelli inequalities,” *Statistical Methods & Applications* 28 (2019), 495–506. DOI: 10.1007/s10260-019-00452-2.
