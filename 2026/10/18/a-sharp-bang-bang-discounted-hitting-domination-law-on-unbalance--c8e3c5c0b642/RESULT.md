# A sharp bang–bang discounted hitting domination law on unbalanced complete bipartite graphs

## Finding

Let \(G=K_{a,b}\) be the finite simple complete bipartite graph with integer part sizes \(2\le a<b\). Let \(0<\lambda<1\), \(0<\tau\le1\), and let \(\delta_{\lambda,\tau}(G)\) be the least number of pinned vertices \(S\) such that \(\mathbb E_v[\lambda^{T_S}]\ge\tau\) at **every** vertex of the simple random walk. Here \(T_S\) is its first hitting time of \(S\), and \(S\) itself has potential one.

For \(0<\tau\le\lambda\), define
\[
\beta=\frac{\tau(1-\lambda)}{\lambda(1-\tau)},\qquad
\rho=\frac{\tau(1-\lambda^2)}{\lambda^2(1-\tau)}
       =\frac{1+\lambda}{\lambda}\,\beta,\qquad
L=\min\{a\min\{1,\rho\},(a+b)\beta\},\quad K=\lceil L\rceil.
\]
Then \(K\le\delta_{\lambda,\tau}(G)\le K+1\). Whenever the one-sided term is no larger than the balanced term, that is \(a\min\{1,\rho\}\le(a+b)\beta\), **equality** \(\delta_{\lambda,\tau}(G)=K\) holds. Otherwise \(\delta_{\lambda,\tau}(G)\) is exactly \(K\) if the coefficient \([z^K]P_{a,b;\lambda,\tau}(z)\) defined below is positive, and exactly \(K+1\) if it is zero. For \(\tau>\lambda\), \(\delta_{\lambda,\tau}(G)=a+b\).

The complete counting polynomial of feasible pinned sets is
\[
P_{a,b;\lambda,\tau}(z)=\sum_{q=0}^a\sum_{r=0}^b
  \binom aq\binom br\,\mathsf F_{q,r}\,z^{q+r}.
\]
For \(q<a\), \(r<b\), put \(s=q/a\), \(t=r/b\), and
\[
U_{q,r}=\frac{\lambda t+\lambda^2s(1-t)}{1-\lambda^2(1-s)(1-t)},\qquad
V_{q,r}=\frac{\lambda s+\lambda^2t(1-s)}{1-\lambda^2(1-s)(1-t)}.
\]
Here \(\mathsf F_{q,r}=1\) precisely when \(U_{q,r}\ge\tau\) and \(V_{q,r}\ge\tau\). On the boundary \(q=a\) or \(r=b\), set \(\mathsf F_{q,r}=1\) if the set is all of \(V(G)\), or if \(\tau\le\lambda\); otherwise set it to zero. Thus every coefficient, every optimizer profile, and the exact number \([z^{\delta_{\lambda,\tau}(G)}]P_{a,b;\lambda,\tau}(z)\) of minimum placements are determined by \((a+b+2)\)-scale finite binomial sums, without enumerating vertex subsets.

The continuous placement lower bound has an explicit phase change. For \(0<\tau\le\lambda^2\), its winning mechanism is one-sided if \(b/a\ge1/\lambda\) and balanced if \(b/a\le1/\lambda\); equality gives a tie, with the one-sided rounding remaining exact. For \(\lambda^2<\tau\le\lambda\), the competition is between the entire smaller part (cost \(a\)) and the balanced density (cost \((a+b)\beta\)); the transition is \(\tau_*=\lambda a/[a+(1-\lambda)b]\) whenever \(b/a<1/\lambda\). In particular the aspect-ratio boundary below \(\lambda^2\) does not depend on \(\tau\).

The additive constant one is **sharp**: at \(G=K_{3,4}\), \(\lambda=1/3\), \(\tau=1/8\), one has \(L=2\), but \(\delta_{1/3,1/8}(K_{3,4})=3\). Exactly \(31\) minimum source sets occur, with part occupancies \((q,r)=(1,2),(2,1),(3,0)\) contributing \(18,12,1\) sets.

## Assumptions and scope

Only unweighted, undirected simple complete bipartite graphs are claimed, with \(2\le a<b\); the transition matrix is uniform over neighbors. The fidelity is homogeneous with \(0<\lambda<1\). The threshold satisfies \(0<\tau\le1\), including equality boundaries. Source labels within a part are distinguished for counting. The lower bound \(L\) is real-valued and is **not** asserted to be an optimum of a standard linear program; it comes from a particular continuous part-density relaxation. Its integer rounding is exact on the one-sided branch and can miss by one on the balanced branch.

## Proof

**1. Two-level potentials and the exact polynomial.** If \(q\) vertices are selected in the part of size \(a\), and \(r\) in the part of size \(b\), every unselected vertex in each part has a common discounted hitting potential by within-part symmetry. When \(q<a\), \(r<b\), the two potentials \(u,v\) solve
\[
u=\lambda\left(\frac rb+\frac{b-r}{b}v\right),\qquad
v=\lambda\left(\frac qa+\frac{a-q}{a}u\right).
\]
The determinant \(1-\lambda^2(1-s)(1-t)>0\) makes this system uniquely solvable and gives \(u=U_{q,r}\), \(v=V_{q,r}\). Every chosen vertex has potential one. When an entire part is selected, any unselected vertex in the opposite part has potential exactly \(\lambda\), since its neighbors are all selected; no condition is needed on the selected part. This proves the feasibility indicator and the all-set polynomial. If \(\tau>\lambda\), any non-source has potential at most \(\lambda\), so only the full set qualifies.

**2. Lower bound from concavity.** Suppose \(0<\tau<\lambda\) and both parts contain at least one unselected vertex. Let \(s,t\in[0,1)\) be their selected fractions. Subtraction of the two formulas yields
\[
v-u=\frac{\lambda(1-\lambda)(s-t)}{1-\lambda^2(1-s)(1-t)}.
\]
In the half-region \(s\ge t\), the binding condition is \(u\ge\tau\). Define \(C=\tau(1-\lambda^2)\), \(A=\lambda(1-\tau\lambda)\), \(B=\lambda^2(1-\tau)>0\). Rearranging the exact expression for \(u\) gives
\[
s\ge f(t):=\frac{C-At}{B(1-t)}.
\]
Here \(f(0)=\rho\), \(f(\beta)=\beta\), and
\[
f'(t)=\frac{\tau-\lambda}{B(1-t)^2}<0,\qquad
f''(t)=\frac{2(\tau-\lambda)}{B(1-t)^3}<0.
\]
If \(t\ge\beta\), the cost \(as+bt\ge(a+b)\beta\). If \(0\le t<\beta\), feasibility requires \(f(t)\le1\). This restricts \(t\) to an interval with right endpoint \(\beta\), and left endpoint \(0\) when \(\rho\le1\), or the unique point \(t_0>0\) satisfying \(f(t_0)=1\) when \(\rho>1\). The cost is bounded below by the concave function \(af(t)+bt\), whose minimum on the interval is at an endpoint. The right endpoint costs \((a+b)\beta\); the left costs \(a\rho\) if \(\rho\le1\), and at least \(a\) otherwise. Thus \(as+bt\ge\min\{a\min(1,\rho),(a+b)\beta\}\). In the opposite half-region \(t\ge s\) the same argument interchanges \(a,b\); since \(a\le b\), its lower bound is no smaller. When an entire part is selected, the cardinality is at least \(a\), also no smaller than \(L\). Therefore every feasible integer source set has size at least \(K=\lceil L\rceil\).

For \(\tau=\lambda\), a non-source can attain potential \(\lambda\) only if all of its neighbors have potential one; any non-source in each part violates this. Thus the feasible proper sets are exactly those containing an entire part, and \(\delta_{\lambda,\lambda}=a\), which agrees with \(K\).

**3. Rounding and sharpness.** If \(L=a\min(1,\rho)\), pin exactly \(\lceil a\min(1,\rho)\rceil\) vertices of the smaller part. When that number is smaller than \(a\), substituting \(t=0\) into the two-potential formulas verifies \(u\ge\tau\) (and hence \(v\ge u\)); if the entire part is pinned, the opposite potential equals \(\lambda\ge\tau\). Thus this set has size exactly \(K\).

If \(L=(a+b)\beta\), pin \(\lceil a\beta\rceil\) vertices of the first part and \(\lceil b\beta\rceil\) of the second. At fractional occupancies \(s=t=\beta\) the two unselected potentials both equal \(\tau\); adding sources can only increase discounted first-hitting probabilities. This choice therefore qualifies and has size at most \(\lceil(a+b)\beta\rceil+1=K+1\). The polynomial's coefficient at \(z^K\) decides which of these two sizes is optimal, and its lowest nonzero coefficient counts all optimizers.

For \(K_{3,4}\) with \(\lambda=1/3\) and \(\tau=1/8\), the formula gives \(\beta=2/7\), \(\rho=8/7\), \(L=2\). The two-source occupancy possibilities \((0,2),(1,1),(2,0)\) all fail one of the exact rational inequalities. Three-source profiles \((1,2),(2,1),(3,0)\) qualify and their binomial counts add to \(\binom31\binom42+\binom32\binom41+1=31\). Thus the additive bound cannot be reduced.

**4. Aspect-ratio transition.** For \(\tau\le\lambda^2\), \(\rho\le1\) and the two real candidate costs are \(a\rho\) and \((a+b)\beta\). Their comparison using \(\rho/\beta=(1+\lambda)/\lambda\) is exactly \(b/a\gtreqless1/\lambda\). For \(\tau>\lambda^2\), \(\rho>1\), so the one-sided cost is \(a\); solving \(a=(a+b)\beta\) gives the stated \(\tau_*\). This completes all boundary cases.

## Verification

The standalone Python 3 checker `verify_biclique.py` uses `fractions.Fraction` throughout. Its independent graph-level calculation builds the full pinned transition system on explicitly labeled vertices and solves by rational Gauss–Jordan elimination, independently of the two-part reduction. It checks exact coefficient agreement on \(1,860\) labeled subset instances and \(11,160\) threshold comparisons, and checks the relaxation/rounding bound on \(4,770\) rational parameter instances. It also confirms the strict one-vertex integrality gap and \(31\) minimum placements in \(K_{3,4}\). Run `python3 verify_biclique.py`; the recorded output is in `verification_output.txt`.

## Relationship to prior work

The strict unequal-part condition \(2\le a<b\) is essential to the claim scope. Balanced bicliques are excluded; the star family \(a=1\) is likewise excluded because it is treated in the initiating manuscript. The result concerns the unequal-size aspect-ratio dependence, the sharp one-additive bound and the all-set profile across genuinely unbalanced bicliques.

Allagan, Pereyra and Massey (2026, arXiv:2609.31535v1) introduced the minimum-size discounted hitting floor, its exact general mixed-integer formulation, and formulas for stars, complete graphs and spiders. Those definitions and the standard pinned linear equations are reused rather than claimed as new. Their Sections 6–8 do not give the complete bipartite all-set polynomial, the shape of this continuous bound, the threshold-independent aspect-ratio boundary, or its sharp one-additive rounding law. Guo et al. (2024) study computation of group hitting probabilities for specified/queried targets; Li et al. (2014) study finite-horizon random-walk aggregate objectives. Neither published description gives the present universal floor on complete bipartite graphs. Exact biclique random-walk formulas alone also do not imply this optimization and optimizer-count theorem.

## Limitations

The claim excludes both the balanced family \(a=b\) and stars \(a=1\). The quantitative law depends on complete bipartite symmetry and cannot be inferred for arbitrary bipartite graphs. The bounds become exact via the coefficient test only after evaluating up to \(O(ab)\) part-occupancy pairs; there is no claim of a single floor-function formula for the balanced branch. The displayed real relaxation is not asserted to be a traditional LP relaxation, and no claim is made about weighted or heterogeneous walks. The motivating manuscript was inspected directly; equivalent results in unindexed research or inaccessible primary texts remain an originality risk. Computational verification is finite and does not replace the universal concavity proof. Independent external validation has not been performed.

## References

1. Julian D. Allagan, Kevin Pereyra, and William A. Massey, *Discounted Hitting Domination on Graphs with Submodularity, Complexity and Exact Algorithms*, arXiv:2609.31535v1 (first posted 2026-09-25), https://arxiv.org/pdf/2609.31535v1.
2. Qintian Guo, Dandan Lin, Sibo Wang, Raymond Chi-Wing Wong, and Wenqing Lin, *Efficient Algorithms for Group Hitting Probability Queries on Large Graphs*, IEEE TKDE 36 (2024), 2995–3008, doi:10.1109/TKDE.2023.3349164.
3. Rong-Hua Li, Jeffrey Xu Yu, Xin Huang, and Hong Cheng, *Random-walk domination in large graphs*, ICDE 2014, 736–747; arXiv:1302.4546.
