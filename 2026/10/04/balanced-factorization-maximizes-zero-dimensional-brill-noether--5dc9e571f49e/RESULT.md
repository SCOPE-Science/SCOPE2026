# Balanced factorization maximizes zero-dimensional Brill–Noether counts
## Finding
Let \(C\) be a general smooth complex curve of genus \(g\ge 2\). For a numerical type \((r,D)\) with Brill–Noether number
\[
\rho(g,r,D)=g-(r+1)(g-D+r)=0,
\]
put \(a=r+1\) and \(b=g-D+r\). Then \(ab=g\), and the zero-dimensional Brill–Noether scheme is reduced and has
\[
N_g(a,b)=\#G^r_D(C)=g!\prod_{i=0}^{a-1}\frac{i!}{(b+i)!}.
\]
For factor pairs \(1\le a<c\le e<b\) with \(ab=ce=g\), one has the strict inequality
\[
N_g(a,b)<N_g(c,e).
\]
Thus, writing
\[
a_* = \max\{a:a\mid g,\ a\le \sqrt g\},\qquad b_*=g/a_*,
\]
the largest zero-dimensional Brill–Noether count at genus \(g\) is \(N_g(a_*,b_*)\). Up to Serre duality the maximizing numerical type is unique. Explicitly it is
\[
(r,D)=\bigl(a_*-1,(a_*-1)(b_*+1)\bigr),
\]
and, if \(a_*<b_*\), its distinct Serre-dual type is
\[
(r',D')=\bigl(b_*-1,(b_*-1)(a_*+1)\bigr).
\]
If \(g\) is a square these two numerical types coincide.

## Assumptions and scope
The curve is general in moduli over \(\mathbb C\), and \(g\ge2\). Only numerical types with \(\rho=0\) are compared. The statement compares the cardinalities of the reduced zero-dimensional varieties of linear series; it does not assert an ordering of positive-dimensional Brill–Noether loci or of pointed/ramified variants.

The substitution \(a=r+1\), \(b=g-D+r\) turns \(\rho=0\) into \(ab=g\), while
\[
D=(a-1)(b+1).
\]
Hence the available zero-dimensional numerical types are parametrized by the divisor pairs of \(g\). Transposition \((a,b)\leftrightarrow(b,a)\) is exactly the numerical action of Serre duality.

## Proof
Griffiths and Harris prove that for a general curve the expected Brill–Noether dimension is attained, with multiplicity one, and give the fundamental-class coefficient
\[
\lambda(g,r,D)=\prod_{i=0}^{r}\frac{i!}{(g-D+r+i)!}.
\]
When \(\rho=0\), integrating the zero-dimensional class gives
\[
\#G^r_D(C)=g!\lambda(g,r,D)
=g!\prod_{i=0}^{a-1}\frac{i!}{(b+i)!}.
\]
This is Castelnuovo's classical count. Farkas and Lian also identify it with the degree of the relevant Grassmannian.

The denominator is the hook product of an \(a\times b\) rectangle. Indeed, the multiset of rectangular hook lengths is the same as
\[
H_{a,b}=\{i+j-1:1\le i\le a,\ 1\le j\le b\},
\]
and therefore
\[
\prod_{h\in H_{a,b}}h
=\prod_{i=0}^{a-1}\frac{(b+i)!}{i!}.
\]
Thus \(N_g(a,b)=g!/\prod_{h\in H_{a,b}}h\).

It remains to prove the balancing lemma. Suppose \(1\le a<c\le e<b\) and \(ab=ce=g\). For an integer \(t\), let
\[
F_{a,b}(t)=\#\{h\in H_{a,b}:h\le t\}.
\]
For \(a\le b\), direct counting along diagonals gives
\[
F_{a,b}(t)=
\begin{cases}
0,&t\le0,\\
\frac{t(t+1)}2,&0\le t\le a,\\
at-\frac{a(a-1)}2,&a\le t\le b,\\
ab-\frac{(a+b-1-t)(a+b-t)}2,&b\le t\le a+b-1,\\
ab,&t\ge a+b-1.
\end{cases}
\]
We claim \(F_{c,e}(t)\ge F_{a,b}(t)\) for every \(t\), with strict inequality for some \(t\).

For \(t\le a\) the two functions agree. For \(a\le t\le c\),
\[
F_{c,e}(t)-F_{a,b}(t)=\frac{(t-a)(t-a+1)}2\ge0.
\]
For \(c\le t\le e\),
\[
F_{c,e}(t)-F_{a,b}(t)
=\frac{(c-a)(2t-a-c+1)}2>0.
\]
Now take \(e\le t\le\min\{b,c+e-1\}\), and write \(q=c+e-t\). The old and new upper-tail deficits are
\[
g-F_{a,b}(t)=a(b-t)+\frac{a(a-1)}2,
\qquad
g-F_{c,e}(t)=\frac{q(q-1)}2.
\]
Twice their difference is a concave quadratic in \(q\). At the endpoint \(q=c\) it equals
\[
(c-a)(2e-a-c+1)>0.
\]
At the other endpoint either \(q=1\), or \(t=b\) and \(q=c+e-b\le a\); the latter inequality is equivalent to \((c-a)(e-a)\ge0\). Hence the old deficit is at least the new deficit at both endpoints, and therefore throughout this interval.

Finally, for \(t\ge b\), either \(F_{c,e}(t)=g\), or both rectangles are in their upper tails. Since
\[
a+b-c-e=\frac{(c-a)(e-a)}a>0,
\]
the old tail parameter is larger, so its deficit is larger. This completes the cumulative comparison.

Cumulative dominance means that, after sorting the two hook multisets increasingly, each hook for the more balanced rectangle \(c\times e\) is at most the corresponding hook for \(a\times b\). The inequality is strict somewhere (already at \(t=a+1\)). Consequently
\[
\prod_{h\in H_{c,e}}h<\prod_{h\in H_{a,b}}h,
\]
and hence \(N_g(a,b)<N_g(c,e)\).

Among factor pairs with first factor at most \(\sqrt g\), repeated application of this strict balancing inequality shows that the maximum occurs at the divisor \(a_*\) closest to \(\sqrt g\) from below. Transposition preserves the rectangle hook product. Under \((a,b)\leftrightarrow(b,a)\), the corresponding degrees add to \(2g-2\), so the two maximizing numerical types are Serre dual; they coincide exactly when \(a_*=b_*\).

## Verification
A standalone exact-arithmetic checker, `artifacts/verify.py`, recomputes the Castelnuovo number from factorial products, independently computes the rectangular hook product, checks transposition symmetry and the Serre-dual degree relation, and verifies cumulative hook dominance for every pair of divisor rectangles for all genera \(2\le g\le300\). It reports `VERIFY_OK` after 299 genera and 1407 strict factor-pair comparisons. This finite regression test is not used as a proof of the theorem; the infinite statement is established by the symbolic cumulative-hook argument above.

## Relationship to prior work
Castelnuovo gave the classical finite count in 1889; a modern rigorous treatment is supplied by Griffiths and Harris. Farkas and Lian restate the same number as a Grassmannian degree, and Anderson--Chen--Tarasca recover the \(\rho=0\) Castelnuovo formula in a broader determinantal framework. These sources fix a single numerical type \((r,D)\) (or study richer incidence/ramification data). The inspected sources do not compare all \(\rho=0\) types at a fixed genus or identify the closest divisor of \(g\) as the extremizer.

The new content here is the strict balancing theorem across all divisor rectangles of fixed area \(g\), together with its Brill–Noether interpretation: the most numerous isolated linear-series problem is determined exactly by the factor of \(g\) nearest \(\sqrt g\), and the only numerical ambiguity is Serre duality.

## Limitations
The originality conclusion is bounded by the inspected literature and database searches. A combinatorial statement equivalent to the rectangular hook-product monotonicity may exist independently of Brill–Noether theory even if it was not located under the searched terminology. The geometric claim is only for general curves and \(\rho=0\); no assertion is made for special curves, positive-dimensional loci, or imposed ramification. The checker covers a finite range only and is included solely as regression evidence.

## References
1. G. Castelnuovo, *Numero delle involuzioni razionali giacenti sopra una curva di dato genere*, Rend. R. Accad. Naz. Lincei (4) 5 (1889), 130--133.
2. P. Griffiths and J. Harris, *On the variety of special linear systems on a general algebraic curve*, Duke Math. J. 47 (1980), 233--272. DOI: 10.1215/S0012-7094-80-04717-1.
3. G. Farkas and C. Lian, *Linear series on general curves with prescribed incidence conditions*, J. Inst. Math. Jussieu 22 (2023), 2857--2877. DOI: 10.1017/S1474748022000251.
4. D. Anderson, L. Chen, and N. Tarasca, *K-classes of Brill--Noether loci and a determinantal formula*, Int. Math. Res. Not. 2022 (2022), 12653--12698. DOI: 10.1093/imrn/rnab025.
