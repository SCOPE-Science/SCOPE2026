# A flat three-regime Euclidean distortion law for matching-stretched bipartite metrics

## Finding

For every integer \(n\ge3\) and real \(1\le s\le3\), let \(X_{n,s}=\{a_1,\ldots,a_n,b_1,\ldots,b_n\}\) have distances
\[
 d(a_i,a_j)=d(b_i,b_j)=2\quad(i\ne j),\qquad
 d(a_i,b_j)=\begin{cases}s,&i=j,\\1,&i\ne j.\end{cases}
\]
This is the shortest-path metric of a complete bipartite graph with its perfect-matching edges assigned length \(s\), the remaining edges having length \(1\). Put
\[
 r=s^2,\qquad r_- = \frac{2(n-1)}{n-2},\qquad r_+=\frac{8(n-1)}n.
\]
The least distortion of an embedding into any real Hilbert space is attained, and its **exact square** is
\[
\boxed{
 c_2(X_{n,s})^2=\begin{cases}
 \dfrac{4(n-1)}{n-1+r},&1\le r\le r_-,\\[4pt]
 \dfrac{4(n-2)}n,&r_-\le r\le r_+,\\[4pt]
 \dfrac{r(n-2)}{2(n-1)},&r_+\le r\le9.
\end{cases}}
\]
In particular there is a **nondegenerate interval of matching-edge lengths on which the exact optimal distortion is constant**. Every optimal embedding, after rescaling so its least pairwise stretch is \(1\), is unique up to a Hilbert-space isometry. Its minimum affine dimension is \(2n-2\) when \(1\le r<r_-\), but just \(n-1\) when \(r_-\le r\le9\). The reduction of affine dimension at the first transition is sharp.

At the two graph-metric endpoints, the formula specializes to
\[
 c_2(K_{n,n})^2=\frac{4(n-1)}n,
 \qquad c_2(K_{n,n}\setminus M_n)^2=\frac{9(n-2)}{2(n-1)}.
\]
These endpoint values are consequences of the general result; the formulas for graph-metric endpoints are not claimed as separate priority results.

## Assumptions and scope

The source metric is finite, all \(2n\) points are retained, and no additional edge weights vary. A bi-Lipschitz embedding \(F:X_{n,s}\to H\) into a real Hilbert space has distortion
\[
 \operatorname{dist}(F)=
 \frac{\max_{x\ne y}\|F(x)-F(y)\|/d(x,y)}
 {\min_{x\ne y}\|F(x)-F(y)\|/d(x,y)}.
\]
The least distortion is \(c_2\). Positive scalar rescaling makes the least stretch \(1\); writing \(T=\operatorname{dist}(F)^2\), we then have \(d(x,y)^2\le\|F(x)-F(y)\|^2\le T d(x,y)^2\) for every pair. Since \(n\ge3\), two distinct same-class vertices have a two-edge path, while a matched pair has an alternative three-edge path, proving the displayed shortest-path distances for \(1\le s\le3\). Every formula includes its boundary values.

## Proof

**Two universal Hilbert identities.** Write \(A_i=F(a_i)\), \(B_i=F(b_i)\). Let \(\alpha\) be the mean of squared distances over the \(n(n-1)\) unordered within-class pairs from *both* classes; let \(\beta\) be the mean over the \(n(n-1)\) ordered-index cross pairs \((A_i,B_j)\), \(i\ne j\); let \(\gamma\) be the mean over the \(n\) matched pairs \((A_i,B_i)\). In terms of \(T\),
\[
4\le\alpha\le4T,\qquad1\le\beta\le T,\qquad r\le\gamma\le rT.
\]
Expanding squared Hilbert norms and cancelling scalar products yields the **exact** identities
\[
\sum_{i<j}\|(A_i+B_i)-(A_j+B_j)\|^2
=n(n-1)(\alpha+\beta-\gamma),\tag{1}
\]
\[
\left\|\sum_i(A_i-B_i)\right\|^2
=n\left(\gamma-(n-1)(\alpha-\beta)\right).\tag{2}
\]
Thus \(\gamma\le\alpha+\beta\) and \(\gamma\ge(n-1)(\alpha-\beta)\). Combining these inequalities gives
\[
 \alpha-\beta\le\frac{\gamma}{n-1},\qquad
 \gamma-\beta\le\alpha,
 \qquad\beta\ge\frac{n-2}{2(n-1)}\gamma.
\]
Using the elementary pair bounds in three different ways now yields
\[
T\ge\frac{r(n-2)}{2(n-1)},\qquad
T\ge\frac{4(n-1)}{n-1+r},\qquad
T\ge\frac{4(n-2)}n.\tag{3}
\]
For the second, use \(rT\ge\gamma\ge(n-1)(4-T)\). For the third, use \(\gamma\le 2(n-1)\beta/(n-2)\), whence \(4\le\alpha\le n\beta/(n-2)\le nT/(n-2)\). The maximum of the three right sides in (3) is exactly the announced three-branch expression: the descending first-branch function meets the constant at \(r_-\), and the ascending third-branch function meets it at \(r_+\); one has \(1<r_-<r_+<9\).

**Sharp constructions.** Take two centered regular simplices \(u_1,\ldots,u_n\) and \(v_1,\ldots,v_n\), mutually orthogonal, each having side length \(2\). Then
\[
\langle u_i,u_j\rangle=\langle v_i,v_j\rangle
=\begin{cases}2(n-1)/n,&i=j,\\-2/n,&i\ne j.\end{cases}
\]
For \(1\le r\le r_-\), set
\[
 \eta=1-\frac{nr}{n-1+r}\in[-1,0],\qquad
 A_i=u_i,\quad B_i=\eta u_i+\sqrt{1-\eta^2}\,v_i.
\]
The three squared-distance values (within class, cross off matching, matched cross) are
\[
 (\alpha,\beta,\gamma)=
 \left(4,\frac{4(n-1)}{n-1+r},\frac{4r(n-1)}{n-1+r}\right).
\]
All required pair constraints hold with \(T=4(n-1)/(n-1+r)\). If \(r=r_-\), then \(\eta=-1\) and the configuration becomes antipodal.

For \(r_-\le r\le r_+\), set \(A_i=u_i\) and \(B_i=-u_i\). The three squared distances are
\[
 (\alpha,\beta,\gamma)
 =\left(4,\frac{4(n-2)}n,\frac{8(n-1)}n\right).
\]
The matched value belongs to \([r,rT]\) exactly throughout this interval, with \(T=4(n-2)/n\). This one antipodal simplex configuration is simultaneously optimal for every parameter in the plateau.

For \(r_+\le r\le9\), put \(\lambda^2=rn/[8(n-1)]\) and set \(A_i=\lambda u_i\), \(B_i=-\lambda u_i\). Then
\[
 (\alpha,\beta,\gamma)
 =\left(\frac{rn}{2(n-1)},\frac{r(n-2)}{2(n-1)},r\right),
\]
which obeys the pair bounds with \(T=r(n-2)/(2(n-1))\). This proves exact sharpness and attainment in all cases, including the transition points.

**All extremizers and affine rank.** In the open low branch, equality in the second lower bound in (3) forces \(\alpha=4\), \(\beta=T\), \(\gamma=rT\). Since every pairwise squared distance lies on the indicated side of its corresponding bound, *all* within-class, off-matching, and matching distances are thereby individually fixed. Their distance matrix determines the entire configuration up to isometry. The displayed two-simplex construction has affine dimension \(2n-2\) because \(-1<\eta\le0\).

On the plateau, equality in the third lower bound forces \(\alpha=4\), \(\beta=T\), \(\gamma=8(n-1)/n\), together with equality in (1) and (2). At the high branch, equality in the first lower bound forces \(\beta=T\), \(\gamma=r\), \(\alpha=\gamma-\beta\), and again equality in (1) and (2). In both situations (1) implies that every \(A_i+B_i\) is the same vector and (2) implies that the sums of the \(A_i\) and \(B_i\) coincide. After translating, \(B_i=-A_i\) and \(\sum_i A_i=0\). Plateau equality also fixes each same-class distance at \(2\), forcing a centered regular simplex. High-branch equality fixes each \(\|A_i-B_i\|^2=r\) and each \(\|A_i-B_j\|^2=T\) for \(i\ne j\), forcing equal squared norms and equal off-diagonal inner products for \(A_i\); the centered configuration is again a unique regular simplex. Thus every normalized optimum is congruent to the indicated construction, and the affine dimension is \(n-1\). At \(r=r_-\) the low-branch configuration already equals the antipodal simplex, and at \(r=r_+\) the plateau and high constructions coincide. This proves rigidity and the exact dimension jump.

## Verification

Run `python3 verify_matching_stretch_distortion.py` in a standard Python 3 environment. The standalone standard-library checker uses exact fractions to test each branch, endpoint, all three squared-distance classes, the two Hilbert inequalities, the sharp lower bounds, and the predicted centered-Gram ranks over \(161\) configurations. It independently checks both underlying universal identities on \(120\) arbitrary rational-vector configurations. It also checks the six-cycle and cube specializations. The proof above, not finite testing, establishes the assertions for every real \(s\) and every integer \(n\ge3\).

## Relationship to prior work

Robertson's 2023 preprint explicitly evaluated the complete-bipartite endpoint and developed general distorted-negative-type duality; the case \(s=1\) is therefore acknowledged as previously established. Vallentin's 2005 preprint (published in 2008) developed the symmetry-reduced semidefinite approach to least Euclidean distortion for distance-regular graph metrics, including Hamming graphs and strongly regular graphs; the full text presents a general spectral lower bound. Jolissaint and Valette's 2011 preprint (journal version in 2014) established spectral-gap distortion bounds for regular graphs. Cioabă, Gupta, Ihringer, and Kurihara's 2021 preprint (published in 2022) proved a sharp general formula for **unweighted distance-regular graphs of diameter three**, covering the unweighted crown-graph endpoint as a corollary. The present result does *not* claim that endpoint anew. Rather, it gives the full continuous matching-stretch parameter, the exact flat plateau, uniqueness of **every** optimum (not just a symmetric optimum), and the dimension jump at a real-valued critical parameter. The earlier spectral graph formulas do not directly furnish this nonuniform weighted metric classification. The related negative-type classification of these distances concerns isometric snowflakes, a distinct invariant from least bi-Lipschitz distortion.

## Limitations

The metric family is balanced, with a single uniformly stretched perfect matching and fixed within-part distances. No assertion is made about unequal part sizes, heterogeneous matching lengths, arbitrary graph weights, other Banach targets, or the classification of all distance-regular graphs. This is an analytic classification with reproducible exact-rational tests; it has not undergone independent validation. Exhaustive novelty against differently stated or unindexed literature is not certified.

## References

1. F. Vallentin, *Optimal distortion embeddings of distance regular graphs into Euclidean spaces*, first posted September 30, 2005, arXiv:math/0509716; Journal of Combinatorial Theory, Series B **98** (2008), 95–104.
2. P.-N. Jolissaint and A. Valette, *\(L^p\)-distortion and \(p\)-spectral gap of finite graphs*, first posted October 5, 2011, arXiv:1110.0909; Bulletin of the London Mathematical Society **46** (2014), 329–341.
3. S. M. Cioabă, H. Gupta, F. Ihringer, and H. Kurihara, *The least Euclidean distortion constant of a distance-regular graph*, first posted September 20, 2021, arXiv:2109.09708; Discrete Applied Mathematics (2022).
4. G. Robertson, *Negative type and bi-Lipschitz embeddings into Hilbert space*, first posted September 27, 2023, arXiv:2309.16070, Section 4.
5. N. Linial and A. Magen, *Least-distortion Euclidean embeddings of graphs: products of cycles and expanders*, Journal of Combinatorial Theory, Series B **79** (2000), 157–171, DOI:10.1006/jctb.2000.1953.
