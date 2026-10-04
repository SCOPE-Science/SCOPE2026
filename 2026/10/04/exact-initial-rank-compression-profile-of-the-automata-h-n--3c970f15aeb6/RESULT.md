# Exact initial rank-compression profile of the automata \(H_n\)
## Finding
For the Ananichev–Gusev–Volkov automaton \(H_n\) with \(n\ge4\), let \(\lambda_n(s)=\min\{|w|:|Qw|\le n-s\}\) and \(h_n=\lfloor n/2\rfloor+1\). Then \(\lambda_n(1)=1\), with unique shortest word \(b\); for every \(2\le s\le h_n\), \(\lambda_n(s)=3s-3\), with unique shortest word \((bab)^{s-1}\). Whenever \(h_n+1\le n-1\), the linear law fails at the next deficiency: \(\lambda_n(h_n+1)>3h_n\).

Thus the named family has a rigid linear high-rank compression regime that lasts exactly through deficiency \(h_n\), followed by immediate saturation. This profile is distinct from the already-known full reset threshold \(n^2-4n+6\).

## Assumptions and scope
For \(n\ge4\), use the labeling of Ananichev, Gusev and Volkov. The state set is \(Q=\{1,2,\ldots,n\}\). The letter \(a\) swaps states \(1\) and \(n\) and fixes every other state. The letter \(b\) acts by
\[
b(i)=\begin{cases}
i+1,&1\le i<n-1,\\
1,&i=n-1,\\
3,&i=n.
\end{cases}
\]
For a word \(w\), write \(Qw\) for the image of all states. A use of \(b\) is called effective when it strictly decreases the current image size. Since \(a\) is a permutation and \(b\) has the unique collision pair \(\{2,n\}\), each effective \(b\) decreases rank by exactly one.

## Proof
The first rank decrease must be caused by \(b\), and in a shortest word any initial \(a\) is removable because \(Qa=Q\). Hence deficiency one requires one letter and its unique shortest word is \(b\).

After every application of \(b\), state \(n\) is absent because no state maps to \(n\) under \(b\). Before any later effective \(b\), state \(n\) must therefore be restored. In a shortest word \(aa\) cannot occur because \(a^2\) is the identity. Moreover, no \(b\) can occur after the last \(a\) that restores \(n\), because such a \(b\) would remove \(n\) again. Thus every effective \(b\) after the first is immediately preceded by \(a\). To restore \(n\), that \(a\) must swap a present state \(1\) into \(n\), so immediately before the effective \(b\), state \(1\) is absent. Since state \(1\) is the unique preimage of state \(2\) under \(b\), the image after every nonfirst effective \(b\) misses both \(2\) and \(n\).

Consequently the second effective \(b\) needs at least the two intervening letters \(ab\). After any nonfirst effective \(b\), both \(2\) and \(n\) are absent. Before the next effective \(b\), state \(2\) must be restored; the only way to do so is by applying \(b\) while state \(1\) is present. State \(n\) must then be restored by \(a\), followed by the effective \(b\). Hence each later rank decrease costs at least the three-letter block \(bab\). If a word has deficiency at least \(s\ge2\), it has at least \(s\) effective occurrences of \(b\), so
\[
|w|\ge 1+2+3(s-2)=3s-3.
\]
Equality forces every gap just described to be shortest, hence forces the unique word \((bab)^{s-1}\).

It remains to determine how long this forced word keeps decreasing rank. Let \(H_r=Q\setminus Q(bab)^r\). Direct induction from the transition formulas gives, for
\(1\le r\le\lfloor(n-1)/2\rfloor\),
\[
H_r=\{n,2,4,\ldots,2r\}.
\]
If \(n=2m\), the next iterate satisfies
\[
H_m=\{1,2,4,\ldots,2m\}.
\]
Therefore \((bab)^{s-1}\) has deficiency exactly \(s\) for every \(2\le s\le\lfloor n/2\rfloor+1\). Together with the lower bound this proves the formula and uniqueness throughout the stated range.

At the next step, when such a deficiency exists, another direct substitution in the same hole formulas shows that \((bab)^{h_n}\) does not acquire a new hole: its deficiency is still \(h_n\). But any word of length \(3h_n\) that reached deficiency \(h_n+1\) would have equality in the lower-bound argument and hence would have to equal \((bab)^{h_n}\). This contradiction proves \(\lambda_n(h_n+1)>3h_n\).

## Verification
The standalone verifier `artifacts/verify_h_profile.py` reconstructs the transition maps from the displayed definition. Exact breadth-first search of the full power automaton for every \(4\le n\le14\) checks every claimed minimum length and confirms that the shortest word is unique in every claimed case; it also checks the strict first-saturation boundary whenever that boundary exists. Direct replay of the forced witnesses and the saturation step is performed for every \(4\le n\le300\). Running the packaged script produces exactly `VERIFY_OK`.

These finite computations are checks of the symbolic proof, not substitutes for the all-\(n\) argument.

## Relationship to prior work
Ananichev, Gusev and Volkov define \(H_n\) in the 2013 extended paper and prove only its full reset threshold \(n^2-4n+6\), using a reduction to a Wielandt subautomaton. Their earlier 2010 preprint announces an unnamed series with reset length \(n^2-4n+6\) for a future extended version but does not define \(H_n\). The exact intermediate-rank thresholds, uniqueness of the shortest compression words, and the first saturation boundary proved here are not implications of the endpoint reset-threshold theorem.

Searches for aliases and stronger coverage included `H_n automaton rank compression profile shortest word`, `H_n automaton deficiency shortest rank word bab`, `slowly synchronizing automata intermediate rank H_n`, and `rank threshold H_n Ananichev Gusev Volkov`, together with semantic searches of the published published-finding corpus collection. No matching statement was found. General work on shortest reset words and minimum-rank words does not supply this named-family profile.

## Limitations
The theorem concerns the fixed labeling and transition structure above. It determines the initial compression profile only through the first saturation point; it does not determine \(\lambda_n(s)\) for all larger deficiencies, nor does it reprove the known full reset threshold. Literature search cannot prove absolute novelty; the residual originality risk is an unindexed or differently phrased earlier statement of the same intermediate-rank profile.

## References
1. D. S. Ananichev, V. V. Gusev, M. V. Volkov, *Primitive digraphs with large exponents and slowly synchronizing automata*, arXiv:1302.5793v1, first public 2013-02-23; Journal of Mathematical Sciences 192 (2013), DOI:10.1007/s10958-013-1392-8.
2. D. S. Ananichev, V. V. Gusev, M. V. Volkov, *Slowly synchronizing automata and digraphs*, arXiv:1005.0129v1, first public 2010-05-02; MFCS 2010, DOI:10.1007/978-3-642-15155-2_7.
