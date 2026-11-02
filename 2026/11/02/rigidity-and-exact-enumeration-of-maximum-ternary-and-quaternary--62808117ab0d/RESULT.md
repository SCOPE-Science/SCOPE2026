# Rigidity and exact enumeration of maximum ternary and quaternary two-distance codes

## Finding

For every integer \(n\ge 17\) and every **labeled** alphabet \(\Sigma\) of cardinality \(q\in\{3,4\}\), let \(\mathcal C\subseteq\Sigma^n\) have Hamming distance in \(\{2,4\}\) between any two different members. Then \(|\mathcal C|\le 1+\binom n2\). Equality holds **if and only if** there are a word \(c\in\Sigma^n\) and symbols \(a_i\in\Sigma\setminus\{c_i\}\), for every \(i\in\{1,\ldots,n\}\), such that

\[
\mathcal C=\{c\}\cup\{c^{\{i,j\}}:1\le i<j\le n\},
\]

where \(c^{\{i,j\}}\) agrees with \(c\) except that its symbols in positions \(i,j\) are \(a_i,a_j\). The center \(c\) and all alternatives \(a_i\) are uniquely determined by \(\mathcal C\). Hence, for each \(n\ge17\), there is precisely **one** maximum-code orbit under Hamming isometries, and the number of *distinct labeled* maximum codebooks is

\[
\boxed{(q(q-1))^n}.
\]

The previously known maximum cardinality is not claimed to be new; the classification of all equality cases and their exact number are the result.

## Assumptions and scope

No linear, additive, constant-weight, or field structure is assumed. A Hamming isometry may permute coordinates and independently permute the alphabet in each coordinate. A codebook is a subset (not a tuple) of the labeled space \(\Sigma^n\). The code is required to achieve the *unrestricted* optimum \(1+\binom n2\), proved by Lin, Djaljapayan, and Yu for \(q=3,4\) and \(n\ge6\) [1]. The present equality-case assertion is restricted to \(n\ge17\).

## Proof

**1. Normalization and the decisive structural alternative.** Embed a ternary code into a quaternary Hamming space when necessary. Independently permute symbols in the coordinates so that a chosen codeword becomes \(0^n\). The other codewords have weights two or four, giving a disjoint union \(\mathcal C=\{0^n\}\sqcup C_2\sqcup C_4\). We invoke the *proved structural estimates* in [1, Sections 2, 6, 7], not an unverified classification hypothesis. If \(C_4\neq\varnothing\), its weight-four supports are pairwise \(2\)-intersecting. The proof of [1, Theorem 7.1] bounds every possibility **apart** from a common-two-coordinate core with at least three disjoint external edges by one of

\[
4n+32,\quad 6n+25,\quad 4n+22,\quad 4n+26,\quad 4n+17,\quad 7n-11.
\]

All six are *strictly smaller* than \(1+\binom n2\) for each \(n\ge17\). For example, the closest case satisfies \(1+\binom n2-(6n+25)=\frac{(n-16)(n+3)}2>0\). Each other strict gap at \(n=17\) grows thereafter because the quadratic benchmark has greater increments. Consequently, if a maximum code has \(C_4\neq\varnothing\), some fixed coordinate pair \(P=\{u,v\}\) belongs to every weight-four support, and the graph on the remaining \(n-2\) coordinates whose edges are the other two positions of those supports contains a matching of size three.

**2. Rigidity of a full pure weight-two layer.** Suppose a collection \(B\) of weight-two words on \(N\ge15\) coordinates has mutual distances in \(\{2,4\}\) and \(|B|=\binom N2\). The proof of [1, Eq. (5)] shows that if \(r\) distinct supports are isolated from all other supports, then

\[
|B|\le\binom N2-r(2N-2r-4).
\]

As \(0\le r\le\lfloor N/2\rfloor\) and \(N\ge15\), the deficit is positive whenever \(r>0\). Thus \(r=0\), every support has multiplicity at most one, and equality forces *every* two-element support to appear. If supports \(\{i,j\}\) and \(\{i,k\}\) share only \(i\), the symbols at \(i\) must agree: otherwise the two words have forbidden distance three. Since all pairs occur and \(N\ge3\), each coordinate has one fixed nonzero alternative symbol across every incident pair. The full layer is therefore the canonical weight-two shell for these symbols.

**3. Equality when \(C_4=\varnothing\).** With \(B=C_2\) and \(N=n\), Step 2 applies: the normalized code is exactly \(0^n\) together with the complete, symbol-synchronized weight-two shell. This is the asserted construction centered at \(0^n\).

**4. Equality when \(C_4\neq\varnothing\).** We are in the common-pair/matching-three case of Step 1. Lemma 6.1 of [1] proves

\[
|C_4|\le\binom{n-2}{2},\qquad |C_2|\le2n-3.
\]

Their right sides sum to \(\binom n2\), so a maximum code must attain equality in *both*. Write \(P=\{u,v\}\). The proof of [1, Lemma 6.1] uses three disjoint external edges to show every word in \(C_4\) uses the same two nonzero symbols, say \(\alpha,\beta\), on \(u,v\), respectively. Erasing \(P\) preserves all distances within \(C_4\), and produces a pure weight-two code on \(n-2\ge15\) coordinates of size \(\binom{n-2}{2}\). By Step 2, it contains exactly one word on every external pair \(\{i,j\}\), and its symbol at each coordinate \(i\notin P\) is a fixed nonzero \(t_i\). Thus \(C_4\) is completely determined.

Every weight-two support must meet each of the three disjoint four-supports \(P\cup e_1,P\cup e_2,P\cup e_3\); a support avoiding \(P\) meets at most two of them and would create distance six with a third. Hence any weight-two support is either \(P\) or a *spoke* \(\{u,i\}\) or \(\{v,i\}\), \(i\notin P\). Lemma 6.1 also shows these spokes have multiplicity at most one and, if one occurs, the core support \(P\) has multiplicity at most one. There are exactly \(2(n-2)+1=2n-3\) supports of these types. Equality \(|C_2|=2n-3\) forces all of them to occur once.

The word on \(\{u,i\}\) has symbol \(\alpha\) at \(u\): compare it with a four-word whose external pair avoids \(i\), and use the forbidden-distance-three rule for a one-coordinate support intersection. Similarly the word on \(\{v,i\}\) has symbol \(\beta\) at \(v\). Comparing the first spoke with a four-word whose external pair *contains* \(i\), now with common support \(\{u,i\}\) and already matching \(\alpha\), forces the spoke's symbol at \(i\) to be \(t_i\): otherwise their distance would be three. The analogous argument applies to the \(v\)-spoke. Finally, the weight-two word on \(P\) must use \(\alpha\) and \(\beta\), because it intersects the spokes separately at \(u\) and \(v\).

Let \(c\) be the core word with \(c_u=\alpha,c_v=\beta\) and \(c_i=0\) elsewhere; choose alternate symbols \(a_u=a_v=0\) and \(a_i=t_i\) outside \(P\). Then \(c\in C_2\), and its two-position flips comprise: the original zero word (flipping \(u,v\)); every spoke in \(C_2\) (flipping one core and one outer position); and every word of \(C_4\) (flipping the two outer positions of its external pair, since it agrees with \(c\) on \(P\)). Thus \(\mathcal C\) is exactly the asserted even-weight-two shell centered at \(c\).

**5. Converse, unique parameters, and enumeration.** Every proposed shell has \(1+\binom n2\) distinct words, and any two different members have Hamming distance two or four: this follows by counting the symmetric difference of two distinct index pairs, or by comparing a pair word with the center. The published upper bound [1] makes it maximum. The center is the **unique** codeword at distance two from every other codeword: any noncenter pair word has a different pair word on disjoint coordinates, at distance four, since \(n\ge17\). From that unique center each \(a_i\) is determined by any distance-two word that changes coordinate \(i\). Thus distinct centers or alternates give distinct labeled codes, proving the count \(q^n(q-1)^n\). All shells are isometric under independent coordinatewise alphabet permutations, proving the unique orbit. \(\square\)

## Verification

The standalone script `check_extremizers.py` exhaustively constructs the parameterized family for \((q,n)=(2,5),(3,4),(3,5),(4,4)\), verifies pairwise allowed distances and uniqueness of centers, and checks distinct labeled parameters produce distinct codes. It also tests explicit constructions for \(q=3,4\) at lengths \(17\) and \(24\). The recorded stdout is in `verification_output.txt`. These checks **do not** enumerate every admissible noncanonical code nor independently establish the all-length classification: that conclusion is the proof above using the published inequalities. The cited source papers are not embedded.

## Relationship to prior work

Lin, Djaljapayan, and Yu [1] establish the maximum *size* for all \(n\ge6\) and \(q=3,4\), and prove the structural inequalities needed for this equality analysis. Their paper presents the standard construction but does not state a classification or enumerate all maximum codebooks. The new inference requires eliminating strict alternative cases, forcing equality in both layer bounds, and then proving complete symbol synchronization and uniqueness of center. Their companion work [2] treats the maximum *size* in the distinct regime \(q\ge5\), without implying a ternary/quaternary classification. Earlier binary two-distance size results [3] do not supply the nonbinary equality cases. An unindexed prior extremizer classification or an implicit equivalent consequence in other literature remains a priority risk.

## Limitations

No equality-case assertion is made for \(n\le16\). No claim is made about larger alphabets or about other allowed distance sets. The argument derives a new rigidity conclusion from stated estimates in [1], rather than reproving all those estimates from first principles; its mathematical validity is conditional on those published lemmas. The finite script tests canonical constructions and injectivity, not exhaustiveness of arbitrary codes.

## References

[1] Yen-Chi Roger Lin, Valjakas Djaljapayan, Wei-Hsuan Yu, *The Ternary and Quaternary Cases of the \(\{2,4\}\)-Distance Code Conjecture*, arXiv:2610.30615v1, posted 2026-10-22; especially Lemma 2.1, Eq. (5), Lemma 6.1 and Theorem 7.1. https://arxiv.org/html/2610.30615v1

[2] Valjakas Djaljapayan, Yen-Chi Roger Lin, Wei-Hsuan Yu, *Asymptotically Sharp Length Thresholds for \(q\)-ary Codes with Distances \(2\) and \(4\)*, arXiv:2610.30613v1, posted 2026-10-22. https://arxiv.org/html/2610.30613v1

[3] Alexander Barg, Alexey Glazyrin, Wei-Jiun Kao, Ching-Yi Lai, Pin-Chieh Tseng, Wei-Hsuan Yu, *On the size of maximal binary codes with 2, 3, and 4 distances*, arXiv:2210.07496v1 (2022); *Combinatorial Theory* 4 (2024). https://arxiv.org/abs/2210.07496
