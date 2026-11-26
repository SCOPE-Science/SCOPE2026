# Sharp finite-size prevalence of weak excluded middle in Heyting algebras

## Finding

Let \(H\) be a finite Heyting algebra, and let \(w(H)\) be the proportion of elements \(a\in H\) satisfying \(\neg a\vee\neg\neg a=\top\). If \(H\) has \(n\ge3\) join-irreducible elements and \(w(H)<1\), then
\[
w(H)\le\frac{2^{n-2}+1}{2^{n-2}+3}.
\]
Equality holds exactly for the downset Heyting algebra of \(A_2\oplus A_{n-2}\), the ordinal sum of a two-point antichain below an \((n-2)\)-point antichain. Thus \(2/(2^{n-2}+3)\) is the smallest positive failure proportion at fixed join-irreducible count. The previously known componentwise counting identity is a tool in the proof, not a second novelty claim.

## Assumptions and scope

The sampling is uniform on the elements of \(H\). Write \(H=J(P)\) under finite Birkhoff representation, with \(P\) the poset of join-irreducibles and \(J(P)\) its downset algebra, including the empty ideal. Components are for the undirected comparability graph. The pseudocomplement is \(\neg a=a\to\bot\). The bound concerns nonvalidity of this one-variable weak excluded-middle equation, not ordinary excluded middle or a binary failure count. The parameter is \(|P|\), not \(|H|\).

## Proof

**Counting ingredient (previously known).** In the downset convention the component formula from [1] is
\[
\#\{I\in J(P):\neg I\cup\neg\neg I=P\}
=\prod_C \bigl(1+|J(C\setminus\operatorname{Min}(C))|\bigr).
\]
To see it directly, let \(M(p)\) be the set of minima below \(p\), and \(S\) the minima included in \(I\). By the definition of the pseudocomplement, \(p\in\neg I\) exactly when \(M(p)\cap S=\varnothing\); likewise \(p\in\neg\neg I\) exactly when \(M(p)\subseteq S\). Indeed, a minimum below \(p\) that is missing from \(I\) witnesses failure of the second condition, whereas if all such minima are in \(I\), every point below \(p\) has an element of \(I\) below it. Inside a component all minima are linked by successive common upper bounds: the nonempty cliques \(M(p)\) overlap at successive vertices of any comparability path, by inclusion for comparable vertices. Hence every point is covered by one of the two pseudocomplements exactly when on each component \(S\) contains no minimum or all minima. An ideal in the first case is empty in that component; in the second case deleting the minima leaves an arbitrary ideal of the remaining induced poset. This proves the identity and shows validity exactly when every component has only one minimum. The formula also holds for the empty poset by the empty product convention.

**Extremal inequality.** Take a component \(C\) with \(s\) points and \(m\ge2\) minima, and let \(G,B\) count its satisfying and failing ideals, respectively. The formula gives \(G\le 1+2^{s-m}\le 1+2^{s-2}\). Every nonempty proper subset of the minima is a failing ideal, so \(B\ge 2^m-2\ge2\). Since \(B/(B+G)\) is strictly increasing in \(B\) and strictly decreasing in \(G\) for positive counts,
\[
1-w(J(C))\ge \frac{2}{2^{s-2}+3}.
\]
Equality requires \(m=2\), the upper bound \(G=1+2^{s-2}\) and exactly two failing ideals. The upper bound on \(G\) is attained only when the nonminima are an antichain. If any nonminimum were above just one minimum, its principal ideal would be an additional failing ideal. Thus every nonminimum is above both, and \(C=A_2\oplus A_{s-2}\) up to isomorphism. Conversely that order has exactly two failing ideals (the singleton minima) and \(1+2^{s-2}\) satisfying ideals.

For any \(P\) giving \(w(H)<1\), such a component exists. The probabilities multiply over components, so \(w(H)\le w(J(C))\le(2^{s-2}+1)/(2^{s-2}+3)\). The last expression is strictly increasing in \(s\), and \(s\le n\); global equality therefore forces \(s=n\). This proves the result and its equality characterization, including \(n=3\).

## Verification and limits

The unchanged companion `verify_wem.py` evaluates both pseudocomplements exactly on all naturally labeled posets through six vertices and cross-checks the stated extremal family through size sixteen (direct success enumeration through thirteen). These bounded checks corroborate the result; the proof above applies at all sizes. This is not a characterization of every attainable proportion.

## Relationship to prior work

The joint satisfaction table in [1] gives the same marginal component identity in the upset convention; reversing the order exchanges maxima with minima. Bumpus and Kocsis [2] show that weak excluded middle has no uniform positive satisfiability gap across finite algebras. The bound here identifies the best positive gap at each fixed join-irreducible count and the unique order that attains it. Lávička, Moraschini and Raftery [3] study global validity and the connection with \(\mathbf{KC}\). The related second-De-Morgan comparison in [4] concerns ordered pairs and equality between two defect counts, and includes the family \(J(A_2\oplus Q)\) with two unary failures. To obtain the present optimum one must bound the unary failure *proportion* against all other nonvalid types, including disconnected orders, and then identify the unique maximizing \(Q\) at fixed size.

## References

1. *Joint weak-excluded-middle and double-negation spectra on finite Heyting frames*, [Resultary record 826a5e04fbd5](https://github.com/Resultary/2026/tree/main/2026/10/18/SCOPE-joint-weak-excluded-middle-and-double-negation-spectra-on-finite--826a5e04fbd5), Finding and proof of component count.
2. B. M. Bumpus and Z. A. Kocsis, *Degree of Satisfiability in Heyting Algebras*, [arXiv:2110.11515](https://arxiv.org/abs/2110.11515), Theorems 2.4 and 2.19, and Section 6.6.
3. T. Lávička, T. Moraschini and J. G. Raftery, *The Algebraic Significance of Weak Excluded Middle Laws*, [arXiv:2108.09168](https://arxiv.org/abs/2108.09168), Introduction and Theorem 8.5.
4. *Sharp first-defect rigidity for the second De Morgan law in finite Heyting algebras*, [Resultary record 30a6c75e00c5](https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-sharp-first-defect-rigidity-for-the-second-de-morgan-law-in-fini--30a6c75e00c5), Finding and rigidity proof.
