# A triangle fingerprint in the third cumulants of random matching color profiles

## Finding
Let \(n\ge3\) and partition all edges of the complete graph \(K_{2n}\) into \(q\ge3\) nonempty color classes, such that the subgraph of color \(i\) is spanning and \(d_i\)-regular. In particular, \(d_i\ge1\) and \(\sum_i d_i=2n-1\). Sample a perfect matching \(M\) uniformly and let \(L_i\) be the number of its edges of color \(i\). Set
\[
A_n=\frac{2n(n-1)}{(2n-1)(2n-3)}.
\]
The complete covariance matrix is independent of the arrangement of colored edges:
\[
\operatorname{Cov}(L_i,L_j)=A_n\left(d_i\mathbf1_{i=j}-\frac{d_id_j}{2n-1}\right).
\]
Equivalently, with \(p_i=d_i/(2n-1)\), this is precisely \(2(n-1)/(2n-3)\) times the covariance of a multinomial sample of size \(n\) with category probabilities \(p_i\). The covariance has rank \(q-1\), and all distinct color counts are strictly negatively correlated.

For three *distinct* colors \(i,j,k\), let \(T_{ijk}\) be the number of ordinary vertex triangles in the colored complete graph whose three edge colors are precisely \(i,j,k\), one of each. The entire dependence of their third mixed cumulant on the particular regular edge coloring is the negative triangle term:
\[
\boxed{\kappa(L_i,L_j,L_k)=
\frac{2n(4n^2-8n+5)d_id_jd_k}{(2n-5)(2n-3)(2n-1)^3}
-\frac{T_{ijk}}{(2n-5)(2n-3)(2n-1)}.}
\]
Here \(\kappa(X,Y,Z)=\mathbb E[XYZ]-\mathbb E[XY]\mathbb E[Z]-\mathbb E[XZ]\mathbb E[Y]-\mathbb E[YZ]\mathbb E[X]+2\mathbb E[X]\mathbb E[Y]\mathbb E[Z]\).

This distinction occurs even inside one fixed one-factorization. In the affine coloring of \(K_8\) with vertices \(\mathbb F_2^3\), color the edge \(\{x,y\}\) by the nonzero vector \(x+y\). Every color class is a perfect matching. For distinct nonzero colors \(a,b,c\), the third mixed cumulant equals
\[
\kappa(L_a,L_b,L_c)=
\begin{cases}
-32/1715,&a+b+c=0,\\
296/5145,&a+b+c\ne0.
\end{cases}
\]
Thus all seven color counts have identical means and pairwise covariance, but color triples can have strictly opposite signs of their third mixed cumulants. The first and second moments are blind to colored triangle geometry; the third mixed moments recover the rainbow-triangle counts exactly.

## Assumptions and scope
A regular color class means every vertex has the same integer degree \(d_i\) in that class. The edge classes form a partition of *all* edges of \(K_{2n}\). Color classes need not be connected, isomorphic, or single matchings. A uniformly random perfect matching means each of the \((2n-1)!!\) matchings has the same probability. The theorem holds for each finite integer \(n\ge3\); it makes no asymptotic claim. Repeated-color third cumulants are not covered by the displayed triangle formula.

## Proof
For any \(r\in\{1,2,3\}\) prescribed vertex-disjoint edges, the probability that all belong to \(M\) is
\[
p_r=\prod_{s=0}^{r-1}(2n-2s-1)^{-1}.
\]
If two prescribed edges meet, their simultaneous inclusion has probability zero. Each color \(i\) has \(n d_i\) edges. Consequently,
\[
\mathbb E L_i=\frac{n d_i}{2n-1}.
\]
For distinct colors \(i,j\), exactly \(2n d_i d_j\) ordered pairs of differently colored edges intersect. Hence their disjoint ordered pairs number \(n(n-2)d_id_j\), and
\[
\mathbb E[L_iL_j]=n(n-2)d_id_jp_2.
\]
For one color \(i\), among its ordered pairs of *different* edges, exactly \(2n d_i(d_i-1)\) intersect; hence
\[
\mathbb E L_i^2=n d_i p_1+n d_i\bigl((n-2)d_i+1\bigr)p_2.
\]
Subtracting products of first moments in these two cases, and simplifying, gives the claimed covariance matrix.

For distinct colors \(i,j,k\), first choose disjoint edges \(e_i,e_j\) of colors \(i,j\). There are \(n(n-2)d_id_j\) ordered choices. The number of color-\(k\) edges avoiding their four endpoints equals \((n-4)d_k\) plus the number of color-\(k\) edges entirely within those four endpoints. Since the three colors are distinct, such an internal color-\(k\) edge joins an endpoint of \(e_i\) to an endpoint of \(e_j\). Summed over all disjoint \((e_i,e_j)\), these internal edges contribute
\[
2n d_id_jd_k-T_{ijk}.
\]
Indeed, fixing a color-\(k\) edge with endpoints \(u,v\), there are \(2d_id_j\) potential choices of an \(i\)-edge at one endpoint and a \(j\)-edge at the other, except when the two other endpoints coincide. The excluded cases are in bijection with triangles using exactly the three colors. Therefore the ordered triples of pairwise disjoint edges of respective colors \(i,j,k\) number
\[
Q_{ijk}=n\bigl((n-2)(n-4)+2\bigr)d_id_jd_k-T_{ijk}
=n(n^2-6n+10)d_id_jd_k-T_{ijk}.
\]
Each such triple is present in \(M\) with probability \(p_3\), so
\[
\mathbb E[L_iL_jL_k]=\frac{n(n^2-6n+10)d_id_jd_k-T_{ijk}}{(2n-1)(2n-3)(2n-5)}.
\]
Insert this and the first two moment formulas into the definition of \(\kappa\). The color-degree coefficient reduces algebraically to \(2n(4n^2-8n+5)/[(2n-5)(2n-3)(2n-1)^3]\); the triangle coefficient is \(-p_3\). This proves the third-cumulant identity.

For the covariance rank, take any real vector \(w\) and put \(\bar w=\sum_i d_iw_i/(2n-1)\). Then
\[
w^{\mathsf T}\operatorname{Cov}(L)w=A_n\sum_i d_i(w_i-\bar w)^2.
\]
Since every \(d_i\) is positive, the only null vectors are constants, and every distinct-color covariance is negative.

For the affine witness, put \(n=4\). The edges of color \(a\ne0\) are exactly \(\{x,x+a\}\), a degree-one color class. A triangle with three prescribed distinct colors \(a,b,c\) exists precisely when \(a+b+c=0\), and in that case there are eight such triangles: one for each vertex at which the \(a\)- and \(b\)-colored sides meet. Thus \(T_{abc}\) is respectively \(8\) or \(0\). Substitution in the general formula yields \(296/5145-8/105=-32/1715\) or \(296/5145\), proving both signs.

## Verification
The standalone `verify_moments.py` enumerates every perfect matching of the indicated complete graphs and computes exact rational moments independently from the theorem's counting formulas. It checks the full first- and second-moment identities and each distinct-color third moment and cumulant for cyclic length colorings on \(K_6,K_8,K_{10},K_{12}\), the affine seven-color factorization of \(K_8\), and a coarsening of that factorization into three regular colors. It also enumerates all vertex triangles, verifies the affine color-triple dichotomy, and tests the two opposite exact third-cumulant values. There are no numerical tolerances or statistical sampling. Run `python3 verify_moments.py` using Python 3 standard library only. Finite checking is corroboration; the counting argument above establishes all \(n\ge3\).

## Relationship to prior work
Woolbright and Fu (1998) prove existence of a rainbow perfect matching in every one-factorization of a complete graph of even order. Their full primary text studies existence via edge-switching and case analysis, rather than the exact distribution of colors in a uniformly random matching. Acan (2015) studies uniformly random chord diagrams (uniform perfect matchings of cyclically ordered points) and shows fixed collections of short chord-length counts approach independent Poisson laws; this is about limiting local counts, not third color-profile cumulants for arbitrary regular edge partitions. Bal and Frieze (2013) study existence of rainbow matchings in randomly edge-colored random graphs/hypergraphs, again a different random object. Classical two- and three-edge probabilities in uniform matchings are used as inputs here and are not claimed as new. The specific third-order rainbow-triangle fingerprint, combined with exact second-order design universality and the affine sign reversal, was not found in the primary statements inspected or in the described mathematical searches; this is not a proof of historical uniqueness.

## Limitations
The formulas require uniform perfect matchings of a complete graph and each color class to be regular. For arbitrary nonregular colorings, the first two moments depend on local degrees rather than just color sizes. The displayed third cumulant applies only to *three distinct* colors. It does not determine the full joint distribution, higher cumulants, or an asymptotic central limit law. General weighted-matching moment expansions could implicitly encode the formula even without displaying it in this form; independent historical-priority review remains outstanding. The result has received a self-review, not independent audit.

## References
1. D. E. Woolbright and H.-L. Fu, *On the Existence of Rainbows in 1-Factorizations of* \(K_{2n}\), Journal of Combinatorial Designs **6** (1998), 1–20. DOI: `10.1002/(SICI)1520-6610(1998)6:1<1::AID-JCD1>3.0.CO;2-J`. Full-text material available at `https://www.researchgate.net/publication/242938358_On_the_existence_of_rainbows_in_1-factorizations_ofK2n`.
2. H. Acan, *On a Uniformly Random Chord Diagram and Its Intersection Graph*, first posted January 7, 2015, `arXiv:1501.01489`, especially Theorem 4.2.
3. D. Bal and A. Frieze, *Rainbow Matchings and Hamilton Cycles in Random Graphs*, `arXiv:1311.6423`, first posted November 25, 2013.
