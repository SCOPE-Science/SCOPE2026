# Price-ratio phase transition for reversible cyclic one-defect synchronizers

## Finding

For integers \(n\ge2\), \(1\le k<n\), let \(T_{n,k}\) have states \(\mathbb Z/n\mathbb Z\) and input letters \(a,c,b\), acting by \(a(q)=q+1\), \(c(q)=q-1\), and \(b(0)=k\) with \(b(q)=q\) for \(q\ne0\), all residues taken modulo \(n\). For strictly positive real letter costs \(\alpha\) for \(a\), \(\gamma\) for \(c\), and \(\beta\) for \(b\), the automaton synchronizes **if and only if** \(\gcd(n,k)=1\). In the coprime case its exact least reset cost is
\[
\boxed{\beta(n-1)+(n-2)\min\{(n-k)\alpha,k\gamma\}.}
\]
If \((n-k)\alpha<k\gamma\), the unique least-cost reset word is \(b(a^{n-k}b)^{n-2}\). If \((n-k)\alpha>k\gamma\), it is \(b(c^k b)^{n-2}\). On the exact price-ratio boundary \((n-k)\alpha=k\gamma\), there are **exactly \(2^{n-2}\) distinct optimum words**: \(b(s_1b)\cdots(s_{n-2}b)\), where each \(s_j\) is independently either \(a^{n-k}\) or \(c^k\). At \(n=2\) this correctly gives the single optimal word \(b\).

## Assumptions and scope

Every input symbol is a complete deterministic transition; words are read left to right. A reset word sends the entire state set to one state. The inverse rotation \(c\) is a separate literal input letter, rather than a zero-cost inverse operation, and its price is strictly positive. Costs are additive over individual letter occurrences. The theorem applies only to the displayed reversible cyclic single-merge automaton, not arbitrary automata with inverse generators.

## Proof

For a word \(w\), write \(A,C,B\) for its counts of the three input letters. For each initial state \(q\), let \(H_q\) count the \(b\)'s encountered by its trajectory while it is at state \(0\). Every \(a\) moves a trajectory by \(+1\), every \(c\) by \(-1\), and every effective \(b\) by \(+k\). Consequently its endpoint is
\[
q+A-C+kH_q\pmod n.
\]
If \(d=\gcd(n,k)>1\), endpoints of two trajectories starting in distinct residue classes modulo \(d\) cannot agree, because their endpoints differ modulo \(d\) exactly by their starting-state difference. No reset word exists.

Suppose \(d=1\) and \(w\) resets. All endpoints equal \(r\), so \(kH_q\equiv r-q-A+C\pmod n\). Thus the \(n\) numbers \(H_q\) run through all residues modulo \(n\); some \(q_*\) has \(H_{q_*}\ge n-1\). Between consecutive effective \(b\)'s on this trajectory, the state must travel from \(k\) to \(0\) using the cycle edges \(+1\) and \(-1\). Intervening ineffective \(b\)'s do nothing to that trajectory. The least strictly positive cost of any such walk is
\[
\delta=\min\{(n-k)\alpha,k\gamma\}.
\]
Indeed, after eliminating any immediate backtracking pair, every minimum-cost walk is a simple path on the undirected cycle; the only simple paths from \(k\) to \(0\) are the clockwise path of \(n-k\) forward steps and the counterclockwise path of \(k\) backward steps. These are the only minimum-cost walks, except that both qualify at a tie. There are at least \(H_{q_*}-1\ge n-2\) disjoint gaps, so the total rotation cost is at least \((n-2)\delta\). Moreover \(b\) lowers the size of the current image set by at most one, while rotations preserve size, hence \(B\ge n-1\). Every reset word therefore costs at least \(\beta(n-1)+(n-2)\delta\).

Both \(a^{n-k}\) and \(c^k\) act on every state as translation by \(-k\). Fix either translation word \(s\). Define \(S_j=Q\setminus\{0,-k,\ldots,-(j-1)k\}\) for \(1\le j\le n-1\). Coprimality gives \(|S_j|=n-j\), while \(Qb=S_1\) and \(S_jsb=S_{j+1}\) for every \(j\le n-2\): translation shifts the deleted set to \(\{-k,\ldots,-jk\}\), and applying \(b\) removes \(0\), whose image \(k\) is still present. Thus any \(b(s_1b)\cdots(s_{n-2}b)\), with the stated two choices of \(s_j\), resets and has precisely the lower-bound cost when the choices are cheapest.

For **equality** at positive costs, necessarily \(B=n-1\), so the trajectory with \(H_{q_*}\ge n-1\) encounters **every** \(b\) effectively. Each of its \(n-2\) inter-merge gaps must be a minimum-cost path of cost \(\delta\); no rotation or merge can occur before the first \(b\), after the last \(b\), or as an extra step in a gap. The simple-path argument forces each gap to be exactly \(a^{n-k}\) or \(c^k\), depending on which one minimizes its cost. Strict inequality gives one word, and equality gives two independent choices in each of \(n-2\) gaps, hence exactly \(2^{n-2}\) literal words. This proves the cost formula, synchronizability criterion, and complete optimum-word classification. \(\square\)

## Verification

The standalone standard-library script `verify.py` builds all subset transitions and runs Dijkstra optimization, counting all least-cost paths. For every \(2\le n\le9\) and \(1\le k<n\), it checks noncoprime impossibility and six cost triples in each coprime case, including exact tie ratios. All 162 weighted instances and nine nonsynchronizing parameter pairs agree with the theorem. This finite computation is not the proof for all parameters. Run `python3 verify.py`.

## Relationship to prior work

The one-way cyclic single-merge automaton has a classical \(k=1\) case, and exact thresholds are also known for arbitrary coprime \(k\) when **only one rotation direction** is allowed. Those results do not directly classify all optimum words under three independently priced letters when the inverse rotation is a separate available operation. Don and Zantema studied the different switch-count objective; Szykuła and Zyzik studied unit-length algorithms. The present result adds the reversible generator, exhibits a sharp price-ratio phase transition, and counts all optimum words at the transition. A differently described prior result on reversible one-defect automata is a genuine residual originality risk.

## Limitations

Strict positivity of all three prices is required for the exact optimal-word count; free letters permit additional representations. The result is specific to a cycle and one idempotent defect, with the inverse generator supplied as another letter. The finite checker is supplementary. Independent scholarly validation of novelty and proof has not occurred.

## References

1. H. Don and H. Zantema, *Counting symbol switches in synchronizing automata*, arXiv:1812.04050v1, public 10 December 2018, https://arxiv.org/abs/1812.04050 .
2. S. Cambie, M. de Bondt and H. Don, *Extremal Binary PFAs in a Černý Family*, arXiv:2108.13927v1, public 25 August 2021, https://arxiv.org/abs/2108.13927 .
3. M. Szykuła and A. Zyzik, *An Improved Algorithm for Finding the Shortest Synchronizing Words*, arXiv:2207.05495v1, public 3 July 2022, https://arxiv.org/abs/2207.05495 .
