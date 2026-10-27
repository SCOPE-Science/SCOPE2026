# Exact worst-case two-deletion list size in every binary VT syndrome class

## Finding
For every integer \(n\ge3\) and syndrome \(a\in\{0,\ldots,n\}\), define the binary Varshamov--Tenengolts class
\[
\mathrm{VT}_a(n)=\left\{x\in\{0,1\}^n:\sum_{i=1}^{n}i x_i\equiv a\pmod{n+1}\right\}.
\]
Write \(\mathcal I_2(y)\) for all distinct length-\(n\) binary supersequences of \(y\in\{0,1\}^{n-2}\). Then
\[
\boxed{\max_{y\in\{0,1\}^{n-2}}|\mathrm{VT}_a(n)\cap\mathcal I_2(y)|=\left\lfloor\frac n2\right\rfloor+1}\quad(n\ge3).
\]
Every syndrome has a matching explicitly constructible received word. This is a worst-case, per-syndrome two-deletion statement, not an average over words or syndromes.

## Assumptions and scope
The channel deletes exactly two arbitrary coordinates from binary words of length \(n\); distinct input words, not deletion position pairs, count toward a decoding list. Symbols are indexed from \(1\). All modular arithmetic is modulo \(N=n+1\). The exception \(n=2\) has maximum \(2\) for syndrome \(0\) and \(1\) for each of the other two syndromes. No random-channel assumption is made.

## Proof
**1. Perfect single-insertion partition.** Fix a length-\(n-1\) binary word \(z\), with \(w\) ones and weighted checksum \(s=\sum_{i=1}^{n-1} i z_i\). Its \(n+1\) distinct single-insertion supersequences occupy each VT syndrome once. Indeed, inserting \(0\) contributes exactly the syndromes \(s,s+1,\ldots,s+w\): an insertion shifts the index of each one to its right. Inserting \(1\) gives \(s+w+1,\ldots,s+n\): at position \(j\), the increment is \(j+\#\{\text{ones right of }j\}=w+1+\#\{\text{zeros strictly left of }j\}\). Duplicate insertions inside a constant run give the same word and have already been identified. These intervals contain every residue modulo \(N\) once.

**2. A universal bound.** Fix received word \(y\) of length \(n-2\). Its distinct single-insertion supersequences form a set \(Z\) of size exactly \(n\). Each \(z\in Z\) has a unique extension \(c\in\mathrm{VT}_a(n)\) by Step 1, and each such \(c\) contains \(y\) as a two-deletion subsequence. Hence the \(n\) intermediate words are partitioned into nonempty fibers indexed by the possible VT parents. If \(L\) is the number of fibers and \(s_1\) the number of singleton fibers, then \(n\ge 2L-s_1\).

A singleton fiber can arise only when its parent \(c\) is obtained by inserting two identical symbols in a single gap of \(y\). To see this, choose any two deleted coordinates in \(c\). Deleting either one separately produces an intermediate word. Deletion at two different constant runs of a fixed word always gives different outputs: equality of the two single-deletion outputs forces every symbol between the deleted coordinates to agree, hence both belong to the same run. Deleting two coordinates in the same run is equivalent to inserting two copies of that run's bit in one gap.

Set \(m=n-2\), let \(w\) and \(z=m-w\) be the one/zero counts in \(y\), and let \(S=\sum_{i=1}^{m}i y_i\). All doubled-zero candidates have checksum \(S+2h\), \(0\le h\le w\), where \(h\) counts ones on the right. All doubled-one candidates have checksum \(S+2m+3-2t\), \(0\le t\le z\), where \(t\) counts zeros on the right. For odd \(N\), each progression meets a prescribed syndrome at most once, so \(s_1\le2\). For even \(N\), the two progressions have opposite parity, while each progression has fewer than \(N\) terms and step size two, so a specified residue admits at most two total candidates. In either case \(s_1\le2\). Thus \(2L\le n+2\), giving \(L\le\lfloor n/2\rfloor+1\).

**3. Explicit witnesses for all syndromes.** Let \(e_S\) be the binary word of length \(n\) with ones exactly in positions \(S\); let \(k=\lfloor n/2\rfloor\). In each case the following \(k+1\) supports have checksum \(a\) and contain the displayed \(y\) as a subsequence.

For \(a=0\) and either parity, use \(y=0^{n-2}\) and the supports \(\varnothing\) and \(\{i,N-i\}\) for \(1\le i\le k\). For odd \(n=2k+1\) and odd \(a\), use \(y=0^{n-2}\), singleton support \(\{a\}\), and the \(k\) two-element sets \(\{i,j\}\subset\{1,\ldots,n\}\) with \(i+j\equiv a\pmod N\). These pairs exist because the involution \(i\mapsto a-i\pmod N\) has no fixed point when \(N\) is even and \(a\) odd; removing the pair involving zero leaves exactly \(k\) nonzero pairs.

For odd \(n\) and \(a=2\), use \(y=10^{n-3}\), the support \(\{2\}\), and \(\{1,j,N+1-j\}\) for \(2\le j\le k+1\). For odd \(n\ge5\) and \(a=4\), use \(y=010^{n-4}\), supports \(\{4\}\) and \(\{1,3\}\), and \(\{2,j,N+2-j\}\) for \(3\le j\le k+1\). For all other even nonzero \(a\) at odd \(n\), thus \(6\le a\le n-1\), use \(y=10^{n-3}\), the two supports \(\{1,a-1\}\) and \(\{2,a-2\}\), and the \(k-1\) triples \(\{1,j,l\}\) with \(2\le j<l\le n\), \(j+l\equiv a-1\pmod N\). Exactly \(k-1\) such pairs \(j,l\) exist by the fixed-point-free involution on residues \(\{2,\ldots,n\}\), accounting for the two excluded pairs incident to residues zero and one.

For even \(n=2k\ge4\) and \(1\le a=r\le n-2\), use \(y=0^{r-1}1 0^{n-r-2}\). Include supports \(\{r\}\) and \(\{r+1,n\}\). Among the \(k\) pairs \(\{u,v\}=\{i,N-i\}\) with \(u<v\), omit the unique pair containing \(r\), and associate to each remaining pair one triple:
\[
T_{u,v}=\begin{cases}
\{r,u,v\},&r<u,\\
\{u,r-1,r+2\},&u<r<v=r+1,\\
\{u,r,r+2\},&u<r<v=r+2,\\
\{u,r+1,v-1\},&u<r<v,\ v\ge r+3,\\
\{u-1,v-1,r+2\},&v<r.
\end{cases}
\]
These triples have three distinct valid positions, total position sum congruent to \(r\), and their sole received one can be shifted back to received coordinate \(r\) by deleting the other two ones (or, for triples containing \(r\), deleting the two later/earlier appropriate ones). They are pairwise distinct: cases are separated by the numbers of chosen positions below, equal to, or above \(r\); the only potentially overlapping patterns (the \(v=r+1\) case and \(v<r\) case) differ because only the former contains \(r-1\). Within each case the original pair is recoverable from the triple. Thus the two short supports and \(k-1\) triples give \(k+1\) distinct parents. Finally for \(a=n-1,n\), reverse the witness for syndrome \(N-a\): reversal preserves subsequence containment and negates the weighted checksum modulo \(N\). This exhausts every syndrome and proves sharpness. \(\square\)

## Verification
The standalone `verify.py` computes insertion supersets independently and exhaustively evaluates every binary received word and syndrome at \(3\le n\le13\), obtaining the theoretical maximum each time. It additionally generates and independently checks the explicit witness set for every \(n,a\) with \(3\le n\le80\), including each support's syndrome, length, subsequence property, and cardinality. Execute `python3 verify.py`; the recorded output ends in `VERIFY_OK`. These finite checks supplement, rather than replace, the all-length proof.

## Relationship to prior work
Banerjee, Con, Wachter-Zeh and Yaakobi (2026), *On the Average List Size of VT Codes under Two Insertions or Two Deletions*, studies mean list size and gives average bounds across received words and syndrome classes. The present theorem is an exact **per-syndrome maximum** with matching witnesses, not a restatement of those averages. Wachter-Zeh (2017), *List Decoding of Insertions and Deletions*, bounds the two-deletion VT list by \(n\) via the perfect one-deletion structure; here the bound is sharpened to \(\lfloor n/2\rfloor+1\) and shown sharp for every syndrome. Search and comparison against related finite code enumerations found no implication of the claimed infinite per-syndrome identity; unindexed equivalent work remains a possibility.

## Limitations
This result concerns binary VT checksum classes with **exactly two** deletions and distinct parents. It does not imply an efficient list-decoding algorithm, a matching result for other edit channels, or exact average list distributions. No independent scientific audit has been performed; the proof and computations are reproducible but may require further external scrutiny.

## References
1. A. Banerjee, R. Con, A. Wachter-Zeh, E. Yaakobi, *On the Average List Size of VT Codes under Two Insertions or Two Deletions* (2026), arXiv:2610.15767v1, https://arxiv.org/abs/2610.15767.
2. A. Wachter-Zeh, *List Decoding of Insertions and Deletions* (2017), arXiv:1701.02612v4, https://arxiv.org/abs/1701.02612.
