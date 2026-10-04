# An infinite composite-modulus counterfamily to the pretzel quiver formula
## Finding
For every odd prime \(p\ge5\), let
\[
L_p=P(p,p,p)
\]
be the positive \(3\)-pretzel knot and let \(R_{2p}\) be the dihedral quandle on \(\mathbb Z_{2p}\), with operation
\[
x\mathbin{\triangleright}y=2y-x.
\]

The full quandle coloring quiver of \(L_p\) has the following exact structure. The \(2p\) trivial colorings form one complete directed pseudograph in which every ordered pair has edge multiplicity \(2p\). The nontrivial colorings split into exactly \(p+1\) complete directed pseudographs, each with
\[
2p(p-1)
\]
vertices and edge multiplicity \(2\). From every vertex of every nontrivial block there are exactly \(2\) edges to each trivial coloring, and there are no edges between different nontrivial blocks.

Equivalently, the nontrivial strongly connected components are indexed by
\[
\mathbb P^1(\mathbb F_p).
\]

For these same parameters, Theorem 29 of Meng--Liu--Zhou has
\[
d_1=d_2=p
\]
and predicts only four nontrivial strongly connected components: three of size
\[
2p(p-1)
\]
and one of size
\[
2p(p-1)(p-2).
\]
Therefore Theorem 29 is false for every odd prime \(p\ge5\).

At the smallest counterexample \(p=5\), the actual strongly connected component sizes are
\[
10,40,40,40,40,40,40,
\]
whereas Theorem 29 predicts
\[
10,40,40,40,120.
\]

## Assumptions and scope
The source denotes the dihedral quandle by \(\mathbb Z_n\); here \(R_n\) is used to distinguish the quandle from its underlying cyclic group.

The source's Theorem 20 gives the coloring equations for the positive \(3\)-pretzel link \(P(p_1,p_2,p_3)\). The source's Theorem 29 is stated for positive integers \(p_1,p_2,p_3,n\) when
\[
d_1=\gcd(\gcd(p_1,p_2,p_3),n)
\]
and
\[
d_2=\gcd\left(\frac{|p_1p_2+p_1p_3+p_2p_3|}{\gcd(p_1,p_2,p_3)},n\right)
\]
are primes.

For \(p_1=p_2=p_3=p\) and \(n=2p\),
\[
d_1=d_2=p,
\]
so every odd prime \(p\) lies within the printed hypotheses. Since \(p\) is odd, \(P(p,p,p)\) is a knot.

## Proof
The source's coloring equations are
\[
p_1(p_3-1)(a-b)+p_3(c-a)\equiv0\pmod n
\]
and
\[
p_1(p_2+1)(a-b)+p_2(c-b)\equiv0\pmod n.
\]
Set \(p_1=p_2=p_3=p\) and \(n=2p\). Because both \(p-1\) and \(p+1\) are even, these reduce to
\[
p(c-a)\equiv0\pmod{2p},
\qquad
p(c-b)\equiv0\pmod{2p}.
\]
Thus \(a,b,c\) have one common parity. Every coloring has a unique representation
\[
(a,b,c)=(e+2A,e+2B,e+2C),
\qquad
e\in\mathbb F_2,\quad A,B,C\in\mathbb F_p.
\]
Hence there are \(2p^3\) colorings, agreeing with Theorem 20.

Taniguchi's Lemma 3.4 states that every endomorphism of \(R_n\), for arbitrary \(n>1\), is uniquely affine:
\[
f_{r,s}(x)=rx+s,
\qquad
r,s\in\mathbb Z_n.
\]
For a nontrivial coloring define
\[
v(a,b,c)=
\left(
\frac{b-a}{2},
\frac{c-a}{2}
\right)
\in
\mathbb F_p^2\setminus\{0\}.
\]
Division by \(2\) here means: first use that both differences are even in \(\mathbb Z_{2p}\), then identify the resulting residues modulo \(p\).

Under \(f_{r,s}\),
\[
v(f_{r,s}(a),f_{r,s}(b),f_{r,s}(c))
=
\bar r\,v(a,b,c),
\]
where \(\bar r\) is the residue of \(r\) modulo \(p\). Therefore every nonconstant image preserves the projective class
\[
[v]\in\mathbb P^1(\mathbb F_p).
\]
If \(\bar r=0\), all three output colors are equal, so the image is trivial.

Fix one projective class \(\ell\). There are \(p-1\) nonzero vectors on \(\ell\), \(p\) choices of \(A\), and \(2\) choices of parity \(e\). Thus the corresponding block has
\[
2p(p-1)
\]
colorings. Since
\[
|\mathbb P^1(\mathbb F_p)|=p+1,
\]
there are exactly \(p+1\) such blocks.

Between two nontrivial colorings in the same projective block, the residue \(\bar r\in\mathbb F_p^\times\) is uniquely determined by their difference vectors, and the residue of \(s\) modulo \(p\) is then uniquely determined by one coordinate. The residue of \(r\) modulo \(2\) can be chosen in two ways, after which the residue of \(s\) modulo \(2\) is forced. By the Chinese remainder theorem there are exactly \(2\) affine endomorphisms between the two colorings.

The same count gives exactly \(2\) endomorphisms from any nontrivial coloring to any prescribed trivial coloring. For two trivial colorings, \(r\) can be arbitrary in \(\mathbb Z_{2p}\), and \(s\) is then determined, giving edge multiplicity \(2p\). No endomorphism can send one nontrivial projective class to another.

Finally, substituting \(n=2p\) and \(d_1=d_2=p\) into Theorem 29 gives two nontrivial blocks from \(G_2\), one from \(G_3\), and one asserted complete \(G_4\) block on
\[
2p(p-1)(p-2)
\]
vertices. For \(p\ge5\), that last block actually splits into \(p-2\) projective blocks of size \(2p(p-1)\). The strongly connected component decompositions differ, so the theorem is false as stated.

## Verification
The recent source was inspected at Theorem 20, its explicit coloring equations, Theorem 29, and the subsequent prime-modulus theorem. Its arXiv record gives primary MSC \(57K10\) and first submission date 2026-09-24.

The affine-endomorphism lemma was independently checked in Taniguchi's earlier paper. It applies to every dihedral quandle order \(n>1\), not only prime order.

The bundled verifier directly constructs every coloring and every affine endomorphism for
\[
p=5,7,11.
\]
For each coloring it checks the complete target set and every edge multiplicity against the projective-block description. It prints:

`VERIFY_OK primes=5,7,11 p5_actual=10+40+40+40+40+40+40 p5_theorem29=10+40+40+40+120 projective_block_pattern=true`

This finite replay is not the infinite proof. The all-prime conclusion follows from the symbolic parity reduction, the affine-endomorphism theorem, the projective invariant, and the Chinese remainder theorem.

## Relationship to prior work
Meng--Liu--Zhou Theorem 29 gives the composite-modulus block formula refuted here. Their later Theorem 30 treats prime modulus and therefore does not apply to the present modulus \(2p\).

Taniguchi proves that every dihedral-quandle endomorphism is affine and develops general comparison results for prime and squarefree composite orders. Those results supply an important structural input, but the inspected paper does not state the present \(P(p,p,p)\), \(R_{2p}\) decomposition or identify the failure of Meng--Liu--Zhou Theorem 29.

The discrepancy is not a coloring-number error. Both formulas have the same total
\[
2p^3
\]
vertices. The failure is in connectivity: the printed \(G_4\) merges \(p-2\) distinct projective classes that affine endomorphisms cannot connect.

Searches using the source title, theorem number, equal-prime condition, \(P(5,5,5)\), \(R_{10}\), composite dihedral quandles, and projective-block formulations did not locate an earlier statement of this counterfamily.

## Limitations
The result refutes Theorem 29 as stated and gives an exact repair on the infinite subfamily
\[
(P(p,p,p),R_{2p}),
\qquad p\ge5\text{ prime}.
\]
It does not provide a corrected version of Theorem 29 for every composite modulus and every triple \((p_1,p_2,p_3)\).

The projective decomposition exploits the special parity form of the coloring equations on this subfamily. Additional arithmetic strata can occur for other composite moduli.

## References
1. Q. Meng, X. Liu, and B. Zhou, *Quandle coloring quivers of pretzel links*, arXiv:2609.29127v1, first submitted 2026-09-24.
2. Y. Taniguchi, *Quandle coloring quivers of links using dihedral quandles*, arXiv:2004.12437v1; Journal of Knot Theory and Its Ramifications 30 (2021), 2150011.
