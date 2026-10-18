# Signed total Roman weight enumerator and exact minimum-function counts for crown graphs

## Finding

Let \(n\ge 2\), and let the crown graph \(G_n\) have labelled vertices \(a_1,\ldots,a_n,b_1,\ldots,b_n\) and exactly the edges \(a_i b_j\) with \(i\ne j\). An STRD function is a labelling \(f:V(G_n)\to\{-1,1,2\}\) such that every open-neighbourhood label sum is at least \(1\) and every vertex labelled \(-1\) has a neighbour labelled \(2\). Put \(\omega(f)=\sum_vf(v)\), and define its full weight enumerator by

\[
R_n(z)=\sum_{f\text{ STRD on }G_n}z^{\omega(f)}.
\]

**Theorem.** The exact polynomial \(R_n(z)\) is the following nine-type multinomial sum, whose admissibility conditions involve only nine integer cell counts. For \(p,q\in\{-1,1,2\}\), let \(m_{pq}\) be nonnegative integers with \(\sum_{p,q}m_{pq}=n\), and define

\[
A=\sum_{p,q}p m_{pq},\qquad B=\sum_{p,q}q m_{pq},\qquad
M_A=\max\{p:m_{pq}>0\},\quad M_B=\max\{q:m_{pq}>0\},
\]
\[
t_A=\sum_qm_{2q},\quad t_B=\sum_pm_{p2},\quad
r_A=\sum_qm_{-1,q},\quad r_B=\sum_pm_{p,-1}.
\]

A matrix \(m\) is **admissible** if \(A\ge1+M_A\), \(B\ge1+M_B\), and the following conditions both hold:

\[
\begin{aligned}
&t_B=0\ \Longrightarrow\ r_A=0,\qquad t_B=1\ \Longrightarrow\ m_{-1,2}=0,\\
&t_A=0\ \Longrightarrow\ r_B=0,\qquad t_A=1\ \Longrightarrow\ m_{2,-1}=0.
\end{aligned}
\]

There are no additional conditions when the corresponding \(t\) is at least \(2\). Then

\[
\boxed{R_n(z)=\sum_{m\text{ admissible}}\frac{n!}{\prod_{p,q}m_{pq}!}\,z^{A+B}.}
\]

Consequently, the signed total Roman domination number is

\[
\boxed{\gamma_{stR}(G_n)=\begin{cases}4,&n=2,\\6,&n\ge3.\end{cases}}
\]

The **exact number** \(H_n=[z^{\gamma_{stR}(G_n)}]R_n(z)\) of labelled minimum-weight functions is as follows. Put

\[
\mathcal T_n=\left\{t\in\{1,\ldots,n\}: u_t=\frac{n+3-3t}{2}\in\mathbb Z_{\ge0},\quad
v_t=n-t-u_t\in\mathbb Z_{\ge0}\right\},
\]
\[
q_{n,t}=\frac{n!}{t!\,u_t!\,v_t!},\qquad
T_n=\sum_{t\in\mathcal T_n}q_{n,t}.
\]

For odd \(n\ge5\),

\[
\boxed{H_n=T_n^2.}
\]

For even \(n\ge4\), set

\[
D_n=\frac1n\sum_{t\in\mathcal T_n}v_tq_{n,t},\qquad
U_n=n\binom{n-1}{n/2-1},\qquad
J_n=n(n-1)\binom{n-2}{n/2-2}^{2}.
\]

Then

\[
\boxed{H_n=T_n^2-2U_nD_n+J_n.}
\]

The two boundary cases are \(H_2=1\) and \(H_3=10\). In order \(n=2,3,4,5,6,7\), the minimum-function counts are \(1,10,84,900,3280,44100\), respectively. Values for the complete bipartite graph, for the six-cycle, and for the three-cube that are implied by prior results are not claimed as new; the all-weight enumeration and uniform formulas for the minimum-function multiplicities are the contribution.

## Assumptions and scope

The graph is finite and simple; vertices and deleted matching pairs are individually labelled. The two sides of the bipartition are distinguished. The invariant uses *open* neighbourhoods, not closed ones, with threshold \(1\), alphabet \(\{-1,1,2\}\), and the additional requirement that each \(-1\) receive at least one neighbouring \(2\). Two labellings differing at any vertex are counted separately. Every integer \(n\ge2\) is covered, including the disconnected matching \(G_2\) and the connected graphs \(G_n\) for \(n\ge3\). The nine-type expression has a finite \(O(n^8)\)-term upper bound (the number of weak compositions into nine cells) for each \(n\), without an asymptotic coefficient claim.

## Proof

**1. Local inequalities and the exact nine-type criterion.** Write \(A_f=\sum_if(a_i)\) and \(B_f=\sum_if(b_i)\). The open neighbourhood of \(b_i\) contains precisely the \(a_j\) with \(j\ne i\), so its weight is \(A_f-f(a_i)\). Similarly the neighbourhood weight at \(a_i\) is \(B_f-f(b_i)\). Thus all neighbourhood inequalities hold precisely when

\[
A_f\ge1+\max_i f(a_i),\qquad B_f\ge1+\max_i f(b_i).
\]

For a vertex \(a_i\) labelled \(-1\), a defending \(2\) on the opposite side is available if and only if

\[
\#\{j:f(b_j)=2\}-\mathbf1_{\{f(b_i)=2\}}\ge1.
\]

If the opposite side has zero \(2\)'s, no \(-1\) is permitted; if it has exactly one \(2\), the matched vertex cannot carry \(-1\); if it has at least two \(2\)'s, every \(-1\) has a defender. The symmetric assertion holds on the other side. Finally, each labelling determines a unique matrix \(m_{pq}=\#\{i:(f(a_i),f(b_i))=(p,q)\}\), and there are \(n!/\prod m_{pq}!\) labellings of any fixed nine-type matrix. The above conditions depend only on that matrix and are exactly the stated admissibility conditions. Summing proves the polynomial identity for all \(n\ge2\).

**2. Minimum weight.** If each side contains a \(2\), then its respective maximum label is \(2\); therefore \(A_f,B_f\ge3\) and \(\omega(f)\ge6\). Suppose instead, for example, that the \(a\)-side has no \(2\). Since there is no \(2\) there to defend a negative vertex on the \(b\)-side, every \(b\)-label lies in \(\{1,2\}\), so \(B_f\ge n\). All \(a\)-labels lie in \(\{-1,1\}\) and their neighbourhood inequality forces \(A_f\ge2\). For \(n\ge5\) this gives total weight at least \(7\). For \(n=3\), parity makes \(A_f\ge3\), whence total weight at least \(6\). For \(n=4\), attaining total weight at most \(6\) would force \(B_f=4\) and \(A_f=2\). But all \(b\)-labels would then be \(1\), so no \(a\)-label could be \(-1\), contradicting \(A_f=2\). Hence, for every \(n\ge3\), every valid function has weight at least \(6\).

For odd \(n\ge3\), choose on each side two labels \(2\), \((n-3)/2\) labels \(1\), and \((n-1)/2\) labels \(-1\). Each side sums to \(3\), and two \(2\)'s on each side defend all negatives, so this is valid. For even \(n\ge4\), choose on each side one \(2\), \(n/2\) labels \(1\), and \(n/2-1\) labels \(-1\), placing the unique \(2\) in the same matched pair on both sides. Again both sums equal \(3\), all neighbourhood inequalities hold, and neither unique \(2\) is paired to a \(-1\). Thus weight \(6\) is attained. If \(n=2\), the graph consists of two disjoint edges; each vertex must have a positive label, and all ones give the unique weight-four function.

**3. Enumerating all minima.** For \(n\ge4\), the preceding argument also shows that a minimum-weight function must have a \(2\) on both sides and must have weight exactly \(3\) on each side. If a side has \(t\) labels \(2\), \(u\) labels \(1\), and \(v\) labels \(-1\), then \(t+u+v=n\) and \(2t+u-v=3\), equivalently \(3t+2u=n+3\). This gives the stated \(u_t,v_t\) and the multinomial count \(q_{n,t}\).

When \(n\) is odd, the equation forces \(t\) to be positive and even, hence at least \(2\). Thus every such choice on either side is mutually compatible: all \(-1\) vertices have defenders, and the neighbourhood sums are valid. Independent choices on the sides give \(H_n=T_n^2\) for odd \(n\ge5\).

When \(n\) is even, \(t\) is odd. Before enforcing the \(-1\) defender condition there are \(T_n^2\) ordered pairs of weight-three side labellings. A pair fails because the \(b\)-side has a **unique** \(2\) at a position carrying \(-1\) on the \(a\)-side, or symmetrically. There are \(U_n\) choices of a side labelling with a unique \(2\), and \(D_n\) choices of a side labelling carrying \(-1\) at any specified position, by index symmetry. Therefore each of these two failure events has size \(U_nD_n\).

Their intersection requires distinct positions \(i,j\) for the unique \(2\)'s, because each such position is \(-1\) on the opposite side. Given \(i\ne j\), each side must place its unique \(2\) at the prescribed position and a \(-1\) at the other position; its remaining \(n/2-2\) negative labels can be distributed among the other \(n-2\) vertices in \(\binom{n-2}{n/2-2}\) ways. Hence the intersection has size \(J_n\). Inclusion-exclusion gives \(H_n=T_n^2-2U_nD_n+J_n\), for every even \(n\ge4\).

For \(n=3\), any side of weight \(3\) containing a \(2\) has two \(2\)'s and one \(-1\), giving three choices; the two sides give \(9\) minimum functions. The only minimum function with a side containing no \(2\) is the all-ones labelling on both sides: the no-\(2\) side has weight at least \(3\) by parity, the other side must contain no negatives, and total weight \(6\) forces every label to be \(1\). Thus \(H_3=9+1=10\). This completes the proof.

## Verification

The standalone standard-library script `VERIFY.py` implements two separately formulated exact enumerators: one examines each labelled vertex and its literal graph neighbourhood, and the other enumerates the nine-type weak compositions and their multinomial weights. It compares the **complete polynomial** for each integer \(2\le n\le7\) and independently checks the closed minimum-weight coefficient for the same six instances. The respective minimum counts are \(1,10,84,900,3280,44100\); all six polynomial and minimum-count comparisons pass. To reproduce, run `python VERIFY.py` with Python 3. No third-party packages or input files are required. The finite checks are corroboration; the proof above handles all integers \(n\ge2\).

## Relationship to prior work

Koster, Volkmann and Wehrmann (2026, arXiv:2606.27175, first submitted 2026-06-25) study signed total Roman domination and domatic numbers on cubic and complete multipartite graphs. Their Proposition D, attributing an earlier theorem to Zhao and Miao (2017), gives the signed total Roman domination number of the *undeleted* complete bipartite graphs; for \(K_{n,n}\) it is \(2\) when \(n\ge4\), but it is \(4\) when \(n=3\). The crown graph with \(n\ge3\) is not complete multipartite, so these numerical results do not imply its all-weight distribution. The present theorem shows that deleting a perfect matching increases the minimum by exactly four for every \(n\ge4\).

The case \(G_3\cong C_6\) has previously known minimum weight \(6\). The case \(G_4\cong Q_3\) is also covered numerically by Koster, Volkmann and Wehrmann's cubic open-packing identity. Neither of these special-case numerical observations is claimed as original. The contribution here is the full polynomial and uniform closed enumeration of all minimum functions in the entire crown family, in particular all \(n\ge5\). A separately indexed prior Roman-domination result on crown graphs uses *perfect* Roman labellings \(\{0,1,2\}\), with a different condition; it does not imply this signed-total enumerator.

## Limitations

This is a self-contained enumerative theorem for the specified crown graphs, not an algorithm for arbitrary bipartite graphs. The finite verifier does not prove the infinite result; the proof provides that. Some older full texts were unavailable through the sources inspected. Equivalent unindexed results under the terms matching-deleted biclique or bipartite double cover could still exist. No claim of definitive bibliographic priority or independent verification is made.

## References

1. A. M. C. A. Koster, L. Volkmann and M. Wehrmann, *Signed Total Roman Domination and Domatic Numbers: Degree Three and Complete Multipartite Graphs*, 2026, arXiv:2606.27175, https://arxiv.org/abs/2606.27175 (first public version 2026-06-25).
2. Y. Zhao and L. Miao, *Signed Roman (Total) Domination Numbers of Complete Bipartite Graphs and Wheels*, Communications in Mathematical Research 33(4) (2017), 318–326, https://doi.org/10.13447/j.1674-5647.2017.04.04.
3. M. Chellali, N. Jafari Rad, S. M. Sheikholeslami and L. Volkmann, *Varieties of Roman Domination II*, AKCE International Journal of Graphs and Combinatorics 17 (2020), 966–984, https://doi.org/10.1016/j.akcej.2019.12.001.
