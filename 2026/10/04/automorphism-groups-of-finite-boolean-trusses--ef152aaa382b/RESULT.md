# Automorphism groups of finite Boolean trusses

## Finding

Every finite Boolean truss \(T\) has a decomposition
\[
T\cong \mathrm{T}(\mathbb F_2^r)\times L(G)\times R(H),
\]
where \(r\ge 0\), \(G\) and \(H\) are finite abelian groups, and \(L(G)\), respectively \(R(H)\), denotes the left-zero, respectively right-zero, truss carried by the abelian heap of the indicated group. The integer \(r\) and the isomorphism types of \(G\) and \(H\) are determined by \(T\).

The full truss automorphism group splits as
\[
\operatorname{Aut}_{\mathrm{tr}}(T)
\cong
S_r\times \operatorname{Hol}(G)\times \operatorname{Hol}(H),
\]
where \(\operatorname{Hol}(G)=G\rtimes\operatorname{Aut}(G)\). Hence
\[
|\operatorname{Aut}_{\mathrm{tr}}(T)|
=
r!\,|G|\,|\operatorname{Aut}(G)|\,|H|\,|\operatorname{Aut}(H)|.
\]

When \(G\cong(\mathbb F_2)^\ell\) and \(H\cong(\mathbb F_2)^s\), this becomes
\[
|\operatorname{Aut}_{\mathrm{tr}}(T)|
=
r!\,2^{\ell+s}
|\operatorname{GL}(\ell,2)|
|\operatorname{GL}(s,2)|.
\]

## Assumptions and scope

A truss is understood as an abelian heap equipped with an associative multiplication distributing over the heap operation. A Boolean truss is one whose multiplication is idempotent. The statement concerns finite Boolean trusses, including degenerate one-element factors. For an abelian group \(G\), its associated heap has ternary operation \([x,y,z]=x-y+z\).

The structural input is the 2026 classification of Boolean trusses by Andruszkiewicz and Rybołowicz. Their Theorem 3.8 decomposes any Boolean truss into two Boolean-ring factors and left-zero and right-zero factors. Their Theorem 3.9 shows that the commutative, left-zero, and right-zero pieces are intrinsically recoverable under isomorphism. Their Corollary 3.13 shows that when the Boolean ring controlling the commutative piece is unital, the two Boolean-ring factors combine to the ordinary ring truss. Every finite Boolean ring is unital and is isomorphic to \((\mathbb F_2)^r\) for a unique \(r\).

## Proof

Write the finite Boolean truss in the classified form. Because the Boolean ring in the commutative piece is finite, it is unital. Corollary 3.13 therefore replaces its two ring-type factors by a single truss \(\mathrm{T}(P)\), where \(P\cong(\mathbb F_2)^r\). By Theorem 3.9 and Remark 3.11, the left-zero and right-zero factors are determined, as heaps, by finite abelian groups \(G\) and \(H\). Thus it is enough to study
\[
T=P\times G\times H
\]
with componentwise heap operation and multiplication
\[
(p,g,h)(q,g',h')=(pq,g,h').
\]

For \(a=(p,g,h)\), the proof of Theorem 3.9 identifies three intrinsic subsets: the commuting leaf, on which only the \(P\)-coordinate varies; the left leaf, on which only the \(G\)-coordinate varies; and the right leaf, on which only the \(H\)-coordinate varies. Every truss automorphism preserves these three families of leaves. Therefore any automorphism has the coordinate form
\[
(p,g,h)\longmapsto(\sigma(p),\alpha(g),\beta(h)).
\]

Heap preservation makes \(\sigma\), \(\alpha\), and \(\beta\) heap automorphisms. Multiplication preservation gives
\[
\sigma(pq)=\sigma(p)\sigma(q),
\]
while the left-zero and right-zero multiplications impose no additional condition on \(\alpha\) or \(\beta\). The zero of \(P\) is the unique multiplicative absorber, so \(\sigma(0)=0\). A heap automorphism fixing \(0\) is additive; hence \(\sigma\) is a Boolean-ring automorphism. Conversely, any ring automorphism of \(P\) together with arbitrary heap automorphisms of the two rectangular factors gives a truss automorphism.

For \(P\cong(\mathbb F_2)^r\), a ring automorphism permutes the \(r\) primitive idempotents, so
\[
\operatorname{Aut}(P)\cong S_r.
\]
For any abelian group \(G\), after choosing a heap origin, every heap automorphism is uniquely affine,
\[
x\longmapsto \varphi(x)+c,
\qquad
\varphi\in\operatorname{Aut}(G),\quad c\in G.
\]
Thus the heap automorphism group is the holomorph \(G\rtimes\operatorname{Aut}(G)\). Applying this to both rectangular factors proves the stated direct-product decomposition and the order formula.

## Verification

The proof above is symbolic and covers every finite Boolean truss. As a finite consistency check, `verify.py` directly enumerates all permutations of several small models and tests both the heap law and multiplication. It obtains the predicted automorphism counts for
\[
(r,G,H)=(1,C_2,1),\ (2,1,1),\ (0,C_3,1),\ (0,C_2,C_2),\ (1,C_2,C_2),
\]
with respective counts \(2,2,6,4,4\), and terminates with `CHECK_OK`.

These computations are checks of the structural proof, not substitutes for it.

## Relationship to prior work

Andruszkiewicz and Rybołowicz classify Boolean trusses up to isomorphism and explicitly recover the commutative, left-zero, and right-zero factors. The inspected full text does not state an automorphism-group theorem, and a full-text search for the term “automorph” returns no occurrence. The present result passes from their intrinsic decomposition to the exact symmetry group of every finite Boolean truss.

The earlier paper *Ideal ring extensions and trusses* develops ring-extension models and truss isomorphisms. Its inspected full text likewise does not state an automorphism-group formula for finite Boolean trusses. General automorphism facts for rectangular bands do not by themselves give the result here because a truss automorphism must also preserve the abelian-heap structure; that requirement replaces arbitrary permutations of the left and right coordinates by affine automorphism groups.

## Limitations

The result is restricted to finite Boolean trusses. For infinite Boolean rings, the commutative factor need not reduce to a finite product of copies of \(\mathbb F_2\), and its automorphism group need not be a finite symmetric group. The holomorph description of a heap automorphism group uses a choice of heap origin; its abstract isomorphism type is independent of that choice.

A residual literature risk remains that an equivalent symmetry formula may appear in older work under combined semigroup-and-torsor terminology rather than the phrase “Boolean truss.” Targeted searches and inspection of the closest truss sources did not locate such a statement.

## References

1. R. R. Andruszkiewicz and B. Rybołowicz, *Boolean Trusses as Rectangular Bands and Boolean Rings*, arXiv:2609.31051v1, 2026.
2. R. R. Andruszkiewicz, T. Brzeziński, and B. Rybołowicz, *Ideal ring extensions and trusses*, arXiv:2101.09484, 2021.
