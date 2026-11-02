# Sharp quadratic distance moment for three-path metric networks

## Finding
Let a compact theta metric graph consist of three internally disjoint paths of positive lengths \(0<a\le b\le c\), joining the same two vertices, with the intrinsic shortest-path metric. Let \(P,Q\) be independent uniform-arclength points, let \(D=d(P,Q)\), and put \(L=a+b+c\). Then
\[
\mathbb E[D^2]=\frac{T(a,b,c)}{12L^2},
\]
where
\[
\begin{aligned}
T(a,b,c)={}&3a^4+2a^3b+2a^3c+3a^2b^2+3a^2c^2\\
&+4ab^3+6ab^2c+6abc^2+4ac^3\\
&+b^4+2b^3c+3b^2c^2+2bc^3+c^4.
\end{aligned}
\]
The sharp fixed-total-length inequalities are
\[
\boxed{\frac{7}{162}L^2\le \mathbb E[D^2]<\frac{L^2}{12}}.
\]
Equality on the left holds exactly when all three paths have length \(L/3\). The right constant is a sharp, unattained supremum, approached when two path lengths tend to zero and the third tends to \(L\). This is an intrinsic, continuous second-distance-moment theorem, not a statement about Euclidean embedding, uniformly sampled vertices, or the first distance moment.

## Assumptions and scope
Each path is a copy of a real interval with its ordinary length, with its two endpoints identified with the same two network junctions. The network metric is the infimum of lengths of connecting paths; probability is the normalized one-dimensional Hausdorff measure on its three edges, so sampling an edge has probability proportional to its physical length. All path lengths are **strictly positive**; the extreme degenerate network appears only as a limit. Relabeling paths makes \(0<a\le b\le c\) unambiguous. Put \(K=L^2\mathbb E[D^2]\), the unnormalized double integral of squared distance.

## Proof
**1. Distances on a single arm.** For points at coordinates \(x,y\in[0,u]\) on the same arm, the alternative route between their junctions uses the shortest other arm, of length \(h\). Thus, with \(t=|x-y|\),
\[
d(x,y)=\min\{t,u+h-t\}.
\]
Since ordered pairs with separation in \((t,t+dt)\) occupy area \(2(u-t)dt\), integration yields
\[
I(u;h):=\int_0^u\!\int_0^u d(x,y)^2\,dx\,dy=
\begin{cases}
u^4/6,&h\ge u,\\[2pt]
(u^4+2hu^3-2h^3u+h^4)/12,&h<u.
\end{cases}
\]

**2. Distances between different arms.** Let the two sampled arms have lengths \(p\ge q\), and let the third arm have length \(h\). With coordinates \(x\in[0,p]\), \(y\in[0,q]\), an exhaustive list of shortest path types gives
\[
d(x,y)=\min\{x+y,\ p+q-x-y,\ x+h+q-y,\ p-x+h+y\}.
\]
If the third arm is not shorter than the shorter sampled arm (\(h\ge q\)), its shortcuts are never advantageous. Integrating the first two branches gives
\[
J_0(p,q)=\int_0^p\!\int_0^q\min(x+y,p+q-x-y)^2\,dy\,dx
=\frac{q(p^3+3p^2q+3pq^2-q^3)}{12}.
\]
If \(h<q\), the omitted shortcuts improve the distance in two opposite-sign triangular regions after centering \(X=x-p/2\), \(Y=y-q/2\). On these regions the improvement in distance is \((2\min\{|X|,|Y|\}-h)_+\). Direct integration of the difference of squares over the two triangles produces
\[
J(p,q;h)=J_0(p,q)-\frac{(q-h)^2}{24}
\bigl(3p^2+4pq-2q^2+2hp-4hq-3h^2\bigr).
\]
For \(h\ge q\), put \(J(p,q;h)=J_0(p,q)\). The formulas agree at \(h=q\). These are integrations over the original distance, not an assumed independence of route lengths.

**3. Combine the six integration regions.** Under \(a\le b\le c\), the same-arm contributions are \(I(a;b)\), \(I(b;a)\), \(I(c;a)\); the three different-arm regions (each in two possible orders) contribute \(2J(b,a;c)\), \(2J(c,a;b)\), \(2J(c,b;a)\). Therefore
\[
K=I(a;b)+I(b;a)+I(c;a)
+2\bigl(J(b,a;c)+J(c,a;b)+J(c,b;a)\bigr).
\]
Substitution, multiplication, and collection of monomials give the polynomial \(T/12\) displayed in the finding. This identity is exact even when the longest arm exceeds the sum of the other two.

**4. Exact lower and upper certificates.** Put \(x=a>0\), \(y=b-a\ge0\), \(z=c-b\ge0\). Then \(L=3x+2y+z\). Direct expansion yields the two **nonnegative coefficient identities**
\[
\begin{aligned}
324\Bigl(K-\frac7{162}L^4\Bigr)={}&
216x^2y^2+216x^2yz+216x^2z^2+168xy^3\\
&+252xy^2z+288xyz^2+102xz^3+19y^4\\
&+38y^3z+69y^2z^2+50yz^3+13z^4,
\end{aligned}
\]
\[
\begin{aligned}
12\Bigl(\frac{L^4}{12}-K\Bigr)={}&
39x^4+104x^3y+52x^3z+96x^2y^2\\
&+96x^2yz+18x^2z^2+40xy^3+60xy^2z\\
&+24xyz^2+2xz^3+7y^4+14y^3z+9y^2z^2+2yz^3.
\end{aligned}
\]
Every term is nonnegative. Since \(x>0\), the upper gap is strictly positive. The lower gap vanishes precisely when \(y=z=0\), i.e., the equilateral theta graph. For \(a=b=\varepsilon\), \(c=L-2\varepsilon\), these identities show \(K\to L^4/12\) as \(\varepsilon\downarrow0\), proving sharpness of the upper constant. The limiting circle has \(\mathbb E D^2=L^2/12\), in agreement with this limit.

**5. No underlying stochastic dominance.** Let \(F(t)=\Pr(D\le t)\). At fixed \(L\), for the equilateral theta graph, exact short-route triangle areas give \(F_{\mathrm{eq}}(t)=2t/L+3t^2/L^2\) for \(0<t<L/3\). As \(a\downarrow0\) with \(b=c=(L-a)/2\), the limiting graph is a wedge of two circles of circumference \(L/2\), with \(F_{\mathrm{wedge}}(t)=2t/L+4t^2/L^2\) for \(0<t<L/4\). At \(t=L/5\) the latter exceeds the former by \(1/25\). Distances, normalized arclength measures and their threshold probabilities vary continuously under this edge-length limit (the relevant level sets have zero product-arclength measure); hence some strictly positive unequal theta graphs have more short-distance pairs than the equilateral graph, despite their larger second moments. The moment bound is therefore not a trivial pointwise stochastic order consequence.

## Verification
Run `python3 verify_second.py` with a Python 3 standard-library interpreter. The shipped verifier checks 1,064 deterministic identities and numerical cases, including the exact gap certificates on hundreds of rational triples, independently integrating the original four-branch shortest-path formula over sampled pair coordinates, and comparing the exact limiting short-distance CDF coefficients. The execution returned `VERIFY_OK 1064 exact rational identities, independent double quadratures, and CDF-limit comparison`. These finite checks corroborate the proof; the theorem follows from the integrations and coefficient identities, not from sampling or test coverage.

## Relationship to prior work
Doyle and Graver's 1982 *Mean distance for shapes* and its summary study the **first moment** of travel distance on shape networks; their publisher material was examined but the complete 1982 journal article was inaccessible. Garijo–Márquez–Silveira's 2021 preprint (later journal article) computes continuous **mean distance** on weighted graphs; Baptista–Kennedy–Mugnolo's 2023 preprint also proves general **first-moment** inequalities for metric graphs, including the upper-loop extremizer. The Hosoya/hyper-Wiener graph-index literature motivates **squared distances** but works with discrete vertex metrics. The first-moment theta formula and its sharp minimizer are previously established and explicitly excluded here. The result above concerns the different quadratic arclength-pair statistic, its exact shape formula, sharp constants and the obstruction to stochastic ordering. Historical originality is provisional; no priority assertion is made beyond the actual comparisons reported separately.

## Limitations
The sharp constants are proved only for **three-arm** metric theta networks with strictly positive lengths; they are not claimed for four or more parallel arms, general compact metric graphs, or Euclidean straight-line distances. The upper value is a supremum, not a maximizer among such theta networks. Numerical computations do not independently certify the infinite family; an independent audit has not been performed. Full-text inspection of Doyle–Graver (1982) was not possible, so an earlier implicit or explicit quadratic version remains a priority risk. Historical source-date metadata records the first citation with an exact publicly verified day, not the date of the earliest historical publication.

## References
1. J. K. Doyle and J. E. Graver, *Mean distance for shapes*, Journal of Graph Theory 6 (1982), 453–471, DOI `10.1002/jgt.3190060410` (publisher bibliographic page, full text inaccessible).
2. J. K. Doyle and J. E. Graver, *A Summary of Results on Mean Distance in Shapes*, Environment and Planning B 9 (June 1982), 177–179, DOI `10.1068/b090177` (abstract and bibliography inspected).
3. E. Deutsch and S. Klavžar, *Computing Hosoya polynomials of graphs from primary subgraphs*, arXiv:`1212.3179`, first submitted 2012-12-13 (discrete squared-distance background, not a theta metric-graph theorem).
4. D. Garijo, A. Márquez, and R. I. Silveira, *Continuous mean distance of a weighted graph*, arXiv:`2103.11676`, submitted 2021-03-22, Results in Mathematics (2023).
5. L. N. Baptista, J. B. Kennedy, and D. Mugnolo, *Mean distance on metric graphs*, arXiv:`2312.04952`, submitted 2023-12-08.
