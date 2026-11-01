# The full \(2^4\rtimes S_5\) homology character of the Clebsch independence complex

## Finding
Let \(A=\mathbb F_2^4\), let \(u_1,\ldots,u_4\) be its coordinate vectors and \(u_5=u_1+u_2+u_3+u_4\). Let \(C=\operatorname{Cay}(A,\{u_1,\ldots,u_5\})\) be the degree-five Clebsch (folded five-cube) graph and \(K=\operatorname{Ind}(C)\). Its full graph automorphism group is \(G=A\rtimes S_5\), where \(S_5\) permutes the five generators. For each \(i\), let \(a_i:A\to\mathbb F_2\) be the unique linear functional with \(a_i(u_i)=0\) and \(a_i(u_j)=1\) for \(j\ne i\), and put \(\epsilon_i(t)=(-1)^{a_i(t)}\). For every \(t\in A\) and \(\sigma\in S_5\), writing \(f(\sigma)=|\{i:\sigma(i)=i\}|\), the complete rational third-homology character is
\[
\operatorname{tr}((t,\sigma)\mid\widetilde H_3(K;\mathbb Q))
=\operatorname{sgn}(\sigma)\left(f(\sigma)-1+\sum_{\sigma(i)=i}\epsilon_i(t)\right).
\]
As a \(\mathbb Q[G]\)-module this is the direct sum of the inflation of \(\operatorname{sgn}_{S_5}\otimes\mathrm{Std}_{S_5}\) and the five-dimensional induced module \(\operatorname{Ind}_{A\rtimes S_4}^{G}(\epsilon_5\otimes\operatorname{sgn}_{S_4})\), where \(S_4\) fixes generator \(u_5\). In particular, the translation-fixed subspace has dimension four, while the full-automorphism-fixed subspace is zero. The nonequivariant wedge \(K\simeq\bigvee^9 S^3\) is already known and is not claimed as original.

## Assumptions and scope
Take \(A\) to be a four-dimensional vector space over the two-element field, with bit-mask labels \(0,\ldots,15\). Its five edge directions are \(1,2,4,8,15\). The graph joins distinct vertices whose bitwise xor lies in that set. The complex \(K\) consists of all independent vertex subsets, including the empty face. All homology representations are over \(\mathbb Q\), in reduced degree three; this makes the group-character statement distinct from the integral nonequivariant homotopy classification. The first available historical topology reference underlying the direction was publicly posted on 2010-07-02 (Barmak, arXiv:1007.0418v1).

The five functionals \(a_i\) exist uniquely because the five directions have the single linear relation \(u_1+\cdots+u_5=0\), and the prescribed five values, four equal to one and one equal to zero, satisfy that relation in characteristic two. In bit-mask dual coordinates their masks are \(14,13,11,7,15\), respectively.

## Proof
**1. Full symmetry group.** Translations of \(A\) and linear changes of coordinates permuting the five directions give \(16\cdot120=1920\) distinct automorphisms. Conversely an automorphism is determined by its image of the zero vertex and by the induced permutation of its five neighbors. Indeed, for any two distinct directions \(u_i,u_j\), the vertices \(0\) and \(u_i+u_j\) are precisely the common neighbors of \(u_i\) and \(u_j\). The other ten vertices are uniquely indexed by unordered pairs of directions. Therefore the stabilizer of zero embeds into \(S_5\), and these 1,920 automorphisms exhaust the group.

**2. Homology concentration.** An exhaustive independent-set enumeration on sixteen vertices yields exactly 392 nonempty faces, with face vector \((16,80,160,120,16)\) by dimensions zero through four. Order the vertices by
`(3,14,7,9,13,11,4,5,12,8,1,0,15,6,2,10)`.
Starting with all faces unmatched, at each vertex \(v\) pair every still-unmatched face \(F\) not containing \(v\) with the also-unmatched face \(F\cup\{v\}\), scanning faces by integer bit mask. The program reconstructs 191 pairs, leaving exactly one critical vertex and nine critical tetrahedra. On the 1,200 nonempty face-incidences, reverse matched arrows and topologically sort; all 392 faces are removed. This is an exhaustive acyclicity certificate, not a sample. Forman's theorem yields \(K\simeq\bigvee^9 S^3\), and hence \(\widetilde H_i(K;\mathbb Q)=0\) for \(i\ne3\) and \(\dim\widetilde H_3(K;\mathbb Q)=9\). This argument independently verifies the homology premise, while acknowledging the previous public nonequivariant result.

**3. Signed Lefschetz character.** For any affine automorphism \(g\), the reduced simplicial Lefschetz identity and concentration in degree three give
\[
\chi_H(g)=1+\sum_{\substack{\varnothing\ne F\in K\\gF=F}}(-1)^{|F|}\operatorname{sgn}(g|_F).
\]
Here \(\operatorname{sgn}(g|_F)\) is the permutation sign on the vertices of \(F\), in increasing bit-mask order. Equivalently, decompose the sixteen graph vertices into \(g\)-orbits, discard orbits that have internal graph edges, and form all compatible sets \(J\) of the remaining orbits. Each selected vertex orbit contributes minus one, yielding
\[
\chi_H(g)=\sum_{J\text{ pairwise compatible}}(-1)^{|J|}.
\]
The two formulas are independently enumerated by different loops. Exhaustively applying both to all \(16\cdot5!=1920\) distinct pairs \((t,\sigma)\) gives exactly the formula stated in the Finding. The complete verifier checks equality, for every pair, against an independently evaluated right-hand side. In particular pure translations have traces \(9\) once, \(1\) five times, and \(5\) ten times; their Fourier multiplicities are four at the trivial character and one at each of the five characters \(\epsilon_i\), with all other multiplicities zero.

**4. Identification of the module.** The sign-twisted standard \(S_5\)-module has character \(\operatorname{sgn}(\sigma)(f(\sigma)-1)\) and translations act trivially. For the induced module, use coset basis indexed by the five distinguished directions. The affine element \((t,\sigma)\) contributes to its trace only at positions fixed by \(\sigma\). On each fixed position \(i\), the contribution is \(\operatorname{sgn}(\sigma)\epsilon_i(t)\). The sum is exactly the second term in the displayed character formula. Since finite-dimensional rational representations of a finite group are semisimple and their characters determine their isomorphism classes, the stated direct sum is the full rational homology representation.

The translation-invariant space comes entirely from the four-dimensional first summand. Its \(S_5\)-representation is the sign-twisted standard module, which has no invariant vector. The second summand has no translation-invariant vector. Thus \(\dim\widetilde H_3(K;\mathbb Q)^A=4\) and \(\dim\widetilde H_3(K;\mathbb Q)^G=0\).

## Verification
Run `python3 verify_clebsch_action.py` from the same directory; only the Python standard library is required. It reconstructs all face masks and the graph, checks the strongly regular neighbor conditions, every matching pair and every directed cover relation, and topologically sorts the complete oriented face-incidence diagram. It then checks all 1,920 affine transformations against both the signed-fixed-simplex character and the independent vertex-orbit method, and verifies both equal the asserted representation character. It also computes all sixteen translation Fourier multiplicities by exact integer sums. The recorded output ends with `VERIFY_OK`; the verifier can be rerun without external data or cached certificates.

## Relationship to prior work
Barmak's 2010 theorem shows that independence complexes of triangle-free graphs are suspensions, a nonequivariant result which does not identify this automorphism representation. Two previously published calculations for exactly the same Clebsch/folded-five-cube independence complex establish the integral homotopy equivalence to nine three-spheres; those results are credited and **not** relabeled as discoveries here. Their inspected findings, proofs, and stated scope do not compute actions of translations, the full semidirect product, or a rational homology character. The complete group module in the Finding is additional information, not a restatement of the Betti number. Searches also considered the complementary degree-ten Clebsch clique complex, the Greenwood–Gleason and Segre/projective-cube names, and stronger equivariant claims; none located a covering statement.

## Limitations
The character is for this sixteen-vertex graph only, not an all-dimension folded-cube representation theorem. The proof uses exhaustive finite enumeration of 392 faces and 1,920 automorphisms; correctness is conditional on the transparent standalone finite verifier and standard discrete-Morse, Lefschetz, and character-theory arguments. An equivalent representation could appear in unindexed literature. No claim of external or independent certification is made.

## References
1. J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418v1, first publicly posted 2010-07-02, especially Theorem 3.4: https://arxiv.org/html/1007.0418v1.
2. *The folded five-cube independence complex is a wedge of nine three-spheres*, publicly accessible research record dated 2026-10-11: https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-the-folded-five-cube-independence-complex-is-bigvee-9-s-3--fb89079b9172.
3. *The Clebsch independence complex is a wedge of nine three-spheres*, publicly accessible research record dated 2026-10-11: https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-the-clebsch-independence-complex-is-a-wedge-of-nine-3-spheres--344f83b86fa0.
4. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145. https://doi.org/10.1006/aima.1997.1650.
