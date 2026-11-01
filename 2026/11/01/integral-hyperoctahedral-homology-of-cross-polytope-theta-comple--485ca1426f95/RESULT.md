# Integral hyperoctahedral homology of cross-polytope theta complexes

## Finding

Let \(n\ge2\) and \(1\le k\le n-1\). Form the face hypergraph \(\mathcal H_{n,k}\) of the \(n\)-dimensional cross-polytope: its vertices are \(\{i^+,i^-:1\le i\le n\}\) and its hyperedges choose one signed vertex from each of \(k+1\) distinct antipodal pairs. Let \(\Theta_{n,k}=\Theta(\mathcal H_{n,k})\), with faces the vertex subsets avoiding some hyperedge.

The hyperoctahedral group \(B_n=(C_2)^n\rtimes S_n\) acts naturally. Define its sign-flip character \(\eta:B_n\to\{\pm1\}\) by \(\eta((\epsilon_i),\pi)=\prod_{i=1}^{n}\epsilon_i\). Let \(U_n=\ker(\mathbb Z^n\xrightarrow{\sum}\mathbb Z)\), with coordinate-permutation action of \(S_n\), inflated to \(B_n\). For \(d=2n-k-2\), the **complete integral homology-module classification** is

\[
\widetilde H_i(\Theta_{n,k};\mathbb Z)\cong_{\mathbb Z[B_n]}
\begin{cases}
\mathbb Z_\eta\otimes_{\mathbb Z}(\bigwedge^k U_n)^*,&i=d,\\
0,&i\ne d,
\end{cases}
\]

where \(M^*=\operatorname{Hom}_{\mathbb Z}(M,\mathbb Z)\) carries the contragredient action. In particular the unique reduced Betti number is \(\binom{n-1}{k}\), and there is no integral torsion. The rational character on \(g=((\epsilon_i),\pi)\) has the exact cycle formula

\[
\operatorname{tr}(g\mid\widetilde H_d(\Theta_{n,k};\mathbb Q))=
\left(\prod_i\epsilon_i\right)[t^k]
\frac{\prod_{c\in\operatorname{Cyc}(\pi)}(1-(-t)^{|c|})}{1+t}.
\]

For \(k=1\) and every \(n\ge3\), the restriction to the unsigned subgroup \(S_n\) is the **weight lattice** \(U_n^*\cong\mathbb Z^n/\mathbb Z(1,\ldots,1)\), not the root (augmentation-kernel) lattice \(U_n\). These two integral \(S_n\)-modules are not isomorphic, although their rationalizations are isomorphic. This is a characteristic-dependent distinction that the previously known wedge-of-spheres homotopy type cannot detect.

## Assumptions and scope

The ranges \(n\ge2\) and \(1\le k\le n-1\) are inclusive. All homology is reduced, ordinary simplicial homology of the unquotiented theta complex over \(\mathbb Z\). The group acts by permuting the \(2n\) signed vertices. The displayed module is an integral module, not merely a rational character identity or a statement about Borel equivariant homology. The case \(k=1\), \(n=2\), is included in the module formula but excluded from the nonisomorphism corollary.

## Proof

**1. Identify the Alexander dual.** A subset of signed vertices is independent in \(\mathcal H_{n,k}\) if and only if it meets at most \(k\) antipodal pairs: if it meets \(k+1\) pairs, choosing one vertex from each produces a forbidden hyperedge, and the converse is immediate. Thus \(I_{n,k}=\operatorname{Ind}(\mathcal H_{n,k})\) has simplices exactly those supports of size at most \(k\). By the definition of the theta complex, \(\Theta_{n,k}=\operatorname{AD}(I_{n,k})\) on the full \(2n\)-vertex set.

**2. Compute the integral module of the independence complex.** Let \(L_{n,k}=\operatorname{sk}_{k-1}\Delta^{n-1}\), the \((k-1)\)-skeleton of the simplex on the unsigned indices \(1,\ldots,n\). The support projection \(p:I_{n,k}\to L_{n,k}\) sends both \(i^+\) and \(i^-\) to \(i\). It is \(B_n\)-equivariant if sign flips act trivially on the target. A simplicial section \(s\) chooses every positive vertex; \(p\circ s=\mathrm{id}\). For every face \(\sigma\) of \(I_{n,k}\), the union \(\sigma\cup s(p(\sigma))\) still meets at most \(k\) antipodal pairs and is a face. Consequently \(s\circ p\) is contiguous to the identity. Hence \(p_*\) is an integral homology isomorphism and is \(B_n\)-equivariant, even though the chosen section is not equivariant.

Write \(E_n=\mathbb Z^n\) with ordered generators \(e_i\) and augmentation \(\varepsilon(e_i)=1\). The augmented chains of the full simplex are \(\widetilde C_{j-1}=\bigwedge^jE_n\) with differential \(\iota_\varepsilon\), contraction by \(\varepsilon\). Splitting \(E_n=\mathbb Ze_1\oplus U_n\) shows \(\ker(\iota_\varepsilon:\bigwedge^kE_n\to\bigwedge^{k-1}E_n)=\bigwedge^k U_n\). There are no chains in dimension \(k\) in the skeleton; in lower degrees the full-simplex complex is exact. Thus

\[
\widetilde H_i(I_{n,k};\mathbb Z)=
\begin{cases}
\bigwedge^k U_n,&i=k-1,\\
0,&i\ne k-1,
\end{cases}
\]

as integral \(B_n\)-modules, with sign flips acting trivially.

**3. Track the orientation in integral Alexander duality.** For a finite simplicial complex \(K\) on an ordered \(N\)-element vertex set \(V\), the signed complement identification of relative simplex chains and dual cochains, together with the long exact sequence of \((\Delta^{N-1},K)\), yields

\[
\widetilde H_i(\operatorname{AD}(K);\mathbb Z)
\cong \mathbb Z_{\operatorname{sgn}_V}\otimes
\widetilde H^{N-i-3}(K;\mathbb Z).
\]

It is natural for permutations when the sign of the permutation of the entire oriented vertex set is included: the complement orientation times the original orientation equals the ambient orientation. This is the equivariant sign refinement of integral combinatorial Alexander duality; it follows directly by comparing the ordered complementary face bases of the relative chain complex. Here \(N=2n\). A permutation of the \(n\) antipodal **pairs** permutes blocks of size two and is even on the \(2n\) vertices, whereas exchanging signs within one pair is odd. Therefore \(\operatorname{sgn}_V=\eta\). Substituting \(i=2n-k-2\), and using torsion-freeness plus the integral universal coefficient theorem, gives \(\widetilde H^{k-1}(I_{n,k};\mathbb Z)\cong(\bigwedge^k U_n)^*\) and all displayed assertions about integral modules and vanishing.

**4. Character and integral distinction.** If \(\pi\in S_n\) has cycles \(c\), then \(\det(1+t\pi\mid E_n\otimes\mathbb Q)=\prod_c(1-(-t)^{|c|})\). Since \(E_n\otimes\mathbb Q\cong\mathbb Q\oplus(U_n\otimes\mathbb Q)\), dividing by \(1+t\), taking the coefficient of \(t^k\), and applying \(\eta\) proves the character formula.

For \(k=1\), the dual lattice is \(U_n^*\cong\mathbb Z^n/\mathbb Z(1,\ldots,1)\). Choose any prime \(p\mid n\), with \(n\ge3\). After reduction modulo \(p\), the vector \((1,\ldots,1)\) belongs to \(U_n\otimes\mathbb F_p\) and spans its one-dimensional \(S_n\)-fixed subspace. By contrast, if the class of \(v\in\mathbb F_p^n\) in \(U_n^*\otimes\mathbb F_p=\mathbb F_p^n/\mathbb F_p(1,\ldots,1)\) is fixed by a transposition \((ij)\), then \((v_i-v_j)(e_j-e_i)\) must be a multiple of the all-ones vector. For \(n\ge3\) the left side has a zero coordinate outside \(\{i,j\}\), forcing that multiple to be zero; hence \(v_i=v_j\). Varying \(i,j\) makes \(v\) constant, hence zero in the quotient. The dual lattice has no invariant vector in this characteristic. Their mod-\(p\) reductions therefore differ, proving the stated integral nonisomorphism. Rational self-duality of the standard representation gives their rational isomorphism. \(\square\)

## Verification

The independent, deterministic scripts `verification/verify_crosspoly.py` and `verification/check_lattices.py` use only the Python standard library. The first enumerates every signed simplex of \(\Theta_{n,k}\), computes the reduced signed Lefschetz character of every element of \(B_n\), and compares it with the formula for \((n,k)=(2,1),(3,1),(3,2),(4,1),(4,2),(4,3),(5,2)\). The second independently computes fixed-vector dimensions of the two integral lattices modulo a prime divisor of \(n\), for \(3\le n\le10\). See `verification/verification_output.txt`. These are finite consistency checks, not the proof of the all-parameter theorem; the proof is above.

## Relationship to prior work

Conant and Thistlethwaite computed the ordinary homotopy type of these exact theta complexes in their Theorem 7. Their sphere multiplicities and the nonequivariant homology ranks are **previously known**. The present statement refines that calculation by identifying the full integral \(B_n\)-module and an explicit root-versus-weight obstruction; it does not claim a new wedge decomposition. Björner and Tancer gave a general integral combinatorial Alexander duality proof; the signed group action and cross-polytope-specific lattice computation are made explicit here. Work on polyhedral joins provides broader nonequivariant methods but does not supply this particular integral group-module identification in the inspected material.

## Limitations

No \(B_n\)-equivariant wedge decomposition, Borel equivariant homology, or integral homotopy classification is claimed. The character alone would not certify the integral module; the integral proof uses the signed duality and the explicit augmentation lattice. Prior general machinery makes this result an accessible deduction, so an equivalent unstated or unindexed specialization remains an originality risk. Finite checks do not establish the infinite theorem without the written proof.

## References

1. J. Conant and O. Thistlethwaite, *Boolean formulae, hypergraphs and combinatorial topology*, arXiv:0808.0739 (first public version 2008-08-05), especially Sections 2, 5.3, 6, Theorem 7. https://arxiv.org/abs/0808.0739
2. A. Björner and M. Tancer, *Combinatorial Alexander Duality — A Short and Elementary Proof*, arXiv:0710.1172 (first public version 2007-10-05), especially Sections 2–4. https://arxiv.org/abs/0710.1172
3. A. Carnero Bravo, *Polyhedral joins and graph complexes*, arXiv:2307.14321 (first public version 2023-07-26), Sections 1–3 for broader polyhedral-join context. https://arxiv.org/abs/2307.14321
