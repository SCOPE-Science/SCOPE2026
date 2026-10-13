# An exact parity dichotomy for cyclic automata with alternating successor collapse

## Finding
For every integer \(n\ge2\), put \(Q_n=\mathbb Z/n\mathbb Z\). On its representatives \(0,1,\ldots,n-1\), define the binary automaton with letters
\[
a(i)=i+1\pmod n,\qquad b(i)=\begin{cases}i+1\pmod n,&i\text{ even},\\i,&i\text{ odd}.\end{cases}
\]
A reset word sends every initial state to the same final state, and \(R(n)\) is its minimum length, with \(R(n)=\infty\) when none exists. **The exact parity classification is**
\[
R(n)=\begin{cases}1,&n=2,\\
\infty,&n\ge4\text{ even},\\
(n^2-3n+4)/2,&n\ge3\text{ odd}.
\end{cases}
\]
For \(n=2k+1\ge5\), an optimal word (read left to right) is
\[
W_k=b^2\left(\prod_{j=1}^{k-2}a^{n-2j}ba^{2j}b\right)a^3b^2,
\]
with the product in increasing \(j\). At \(n=3\), the optimal word is \(b^2\). Thus the same natural alternating rule changes from nonsynchronizing to a quadratic exact threshold according to the parity of the cycle length.

## Assumptions and scope
The parity in the definition of \(b\) refers to the canonical integer representatives, not an abstract parity homomorphism on an odd cyclic group. The rule at the seam is important: if \(n\) is odd, \(b(n-1)=0\) and \(b(0)=1\), so \(b\) is **not idempotent**; it has a two-step chain. All letters have unit word cost; no additional transition letters are present. The theorem includes every integer \(n\ge2\), but not other simultaneous-merger configurations.

## Proof
**Even cycles and the three-state case.** If \(n\ge4\) is even, the image of \(b\) on \(Q_n\) is exactly the \(n/2\)-element odd class \(O\). The full cycle \(a\) interchanges the odd and even parity classes, and \(b\) sends either complete parity class bijectively onto \(O\). Before the first \(b\), a word preserves the full state set. After the first \(b\), every subsequent letter preserves image cardinality \(n/2>1\). No reset word exists. At \(n=2\), \(b\) itself is constant. For \(n=3\), direct inspection shows that \(b^2\) is constant and neither letter is constant, giving \(R(3)=2\).

**Upper bound on odd cycles.** Now let \(n=2k+1\ge5\). After \(b^2\), the image is \(S_0=\{1,3,\ldots,n-2\}\). For \(1\le j\le k-2\), define \(S_{j-1}=\{2j-1,2j+1,\ldots,n-2\}\). Applying \(a^{n-2j}b\) sends it to \(\{0,1,3,\ldots,n-2j-2\}\); applying \(a^{2j}b\) next yields \(S_j=\{2j+1,2j+3,\ldots,n-2\}\). Thus the product removes one state per two applications of \(b\). At the end \(S_{k-2}=\{n-4,n-2\}\), and \(a^3b^2\) sends this set successively to \(\{n-1,1\}\), \(\{0,1\}\), and \(\{1\}\). Consequently \(W_k\) resets the automaton. It contains \(2k\) copies of \(b\) and \((k-2)n+3\) copies of \(a\), hence has length \(2k^2-k+1=(n^2-3n+4)/2\).

**Inverse intervals.** To show optimality, we give a potential on the complete family of possible reverse reachable sets. For \(1\le L<n\), let \(I_{L,s}=\{s,s+1,\ldots,s+L-1\}\pmod n\), where \(0\le s<n\). The end and start of a proper cyclic interval are unambiguously specified, even when the interval crosses \(0\). Inverse \(a\) sends \(I_{L,s}\) to \(I_{L,s-1\bmod n}\). Put \(e=(s+L-1)\bmod n\), \(\alpha=\mathbf1_{\{s=0\text{ or }s\text{ odd}\}}\), and \(\beta=\mathbf1_{\{e\text{ even}\}}\). Directly from the fibers \(b^{-1}(0)=\{n-1\}\), \(b^{-1}(t)=\{t-1,t\}\) for odd \(t\), and \(b^{-1}(t)=\varnothing\) for even \(t\ne0\), one obtains
\[
b^{-1}(I_{L,s})=I_{L+\alpha-\beta,\,s-\alpha\bmod n}.
\]
An interval with length zero means the empty set; if the length becomes \(n\), the expression means the entire state set. The formula covers the wrap-around seam and shows that every nonempty iterated inverse image of a singleton is a cyclic interval or the full set.

**A global lower-bound potential.** Write \(n=2k+1\). For a proper nonempty cyclic interval define \(P(I_{L,s})\) by
\[
P(I_{1,s})=0,\qquad P(I_{2,s})=1,
\]
\[
P(I_{2j+1,s})=jn+1-s\qquad (3\le 2j+1<n),
\]
\[
P(I_{2j,s})=\begin{cases}(j-1)n+1-s,&s\le n-2j-1,\\jn+1-s,&s\ge n-2j,\end{cases}
\qquad (4\le2j<n),
\]
and \(P(Q_n)=(k-1)n+2=2k^2-k+1\). We claim that for either input letter \(c\in\{a,b\}\) and every nonempty reverse image, the **one-step potential inequality** is
\[
P(c^{-1}(I))\le P(I)+1.
\]
For the rotation \(a\), all interior changes of the start point reduce \(s\) by one and raise \(P\) by at most one. On crossing the exceptional even-length boundary \(s=n-L\), the potential drops by \(n-1\); the wrap from \(s=0\) to \(s=n-1\) changes it by at most one. The cases \(L=1,2\) and \(L=n\) are immediate.

Here is a complete arithmetic check for inverse \(b\). Distinguish the **nonwrapping case** \(s+L-1<n\) from the wrapping case \(s+L-1\ge n\), and the parity of \(s\). For odd \(L\ge3\): in the nonwrapping case, \(s=0\) leaves \(L\) unchanged and replaces \(s\) by \(n-1\), lowering \(P\) by \(n-1\); odd \(s>0\) gives length \(L+1\), start \(s-1\), and raises \(P\) by exactly one; even \(s>0\) gives length \(L-1\) and lowers \(P\) by \(n\), except at \(L=3\) where the special value \(P(I_{2,s})=1\) is smaller still. In the wrapping case, odd \(s\) keeps \(L\) and raises \(P\) by one, while even \(s\) leaves both unchanged. For even \(L\ge4\): nonwrapping \(s=0\) grows to length \(L+1\) and raises \(P\) by one; nonwrapping odd \(s\) keeps \(L\) and raises \(P\) by one, **except** at \(s=n-L\), where \(P\) drops by \(n-1\); nonwrapping even \(s>0\) is unchanged. Wrapping odd \(s\) grows to length \(L+1\) and raises \(P\) by one, except when \(L=n-1\), where the resulting full set has potential increase \(s-n+1\le0\). Wrapping even \(s\) shrinks to \(L-1\) and lowers \(P\) by \(n\). For \(L=2\), direct substitution gives maximum increment one (and possible empty inverse sets are discarded); for \(L=1\), any nonempty inverse has potential at most one; for \(L=n\), the inverse is full. This exhausts the possibilities and proves the inequality.

Now let \(w=c_1\cdots c_T\) be *any* reset word with final state \(q\). Starting with \(\{q\}\), apply the inverses \(c_T^{-1},\ldots,c_1^{-1}\) successively. All intermediate sets are nonempty and, by the inverse-interval formula, are cyclic intervals until they become \(Q_n\). The potential starts at zero and ends at \(2k^2-k+1\); since each inverse step can raise it by at most one, \(T\ge2k^2-k+1\). The displayed word attains equality, completing the proof.

## Verification
Run `python3 artifacts/verify.py` with the Python standard library. The checker independently performs subset-automaton breadth-first search for every \(2\le n\le19\), compares the exact reset distance or nonsynchronizability with the theorem, replays the explicit odd-cycle witnesses for all odd \(3\le n\le151\), and tests all rotation/preimage/potential transition cases for odd \(5\le n\le101\). On the accompanying file it prints:

```
VERIFY_OK bfs_n=2..19 bfs_cases=18 witness_odd_n=3..151_count=75 inverse_potential_edges=347214
```

The proof of the infinite classification is the preceding symbolic argument. Neither finite search nor the reported test counts are used to justify untested values.

## Relationship to prior work
Gusev's Eulerian family (2011/2013) has **the same numerical odd-order threshold** \((n^2-3n+4)/2\); that coincidence is explicitly acknowledged. The Gusev construction uses two nonpermutation letters, one idempotent and the other nearly idempotent. Here one letter is an \(n\)-cycle permutation, and the second alternately merges adjacent pairs with a nonidempotent two-step seam when \(n\) is odd. The families are not isomorphic as letter-preserving automata: one has an invertible generator and the other does not. Thus Gusev's exact theorem does not by itself determine the threshold here; no claim of a new extremal numerical value is made. Volkov's public exposition reproduces Gusev's transitions and proof (Lecture V, pages 20–23 of the slide deck). Volkov's 2018 low-rank-idempotent constructions concern a different alphabet/rank condition, and Rystsov–Szykuła's transformation-monoid results concern monoid bounds and generators with one point of contraction rather than this multiple-pair letter. Eppstein's general interval approach motivates the reverse interval method, but does not give the present explicit parity classification and sharp polynomial. A separate cyclic pair-compression problem with an **idempotent** parity map has a different asserted odd threshold; that map is not conjugate to the present nonidempotent \(b\). An exhaustive originality comparison against related indexed statements and accessible technical papers did not reveal a covering implication.

## Limitations
The conclusion is specific to the exact cyclic shift and the exact simultaneous parity-dependent successor map above. The potential is constructed for odd \(n\ge5\), while the small cases are proved separately. It does not assert a new universal synchronization bound or give an optimal word for a different alternating collapse. Priority beyond the consulted indexed and publicly accessible literature requires independent checking. Gusev's original journal paper was accessible only in partial publisher preview; the accessible full technical reconstruction of its automaton and proof is used for the distinction.

## References
1. V. V. Gusev, *Lower Bounds for the Length of Reset Words in Eulerian Automata*, Reachability Problems (2011), DOI:10.1007/978-3-642-24288-5_16; extended version, International Journal of Foundations of Computer Science 24(2) (2013), 251–262, DOI:10.1142/S0129054113400108.
2. M. V. Volkov, *Synchronization Finite Automata, Lecture V: Expansion Method*, pages 20–23, https://kadm.kmath.ru/files/synchroprint5.pdf (full technical account of Gusev's two-letter construction).
3. M. V. Volkov, *Slowly Synchronizing Automata with Idempotent Letters of Low Rank*, arXiv:1807.07048, first posted 18 July 2018, https://arxiv.org/abs/1807.07048.
4. I. Rystsov and M. Szykuła, *Reset Thresholds of Transformation Monoids*, arXiv:2309.08321, first posted 15 September 2023, https://arxiv.org/abs/2309.08321.
5. Y. Zhu, *A Quadratic Upper Bound on the Reset Thresholds of Synchronizing Automata Containing a Transitive Permutation Group*, arXiv:2407.08135, first posted 11 July 2024, https://arxiv.org/abs/2407.08135.
6. D. Eppstein, *Reset Sequences for Monotonic Automata*, SIAM Journal on Computing 19 (1990), 500–510, https://ics.uci.edu/~eppstein/pubs/Epp-SJC-90.pdf.
7. *Reset threshold of the cyclic pair-compression automaton*, TheoremDB problem P2560, https://www.theoremdb.org/statements/cyclic-pair-compression-reset-threshold/ (a different idempotent variant; its asserted polynomial is not used here).
