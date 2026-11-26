# Chordality of full commuting graphs of odd dihedral-quandle endomorphisms

## Finding

Let \(n\ge 3\) be odd, and let \(R_n=\mathbb Z/n\mathbb Z\) have the dihedral-quandle operation \(x\triangleright y=2y-x\). Let \(\Gamma_n\) be the simple graph on **all** quandle endomorphisms of \(R_n\), joining distinct maps exactly when they commute. Then
\[
\Gamma_n\text{ is chordal}\quad\Longleftrightarrow\quad n\text{ is a prime power}.
\]
For \(n=p^e\) there is an explicit recursive perfect-elimination order: remove first the vertices with a unit coordinate in determinant coordinates. For \(e=1\) only zero remains; for \(e\ge2\), lift the order modulo \(p^{e-2}\) to the remaining vertices, one fiber at a time. In particular \(\Gamma_{p^e}\) is perfect and its chromatic number is \(p^e\). If \(n\) has at least two distinct prime factors, an induced four-cycle is given by orthogonal Chinese remainder idempotents.

## Assumptions and scope

The graph includes the identity, constant maps and noninvertible endomorphisms. A graph is chordal if it has no induced cycle of length at least four. A perfect-elimination order is an ordering in which every vertex's neighbors later in the order form a clique. We use the standard equivalence between chordality and existence of such an order, and the fact that greedy coloring in reverse order uses the clique number of the graph. The auxiliary determinant graph at modulus \(1\) consists of one vertex. No assertion about even moduli is needed.

## Proof

**Determinant coordinates.** If \(f\) is an endomorphism, put \(h(x)=f(x)-f(0)\). Then \(h(2y-x)=2h(y)-h(x)\). Specializing gives \(h(-x)=-h(x)\) and \(h(2y)=2h(y)\). It follows that \(h(2y+x)=h(2y)+h(x)\), and, as \(2\) is invertible modulo \(n\), \(h\) is additive. Thus \(f(x)=ax+b\); conversely every map of this form preserves the operation. The maps \(ax+b\) and \(cx+d\) commute exactly when \((a-1)d-(c-1)b=0\pmod n\). The coordinates \((a-1,b)\) identify \(\Gamma_n\) with the graph on pairs over \(\mathbb Z/n\mathbb Z\) in which adjacency is vanishing of the determinant, with loops excluded.

**Primitive vertices.** For \(n=p^e\), call a vector \(v\) primitive if at least one coordinate is a unit. Solving the equation \(\det(v,w)=0\) using that coordinate gives \(w=tv\) for a unique \(t\in\mathbb Z/p^e\mathbb Z\). All vectors on this line commute pairwise. Thus each primitive vertex has a complete closed neighborhood, of size \(p^e\). They can be eliminated in arbitrary order, since deleting earlier vertices cannot spoil this property. When \(e=1\), just the zero vector remains.

**The nonprimitive subgraph.** For \(e\ge2\) each remaining vector is uniquely \(px\) with \(x\) a vector modulo \(p^{e-1}\). Define its fiber label to be \(x\bmod p^{e-2}\). Each fiber has \(p^2\) vertices and induces a clique. Two different fibers are fully joined if and only if their labels are adjacent in the determinant graph modulo \(p^{e-2}\), since
\[
\det(px,py)=0\pmod{p^e}\quad\Longleftrightarrow\quad\det(x,y)=0\pmod{p^{e-2}}.
\]
For \(e=2\) this gives one complete fiber. Inductively take a perfect-elimination order of the base labels and eliminate each fiber in turn, in any internal order. At a vertex, its later neighbors are the remaining vertices of its own fiber and all later fibers whose labels neighbor its own. The later neighboring labels form a clique, so all of these neighbors form a clique. This proves that the lifted order is a perfect-elimination order and proves chordality. Restricting this order to any induced subgraph gives a perfect-elimination order there, proving perfectness by reverse greedy coloring.

**Chromatic number.** A primitive line is a clique of size \(p^e\), and any clique meeting a primitive vertex is contained in its line. A clique in the nonprimitive subgraph uses fibers over a clique in the smaller graph, hence has size at most \(p^2p^{e-2}=p^e\) by induction, with the one-vertex graph at exponent zero. For \(e=1\) the primitive line bound and the singleton core suffice. Thus the clique number is \(p^e\); the elimination order gives a coloring with exactly that many colors.

**Obstruction at other odd moduli.** Write \(n=rs\) with \(r,s>1\) relatively prime. Let \(\epsilon_r\) and \(\epsilon_s\) be the idempotents corresponding to \((1,0)\) and \((0,1)\) in the Chinese remainder coordinates. In the stated cyclic order the four distinct vertices
\[
(\epsilon_r,0),\quad(\epsilon_s,0),\quad(0,\epsilon_r),\quad(0,\epsilon_s)
\]
have consecutive determinant zero, since \(\epsilon_r\epsilon_s=0\); the two opposite determinants are the nonzero idempotents \(\epsilon_r\) and \(\epsilon_s\). This is an induced four-cycle, completing the dichotomy.

## Verification

Run `python3 verify.py` in this directory. It checks the endomorphism normal form by exhaustive function enumeration at \(n=3,5\); compares the determinant relation against affine composition and tests the lifted elimination order at \(n=3,5,9,25,27\); and tests the four-cycle by affine composition at \(n=15,21,45\). These finite cases corroborate the proof but do not establish the all-modulus conclusion.

## Relationship to prior work

Cameron–Kuzma introduced deep commuting graphs, and Hatui–Mukherjee–Patra studied them, including finite abelian examples and strong products. The rank-two determinant graph here has been identified with the deep commuting graph of \((\mathbb Z/p^e\mathbb Z)^2\), and its clique number and the classification and count of maximum cliques were established in *Maximum pairwise lift-commuting subsets*. Those results are not new here. The strong-product description also explains the negative side of the boundary: in a product of two noncomplete factors with dominant vertices, induced three-vertex paths through the dominant vertices give the same four-cycle. The direct remainder-idempotent proof gives its labels in the endomorphism graph.

The determinant criterion, field case, and assorted numerical invariants for related upper triangular ring commuting graphs were studied by Cheraghpour and collaborators. The chain-ring computations in *Two-pole commuting tuple and clique enumerators* use a unit pivot and a reduction of nonprimitive determinant-zero tuples, related to the two adjacency calculations used here. That record gives all-size clique enumerators, which are not part of the finding here. The focus is the graph-structural use of the complete-neighborhood and quotient reductions to establish an explicit elimination order and the chordality boundary. It does not assert historical priority for these determinant reductions.

## Limitations

The positive statement is about the full graph for odd prime-power moduli. The obstruction treats odd moduli with multiple prime factors; no chromatic number is computed for these moduli. The result makes no claim about even dihedral-quandle moduli or about all-size clique enumeration. The literature comparison is bounded.

## References

1. P. J. Cameron and B. Kuzma, *Between the enhanced power graph and the commuting graph*, https://arxiv.org/abs/2012.03789, DOI 10.1002/jgt.22871.
2. S. Hatui, S. Mukherjee and K. L. Patra, *On the deep commuting graph of a finite group*, Lemma 2.10 and Sections 3–4, https://arxiv.org/abs/2511.13303.
3. *Maximum pairwise lift-commuting subsets in \(C_{p^a}\times C_{p^a}\)*, https://github.com/Resultary/2026/blob/main/2026/10/4/SCOPE-maximum-pairwise-lift-commuting-subsets-in-c-p-a-imes-c-p-a--6b7aca53a924/RESULT.md.
4. H. Cheraghpour, M. N. Ghosseiri, M. Jafari and F. Seyfpour, *On Commuting graphs of triangular rings*, https://arxiv.org/abs/2402.12619v1.
5. *Two-pole commuting tuple and clique enumerators for triangular algebras*, https://github.com/Resultary/2026/blob/main/2026/11/2/SCOPE-two-pole-commuting-tuple-and-clique-enumerators-for-triangular-a--8fae3394a05c/RESULT.md.
