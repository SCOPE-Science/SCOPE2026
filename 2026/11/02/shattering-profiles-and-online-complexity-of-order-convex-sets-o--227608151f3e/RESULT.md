# Shattering profiles and online complexity of order-convex sets on two-row posets

## Finding

For each integer \(n\ge1\), let \(P_n=\{0,1\}\times\{1,\ldots,n\}\), with coordinatewise partial order, and let \(\mathcal C_n\) comprise **all** order-convex subsets, including the empty set and the entire poset. A hypothesis is the incidence vector of a member of \(\mathcal C_n\), and a query asks membership of one specified element of \(P_n\).

The exact number of hypotheses is
\[
N_n=|\mathcal C_n|=\frac{n^4+4n^3+17n^2+14n+12}{12}.
\]
A support is VC-shattered if and only if it contains **no three-element strict chain**. Consequently the complete shattered-support polynomial, valid for every \(n\ge1\), is
\[
\boxed{\Phi_n(z)=1+2nz+\binom{2n}{2}z^2
 +\frac12\binom{2n}{3}z^3
 +\frac{n(n-1)^2(n-2)}{12}z^4.}
\]
In particular,
\[
\operatorname{VCdim}(\mathcal C_n)=
\begin{cases}2,&n=1,\\3,&n=2,\\4,&n\ge3.\end{cases}
\]

There is nevertheless unbounded adaptive complexity. Put \(p=\lfloor n/2\rfloor\), \(q=\lceil n/2\rceil\), and, for \(m\ge1\), define
\[
\lambda(m)=\left\lfloor\log_2\left\lceil\frac m2\right\rceil\right\rfloor
 +\left\lfloor\log_2\left(\left\lfloor\frac m2\right\rfloor+1\right)\right\rfloor,
\qquad\lambda(0)=0.
\]
Then for all \(n\ge1\),
\[
\boxed{\lambda(p)+\lambda(q)\le \operatorname{Ldim}(\mathcal C_n)
\le\left\lfloor\log_2 N_n\right\rfloor.}
\]
In particular, the leading logarithmic coefficient is exact:
\[
\operatorname{Ldim}(\mathcal C_n)=4\log_2 n+O(1)
\quad(n\to\infty).
\]

Exact finite values, calculated by the exhaustive version-space recurrence below, are:

| \(n\) | \(N_n\) | \(\operatorname{VCdim}\) | \(\operatorname{Ldim}\) | \(\lfloor\log_2 N_n\rfloor\) |
|---:|---:|---:|---:|---:|
| 1 | 4 | 2 | 2 | 2 |
| 2 | 13 | 3 | 3 | 3 |
| 3 | 33 | 4 | 4 | 5 |
| 4 | 71 | 4 | 5 | 6 |
| 5 | 136 | 4 | 6 | 7 |
| 6 | 239 | 4 | 7 | 7 |
| 7 | 393 | 4 | 8 | 8 |
| 8 | 613 | 4 | 8 | 9 |
| 9 | 916 | 4 | 9 | 9 |
| 10 | 1321 | 4 | 9 | 10 |

Attainment of the hypothesis-count bound is therefore nonmonotone within this natural family: the bound fails for \(n=3,4,5\), holds for \(n=6,7\), fails for \(n=8\), holds for \(n=9\), and fails for \(n=10\).

## Assumptions and scope

Coordinatewise order means \((a,i)\le(b,j)\) exactly when \(a\le b\) and \(i\le j\). A set \(C\) is order-convex if \(x,z\in C\) and \(x\le y\le z\) imply \(y\in C\). No connectedness, nonemptiness, or fixed-cardinality constraint is imposed. The VC domain consists of the \(2n\) elements of this poset; the adaptive dimension is the classical binary Littlestone dimension of the same incidence-vector concept family. A complete adaptive mistake tree of depth \(d\) has every binary answer sequence of length \(d\) realizable by a hypothesis.

## Proof

**1. Canonical ideal differences and their count.** For any nonempty convex set \(C\), its down-closure \(J=\downarrow C\) is an ideal and \(I=J\setminus C\) is also an ideal: if \(y\in I\), \(x\le y\), and \(x\in C\), some \(z\in C\) satisfies \(y\le z\); then \(x\le y\le z\) contradicts convexity. Hence \(C=J\setminus I\). Conversely, a difference of nested ideals is convex. Canonicality of \(J\) is equivalent to requiring every maximal element of \(J\) to lie in \(C\), or equivalently \(I\subseteq J\setminus\operatorname{Max}(J)\). Thus \(C\mapsto(J,I)\) is a bijection between nonempty convex sets and pairs where \(J\) is a nonempty ideal and \(I\) is an ideal of \(J\setminus\operatorname{Max}(J)\).

Every ideal \(J\) of \(P_n\) has unique row-prefix lengths \((p,q)\) with \(0\le q\le p\le n\). The number of eligible \(I\) is \(p\) if \(q=0<p\); it is \(q(p-(q-1)/2)\) if \(0<q<p\); and it is \(p(p+3)/2\) if \(q=p>0\). Adding the single empty set gives
\[
1+\sum_{p=1}^n p+\sum_{p=1}^n\frac{p(p+3)}2
+\sum_{p=2}^n\sum_{q=1}^{p-1}q\left(p-\frac{q-1}{2}\right)
=\frac{n^4+4n^3+17n^2+14n+12}{12}.
\]
This counts distinct convex sets, not presentations by arbitrary ideal pairs.

**2. Shattering criterion for any poset.** The order-convex hull of a subset \(A\) is precisely \(\uparrow A\cap\downarrow A\): the latter is convex and is the smallest convex set containing \(A\). If a support \(S\) contains \(x<y<z\), the required trace selecting \(x,z\) but excluding \(y\) is impossible. Conversely, when \(S\) has no three-element chain, for each trace \(A\subseteq S\), every point in \(S\cap(\uparrow A\cap\downarrow A)\) belongs to \(A\); otherwise two selected elements would surround an unselected element in a strict chain. Therefore every trace is realized by its convex hull.

**3. Counting shattered supports.** Every support of size at most two is shattered. A three-point support is excluded exactly when it is a strict three-chain. Three-chains lying in one row contribute \(2\binom n3\); the two mixed row-patterns contribute \(2\binom{n+1}3\). Their sum is \(\tfrac12\binom{2n}3\), leaving exactly the same number of shattered triples.

A shattered four-element support must select two points \(1\le i<j\le n\) from the bottom row and two \(1\le k<\ell\le n\) from the top row, since each row is a chain. Such a support avoids all strict three-chains exactly when \(k<i\) **and** \(\ell<j\). Summing first over the two bottom coordinates gives
\[
\sum_{1\le i<j\le n}\ \sum_{k=1}^{i-1}\ \sum_{\ell=k+1}^{j-1}1
=\frac{n(n-1)^2(n-2)}{12}.
\]
No support of size five can be shattered: it would contain at least three points in one of the two row chains. Supports of size four exist exactly when \(n\ge3\). This proves the polynomial and VC dimension.

**4. Online lower bound and asymptotic.** Split the columns at \(p\). The bottom-row right strip \(\{(0,j):p<j\le n\}\) and top-row left strip \(\{(1,j):1\le j\le p\}\) are mutually incomparable. Independently choose a consecutive interval in each strip, allowing empty intervals. Their union is order-convex because there are no comparable cross-strip pairs. For a chain of length \(m\), restrict to intervals containing a central position \(c=\lceil m/2\rceil\). The left endpoint has \(c\) choices, and the right endpoint has \(m-c+1\) choices; membership queries on opposite sides of the center identify these two parameters by independent binary threshold trees of depths \(\lfloor\log_2 c\rfloor\) and \(\lfloor\log_2(m-c+1)\rfloor\). Querying the four endpoint parameters successively constructs a complete tree of depth \(\lambda(p)+\lambda(q)\), proving the stated lower bound. For \(p=0\), omit the empty strip.

Every complete adaptive tree of depth \(d\) needs at least \(2^d\) distinct hypotheses, giving the upper bound. The lower bound is \(4\log_2 n-O(1)\), while the upper bound is \(4\log_2 n+O(1)\) by the exact cardinality formula. Together they prove the claimed sharp leading term.

**5. Exact finite adaptive ranks.** For a nonempty version space \(V\subseteq\mathcal C_n\), write \(V_x^a=\{C\in V:\mathbf1[x\in C]=a\}\). The full exact recurrence is
\[
R(V)=\begin{cases}
0,&|V|\le1,\\
\max\limits_{x:\,V_x^0,V_x^1\ne\varnothing}
 \bigl(1+\min\{R(V_x^0),R(V_x^1)\}\bigr),&\text{otherwise},
\end{cases}
\]
with an empty maximum interpreted as zero. The recurrence exhausts every possible first query and both answers. `lattice_verify.py` enumerates all convex sets via nested ideal differences, uses exact arbitrary-precision bitsets and memoizes every version space reached; it reproduces all ten displayed ranks without sampling or search timeouts. `certificates.json` contains explicit complete lower-bound query trees for the final four parameters; `structural_verify.py` separately checks all certificate leaves and all support traces through the eighth parameter. The rank recurrence proves finite upper bounds, while the certificates witness finite lower bounds.

## Verification

With Python 3 and all supplied files in one directory, run `python lattice_verify.py` and then `python structural_verify.py`. The first program recomputes every displayed finite rank and the hypothesis counts, independently enumerates all convex sets from order-betweenness triples through the eighth parameter, and regenerates the complete lower-bound certificates. The second program separately enumerates convex subsets via order triples, independently validates the full polynomial by enumerating supports and checking actual incidence traces through the eighth parameter, and checks every node and terminal hypothesis of the stored lower-bound certificates. Neither program uses floating-point values to decide any reported exact dimension or count.

## Relationship to prior work

Seiffarth, Horváth and Wrobel study closed-set and halfspace separation in finite closure systems, including lattice-related cases; their investigation motivates examining concrete closure families but does not establish the order-convex two-row shattering polynomial or adaptive ranks. Stadtländer, Horváth and Wrobel study learning weakly convex concepts in metric spaces rather than the order-convex subsets of a finite product poset. Thiessen and Gärtner study online learning of geodesically convex sets on graphs, a distinct betweenness relation. The general theory of order ideals and the two-family theorem in poset combinatorics provide useful context; an order ideal is a restricted special case of an order-convex set and its learning dimensions do not determine those of all order-convex subsets.

## Limitations

The exact Littlestone-dimension classification is asserted only through \(n=10\). For larger parameters the proved upper and lower bounds have matching leading coefficient but leave a bounded additive gap; no exact all-parameter formula is claimed. The finite results rely on exhaustive, reproducible evaluation of the stated recurrence, not a symbolic closed form. The full historical priority of the formulas, especially under the terminology of convex subsets, differences of ideals and order intervals, remains uncertain.

## References

1. F. Seiffarth, T. Horváth and S. Wrobel, *Maximal Closed Set and Half-Space Separations in Finite Closure Systems*, ECML PKDD 2019, LNCS 11906, pp. 21–37; expanded version arXiv:2001.04417 (first public conference presentation verified 2019-09-19), https://arxiv.org/abs/2001.04417.
2. E. Stadtländer, T. Horváth and S. Wrobel, *Learning Weakly Convex Sets in Metric Spaces*, arXiv:2105.06251 (first public preprint 2021-05-10), https://arxiv.org/abs/2105.06251.
3. M. Thiessen and T. Gärtner, *Online Learning of Convex Sets on Graphs*, ECML PKDD 2022, pp. 349–364, doi:10.1007/978-3-031-26412-2_22, https://mlanthology.org/ecmlpkdd/2022/thiessen2022ecmlpkdd-online/.
