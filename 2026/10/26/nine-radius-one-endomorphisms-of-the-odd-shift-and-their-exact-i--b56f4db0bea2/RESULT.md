# Nine radius-one endomorphisms of the odd shift and their exact image entropy spectrum

## Finding
Let \(X\subset\{0,1\}^{\mathbb Z}\) be the **odd shift**, in which the number of zeros between any two consecutive ones must be odd. For each Wolfram elementary rule \(r\in\{0,\dots,255\}\), let \(F_r\) use the centered neighborhood \((x_{i-1},x_i,x_{i+1})\).

Exactly **72 rule codes** satisfy \(F_r(X)\subseteq X\), inducing exactly **nine different maps** on \(X\). Exactly **32 codes**, representing four maps, are surjective onto \(X\): the three coordinate shifts and the coordinatewise XOR of the two neighboring sites (represented by Rule 18, equivalently Rule 90 on \(X\)). There are exactly **five image subshifts** and exactly **four image-entropy values**, namely
\[
0,\quad \frac12\log\frac{1+\sqrt5}{2},\quad
\frac12\log\lambda,\quad \frac12\log2,
\]
where \(\lambda\in(1,2)\) is the unique root above one of \(t^3-2t^2+t-1=0\). In particular the middle two values are distinct, ordered as displayed.

For the non-shift onto map \(D=F_{18}|_X\), every **nonzero** point of \(X\) has exactly two antecedents, while the all-zero point has exactly three. This fibre calculation complements—but does not claim to rediscover—the previously observed Rule-18/Rule-90 equality on \(X\).

## Assumptions and scope
The system is the two-sided binary odd shift, allowing the all-zero configuration and configurations with only finitely many ones. The rule number follows \(f_r(a,b,c)=\lfloor r/2^{4a+2b+c}\rfloor\bmod2\), with \(a,b,c\in\{0,1\}\). Classification is of global restricted maps \(F_r|_X\), not of distinct eight-entry truth tables on the entire full shift. Entropy means spatial topological entropy for the one-site shift \(\sigma\) restricted to each image \(F_r(X)\).

Write \(X_p=\{x\in X:x_j=0\text{ whenever }j\not\equiv p\pmod2\}\), for \(p\in\{0,1\}\). For a two-sided binary sequence \(a\), denote by \(\iota_p(a)\in X_p\) its insertion at positions \(2k+p\), with all opposite-parity positions zero. For a coarse binary subshift \(Z\), write \(\iota(Z)=\iota_0(Z)\cup\iota_1(Z)\). The image classifications below use this notation. The forbidden-word shift \(Z_w\) consists of every bi-infinite binary sequence avoiding the finite word \(w\).

## Proof
**1. Parity decomposition.** In an odd-gap configuration, successive positions of ones differ by an even integer; hence all ones occupy one parity class. Conversely any sequence supported on one parity has odd-length zero gaps. Therefore \(X=X_0\cup X_1\), with \(X_0\cap X_1=\{0^{\mathbb Z}\}\), and each component under \(\sigma^2\) is conjugate to the binary full shift.

**2. Complete endomorphism census.** The only length-three blocks in \(X\) are `000`, `001`, `010`, `100`, `101`. If the local output on `000` is one, the zero configuration maps to the forbidden all-one configuration. Thus a self-map must have \(f(000)=0\). If \(f(010)=1\), any nonzero value among \(f(001),f(100),f(101)\) produces outputs on both parities for a suitable input with an isolated one far from a realization of that nonzero neighborhood. Hence these three bits must all vanish, giving precisely the identity map.

If \(f(010)=0\), the three values \(f(001),f(100),f(101)\) are arbitrary. An input \(x=\iota_p(a)\) maps into the opposite parity component, where the coarse output is \(g(a_k,a_{k+1})\), with
\[
g(0,0)=0,\quad g(0,1)=f(001),\quad
g(1,0)=f(100),\quad g(1,1)=f(101).
\]
Thus exactly eight maps arise besides the identity, and no others. Each restricted map has eight distinct Wolfram-code extensions, because the three forbidden three-blocks `011`, `110`, `111` can be assigned freely. This proves \(9\times8=72\) self-preserving codes.

**3. Exact images and surjectivity.** The complete list is:

| Representative rule | Coarse operation (or same-phase identity) | Image | Onto? |
| --- | --- | --- | --- |
| 0 | zero | \(\{0^{\mathbb Z}\}\) | No |
| 2 | \((1-u)v\) | \(\iota(Z_{11})\) | No |
| 4 | identity on \(X\) | \(X\) | Yes |
| 16 | \(u(1-v)\) | \(\iota(Z_{11})\) | No |
| 18 | \(u\oplus v\) | \(X\) | Yes |
| 32 | \(uv\) | \(\iota(Z_{101})\) | No |
| 34 | \(v\) | \(X\) | Yes |
| 48 | \(u\) | \(X\) | Yes |
| 50 | \(u\lor v\) | \(\iota(Z_{010})\) | No |

The difference map \(u\oplus v\) is onto the bilateral full shift: given any binary output \(b\), choose one input coordinate and solve \(a_{k+1}=a_k\oplus b_k\) in both directions. The two projections and the identity are also onto. A rise or fall indicator cannot output adjacent ones on the coarse scale; conversely if \(b\) has no adjacent ones, \(a_k=b_{k-1}\) realizes the rise indicator, and \(a_k=b_k\) realizes the fall indicator.

For the AND map \(b_k=a_ka_{k+1}\), the pattern `101` cannot occur; conversely every \(b\in Z_{101}\) is realized by \(a_k=b_{k-1}\lor b_k\). The OR image is the digit complement of the AND image by De Morgan's law, hence equals \(Z_{010}\) on the coarse scale. The zero map has singleton image. Thus the nine maps have exactly five distinct images, of which four maps are onto. Each restricted map is represented by eight elementary rule codes, yielding \(4\times8=32\) onto codes.

**4. Exact entropy.** Since \(\sigma\) exchanges the two parity components, \(h_\sigma(\iota(Z))=\frac12 h_\sigma(Z)\). The singleton has entropy zero; \(X\) has entropy \(\frac12\log2\). The coarse golden-mean shift \(Z_{11}\) has adjacency polynomial \(t^2-t-1\), hence entropy \(\log\frac{1+\sqrt5}{2}\). The binary two-block state graph for \(Z_{101}\) has adjacency matrix
\[
A=\begin{pmatrix}
1&1&0&0\\
0&0&1&1\\
1&0&0&0\\
0&0&1&1
\end{pmatrix},
\]
with characteristic polynomial \(t(t^3-2t^2+t-1)\); exchanging zeros and ones gives the same entropy for \(Z_{010}\). The cubic is strictly increasing above one, is negative at the golden ratio, and positive at two, so its unique root \(\lambda\) above one strictly lies between the golden ratio and two. This proves the four distinct levels.

**5. Exact fibres of the non-shift onto map.** On \(X_p\), Rule 18 is the XOR neighbor rule \(a_k\mapsto a_k\oplus a_{k+1}\) in the opposite phase, since only the five admissible three-blocks matter. Every coarse output has exactly two binary predecessors, differing by global bit complementation. For nonzero \(y\in X\), the output phase is uniquely determined, so there are exactly two predecessors in \(X\). At the zero output, each of the two source phases contributes its two constant coarse sequences; the all-zero antecedent occurs in both phases, leaving precisely three distinct antecedents.

## Verification
Running `python3 verify.py` checks all 256 rule codes and the nine distinct restricted truth tables, exhaustively enumerates admissible finite input blocks to compare all nine image languages through output length eight, verifies the exact adjacency characteristic polynomials by integer arithmetic, and tests the Rule-18/Rule-90 equality on all five admissible neighborhoods. The exhaustive finite tests corroborate the classification; the unrestricted statements follow from the preceding parity decomposition, explicit preimage formulas, and finite complete truth-table analysis. No numerical approximation is required for the entropy identities.

## Relationship to prior work
Salo's 2014 article explicitly discusses the odd shift and general surjectivity properties of nonuniform cellular automata. It does not give the nine-map census or the image-entropy classification for centered radius-one self-maps of this subshift. In a September 2022 MathOverflow answer about Rule 18, Salo explicitly identified the same odd shift and stated that Rule 18 restricts to Rule 90 on it; this equality and its elementary derivative consequences are **prior work**, not claimed as newly discovered. The present claim concerns instead the complete restricted-map census, the five precisely identified images, and the four exact entropy levels. The predecessor-fibre calculation is recorded as a component of the classification, not a standalone novelty claim.

## Limitations
Only centered binary radius-one local maps are classified; arbitrary higher-radius endomorphisms are not. The four entropy levels are **image entropies** under the spatial shift, not entropy of the self-map under temporal iteration. The standard conjugacies and entropy formulas are elementary; the contribution is the complete classification and exact image spectrum for this natural sofic shift. An earlier unindexed census or equivalent computation remains a historical priority risk; no independent audit has been performed.

## References
1. V. Salo, *Realization problems for nonuniform cellular automata*, Theoretical Computer Science **559** (2014), 91–107, DOI: `10.1016/j.tcs.2014.07.031` (discussion of odd shift, definitions, and surjectivity; publicly available full HTML text).
2. V. Salo, response to *Mysteries of Wolfram's rule 18*, MathOverflow, 2022-09-07, `https://mathoverflow.net/questions/429911/mysteries-of-wolframs-rule-18` (explicit prior observation that Rule 18 preserves the odd shift and restricts to Rule 90).
