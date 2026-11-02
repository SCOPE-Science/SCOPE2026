# Sharp Lipschitz spread and parity frustration in bouquets of congruent cycles

## Finding

**Theorem (exact spread, optimizer rigidity and alternating attachment law).** Let \(q\ge 4\) and \(r\ge 2\) be integers. Identify one vertex of each of \(r\) disjoint unit-edge cycles of length \(q\) to form the rooted Dutch-windmill graph \(R_{q,r}\). Equip all \(N=1+r(q-1)\) vertices with uniform probability and graph shortest-path distance. Put
\[
 d_j=\min\{j,q-j\}\quad(1\le j<q),\qquad
 a_q=\sum_{j=1}^{q-1}d_j,\qquad
 b_q=\sum_{j=1}^{q-1}d_j^2.
\]
The sharp real Lipschitz–Poincaré variance constant is
\[
 \operatorname{spr}(R_{q,r})
 :=\max_{\operatorname{Lip}(f)\le1}\frac1N\sum_{v\in V(R_{q,r})}(f(v)-\bar f)^2
 =\frac{r b_q}{N}-\mathbf1_{\{r\text{ odd}\}}\frac{a_q^2}{N^2}.
\]
Every maximizing function, and no others, is obtained by assigning the common vertex any value \(c\in\mathbb R\) and, on each petal \(C_q^{(i)}\), defining
\[
 f(v)=c+\varepsilon_i\, d_{C_q^{(i)}}(v,o),
 \qquad \varepsilon_i\in\{-1,1\},
 \qquad\left|\sum_{i=1}^r\varepsilon_i\right|=r\bmod 2.
\]
Thus for an even number of petals the signs balance exactly; for an odd number they differ by one. Relabelling or reflecting petals gives no additional type of maximizer.

For fixed \(q\), writing \(V_r=\operatorname{spr}(R_{q,r})\), the sharp constants satisfy
\[
 V_{r+1}<V_r\quad\text{when }r\ge2\text{ is even},\qquad
 V_{r+1}>V_r\quad\text{when }r\ge3\text{ is odd},
 \qquad \lim_{r\to\infty} V_r=\frac{b_q}{q-1}.
\]
In particular, adding a further congruent cycle decreases the sharp spread whenever the old bouquet contains an even number of petals, despite increasing its vertex set.

## Assumptions and scope

Each petal is a *simple* cycle with \(q\ge4\) vertices, different petals share exactly the root \(o\), and there are no other edges. Functions are real and satisfy \(|f(u)-f(v)|\le1\) on graph edges; this is equivalent to the shortest-path \(1\)-Lipschitz condition. Means and variances use equal masses at all \(N\) distinct vertices, including a single copy of the root. The theorem covers every finite integer pair \((q,r)\) in the stated range. It neither concerns graph adjacency spectral spread nor asserts monotonicity for arbitrary graph attachments.

Useful closed expressions are, for even \(q=2k\), \(a_q=k^2\) and \(b_q=k(2k^2+1)/3\), and for odd \(q=2k+1\), \(a_q=k(k+1)\) and \(b_q=k(k+1)(2k+1)/3\).

## Proof

**1. The single-cycle centered-variance lemma.** For every real one-Lipschitz \(g\) on a unit cycle \(C_q\),
\[
 \sum_{v\in C_q}(g(v)-\bar g)^2\le b_q-\frac{a_q^2}{q}.
 \tag{1}
\]
Equality is attained by distance-to-vertex functions and their negatives, up to an additive constant. This follows from the permutation-convexity classification of cycle profiles underlying the proof of Yancey, Section 2.3, Theorem 2.9. That paper states its conclusion for a logarithmic moment-generating objective, rather than for centered quadratic variance: the relevant intermediate argument identifies the permutation-extreme subset of the cycle Lipschitz polytope with translates and reflections of the distance-to-a-vertex profile. Although that paper phrases the argument for the centered logarithmic moment generating function, its displayed permutation decomposition and exclusion argument use only strict convexity and permutation invariance. Both hold for the centered quadratic form \(\sum(g-\bar g)^2\): if two nonidentical centered vectors have mean-preserving convex average, strict convexity gives a strictly smaller quadratic value; permutation leaves the quadratic value invariant. Consequently the same combinatorial exclusion proves (1). In particular, the distance profile of \(o\) has values \((0,d_1,\ldots,d_{q-1})\), with centered squared sum \(b_q-a_q^2/q\). This establishes the numerical constant in (1) and its validity for both even and odd cycles. No assertion of a new one-cycle inequality is made here.

**2. Reduction to petal sums.** Translation invariance permits \(f(o)=0\). For petal \(i\), let \(S_i\) and \(Q_i\) be the sum of its \(q-1\) nonroot values and the sum of their squares. The root is zero, so (1) gives
\[
 Q_i-\frac{S_i^2}{q}\le b_q-\frac{a_q^2}{q}.
 \tag{2}
\]
Since \(|f(v)|\le d_{C_q}(o,v)\), we also have \(|S_i|\le a_q\). The total unnormalized centered squared deviation \(J=N\operatorname{Var}(f)\) therefore obeys
\[
 J=\sum_i Q_i-\frac{(\sum_i S_i)^2}{N}
 \le r\Bigl(b_q-\frac{a_q^2}{q}\Bigr)
 +\frac1q\sum_i S_i^2-\frac1N\Bigl(\sum_iS_i\Bigr)^2.
 \tag{3}
\]
All inequalities are valid for every real admissible function, not only extreme points.

**3. Sharp cubical maximization.** Regard the right side of (3) as a quadratic \(F(S_1,\ldots,S_r)\) on \([-a_q,a_q]^r\). With all other coordinates fixed, its coefficient of \(S_i^2\) is \(1/q-1/N>0\), because \(N=1+r(q-1)>q\). Thus \(F\) is *strictly convex separately in every coordinate*, and every maximizer over the box has \(S_i\in\{-a_q,a_q\}\). At those corners, writing \(S_i=\varepsilon_i a_q\), equation (3) becomes
\[
 J\le r b_q-\frac{a_q^2}{N}\Bigl(\sum_i\varepsilon_i\Bigr)^2.
 \tag{4}
\]
The smallest absolute sum of \(r\) signs is zero for even \(r\) and one for odd \(r\). Choose \(f(v)=\varepsilon_i d_{C_q}(o,v)\) on petal \(i\): all edge constraints hold, \(S_i=\varepsilon_i a_q\), \(Q_i=b_q\), and (2)–(4) are equalities. Dividing (4) by \(N\) proves the sharp constant.

For rigidity, equality in the sharp bound forces \(F\) to be maximized and hence every \(|S_i|=a_q\). Equality in the triangle bound \(|S_i|\le\sum_{v\ne o}d(o,v)=a_q\), together with \(|f(v)|\le d(o,v)\), forces each nonroot value on that petal to be \(\varepsilon_i d(o,v)\). Finally (4) requires the minimum possible signed sum. This proves the claimed *complete* optimizer classification without requiring classification of all equality cases in the single-cycle inequality.

**4. Alternating attachment law.** Set \(h=q-1\) and \(N_r=1+rh\). The exact formula gives, for odd \(r\),
\[
 V_{r+1}-V_r=\frac{b_q}{N_rN_{r+1}}+\frac{a_q^2}{N_r^2}>0.
 \tag{5}
\]
For even \(r\),
\[
 V_{r+1}-V_r=
 \frac{b_qN_{r+1}-a_q^2N_r}{N_rN_{r+1}^2}.
 \tag{6}
\]
Direct substitution of the two displayed formulas for \(a_q,b_q\) gives \(a_q^2\ge2b_q\) for every \(q\ge4\). Also \(N_{r+1}/N_r=1+h/N_r<1+1/r\le3/2\) when \(r\ge2\). Thus the numerator in (6) is strictly negative. Finally \(r/N_r\to1/h\) and \(a_q^2/N_r^2\to0\), giving the stated limit.

## Verification

The supplied standalone Python program `verify_cycle_roses.py` uses only the standard library. Execute `python3 verify_cycle_roses.py`. It independently enumerates the vertices of the rooted-cycle Lipschitz polytope for cycle lengths \(3\) through \(11\), then checks the single-cycle centered-variance maximum; performs exact dynamic-programming optimization over all petal-state sums for lengths \(3\) through \(10\) and petal counts \(2\) through \(8\); performs direct labelled extreme-potential checks on selected graphs; and tests the alternating attachment inequalities on a larger finite grid. All integer and rational comparisons use exact arithmetic. These checks are finite diagnostics and are not proofs of the all-parameter theorem; the proof above supplies that argument.

## Relationship to prior work

The foundational graph-spread problem, a sharp variance inequality for uniformly sampled graph vertices, predates this result. Addario-Berry, Janson and McDiarmid (first public preprint 2009-02-06) study primarily random-graph spread, not the one-point unions here. Yancey's cycle analysis (2017, Section 2.3 and Theorem 2.9) supplies the crucial one-cycle permutation-extremal structure; the present proof explicitly uses rather than reclaims it. The separate previously studied *clique-bouquet* family includes triangle petals, so \(q=3\) is deliberately excluded. For \(q\ge4\), petals are noncomplete cycles; neither the clique formula nor a direct sum of individual variances gives the present parity correction or its strictly alternating attachment law. Related work on cactus transportation-space basis constants, numerical indices of cycles, and cycle-homology invariants concerns different quantities and does not imply (3)–(6). Searches for a stronger gluing/spread formula and for one-point unions of cycles did not identify a covering theorem; this is not a proof of comprehensive literature uniqueness.

## Limitations

The conclusion requires congruent unit-edge cycle petals, one identified root, real scalar observables, and uniform vertex masses. In particular, it does not classify heterogeneous cycle lengths, arbitrary cactus graphs, weighted vertices, higher centered moments, or sharp concentration tails. The single-cycle extremal lemma is cited from an accessible published preprint with a detailed adaptation of its strict-convexity argument; a different, unindexed formulation of a one-point-union spread theorem remains a literature-priority risk. Independent scientific validation has not been performed.

## References

1. L. Addario-Berry, S. Janson and C. McDiarmid, *On the spread of random graphs* (preprint first public 2009-02-06), arXiv:0902.1156, https://arxiv.org/abs/0902.1156.
2. M. P. Yancey, *Probabilistic and Geometrical Applications to Graph Theory* (2017), Section 2.3, Theorem 2.9, arXiv:1705.09725, https://arxiv.org/html/1705.09725v1.
3. N. Alon, R. Boppana and J. Spencer, *An asymptotic isoperimetric inequality*, Geometric and Functional Analysis **8** (1998), 411–436, https://doi.org/10.1007/s000390050062. The older foundational citation is bibliographic background, not a source of the new bouquet formula.
