# Sharp horizon transition for variation of finite uncentered interval maxima

## Finding

For every integer \(n\ge 2\) and horizon \(R\in\{1,\ldots,n\}\), define the uncentered interval maximal operator on a real \(n\)-term sequence by
\[
(U_R f)(i)=\max_{\substack{1\le a\le i\le b\le n\\ b-a+1\le R}}\frac{1}{b-a+1}\sum_{j=a}^{b}|f(j)|,
\qquad i=1,\ldots,n.
\]
Write \(V(f)=\sum_{i=1}^{n-1}|f(i+1)-f(i)|\). Its exact one-input variation amplification constant is
\[
\boxed{\sup_{V(f)>0}\frac{V(U_R f)}{V(f)}=
\begin{cases}
1,&1\le R<n,\\
1-\dfrac1n,&R=n.
\end{cases}}
\]
Every value is attained by the endpoint indicator \(f=\mathbf{1}_{\{1\}}\). In particular, admitting all contiguous intervals forces strict finite-size contraction, while excluding even the sole longest interval restores the sharp factor \(1\).

## Assumptions and scope

The path is the ordered vertex set \(\{1,\ldots,n\}\) with unit counting mass at each vertex. Intervals are arbitrary nonempty **contiguous vertex intervals containing the evaluation vertex**; they need not be centered graph balls. The positive integer \(R\) caps their number of vertices, not their radius. The input may be real and signed; averages are of absolute values. No endpoint padding or outside vertices are used. The result is for one-input variation, not a two-input variation Lipschitz constant.

## Proof

It is sufficient to take \(f\ge0\): the operator depends only on \(|f|\), and \(V(|f|)\le V(f)\). Write \(g=U_R f\), so \(g(i)\ge f(i)\).

**Peak-contact lemma.** Every maximal contiguous plateau \(I\) on which \(g\) takes a local-maximum value \(H\), with the adjacent values outside \(I\) (if any) strictly smaller, contains a vertex \(p\) with \(f(p)=g(p)=H\). Indeed, take any \(i\in I\) and a maximizing interval \(K\) for \(g(i)=H\). If \(K\) crossed an endpoint of \(I\), it would contain the neighboring vertex \(j\notin I\) where \(g(j)<H\); but the very same average over \(K\) would give \(g(j)\ge H\), a contradiction. Thus \(K\subseteq I\). Since \(f(j)\le g(j)=H\) for every \(j\in K\), their average can equal \(H\) only if \(f(j)=H\) on \(K\); any such vertex is a contact point. This argument also treats maximum plateaus at either boundary. If \(g\) is constant, the claimed variation bound is immediate.

Choose one contact point in each local-maximum plateau, and choose points in the intervening local-minimum plateaus and at any unpaired boundary minima. These points occur in increasing order and split the graph into disjoint subpaths on which \(g\) is monotone. Each nonzero change of \(g\) along the selected subpaths connects a contact maximum \(p\) with an adjacent valley \(v\); the total variation \(V(g)\) is exactly the sum of these peak-to-valley height differences. The input variations on the corresponding disjoint subpaths sum to at most \(V(f)\).

For an arbitrary horizon, \(g(p)=f(p)=H\) and \(g(v)\ge f(v)\), so
\[
0\le g(p)-g(v)\le f(p)-f(v)\le V(f;[p,v]),
\]
where \(V(f;[p,v])\) denotes the sum of the absolute adjacent differences between the two vertices. Summing proves \(V(U_R f)\le V(f)\) for all \(R\).

For \(R=n\), **the entire interval between \(p\) and \(v\) is admissible**. Put \(d=|p-v|\ge1\) and \(m=\min_{j\in[p,v]} f(j)\), where \([p,v]\) is the contiguous interval with those endpoints. Its average is at least
\[
\frac{H+dm}{d+1}=m+\frac{H-m}{d+1},
\]
because one of its \(d+1\) entries equals \(H\) and all others are at least \(m\). Consequently,
\[
g(p)-g(v)\le\frac{d}{d+1}(H-m)
\le\frac{n-1}{n}\,V(f;[p,v]).
\]
Summing over the disjoint peak-to-valley subpaths yields \(V(U_n f)\le(1-1/n)V(f)\).

For sharpness, take \(f(1)=1\) and \(f(i)=0\) for \(i\ge2\). Then \(V(f)=1\), and a direct interval calculation gives
\[
(U_R f)(i)=
\begin{cases}
1/i,&1\le i\le R,\\
0,&R<i\le n.
\end{cases}
\]
When \(R<n\), its variation telescopes from \(1\) down to \(0\), and is exactly \(1\). When \(R=n\), it telescopes from \(1\) to \(1/n\), and is exactly \(1-1/n\). This proves both sharp constants and attainment.

## Verification

The standalone `verify.py` uses exact rational arithmetic. It tested all ternary-valued, nonnegative input profiles for \(2\le n\le8\) and every admissible horizon (73,809 profile/horizon cases), plus 3,000 signed rational cases at larger lengths. It checked 35 endpoint-indicator sharpness profiles. All checks passed. To reproduce, run `python3 verify.py` using Python 3. The analytic argument above establishes the universal result independently of finite testing.

## Relationship to prior work

Aldaz and Pérez Lázaro (arXiv:math/0601044, first public 2006-01-03) proved nonincrease of variation for the continuous one-dimensional uncentered maximal operator and its length-truncated version. Bober, Carneiro, Hughes, and Pierce (arXiv:1005.3030, first public 2010-05-17) proved the sharp coefficient \(1\) for the uncentered discrete maximal operator on the whole integer line. The present result concerns the exact, strictly smaller constant for a *finite, fully accessible interval family* and the abrupt change when its longest interval is disallowed. The coefficient \(1\) for truncated horizons is consistent with the earlier general variation-contraction mechanism, and is not claimed as a new stand-alone variation inequality.

González-Riquelme, Kovač, and Madrid (arXiv:2603.12462, 2026-03-12) conjectured \(1-1/n\) for the **centered graph-ball** maximal operator on finite paths. That family of admissible averages is different: the present noncentered interval theorem neither assumes nor resolves that conjecture.

## Limitations

This is not a result for centered graph-ball maximal averages, arbitrary finite graphs, positive unequal vertex masses, or two-input variation Lipschitz constants. The finite-size improvement depends on the inclusion of every interval, including the full path. Literature comparison cannot establish logical uniqueness and may miss an equivalent finite-interval statement in older sources; the closest accessible primary works were inspected for their relevant theorems and proofs.

## References

1. J. M. Aldaz and J. Pérez Lázaro, *Functions of bounded variation, the derivative of the one dimensional maximal function, and applications to inequalities*, arXiv:math/0601044 (first public 2006-01-03), especially Theorem 2.5 and Remark 2.6. https://arxiv.org/abs/math/0601044
2. J. Bober, E. Carneiro, K. Hughes, and L. B. Pierce, *On a discrete version of Tanaka's theorem for maximal functions*, arXiv:1005.3030 (first public 2010-05-17), especially Section 2 and Theorem 1. https://arxiv.org/abs/1005.3030
3. C. González-Riquelme, V. Kovač, and J. Madrid, *Sharp variational inequalities for the Hardy–Littlewood maximal operator on finite undirected graphs*, arXiv:2603.12462 (first public 2026-03-12), especially the introduction and Conjecture 5. https://arxiv.org/html/2603.12462v1
4. C. González-Riquelme and J. Madrid, *Sharp inequalities for maximal operators on finite graphs, II*, J. Math. Anal. Appl. 506 (2022), article 125647; DOI: 10.1016/j.jmaa.2021.125647.
