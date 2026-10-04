# Parity-alternating initial rank compression in the automata \(F_n\)
## Finding
For every odd \(n>3\), let \(F_n\) be the deterministic automaton on \(Q=\{1,\ldots,n\}\) with
\[
a(i)=\begin{cases}i,&i<n,\\2,&i=n,\end{cases}
\qquad
b(i)=\begin{cases}i+1,&i<n,\\1,&i=n.\end{cases}
\]
For \(1\le s<n\), define
\[
\lambda_n(s)=\min\{|w|:|Qw|\le n-s\}.
\]
Then, throughout the natural initial half-rank range \(1\le s\le(n+1)/2\),
\[
\lambda_n(s)=
\begin{cases}
3s-2,&s\text{ odd},\\
3s-3,&s\text{ even}.
\end{cases}
\]
Writing \(s=2r+1\), the word \(a(bab^3a)^r\) has length \(3s-2\) and image size \(n-s\). Writing \(s=2r\), the word \(a(bab^3a)^{r-1}ba\) has length \(3s-3\) and image size \(n-s\).

## Assumptions and scope
The state labels and letter actions are exactly those in the defining source. The theorem concerns odd \(n>3\) and only deficiencies \(s\) through \((n+1)/2\). No assertion is made here about the exact profile beyond that boundary.

The rank of a word means the cardinality of the image \(Qw\). The letter \(b\) is a permutation. The letter \(a\) has one collision pair, \(\{2,n\}\), and therefore lowers the image size by one exactly when both \(2\) and \(n\) are present immediately before it is applied.

## Proof
Fix odd \(n>3\) and a deficiency \(s\) in the stated range. Consider a shortest word \(w\) with \(|Qw|\le n-s\). Since \(b\) preserves image size and each occurrence of \(a\) lowers image size by at most one, the prefix ending at the \(s\)-th rank-lowering occurrence of \(a\) already has image size \(n-s\). Hence a shortest \(w\) ends at that occurrence and has exactly \(s\) effective occurrences of \(a\). Also \(a^2=a\), so \(w\) has no factor \(aa\).

Let \(d_i\) be the number of letters strictly between the \(i\)-th and \((i+1)\)-st effective occurrences of \(a\), for \(1\le i<s\). Immediately after every effective \(a\), state \(n\) is absent. Therefore \(d_i\ne0\). We also have \(d_i\ne2\). Indeed, if the two intervening letters were \(bb\), the missing state \(n\) would be carried by \(b^2\) to the missing state \(2\), so the following \(a\) could not be effective. Every other two-letter intervening word contains an \(a\); the possibilities beginning or ending in \(a\) create a forbidden factor \(aa\), except that an earlier intervening \(a\) would itself be the next effective occurrence. Thus each \(d_i\) is either \(1\) or at least \(3\).

If \(d_i=1\), the intervening letter must be \(b\). The rank-lowering factor is then \(aba\). The hole created at \(n\) by the first \(a\) is moved to \(1\) by \(b\), and the second \(a\) leaves that hole at \(1\) while creating a new hole at \(n\). Hence, immediately after this second effective \(a\), both \(1\) and \(n\) are absent. One more \(b\) would move the hole at \(1\) to \(2\), preventing the next \(a\) from being effective. Consequently \(d_i=1\) forces \(d_{i+1}\ge3\). It follows in every case that
\[
d_i+d_{i+1}\ge4.
\]
If \(s\) is odd, then \(s-1\) is even, so pairing all separators gives
\[
\sum_{i=1}^{s-1}d_i\ge2(s-1),
\]
and therefore \(|w|\ge s+2(s-1)=3s-2\). If \(s\) is even, pair the first \(s-2\) separators and use \(d_{s-1}\ge1\); this gives
\[
\sum_{i=1}^{s-1}d_i\ge2(s-2)+1=2s-3,
\]
so \(|w|\ge3s-3\).

It remains to meet these lower bounds. Write \(n=2m+1\). For \(r\ge0\), after the word \(a(bab^3a)^r\), the missing states are exactly
\[
\{n\}\cup\bigcup_{j=0}^{r-1}\{4j+3,4j+4\}.
\]
For \(r\ge1\), after the word \(a(bab^3a)^{r-1}ba\), the missing states are exactly
\[
\{1,n\}\cup\bigcup_{j=1}^{r-1}\{4j,4j+1\}.
\]
These identities follow simultaneously by induction: from an odd-profile hole set, applying \(ba\) shifts the old holes once and adds the new hole \(n\), producing the even-profile set; applying \(b^3a\) shifts that set three more places and adds \(n\), producing the next odd-profile set. The range assumptions prevent wraparound into \(n\) before each effective \(a\): for \(2r+1\le m+1\), the largest displayed ordinary label is \(4r\le2m=n-1\); for \(2r\le m+1\), the largest is \(4r-3\le n-2\). Thus every displayed \(a\) is effective and the hole sets have exactly \(s\) elements. The witnesses therefore attain the lower bounds.

## Verification
The standalone script `artifacts/verify.py` implements the automaton directly. Exact breadth-first search of the full power automaton reproduces every claimed value for all odd \(5\le n\le17\). A separate direct replay checks the witness lengths, image sizes, and the two explicit hole-set formulas for every odd \(5\le n\le301\). Running

`python3 artifacts/verify.py`

prints `VERIFY_OK`. These finite checks corroborate but do not replace the symbolic proof above.

## Relationship to prior work
Ananichev, Gusev, and Volkov define \(F_n\) and prove for odd \(n>3\) that its reset threshold is \(n^2-3n+3\). Their Theorem 7 concerns the rank-one endpoint and exhibits the much longer reset word \((ab^{n-2})^{n-2}a\). The defining subsection does not state shortest lengths for prescribed intermediate image ranks. A full-text search of the inspected source contains no occurrence of the term “rank”; the relevant subsection states the family definition and reset-threshold theorem only.

The present result is not implied by that endpoint theorem: it identifies every shortest length in the initial half-rank regime and shows a parity alternation caused by the local interaction of the unique collision \(\{2,n\}\) with the cyclic letter. Exact-claim, alias, and broader-coverage literature searches did not locate a prior statement of this profile.

## Limitations
The theorem deliberately stops at \(s=(n+1)/2\), where the explicit non-wrapping hole induction is guaranteed. It does not claim the later rank profile or the reset threshold. Literature searches and direct inspection substantially reduce, but cannot eliminate, the risk of an unindexed earlier equivalent statement.

## References
1. D. S. Ananichev, V. V. Gusev, M. V. Volkov, “Primitive digraphs with large exponents and slowly synchronizing automata,” arXiv:1302.5793, first submitted 2013-02-23; DOI:10.1007/s10958-013-1392-8.
2. D. S. Ananichev, V. V. Gusev, M. V. Volkov, “Slowly synchronizing automata and digraphs,” arXiv:1005.0129, 2010.
