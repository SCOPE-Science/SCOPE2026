# Exact \(k\)-avoiding thresholds of the Wielandt automata
## Finding
Let \(W_n\) be the deterministic automaton, for \(n\ge 3\), with state set \(Q=\mathbb Z/n\mathbb Z\) and alphabet \(\{b,c\}\), where
\[
b(i)=i+1\pmod n,
\]
and
\[
c(0)=c(1)=2,\qquad c(i)=i+1\pmod n\quad(2\le i<n).
\]
For a proper subset \(S\subset Q\), let \(d(S)\) be the minimum length of a word \(w\) such that \(Qw\cap S=\varnothing\). The \(k\)-avoiding threshold is
\[
\operatorname{at}_k(W_n)=\max_{|S|=k}d(S).
\]
Then, for every \(1\le k<n\),
\[
\operatorname{at}_k(W_n)=k(n-1)+1.
\]
The unique maximizing \(k\)-subset is
\[
B_{n,k}=\{0\}\cup\{n-k+1,\ldots,n-1\},
\]
where the second set is empty when \(k=1\). A shortest word avoiding it is
\[
w_{n,k}=(cb^{n-2})^{k-1}cb^{n-1}.
\]

## Assumptions and scope
All state arithmetic is modulo \(n\), while displayed representatives lie in \(\{0,1,\ldots,n-1\}\). Word length counts letters in the alphabet \(\{b,c\}\). A word avoids \(S\) precisely when no state of \(Q\) is mapped into \(S\). The statement covers every \(n\ge3\) and every nonempty proper target size \(1\le k<n\).

The automaton is the usual Wielandt automaton up to relabeling of states and letters. The 2010 source defines the underlying Wielandt digraph and its unique binary coloring and proves reset threshold \(n^2-3n+3\). The present claim concerns the different invariant of avoiding prescribed subsets.

## Proof
For a subset \(P\subseteq Q\), write \(P\ell^{-1}\) for its full preimage under a letter \(\ell\). Since \(b\) is the cyclic shift,
\[
Pb^{-1}=P-1.
\]
The only difference between the inverse actions of \(b\) and \(c\) is membership of state \(0\): \(0\in Pb^{-1}\) exactly when \(1\in P\), whereas \(0\in Pc^{-1}\) exactly when \(2\in P\). Consequently,

- if \(1\in P\) and \(2\notin P\), then \(Pc^{-1}=Pb^{-1}\setminus\{0\}\), so \(c^{-1}\) decreases cardinality by one;
- if \(1\notin P\) and \(2\in P\), then \(Pc^{-1}=Pb^{-1}\cup\{0\}\), so it increases cardinality by one;
- otherwise \(Pc^{-1}=Pb^{-1}\).

A word \(w\) avoids \(P\) exactly when \(Pw^{-1}=\varnothing\). In a shortest inverse path from \(P\) to \(\varnothing\), any occurrence of \(c^{-1}\) that enlarges the current set can be replaced by \(b^{-1}\): the replacement produces a subset, and all later inverse actions preserve inclusion. If \(c^{-1}\) agrees with \(b^{-1}\), replace it by \(b^{-1}\) as well. Thus some shortest path is normalized so that every occurrence of \(c^{-1}\) is cardinality-decreasing. Exactly \(k\) such occurrences are then needed from a \(k\)-set. Between them there are only rotations by \(b^{-1}\), and no block needs \(n\) rotations because \(b^n\) is the identity.

Suppose the current nonempty proper set is \(P\). After \(r\) inverse rotations, with \(0\le r<n\), a deleting \(c^{-1}\) is possible precisely when, for \(p=r+1\pmod n\),
\[
p\in P,\qquad p+1\notin P.
\]
Thus \(p\to p+1\) is an occupied-to-empty cyclic boundary. The deletion costs
\[
r+1=\begin{cases}p,&1\le p\le n-1,\\ n,&p=0,\end{cases}
\]
and the new set is
\[
(P\setminus\{p\})-p.
\]

Now fix \(k\). If a \(k\)-set \(P\) is not \(B_{n,k}\), it has an occupied-to-empty boundary \(p\ne0\). Indeed, a nonempty proper cyclic set whose only such boundary is \(0\to1\) must be exactly \(\{0\}\cup\{m,m+1,\ldots,n-1\}\), and cardinality then forces \(m=n-k+1\). Delete at a boundary \(p\ne0\). This costs at most \(n-1\), and the resulting set omits both \(0\) (the deleted state) and \(1\) (the image of the already absent successor \(p+1\)). Hence every subsequent nonempty set has no boundary at \(p=0\), so each later deletion also costs at most \(n-1\). Therefore
\[
d(P)\le k(n-1)\qquad(P\ne B_{n,k}).
\]

For \(B_{n,k}\), the only occupied-to-empty boundary is \(0\to1\). Hence the first normalized deletion necessarily costs \(n\) and leaves
\[
T_{k-1}=\{n-k+1,\ldots,n-1\}.
\]
For \(j\ge1\), the tail \(T_j=\{n-j,\ldots,n-1\}\) has the unique occupied-to-empty boundary \(n-1\to0\). Its forced deletion costs \(n-1\) and sends \(T_j\) to \(T_{j-1}\). Thus every avoiding word for \(B_{n,k}\) has length at least
\[
n+(k-1)(n-1)=k(n-1)+1.
\]
The word \(w_{n,k}=(cb^{n-2})^{k-1}cb^{n-1}\) realizes exactly these inverse deletion blocks, from right to left, so equality holds. The strict bound for every other \(k\)-set proves uniqueness of the maximizer.

## Verification
The standalone verifier `artifacts/verify_wielandt_avoiding.py` constructs the full image-subset automaton and computes exact shortest avoidance distances. Exhaustive checks for every \(3\le n\le11\) and every \(1\le k<n\) confirm both the formula and uniqueness of \(B_{n,k}\). It also replays the explicit witness for every parameter pair with \(3\le n\le40\). Its recorded output ends with `VERIFY_OK`.

These finite computations are cross-checks, not the proof of the infinite statement. The all-parameter conclusion rests on the inverse-action normalization and cyclic-boundary argument above.

## Relationship to prior work
Ananichev, Gusev, and Volkov introduced the binary Wielandt automata in this form (up to relabeling), proving the reset threshold \(n^2-3n+3\). Gusev and Pribavkina later placed \(W_n\) inside a larger two-cycle family and again studied reset thresholds. Neither source states avoiding thresholds.

Ferens, Szykuła, and Vorel define \(k\)-avoiding thresholds and study general bounds; their paper gives the four-state Černý example but does not mention the Wielandt automata. A published record subsequently gives the exact formula \(kn\) for the Černý series. That result does not imply the theorem here: \(W_n\) has a different nonpermutation letter and a different inverse boundary cost, even though \(W_n\) is related to an induced action inside the classical Černý construction.

The extension literature was also checked because avoidance of \(S\) is equivalent to total extension of \(Q\setminus S\). Kisielewicz and Szykuła study difficult extension in different automata and do not treat \(W_n\). Don's 1-contracting results give reachability mechanisms and upper bounds for certain circular automata but do not state the exact \(k\)-avoiding profile above. Volkov's survey discusses both \(W_n\) and avoidability, but in separate contexts and without this formula.

## Limitations
Originality is asserted to the best of the searches and source inspections described in the accompanying review, not as a proof that no equivalent statement exists in older terminology. The main residual risk is an unindexed subset-reachability or total-extension treatment of the Wielandt automata that implicitly contains the same exact distances.

The theorem is labeling-sensitive only in its description of the unique extremal subset: under an isomorphism, the corresponding image of \(B_{n,k}\) is the unique extremal target. The numerical threshold itself is isomorphism-invariant.

## References
1. D. S. Ananichev, V. V. Gusev, M. V. Volkov, *Slowly synchronizing automata and digraphs*, arXiv:1005.0129v1, 2010, https://arxiv.org/abs/1005.0129.
2. V. V. Gusev, E. V. Pribavkina, *Reset thresholds of automata with two cycle lengths*, arXiv:1403.3992, 2014, https://arxiv.org/abs/1403.3992.
3. H. Don, *The Černý Conjecture and 1-Contracting Automata*, Electronic Journal of Combinatorics 23(3), P3.12, 2016, https://doi.org/10.37236/5616.
4. A. Kisielewicz, M. Szykuła, *Synchronizing Automata with Extremal Properties*, arXiv:1608.01268v1, 2016, https://arxiv.org/abs/1608.01268.
5. R. Ferens, M. Szykuła, V. Vorel, *Lower Bounds on Avoiding Thresholds*, MFCS 2021, https://doi.org/10.4230/LIPIcs.MFCS.2021.46.
6. M. V. Volkov, *Synchronization of finite automata*, Russian Mathematical Surveys 77(5), 2022, https://doi.org/10.4213/rm10005e.
