# Exact all-budget noise-free leader selection on clique coronas

## Finding
Let \(n\ge3\) be an integer and let \(H_n=K_n\circ K_1\) be the unweighted graph obtained by attaching one private leaf \(\ell_i\) to every core vertex \(v_i\) of an \(n\)-vertex clique. For each integer budget \(1\le b\le2n-1\), a leader set \(S\) has exactly \(b\) distinct vertices. Let \(L\) be the original unweighted combinatorial Laplacian and minimize the noise-free follower-coherence objective
\[
J(S)=\operatorname{tr}\bigl(L_{V(H_n)\setminus S,V(H_n)\setminus S}^{-1}\bigr).
\]
All optimal sets are classified as follows. Define
\[
P_n(b)=nb^2+(2n^2+3n+2)b-2n(n+1)^2.
\]
For \(1\le b\le n\):

- If \(P_n(b)<0\), an optimal set consists of exactly one core vertex and \(b-1\) leaves, none paired with that core and all on distinct remaining pairs. Every such set is optimal, and there are exactly \(n\binom{n-1}{b-1}\) of them.
- If \(P_n(b)>0\), an optimal set consists of exactly \(b\) leaves, with no core leaders. Every such set is optimal, and there are exactly \(\binom nb\) of them.

The integer equality \(P_n(b)=0\) **never occurs** for \(n\ge3\) and \(1\le b\le n\); thus the two cases are exhaustive and mutually exclusive. The unique real positive root \(\kappa_n\) of \(P_n\) gives the sharp budget transition, with core selection optimal for \(b<\kappa_n\) and all-leaf selection optimal for \(b>\kappa_n\). Moreover \(\kappa_n/n\to\sqrt3-1\).

For \(n<b\le2n-1\), every optimal set consists of **all \(n\) leaves** and exactly \(b-n\) core vertices; there are \(\binom{n}{b-n}\) such sets. No other leader sets are optimal.

For the smaller-budget regimes, exact optimal costs are \(F_1(n,b)\) or \(F_0(n,b)\), respectively, where
\[
\begin{aligned}
F_0(n,b)={}&n-b+\frac{2(n-b)}n+\frac{b+n}{n+1}+\frac{2(n-b)(n+1)}{nb},\\
F_1(n,b)={}&n-b+1+\frac{2(n-b)}n+\frac{b-1}{n+1}\\
&+\frac{2(n-b)(n+1)}{n(n+b)}+\frac{n(b-1)}{(n+1)(n+b)}.
\end{aligned}
\]
For \(n<b\le2n-1\), the minimum is
\[
F_+(n,b)=\frac{2n-b}{n+1}+\frac{2n-b}{(n+1)(b-n+1)}.
\]

## Assumptions and scope
All edges have conductance one and all vertices have unit follower noise variance. Leaders are perfectly grounded; the optimization uses the **original** Laplacian principal submatrix, without recalculating follower degrees. The objective is exactly the inverse trace, not a factor-of-two or vertex-average normalization. The graph is simple and undirected. The case \(b=2n\) has no followers and is excluded by convention. No claim is made for other core graphs, weighted edges, or finite leader gain.

## Proof
**1. Four pair statuses and exact grounded trace.** Every core–leaf pair \((v_i,\ell_i)\) has one of four states. Write \(u\) for neither endpoint a leader, \(x\) for core-only leader, \(c\) for leaf-only leader, and \(y\) for both endpoints leaders. Then
\[
u+x+c+y=n,\qquad b=x+c+2y.
\]
For each of the \(x\) core-only leader pairs, the ungrounded leaf is an isolated follower block of degree one and contributes one to the trace. For the other pairs, eliminate the \(u\) ungrounded leaves by a Schur complement. The resulting grounded core matrix is \(D-\mathbf 1\mathbf1^{\mathsf T}\), where \(D\) is diagonal with \(u\) entries \(n\) and \(c\) entries \(n+1\). Set
\[
\delta=1-\frac un-\frac c{n+1}>0.
\]
By the rank-one inverse identity, each of the \(u\) core diagonal inverse entries is \(1/n+1/(n^2\delta)\), and each of the \(c\) entries is \(1/(n+1)+1/((n+1)^2\delta)\). The leaf–core block inversion adds one plus another core inverse diagonal for each ungrounded leaf. Consequently the **complete** trace formula for every legal leader set is
\[
\boxed{J(u,x,c,y)=u+x+\frac{2u}{n}+\frac c{n+1}+
\frac{2u/n^2+c/(n+1)^2}{1-u/n-c/(n+1)}.}
\tag{1}
\]
If \(u=c=0\), interpret the last fraction as zero and formula (1) as \(J=x\), consistent with the empty grounded core block. Positivity of \(\delta\) when \(u+c>0\) follows from the positive definiteness of the grounded Laplacian and the Schur complement, or directly from \(b\ge1\).

**2. Excluding simultaneous empty and fully grounded pairs.** Suppose \(u,y\ge1\). Move a leader from a fully grounded pair to an empty pair, converting the two states into one core-only and one leaf-only pair. Counts change by
\[
(u,x,c,y)\mapsto(u-1,x+1,c+1,y-1).
\]
The \(u+x\) term is unchanged. The term \(2u/n+c/(n+1)\) strictly decreases by \(2/n-1/(n+1)>0\). In the final fraction of (1), its nonnegative numerator strictly decreases by \(2/n^2-1/(n+1)^2>0\), while its positive denominator strictly increases by \(1/(n(n+1))\). Thus this feasible exchange strictly lowers \(J\). Therefore an optimum has \(u=0\) or \(y=0\).

**3. Budgets at most \(n\).** Since \(u=n-b+y\), an optimum with \(b\le n\) must have \(y=0\). Hence \(u=n-b\), \(c=b-x\), and the cost reduces to a function \(f(x)\), with integer \(0\le x\le b\), given by formula (1). Direct differentiation yields
\[
f''(x)=\frac{2n(2n^2+2n-bn-2b)}{(b+nx)^3}>0
\qquad(0\le x\le b,\; b\le n).
\]
For \(b\ge2\), exact subtraction gives
\[
f(2)-f(1)=
\frac{b^2n+4bn^2+3bn+2b-4n^2-2n}
{(b+n)(b+2n)(n+1)}>0.
\]
The last numerator is positive because its value at \(b=2\) is \(4(n+1)^2>0\) and it increases in \(b\ge2\). Strict convexity then makes every integer \(x\ge2\) strictly inferior to \(x=1\). For \(b=1\), only \(x=0,1\) are possible. Finally,
\[
f(1)-f(0)=\frac{P_n(b)}{b(b+n)(n+1)}.
\]
Thus exactly the two claimed configurations can minimize, selected by the sign of \(P_n(b)\). Substituting \(x=0\) or \(x=1\) into (1) gives \(F_0\) and \(F_1\).

There are no integer ties: modulo \(n\), \(P_n(b)\equiv2b\pmod n\). If \(P_n(b)=0\), then \(n\mid2b\). For odd \(n\) this forces \(b=n\). For even \(n\) it forces \(b=n/2\) or \(b=n\). But
\[
P_n(n)=n^2(n-1)>0,\qquad
P_n(n/2)=-\frac{n(3n^2+10n+4)}4<0.
\]
This eliminates equality. The positive root is
\[
\kappa_n=\frac{-(2n^2+3n+2)+\sqrt{(2n^2+3n+2)^2+8n^2(n+1)^2}}{2n},
\]
and its normalized limit is \(\sqrt3-1\).

**4. Budgets greater than \(n\).** If \(b>n\), feasibility forces \(y>0\), hence the strict exchange in step 2 forces \(u=0\). Then \(y=b-n\) and \(x+c=2n-b\). Substitution into (1) gives
\[
J=(2n-b-c)+\frac c{n+1}+\frac{c}{(n+1)(n+1-c)}.
\]
Its derivative as a continuous function of \(c\in[0,2n-b]\) is
\[
-\frac n{n+1}+\frac1{(n+1-c)^2}<0,
\]
since \(c\le2n-b\le n-1\). Hence the unique minimizing status profile has \(x=0\) and \(c=2n-b\), i.e. every leaf grounded. Substitution gives \(F_+\). Permuting the clique pairs counts the distinct optimal sets in all regimes and completes the proof.

## Verification
Run `python3 verify_corona.py` in an environment with the versions of NumPy and SymPy specified in `requirements.txt`. The program proves six symbolic identities via exact algebra, checks 1,932 exact-rational budget cases over clique sizes \(3\) through \(44\), exhaustively checks 5,432 actual leader subsets over clique sizes \(3\) through \(6\), and independently inverts 468 representative grounded matrices with exact SymPy arithmetic through clique size \(8\). Its full standard output is in `verification_output.txt`. The unbounded theorem follows from the analytical argument above, not from the finite computations.

## Relationship to prior work
Lin, Fardad and Jovanović formulated the noise-free leader-selection optimization through the grounded-Laplacian inverse trace and presented relaxation/greedy algorithms [1]. Fitch and Leonard established joint centrality and special-graph examples such as cycles and paths [2]. Du et al. developed Laplacian spectral formulas for weighted corona-network **leaderless** first-order coherence [3]. Sharma, Adhikari and Mishra studied corona graph spectral structure [4]. These results motivate the object and techniques; none of the inspected portions establishes the present **all-budget** exact optimum, quadratic leader-type phase transition, no-pairing exchange or optimizer counts for the clique corona. The known generic inverse-trace formulation alone does not optimize over the leader sets in this family.

## Limitations
This is an exact result only for unit-weight clique coronas with one private leaf per core and perfectly grounded leaders. The classification does not imply an optimal greedy selection order, nor does it extend automatically to arbitrary weighted coronas. Self-review is not independent mathematical validation. Equivalent results in specialized or incompletely indexed literature remain possible, especially under alternative terms such as sun graphs or pendant-corona consensus networks.

## References
1. F. Lin, M. Fardad and M. R. Jovanović, *Algorithms for Leader Selection in Stochastically Forced Consensus Networks*, arXiv:1302.0450 (first public 2013-02-03), https://arxiv.org/abs/1302.0450.
2. K. E. Fitch and N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569 (first public 2014-07-07), https://arxiv.org/abs/1407.1569.
3. W. Du, J. Zhu, H. Gao and X. Li, *Consensus analysis of the weighted corona networks*, Frontiers in Physics 10:948247 (2022), DOI:10.3389/fphy.2022.948247.
4. R. Sharma, B. Adhikari and A. Mishra, *Structural and Spectral properties of Corona Graphs*, arXiv:1507.05335 (2015), https://arxiv.org/abs/1507.05335.
