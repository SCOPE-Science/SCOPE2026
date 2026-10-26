# Joint image-rank census of commuting idempotents in the regressive transformation monoid

## Finding

For every integer \(n\geq 0\), let \(D_n\) be the monoid of all maps \(f:[n]\to[n]\) satisfying \(f(i)\leq i\) at every point. The empty map is included for \(n=0\). Define the polynomial
\[
P_n(u,v,w)=\sum_{\substack{e,f\in D_n\\e^2=e,\ f^2=f,\ ef=fe}}
u^{|\operatorname{im}e|}v^{|\operatorname{im}f|}w^{|\operatorname{im}(ef)|}.
\]
Here \(ef=e\circ f\), and exponents are nonnegative integers. Introduce polynomials \(H_s(u,v)\) for all \(s\geq1\) by \(H_1=1\) and
\[
H_{s+1}=\left(u+v+(1+u\partial_u)(1+v\partial_v)\right)H_s.
\]
Then the **complete three-rank exponential generating function** is
\[
\boxed{\sum_{n\geq0}P_n(u,v,w)\frac{z^n}{n!}
=\exp\left(wuv\sum_{s\geq1}H_s(u,v)\frac{z^s}{s!}\right).}
\]
In particular, if \(C_n=P_n(1,1,1)\), then \(C_0=1\) and
\[
C_n=\sum_{s=1}^n\binom{n-1}{s-1}H_s(1,1)C_{n-s}.
\]
The counts for \(n=1,\ldots,7\) are \(1,4,21,139,1114,10465,112513\). The number of ordered pairs whose common product has rank \(k\) is
\[
\frac{n!}{k!}[z^n]\left(\sum_{s\geq1}H_s(1,1)\frac{z^s}{s!}\right)^k
\quad(0\leq k\leq n).
\]
Thus the result determines all simultaneous image ranks, not merely the total number of idempotents.

## Assumptions and scope

All sets are finitely labeled by their natural chain order. No order-preservation assumption is made: only the regressive condition \(f(i)\leq i\). All pairs are ordered, and the maps are total. The result is an exact integer identity for every \(n\geq0\), independent of coefficient fields or probability models. Composition is the usual composition of maps. There is no asymptotic assertion.

## Proof

**1. Product fibers.** Let \(e,f\) be commuting idempotents in \(D_n\) and put \(g=ef=fe\). Then \(g\) is idempotent, \(eg=ge=g\), and \(fg=gf=g\). Consequently, \(e\) and \(f\) preserve every fiber of \(g\). Since \(g\) is regressive and idempotent, each fiber \(B\) has unique common fixed point \(c=g(B)=\min B\). Indeed, \(g(c)=c\), \(c\leq x\) for \(x\in B\), and \(c\in B\); also \(e(c)=f(c)=c\), since \(g(c)=c\) and both maps are regressive.

Conversely, every set partition of \([n]\), together with a commuting idempotent pair on each block whose common composition is the constant map to its minimum, yields a commuting idempotent pair on \([n]\). This correspondence is bijective. Only the relative chain order inside each block enters the count.

**2. Classification inside one block.** Write a block of size \(s\) as \(b_1<b_2<\cdots<b_s\), with \(c=b_1\). Let \(E\) be the nonroot points fixed by \(e\), and \(F\) those fixed by \(f\). They are disjoint: a point fixed by both would be fixed by \(g\), hence equal \(c\). For \(x\in E\), the identity \(f(e(x))=g(x)=c\) forces \(f(x)=c\); for \(x\in F\), similarly \(e(x)=c\). Any remaining point \(x\) is neither fixed by \(e\) nor by \(f\). Idempotency forces
\[
e(x)\in (E\cap[c,x))\cup\{c\},\qquad
f(x)\in (F\cap[c,x))\cup\{c\}.
\]
Every such choice is regressive. It is also sufficient: applying the other idempotent to either chosen image gives \(c\), while points of \(E\) and \(F\) have the specified images. Thus \(ef=fe\) equals the constant map to \(c\) on the block. These data therefore classify all block pairs without overcounting.

**3. Local rank polynomial.** Process \(b_2,b_3,\ldots,b_s\) in increasing order. After previous choices, suppose \(a\) nonroot points belong to \(E\), and \(b\) belong to \(F\). The next point can belong to \(E\) (weight \(u\)), belong to \(F\) (weight \(v\)), or belong to neither (\((a+1)(b+1)\) choices). The operator \((1+u\partial_u)(1+v\partial_v)\) multiplies each monomial \(u^a v^b\) by exactly \((a+1)(b+1)\). Starting at \(H_1=1\) proves the stated recurrence. In this fiber the ranks of \(e,f,g\) are \(1+|E|\), \(1+|F|\), and \(1\), respectively, so its three-rank weight is \(wuvH_s(u,v)\).

Equivalently the local polynomial admits the explicit finite sum
\[
H_s(u,v)=\sum_{\substack{E,F\subseteq\{2,\ldots,s\}\\E\cap F=\varnothing}}
u^{|E|}v^{|F|}
\prod_{\substack{2\leq j\leq s\\j\notin E\cup F}}
(1+|E\cap\{2,\ldots,j-1\}|)(1+|F\cap\{2,\ldots,j-1\}|).
\]
Empty sets and products have their usual meanings.

**4. Labeled-set assembly.** The product fibers form an arbitrary set partition of \([n]\); a fiber of size \(s\) receives the weight \(wuvH_s(u,v)\) independent of the actual labels, because they are read in increasing order. The exponential formula for weighted set partitions therefore gives the boxed identity. Marking the number of fibers by \(w\) yields the product-rank coefficient formula. Decomposing according to the fiber containing \(1\) gives the recurrence for \(C_n\). All steps are exact for every \(n\).

## Verification

The standalone program `verification.py` computes the local recurrence and the weighted-partition recurrence using exact integer coefficients. Independently, it enumerates every regressive map, filters idempotents by direct composition, and tests every ordered pair for commutation and its triple of image ranks. The two complete rank distributions coincide for \(1\leq n\leq7\). The exhaustive counts of idempotents are \(1,2,5,15,52,203,877\); commuting ordered-pair counts are \(1,4,21,139,1114,10465,112513\). The program also checks the fixed product-fiber count against the local polynomial for each tested \(n\). These finite checks are corroboration, not a replacement for the general bijective proof.

## Relationship to prior work

Zhao and Hu, *The monoid of all order-decreasing full transformations* (2024), examine maximal subsemigroups, maximal idempotent-generated subsemigroups, and abundance in precisely the monoid \(D_n\). The new claim instead determines the joint three-rank distribution of ordered commuting idempotents. Their full text was not accessible in this examination; this is an explicit priority risk, not evidence of absence.

Zhao and Hu, *On the monoid of all order-decreasing partial transformations* (2025), provide the minimum-of-kernel-block description of regressive idempotents and study maximal subsemigroups and abundance. Its inspected mathematical statements do not give a commuting-pair enumeration. Fernandes (2024) studies presentations and ranks of the smaller monoid of order-preserving regressive maps with interval images, not this unrestricted regressive commutation invariant.

Existing formulas for ordered commuting idempotents in the **full** transformation monoid, and for **order-preserving** commuting idempotents, are structurally related but do not supply this distribution: the regressive condition forces each idempotent kernel class to choose its *minimum* as image and introduces strict earlier-point restrictions in each product fiber. In the unrestricted full monoid those choices are label-symmetric; here the local differential recurrence is order-sensitive. This is a logical nonimplication claim about those cited formulas, not proof of exhaustive novelty.

## Limitations

The work covers only ordered commuting pairs of total regressive idempotents; it does not count arbitrary pairs, larger commuting families, partial transformations, or conjugacy classes. The generating function is formal and provides no asymptotic estimates. No literature search proves publication priority; the closest full-transformation and monotone results, and a directly relevant inaccessible 2024 paper, remain genuine originality considerations.

## References

1. P. Zhao and H. Hu, *The monoid of all order-decreasing full transformations*, Communications in Algebra 52 (2024), 4834–4843, DOI: 10.1080/00927872.2024.2359052; first public online date 2024-06-21.
2. P. Zhao and H. Hu, *On the monoid of all order-decreasing partial transformations*, Filomat 39 (2025), 1149–1162, DOI: 10.2298/FIL2504149Z; publicly available complete text at https://www.pmf.ni.ac.rs/filomat-content/2025/39-4/39-4-6-25122.pdf.
3. V. H. Fernandes, *On the monoid of order-preserving transformations of a finite chain whose ranges are intervals*, Semigroup Forum 109 (2024), 336–346, DOI: 10.1007/s00233-024-10466-2; full open-access article https://link.springer.com/article/10.1007/s00233-024-10466-2.
4. A. Dağdeviren and G. Ayık, *Combinatorial results for semigroups of orientation-preserving transformations*, Turkish Journal of Mathematics 48 (2024), 106–117, DOI: 10.55730/1300-0098.3496; abstract publicly available https://journals.tubitak.gov.tr/math/vol48/iss2/2/.
