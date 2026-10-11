# A four-to-four contact transition in radial mean bodies of the square

## Finding
Let \(Q=[-1,1]^2\). For every real parameter \(p>-1\), write \(R_pQ\) for its radial \(p\)-mean body (under the standard Gardner--Zhang convention). If \(u=(u_1,u_2)\in S^1\), set
\[
q(u)=\frac{\min\{|u_1|,|u_2|\}}{\max\{|u_1|,|u_2|\}}\in[0,1].
\]
The complete directional radial profile is
\[
\rho_p(u)=
\begin{cases}
2\sqrt{1+q^2}\left(\frac{p+2-pq}{(p+1)(p+2)}\right)^{1/p},&p\ne0,\\
2\sqrt{1+q^2}\,e^{-1-q/2},&p=0,
\end{cases}
\qquad q=q(u).
\]
The *only* directions of maximal Euclidean radius are the coordinate axes for \(-1<p<2\), the diagonals for \(p>2\), and both the axes and diagonals for \(p=2\). Thus precisely eight directions maximize at the sharp parameter \(p=2\); there are four at every other parameter. The *only* minimizing directions are the diagonals for \(-1<p\le0\), or the eight unit directions with \(q=1/(p+1)\) for \(p>0\). This yields complete Euclidean inradius and circumradius classifications throughout the newly available negative-parameter regime as well as all nonnegative parameters.

More explicitly, set
\[
A_p=2(p+1)^{-1/p},\quad
D_p=2\sqrt2\left(\frac{2}{(p+1)(p+2)}\right)^{1/p}
\]
for \(p\ne0\), with continuous limits \(A_0=2/e\) and \(D_0=2\sqrt2/e^{3/2}\). For \(p>0\), set \(M_p=\rho_p(u)\) at \(q(u)=1/(p+1)\). Then the sharp enclosing and contained Euclidean radii are, respectively, \((A_p,D_p)\) for \(-1<p\le0\), \((A_p,M_p)\) for \(0<p<2\), \((A_2,M_2)=(D_2,M_2)\) for \(p=2\), and \((D_p,M_p)\) for \(p>2\). At \(p=2\),
\[
\operatorname{rad}_{\rm out}(R_2Q)=\frac{2}{\sqrt3},\qquad
\operatorname{rad}_{\rm in}(R_2Q)=\frac{10}{9}.
\]
The axial-to-diagonal crossing is transverse:
\[
\log\frac{D_p}{A_p}=\frac{\log2-1/2}{4}(p-2)+O\bigl((p-2)^2\bigr).
\]

## Assumptions and scope
This is a complete exact Euclidean directional-radius theorem for the **fixed square** \(Q\), with \(p\in(-1,\infty)\). The ambient norm used for inradius and circumradius is the ordinary Euclidean norm (not an affine-invariant norm). The radial \(p\)-mean body definition and the negative-parameter normalization agree with Proposition 10 of Langharst, arXiv:2603.14134v4. At \(p=0\) all expressions mean continuous limits, not division by zero. The center is the origin, automatically the common center of all bodies by their fourfold symmetry.

## Proof
**1. Exact square covariogram.** The covariogram \(g_Q(x)=|Q\cap(Q+x)|\) satisfies
\[
\frac{g_Q(x)}{|Q|}=\prod_{i=1}^2\left(1-\frac{|x_i|}{2}\right)_+.
\]
By reflecting and permuting coordinates, we may assume \(u=(a,b)\) with \(a\ge b\ge0\), \(a^2+b^2=1\), and put \(q=b/a\). For \(t\ge0\), writing \(T=2/a=2\sqrt{1+q^2}\), the normalized covariogram on the ray \(tu\) is \((1-t/T)(1-qt/T)\) for \(0\le t\le T\), and zero afterward.

**2. Unified negative and positive moments.** The derivative measure \(d(-g_Q(tu)/|Q|)\) has density \(((1+q)-2qt/T)\,dt/T\) on \([0,T]\), no atom at the endpoint, and total mass one. For every real \(p>-1\), \(p\ne0\), the one-dimensional formula for the radial mean body (the integration-by-parts form of Proposition 10 in the cited source) is
\[
\rho_p(u)^p=\int_0^\infty t^p\,d\left(-\frac{g_Q(tu)}{|Q|}\right)
=T^p\left(\frac{1+q}{p+1}-\frac{2q}{p+2}\right)
=T^p\frac{p+2-pq}{(p+1)(p+2)}.
\]
The integral converges even for \(-1<p<0\), because its density is bounded at the origin. Raising to the power \(1/p\) gives the stated profile. Passing to \(p=0\) in the logarithm yields \(\rho_0(u)=T\exp(-1-q/2)\). Thus the formula holds on the *entire* parameter interval.

**3. Exhaustive critical directions.** For every \(p>-1\), including \(p=0\) by continuity, the derivative in the reduced angle ratio is
\[
\frac{d}{dq}\log\rho_p(q)=\frac{q}{1+q^2}-\frac{1}{p+2-pq}
=-\frac{(q-1)((p+1)q-1)}{(1+q^2)(p+2-pq)}.
\]
The denominator is strictly positive for \(0\le q\le1\) and \(p>-1\). For \(-1<p\le0\), the derivative is strictly negative on \([0,1)\), so axes uniquely maximize and diagonals uniquely minimize. For \(p>0\) the derivative is negative before \(q_*=(p+1)^-1\) and positive after, so the unique reduced minimum is \(q_*\), while all reduced global maxima lie at \(q=0\) or \(q=1\). Each interior \(q_*\) represents exactly eight unit directions; each endpoint represents exactly four.

**4. Sharp endpoint comparison.** Comparing the exact axial and diagonal values gives
\[
\log\frac{D_p}{A_p}=\frac{\log2}{2}-\frac{\log(1+p/2)}{p},
\]
with the continuous value at \(p=0\). The function \(p\mapsto\log(1+p/2)/p\) is strictly decreasing on \((-1,\infty)\): its derivative has numerator \(p/(p+2)-\log(1+p/2)<0\) for \(p\ne0\), by the strict log inequality \(\log y>1-1/y\) for \(y\ne1\). The endpoint values therefore cross exactly once, at \(p=2\), where \(\log(1+2/2)/2=(\log2)/2\). This proves all maximizer classes, including the eightfold equality at the transition. Direct substitution at \(p=2\), \(q=0,1,1/3\) yields the displayed sharp Euclidean radii. Differentiating the endpoint logarithmic ratio at \(p=2\) gives \((\log2-1/2)/4>0\) and proves transversality.

## Verification
The proof uses exact elementary identities and inequalities, not a finite exhaustive search. A standalone standard-library program `verify.py` checks the exact moment identity for rational parameters, the factorization of the critical equation, the sharp \(p=2\) values, and samples the predicted extremum pattern across the negative and positive parameter regimes. Execute `python3 verify.py` in the same directory. The program's finite sampling is a consistency check; the uniform-for-all-parameters assertions are established by the displayed derivative sign and log inequality.

## Relationship to prior work
Gardner and Zhang introduced the radial mean body interpolation between the polar projection body and the difference body. Langharst (2026), Theorem 3, proves convexity for the full interval \(p>-1\), settling the previously open negative-parameter case; Proposition 10 gives the general covariogram-moment representation used in the first step of this proof. Neither that general representation nor the general convexity/inclusion theorems determines the square's exact Euclidean maximizer/minimizer directions or its unique axis-to-diagonal transition without a separate angular extremization. The 2014 dual-quermassintegral inequalities of Wang and Zhang address integrals and inclusion inequalities, not this sharp pointwise angular contact classification. The formula is a transparent application of the known moment framework; the additional finding is the complete sharp angular phase diagram and exhaustive equality classes, not a new convexity theorem.

## Limitations
The result concerns only the canonical square and Euclidean radial extremes, and does not establish a universal phase transition for other convex bodies, a global isoperimetric inequality, or an optimal affine-invariant eccentricity. Earlier publications may contain an unindexed explicit square computation; while targeted searches located no covering result, absolute historical novelty is not certified. The value here lies in the complete parameter-and-direction classification of a canonical operator benchmark, including the negative \(p\)-range and the nontrivial interior-minimum regime.

## References
1. D. Langharst, *Convexity of Radial Mean Bodies via an Extension of Ball's Bodies*, arXiv:2603.14134v4 (2026), especially Theorem 3 and Proposition 10, https://arxiv.org/pdf/2603.14134.
2. R. J. Gardner and G. Zhang, *Affine inequalities and radial mean bodies*, Amer. J. Math. **120** (1998), 505–528, https://doi.org/10.1353/ajm.1998.0021.
3. W. Wang and T. Zhang, *Inequalities for dual quermassintegrals of the radial p-th mean bodies*, J. Inequal. Appl. **2014**, 252, https://doi.org/10.1186/1029-242X-2014-252.
