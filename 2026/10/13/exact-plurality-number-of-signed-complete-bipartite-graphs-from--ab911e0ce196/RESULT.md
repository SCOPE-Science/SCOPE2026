# Exact plurality number of signed complete bipartite graphs from sign correlations
## Finding
Let \(\Gamma=(K_{m,n},\sigma)\) be a signed complete bipartite graph with \(m,n\ge2\). Write the sign matrix as \(S=(s_{ij})\in\{-1,1\}^{m\times n}\), with rows indexed by the first shore and columns by the second shore.

For row \(i\), set \(p_i=|\{j:s_{ij}=1\}|\), \(q_i=n-p_i\), and \(\rho_{ik}=\sum_{j=1}^n s_{ij}s_{kj}\) for \(k\ne i\). Let \(r_i^+\), \(r_i^-\), and \(r_i^0\) be the numbers of positive, negative, and zero values among these \(m-1\) row correlations, and put
\[
R_i=r_i^0+\max\{1+p_i+r_i^++\mathbf 1_{r_i^->0},\ q_i+r_i^-+\mathbf 1_{r_i^+>0}\}.
\]
For column \(j\), define \(P_j\), \(Q_j\), \(c_j^+\), \(c_j^-\), and \(c_j^0\) analogously from the signs in that column and its inner products with the other columns, and put
\[
C_j=c_j^0+\max\{1+P_j+c_j^++\mathbf 1_{c_j^->0},\ Q_j+c_j^-+\mathbf 1_{c_j^+>0}\}.
\]
Then the plurality number is
\[
Y(\Gamma)=\max\left\{\max_{1\le i\le m}R_i,\ \max_{1\le j\le n}C_j\right\}.
\]
Thus an arbitrary signed biclique has an exact plurality formula determined by the one-shore sign counts and pairwise sign correlations.

## Assumptions and scope
The graph is finite, simple, complete bipartite, and both shores have size at least two. The signed-burning dynamics used here has two colours represented by \(+1\) and \(-1\). A positive edge preserves a propagated colour and a negative edge reverses it. In each propagation phase, an unburned vertex sums the signed colours arriving from its burned neighbors; it becomes the sign of a nonzero sum, while a zero sum leaves it unburned. Each round after the initial ignition has one propagation phase followed by the ignition of one still-unburned vertex in either colour. Burned vertices retain their colours. The plurality number \(Y(\Gamma)\) is the largest number of vertices that can finish in one colour.

The theorem deliberately assumes \(m,n\ge2\); signed stars are a separate boundary family. No claim is made here about minimizing over switching classes or about unsigned graph-burning parameters.

## Proof
Global reversal of the two colour names does not change the plurality objective, so fix the first ignition to have colour \(+1\).

Suppose first that the initial vertex is \(a_i\). At the next propagation phase every vertex \(b_j\) has exactly one burned neighbor, so it receives colour \(s_{ij}\). Therefore among the vertices of the second shore, exactly \(p_i\) have colour \(+1\) and \(q_i\) have colour \(-1\).

After this first propagation, the round ends with one additional ignition. Since every vertex of the second shore is already burned, this second ignition must choose one still-unburned vertex on the first shore and may assign it either colour.

For every other first-shore vertex \(a_k\), the next propagation gives total signed incoming influence
\[
\sum_{j=1}^n s_{kj}s_{ij}=\rho_{ik}.
\]
Thus a non-preempted \(a_k\) burns \(+1\) when \(\rho_{ik}>0\), burns \(-1\) when \(\rho_{ik}<0\), and remains unburned when \(\rho_{ik}=0\). The single second ignition can improve the eventual \(+1\) class by one exactly when a negative-correlation vertex exists, by igniting one such vertex as \(+1\) before it would be forced \(-1\). Symmetrically, it can improve the eventual \(-1\) class by one exactly when a positive-correlation vertex exists. Preempting a zero-correlation vertex gives no extra benefit, because every zero-correlation vertex can already be assigned freely later.

After that correlation-forcing propagation, all non-tied vertices are fixed. The remaining \(r_i^0\) tied vertices lie on the first shore, which is independent, so subsequent ignitions cannot influence one another; every tie may be assigned to the target colour. Therefore the optimum over plays beginning at \(a_i\) is exactly
\[
R_i=r_i^0+\max\{1+p_i+r_i^++\mathbf 1_{r_i^->0},\ q_i+r_i^-+\mathbf 1_{r_i^+>0}\}.
\]
No play beginning at \(a_i\) can do better: there is only one preemptive ignition before the row-correlation wave, and every later choice is a zero-correlation vertex already counted.

The same argument with the two shores exchanged shows that a first ignition at \(b_j\) has optimum \(C_j\). Every legal play has a first ignited vertex on one of the two shores. Taking the maximum over all possible first vertices proves
\[
Y(\Gamma)=\max\left\{\max_i R_i,\max_j C_j\right\}.
\]
Computing all row correlations costs \(O(m^2n)\), and all column correlations cost \(O(mn^2)\), which gives the stated evaluation bound.

## Verification
The accompanying verifier implements one propagation phase followed by one ignition per round and performs an independent recursive search over all later ignition choices. It exhaustively checks every signing of \(K_{2,2}\), \(K_{2,3}\), \(K_{3,2}\), \(K_{2,4}\), \(K_{4,2}\), and \(K_{3,3}\), totaling \(1168\) sign matrices. It also checks \(651\) deterministic structured sign matrices on additional small profiles. In every case the direct game search agrees with the closed correlation formula.

The finite computation is a stress test, not the proof of the arbitrary-size theorem. The proof above is symbolic and covers all \(m,n\ge2\).

## Relationship to prior work
Fallat, Gupta, Khodamoradi, and Zilles introduced signed graph burning and the plurality number in 2026. Their public arXiv record lists primary MSC \(05C57\) and secondary MSC \(05C22\), and the abstract states that the paper gives a code-theoretic formulation, switching-class consequences, exact results for signed paths under stated conditions, and hardness results. The same public record does not state an exact complete-bipartite formula.

Targeted literature searches used the terms “plurality number,” “signed burning,” “complete bipartite,” “biclique,” “row correlation,” “matrix correlation,” and equivalent sign-inner-product language. No indexed result located in those searches implied the displayed biclique formula. The nearest search results with complete bipartite graphs or signed matrices concerned different invariants such as signed domination, spectral signings, or unrelated bipartite parameters.

## Limitations
The accessible primary record supplied the title, authors, submission date, MSC classifications, abstract, and high-level scope, but a lawful full-text copy could not be retrieved for direct section-by-section comparison in this review. Because the paper is extremely recent, an unindexed complete-bipartite observation inside the unavailable full text remains a real bibliographic risk. This limitation affects the originality comparison, not the internal proof of the formula stated above. The theorem is restricted to complete bipartite graphs with both shores nontrivial.

## References
1. Shaun Fallat, Himanshu Gupta, Kamyar Khodamoradi, and Sandra Zilles, *Burning Signed Graphs*, arXiv:2610.02506v1, first submitted 1 October 2026, MSC \(05C57\), \(05C22\).
