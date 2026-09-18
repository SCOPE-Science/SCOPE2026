# Fixed-alphabet q-ary deletion codes with coefficient 2t-1

## Result

Let \(q\ge 2\) and \(t\ge 2\) be fixed integers, and let \(\Sigma\) be an alphabet of size \(q\). For all sufficiently large \(n\), there exists a code \(C\subseteq\Sigma^n\) correcting \(t\) deletions such that
\[
\operatorname{red}_q(C):=n-\log_q|C|
\le (2t-1)\log_q n+O_{q,t}(\log\log n).
\]
Equivalently, its redundancy in bits is
\[
(n-\log_q|C|)\log_2 q
\le (2t-1)\log_2 n+O_{q,t}(\log\log n).
\]
For \(q=2\) this is En Gad's theorem. The new case is every fixed \(q>2\).

The proof extends the substring-spectrum/random-linear-hash construction of En Gad. That paper explicitly asks whether the coefficient \(2t-1\) continues to hold over a fixed larger alphabet. The extension requires checking the places where the binary alphabet enters the proof; the witness and hashing arguments themselves are alphabet-free once the local-edit catalogue has the same bubble structure.

## Proof

### 1. A dense family of q-ary repeat-free words

Take exactly the same length scale as in the binary argument,
\[
k=2\lceil\log_2 n\rceil+2,\qquad L=3(k+1).
\]
Call a q-ary word \(k\)-unique if its length-\(k\) substrings are pairwise distinct.

For two prescribed starting positions, equality of their length-\(k\) windows has probability \(q^{-k}\) in a uniformly random q-ary word. This remains true for overlapping windows: if the shift is \(s<k\), equality says that a block of length \(k+s\) has period \(s\), giving \(q^s\) valid blocks among \(q^{k+s}\). Thus
\[
\Pr[\text{not }k\text{-unique}]
\le {n\choose 2}q^{-k}
\le {n\choose 2}2^{-k}<\frac18.
\]
Hence at least \((7/8)q^n\) words are \(k\)-unique.

The de Bruijn-path argument is unchanged over an alphabet of any size: for an \((L-1)\)-unique word, its length-\(L\) substring spectrum is the edge set of a simple directed path and therefore determines the word uniquely. The shared-source-letters lemma used after one edit is likewise purely positional and remains valid verbatim.

### 2. q-ary bubbles

The only substantive binary change is the local description of shortening or lengthening a constant run. For \(d\in\Sigma\), \(1\le\rho\le k+1\), and words \(A,B\in\Sigma^{L-\rho}\) satisfying
\[
\operatorname{last}(A)\ne d,\qquad \operatorname{first}(B)\ne d,
\]
define
\[
P=A d^\rho B,\qquad P'=A d^{\rho-1}B.
\]
The two words have the same first and last \(L-1\) symbols. As in the binary construction, when their de Bruijn walks are simple and meet only at those endpoints, the signed difference of their length-\(L\) spectra is a bubble. A rule is a sum of \(t\) deletion-oriented and \(t\) insertion-oriented bubbles with vertex-disjoint supports.

Every separated alignment with exactly \(t\) deletions and \(t\) insertions produces such a rule. Indeed, a run in a \(k\)-unique word has length at most \(k\), so a single edit changes a maximal \(d\)-run as above with \(\rho\le k+1\). Simplicity follows from the same shared-source argument as in the binary proof.

It remains to exclude an internal vertex common to the two local paths. If the length-\((L-1)\) vertex windows of \(P\) and \(P'\) start at offsets \(a,b\), the shared-source lemma forces \(a-b\in\{0,1\}\). If \(a=b>0\), the compared windows include the position at which
\[
P[L-1]=d,\qquad P'[L-1]=P[L]=\operatorname{first}(B)\ne d,
\]
a contradiction. Hence \(a=b=0\), the initial endpoint. If \(a=b+1\) and \(b<L-\rho\), then with \(j=L-\rho-1\), the compared windows contain
\[
P[j+1]=d,\qquad P'[j]=\operatorname{last}(A)\ne d,
\]
a contradiction. Thus \((a,b)=(L-\rho+1,L-\rho)\), the terminal endpoint. Different well-separated edits have vertex-disjoint bubbles by the same shared-source argument. Consequently the q-ary catalogue has exactly the structural properties used later: every rule is nonzero, has entries in \(\{-1,0,1\}\), consists of \(2t\) disjoint bubbles, and is closed under negation.

### 3. Random linear hashing is alphabet-independent

Index coordinates by q-ary \(L\)-grams and choose independent uniform \(\xi_g\in[0,1)\). For an integer spectrum vector \(p\), put
\[
H(p)=\sum_g \xi_g p_g\pmod 1
\]
and divide the circle into \(Q\) equal label intervals. Exactly as in En Gad's Lemma 3.2, any \(R\) rationally linearly independent integer difference vectors have independent uniform hashes, so they all pass the necessary equal-label test with probability \((2/Q)^R\). This linear-algebra statement does not depend on the number of coordinates or on \(q\).

The exceptional-conflict estimate also keeps the same power of \(n\). For a fixed source word, an alignment with \(d\) deletions and \(d\) insertions is specified by its anchors and its \(d\) inserted symbols. The binary factor \(2^d\) becomes \(q^d\). Because \(q,t\) are fixed, this changes only the constant. Thus the number of records with \(d<t\), or with \(d=t\) but a separation failure, is
\[
O_{q,t}(L n^{2t-1}),
\]
and the probability that a fixed \(k\)-unique word has such an equal-label partner is
\[
O_{q,t}\!\left(\frac{L n^{2t-1}}{Q}\right).
\]

### 4. Witness extraction and counting

The bounded-witness argument from an odd cycle in the equal-label conflict graph uses only the signed supports of rules, rational linear dependence, and the fact that every rule has \(2t\) vertex-disjoint bubbles. Therefore its component bound and witness-size bound transfer unchanged.

The counting lemma needs one minor alphabet accounting change. A bubble header now records its orientation, run length \(\rho\), and edited symbol \(d\in\Sigma\), giving \(q\) possibilities for the last item instead of two. When a known \(k\)-symbol stretch is transferred across the edit, at most one additional alphabet symbol is needed, giving again \(q\) possibilities rather than two. Since \(q\) is fixed, these factors are absorbed into the polynomial-in-\(L,R\) description cost. Hence there is a constant \(a_{q,t}\) such that generating sets with \(R\) rules and \(c\) connected components number at most
\[
n^c(LR)^{a_{q,t}R}.
\]

We deliberately retained \(k=2\lceil\log_2 n\rceil+2\), so \(L\ge\log_2 n\). Thus the binary proof's treatment of the possible extra connected component for \(R>L\), using \(n\le 2^R\), remains literally available. Enlarging the polylogarithmic exponent to absorb the fixed q-ary description factors, there is a constant \(b_{q,t}\) for which the entire obstruction union bound works with
\[
Q=C_{q,t}\, n^{2t-1}L^{b_{q,t}}
\]
for a sufficiently large fixed constant \(C_{q,t}\).

### 5. Selecting the code

For some hash, a positive constant fraction of the \(k\)-unique words survives both exceptional-family deletion and deletion of non-bipartite conflict components. Keeping the larger side of every remaining bipartite component loses at most another factor two. Finally select the largest of the \(Q\) hash-label classes. Therefore, for a constant \(c_{q,t}>0\),
\[
|C|\ge c_{q,t}\frac{q^n}{Q}.
\]
Every two distinct words in \(C\) are nonconfusable, hence \(C\) corrects \(t\) deletions. Consequently
\[
\begin{aligned}
\operatorname{red}_q(C)
&\le \log_q Q+O_{q,t}(1)\\
&=(2t-1)\log_q n+O_{q,t}(\log L)\\
&=(2t-1)\log_q n+O_{q,t}(\log\log n).
\end{aligned}
\]
This proves the theorem.

## Significance

For fixed q, the classical existential graph-colouring scale for q-ary t-deletion codes has leading bit redundancy \(2t\log_2 n\). The theorem lowers that coefficient to \(2t-1\) for every fixed alphabet, not only the binary alphabet. In particular, for every fixed \(q>2\), two-deletion-correcting q-ary codes exist with
\[
3\log_2 n+O_q(\log\log n)
\]
bits of redundancy, or equivalently
\[
3\log_q n+O_q(\log\log n)
\]
q-ary symbols of redundancy.

## Verification

`artifacts/verify_qary_local.py` checks two finite ingredients of the extension. First, it exhaustively verifies the exact \(q^{-k}\) probability count for equality of overlapping q-ary length-\(k\) windows in representative ranges. Second, for millions of ternary and quaternary local words it checks the endpoint contradiction used in the q-ary bubble proof whenever the shared-source offset difference is 0 or 1. `artifacts/verification.txt` records the output. These checks are sanity tests; the theorem is proved analytically above.

## Limitations

- The result is existential. It does not make the random-hash/two-colouring construction efficiently encodable or decodable.
- It keeps the \(O_{q,t}(\log\log n)\) correction and does not improve the leading coefficient below \(2t-1\).
- The alphabet size q is fixed as \(n\to\infty\); no uniform claim is made when q grows with n.
- Originality is qualified to the best of our knowledge. The motivating preprint is extremely recent and explicitly lists this extension as open, so a near-simultaneous observation or later revision is the principal residual risk.

## Literature context and originality boundary

En Gad's arXiv:2609.19493 proves the binary coefficient \(2t-1\) result and, in its further-questions section, explicitly states that codes over a fixed larger alphabet appear to share the needed properties and asks whether the coefficient \(2t-1\) holds. The present contribution is the proof that it does, by identifying and repairing every binary-specific step.

Prior q-ary multiple-deletion work includes explicit constructions with larger leading redundancy; for example, Song and Cai's arXiv:2210.14006 gives an explicit q-ary two-deletion construction with leading coefficient 5 in its stated logarithmic redundancy. Separate burst-deletion results do not cover arbitrary t deletions. A literature search for q-ary/nonbinary multiple-deletion codes, the coefficient \(2t-1\), substring-spectrum hashing, and equivalent fixed-alphabet formulations found no earlier statement of the theorem above. No novelty is claimed for de Bruijn spectra, repeat-free words, random linear hashing, or the binary witness method themselves.

## References

1. Eyal En Gad, *Polynomially larger deletion codes by linear hashing of substring counts*, arXiv:2609.19493 (2026), especially Theorem 6.2 and Section 8.
2. Wentu Song and Kui Cai, *Non-binary Two-Deletion Correcting Codes and Burst-Deletion Correcting Codes*, arXiv:2210.14006 (2022).
3. Z. Ye et al., *Some New Constructions of q-ary Codes for Correcting a Burst of at Most t Deletions*, Entropy 27(1):85 (2025). This paper summarizes the classical q-ary existential bounds and treats the distinct burst-deletion model.
