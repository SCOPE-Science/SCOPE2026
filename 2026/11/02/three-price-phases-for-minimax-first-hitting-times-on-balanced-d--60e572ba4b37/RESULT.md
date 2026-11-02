# Three price phases for minimax first-hitting times on balanced double stars

## Finding

Let \(m\ge2\), \(B>0\), and \(P,Q,R>0\). Form a double-star tree with two adjacent hubs, each joined to exactly \(m\) pendant leaves. Every undirected edge \(e\) has an independently selectable positive rate \(w_e\); the continuous-time Markov generator has \(q_{uv}=q_{vu}=w_e\) on that edge, diagonal entries chosen for zero row sums, and no other transitions. Each left-spoke rate costs \(P\), each right-spoke rate costs \(Q\), and the bridge rate costs \(R\). The budget is \(\sum_e p_e w_e\le B\). Minimize the greatest mean first-hitting time \(T(w)=\max_{u\ne v}\mathbb E_u\tau_v\).

Write \(N=2m+2\), \(H=\max(P,Q)\), \(L=\min(P,Q)\), and \(S=\sqrt{mL}+\sqrt{R(m+1)}\). Call the higher-priced spokes *expensive*, and the others *cheap* (when \(P=Q\), either designation is valid). Set
\[
H_1=(N-1)L,\qquad H_2=\frac{N-1}{m}S^2=(N-1)\left(\sqrt L+\sqrt{\frac{R(m+1)}m}\right)^2.
\]
Then the **unique global optimizer among all independent edge rates** is constant on each spoke class. Write its expensive-spoke, cheap-spoke, and bridge rates as \(a=1/x\), \(b=1/y\), \(c=1/z\), respectively. Precisely one of the following formulas (with agreement at their shared boundaries) applies:

**Equal-spoke phase, \(H\le H_1\).** Put \(W=\sqrt{mN(H+L)}+\sqrt{R(m+1)}\). Then
\[
x=y=\frac{W}{B}\sqrt{\frac{m(H+L)}{N}},\quad z=\frac WB\sqrt{\frac R{m+1}},\quad T_* =\frac{W^2}{B}.
\]
Both spoke classes have the same optimal rate, even though their prices may be different. The boundary \(H/H_1=1\) is independent of the bridge price.

**Directed-crossing phase, \(H_1<H<H_2\).** Put \(W=\sqrt{mH(N-1)}+\sqrt{mL}+\sqrt{R(m+1)}\). Then
\[
x=\frac WB\sqrt{\frac{mH}{N-1}},\quad y=\frac WB\sqrt{mL},\quad z=\frac WB\sqrt{\frac R{m+1}},\quad T_* =\frac{W^2}{B}.
\]
Only hitting from a cheap leaf to an expensive leaf is maximal.

**Within-class/crossing phase, \(H\ge H_2\).** Put \(C=mH+S^2\). Then
\[
x=\frac CB,\quad y=\frac CB\frac{\sqrt{mL}}S,\quad z=\frac CB\frac{\sqrt{R/(m+1)}}S,\quad T_*=\frac{NC}{B}.
\]
Hitting between two expensive leaves and hitting from a cheap leaf to an expensive leaf tie at the optimum. At \(H=H_2\), the formulas in the last two phases coincide.

For a fully rational illustration, take \(m=2\), \(Q=1\), and \(R=2/3\). The two exact price thresholds are \(H_1=5\) and \(H_2=20\). At \(P=5\) and \(B=98\), all spokes have optimal rate \(7\), the bridge has rate \(21\), and \(T_*=1\). At \(P=30\) and \(B=68\), the expensive spokes have rate \(1\), the cheap spokes rate \(2\), the bridge rate \(6\), and \(T_*=6\).

## Assumptions and scope

All edge rates are symmetric in their two orientations, strictly positive, and chosen independently before optimization; hence the stationary distribution is uniform, irrespective of vertex degree. There are exactly \(m\) left and \(m\) right leaves, with \(m\ge2\). Price is fixed within each leaf class, and the bridge has its own positive price. The objective is the maximum over **ordered pairs** of states; it is not commute time, resistance diameter, the discrete-time degree-normalized random walk, or spectral mixing time. The budget is linear in transition rates, not in their reciprocals.

## Proof

**Tree identity.** For any finite tree whose generator has symmetric edge rates \(w_e>0\), let \(e\) be oriented toward a fixed target along the source-to-target path. Removing \(e\) leaves a component containing the source, of size \(s_e\). Solving the Dirichlet first-step equations \(\sum_{v\sim u}w_{uv}(h(u)-h(v))=1\) away from the target, and summing over this source component, shows that the voltage drop from the source side to the target side across \(e\) is \(s_e/w_e\). Telescoping gives
\[
\mathbb E_u\tau_v=\sum_{e\in\mathrm{path}(u,v)}\frac{s_e}{w_e}.
\]
Appending a terminal edge to either end of a path increases this hitting time, so a maximal ordered pair can be taken as two distinct leaves.

**Four canonical leaf-pair averages.** For a general, potentially nonuniform allocation, let \(a_i\) denote expensive-spoke rates, \(b_i\) cheap-spoke rates, and \(c\) the bridge rate. Put \(x=m^{-1}\sum_i a_i^{-1}\), \(y=m^{-1}\sum_i b_i^{-1}\), and \(z=c^{-1}\). Average hitting times over all ordered distinct leaf pairs within a class, and over all ordered pairs between the classes. The four averages are exactly
\[
Nx,\quad Ny,\quad x+(N-1)y+(m+1)z,\quad (N-1)x+y+(m+1)z.
\]
Thus the largest hitting time is at least their maximum \(F(x,y,z)\), with equality for classwise constant rates. The exact labels of the two crossing averages depend on direction; the one with coefficient \(N-1\) on \(x\) is from a cheap leaf to an expensive leaf.

**Global lower certificate.** Any convex combination of these four averages is a lower bound for \(T\). Write the combination as \(\alpha x+\beta y+\gamma z\), with strictly positive coefficients. Since the individual cost is \(H\) on each expensive spoke, \(L\) on each cheap spoke, and \(R\) on the bridge, Cauchy--Schwarz gives the universal bound
\[
T\ge\alpha x+\beta y+\gamma z\ge
\frac{\left(\sqrt{mH\alpha}+\sqrt{mL\beta}+\sqrt{R\gamma}\right)^2}{B}.
\]
Equality in this last inequality forces every rate in either leaf class to coincide, because all coefficients are positive. The proof now constructs a matching convex-combination certificate in each phase.

**Phase I.** Let \(\theta=(NH/(H+L)-1)/(N-2)\). If \(H\le(N-1)L\) (and \(H\ge L\) by definition), then \(0\le\theta\le1\). Combine the crossing average \((N-1)x+y+(m+1)z\) with weight \(\theta\) and its reverse with weight \(1-\theta\). The resulting coefficients are \(\alpha=NH/(H+L)\), \(\beta=NL/(H+L)\), and \(\gamma=m+1\). The Cauchy lower bound becomes \(W^2/B\). Its equality conditions give the displayed \(x=y\) and \(z\); at that point both crossing averages equal \(Nx+(m+1)z\), strictly exceeding both within-class averages. Hence the lower bound is attained.

**Phase II.** Use the single cheap-to-expensive crossing average, giving \((\alpha,\beta,\gamma)=(N-1,1,m+1)\). Cauchy equality gives the displayed three reciprocal rates and bound \(W^2/B\). The inequality \(x\ge y\) is exactly \(H\ge(N-1)L\), so this crossing direction dominates the reverse. Its dominance over the within-expensive-leaf average \(Nx\) is exactly
\[
x-y\le(m+1)z\quad\Longleftrightarrow\quad H\le\frac{N-1}{m}S^2=H_2.
\]
It then dominates \(Ny\) too. For \(H_1<H<H_2\) these inequalities are strict, so only the specified crossing direction is maximal.

**Phase III.** Let \(\eta=[mH-(N-1)S^2]/[mH+S^2]\). Under \(H\ge H_2\), \(0\le\eta<1\). Combine the within-expensive-leaf average \(Nx\) with weight \(\eta\) and the cheap-to-expensive crossing average with weight \(1-\eta\). The resulting coefficients are
\[
\alpha=N-1+\eta,\quad\beta=1-\eta,\quad\gamma=(m+1)(1-\eta).
\]
Its Cauchy equality conditions reduce to \(x=C/B\), \(y=(C/B)\sqrt{mL}/S\), and \(z=(C/B)\sqrt{R/(m+1)}/S\), satisfying \(x=y+(m+1)z\). The active within-class and crossing averages both equal \(Nx\); the other two averages cannot be larger because \(x\ge y\). The Cauchy certificate attains \(NC/B\), proving optimality. At both thresholds the adjacent formulas agree directly.

**Uniqueness and budget saturation.** In every phase the matching certificate has strictly positive coefficient on the reciprocal of every individual edge. Equality in Cauchy--Schwarz consequently determines every individual conductance uniquely, including at both phase boundaries. A solution cannot leave budget unspent: increasing all rates by a common factor strictly decreases all hitting times. This completes the unrestricted proof.

## Verification

Run `python3 verify.py` with Python 3, NumPy and SymPy installed. It reconstructs full absorbing continuous-time Markov-chain systems exactly for 12 rational examples, separately checks 720 randomly selected budgets/price vectors against 720 positive dual certificates and 8,640 nonuniform full-edge allocations, and checks 48 comparisons straddling the two phase surfaces. The checks were replayed from the standalone source. The symbolic proof above, not finite testing, establishes the general theorem.

## Relationship to prior work

H. Xu and S.-T. Yau, *An explicit formula of hitting times for random walks on graphs* (public arXiv submission on 2013-11-30), develops hitting-time formulas for degree-normalized discrete-time random walks and covers tree/cutpoint methods. This supplies hitting-time background, but it is not a rate-budget minimax theorem for uniform-stationary continuous-time chains. A. Ghosh, S. Boyd and A. Saberi, *Minimizing Effective Resistance of a Graph*, study sum-of-pair resistances and their optimal allocation on trees, and mention maximum resistance as a separate convex problem. Neither their average-resistance objective nor resistance diameter is equivalent to the **maximum oriented hitting time** here. M. Fiedler's 1993 *Some minimax problems for graphs* addresses absolute graph characteristics including weighted tree diameter; its available abstract does not report the oriented first-passage result, but full-text priority comparison remains a limitation.

The nearest adjacent design problems concern paths, single-hub stars, and double-star resistance design. These do not imply the full three-region transition for directed mean hitting times across a bridge with independently priced spoke classes. This difference rests on the directional crossing coefficients \(1\) and \(N-1\), and on the within-class competition, rather than a changed name or parameter.

## Limitations

The theorem does not cover unequal leaf counts, varying prices within a spoke class, nonsymmetric transition generators, nonuniform stationary probabilities, or general trees. It concerns mean first-hitting times, not their distributions, mixing time, or rate variance. Independent specialist priority checking is desirable, especially for older weighted-tree minimax literature; published searches are not a proof of absolute novelty. The numerical verifier checks finite cases only. An independent mathematical audit has not been performed.

## References

1. H. Xu and S.-T. Yau, *An explicit formula of hitting times for random walks on graphs*, arXiv:1312.0065, submitted 2013-11-30. https://arxiv.org/abs/1312.0065
2. A. Ghosh, S. Boyd and A. Saberi, *Minimizing Effective Resistance of a Graph*, SIAM Review 50 (2008), 37--66, doi:10.1137/050645452. Preprint: https://www.stat.berkeley.edu/~aldous/206-RWG/RWGpapers/ghosh_boyd.pdf
3. M. Fiedler, *Some minimax problems for graphs*, Discrete Mathematics 121 (1993), 65--74. https://dblp.org/rec/journals/dm/Fiedler93
