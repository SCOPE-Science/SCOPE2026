# Sharp two-leader coupling threshold for a weighted clique barbell

## Finding

Consider a unit-conductance edge joining the two vertices of a clique of order two, and a unit-conductance clique of order \(q\ge3\). Give the single edge connecting the two clique gateways conductance \(t>0\), while retaining conductance one on every edge internal to either clique. Exactly two noise-free leaders are selected to minimize the grounded-Laplacian inverse trace \(J(S)=\operatorname{tr}(L_{FF}^{-1})\), proportional to the total stationary variance of unit-noise followers.

Name the gateway and other vertex of the two-vertex clique \(a,u\), and the gateway and remaining vertices of the larger clique \(b,v_1,\ldots,v_{q-1}\). Write
\[
\tau_q=\frac{q+2}{q-2}.
\]
**For every integer \(q\ge3\) and every real \(t>0\), all minimizing unordered leader pairs are exactly**

- \(\{u,v_i\}\), for every \(1\le i\le q-1\), if \(0<t<\tau_q\);
- these \(q-1\) pairs **and** \(\{u,b\}\), if \(t=\tau_q\);
- the unique pair \(\{u,b\}\), if \(t>\tau_q\).

There are no other ties. In particular, the two-vertex-clique gateway \(a\) is never a leader in an optimum. The minimum of the inverse-trace objective is
\[
\min\left\{
\frac{2q^2t+3q^2+3qt-2q-6t}{q(qt+q+2t)},
\frac{2qt+3q-2t-2}{q(t+1)}
\right\}.
\]
If the bridge conductance does not exceed one, the larger-clique non-gateway remains optimal for every finite \(q\); if \(t>1\) is fixed, the larger-clique gateway becomes optimal for every integer \(q>2(t+1)/(t-1)\), with an equality tie only at an integral boundary.

## Assumptions and scope

The graph has \(q+2\) vertices and consists of disjoint \(K_2\) and \(K_q\) together with exactly one interclique edge \(ab\). Each internal edge has positive conductance one, and \(ab\) has conductance \(t>0\). There are two distinct, perfectly anchored/noise-free leader vertices. All follower nodes have independent, equal-intensity additive white noise and obey continuous-time linear consensus. The weighted combinatorial Laplacian is \(L\), and \(L_{FF}\) is its principal submatrix on followers \(F=V\setminus S\). Because the graph is connected and the leader set is nonempty, \(L_{FF}\) is positive definite. If follower noise covariance is the identity, the actual stationary covariance trace is \(J(S)/2\), so minimizing \(J\) and variance are equivalent; the displayed formulas concern \(J\) rather than the half-scaled variance.

Here a gateway means the unique endpoint of the bridge in a given clique; a non-gateway is any other clique vertex. The graph has automorphism group exchanging the larger clique's \(q-1\) non-gateway vertices. There are exactly seven leader-pair orbits when \(q\ge3\).

## Proof

**Step 1: reduction to seven exact rational costs.** Denote the seven types by \(GG=\{a,b\}\), \(GN=\{a,v_1\}\), \(NG=\{u,b\}\), \(NN=\{u,v_1\}\), \(AA=\{a,u\}\), \(BV=\{b,v_1\}\), and \(VV=\{v_1,v_2\}\). Every unordered pair belongs to precisely one of these types by clique symmetry.

For any type let \(k\) be the number of follower vertices among the larger clique's non-gateways. On their contrast subspace, the grounded Laplacian equals \(qI\); its contribution to the inverse trace is \((k-1)/q\) when \(k\ge1\). On the remaining subspace, use the basis formed by the available individual follower coordinates \(a,u,b\), and, when \(k\ge1\), the normalized sum of those \(k\) non-gateways. The resulting matrix is obtained by deleting leader rows/columns from
\[
M_k=\begin{pmatrix}
1+t&-1&-t&0\\
-1&1&0&0\\
-t&0&q-1+t&-\sqrt{k}\\
0&0&-\sqrt{k}&q-k
\end{pmatrix}.
\]
The constant-sum coordinate of the large clique is omitted if \(k=0\); in that case the trace is computed on the remaining coordinates alone. The only instance of \(k=0\) is \(q=3\) with the \(VV\) type. All diagonal degrees in this block include edges incident with removed leaders. Thus the inverse trace is the ordinary inverse trace of the indicated symmetric block, plus the \((k-1)/q\) contribution when present.

Taking the traces of the exact inverses gives the following complete table:
\[
\begin{aligned}
J_{GG}&=\frac{3q-2}{q},\\
J_{GN}&=\frac{3q^2+5qt-2q-6t}{q(q+2t)},\\
J_{NG}&=\frac{2qt+3q-2t-2}{q(t+1)},\\
J_{NN}&=\frac{2q^2t+3q^2+3qt-2q-6t}{q(qt+q+2t)},\\
J_{AA}&=\frac{q^2+2qt-2t}{qt},\\
J_{BV}&=\frac{5qt+4q-6t}{2qt},\\
J_{VV}&=\frac{5t+4}{2t}.
\end{aligned}
\]
These are exact identities for all \(q\ge3\), including the \(q=3\) exceptional reduced-matrix dimension. Each identity can alternatively be verified by taking an adjugate trace and determinant of the displayed grounded block. A fully standalone exact-arithmetic checker is supplied.

**Step 2: exclude five types, globally.** Exact subtraction and factorization yield
\[
\begin{aligned}
J_{GG}-J_{NN}&=\frac{t(q^2+q+2)}{q(qt+q+2t)},\\
J_{GN}-J_{NN}&=\frac{t(q^2+(q-2)t)}{(q+2t)(qt+q+2t)},\\
J_{AA}-J_{NG}&=\frac{(q-1)t+q}{t(t+1)},\\
J_{BV}-J_{NG}&=\frac{(q-2)t^2+(3q-2)t+4q}{2qt(t+1)},\\
J_{VV}-J_{NG}&=\frac{(q+4)t^2+(3q+4)t+4q}{2qt(t+1)}.
\end{aligned}
\]
Every denominator and every numerator is strictly positive on \(q\ge3,t>0\). Since the global minimum is no greater than either \(J_{NN}\) or \(J_{NG}\), none of the five other types minimizes it. Notice that this argument does not silently assume that an optimum places one leader in each clique; all pairs within one clique are included.

**Step 3: unique threshold.** The remaining difference is
\[
J_{NG}-J_{NN}=
-\frac{t\big((q-2)t-(q+2)\big)}
{q(t+1)(qt+q+2t)}.
\]
Its denominator is strictly positive, and its numerator has one, and only one, zero at \(t=\tau_q\) in \((0,\infty)\). Hence \(NN\) is strictly better for \(t<\tau_q\), both types tie at that point, and \(NG\) is strictly better above it. Clique symmetry supplies exactly \(q-1\) pairs of type \(NN\) and exactly one pair of type \(NG\). The displayed optimum and the claimed tie counts follow. Finally, \(\tau_q=1+4/(q-2)\), giving the fixed-bridge-weight consequence.

## Verification

Run `python barbell_phase_verify.py` with SymPy installed. The checker verifies all seven rational orbit identities by exact symbolic inversion of the reduced grounded blocks, all six decisive exact cost differences, and 224 independent direct grounded inverse comparisons on eight clique sizes and four positive rational bridge weights each. It also checks 32 exhaustive seven-orbit minima. No floating-point results enter the proof. In the \(q=3,VV\) boundary case the symbolic continuation has an auxiliary decoupled coordinate whose inverse trace cancels a formal contrast term, and the actual three-clique case is separately checked by direct grounded inversion. These finite checks are supplementary; the proof above applies to all allowed parameters.

## Relationship to prior work

Lin, Fardad and Jovanović (arXiv:1302.0450; first public 2013-02-03) formulate the stochastic leader-placement problem with the grounded-Laplacian inverse-trace objective and develop general relaxations and greedy algorithms. Fitch and Leonard (arXiv:1407.1569; first public 2014-07-07) develop joint centrality and exact special solutions for paths and cycles. Patterson, McGlohon and Dyagilev (arXiv:1412.6595; first public 2014-12-20) provide exact leader-selection algorithms for weighted paths and rings. Patterson, Yi and Zhang (arXiv:1708.06873; first public 2017-08-23) give general resistance-distance formulas and special solutions on paths, cycles, and certain trees. Their general formulas permit evaluating a candidate barbell leader set but their inspected special-case theorems do not state the seven-orbit comparison or this weighted bridge phase boundary. This finding depends mathematically on elementary symmetry reduction and exact comparison, not on an assertion that the general optimization problem has no known algorithm.

## Limitations

The theorem concerns a two-vertex satellite clique attached through one positive-conductance bridge to a homogeneous larger clique, with exactly two noise-free leaders and identical follower noise variances. It does not classify arbitrary clique orders on both sides, unequal internal clique weights, additional bridges, noise-corrupted leaders, or a different objective such as convergence rate or controllability. A general-purpose prior formula is not excluded from being able to derive the result. Literature overlap was checked against identified accessible sources, but historical completeness or independent validation is not claimed.

## References

1. F. Lin, M. Fardad and M. R. Jovanović, *Algorithms for Leader Selection in Stochastically Forced Consensus Networks*, arXiv:1302.0450 (first posted 2013-02-03), https://arxiv.org/abs/1302.0450.
2. K. E. Fitch and N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569 (first posted 2014-07-07), https://arxiv.org/abs/1407.1569.
3. S. Patterson, N. McGlohon and K. Dyagilev, *Efficient, Optimal k-Leader Selection for Coherent, One-Dimensional Formations*, arXiv:1412.6595 (first posted 2014-12-20), https://arxiv.org/abs/1412.6595.
4. S. Patterson, Y. Yi and Z. Zhang, *A Resistance Distance-Based Approach for Optimal Leader Selection in Noisy Consensus Networks*, arXiv:1708.06873 (first posted 2017-08-23), https://arxiv.org/abs/1708.06873.
