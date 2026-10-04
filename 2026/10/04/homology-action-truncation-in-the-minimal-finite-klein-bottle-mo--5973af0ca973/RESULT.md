# Homology-action truncation in the minimal finite Klein-bottle models
## Finding
For either 16-point minimal finite model \(K_{1,0}\) or \(K_{0,1}\) of the Klein bottle, there are exactly \(7{,}678{,}760\) continuous self-maps and exactly ten induced endomorphisms of
\[
H_1(K;\mathbb Z)\cong\mathbb Z\oplus\mathbb Z/2.
\]
Choose an order-two class \(t\) and a free generator \(x\). Every induced map has
\[
t\mapsto\delta t,\qquad x\mapsto kx+\varepsilon t,
\]
where \(k\in\{-1,0,1\}\) and \(\delta,\varepsilon\in\mathbb Z/2\), with \(\delta=0\) when \(k=0\). Conversely, every such triple occurs. Exactly 16 self-maps induce integral-homology isomorphisms, and those 16 maps are exactly the homeomorphisms.

The classical Klein bottle admits the same parity pattern with arbitrary integer \(k\). Thus the cardinality-minimal finite models retain the classical torsion/free parity constraint while truncating the free multiplier to \(-1,0,1\).

## Assumptions and scope
Finite \(T_0\) spaces are identified with specialization posets, so continuous maps are order-preserving. The model \(K_{1,0}\) is the 16-point height-two poset of Cianci--Ottina; \(K_{0,1}\) is its opposite. The statement concerns direct self-maps of these finite spaces, not subdivisions, refinements, or larger finite models.

Label minima \(c_1,\ldots,c_4\), middle points \(b_1,\ldots,b_8\), and maxima \(a_1,\ldots,a_4\). The lower covers are
\[
b_1,b_7>c_1,c_3,\quad b_2,b_8>c_2,c_4,\quad
b_4,b_5>c_1,c_2,\quad b_3,b_6>c_3,c_4,
\]
and the upper covers are
\[
a_1>b_1,b_2,b_3,b_4,\quad a_2>b_1,b_2,b_5,b_6,
\]
\[
a_3>b_3,b_5,b_7,b_8,\quad a_4>b_4,b_6,b_7,b_8.
\]

## Proof
The order complex has 48 oriented one-simplices and 32 two-simplices. Use
\[
t=[c_1,b_4]-[c_2,b_4]+[c_2,b_5]-[c_1,b_5]
\]
and
\[
x=[c_1,b_1]-[c_3,b_1]+[c_3,b_7]-[c_1,b_7].
\]
The verifier checks an explicit integral two-chain \(S\) with \(\partial S=2t\), a mod-two cocycle \(\tau\) with \(\tau(t)=1,\tau(x)=0\), and an integral cocycle \(\alpha\) with \(\alpha(t)=0,\alpha(x)=1\). It also verifies
\[
\operatorname{rank}_{\mathbb Q}d_1=15,\qquad
\operatorname{rank}_{\mathbb Q}d_2=32,\qquad
\operatorname{rank}_{\mathbb F_2}d_2=31,
\]
consistent with \(H_1(K;\mathbb Z)\cong\mathbb Z\oplus\mathbb Z/2\).

For a self-map \(f\), set
\[
k=\alpha(f_\#x),\qquad \delta=\tau(f_\#t),\qquad \varepsilon=\tau(f_\#x).
\]
Exhaustive enumeration gives exactly these multiplicities:

| \(k\) | \(\delta\) | \(\varepsilon\) | maps |
|---:|---:|---:|---:|
| \(0\) | \(0\) | \(0\) | \(7{,}661{,}824\) |
| \(0\) | \(0\) | \(1\) | \(11{,}072\) |
| \(-1\) | \(0\) | \(0\) | \(1{,}462\) |
| \(-1\) | \(0\) | \(1\) | \(1{,}462\) |
| \(1\) | \(0\) | \(0\) | \(1{,}462\) |
| \(1\) | \(0\) | \(1\) | \(1{,}462\) |
| \(-1\) | \(1\) | \(0\) | \(4\) |
| \(-1\) | \(1\) | \(1\) | \(4\) |
| \(1\) | \(1\) | \(0\) | \(4\) |
| \(1\) | \(1\) | \(1\) | \(4\) |

The sum is \(7{,}678{,}760\). The induced map is an isomorphism exactly for \(k=\pm1\) and \(\delta=1\); there are 16 such maps. The verifier independently finds exactly 16 bijective order-preserving maps, and the two sets coincide, so integral-homology isomorphism is equivalent here to being a homeomorphism.

Order reversal does not change the set of order-preserving self-functions, and the order complexes of a poset and its opposite have the same abstract simplices. Transporting generators therefore gives the same result for \(K_{0,1}\).

Gonçalves--Kelly's classical normal forms imply after abelianization
\[
t\mapsto\delta t,\qquad x\mapsto kx+\varepsilon t
\]
for arbitrary integer \(k\), with \(\delta=0\) for even \(k\), arbitrary \(\delta\) for odd \(k\), and arbitrary \(\varepsilon\). The ten finite-model actions are exactly the members of that family with \(k\in\{-1,0,1\}\).

## Verification
Run `python3 verify.py`. It reconstructs the poset, checks the cycle/cocycle and rank certificates, exhaustively enumerates every order-preserving self-map, computes all induced actions, and independently checks bijectivity. Its summary is:
`VERIFY_OK`
`continuous_self_maps=7678760`
`induced_H1_endomorphisms=10`
`bijective_self_maps=16`
`H1_isomorphism_maps=16`
`free_multipliers=-1,0,1`
`opposite_model_same_result=true`

## Relationship to prior work
Cianci--Ottina prove that the Klein bottle has exactly two 16-point minimal finite models and give the explicit posets; the inspected material does not give this self-map census or induced-homology image. Gonçalves--Kelly classify classical Klein-bottle self-maps; their result yields the unrestricted homological parity family but not which actions are realized directly on either 16-point model. Targeted model-name, alias, exact-count, and published-finding corpus searches found no source stating the finite census, the ten-element image, or the multiplier truncation.

## Limitations
The result concerns direct self-maps of the two cardinality-minimal models and does not constrain larger finite models or subdivisions. The exhaustive component is computer-assisted but is replayable from the embedded deterministic verifier. Literature search cannot exclude every obscure or unindexed source, so a residual originality risk remains.

## References
D. L. Gonçalves and M. R. Kelly, “Wecken type problems for self-maps of the Klein bottle,” *Fixed Point Theory and Applications* (2006), Article ID 75848, DOI 10.1155/FPTA/2006/75848.

N. Cianci and M. Ottina, “Poset splitting and minimality of finite models,” arXiv:1512.06088v1 (2015), later published in *Journal of Combinatorial Theory, Series A*.
