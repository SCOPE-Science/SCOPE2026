# Exact Dyck-factor starting positions and multiplicities in the paperfolding word
## Finding
Let \(\mathbf p=p_1p_2\cdots\) be the regular paperfolding word defined, for every \(n\ge1\), by
\[
p_n=\begin{cases}
0,&\text{the odd part of }n\text{ is }1\pmod4,\\
1,&\text{the odd part of }n\text{ is }3\pmod4.
\end{cases}
\]
Interpret \(0\) as an opening parenthesis and \(1\) as a closing parenthesis. A nonempty factor is **Dyck** if it has equal numbers of the two symbols and every prefix has at least as many \(0\)'s as \(1\)'s.

For integers \(K\ge2\), \(1\le r<K\), put
\[
L_{K,r}=2^K-2^r,\qquad P_K=2^{K+1}.
\]
Then **every** Dyck-factor occurrence in \(\mathbf p\) is described by the following exact law:

* The nonempty Dyck-factor lengths are precisely the integers \(L_{K,r}\) above, and each such integer determines a unique \((K,r)\).
* For the length \(L_{K,r}\), the factor beginning at the one-based symbol position \(a+1\), with \(a\ge0\), is Dyck **if and only if**
\[
a\equiv2^r-1\quad\text{or}\quad a\equiv2^K\pmod{P_K}.
\]
* Exactly **one** distinct Dyck word occurs for \(L=2\) and for \(L=4\); at every other permitted length exactly **two** distinct Dyck words occur. The two words at each length are represented by the factors starting at the boundary offsets \(a=2^r-1\) and \(a=2^K\).

For each fixed \(L_{K,r}\), its set of starting boundary offsets has natural density \(2^{-K}\). More precisely, for every \(M\ge K+1\), the prefix of \(\mathbf p\) of length \(2^M-1\) contains exactly \(2^{M-K}\) Dyck occurrences of that fixed length. Equivalently, the permitted **semilengths** are precisely \(2^k-2^i\), where \(0\le i<k\); the full length is twice the semilength.

## Assumptions and scope
A starting *boundary offset* \(a\) means the factor is \(p_{a+1}\cdots p_{a+L}\). This convention avoids confusion between a symbol index and the integer position of its preceding prefix boundary.

The theorem concerns the ordinary regular paperfolding word with the displayed odd-part convention. It does not claim the same support or residue classes for an arbitrary generalized paperfolding sequence.

The word-count assertion counts **distinct factor words**, not occurrences; the occurrence-density assertion counts starting offsets. All congruences are in ordinary nonnegative integers. The empty Dyck word is excluded. 

## Proof
Define the signed parenthesis increment and prefix height by
\[
\epsilon_n=1-2p_n,\qquad H(0)=0,\qquad H(N)=\sum_{n=1}^N\epsilon_n.
\]
Let \(G(N)=N\mathbin{\mathrm{xor}}\lfloor N/2\rfloor\), the binary reflected Gray code, and let \(w(N)\) denote the number of \(1\)-bits in \(G(N)\).

**Gray-height identity.** Consecutive Gray codes differ in exactly the bit indexed by \(t=\nu_2(N)\). In \(G(N)\), that bit is \(1\) exactly when the second-lowest bit in the odd part of \(N\) is \(0\), namely when the odd part is \(1\pmod4\). Thus
\[
w(N)-w(N-1)=\epsilon_N.
\]
Since both functions vanish at \(0\), we obtain
\[
H(N)=w(N)\qquad(N\ge0).
\]
In particular, the factor between offsets \(a\) and \(b\), with \(0\le a<b\), is Dyck exactly when
\[
H(a)=H(b)\quad\text{and}\quad H(t)\ge H(a)\text{ for all }a\le t\le b.
\]

**Classification by reflected halves.** For an integer \(m\ge1\), let \(\mathcal H_m\) be the finite list \((H(0),\ldots,H(2^m-1))\). The reflected Gray construction gives
\[
\mathcal H_m=\mathcal H_{m-1}\ \Vert\ (1+\operatorname{rev}\mathcal H_{m-1}).
\]
Here \(\Vert\) is concatenation. The only zero-height point of \(\mathcal H_m\) is its first entry, because Gray coding is a bijection; the height-one entries are exactly at offsets
\[
1,3,7,\ldots,2^m-1.
\]
(The Gray code has a single nonzero bit precisely at those indices.)

Suppose a nonempty Dyck interval \([a,b]\) in \(\mathcal H_m\) crosses the midpoint \(2^{m-1}\). Its leftmost midpoint-adjacent height is \(H(2^{m-1}-1)=1\), while every height in the right half is at least \(1\). Equal endpoint heights together with the Dyck lower-bound condition force the common endpoint height to equal \(1\). By the reflected-half formula, the unique height-one position in the right half is the final index \(b=2^m-1\). On the left, \(a\) must be \(2^r-1\) for some \(1\le r<m\). Therefore every crossing Dyck interval is exactly
\[
[a,b]=[2^r-1,2^m-1],\qquad b-a=2^m-2^r.
\]
Conversely, these intervals are Dyck: their endpoints have height one and all intermediate positive-index heights are at least one.

Intervals lying wholly inside the first half are copies of intervals in \(\mathcal H_{m-1}\). Intervals in the second half are reflected, height-shifted copies and retain the Dyck condition. Induction on \(m\) therefore proves that every possible nonempty Dyck length, at every finite depth and hence in the infinite word, is \(2^K-2^r\), \(1\le r<K\). Each occurs by its displayed crossing witness. Its pair of exponents is unique because the exact power of two dividing the length is \(2^r\) and the remaining odd factor is \(2^{K-r}-1\).

**The complete starting-position law.** Fix \((K,r)\), and abbreviate \(L=2^K-2^r\), \(P=2^{K+1}\). At depth \(K\), the unique occurrence is the crossing interval starting at \(2^r-1\). At depth \(K+1\), its first-half copy starts at \(2^r-1\), and its reflected second-half copy starts at
\[
2^{K+1}-1-\bigl((2^r-1)+L\bigr)=2^K.
\]
There are no new midpoint-crossing intervals of length \(L\) at any depth \(m>K\), because such an interval at depth \(m\) has length at least \(2^{m-1}\ge2^K>L\). Every subsequent copy of an \(L\)-interval lies in one half. Reflection at depth \(m\ge K+2\) sends a start \(a\) to
\[
a'=2^m-1-(a+L),
\]
which exchanges the residues \(2^r-1\) and \(2^K\) modulo \(P\); translation by a half-block of size divisible by \(P\) preserves those residues. Induction therefore shows that **all** starts have one of these two residues.

For the reverse implication, a candidate interval with \(a\equiv2^r-1\pmod P\) occupies, within its \(P\)-block, exactly the positions from \(2^r\) to \(2^K-1\). A candidate with \(a\equiv2^K\pmod P\) occupies positions from \(2^K+1\) to \(P-2^r\). Neither interval contains a symbol index divisible by \(2^K\). For any such index \(n\), the odd part of \(n+P\) is congruent modulo four to the odd part of \(n\), hence \(p_{n+P}=p_n\). Every factor at one of the two starting residues thus equals the corresponding already-verified canonical Dyck factor. This proves sufficiency and the exact position classification.

There are exactly two allowed starts per complete block of size \(P\). Thus the natural density is \(2/P=2^{-K}\), and there are exactly \(2^{M-K}\) starts whose factors lie in the prefix of length \(2^M-1\) whenever \(M\ge K+1\): the starts in the final block finish no later than its final symbol.

**Distinct factor count.** The preceding periodicity shows that at most two distinct Dyck words occur at length \(L\). At length \(2\) the two canonical factors are both \(01\); at length \(4\) both are \(0011\). For all other permitted lengths they differ. Indeed, compare the two canonical factors at one-based relative position \(t\):

* If \(r=1\), \(K\ge3\), take \(t=2\). The first canonical factor has symbol \(p_3=1\), while the second has \(p_{2^K+2}=0\).
* If \(r=2\), \(K\ge4\), take \(t=4\). The first has \(p_7=1\), while the second has \(p_{2^K+4}=0\).
* If \(r\ge3\), take \(t=2^{r-1}+1\). The first has \(p_{3\cdot2^{r-1}}=1\), while the second has \(p_{2^K+2^{r-1}+1}=0\).

All these comparisons follow immediately by reducing the odd parts modulo four. This proves the exact one-versus-two classification and completes the theorem.

## Verification
Run `python3 verify.py` beside `certificate.json`. The verifier constructs the paperfolding word independently from its odd-part rule and its predicted Gray-code height and confirms equality of signed prefix heights through \(2^{18}\) indices.

For every Gray-prefix depth \(2\le m\le12\), it enumerates **all** Dyck intervals in the entire \(2^m\)-entry height path and compares their length-to-start sets with the asserted congruences, not merely the number of observed lengths. It also checks the distinct-word classification for \(2\le K\le12\), stability under eight successive block translations, and the exact finite-prefix occurrence counts.

These checks do not establish the theorem for unbounded lengths; that follows from the recursive reflected-half induction and the odd-part invariance in the proof.

## Relationship to prior work
Mol, Rampersad, and Shallit explicitly raise a power-of-two-difference conjecture for Dyck factors of the regular paperfolding word in the last section of their paper *Dyck Words, Pattern Avoidance, and Automatic Sequences*. The paper's full text gives exact Dyck descriptions for other classical words, and its period-doubling proposition permits only three nonempty Dyck words, but it does not give all paperfolding factor starting positions or the number of distinct Dyck factors of any permitted length.

The length-support statement alone is an existential criterion and is not asserted here as a separate novel result. The contribution is the **complete occurrence-locus formula**, which decides the Dyck property of every individual factor in constant time from its length and starting residue, together with the **exact factor multiplicities** and occurrence densities. The proof uses a reflected binary Gray-code height model instead of a brute-force list of factors.

Work on Gray-code listings of Dyck words addresses a different object: it orders Dyck words themselves in a Gray code, rather than studying Dyck intervals inside the fixed paperfolding word. Standard descriptions of binary reflected Gray codes supply the elementary recursion used here but do not state the occurrence classification.

## Limitations
The classification uses the regular paperfolding word, not every generalized paperfolding word. It concerns nonempty Dyck factors and distinguishes distinct factors from their infinitely many occurrences. It does not classify nesting levels or other parenthesis alphabets. An older unindexed derivation from Gray-code weight paths remains a residual originality risk.

## References
1. L. Mol, N. Rampersad, and J. Shallit, “Dyck Words, Pattern Avoidance, and Automatic Sequences,” arXiv:2301.06145v1, first public 2023-01-15; *Communications in Mathematics* 33 (2025), no. 2, paper 5, DOI 10.46298/cm.12695. In particular, Section 6, Conjecture 6.5.
2. V. Vajnovszki and D. Wong, “Greedy Gray Codes for Dyck Words and Ballot Sequences,” in *Computing and Combinatorics*, LNCS 14423 (2024), pp. 29–40, DOI 10.1007/978-3-031-49193-1_3 (distinct Gray-code enumeration problem).
