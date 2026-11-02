# Three-phase optimal leader allocation for inverse-square coherence on two-hub bipartite networks

## Finding

Let \(K_{2,q}\) be the unit-conductance complete bipartite graph with two hub vertices and \(q\) peripheral vertices. For arbitrary integers \(q\ge k\ge2\), choose exactly \(k\) perfectly grounded, noise-free leaders and minimize
\[
J(S)=\operatorname{tr}\bigl(L_{V\setminus S,V\setminus S}^{-2}\bigr),
\]
where \(L\) is the unnormalized combinatorial Laplacian. Write \(a=|S\cap\{\text{two hubs}\}|\in\{0,1,2\}\) and \(h=q-k\). All placements with the same \(a\) have the same objective, and their exact costs are
\[
\begin{aligned}
J_0(q,k)&=\frac{h-1}{4}+\frac1{q^2}+\frac{q^2+4h+4}{4k^2},\\
J_1(q,k)&=\frac h4+\frac{q^2+2h+6}{(q+k-1)^2},\\
J_2(q,k)&=\frac{h+2}{4}.
\end{aligned}
\]
These formulas remain valid at \(k=q\), including the case of an empty peripheral follower class.

For each real \(k\ge2\), let \(\gamma_k>k\) be the **unique** solution \(J_0(q,k)=J_1(q,k)\) in the real variable \(q\ge k\). For \(k\ge4\), put
\[
\eta_k=k-3+\sqrt{2k^2-4k-2}.
\]
Let \(\zeta_k\ge k\) be the unique solution \(J_0(q,k)=J_2(q,k)\). Then the following is a complete description of **all** minimizers for every integer \(q\ge k\ge2\):

* If \(k=2\) or \(k=3\), the minimizing hub count is \(0\) for \(q<\zeta_k\), and \(2\) for \(q>\zeta_k\), with both counts optimal at equality. One hub is never optimal.
* If \(k\ge4\) and \(\gamma_k<\eta_k\), the minimizing hub count progresses through \(0\), \(1\), and \(2\) at the respective real boundaries \(\gamma_k\) and \(\eta_k\). At the first boundary counts \(0,1\) tie; at the second counts \(1,2\) tie.
* If \(k\ge4\) and \(\gamma_k>\eta_k\), only counts \(0\) and \(2\) can minimize, switching at \(\zeta_k\), with a tie there. If \(\gamma_k=\eta_k\), all three hub counts tie at the common boundary, and counts \(0\) and \(2\) minimize on its respective sides.

A boundary is a tie only if it is an admissible **integer** \(q\); otherwise the strict inequalities determine the integer optimum. Within every minimizing hub-count class, **every** choice of the requisite peripheral vertices is optimal.

The three-phase regime is asymptotically nonempty and has sharp linear-scale boundaries. Let \(\alpha\in(1,2)\) be the unique real solution
\[
\frac{\alpha^2-1}{4}=\frac{\alpha^2}{(\alpha+1)^2},
\qquad \alpha\approx1.5815459579,
\]
and put \(\beta=1+\sqrt2\). Then
\[
\lim_{k\to\infty}\frac{\gamma_k}{k}=\alpha,
\qquad
\lim_{k\to\infty}\frac{\eta_k}{k}=\beta.
\]
Consequently, for each fixed \(c\in(\alpha,\beta)\), every sufficiently large integer \(k\) with \(q/k\to c\) has **exactly one grounded hub** in every optimum; if \(1<c<\alpha\) the optimum has no grounded hubs, and if \(c>\beta\) it has both. A finite exact witness is \((k,q)=(7,11)\), with
\[
(J_0,J_1,J_2)=\left(\frac{8761}{5929},\frac{424}{289},\frac32\right),
\]
so the unique optimal hub count is \(1\); at \((7,12)\) the corresponding values are \((1879/1008,565/324,7/4)\), again with one hub optimal.

## Assumptions and scope

The graph is undirected, unweighted (unit conductance), and has precisely two equivalent hubs adjacent to each of \(q\) equivalent peripherals, with no within-class edges. Every leader is completely grounded and noiseless. The positive definite follower principal Laplacian is used; no pseudoinverse or ungrounded zero mode enters the objective. The leader budget satisfies \(2\le k\le q\), leaving at least two followers. Real critical values are used to express phase boundaries but only integer \(q,k\) correspond to graphs. A second-order consensus system with proportional-Laplacian position and velocity feedback and white acceleration noise has stationary position variance proportional to \(J(S)\) under ideal grounding; no finite leader gain or arbitrary damping law is asserted.

## Proof

**1. Exact spectral reduction.** If \(a\) hubs are grounded, let \(r=2-a\) hubs and \(s=q-k+a\) peripherals remain followers. After classwise ordering the follower Laplacian is
\[
M_{r,s}=\begin{pmatrix}q I_r&-\boldsymbol1_r\boldsymbol1_s^{\mathsf T}\\
-\boldsymbol1_s\boldsymbol1_r^{\mathsf T}&2I_s\end{pmatrix}.
\]
For \(r,s>0\), zero-sum vectors in each class give eigenvalues \(q\) of multiplicity \(r-1\) and \(2\) of multiplicity \(s-1\). The remaining two-dimensional block is
\[
B=\begin{pmatrix}q&-\sqrt{rs}\\-\sqrt{rs}&2\end{pmatrix},
\qquad \det B=2q-rs>0.
\]
A direct inverse gives
\[
\operatorname{tr}(B^{-2})=\frac{q^2+4+2rs}{(2q-rs)^2},
\]
so
\[
J=\frac{r-1}{q^2}+\frac{s-1}{4}+
\frac{q^2+4+2rs}{(2q-rs)^2}.
\]
If \(r=0\), the grounded matrix is \(2I_s\) and \(J=s/4\); if \(s=0\), it is \(qI_r\) and \(J=r/q^2\). Direct substitution in the displayed rational expression agrees in both cases (the negative apparent multiplicities cancel), so it may be used uniformly. Substituting \(r=2-a\) and \(s=q-k+a\) yields exactly the three costs in the Finding.

**2. Single-crossing of each pair.** For fixed \(k\ge2\), use the continuous auxiliary variable \(q\ge k\). Exact subtraction gives
\[
J_1-J_2=\frac{q^2+(6-2k)q+11-2k-k^2}{2(q+k-1)^2},
\]
and
\[
J_0-J_2=\frac{(q+2)^2}{4k^2}-\frac1k-\frac34+\frac1{q^2}.
\]
The numerator of \(J_1-J_2\) is strictly increasing for \(q\ge k\), since its derivative is at least \(6\). At \(q=k\), it is \(-2k^2+4k+11\): positive for \(k=2,3\) and negative for each integer \(k\ge4\). Hence the first two cases have \(J_1>J_2\) throughout, whereas for \(k\ge4\) there is exactly one crossing at \(\eta_k\), with \(J_1<J_2\) below and \(J_2<J_1\) above. Moreover,
\[
\frac{\mathrm d}{\mathrm dq}(J_0-J_2)
=\frac{q+2}{2k^2}-\frac2{q^3}>0
\quad(q\ge k\ge2),
\]
and at \(q=k\), \(J_0-J_2=-(k-2)(k+2)/(2k^2)\le0\), strictly for \(k>2\). The difference tends to infinity with \(q\). Thus \(\zeta_k\) exists and is unique (and \(\zeta_2=2\)).

To verify the remaining single crossing, put \(F_k(q)=J_0-J_1\). Its exact derivative is
\[
F_k'(q)=\frac{q+2}{2k^2}-\frac2{q^3}
-\frac{2((k-2)q+3k-7)}{(q+k-1)^3}.
\]
For \(q\ge k\ge3\), set \(t=k-1\le q\) and observe
\[
\frac{2((k-2)q+3k-7)}{(q+k-1)^3}
\le\frac{2t(q+3)}{(q+t)^3}
\le\frac8{27q}\left(1+\frac3q\right),
\]
using \(\sup_{z\ge0}z/(1+z)^3=4/27\). Because \(k\le q\), this implies
\[
F_k'(q)\ge\frac1q\left(\frac{11}{54}+\frac1{9q}-\frac2{q^2}\right)>0
\qquad(q\ge3).
\]
For \(k=2\) and \(2\le q\le3\), the final term in the exact derivative is positive and the first two terms already have a positive sum; thereafter the preceding bound applies. Finally,
\[
F_k(k)=-\frac{k^4-2k^2+8k-2}{k^2(2k-1)^2}<0,
\qquad \lim_{q\to\infty}F_k(q)=+\infty.
\]
There is therefore exactly one \(\gamma_k>k\), with \(J_0<J_1\) below and \(J_1<J_0\) above.

**3. Every global optimizer and all ties.** If \(k\le3\), \(J_1>J_2\) everywhere, so the unique switch between \(J_0\) and \(J_2\) at \(\zeta_k\) proves the first case. For \(k\ge4\), all pairwise comparisons switch only once. If \(\gamma_k<\eta_k\), then at \(\gamma_k\), \(J_0=J_1<J_2\), and at \(\eta_k\), \(J_1=J_2<J_0\); their sign patterns give the \(0\to1\to2\) classification. If \(\gamma_k>\eta_k\), at \(\eta_k\) we have \(J_0<J_1=J_2\) and at \(\gamma_k\), \(J_2<J_0=J_1\); hence the unique \(J_0=J_2\) crossing lies strictly between them and count \(1\) never minimizes. If the boundaries coincide, all costs agree at that point. The strict comparisons away from the boundaries and the graph automorphisms establish every minimizer and every tie.

**4. Asymptotics and motivation.** Fix \(c>1\) and set \(q/k\to c\). Subtracting the common quantity \((q-k)/4\) from all three costs gives, respectively,
\[
\frac{c^2-1}{4}+o(1),\qquad
\frac{c^2}{(c+1)^2}+o(1),\qquad
\frac12.
\]
The first two limits cross at the unique \(\alpha\in(1,2)\): their difference is strictly increasing for \(c\ge1\), being the function \((c^2-1)/4-c^2/(c+1)^2\) with strictly positive derivative \(c/2-2c/(c+1)^3\). The second and third cross at \(\beta=1+\sqrt2\), with \(\alpha<\beta\). The strict single-crossing results, uniformity of these rational limits on compact ratio intervals, and uniqueness imply \(\gamma_k/k\to\alpha\) and \(\eta_k/k\to\beta\). For every \(c\) strictly between these constants, one hub is therefore the unique optimal hub count for sufficiently large \(k\); the exterior regimes follow similarly. The two exact \(k=7\) witnesses follow by rational substitution.

## Verification

A standalone Python 3 standard-library program, `verify.py`, constructs each actual grounded Laplacian and inverts it using rational Gauss–Jordan elimination, independent of the spectral reduction. Running `python verify.py` gave the embedded `verification.log` with `VERIFY_OK`: 1,920 exhaustive labeled leader-subset comparisons across 28 small parameter pairs, 693 additional class-representative grounded-matrix inverses, and 465 exact pairwise-difference checks. The program additionally verifies the strict one-hub optima at \((k,q)=(7,11),(7,12)\), a one/two-hub tie at \((11,22)\), and the small-budget regime. These checks are finite corroboration, not a proof of the infinitely many parameter cases. The analytical argument above supplies that proof.

## Relationship to prior work

Fitch and Leonard [1] provide the first-order inverse-trace joint-centrality framework and graph examples, not the inverse-square \(K_{2,q}\) phase classification. Mackin and Patterson [2, Theorem 5] derive the inverse-square performance expression for stable second-order consensus with finite absolute-information gains and prove general submodularity and greedy approximation, rather than the present exact ideal-grounding, all-budget bipartite optimizer. Patterson and colleagues [3] analyze weighted paths and cycles, not this two-hub family. The present result does not assert discovery of the grounded inverse-square objective, general spectral reduction, or universal submodularity: it resolves a specific exact allocation question and exhibits a mixed-class optimal phase. Earlier specialized exact biclique results for the inverse-trace objective and for nearly balanced inverse-square leader placement concern different domains; neither gives the three-phase inverse-square law on unbounded \(K_{2,q}\).

## Limitations

Only unit-conductance \(K_{2,q}\), exactly \(2\le k\le q\) ideal grounded leaders, and the unnormalized inverse-square objective are classified. Finite-gain leaders, heterogeneous conductances, different parts sizes, other feedback laws, and all other network topologies are excluded. The real roots describe ties only when integer vertex counts attain them. The leading asymptotic phase law does not assert a uniform finite threshold for every \(k\). Specialized prior coverage may exist despite the documented comparisons, and no claim of publication priority or independent mathematical certification is made.

## References

1. K. E. Fitch and N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569, initial public posting July 7, 2014, https://arxiv.org/abs/1407.1569.
2. E. Mackin and S. Patterson, *Submodularity in Systems with Higher Order Consensus with Absolute Information*, arXiv:1905.09156, first posted May 22, 2019, https://arxiv.org/abs/1905.09156.
3. S. Patterson, N. McGlohon, and K. Dyagilev, *Efficient, Optimal k-Leader Selection for Coherent, One-Dimensional Formations*, arXiv:1412.6595, first posted December 20, 2014, https://arxiv.org/abs/1412.6595.
4. S. Patterson and B. Bamieh, *Leader Selection for Optimal Network Coherence*, IEEE CDC (2010), DOI:10.1109/CDC.2010.5718151.
