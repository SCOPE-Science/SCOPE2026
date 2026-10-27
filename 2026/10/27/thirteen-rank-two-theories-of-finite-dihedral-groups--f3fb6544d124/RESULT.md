# Thirteen rank-two theories of finite dihedral groups

## Finding

Let \(D_n=\langle r,s\mid r^n=s^2=1,\ srs=r^{-1}\rangle\), the symmetry group of a regular \(n\)-gon, with \(n\ge3\) and \(|D_n|=2n\). Regard \(D_n\) as a relational first-order structure in the language \(\{e,R\}\), where \(e\) names the identity and \(R(x,y,z)\) holds exactly when \(xy=z\). Define \(D_m\equiv_2D_n\) to mean agreement on all sentences of quantifier rank at most two.

**Theorem.** The entire family \(\{D_n:n\ge3\}\) has precisely thirteen \(\equiv_2\)-classes. Five are the singleton-index classes \(n=3,4,5,6,8\). For any two indices \(m,n\ge3\) outside that five-element set,
\[
 D_m\equiv_2D_n\quad\Longleftrightarrow\quad
 [3\mid m\Longleftrightarrow3\mid n]\ \text{and}\
 \min\{v_2(m),3\}=\min\{v_2(n),3\},
\]
where \(v_2(t)\) is the exponent of \(2\) in the prime factorization of \(t\). The smallest possible indices representing the thirteen classes are
\[
 3,4,5,6,7,8,9,10,12,16,18,20,24.
\]
Thus every group in the family agrees at rank two with a dihedral group of order at most \(48\); this bound is sharp **within the dihedral family** because the class characterized by \(3\mid n\) and \(8\mid n\) has smallest index \(24\). For example, \(D_7\equiv_2D_{11}\), whereas \(D_8\not\equiv_2D_{16}\).

## Assumptions and scope

The language includes equality, one named identity constant, and the **ternary multiplication relation**, not a binary multiplication function. Quantifier rank is nesting depth, without bounds on formula length or number of distinct variable names. The index satisfies \(n\ge3\) throughout; no claim is made about arbitrary finite groups, other first-order languages, higher quantifier ranks, or representative size outside this family. The valuation \(v_2\) is zero on odd positive integers.

## Proof

**1. Exact two-round invariant.** For elements \(a,b\) of an arbitrary group with named identity, every atomic formula in the terms \(e,a,b\) is determined by the following eight Boolean assertions (in this order):
\[
 a=e,\ b=e,\ a=b,\ a^2=e,\ b^2=e,\ a^2=b,\ b^2=a,\ ab=e.
\]
Indeed \(ba=e\) is equivalent to \(ab=e\); every other multiplication atom with input/output in \(\{e,a,b\}\) reduces to one of these assertions or an equality. Let \(\tau(a,b)\) denote the resulting eight-bit truth vector and let \(P_G(a)=\{\tau(a,b):b\in G\}\), retaining the atomic assertions concerning \(a\) alone. Put \(\Sigma(G)=\{P_G(a):a\in G\}\). The two-round Ehrenfeucht–Fraïssé criterion yields
\[
 G\equiv_2H\quad\Longleftrightarrow\quad\Sigma(G)=\Sigma(H).
\]
For completeness: after the first selected element, a response can survive all possible second selections if and only if the complete sets of possible final two-element atomic diagrams agree. Requiring this correspondence in both directions is exactly equality of the displayed sets. Conversely, every pointed profile has a rank-one characteristic formula: for every possible two-element quantifier-free diagram, assert that it is realized by a second element exactly when the profile contains it. An outer existential quantifier therefore distinguishes unequal spectra at rank two.

**2. Dihedral extensions.** Write rotations as \(r^j\) for \(j\in\mathbb Z/n\mathbb Z\) and reflections as \(sr^j\). Every reflection is an involution and no reflection is a square in \(D_n\); squares lie in the rotation subgroup. A rotation \(a=r^j\) has a square root in \(D_n\) if and only if the congruence \(2k\equiv j\pmod n\) is solvable. For a nonidentity rotation \(a\), all nongeneric rotational choices of a second element lie among
\[
 e,\ a,\ a^{-1},\ a^2,\quad \{b\in\langle r\rangle:b^2=a\},
\]
a set with at most six elements. At most two rotational elements satisfy \(b^2=e\). Hence for every \(n\ge9\), every nonidentity rotation admits a **generic noninvolution** \(b\) outside all these possibilities. Generic involutions always exist by choosing a reflection (for a reflection \(a\), choose a different reflection). Identity and reflection pointed profiles are independent of \(n\ge3\).

The remaining pointed profiles are determined solely by elementary order and square-root coincidences:

* An involution with a square root exists among rotations exactly when \(4\mid n\).
* A rotation of order three exists exactly when \(3\mid n\). For odd \(n\), its inverse is its unique square root; for even \(n\), one additional square root exists, distinct from the inverse.
* A rotation of order four exists exactly when \(4\mid n\). It admits a square root exactly when \(8\mid n\).
* A rotation of order at least five **without** a square root occurs for every even \(n\ge10\), witnessed by \(r\), and never for odd \(n\). A rotation of order at least five **with** a square root occurs for every odd \(n\ge9\) (take \(r\)) and every even \(n\ge10\) (take \(r^2\)).

All the pointed types described in these cases are distinct as eight-bit extension spectra: the distinguishing tests are identity/involution, coincidence \(a^2=a^{-1}\) (order three), involution of \(a^2\) (order four), existence of \(b^2=a\), presence of a root other than \(a^{-1}\), and existence of a generic noninvolution. No other pointed profile occurs because the list of special second-element values is exhaustive.

**3. All sufficiently large indices.** Name the universal identity and reflection profiles \(E,F\). Write \(H_1,H_0\) for order-at-least-five rotation profiles with and without square roots; \(T_{3,o},T_{3,e}\) for the order-three profiles with one and two square roots; \(I\) for the square-rootable involution profile; and \(T_{4,0},T_{4,1}\) for order-four profiles without/with a square root. Every generic noninvolution required in these definitions exists when \(n\ge9\). Consequently, for every \(n\ge9\), the **complete** pointed spectrum is
\[
 \begin{split}
 \Sigma(D_n)={}&\{E,F,H_1\}
 \cup \begin{cases}\{H_0\},&2\mid n,\\\varnothing,&2\nmid n,\end{cases}\\
 &\cup\begin{cases}\{T_{3,o}\},&3\mid n,\ 2\nmid n,\\\{T_{3,e}\},&6\mid n,\\\varnothing,&3\nmid n,\end{cases}\\
 &\cup\begin{cases}\{I,T_{4,0}\},&4\mid n,\ 8\nmid n,\\\{I,T_{4,1}\},&8\mid n,\\\varnothing,&4\nmid n.\end{cases}
 \end{split}
\]
There are two possible spectra for odd indices (distinguished by divisibility by three) and two each at \(v_2(n)=1\), \(v_2(n)=2\), and \(v_2(n)\ge3\). These eight spectra are pairwise unequal, giving the stated arithmetical equivalence criterion.

**4. Boundary indices.** Direct substitution in the eight atomic assertions gives the following complete spectra at the six small indices. The additional symbols denote the corresponding order-three, order-four, involution, or high-order types **lacking a generic noninvolution**: \(T_{3,s},T_{4,s},I_s,H_s\). In the table \(T_{3,e}\), \(I\), \(T_{4,1}\), \(H_0\), and \(H_1\) have the same meanings as above.

| Index | Complete pointed spectrum |
|---|---|
| \(3\) | \(E,F,T_{3,s}\) |
| \(4\) | \(E,F,I_s,T_{4,s}\) |
| \(5\) | \(E,F,H_s\) |
| \(6\) | \(E,F,T_{3,e},H_0\) |
| \(7\) | \(E,F,H_1\) |
| \(8\) | \(E,F,I,T_{4,1},H_0\) |

For instance, at index five the four nonidentity rotations are exhausted by \(a\), \(a^{-1}\), \(a^2\), and the square root of \(a\), so \(H_s\) has no generic noninvolution. At index seven two generic rotations remain; at index eight a rotation of order at least five with a square root is absent, while it appears at index sixteen. The remaining entries follow from the explicit dihedral product and square-root equations. This finite table is also independently reproduced by the supplied verifier. The five spectra for indices \(3,4,5,6,8\) are different from each other and from all eight large-index spectra; the index-seven spectrum equals the odd, three-free large-index spectrum. This proves exactly thirteen classes.

**5. Sharpness and explicit separation.** Every class occurs at one of the thirteen listed minimal indices. In particular the only way to have simultaneously the order-three profile \(T_{3,e}\) and the order-four square-root profile \(T_{4,1}\) is \(3\mid n\) and \(8\mid n\), first possible at \(n=24\). The construction in step 1 produces a specific rank-two distinguishing sentence for any pair of distinct profiles: quantify the first element realizing a pointed type present in one model and absent in the other. Therefore the listed indices are both sufficient and necessary for the sharp maximum representative order \(2\cdot24=48\).

## Verification

The included `verify.py` is a standalone Python 3 program using only its standard library; run `python3 verify.py` in the directory containing the file. It independently constructs all \(27\) multiplication atoms on \(\{e,a,b\}\) and compares their two-round types to the eight-bit reduction. It also computes arithmetic two-round spectra through index \(300\), checks the arithmetical classification across all index pairs in that range, and exhaustively compares direct full atomic two-round spectra through index \(33\). The recorded output is `verification_output.txt`. The unbounded assertion for all indices is proved by steps 2–4, not by finite testing.

## Relationship to prior work

Walid Gomaa's 2007 dissertation (Section 3.8, Lemma 3.10) and his 2010 paper (Section 8, Lemma 8.2) establish a general correspondence between quantifier-rank equivalence of dihedral groups and of their cyclic rotation groups in this relational group language. They obtain upper and lower depth bounds for distinguishing groups, but do not give the thirteen rank-two classes, the exceptional-index list, the valuation/divisibility classification, or the sharp order-48 representative. The present exact low-rank census uses the same language but independently computes the required two-round extension spectra rather than treating the general correspondence as the desired classification. General finite-model-theoretic game criteria are classical.

## Limitations

The sharp representative bound is internal to the dihedral family; no assertion of the smallest representatives among **all** groups is made. The formulas use a ternary relation, not the functional group language, in which atomic terms can have arbitrarily long products. A complete search of unpublished historical manuscripts is not possible, and equivalent unindexed analyses cannot be ruled out. The computational checks are finite corroboration, not a replacement for the all-index argument.

## References

1. W. Gomaa, *Model Theory and Complexity Theory*, doctoral dissertation, University of Maryland, publicly archived 2007-07-06, especially Chapter 3, Sections 3.2, 3.3, 3.8. https://drum.lib.umd.edu/items/b8c06e8c-d2da-4d80-923e-0bd02e2a8440
2. W. Gomaa, *Descriptive Complexity of Finite Abelian Groups*, International Journal of Algebra and Computation 20 (2010), 1087–1116, especially Sections 2, 6, 8; DOI: 10.1142/S0218196710006047. https://doi.org/10.1142/S0218196710006047
3. L. Libkin, *Elements of Finite Model Theory*, Springer, 2004 (standard Ehrenfeucht–Fraïssé game methods).
