# The sharp \(n-1\) winner-switch bound for one-edge opinion seeding

## Finding
For every finite \(n\)-vertex nonnegatively weighted directed network with unit anchoring and fixed innate opinions \(s_i\in[0,1]\), consider the Friedkin–Johnsen equilibrium as the weight \(t\ge0\) of **just one** directed influence edge increases from zero. At each \(t\), change the innate opinion of exactly one vertex to zero so as to minimize the average equilibrium opinion. Among successive open intervals on which the optimal vertex is unique, the identity of the optimum changes at most \(n-1\) times. For every integer \(n\ge4\), the bound is attained: an explicit directed acyclic network and fixed rational innate opinions have precisely \(n-1\) finite positive switch points and every vertex is, in turn, the unique optimum on a nonempty open interval. Thus a single growing social tie can cause arbitrarily many optimal-seed reversals as network size increases, although no vertex can return as a strict optimum after losing it.

Here a **genuine switch** means two different vertices are uniquely optimal on the two sides of a transition. Ties at isolated parameters are allowed and do not count as additional switches. Deliberately changing a tie-breaker between equal-score candidates does not count.

## Assumptions and scope
Write \(w_{ij}\ge0\) for the weight of the directed edge \(i\to j\), interpreted as **agent \(i\) listening to agent \(j\)**. The row Laplacian is \(L_{ii}=\sum_{j\ne i}w_{ij}\) and \(L_{ij}=-w_{ij}\). With innate opinions \(s\in[0,1]^n\), the equilibrium is the unique vector
\[
z=(I+L)^{-1}s,
\]
so that \(z_i=(s_i+\sum_jw_{ij}z_j)/(1+\sum_jw_{ij})\). The selection criterion is the reduction in \(n^{-1}\sum_i z_i\) when one \(s_j\) is replaced by zero; thus its score is \(s_j\sum_i [(I+L)^{-1}]_{ij}/n\). No arc other than the prescribed \(a\to b\) changes, and innate opinions remain fixed while \(t\) varies. The existing weight of \(a\to b\) at \(t=0\) is zero. There is no connectivity or symmetry requirement.

For the attaining family fix an integer \(m=n-2\ge2\), take vertices \(a,b,v_0,\ldots,v_{m-1}\), and set
\[
\varepsilon=\frac1{10m^4},\quad \alpha_i=m^2-i^2,\quad\beta_i=i\varepsilon,\quad A=\sum_{i=0}^{m-1}\alpha_i,\quad B=\sum_{i=0}^{m-1}\beta_i.
\]
There are fixed arcs \(a\to v_i\) of weights \(\alpha_i\), fixed arcs \(b\to v_i\) of weights \(\beta_i\) whenever \(\beta_i>0\), and a variable arc \(a\to b\) of weight \(t\). The vertices \(v_i\) have no outgoing arcs. Define
\[
T_i=\frac{(1+B)(2i+1)}{2\varepsilon}-\frac{1+A}{2}\quad(0\le i\le m-2),
\]
\[
\delta=\left(1+A+m^2+\frac{T_0}{2}\right)^{-1},\qquad
\kappa=\frac{1+B+2(m-1)\varepsilon+2\varepsilon^2}{2}.
\]
Assign innate opinions \(s_a=1\), \(s_{v_i}=\delta\) for all leaves, and \(s_b=\delta\kappa\). These are fixed rational numbers in \((0,1]\).

## Proof
**Universal upper bound.** Let \(M=I+L(0)\), \(H=M^{-1}\), and write \(e_i\) for coordinate vectors. Changing the single edge gives
\[
M(t)=M+t e_a(e_a-e_b)^\top.
\]
The inverse \(H\) exists and is entrywise nonnegative: each row of \(M\) is a strictly diagonally dominant nonsingular \(M\)-matrix. Put \(x=He_a\). This solves \(x_a=1+\sum_jw_{aj}(x_j-x_a)\), whereas for every \(i\ne a\), \(x_i=\sum_jw_{ij}x_j/(1+\sum_jw_{ij})\). Because \(x\ge0\) and \(x_a>0\), a global positive maximum of \(x\) is attainable only at \(a\); therefore \(d=x_a-x_b>0\). The Sherman–Morrison identity gives
\[
M(t)^{-1}=H-u(t)He_a(e_a-e_b)^\top H,
\qquad u(t)=\frac{t}{1+dt}.
\]
The function \(u\) is strictly increasing on \([0,\infty)\). For every vertex \(j\), the seed score is
\[
G_j(t)=\frac{s_j}{n}\left(\mathbf1^\top He_j-u(t)(\mathbf1^\top He_a)(H_{aj}-H_{bj})\right),
\]
which is affine in the **same** scalar \(u(t)\). If one affine function is strictly above all others at two parameter values, it is strictly above every competitor between them (the difference is affine). Accordingly each vertex occupies at most one interval of unique optimality, and no more than \(n\) distinct unique optimizers, hence no more than \(n-1\) genuine changes, can occur. The argument also handles persistent exact ties by counting only strict-optimizer intervals.

**Attainment.** For the acyclic family, solving backward from its sinks gives
\[
z_{v_i}=s_{v_i},\quad
z_b=\frac{s_b+\sum_i\beta_i s_{v_i}}{1+B},\quad
z_a=\frac{s_a+\sum_i\alpha_i s_{v_i}+t z_b}{1+A+t}.
\]
Multiplying all single-vertex seed scores by the same positive factor \(n(1+A+t)\), the candidate \(a\) has score line \(\ell_a(t)=1\), the leaf \(v_i\) has score line
\[
\ell_i(t)=\delta\left((1+A)\left(1+\frac{\beta_i}{1+B}\right)+\alpha_i+t\left(1+\frac{2\beta_i}{1+B}\right)\right),
\]
and the candidate \(b\) has score line
\[
\ell_b(t)=\frac{\delta\kappa}{1+B}(1+A+2t).
\]
The slopes are **strictly increasing** in the ordering \(a,v_0,v_1,\ldots,v_{m-1},b\), since \(\beta_i=i\varepsilon\) and the choice of \(\kappa\) makes \(\ell_b' -\ell_{m-1}'=2\delta\varepsilon^2/(1+B)>0\). The crossing of \(\ell_a\) with \(\ell_0\) occurs exactly at \(T_0/2\); that of \(\ell_i\) with \(\ell_{i+1}\) occurs exactly at \(T_i\). Finally \(\ell_{m-1}\) crosses \(\ell_b\) at
\[
T_* =\frac{(1+B)((1+A)/2+\alpha_{m-1})-(1+A)\varepsilon^2}{2\varepsilon^2}.
\]
The first crossing is positive, since \(\varepsilon(1+A)<1+B\) (indeed \(A\le m^3\) and \(\varepsilon(1+m^3)<1\) for \(m\ge2\)). Adjacent leaf crossings obey \(T_{i+1}-T_i=(1+B)/\varepsilon>0\). The final crossing satisfies
\[
2\varepsilon^2(T_*-T_{m-2})=(1+B)\left(\frac{1+A}{2}+\alpha_{m-1}-\varepsilon(2m-3)\right)>0.
\]
The last inequality holds because \(\alpha_{m-1}=2m-1\) and \(\varepsilon(2m-3)<1\). Hence
\[
0<T_0/2<T_0<T_1<\cdots<T_{m-2}<T_*<\infty.
\]
For affine lines listed in strictly increasing slope order, if all adjacent intersection abscissae increase strictly, then their pointwise maximum visits every line in that order, on a nonempty open interval. Indeed, the intersection abscissa of any two nonadjacent lines is a positive weighted average of the consecutive intersection abscissae between them, with weights given by their positive slope differences. It therefore cannot eliminate any line from the upper envelope. Applying this fact gives precisely the unique optimal sequence
\[
a,\ v_0,\ v_1,\ldots,\ v_{m-1},\ b,
\]
with \(m+1=n-1\) strictly ordered finite positive crossings, proving sharpness.

Finally, \(\delta\in(0,1)\); and \(0<\kappa<1\) follows from \(B\le1/(20m^2)\), \(2(m-1)\varepsilon\le1/(5m^3)\), and \(2\varepsilon^2\le1/(50m^8)\), whose sum is less than one for all \(m\ge2\). Thus all asserted innate opinions are admissible.

## Verification
The standalone file `verify.py` uses exact `fractions.Fraction` arithmetic to construct the weighted network for each \(2\le m\le17\), independently invert its equilibrium matrix with rational Gauss–Jordan elimination, check the closed-form candidate scores, and test strict optimizers between every adjacent pair of crossings. It also checks the symbolic crossing formulas and their order. Running `python verify.py` prints `ALL_EXACT_RATIONAL_CHECKS_PASSED`. These finite checks supplement, but do not replace, the preceding all-\(m\) proof.

At the smallest case \(n=4\) (\(m=2\)), the construction takes \(\varepsilon=1/160\), \(\delta=4/201\), \(\kappa=13041/25600\), with three exact switching weights \(153/4\), \(153/2\), and \(90156\). The optimal intervention progresses through \(a,v_0,v_1,b\).

## Relationship to prior work
Sun and Zhang, *Opinion Optimization in Directed Social Networks* (arXiv:2306.16847, first publicly submitted 2023-06-29), Theorem 4.1, proves that at a fixed network the optimal one-vertex opinion-reduction intervention maximizes innate opinion times column-sum structure centrality. That fixed-network result does **not** give the number of optimal-intervention changes as one edge is continuously reweighted, nor a family attaining the maximal number of changes. The present result applies the same objective to the standard nonnegative weighted-arc extension, proves a universal parametric switch bound, and constructs a matching sharp acyclic family.

Shrinate and Tripathy, *Towards influence centrality: where to not add an edge in the network?* (arXiv:2412.20112, first publicly submitted 2024-12-28), study how edge reallocation changes the comparative influence of **two stubborn agents** on strongly connected networks. Their intervention operation, candidate set, and conclusions do not imply the \(n-1\) strict-winner progression for arbitrary-vertex single-seed choice under one variable link. Lu et al., *Fairness-Aware Opinion Seeding in Undirected Signed Friedkin–Johnsen Networks* (2026), optimize group fairness in a fixed undirected signed graph rather than count parametric winners. The later *Influence Enhancement in Opinion Dynamics Using Edge Modification: A Kron Reduction-Based Approach* (arXiv:2609.13895) is another potentially relevant edge-modification study; only its accessible abstract and summaries were available, so whole-document exclusion is not claimed.

## Limitations
The universal bound counts distinct **strict** single-seed winners; arbitrary tie-breaking among identically scoring seeds can manufacture spurious changes. Only one edge weight varies, and all innate opinions are fixed. The maximizing family uses rational heterogeneous initial opinions and a directed acyclic network. The statement does not address multiple simultaneous interventions, signed or time-varying arcs, alternative opinion objectives such as polarization, or a fixed upper bound on total edge-weight budget. The example's last switch may occur at a large but finite weight. Existing broader or unindexed sensitivity results could in principle contain an equivalent statement; searches alone do not establish novelty.

## References
1. H. Sun and Z. Zhang, *Opinion Optimization in Directed Social Networks*, arXiv:2306.16847v1 (2023), https://arxiv.org/html/2306.16847v1; particularly Section 4.3, Theorem 4.1.
2. A. Shrinate and T. Tripathy, *Towards influence centrality: where to not add an edge in the network?*, arXiv:2412.20112v1 (2024), https://arxiv.org/html/2412.20112v1; especially Sections III, V, and VII.
3. Z. Lu et al., *Fairness-Aware Opinion Seeding in Undirected Signed Friedkin–Johnsen Networks*, Mathematics 14(19), 3478 (2026), https://doi.org/10.3390/math14193478.
4. A. Shrinate et al., *Influence Enhancement in Opinion Dynamics Using Edge Modification: A Kron Reduction-Based Approach*, arXiv:2609.13895 (2026), https://arxiv.org/abs/2609.13895 (abstract available; full text not inspected).
