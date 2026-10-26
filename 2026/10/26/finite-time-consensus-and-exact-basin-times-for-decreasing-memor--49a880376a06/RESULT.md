# Finite-time consensus and exact basin times for decreasing-memory majority maps

## Finding
Let \(L\ge1\), and let \(w_1\ge w_2\ge\cdots\ge w_L\ge0\) be real weights. For every history \(u=(u_0,\ldots,u_{L-1})\in\{-1,+1\}^L\), define \(Q(u)=\sum_{j=1}^{L}w_j u_{j-1}\), and let \(\operatorname{sgn}_b(q)\) be the sign of \(q\) when nonzero and \(b\) when zero. Define the memory map
\[
F(u_0,\ldots,u_{L-1})=(\operatorname{sgn}_{u_0}(Q(u)),u_0,\ldots,u_{L-2}).
\]
Put \(\sigma(u)=\operatorname{sgn}_{u_0}(Q(u))\). **Every subsequently generated symbol equals \(\sigma(u)\)**. Consequently \(F^L(u)=\sigma(u)^L\), the only periodic states are \((+1)^L\) and \((-1)^L\), and each has exactly \(2^{L-1}\) states in its basin. The exact least settling time \(\tau(u)=\min\{t\ge0:F^t(u)=\sigma(u)^L\}\) is zero when \(u=\sigma(u)^L\), and otherwise
\[
\tau(u)=L-\min\{j\in\{0,\ldots,L-1\}:u_j\ne\sigma(u)\}.
\]
For \(L\ge2\), its sharp maximum over all histories is \(L\) if \(w_1<\sum_{j=2}^{L}w_j\), and \(L-1\) otherwise; for \(L=1\) the maximum is zero. In the uniform-weight case \(w_j=1\), the **full finite settling-time histogram** is explicit: \(N_L(0)=2\), and for \(j=0,\ldots,L-1\), letting \(r=L-j-1\),
\[
N_L(L-j)=2\sum_{k=\max(0,a_{L,j})}^{r}\binom rk,
\]
where \(a_{L,j}=\lfloor L/2\rfloor+1-j\) for odd \(L\); for even \(L=2m\), \(a_{L,0}=m+1\), and \(a_{L,j}=m-j\) for \(j\ge1\). Empty sums are zero. The decreasing-weight hypothesis is substantive: for \(L=2\) and weights \((1,2)\), \((+1,-1)\) and \((-1,+1)\) form a two-cycle.

## Assumptions and scope
The update is deterministic, synchronous, binary, and uses the *current* bit to break zero-score ties. The weights are real, nonnegative and nonincreasing with lag, including zero weights. The theorem describes the entire finite-memory state space, without probabilistic assumptions. It applies to induced clover signed-majority recurrences whenever their cycle-sign sums satisfy this weight condition; such an induced recurrence is derived in Proposition 2 of España--Funez--Ugalde (2025). For example, a positively signed clover with one self-loop and one loop of every length \(2,\ldots,L\) has uniform weights. The original network and its reduced recurrence are not identical during initial transients; the theorem's settling-time values concern the reduced recurrence, not arbitrary unprepared full-network configurations.

## Proof
Let \(u'=F(u)\), \(q=Q(u)\), \(q'=Q(u')\), and \(\sigma=\sigma(u)\). Direct subtraction gives
\[
q'-q=w_1\sigma+\sum_{j=1}^{L-1}(w_{j+1}-w_j)u_{j-1}-w_Lu_{L-1}.
\]
If \(\sigma=+1\), the nonincreasing inequalities imply
\[
q'-q\ge w_1-\sum_{j=1}^{L-1}(w_j-w_{j+1})-w_L=0.
\]
If \(\sigma=-1\), the reverse bound gives \(q'-q\le0\). By definition, \(\sigma=+1\) implies either \(q>0\), or \(q=0\) and \(u_0=+1\). In both cases \(q'\ge0\), and if \(q'=0\), the new current bit is \(u'_0=+1\), so the next tie resolves to \(+1\). The negative case is symmetric. Thus \(\sigma(F(u))=\sigma(u)\). Induction shows every future emitted symbol equals \(\sigma(u)\); after \(L\) emissions the entire history is constant.

The only fixed states are the two constants, and every orbit reaches one of them, so there are no other periodic orbits. Global negation commutes with \(F\) and swaps the two basins; the basins therefore have equal size \(2^{L-1}\). After \(t\) steps the state consists of \(t\) newly emitted copies of \(\sigma\), followed by the retained initial coordinates \(u_0,\ldots,u_{L-t-1}\), which proves the formula for \(\tau\). A history can have \(u_0\ne\sigma\) exactly when \(w_1<\sum_{j=2}^Lw_j\): necessity follows from the weighted score bound and tie rule, and sufficiency uses \(u_0=-1\), \(u_j=+1\) for \(j\ge1\). Otherwise \(\sigma=u_0\) always; the history \((+1,-1,+1,\ldots,+1)\) has \(\tau=L-1\), proving the other sharp cutoff when \(L\ge2\).

For equal weights, fix the final sign \(+1\) and place the **first disagreement** at index \(j\). There are \(j\) initial positive bits, then one negative bit, and \(r=L-j-1\) unrestricted later positions. If \(k\) of these are positive, the total is \(j+k\). For odd \(L\), selecting \(+1\) requires \(j+k\ge\lfloor L/2\rfloor+1\). For even \(L=2m\), it requires \(j+k\ge m\) when \(j\ge1\) (the initial bit is positive and wins ties), and \(k\ge m+1\) when \(j=0\) (the initial bit is negative and loses ties). Count \(\binom rk\) possibilities and double by global sign reversal. Exactly two constant histories have \(\tau=0\). Finally, with weights \((1,2)\) the two displayed states map to each other by direct substitution.

## Verification
Run `python verify.py`. It exhaustively checks every initial history for each of \(1286\) nonincreasing integer weight vectors of lengths \(1\) through \(8\) with weights in \(\{0,1,2,3,4\}\); it also checks every uniform-weight histogram against the formula for each of those lengths. Its output ends with `CHECKS_PASS 1286`. The infinite-parameter theorem is established by the algebraic argument above, not by these finite tests.

## Relationship to prior work
España, Funez, and Ugalde (arXiv:2509.03654, Proposition 2 and Section 4) derive the signed-majority delay recurrence for clover networks and analyze a single-coefficient dominance regime. Their induced recurrence statement is used here, not claimed as new. A nonincreasing weight vector with multiple comparable positive coefficients (e.g. all ones of length at least three) is generally outside their strict single-coefficient dominance condition. The present theorem gives full basin selection and exact settling times for this non-dominant cone. Existing work on majority-vote consensus with memory, including Marzagão et al. (AAAI 2021), concerns different network protocols; full equivalence or an earlier statement under other terminology has not been ruled out.

## Limitations
The result does not cover negative weights, nonmonotone positive weights, asynchronous updates, stochastic majority decisions, or arbitrary full-network transient times. It does not assert the decreasing-weight condition is necessary for convergence: the counterexample only proves that dropping it permits oscillation. The paper-source relationship does not establish exhaustive historical priority, and no independent validation has been performed.

## References
- A. España, W. Funez, E. Ugalde, *Dominant vertices and attractors' landscape for Boolean networks*, arXiv:2509.03654, first posted 2025-09-03; see Proposition 2, Section 4, and concluding remarks. https://arxiv.org/abs/2509.03654 ; https://arxiv.org/html/2509.03654v3 .
- D. Kohan Marzagão, L. Basualdo Bonatto, T. Madeira, M. M. Gauy, P. McBurney, *The Influence of Memory in Multi-Agent Consensus*, AAAI 2021, DOI:10.1609/aaai.v35i13.17342. https://ojs.aaai.org/index.php/AAAI/article/view/17342 .
