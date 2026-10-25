# Two coordinate-permutation modules in critical toroidal Vietoris–Rips homology

## Finding

Let \(k\ge2\) be an integer, put \(N=3k\), and give \(T=(\mathbb Z/N\mathbb Z)^2\) the product cyclic shortest-path metric
\[
d((x,y),(x',y'))=\min(|x-x'|,N-|x-x'|)+\min(|y-y'|,N-|y-y'|).
\]
Let \(K_k=\operatorname{VR}_{\le k}(T)\) be the clique complex of all finite vertex sets of diameter at most \(k\). Translations act on \(K_k\) through \(G=T\). Set
\[
H_x=\langle(k,0)\rangle,\qquad H_y=\langle(0,k)\rangle.
\]
Then **the rational translation representation** has the following exact decomposition:
\[
\boxed{H_2(K_k;\mathbb Q)\oplus\mathbb Q\ \cong\ \mathbb Q[G/H_x]\oplus\mathbb Q[G/H_y]}
\]
as rational \(G\)-modules. Here \(\mathbb Q\) is the trivial one-dimensional module, and \(\mathbb Q[G/H]\) is the permutation module of the indicated cosets. In particular, with \(g=(a,b)\in G\), its second-homology trace is
\[
\boxed{\operatorname{tr}(g\mid H_2(K_k;\mathbb Q))=
\begin{cases}
6k^2-1,&g=(0,0),\\
3k^2-1,&g\in(H_x\cup H_y)\setminus\{0\},\\
-1,&g\notin H_x\cup H_y.
\end{cases}}
\]
For complex characters \(\psi_{u,v}(a,b)=\exp(2\pi i(ua+vb)/N)\), indexed by \(0\le u,v<N\), the corresponding multiplicity is
\[
\boxed{m_{u,v}={\bf1}_{3\mid u}+{\bf1}_{3\mid v}-{\bf1}_{u=v=0}.}
\]
Consequently, \(\dim H_2(K_k;\mathbb Q)^G=1\), and \(|K_k|/G\) has the reduced rational homology of a two-sphere.

## Assumptions and scope

The metric is the **sum** of the two cyclic distances, not their maximum. The filtration uses the inclusive condition \(d\le k\), not a strict inequality. The integer \(k\) is at least two. All representation equivalences are over \(\mathbb Q\) (or after complexification where explicitly indicated); no integral splitting is claimed. The established 2025 homotopy classification of the same complexes is used as prior input: Adams, Adetowubo, Barriga-Acosta, Feng and Sterling prove \(K_k\simeq\bigvee^{6k^2-1}S^2\) for \(k\ge2\). That classification, and the value \(6k^2-1\) itself, are **not claimed as discoveries here**.

## Proof

**1. Homology concentration.** The cited toroidal-grid theorem (Theorem 5.10 of Adams et al., arXiv:2502.07134) gives \(H_0(K_k;\mathbb Q)\cong\mathbb Q\), \(H_2(K_k;\mathbb Q)\cong\mathbb Q^{6k^2-1}\), and all other reduced rational homology groups zero. Since \(K_k\) is connected, translations act trivially on \(H_0\). The identity trace in degree two is therefore \(6k^2-1\).

**2. Translation-fixed face lemma.** Fix a nonzero translation \(g=(a,b)\), and suppose it carries some nonempty simplex \(\sigma\subset K_k\) to itself. Such a simplex is a union of complete orbits of \(\langle g\rangle\). In a cyclic group of length \(3k\), the orbit of a coordinate under a translation of order \(d\) consists of \(d\) evenly spaced points and has cyclic diameter \(3k\lfloor d/2\rfloor/d\). This diameter exceeds \(k\) when \(d=2\) or \(d\ge4\). Thus the orders of both coordinate translations must belong to \(\{1,3\}\). A nonzero order-three coordinate step is either \(k\) or \(2k\); if both coordinates are nonzero then \(d(v,gv)=2k>k\), contradicting the simplex condition. Hence \(g\) is one of \((k,0),(2k,0),(0,k),(0,2k)\).

Consider \(g=(k,0)\); the other three cases follow by symmetry. Every nonempty invariant simplex contains the orbit triangle \(\{(x,y),(x+k,y),(x+2k,y)\}\). These three vertices are pairwise at distance \(k\). No second orbit can be part of the same simplex. Indeed, if a vertex \((z,w)\) has \(w\ne y\), at least one vertex of the displayed triangle has horizontal distance at least \(k\) from \(z\), and the positive vertical distance makes the total distance exceed \(k\). If \(w=y\) and \(z\) lies in a different horizontal orbit, one of the horizontal distances strictly exceeds \(k\). Thus invariant simplices are **exactly** the three-vertex axial orbits; there are \((3k)^2/3=3k^2\) of them. On each oriented triangle \(g\) induces a three-cycle, of sign \(+1\).

**3. Lefschetz traces.** The simplicial Lefschetz number is the alternating sum of signed fixed-face traces, equal to the alternating sum on homology. For \(g\in(H_x\cup H_y)\setminus\{0\}\), Step 2 gives \(L(g)=3k^2\), all in simplex dimension two. For any other nonidentity translation no nonempty simplex is fixed, so \(L(g)=0\). Since \(\operatorname{tr}(g\mid H_0)=1\) and there is no other reduced homology except degree two, \(\operatorname{tr}(g\mid H_2)=L(g)-1\). This proves the displayed character, including the identity case from Step 1.

**4. Representation and Fourier decomposition.** The permutation character of \(\mathbb Q[G/H_x]\) is \(|G/H_x|=3k^2\) on \(H_x\) and zero elsewhere; similarly for \(H_y\). Their sum minus the trivial character has exactly the traces of Step 3. Rational representations of a finite group are semisimple and determined by their ordinary characters (one may extend to \(\mathbb C\), compare multiplicities, and descend the equality of rational characters). This establishes the rational module isomorphism. The one-dimensional character \(\psi_{u,v}\) occurs in \(\mathbb C[G/H_x]\) precisely if \(3\mid u\), and in \(\mathbb C[G/H_y]\) precisely if \(3\mid v\). Subtracting the trivial summand gives the formula for \(m_{u,v}\). In particular \(m_{0,0}=1\). Since a finite group acting simplicially has a barycentrically subdivided admissible action, rational homology of the geometric quotient is the invariant rational homology, proving the quotient statement.

## Verification

The standalone `verify.py` checks the complete finite clique complexes for \(k=2\) and \(k=3\), enumerating respectively 888 and 24,678 nonempty faces, all 36 and all 81 translation elements, signed simplex-orientation contributions, Euler characteristics and the complete trace formulas. At \(k=2\), a separate certificate `morse_certificate.json` lists 432 matched face/coface pairs; the verifier checks that every face is accounted for, that the reversed-pair face-poset orientation is acyclic, and that the only critical cells consist of one vertex and 23 two-simplices. Discrete Morse theory then independently proves \(K_2\simeq\bigvee^{23}S^2\). The actual results are recorded in `verification_output.txt`. The **infinite** assertion follows from Steps 1–4 and the published general homotopy theorem, not from extrapolation of the finite checks.

## Relationship to prior work

Adamaszek and Adams (2015), arXiv:1503.03669, developed the cyclic Vietoris–Rips theory motivating the critical one-third cycle scale. The central same-object prior work is Adams–Adetowubo–Barriga-Acosta–Feng–Sterling (2025), arXiv:2502.07134, Theorem 5.10: it gives the entire nonequivariant homotopy type \(\bigvee^{6k^2-1}S^2\), including \(k=2\). Its full accessible preprint discusses facets, toroidal metric and homotopy, but does not provide this rational translation character or the two-coset representation identity. Thus neither the sphere-wedge count nor its derivation is presented here as new. The 2016 Chaparro Sumalave thesis studies Rips complexes of torus products with the *maximum* metric, whose product theorem does not imply this statement for the \(\ell^1\) graph metric. Published records concerning twisted grids at scale two, thin width-four toroidal grids and toroidal neighborhood/Čech complexes concern different regimes or constructions and do not yield this equivariant representation.

## Limitations

This result describes rational homology under the **translation subgroup**, not the action of the entire dihedral-by-coordinate-swap symmetry group. It does not give an integral \(G\)-module splitting, an explicit equivariant sphere-wedge equivalence, or all persistent homology. The result relies on a published nonequivariant homotopy theorem; the independent finite Morse certificate verifies only \(k=2\). Searches do not exclude equivalent unindexed equivariant work; an additional human literature audit is warranted.

## References

1. M. Adamaszek and H. Adams, *The Vietoris–Rips complexes of a circle*, arXiv:1503.03669 (first public preprint 2015-03-12), https://arxiv.org/abs/1503.03669.
2. H. Adams, A. Y. Adetowubo, H. Barriga-Acosta, Z. Feng and J. Sterling, *Vietoris–Rips complexes of torus grids*, arXiv:2502.07134 (first public preprint 2025-02-10), Theorem 5.10, https://arxiv.org/html/2502.07134v2.
3. G. Chaparro Sumalave, *Vietoris–Rips Complexes of the Circle and the Torus*, Universidad de los Andes master's thesis, October 2016, Chapter 3 (maximum-product metric), https://math.uniandes.edu.co/~aangel79/tesis/gustavo.pdf.
4. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145 (discrete Morse theorem used for the finite certificate).
