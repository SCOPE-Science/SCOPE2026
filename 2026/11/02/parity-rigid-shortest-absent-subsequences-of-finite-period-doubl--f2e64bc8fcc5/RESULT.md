# Parity-rigid shortest absent subsequences of finite period-doubling words

## Finding

Let \(\mu(0)=01\), \(\mu(1)=00\), and \(P_k=\mu^k(0)\). For every integer \(k\ge1\), put
\[
q_k=\frac{2^k-(-1)^k}{3}.
\]
Every binary word of length \(q_k\) is an order-preserving scattered subsequence of \(P_k\), and the complete set of shortest absent scattered subsequences is
\[
\operatorname{SAS}(P_k)=
\begin{cases}
\{1^{q_k+1}\},&k\text{ even},\\
\{1^{q_k-1}00,\ 1^{q_k}0,\ 1^{q_k+1}\},&k\text{ odd}.
\end{cases}
\]
Consequently \(\iota(P_k)=q_k\), every shortest absent word has length \(q_k+1\), and its multiplicity is exactly one at even ranks and three at odd ranks. In particular, \(\iota(P_k)/|P_k|\to 1/3\).

## Assumptions and scope

All words are over the fixed binary alphabet \(\{0,1\}\). A word \(v=v_1\cdots v_m\) is a scattered subsequence of \(w\) if there are strictly increasing positions carrying its letters in order; adjacency is not required. The universality index \(\iota(w)\) is the largest integer \(t\) for which every binary word of length \(t\) appears as a scattered subsequence. A shortest absent scattered subsequence is a missing binary word of length \(\iota(w)+1\). This definition is different from a minimal absent *contiguous* factor.

The theorem concerns exactly the entire dyadic iterate \(P_k\) for each integer \(k\ge1\), and counts distinct missing words, not embeddings. No arbitrary-length prefix statement is asserted.

## Proof

**1. Two universal witnesses.** For an integer \(q\ge1\), set \(U_q=(01)^q0\). In the infinite alternating word beginning with \(0\), a greedy match for a binary word \(u\) of length \(q+1\) ends at zero-based position
\[
2q+\mathbf1_{\{u_1=1\}}-\tau(u),
\]
where \(\tau(u)\) is the number of changes between adjacent letters of \(u\). If \(u\) begins with \(0\), this position is at most \(2q\). If it begins with \(1\) but contains a \(0\), then \(\tau(u)\ge1\), again placing the match at most at position \(2q\). The all-ones word \(1^{q+1}\) has no match because \(U_q\) has only \(q\) ones. Thus precisely that word of length \(q+1\) is absent from \(U_q\). Also, \((01)^q\) is \(q\)-universal, by matching its \(j\)-th pair to the \(j\)-th desired letter.

For \(q\ge2\), set \(V_q=(01)^{q-2}00101\) and \(S_q=1V_q\). The word \(V_q\) contains \((01)^q\) as a subsequence, so it is \(q\)-universal. We claim that \(S_q\) is \((q+1)\)-universal and
\[
\operatorname{SAS}(V_q)=\{1^{q-1}00,\ 1^q0,\ 1^{q+1}\}.
\]
For \(q=2\), direct examination of the eight binary words of length three proves \(S_2=100101\) is \(3\)-universal; the three missing length-three words of \(V_2=00101\) are exactly \(100,110,111\). Suppose the two claims hold for \(q\). Since \(V_{q+1}=01V_q\), a target of length \(q+2\) starting with \(0\) occurs in \(V_{q+1}\) if and only if its remaining \(q+1\) letters occur in \(1V_q=S_q\): choose the first zero greedily. By the inductive universality assertion, every such target occurs. A target starting with \(1\) must choose the next symbol (the unique first one of the prefix \(01\)) greedily; it occurs if and only if its remaining \(q+1\) letters occur in \(V_q\). Therefore the missing set is exactly \(1\operatorname{SAS}(V_q)\), giving the displayed formula at \(q+1\). Finally \(S_{q+1}=101V_q\): a target of length \(q+2\) beginning with \(1\) embeds its suffix in the \((q+1)\)-universal word \(V_{q+1}\), and one beginning with \(0\) embeds its suffix in the \((q+1)\)-universal word \(S_q\). Hence \(S_{q+1}\) is \((q+2)\)-universal, completing the simultaneous induction.

**2. Structure of the iterates.** Every image under \(\mu\) begins with \(0\), and the only occurrence of \(1\) in an image is the final letter of \(\mu(0)=01\). Consequently every \(1\) in \(P_k\) has an immediately preceding \(0\); the \(01\) pairs associated with successive ones are disjoint. If \(q_k\) is the number of ones in \(P_k\), then \(q_0=0\) and \(q_{k+1}=2^k-q_k\), because only zeros yield a one under substitution. Solving this recurrence gives the announced expression for \(q_k\). Selecting the zero immediately before each of the \(q_k\) ones exhibits \((01)^{q_k}\) as a subsequence of \(P_k\), hence \(\iota(P_k)\ge q_k\). The missing word \(1^{q_k+1}\) shows the opposite inequality, hence \(\iota(P_k)=q_k\).

The final letter of \(P_k\) alternates with \(k\), beginning with \(0\) at rank zero. Since \(\mu^2(0)=0100\) and \(\mu^2(1)=0101\), the final four letters of \(P_k\) are \(0100\) for even \(k\ge2\). For odd \(k\ge3\), the last two letters of \(P_{k-2}\) are \(01\), and therefore the final eight letters of \(P_k\) are \(\mu^2(01)=01000101\).

**3. Even ranks.** When \(k\ge2\) is even, \(P_k\) has a zero after its last one. Together with the disjoint \(01\) pairs preceding all ones, this exhibits \(U_{q_k}\) as a subsequence of \(P_k\). By part 1, all length-\((q_k+1)\) binary words except \(1^{q_k+1}\) embed in this witness, hence also in \(P_k\). The exceptional word cannot occur because \(P_k\) has exactly \(q_k\) ones.

**4. Odd ranks.** If \(k\ge3\) is odd, the last eight letters \(01000101\) show that three zeros lie between the \((q_k-2)\)-nd one and the penultimate one, followed by a zero and the final one. Select the disjoint \(01\) pairs at the first \(q_k-2\) ones, then two of those three intervening zeros, then the final \(101\). This embeds \(V_{q_k}\) into \(P_k\). Hence every length-\((q_k+1)\) word outside the three-word absent set of \(V_{q_k}\) occurs in \(P_k\). All three exceptional candidates are absent from \(P_k\): \(1^{q_k+1}\) requires too many ones, \(1^{q_k}0\) requires a zero after the last one, and \(1^{q_k-1}00\) requires two zeros after the penultimate one, when only one zero follows it. The initial odd case \(P_1=01\) has \(q_1=1\) and precisely the missing length-two words \(00,10,11\), agreeing with the same formula.

This proves the full claim for all ranks.

## Verification

Run `python3 checker.py` with standard-library Python 3. The standalone program independently enumerates every binary target at the relevant lengths for ranks \(1\) through \(5\), exhaustively checks the two universal witnesses through parameter \(9\), and uses a next-occurrence/greedy-embedding dynamic program to compare shortest-absence counts through rank \(11\). It also checks each predicted absent string directly and verifies suffix and one-count identities. All tests passed. The finite tests are auxiliary; the unrestricted assertion follows from the proof above.

## Relationship to prior work

Parreau, Rigo, Rowland and Vandomme study the \(2\)-Abelian *contiguous-factor* complexity of the period-doubling fixed point and its block coding (arXiv:1405.3532; first submitted 2014-05-14). That invariant is different from the scattered-subsequence absence language classified here. Kosche, Koß, Manea and Siemer develop general structural and algorithmic tools for shortest absent subsequences and arch factorization (arXiv:2108.13968; first submitted 2021-08-31). Their general characterization applies to arbitrary input words, but the inspected sections do not give the period-doubling-specific parity classification or its closed form. General algorithms can of course compute instances; the claim here is the exact all-ranks language theorem.

## Limitations

The result requires the literal binary substitution iterates and the fixed alphabet \(\{0,1\}\). It does not classify shortest absent subsequences for arbitrary prefixes, contiguous minimal absent factors, or all minimal absent scattered subsequences of unrestricted lengths. Independent validation and exhaustive historical-priority verification have not been performed; a general absent-subsequence algorithm may recover each finite instance without giving this closed-form family law.

## References

1. A. Parreau, M. Rigo, E. Rowland and É. Vandomme, *A new approach to the 2-regularity of the \(\ell\)-abelian complexity of 2-automatic sequences*, first arXiv submission 2014-05-14, arXiv:1405.3532, https://arxiv.org/abs/1405.3532.
2. M. Kosche, T. Koß, F. Manea and S. Siemer, *Absent Subsequences in Words*, first arXiv submission 2021-08-31, arXiv:2108.13968, https://arxiv.org/abs/2108.13968.
