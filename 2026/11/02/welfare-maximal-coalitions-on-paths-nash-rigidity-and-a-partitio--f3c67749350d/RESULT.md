# Welfare-maximal coalitions on paths: Nash rigidity and a partition-count phase transition

## Finding

**Theorem (all-order optimum census, Nash rigidity, and entropy transition).** Fix integers \(p,q\ge1\). On the ordered labeled path \(P_n\), \(n\ge2\), use the induced-coalition-distance game whose *open* scores are \(s(1)=p\) and \(s(d)=-q\) for every finite \(d\ge2\), with utility \(-\infty\) in disconnected coalitions. A singleton has utility zero. Write
\[
w_\ell=2p(\ell-1)-q(\ell-1)(\ell-2),\quad \ell\ge1.
\]
For each \(1\le k\le n\), put \(t_k=\lfloor n/k\rfloor\), \(r_k=n-kt_k\), and
\[
V_k=(k-r_k)w_{t_k}+r_kw_{t_k+1},\qquad V=\max_{1\le k\le n}V_k.
\]
Then **(i)** the maximum social welfare is exactly \(V\); its maximizing partitions are *precisely* the interval partitions whose lengths, for some maximizing \(k\), consist of \(k-r_k\) copies of \(t_k\) and \(r_k\) copies of \(t_k+1\). The exact number of distinct labeled-path maximizers is
\[
N_n(p,q)=\sum_{k:V_k=V}\binom{k}{r_k}.
\]
**(ii)** Every social-welfare maximizing partition is Nash stable under unilateral join-or-singleton deviations. Thus the best Nash-stable welfare equals the unrestricted maximum, without requiring selection among optimal partitions.

**(iii)** Let \(d_\ell=w_\ell/\ell\). The only parameters where the maximizing integer block length is not unique are the countable critical ratios
\[
\frac pq=\frac{L(L+1)-2}{2},\qquad L=2,3,4,\ldots.
\]
Off this critical set, \(N_n(p,q)\) grows at most polynomially in \(n\) for fixed \(p,q\). At the critical ratio for \(L\), the only maximizing block lengths are \(L\) and \(L+1\). For every \(n\ge L(L-1)\), every optimal partition consists of these two lengths and
\[
N_n(p,q)=[z^n]\frac{1}{1-z^L-z^{L+1}}.
\]
Equivalently the counts satisfy \(a_n=a_{n-L}+a_{n-L-1}\), with \(a_0=1\), \(a_j=0\) for \(j<0\); moreover \(N_n(p,q)=\Theta(\alpha_L^n)\), with \(\alpha_L>1\) the unique real root of \(\alpha_L^{L+1}=\alpha_L+1\). This is a change from polynomial to exponential degeneracy of welfare-maximizing coalition partitions.

## Assumptions and scope

The graph has ordered vertices \(1,\dots,n\) and edges \(\{i,i+1\}\). Coalitions are nonempty subsets partitioning these vertices, not assumed connected a priori. The distance used in utility is shortest-path distance in the *induced subgraph of the agent's own coalition*, not ambient-path distance. If a coalition is disconnected, all its agents receive \(-\infty\); this is the original induced-connectivity convention retained in the open-score extension. For a connected coalition \(C\), each member receives the sum of scores of its distinct fellow members. The utility of a singleton is zero. Total welfare is the sum of all agents' utilities, with any disconnected coalition giving welfare \(-\infty\). A Nash deviation moves one agent to a different existing coalition or to a new singleton, with the remaining coalitions unchanged. The deviating agent compares its own utilities; strict improvement is required. All claims are for all integers \(p,q\ge1\), all \(n\ge2\), and the specified path topology. The asymptotic counts keep \(p,q\) fixed as \(n\to\infty\).

## Proof

**Connectedness and finite-block score.** The all-singleton partition has welfare zero, so any optimum contains no disconnected coalition. Every connected induced subgraph of a path is an interval, hence every feasible finite-welfare outcome is an ordered composition \(n=\ell_1+\dots+\ell_k\). An interval of length \(\ell\) contains exactly \(\ell-1\) unordered neighboring pairs, each contributing \(2p\), and \((\ell-1)(\ell-2)/2\) other unordered pairs, each contributing \(-2q\). Hence its welfare is \(w_\ell\).

**Exact maximizers and counts.** Expansion yields \(w_\ell=-q\ell^2+(2p+3q)\ell-(2p+2q)\). If a composition has block lengths \(a\ge b+2\), transferring one vertex from the length-\(a\) block to the length-\(b\) block changes the total welfare by
\[
(w_{a-1}+w_{b+1})-(w_a+w_b)=2q(a-b-1)>0.
\]
Thus, for any specified number \(k\) of blocks, the maximizers have precisely the balanced lengths \(t_k,t_k+1\) and welfare \(V_k\); conversely every order of those lengths gives that welfare. Taking the maximum over \(k\) proves the welfare formula and counting these orders gives the stated binomial sum. In particular it is an exact linear-length arithmetic scan, with no enumeration of set partitions.

**Nash stability of every welfare maximizer.** In an interval block of length \(\ell\ge2\), each endpoint has utility \(p-q(\ell-2)\). If this were negative, splitting that endpoint into a singleton would preserve connectivity of the old remainder and increase social welfare by twice its lost negative utility, impossible in an optimum. Hence endpoint utilities are nonnegative. Every non-endpoint of the block (if any) has utility \(2p-q(\ell-3)\), exceeding the endpoint utility by \(p+q\), and therefore is nonnegative as well. No agent can profit by becoming a singleton. An interior member of a block has no path edge to a different block, so joining another block would give utility \(-\infty\). Finally, any possible connected join of a vertex into another block must take a boundary endpoint (or a singleton) into an adjacent interval block. The departure leaves the source connected (or empty), the arrival extends the target interval, and all distances between the previously present agents within each block are unchanged. Because scores are symmetric, the change of total welfare is precisely twice the change in the deviator's utility. A strictly profitable deviation would increase global welfare, contradiction. Thus every optimum is Nash stable.

**Critical density comparison.** Direct division gives
\[
d_\ell=2p+3q-q\ell-\frac{2(p+q)}{\ell},\qquad
 d_{\ell+1}-d_\ell=\frac{2(p+q)}{\ell(\ell+1)}-q.
\]
The difference strictly decreases with \(\ell\). Since \(d_2=p>d_1=0\) and \(d_\ell\to-\infty\), the maximizing integer length is unique except for a tie between consecutive lengths \(L,L+1\) at exactly \(2(p+q)=qL(L+1)\), equivalent to the stated ratio. No third length ties.

**Noncritical polynomial regime.** Suppose \(L\) uniquely maximizes density \(d=d_L\). The positive gap \(\eta=\min_{j\ne L}(d-d_j)>0\) exists since \(d_j\to-\infty\). Partition \(n\) into \(\lfloor n/L\rfloor\) blocks of size \(L\) and, if necessary, one residual block of size \(r<L\). Writing \(w_0=0\), this partition has welfare at least \(nd-C\), where \(C=\max_{0\le r<L}(rd-w_r)\) depends only on \(p,q\). Any optimal composition has deficit \(nd-V\le C\); each vertex in a block of length different from \(L\) contributes at least \(\eta\) to this deficit. Therefore at most \(\lfloor C/\eta\rfloor\) vertices lie in exceptional blocks. The exceptional block lengths, their number, and their order types range over a finite set depending only on \(p,q\), and inserting any bounded number of such blocks among \(O(n)\) blocks of length \(L\) gives at most \(O(n^B)\) arrangements for some fixed exponent \(B\). This proves polynomial growth.

**Critical exponential regime.** At criticality \(d_L=d_{L+1}=d\), and all other lengths have smaller density, so every partition has welfare at most \(nd\), with equality iff every block length belongs to \(\{L,L+1\}\). Since the two lengths are coprime, every \(n\ge L(L-1)\) is a nonnegative integer combination of them: writing \(n=Lh+r\) with \(0\le r<L\), the representation uses \(r\) blocks of length \(L+1\) and \(h-r\) blocks of length \(L\), and \(h\ge L-1\) implies \(h\ge r\). Thus those and only those two-length compositions maximize welfare. The generating function for ordered sequences of blocks of lengths \(L,L+1\) is \((1-z^L-z^{L+1})^{-1}\); the displayed recurrence follows. Its positive radius \(\rho\in(0,1)\) is the unique root \(\rho^L+\rho^{L+1}=1\). For any complex root of the denominator on \(|z|=\rho\), equality in \(|z^L+z^{L+1}|\le\rho^L+\rho^{L+1}\) requires both \(z^L\) and \(z^{L+1}\) to be positive real, hence \(z=\rho\) because \(\gcd(L,L+1)=1\). The pole at \(\rho\) is simple; all other poles have strictly greater modulus. Partial fractions therefore give \(a_n\sim c\rho^{-n}\) for some \(c>0\). Set \(\alpha_L=1/\rho\). This proves exponential growth and the asserted root equation.

## Verification

The standalone `verify.py` enumerates *all set partitions*, including disconnected possibilities, of path sizes \(2\) through \(8\) for each \(1\le p\le5\), \(1\le q\le4\). It independently calculates induced-coalition utilities and full welfare, checks the claimed maximum and exact number of maximizers, and tests every welfare maximizer against every unilateral move. The finite checks comprise \(105880\) partition/parameter welfare comparisons, \(271\) exact optimum Nash checks, and \(140\) maximum/count parameter profiles. It also checks the critical two-length recurrence and optimum counts for \(L=2,3,4,5,6\), for \(L(L-1)\le n\le100\). To reproduce: `python3 verify.py`. These are finite checks; the unlimited-order assertions follow from the proof, not from finite enumeration.

## Relationship to prior work

Ganian, Hamm, Knop, Roy, Schierreich and Suchý introduced non-normalized score-based social distance games and gave general welfare/stability algorithms and structural results. Their 2023 article (arXiv:2307.05061), and their expanded account (arXiv:2312.07632), identify the **open** negative-tail score variant as a natural extension and give algorithmic bounds; they do not state the present exact path optimum census or critical optimal-partition entropy law. Their general examples show that an unrestricted welfare optimum need not be Nash stable on arbitrary graphs, unlike this path-specific outcome. Kaklamanis, Kanellopoulos, Papaioannou and Patouchas establish price of stability one for the *normalized positive inverse-distance* social distance game on trees (Theorem 12 of their 2020 manuscript). That model and its existential conclusion do not imply the count or the all-optima Nash statement for a negative-tail non-normalized game. The main novelty claimed here is the simultaneous exact optimum census, every-optimum stability, and polynomial-to-exponential change in counts under a negative-distance penalty. Familiar composition generating functions are used as a proof tool, not claimed as newly discovered identities.

## Limitations

The theorem does not cover branching trees, cyclic networks, other scoring tails, or coalitions evaluated using ambient-network rather than induced-coalition distances. The count is of *ordered interval partitions of the labeled path* (not arbitrary labeled set partitions or isomorphism classes). The polynomial-vs-exponential transition is for fixed integer \(p,q\); no uniform asymptotic over changing ratios is asserted. A full literature-priority guarantee is impossible: semantically equivalent results in specialist work not indexed by the inspected sources may exist. No independent external mathematical audit has occurred.

## References

- R. Ganian, T. Hamm, D. Knop, S. Roy, Š. Schierreich, O. Suchý, *Maximizing Social Welfare in Score-Based Social Distance Games*, Electronic Proceedings in Theoretical Computer Science **379** (2023), pp. 272–286; arXiv:2307.05061, first posted 2023-07-11, https://arxiv.org/abs/2307.05061.
- The same authors, *Maximizing Social Welfare in Score-Based Social Distance Games*, expanded account, arXiv:2312.07632, first posted 2023-12-12, https://arxiv.org/abs/2312.07632.
- C. Kaklamanis, P. Kanellopoulos, K. Papaioannou, D. Patouchas, *On the Price of Stability of Some Simple Graph-Based Hedonic Games*, 2020 preprint, https://repository.essex.ac.uk/29051/1/Hedonic%20games.pdf (Theorem 12 and Section 2).
