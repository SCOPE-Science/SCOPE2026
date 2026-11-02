# Dihedral and color-permutation homology of \(\operatorname{Ind}(C_8\times K_3)\)

## Finding

For the categorical graph product \(G=C_8\times K_3\), put \(X=\operatorname{Ind}(G)\). Let \(D_8=\langle r,s\mid r^8=s^2=1,\ srs=r^{-1}\rangle\) act by rotation and reflection of the cycle coordinate; let \(S_3\) permute the three colors. Write \(\operatorname{sgn}\) for the sign representation of \(S_3\) and \(U\) for its standard two-dimensional rational representation. Define two one-dimensional \(D_8\)-representations by
\[
\eta(r)=-1,\quad\eta(s)=-1,\qquad \rho(r)=-1,\quad\rho(s)=1.
\]
Then, as representations of the natural \(D_8\times S_3\)-action,
\[
\widetilde H_4(X;\mathbb Q)\cong \eta\boxtimes\operatorname{sgn},
\qquad
\widetilde H_5(X;\mathbb Q)\cong\rho\boxtimes(\operatorname{sgn}\oplus U),
\]
and all other reduced rational homology vanishes. The integral homotopy type is
\[
X\simeq S^4\vee\bigvee^3 S^5.
\]
The quotient by the full \(D_8\times S_3\) action is rationally acyclic. In contrast, the quotient by the order-three subgroup of color permutations has one reduced rational generator in each of dimensions four and five. The representations, rather than the already reported two-degree free homology, are the main new claim.

## Assumptions and scope

Vertices of \(G\) are \((i,a)\) with \(i\in\mathbb Z/8\mathbb Z\) and \(a\in\{0,1,2\}\). Two distinct vertices are joined exactly if their cycle positions differ by \(\pm1\) modulo eight and their colors differ. \(X\) has all nonempty independent vertex sets as simplices. We use integer oriented simplicial chains with increasing vertex label \(3i+a\). The action is \(r(i,a)=(i+1,a)\), \(s(i,a)=(-i,a)\), and \(\sigma(i,a)=(i,\sigma(a))\) for \(\sigma\in S_3\). The claimed representation is rational; integral homology ranks are also calculated, but no integral module classification is claimed. All the conclusions are for this specific 24-vertex graph, not every categorical cycle product.

## Proof

**1. Exact integral Morse model.** Enumerate independent sets by scanning the 24 vertices in increasing label order. Starting from all nonempty faces, at stage \(v\), pair every presently unmatched face \(F\) not containing \(v\) with \(F\cup\{v\}\), provided both are present. Remove both. The supplied Python verifier constructs all 18,721 nonempty faces and 9,353 pairs, leaves one critical vertex, six critical four-simplices, and eight critical five-simplices, and verifies acyclicity: reverse precisely the matched arrows of the entire Hasse diagram, direct every other cover downward, and topologically sort the resulting 18,721 vertices. All are removed, so the matching is acyclic, not merely heuristically selected.

Ordering the remaining four-cells and five-cells by their bitmask labels, the exact integral Morse boundary from degree five to degree four is
\[
B=\begin{pmatrix}
0&-1&0&0&0&-1&0&0\\
0&0&-1&0&0&0&-1&0\\
0&-1&0&-1&0&0&0&0\\
0&0&-1&-1&0&0&0&0\\
0&0&0&0&-1&0&-1&0\\
0&0&0&0&-1&-1&0&0
\end{pmatrix}.
\]
The primitive row relation \((-1,1,1,-1,-1,1)B=0\) gives rank at most five. The minor with rows \(0,1,2,3,4\) and columns \(1,2,3,4,5\) has determinant one, so the rank is five and all five nonzero Smith factors are units. There are no Morse cells in dimensions one through three. Hence \(\widetilde H_4(X;\mathbb Z)=\mathbb Z\), \(\widetilde H_5(X;\mathbb Z)=\mathbb Z^3\), with no torsion or other reduced homology. The Morse CW complex has one zero-cell, six four-cells and eight five-cells. Its five-cell attaching maps into a wedge of four-spheres are classified by their integer degree vectors; diagonalizing the displayed attaching matrix with unit Smith factors cancels five pairs, leaving the stated wedge \(S^4\vee\bigvee^3S^5\). This step uses the fact that \(\pi_4(\bigvee^6 S^4)\cong\mathbb Z^6\), not an unjustified inference from Betti numbers.

**2. Orientation character in degree four.** The row vector \(\phi=(-1,1,1,-1,-1,1)\), evaluated on the Morse projection of an original four-chain, is an integral cocycle; the verifier checks it vanishes on the boundaries of **every** original five-simplex. One critical four-simplex is lifted by gradient cancellation to an explicit integral four-cycle supported on 66 four-simplices; its pairing with \(\phi\) is \(-1\), proving it represents a primitive generator of fourth homology. Apply each group generator to its oriented simplices, project back along the matching, and divide by this original pairing. The resulting eigenvalues are \(-1\) for \(r\), \(-1\) for \(s\), \(-1\) for a color transposition, and \(+1\) for a color three-cycle. The same identity is checked for all 96 group elements. Hence the degree-four module is \(\eta\boxtimes\operatorname{sgn}\).

**3. Lefschetz traces and the degree-five character.** For \(g\in D_8\times S_3\), compute its signed fixed-simplex trace
\[
L(g)=\sum_{\varnothing\ne F\in X,\,gF=F}(-1)^{|F|-1}\operatorname{sgn}(g|_F).
\]
For \(g=(r^a s^b,\sigma)\), exhaustive exact face enumeration (all 96 elements) gives
\[
L(g)-1=(-1)^a\bigl[((-1)^b-1)\operatorname{sgn}(\sigma)-(\operatorname{fix}(\sigma)-1)\bigr].
\]
By reduced Lefschetz, \(L(g)-1=\chi_4(g)-\chi_5(g)\); therefore
\[
\chi_5(r^a s^b,\sigma)=(-1)^a\bigl(\operatorname{sgn}(\sigma)+\operatorname{fix}(\sigma)-1\bigr).
\]
The last parenthesis is exactly the character of \(\operatorname{sgn}\oplus U\) for \(S_3\). The \(D_8\) factor is \(\rho\), completing the representation claim.

**4. Quotients.** For a finite group acting on a finite complex, rational homology of the quotient is the invariant subspace (use barycentric subdivision and averaging). Neither \(\eta\) nor \(\rho\) is trivial on the eight-cycle rotations, so no positive-degree class survives the full quotient. The color three-cycle fixes the sign line and fixes no vector in \(U\), yielding one invariant in each degree four and five.

## Verification

Run `python3 verify_c8k3.py` with Python 3.10+; the checker uses only the standard library and constructs all graphs, faces, oriented boundaries, matchings and group actions from the definitions above. It tests whole-Hasse acyclicity rather than just local matching rules, reconstructs the exact Morse boundary, checks an explicit unit minor and left null relation, constructs and verifies a closed integral 66-simplex cycle, tests its cohomological pairing, verifies the cocycle against all five-boundaries, and checks all 96 exact fixed-face Lefschetz traces and fourth-homology actions. Success prints `C8_K3_INTEGRAL_MORSE_AND_96_ACTIONS_OK` and the numerical certificates. There is no random sampling or finite-to-infinite extrapolation.

## Relationship to prior work

Antolín Camarena and Carnero Bravo (arXiv:2307.12401, first posted July 23, 2023) proved a two-consecutive-degree homotopy restriction for categorical products \(C_m\times K_n\) when \(m\not\equiv0\pmod3\), allowing possible Moore summands. Their section 3 explicitly lists \(C_8\times K_3\) among cases with free homology determined computationally. Their nonequivariant framework and the existence of free homology in this example are prior art; the present claim is the complete dihedral **and** color-permutation character, a primitive integral orientation-line witness, and the resulting quotient comparison. Their text does not state these actions.

Carnero Bravo's later arXiv:2505.06457 investigates categorical products involving paths, not the cyclic product and its joint \(D_8\times S_3\) action. Goyal, Shukla and Singh's 2021 paper treats generalized Mycielskians of complete graphs and categorical products of complete graphs, not this cyclic example. Related indexed calculations for \(\operatorname{Ind}(C_7\times K_4)\) or generalized Mycielskians likewise do not logically imply the exact module just computed. The novelty comparison is bounded to the inspected documents and actual database and web searches; absence of indexed duplication is not a proof of uniqueness.

## Limitations

This is one natural finite case, not a uniform classification of \(\operatorname{Ind}(C_m\times K_n)\). The exact non-equivariant homology context is already discussed in the 2023 source; do not treat those ranks alone as the principal novel contribution. No homotopy description of the nonfree group quotients, integral torsion analysis of quotients, or full automorphism-group classification is claimed. Possible unindexed or implicit equivariant computations remain a bibliographic risk. Independent external validation has not been performed.

## References

1. O. Antolín Camarena and A. Carnero Bravo, *Homotopy type of the independence complex of some categorical products of graphs*, arXiv:2307.12401, v1 July 23, 2023; v2 September 1, 2023; published in *Homology, Homotopy and Applications* 26(2) (2024), DOI:10.4310/HHA.2024.v26.n2.a17.
2. A. Carnero Bravo, *On independence complexes of graph products*, arXiv:2505.06457, v2 November 11, 2025.
3. S. Goyal, S. Shukla and A. Singh, *Homotopy Type of Independence Complexes of Certain Families of Graphs*, *Contributions to Discrete Mathematics* 16(3) (2021), DOI:10.55016/ojs/cdm.v16i3.71284.

