# Sharp Raney enumeration of maximal stabilization delays in capped cyclic transport

## Finding
For every integer capacity \(c\ge2\), ring length \(k\ge2\), and total inventory \(H\ge ck\), consider the simultaneous cyclic transport map on \(\mathbb N_0^k\)
\[
 F_c(g)_i=g_i-\min(g_i,c)+\min(g_{i+1\pmod k},c),\qquad\sum_i g_i=H.
\]
Let \(\tau(g)\) be the first time when all sites have at least \(c\) chips. These configurations are exactly the fixed points of the map in the indicated high-density sector. Every initial state stabilizes by time \(k-1\), and the exact number of ordered initial inventory vectors with the **maximum** delay \(\tau(g)=k-1\) is
\[
 \boxed{\quad k\,\frac{c}{(c+1)(k-1)+c}\binom{(c+1)(k-1)+c}{k-1}.\quad}
\]
The count does not depend on the inventory surplus \(H-ck\). The per-site contribution is a Raney number counting ordered forests of \(c\) full rooted \((c+1)\)-ary trees with \(k-1\) internal vertices.

## Assumptions and scope
Sites are labelled \(0,\ldots,k-1\), chips are nonnegative integers, and each site simultaneously sends \(\min(g_i,c)\) chips to its predecessor, receiving those sent by its successor. The hypotheses \(c\ge2\), \(k\ge2\), and \(H\ge ck\) are essential to the stated regime; no randomness, weak convergence or thermodynamic limit is assumed. The counting measure distinguishes cyclic translations of an initial state. The formula is for the *largest attainable transient* rather than all transient levels.

## Proof
Set \(m_i(t)=\sum_{s=0}^{t-1}\min(g_i(s),c)\), the cumulative number departing site \(i\) in \(t\) updates, with \(m_i(0)=0\). Conservation and the queue service rule give
\[
 m_i(t+1)=\min\{m_i(t)+c,\,g_i(0)+m_{i+1}(t)\}.
\]
Induction on \(t\) therefore gives the exact min-plus formula
\[
 m_i(t)=\min_{0\le\ell\le t}\left[c(t-\ell)+\sum_{r=0}^{\ell-1}g_{i+r}(0)\right].
\]
Indeed the two terms of the recurrence correspond to a leading idle step and an initial service constraint; the latter ranges over the same prefixes after shifting the index. Define lost service \(h_i(t)=ct-m_i(t)\). Equivalently,
\[
 h_i(t)=\max_{0\le\ell\le t}\left[c\ell-\sum_{r=0}^{\ell-1}g_{i+r}(0)\right].
\]
Every prefix of length at least \(k\) can lose a complete circuit, changing its bracketed value by \(ck-H\le0\). Thus the maximum is attained at some length at most \(k-1\), and \(h_i(t)\) is constant for \(t\ge k-1\). Moreover \(h_i(t+1)-h_i(t)=c-\min(g_i(t),c)\); hence no site has inventory below \(c\) at time \(k-1\), proving the universal bound.

A site \(i\) exhibits an increase at the final possible step from \(k-2\) to \(k-1\) exactly if the new prefix of length \(k-1\) strictly exceeds every shorter prefix. Cancelling the common initial part, this is equivalent to
\[
 \sum_{r=1}^{s}g_{j-r}(0)<cs\quad(1\le s\le k-1),
 \qquad j\equiv i-1\pmod k.
\]
Call this event \(E_j\). For distinct \(j,j'\), the corresponding strict deficits on the two directed arcs between these indices would sum to \(\sum_i(g_i-c)<0\), contrary to \(H\ge ck\); hence the \(k\) events are disjoint. Their union is exactly \(\{\tau=k-1\}\).

To count one \(E_j\), list the other \(k-1\) inventories backwards around the circle as \(a_1,\ldots,a_L\), where \(L=k-1\). The constraints are \(a_r\ge0\) and \(\sum_{r=1}^{s}a_r<cs\) for every \(1\le s\le L\). The omitted coordinate equals \(H-\sum a_r\), and the last strict inequality makes it at least \(H-cL+1\ge c+1\); it therefore introduces no additional restriction or multiplicity.

These constrained words are in bijection with ordered forests of \(c\) full plane \((c+1)\)-ary trees with \(L\) internal vertices: read each \(a_s\) as the number of leaves before the \(s\)-th internal vertex in preorder across a forest of \(c\) initial roots. Before internal vertex \(s\), the count of pending positions is \(cs-\sum_{r=1}^s a_r\) (up to the harmless indexing convention for the final leaf); the strict inequalities say precisely that another internal vertex may be visited. Once the last internal vertex is read, all remaining positions are leaves. The generating series \(T(z)\) for full rooted \((c+1)\)-ary plane trees satisfies \(T=1+zT^{c+1}\). By Lagrange inversion,
\[
 [z^L]T(z)^c=\frac{c}{(c+1)L+c}\binom{(c+1)L+c}{L}.
\]
There are \(k\) disjoint events, which yields the claimed formula. At least one forest exists, so the bound \(k-1\) is attained.

## Verification
Run `python3 verify.py` with a standard Python 3 interpreter. The script directly enumerates inventory vectors for capacities \(1\le c\le3\), ring lengths \(2\le k\le6\) and three high-density totals, computes stopping times by simulation, and checks both the sharp upper bound and the Raney count, returning `VERIFY_OK cases= 45`. The capacity-one instances are independent consistency checks, not included in the new theorem's claimed domain. All infinite parameter conclusions follow from the preceding proof, not from finite enumeration.

## Relationship to prior work
The motivation is the deterministic Rule 184 traffic-jam transient treated by Jha, Wiesenfeld and Laval (2026), following the numerical study of Jha, Wiesenfeld, Lee and Laval (2025). Rule 184 corresponds to single-particle capacity, whereas the present theorem is about arbitrary integer *batch* capacity \(c\ge2\), counts exact maximally delayed states, and identifies the higher-arity Raney forest structure. Classical Catalan-type counts in single-particle traffic models are not claimed as new. The named source's accessible abstract does not establish the capacity-dependent count; its complete text could not be assessed, so literature overlap cannot be excluded solely on that evidence.

## Limitations
The result concerns labelled finite rings with total inventory at least capacity times ring size; it says nothing about lower inventory densities, arbitrary graphs, heterogeneous capacities, random schedules, or the full distribution of delay times. The motivating 2026 paper's complete text was not available for direct comparison. Novelty therefore remains a same-author best-knowledge assessment rather than a historical-priority guarantee; no independent audit has been performed.

## References
- A. Jha, K. Wiesenfeld, J. Laval, *Equilibrium-like statistical mechanics in space-time for a deterministic traffic model far from equilibrium*, arXiv:2602.08991 (first public posting 2026-02-09).
- A. Jha, K. Wiesenfeld, G. Lee, J. Laval, *Evidence of Non-Equilibrium Critical Phenomena in a Simple Model of Traffic*, arXiv:2501.08417 (first public posting 2025-01-14).
- G. N. Raney, *Functional composition patterns and power series reversion*, Trans. Amer. Math. Soc. 94 (1960), 441–451 (classical Raney enumeration; its formula and tree interpretation are used, not claimed as original).
