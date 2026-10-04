# Exact linear chaining depth in the free-group boundary counterexample
## Finding
In the nonsingularized \(\mathbb F_2\)-boundary action constructed in Proposition 6.13 of Tserunyan and Zomback, let \(L\) denote the set of \(P\)-legal infinite reduced words and let \(B_n=[a^{2n+2}]\) for an integer \(n\ge 0\). Define the chaining depth from \(L\) to \(B_n\) to be the least integer \(k\ge 0\) for which there are group elements \(\gamma_0=e,\gamma_1,\ldots,\gamma_k\) such that consecutive translates \(\gamma_iL\) and \(\gamma_{i+1}L\) have positive \(\widetilde\mu\)-intersection and \(\gamma_kL\) has positive \(\widetilde\mu\)-intersection with \(B_n\).

The chaining depth is exactly \(n+1\). One minimizing chain is
\[
L,\ a^2L,\ a^4L,\ldots,\ a^{2n+2}L.
\]
Thus the witness cylinders used to prove failure of bounded chaining have an exact linear obstruction profile rather than only an unbounded lower bound.

## Assumptions and scope
The transition matrix \(P\) is the symmetric matrix chosen in Proposition 6.13: the transitions from a letter \(a^i\) to a letter \(b^j\), and from \(b^i\) to \(b^i\), are positive for \(i,j\in\{-1,1}\), while transitions from \(a^i\) to \(a^i\) vanish; the free-boundary convention also excludes immediate inverse cancellation. The Markov measure has a strictly positive initial distribution. The measure \(\widetilde\mu\) is the nonsingularization used in the paper, so every group translate preserves null sets.

The statement concerns only the specific sets \(L\) and \(B_n\) in that construction. It does not assert a formula for arbitrary measurable sets or for arbitrary transition matrices.

## Proof
The lower bound is the hard direction already established inside the proof of Proposition 6.13: for every positive integer \(n\), there is no \(n\)-chain from \(L\) to \(B_n=[a^{2n+2}]\), even after positive-measure intersections are weakened to nonempty intersections. Hence the required depth is at least \(n+1\). For \(n=0\), a zero-chain would require \(L\cap[a^2]\neq\varnothing\), but a legal word cannot begin with \(aa\) because \(P(a,a)=0\). Thus the same lower bound holds for \(n=0\).

For the matching upper bound, consider the positive Markov cylinder of legal words beginning with \(ab\). Its measure is positive because the initial weight of \(a\) is positive and \(P(a,b)>0\). If \(x=abx_2x_3\cdots\) is such a legal word, then left multiplication by \(a^{-2}\) reduces to
\[
a^{-2}x=a^{-1}bx_2x_3\cdots.
\]
The first transition remains legal because \(P(a^{-1},b)>0\), and every later transition is inherited from \(x\). Consequently this positive cylinder lies in \(L\cap a^2L\). Because \(\widetilde\mu\) is measure-class preserving under the group action, for every integer \(j\ge0\) the intersection
\[
a^{2j}L\cap a^{2j+2}L
\]
has positive \(\widetilde\mu\)-measure.

Finally, the set of legal words beginning with \(b\) has positive measure. Translating that set by \(a^{2n+2}\) causes no cancellation, so its image is a positive-measure subset of both \(a^{2n+2}L\) and \(B_n=[a^{2n+2}]\). Therefore
\[
L,\ a^2L,\ldots,\ a^{2n+2}L
\]
is an \(n+1\)-chain from \(L\) to \(B_n\). Combining the lower and upper bounds gives exact depth \(n+1\).

## Verification
The proof uses only three ingredients that are explicit in the cited construction: the definition of a \(k\)-chain, positivity of Markov cylinders whose transitions are allowed, and measure-class preservation after nonsingularization. The lower bound is the non-chaining argument in Proposition 6.13. The upper bound is checked directly by the two legal transitions \(a\to b\) and \(a^{-1}\to b\) and by a final legal word beginning with \(b\). No finite experiment, asymptotic estimate, or unverified computation is used.

## Relationship to prior work
Tserunyan and Zomback introduce bounded chaining and construct this \(\mathbb F_2\)-boundary example to separate chaining from bounded chaining. Their Proposition 6.13 supplies the family \(B_n=[a^{2n+2}]\) and proves the lower bound that \(L\) does not \(n\)-chain to \(B_n\). The inspected manuscript does not state a matching upper chain or the exact minimum. The argument above closes that quantitative gap by exhibiting an \(n+1\)-chain.

Earlier work on weak double ergodicity and ergodicity with isometric coefficients studies related one-step intersection properties, but it does not formulate this bounded-chain profile for the free-group boundary construction. The new statement is therefore a quantitative sharpening of the specific counterexample, not a new implication between the older ergodic properties.

## Limitations
The exact formula is proved only for the named witness family in Proposition 6.13. It does not classify chain depths between all cylinders, nor does it establish an optimal growth theorem for general nonsingular free-group actions. The literature comparison cannot exclude an unstated observation or later independent derivation; the full text of the source and the most directly related predecessor literature were inspected, and no statement implying this exact minimum was found.

## References
[1] A. Tserunyan and J. Zomback, “Bounded chaining in measurable dynamics,” arXiv:2609.18061v2 (2026), especially Definition 3.1 and Proposition 6.13. First public version: arXiv:2609.18061v1, 2026-09-16.

[2] I. Loh and C. E. Silva, “Strict Doubly Ergodic Infinite Transformations,” arXiv:1512.09340v4; *Dynamical Systems* 32 (2017).

[3] B. Haddock, J. Leng, and C. E. Silva, “Nonsingular transformations that are ergodic with isometric coefficients and not weakly doubly ergodic,” arXiv:2011.14278v1; *Indagationes Mathematicae* 33 (2022).
