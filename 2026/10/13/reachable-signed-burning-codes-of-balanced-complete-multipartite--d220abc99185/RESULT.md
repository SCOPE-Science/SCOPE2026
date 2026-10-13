# Reachable signed-burning codes of balanced complete multipartite graphs

## Finding

Consider a finite connected complete multipartite graph \(G=K_{n_1,\ldots,n_r}\), with \(r\ge 3\), \(n_i\ge1\), \(N=\sum_i n_i\), and a balanced edge signature \(\sigma\). Let \(E\) be the union of the partite sets of size at least two, let \(m=|E|\), and let \(s=N-m\) be the number of singleton-part vertices. Balance supplies a sign vector \(\varepsilon\in\{\pm1\}^{V(G)}\), unique up to negation, satisfying \(\sigma(uv)=\varepsilon(u)\varepsilon(v)\) on each edge. For a word \(w\) and a vertex \(v\), denote by \(w^{(v)}\) the word obtained by changing exactly the sign at \(v\).

**Theorem.** In the two-colour signed-burning process with simultaneous spread preceding each ignition, the complete set of reachable terminal colorings is
\[
\mathcal R(G,\sigma)=\{\varepsilon,-\varepsilon\}\cup
\{\varepsilon^{(v)},(-\varepsilon)^{(v)}:v\in E\}.
\]
These \(2+2m\) terminal words are distinct. For the all-positive signature, the number of reachable terminal words with exactly \(j\) negative coordinates is given by the generating polynomial
\[
W_G(z)=1+z^N+m(z+z^{N-1}).
\]
Let \(a=|\{v:\varepsilon(v)=1\}|\) and \(b=N-a\). The plurality number is
\[
Y(G,\sigma)=\max\bigl(\{a,b\}
\cup\{a+1:E\cap\varepsilon^{-1}(-1)\ne\varnothing\}
\cup\{b+1:E\cap\varepsilon^{-1}(1)\ne\varnothing\}\bigr),
\]
where a conditionally specified set is omitted when its condition is false.

The binary Hamming covering radius of the reachable code, which is invariant under switching, is exactly
\[
\rho(G)=
\begin{cases}
\lfloor N/2\rfloor,&m=0,\\
N/2-1,&m>0\text{ and }N\text{ even},\\
(N-1)/2,&m>0,\ N\text{ odd},\ s\ge (N-1)/2,\\
(N-3)/2,&m>0,\ N\text{ odd},\ s<(N-1)/2.
\end{cases}
\]
Consequently the least plurality number among **all balanced signatures** on \(G\) is \(N-\rho(G)\). In particular, odd-order graphs with a nonsingleton part exhibit a sharp one-unit covering-radius transition according to the number of singleton parts.

For example, the two five-vertex tripartite graphs \(K_{3,1,1}\) and \(K_{2,2,1}\) have covering radii \(2\) and \(1\), respectively, even though both admit a nonsingleton part. Consequently their worst balanced-signature plurality values are \(3\) and \(4\). This exhibits the exact singleton threshold in the smallest order where both regimes coexist.

## Assumptions and scope

The signed-burning rule is that of Fallat, Gupta, Khodamoradi, and Zilles: yellow is represented by \(+1\), green by \(-1\), and unburned by \(0\). At each round every unburned vertex receives the sign of the signed sum of the currently burned neighbours, if this sum is nonzero; afterward exactly one still-unburned vertex may be ignited in either color. Already burned colors never change. Here all graph parts are nonempty, \(r\ge3\), and the signature is balanced (the product of signs on every cycle is positive). Unbalanced signatures and non-complete multipartite graphs are not asserted to satisfy this result.

## Proof

**Unsigned terminal words.** Fix the all-positive signature. The first round ignites a vertex \(x\) of some part \(P\), in sign \(c\in\{\pm1\}\). At the spread step of round two, every vertex outside \(P\) receives sign \(c\), while every other vertex in \(P\) remains unburned because there are no edges within \(P\). If \(P\) is a singleton, the process is complete with constant terminal word \(c\mathbf 1\). Otherwise the sole round-two ignition can color at most one additional vertex \(v\in P\), arbitrarily. At the spread step of round three, every vertex still unburned in \(P\) receives sign \(c\), since all its neighbours outside \(P\) already have that sign and \(N-|P|>0\). Therefore no terminal coloring can differ from \(c\mathbf1\) at more than one coordinate, and such a coordinate must belong to a nonsingleton part. Conversely, for every \(v\in E\), choose another vertex \(x\) in its part, ignite \(x\) in sign \(c\) in round one and \(v\) in sign \(-c\) in round two. This realizes exactly the desired one-coordinate flip. Because \(N\ge3\), the two constant words and the \(2m\) one-flip words are all distinct. The enumerator follows by counting signs.

**Balanced signings and plurality.** The classical switching characterization of balance provides \(\varepsilon\). Under coordinatewise multiplication by \(\varepsilon\), the all-positive process corresponds step-for-step to the signed process: in every signed neighbour sum the factor \(\varepsilon(v)\) pulls outside the sum, and an ignition color changes by that same factor. Hence multiplying the unsigned terminal code by \(\varepsilon\) gives every and only signed terminal coloring, proving the code equality. The unflipped terminal words have respectively \(a\) and \(b\) positive entries. Flipping an eligible negative coordinate of \(\varepsilon\) increases its positive count to \(a+1\), whereas flipping an eligible positive coordinate of \(-\varepsilon\) increases its positive count to \(b+1\). Flips in the other directions only decrease those counts. Symmetry under global color reversal identifies the maximum positive count with the usual maximum same-color count. This proves the plurality formula.

**Hamming distance and radius.** Let \(w\) be an arbitrary \(\pm1\) word, and put \(t=\min(|\{v:w(v)=+1\}|,|\{v:w(v)=-1\}|)\). Define \(\delta(w)=1\) when an eligible coordinate lies in at least one sign class of cardinality \(t\), and \(\delta(w)=0\) otherwise; for \(t=0\), this is zero. The unsigned-code description gives the exact distance identity
\[
d_H(w,\mathcal R(G,+))=t-\delta(w).
\]
Indeed the nearer constant word is at distance \(t\). A one-coordinate flip of that constant reduces the distance by one exactly if the flipped eligible position is in a smaller sign class; all other flips raise it. When both sign classes have size \(t\), either is available.

If \(m=0\), no flip is allowed, so the maximum distance is \(\lfloor N/2\rfloor\). Assume \(m>0\). For even \(N=2q\), a word with \(q\) positive and \(q\) negative coordinates has \(\delta=1\), so distance \(q-1\), whereas every unbalanced word has \(t\le q-1\); hence the maximum is \(q-1\). For odd \(N=2q+1\), only words with smaller sign class of size \(q\) could have distance \(q\). Such a word has \(\delta=0\) precisely when all \(q\) of those coordinates lie among the \(s\) singleton-part vertices. This is possible if and only if \(s\ge q\). Otherwise every word has distance at most \(q-1\), and a word with the two class sizes \(q,q+1\) attains \(q-1\). This proves the radius cases. Coordinatewise sign multiplication is a Hamming isometry, so the radius is switching-invariant. The identity between least plurality over a switching class and \(N\) minus the covering radius follows from the signed-burning formulation (and also directly from the terminal-code equality).

## Verification

The standalone verifier `verify_balanced_multipartite.py` enumerates all complete multipartite profiles with at least three nonempty parts and \(3\le N\le7\). It independently explores every legal spread-and-ignite state, for every balanced signature determined by a gauge word up to global negation, and compares terminal sets, individual plurality values, code size, and exact covering radius with the theorem. There are 99 ordered multipartite profiles, 4,692 tested balanced signatures, and 49,320 corresponding terminal words examined. All assertions passed. This finite check corroborates but does not replace the universal case analysis above.

## Relationship to prior work

Fallat, Gupta, Khodamoradi, and Zilles introduced the process, established switching-equivariance of the terminal code (their Corollary 2.4), and related its covering radius to the worst switching-class plurality (their Proposition 2.9). They investigated paths and hardness reductions, but their arXiv version 1 does not present the complete multipartite terminal-code enumeration, the explicit signature-by-signature plurality formula, or the singleton-part covering-radius threshold. The present argument specializes their framework to a canonical dense class and supplies those exact graph-specific classifications. Their general switching and code identities are acknowledged, not claimed as new.

## Limitations

The theorem is restricted to balanced signed complete multipartite graphs with at least three partite classes; arbitrary unbalanced signings are not included. The proof applies to every order and part profile within that domain. The verifier is exhaustive only for \(N\le7\); it is neither an infinite proof nor an external independent audit. Literature searches do not exclude an unindexed equivalent result. No independent scientific validation is asserted.

## References

1. S. Fallat, H. Gupta, K. Khodamoradi, and S. Zilles, *Burning Signed Graphs*, arXiv:2610.02506v1 (first publicly available October 1, 2026), https://arxiv.org/pdf/2610.02506v1; especially Definition 2.1, Corollary 2.4, Proposition 2.9, Section 3, and Conclusions.
2. F. Harary, *On the notion of balance of a signed graph*, Michigan Math. J. 2 (1953), 143–146 (balanced switching characterization, as cited in [1]).
