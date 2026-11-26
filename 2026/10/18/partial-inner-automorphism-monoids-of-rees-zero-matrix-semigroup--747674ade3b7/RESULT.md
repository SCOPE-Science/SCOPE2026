# Partial inner automorphisms do not detect complete mappings of combinatorial Rees semigroups

## Finding

There are two nonisomorphic, seven-element, combinatorial completely zero-simple semigroups with isomorphic partial inner automorphism monoids of order 18, exactly one of which has a complete mapping. Both examples have the same rectangular index sizes, and neither has a zero sandwich row or column. Thus even within this regular class, the partial inner monoid cannot serve as a complete-mapping existence test.

## Construction and conventions

Use the trivial group, with nonzero elements denoted \((i,\lambda)\), \(i\in\{0,1,2\}\), \(\lambda\in\{0,1\}\), and a distinct absorbing element \(0_S\). Multiplication is \((i,\lambda)(j,\mu)=(i,\mu)\) if \(p_{\lambda j}=1\), and \(0_S\) otherwise. Set
\[
P_A=\begin{pmatrix}1&1&1\\1&0&0\end{pmatrix},\qquad
P_B=\begin{pmatrix}1&1&0\\0&1&1\end{pmatrix}.
\]
Every row and column is nonzero, the regular Rees condition for complete zero-simplicity, and the structure group is trivial. A complete mapping is a bijection \(\alpha\) for which \(a\mapsto a\alpha(a)\) is also bijective. The partial inner monoid uses the maps \(a\mapsto hag\) on \(\{a:(gh)a=a=a(gh)\}\) for \(g,h\in S^1\), with an identity adjoined when necessary.

## Proof

For either pattern, let \(E=\{(i,\lambda):p_{\lambda i}=1\}\), the four nonzero idempotents. Whenever a nonzero element of \(S\) equals \(gh\), the two domain equalities force any nonzero point of the domain to have the same two indices as \(gh\); it is in the domain exactly when \(gh\in E\). A generator therefore either has domain \(\{0_S\}\), or is the map \(\{0_S,e\}\to\{0_S,f\}\) for some \(e,f\in E\), or is the global identity from the adjoined identity. For the middle case, the image of \(e\) is nonzero and is the idempotent \(hg\) if neither conjugator is the adjoined identity; a single identity conjugator yields the local identity instead. For each \(e=(i,\lambda)\) and \(f=(j,\mu)\) in \(E\), the conjugators \(g=(i,\mu)\), \(h=(j,\lambda)\) give \(gh=e\) and \(hag=f\) at \(a=e\). These maps compose as matrix units: the source and target pairs must align to retain a nonzero point, and otherwise their composite is the map fixing \(0_S\) on \(\{0_S\}\). The full identity and this latter absorbing map give exactly two further maps. Thus both monoids are the four-index Brandt semigroup of matrix units with an external identity, of order \(4^2+2\). The semigroups themselves are not isomorphic: their nonzero \(\mathcal L\)-classes are the two classes of fixed last index, and the multisets of idempotent counts are \(\{3,1\}\) and \(\{2,2\}\). For these patterns, the fixed-last-index classes follow directly because some entry in column \(i\) is nonzero, allowing left multiplication of \((i,\lambda)\) to give any \((j,\lambda)\).

For a complete mapping \(\alpha\), the product at \(a=0_S\) is already \(0_S\). Bijectivity of the product map therefore forces \(\alpha(0_S)=0_S\) and every other product to be nonzero. In \(S_A\) the three elements of last index 1 must all be sent to elements of first index 0, the only column hit by that row. Only two such images exist, a contradiction. In \(S_B\), fix \(0_S\) and take
\[
\begin{array}{c|cccccc}
a&(0,0)&(0,1)&(1,0)&(1,1)&(2,0)&(2,1)\\\hline
\alpha(a)&(0,0)&(1,1)&(0,1)&(2,0)&(1,0)&(2,1).
\end{array}
\]
The six nonzero products in the same order are \((0,0),(0,1),(1,1),(1,0),(2,0),(2,1)\). Both lists are permutations, proving the separation.

## Relation to prior work and verification

The natural partial inner maps are those of Araújo et al., arXiv:2605.00041. The regular Rees Brandt classification is also given by *The partial inner automorphism monoid of every completely zero-simple Rees semigroup* (Resultary b82db1836ccf, Finding). Theorem 6.2 of Araújo et al., *Complete Mappings of Semigroups*, arXiv:2608.25092, gives general support-based conditions that already decide the two existence cases individually. The contribution here is the explicit collision between these two invariants in the same small regular class, not either general classification or criterion. The proof provides the entire conjugation-map monoid and both complete-mapping decisions directly; the supplied finite verifier's example checks are corroboration. No minimality assertion is made.
