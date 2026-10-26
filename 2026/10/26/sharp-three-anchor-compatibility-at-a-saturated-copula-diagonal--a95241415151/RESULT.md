# Sharp three-anchor compatibility at a saturated copula diagonal

## Finding

Let \(C\) be a bivariate copula and let \(\Psi(C)=C^{T}*C\) be the Markov product of its transpose with itself. Write \(\delta_C(t)=\Psi(C)(t,t)\). For any \(0<a<b<c<1\), define

\[
 d=a+\frac{(b-a)^2}{1-a},\qquad
 L=a+\frac{(c-a)^2}{1-a},\qquad
 U=c-\frac{(b-a)(1-c)}{1-a}.
\]

**Sharp three-anchor theorem.** Among all bivariate copulas satisfying \(\delta_C(a)=a\) and \(\delta_C(b)=d\), the *exact* range of \(\delta_C(c)\) is

\[
 \boxed{L\le\delta_C(c)\le U.}
\]

Both endpoints and every intermediate value are attained by an explicitly constructible finite checkerboard input copula \(C\). The positive width is

\[
 U-L=\frac{(c-b)(1-c)}{1-a}>0.
\]

**Pairwise-versus-joint incompatibility.** In addition, whenever

\[
 \frac{b^2}{d}\le c<1,
\]

all three pairs of prescribed values \(\delta(a)=a\), \(\delta(b)=d\), \(\delta(c)=c\) are individually attainable within the range of \(\Psi\), but no single such copula attains the three values simultaneously. For instance, the targets

\[
 \delta(1/4)=1/4,\qquad \delta(1/2)=1/3,\qquad \delta(3/4)=3/4
\]

are pairwise realizable yet jointly impossible: the first two force \(7/12\le\delta(3/4)\le2/3\), with both bounds sharp. The mismatch to the proposed third value is \(1/12\).

## Assumptions and scope

A *copula* is the joint distribution function of random variables \(X,Y\), each uniform on \([0,1]\). All conditional probabilities below are understood as measurable versions, and every equality of conditional random variables holds almost surely. The Markov product convention is

\[
 \Psi(C)(u,v)=\int_0^1 \partial_1C(x,u)\,\partial_1C(x,v)\,dx.
\]

Here \(0<a<b<c<1\), with no other regularity assumptions on \(C\). All claims are for exact values at the specified thresholds; in particular the first constraint is the saturated value \(\delta(a)=a\), not an approximation. Checkerboard refers to a copula with a density constant on each cell of a finite rectangular partition.

## Proof

**1. Conditional second moments.** Take a pair \((X,Y)\) having copula \(C\), and put \(F_t=\Pr(Y\le t\mid X)\). Then \(0\le F_a\le F_b\le F_c\le1\), \(\mathbb EF_t=t\), and by the displayed definition

\[
 \delta_C(t)=\mathbb E[F_t^2].
\]

Since \(\delta_C(a)=a=\mathbb EF_a\), \(\mathbb E[F_a(1-F_a)]=0\) and hence \(F_a=\mathbf1_A\) for a measurable event \(A\) with \(\Pr(A)=a\). Nesting forces \(F_b=F_c=1\) on \(A\).

**2. Conditional rigidity at the second anchor.** On the complement \(A^c\), set \(B=F_b\). With

\[
 \alpha=\frac{b-a}{1-a},\qquad \gamma=\frac{c-a}{1-a},
\]

we have \(\mathbb E[B\mid A^c]=\alpha\) and

\[
 \mathbb E[B^2\mid A^c]=\frac{d-a}{1-a}=\alpha^2.
\]

Zero conditional variance forces \(B=\alpha\) almost surely on \(A^c\). Put \(T=F_c\) there. Then \(\alpha\le T\le1\), \(\mathbb E[T\mid A^c]=\gamma\), and

\[
 \delta_C(c)=a+(1-a)\mathbb E[T^2\mid A^c].
\]

Jensen's inequality yields \(\mathbb E[T^2\mid A^c]\ge\gamma^2\). The pointwise inequality \((T-\alpha)(1-T)\ge0\) yields \(T^2\le(1+\alpha)T-\alpha\), hence

\[
 \mathbb E[T^2\mid A^c]\le(1+\alpha)\gamma-\alpha.
\]

Multiplying these bounds by \(1-a\) and adding \(a\) gives exactly \(L\) and \(U\). The factorized width follows by elementary expansion. All statements include strict interior cutoffs and possible zero-density checkerboard cells.

**3. Sharpness and every intermediate value.** We specify finite *latent types*. A row \((w;f_a,f_b,f_c)\) means an event of probability \(w\) on which the three conditional distribution values are those constants. All row probabilities are nonnegative and sum to one. The lower-bound construction consists of

\[
 (a;1,1,1),\quad(1-a;0,\alpha,\gamma).
\]

Its second moments are \((a,d,L)\). The upper-bound construction consists of

\[
 (a;1,1,1),\quad
 \left(\frac{(1-a)(1-c)}{1-b};0,\alpha,\alpha\right),\quad
 \left(\frac{(1-a)(c-b)}{1-b};0,\alpha,1\right).
\]

Its second moments are \((a,d,U)\). To turn either list into an actual copula, split \([0,1]\) for the latent uniform \(X\) into consecutive intervals of row lengths. On the row of type \((f_a,f_b,f_c)\), let the conditional law of \(Y\) put masses

\[
 f_a,\quad f_b-f_a,\quad f_c-f_b,\quad1-f_c
\]

uniformly in the four bins \([0,a]\), \((a,b]\), \((b,c]\), \((c,1]\), respectively. The row averages at thresholds are exactly \(a,b,c\), so the total \(Y\) marginal is uniform; \(X\) is uniform by construction. Thus this is a genuine finite checkerboard copula. Splitting the latent variable among the lower and upper row constructions in any mixture proportion produces every value of \(\delta_C(c)\) between the endpoints while retaining the first two constraints.

**4. Pairwise attainability with joint obstruction.** First \(b^2/d>b\) and \(b^2/d<1\) because \(b^2<d<b\), as is seen from

\[
 d-b^2=\frac{a(1-b)^2}{1-a}>0,\qquad
 b-d=\frac{(b-a)(1-b)}{1-a}>0.
\]

The first two target values are attained by the lower-bound construction above. The pair \((a,c)\) is attained by latent rows of weights \(a,c-a,1-c\) and respective conditional values \((F_a,F_c)=(1,1),(0,1),(0,0)\). The pair \((b,c)\) is attained using the parameters \(r=b^2/d\), \(t=d/b\) and latent rows

\[
 (r;F_b=t,F_c=1),\quad
 (c-r;F_b=0,F_c=1),\quad
 (1-c;F_b=0,F_c=0).
\]

They give \(\mathbb EF_b=rt=b\), \(\mathbb EF_b^2=rt^2=d\), \(\mathbb EF_c=\mathbb EF_c^2=c\). All three pairwise witnesses are checkerboard realizable by the same four-bin (or two-threshold three-bin) construction. But any joint realization would satisfy \(\delta_C(c)\le U<c\), since \((b-a)(1-c)>0\). Contradiction. For the displayed rational triple, substitution gives \(d=1/3\), \(L=7/12\), \(U=2/3\); the condition \(3/4\ge (1/2)^2/(1/3)\) holds with equality.

## Verification

Run the standalone, standard-library-only Python program `verify.py` from the directory containing this document. It checks conditional-moment formulas and nonnegative ordered latent types exactly over randomized rational thresholds, both sharp endpoint constructions, interval mixtures, the rational pairwise-obstruction example, and a family of general pairwise witnesses. It additionally stress-tests a related conditional moment inequality. On the recorded run it printed `PASS: 1904 exact-rational construction, moment, interval and incompatibility checks`. These are finite reproducibility checks, not a substitute for the universal analytic proof above. Every program path used is local to this self-contained artifact package.

## Relationship to prior work

Drnovšek, Kokol Bukovšek, and Stopar (arXiv:2610.13846v1, first public 2026-10-09) establish pointwise optimal bounds for the diagonal of \(\Psi(C)\) when one anchor is prescribed; their Sections 5–6 include checkerboard sharpness constructions. Their concluding Section 7 states that taking maxima of single-anchor bounds does not settle two-or-more-anchor constraints. Our claim is restricted to the saturated first anchor and the exact minimizing value at a second anchor, where a conditional-variance argument makes a *simultaneous* sharp third-anchor interval accessible. The explicit continuum of pairwise-feasible but jointly impossible specifications is distinct from the single-anchor theory and from ordinary copula diagonal bounds, which do not enforce membership in the range of \(\Psi\).

Fuchs (arXiv:2112.10147; journal 2024) develops the dimension-reduction transformation and directed dependence measures. It supplies background for the map but not a three-anchor sharp compatibility interval in the inspected primary text. Existing completely positive matrix constraints and general copula diagonal admissibility remain relevant prior frameworks; no claim of a full classification of arbitrary multi-anchor data is made.

## Limitations

The exact interval theorem assumes the first diagonal value saturates its upper bound and the second equals the indicated minimal conditional second moment. It does not determine the full three-anchor feasible body for arbitrary prescribed values, nor four-or-more-anchor compatibility. The sharp upper interval is not a bound for the diagonal of every arbitrary copula, only for those in the range of \(\Psi\). Prior equivalents hidden in general multithreshold conditional moment or completely positive matrix literature remain a residual originality risk. Verification is analytic plus finite exact arithmetic; no independent scientific audit has been performed.

## References

1. R. Drnovšek, D. Kokol Bukovšek, and N. Stopar, *On diagonal sections of Markov products of copulas*, arXiv:2610.13846v1 (2026-10-09), https://arxiv.org/html/2610.13846v1. Especially Sections 5–7.
2. S. Fuchs, *Quantifying directed dependence via dimension reduction*, arXiv:2112.10147 (public preprint), *Journal of Multivariate Analysis* 201 (2024), Article 105266, https://arxiv.org/abs/2112.10147.
3. W. F. Darsow, B. Nguyen, and E. T. Olsen, *Copulas and Markov processes*, *Illinois Journal of Mathematics* 36 (1992), 600–642. Background reference for the Markov product; no full-text inspection is claimed here.
