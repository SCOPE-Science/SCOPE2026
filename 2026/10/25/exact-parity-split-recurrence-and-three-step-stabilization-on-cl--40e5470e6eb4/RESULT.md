# Exact parity-split recurrence and three-step stabilization on clique coronas

## Finding

Let \(m\ge3\), and let \(G_m=K_m\circ K_1\) be the simple graph obtained by attaching one private leaf to each vertex of a complete graph. Run synchronous binary open-neighbourhood majority dynamics, retaining a vertex's current bit whenever its neighbours tie. Write \(F\) for the resulting map on the \(2m\) labelled vertices and
\[
D_t=\#\{s\in\{0,1\}^{2m}:\ F^{t+2}(s)=F^t(s),\ F^{j+2}(s)\ne F^j(s)\ (0\le j<t)\}.
\]
In particular \(D_t\) counts configurations whose **first** periodic state occurs after exactly \(t\) updates; fixed states count as period-one configurations. Put \(c=\binom{m}{\lfloor m/2\rfloor}\).

For even \(m=2k\ge4\), the complete depth census is
\[
\begin{aligned}
D_0&=2+c^2,\\
D_1&=2(2^m-1),\\
D_3&=c(2^m-c-2),\\
D_2&=2^{2m}-D_0-D_1-D_3.
\end{aligned}
\]
There are exactly \(2+c\) fixed configurations and \((c^2-c)/2\) distinct primitive two-cycles.

For odd \(m=2k+1\ge3\), the complete depth census is
\[
\begin{aligned}
D_0&=2+2c(k+2),\\
D_1&=2(2^m-1)+2c(k+2)(2^k-1),\\
D_3&=2c\,2^k(2^{k+1}-k-3),\\
D_2&=2^{2m}-D_0-D_1-D_3.
\end{aligned}
\]
There are exactly two fixed configurations and \(c(k+2)\) distinct primitive two-cycles.

Every orbit is periodic by time three, with sharp maximum transient time three for \(m\ge4\). The exceptional case \(m=3\) has sharp maximum two and \((D_0,D_1,D_2,D_3)=(20,32,12,0)\).

Under a uniformly random initial state, recurrence itself has a sharp parity split:
\[
\Pr(s\text{ is recurrent})\sim
\begin{cases}
\displaystyle\frac{2}{\pi m},&m\text{ even},\\[4pt]
\displaystyle 2^{-m}\sqrt{\frac{2m}{\pi}},&m\text{ odd},
\end{cases}
\]
while the fraction requiring the maximal three updates is asymptotic to \(\sqrt{2/(\pi m)}\) and \(\sqrt{8/(\pi m)}\) along even and odd \(m\), respectively. Thus a single private leaf at each clique vertex produces polynomially common recurrent states at even orders but exponentially rare recurrent states at odd orders.

## Assumptions and scope

The graph is labelled: its clique vertices are \(u_1,\ldots,u_m\), its leaves are \(v_1,\ldots,v_m\), each \(v_i\) is adjacent only to \(u_i\), and the clique has every edge \(u_i u_j\) for \(i\ne j\). There are no self-loops. A state is \((x,y)\in\{0,1\}^m\times\{0,1\}^m\), with \(x_i\) on \(u_i\) and \(y_i\) on \(v_i\). For any vertex, a strict majority of neighbouring ones sets its new state to one, a strict majority of zeros sets it to zero, and a tie preserves its current bit. All vertices update simultaneously. Transient depth is \(\tau(s)=\min\{t\ge0:F^{t+2}(s)=F^t(s)\}\); the eventual primitive period is either one or two. No probabilistic or asymptotic claim is needed for the exact formulas.

## Proof

Write \(S=\sum_{i=1}^m x_i\) for the number of ones in the clique. Each leaf copies its clique neighbour, so \(y'_i=x_i\). The clique vertex \(u_i\) sees precisely \(S-x_i+y_i\) neighbouring ones among \(m\) neighbours.

**1. Even clique order.** Suppose \(m=2k\). If \(x_i=0\), its new bit is one exactly when \(S+y_i\ge k+1\). If \(x_i=1\), retention at a tie gives the very same inequality: \(S-1+y_i\ge k\). Consequently
\[
(x',y')=\begin{cases}
(\mathbf0,x),& S<k,\\
(y,x),&S=k,\\
(\mathbf1,x),&S>k.
\end{cases}
\tag{1}
\]
Here \(\mathbf0\) and \(\mathbf1\) are homogeneous \(m\)-bit words. When both \(x\) and \(y\) have weight \(k\), (1) swaps them at every step. There are \(c^2\) such states, of which \(c\) are fixed. In addition the two fully homogeneous states are fixed. No other state is recurrent: if \(|x|\ne k\), the next clique word is homogeneous and becomes a fixed all-zero or all-one clique at once; if \(|x|=k\) but \(|y|\ne k\), then after one update the clique word is imbalanced and it subsequently becomes homogeneous. In either case the attached leaves copy that homogeneous word within the following update.

For the exact depth, a homogeneous initial \(x\) reaches a homogeneous full state after one step, unless it was already homogeneous throughout; this contributes \(2(2^m-1)\) states at depth one. If \(|x|=k\) and \(y\) is neither balanced nor homogeneous, (1) produces a nonhomogeneous imbalanced clique at time one; the clique homogenizes at time two, and its leaves do so only at time three. This is precisely the depth-three class, of cardinality \(c(2^m-c-2)\). All remaining nonperiodic states have depth two. These classes partition the \(2^{2m}\) states and establish all the even formulas.

**2. Odd clique order.** Suppose \(m=2k+1\). A strict majority needs at least \(k+1\) neighbouring ones; no tie is possible at clique vertices. For \(S<k\) or \(S>k+1\) the new clique word is respectively \(\mathbf0\) or \(\mathbf1\). At the two borderline weights,
\[
\begin{aligned}
S=k:&\quad x'_i=(1-x_i)y_i,\\
S=k+1:&\quad x'_i=(1-x_i)\lor y_i.
\end{aligned}
\tag{2}
\]
The first borderline output \(z=x'\) is disjoint from \(x\), and \(|z|\le k+1\); the second covers the complement of \(x\), and \(|z|\ge k\).

If \(|x|=k\) and \(|z|\in\{k,k+1\}\), direct substitution into (2) gives \(F(z,x)=(x,z)\): when \(|z|=k\), use disjointness, and when \(|z|=k+1\), use \(z=\mathbf1-x\). If \(|x|=k+1\) and \(|z|\in\{k,k+1\}\), the same substitution works by the complementary-cover condition. Thus all such states become periodic after at most one update. A state among them is recurrent initially precisely when \(y=z\).

Conversely, an imbalanced clique of weight outside \(\{k,k+1\}\) becomes homogeneous at its next update, and its leaves match at most one update afterward. A borderline clique with output weight outside \(\{k,k+1\}\) similarly has a homogeneous clique after two updates and a homogeneous full state after three. These cases exhaust the possibilities and rule out any other recurrent states.

Counting recurrent borderline pairs: with \(|x|=k\), a recurrent \(y\) must be disjoint from \(x\) and have weight \(k\) or \(k+1\). For each of the \(c\) choices of \(x\), there are \(k+1\) choices of \(y\) of weight \(k\), plus one of weight \(k+1\). The complementary case \(|x|=k+1\) has the same count: \(y\) covers \(\mathbf1-x\) and has weight \(k\) or \(k+1\). In total there are \(2c(k+2)\) nonhomogeneous periodic states and exactly two homogeneous fixed states. All nonhomogeneous periodic pairs are genuine two-cycles because \(x=y\) is incompatible with either the disjointness or the cover condition.

For depth one, first count the \(2(2^m-1)\) states with homogeneous \(x\) but not yet homogeneous full states. When \(|x|=k\), there are \(c\) choices of \(x\) and \(k+2\) admissible nonhomogeneous next-clique words \(z\) of weight \(k\) or \(k+1\) disjoint from \(x\). The \(k\) leaf bits on the support of \(x\) are free, yielding \(2^k\) original leaf words for each \(z\); exactly one makes \(y=z\) and is already recurrent. This contributes \(c(k+2)(2^k-1)\) depth-one states. The opposite borderline weight contributes identically by bit complementation. This gives \(D_1\).

For depth three, with \(|x|=k\), its output \(z\) must have weight between one and \(k-1\). Choosing \(z\) within the \(k+1\) complement positions, and choosing arbitrary original leaf bits at the \(k\) occupied clique positions, gives
\[
 c\,2^k\sum_{j=1}^{k-1}\binom{k+1}{j}
 =c\,2^k(2^{k+1}-k-3).
\]
The case \(|x|=k+1\) contributes the same number by complementation. The requirement \(z\ne\mathbf0\) (or \(z\ne\mathbf1\) after complementation) makes the third step genuinely necessary. All other nonperiodic configurations first become periodic at time two, yielding \(D_2\) by subtraction.

**3. Sharpness and asymptotics.** For \(m=3\), the odd formula has \(k=1\), so \(D_3=0\) and \(D_2=12>0\). For odd \(m\ge5\), \(2^{k+1}-k-3>0\). For even \(m\ge4\), \(2^m-c-2>0\). Hence the stated sharp transient times follow. Finally the central binomial estimates \(\binom{m}{\lfloor m/2\rfloor}\sim 2^m\sqrt{2/(\pi m)}\), together with the exact formulas, give all four stated probability asymptotics.

## Verification

A standalone direct-neighbourhood verifier is supplied in `verify_clique_corona.py` and requires only Python's standard library. It constructs the full graph (not the reduced formulas), applies majority at each vertex, computes the least \(t\in\{0,1,2,3\}\) for which \(F^{t+2}(s)=F^t(s)\), and compares each depth population and the fixed/two-periodic census to the proved formulas for every labelled initial state at \(m=3,4,5,6,7,8,9\). These seven tests cover \(349{,}504\) initial states. The recorded output is in `verification_output.txt`; the terminal line is `CLIQUE_CORONA_MAJORITY_VERIFY_OK`.

For example at \(m=5\) the exact depth vector is \((82,302,400,240)\); at \(m=6\) it is \((402,126,2728,840)\). These finite tests are corroboration only. The proof in the preceding section supplies the all-\(m\) statement.

## Relationship to prior work

General majority-dynamics results establish eventual periods at most two on every finite undirected graph (Goles and Olivos, 1980; Benjamini et al., 2014). They do not by themselves determine exact periodic-state counts, depth distributions or the sharp three-step cutoff on this particular corona family. The tie-retaining convention agrees with those sources. The open-access 2024 work of Zehmakan examines stabilization, periodicity and fixed configurations on general graphs and especially cycles; it does not state a clique-corona enumeration. Graph invariants of clique coronas and exact majority results on other graph families concern different statements, and do not imply this paired core–leaf census. Database and web searches found no equivalent classification; this absence does not establish historical uniqueness.

## Limitations

This is a theorem for the deterministic synchronous binary tie-retaining rule on \(K_m\circ K_1\) only. It does not classify asynchronous, randomized-tie, weighted, larger-leaf, or arbitrary-core dynamics; it does not give basin populations separated by which attracting cycle is reached. The number of graph sizes checked computationally is finite, whereas the mathematical proof covers all \(m\ge3\). A possible unindexed historical equivalent and lack of full-text access to the short 1980 threshold paper remain literature risks; independent validation has not been performed.

## References

1. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486v1, first posted 2014-05-11. https://arxiv.org/abs/1405.2486
2. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics **30** (1980), 187–189. https://doi.org/10.1016/0012-365X(80)90121-1
3. A. N. Zehmakan, *Majority opinion diffusion: when tie-breaking rule matters*, Autonomous Agents and Multi-Agent Systems **38** (2024), article 21. https://doi.org/10.1007/s10458-024-09651-y
