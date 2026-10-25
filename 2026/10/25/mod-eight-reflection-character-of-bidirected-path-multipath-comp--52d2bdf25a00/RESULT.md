# Mod-eight reflection character of bidirected-path multipath complexes

## Finding
For every integer \(n\geq1\), let \(B_n\) be the digraph on \(\{0,1,\ldots,n\}\) containing both arcs between successive vertices, let \(X_n\) be its multipath simplicial complex, and let \(\rho(i)=n-i\) be reversal. Put \(d=\lfloor(n-1)/2\rfloor\). The known nonequivariant homotopy equivalence \(X_n\simeq S^d\) gives \(\widetilde H_d(X_n;\mathbb Z)\cong\mathbb Z\) and no other reduced homology. The induced integral action is exactly
\[
\rho_* = \epsilon_n\operatorname{id},\qquad
\epsilon_n=\begin{cases}
-1,&n\equiv1,2,3,4\pmod{8},\\
+1,&n\equiv0,5,6,7\pmod{8}.
\end{cases}
\]
In particular, with the quotient formed by the geometric reversal action,
\[
\widetilde H_i\bigl(|X_n|/\langle\rho\rangle;\mathbb Q\bigr)
\cong\begin{cases}
\mathbb Q,&i=d\text{ and }n\equiv0,5,6,7\pmod{8},\\
0,&\text{otherwise}.
\end{cases}
\]
The new conclusion is the reflection action (not the previously determined sphere homotopy type). The quotient formula is a consequence of the reflection character.

## Assumptions and scope
A multipath is a spanning subgraph whose connected components are isolated vertices or directed simple paths, without directed cycles. A simplex of \(X_n\) is the set of its selected directed arcs. An arc on edge \(\{i,i+1\}\) is encoded by \(+\) for \(i\to i+1\), by \(-\) for \(i+1\to i\), or by \(0\) for absence. Thus faces correspond exactly to words \(w\in\{0,+,-\}^n\) in which adjacent nonzero signs agree. Opposing arcs on one edge would form a directed two-cycle; adjacent opposing signs would give indegree or outdegree two; and no other forbidden configurations can occur on a path. The empty word means the empty simplex. Reversal sends \(w_i\) to the opposite sign of \(w_{n-1-i}\). The integer \(n\) counts undirected path edges, rather than vertices.

## Proof
The established homotopy equivalence \(X_n\simeq S^{\lfloor(n-1)/2\rfloor}\) is Proposition 2.2 of Caputi–Collari–Smith (arXiv:2601.05670, first posted 2026-01-09). Its proof uses the suspension recurrence \(X_n\simeq\Sigma X_{n-2}\), with \(X_1\simeq X_2\simeq S^0\). We apply that known result only to identify the degree and rank of the unique nonzero reduced integral homology group.

Set \(m=\lfloor(n-1)/2\rfloor\). A word fixed under reversal satisfies \(w_i=-w_{n-1-i}\). If \(n\) is odd, its central letter must be zero. If \(n\) is even, its two central letters are opposite; because adjacent nonzero opposite signs are forbidden, both must be zero. All remaining letters are uniquely determined by a valid word of length \(m\) on the left, reflected with signs reversed to the right. This gives an exact bijection of fixed simplices (including the empty one) with faces of \(X_m\).

Every fixed nonempty simplex uses \(2p\) arcs in \(p\) disjoint reversal pairs. On its oriented simplicial chain generator, reversal has permutation sign \((-1)^p\). Its contribution to the reduced simplicial Lefschetz number is therefore \((-1)^{2p-1}(-1)^p=-(-1)^p\). Including the augmented empty simplex, whose degree is \(-1\), yields
\[
\widetilde L(\rho\mid X_n)
=-\sum_{F\in X_m}(-1)^{|F|}
=\widetilde\chi(X_m).
\]
For \(m\geq1\), the established sphere equivalence gives \(\widetilde\chi(X_m)=(-1)^{\lfloor(m-1)/2\rfloor}\); for \(m=0\), the augmented complex \(X_0=\{\varnothing\}\) has \(\widetilde\chi(X_0)=-1\), so the same expression holds using the integer exponent \(\lfloor-1/2\rfloor=-1\).

By the reduced Hopf trace theorem, \(\widetilde L(\rho\mid X_n)=(-1)^m\epsilon_n\), since the unique reduced homology group is a free rank-one group in degree \(m\). Therefore
\[
\epsilon_n=(-1)^{m+\lfloor(m-1)/2\rfloor}.
\]
The exponent is odd for \(m\equiv0,1\pmod{4}\) and even for \(m\equiv2,3\pmod{4}\). Because \(n\) is either \(2m+1\) or \(2m+2\), this is exactly the claimed eight-residue sign rule, including \(n=1,2\).

For the quotient, barycentrically subdivide the finite simplicial complex, making the reversal action simplicial without inversions. Over \(\mathbb Q\), averaging by the order-two group identifies the homology of the orbit complex with the invariant part of the original rational homology. Thus a one-dimensional invariant summand survives exactly when \(\epsilon_n=+1\), and all other reduced quotient groups vanish.

## Verification
Execute the embedded standard-library-only script `check.py` with Python 3. It independently enumerates admissible signed words for \(1\leq n\leq12\), computes their reversal-fixed chain supertraces, checks the fixed-face bijection with \(X_m\), and compares with the formula above. For \(1\leq n\leq9\), it also computes augmented binary simplicial boundary ranks and confirms one reduced mod-two Betti number in degree \(\lfloor(n-1)/2\rfloor\). The expected final line is `REFLECTION_CHARACTERS_OK`. These finite checks are not an infinite proof or a substitute for the established sphere theorem and the chain-level Lefschetz argument.

## Relationship to prior work
Caputi–Collari–Di Trani–Smith (arXiv:2208.04656, initially public 2022-08-09) introduce homotopy computations for multipath complexes, but do not determine this path-reversal character. Caputi–Collari–Smith (arXiv:2601.05670) prove the nonequivariant sphere classification of the exact bidirected-path complexes used here. Their displayed join model for odd path length provides a route to the odd-length sign, and that pre-existing structure is acknowledged. It is not an equivariant classification of the even-length paths or their orbit homology; those conclusions require the fixed-face Lefschetz comparison above.

The later bidirectional-polygon dihedral-homology computation concerns closed cycles with different face sets and homology. The strong discrete Morse path-matching complex of Knudson–Owens-White (arXiv:2609.06844) is another construction, not interchangeable with \(X_n\): for instance its two-edge path complex is contractible, whereas \(X_2\simeq S^0\). Similar periodic signs do not imply identity of complexes or actions.

## Limitations
This classifies the integral automorphism on the unique homology group and the **rational** homology of the orbit space, not the full integral orbit-space homology, equivariant stable homotopy type, or reflection-fixed-point homotopy type. The nonequivariant sphere classification is cited from prior work, not newly established here. Targeted bibliographic and published-record searches did not reveal this complete path-reversal theorem; unidentified equivalent work remains possible.

## References
- L. Caputi, C. Collari, S. Di Trani, J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656, first posted 2022-08-09; Mathematika 70 (2024), e12235. https://arxiv.org/abs/2208.04656
- L. Caputi, C. Collari, J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670, first posted 2026-01-09, especially Proposition 2.2 and its explicit joins. https://arxiv.org/html/2601.05670v1
- K. Knudson, A. Owens-White, *Complexes of strong discrete Morse matchings*, arXiv:2609.06844, first posted 2026-09-06, especially Sections 6 and 10 (a different complex). https://arxiv.org/abs/2609.06844
