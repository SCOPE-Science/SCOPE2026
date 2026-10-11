# Integral branch-permutation homology of extended-star Morse complexes

## Finding
Let \(n\ge2\) be an integer, let \(T_n\) have vertices \(c,a_1,b_1,\ldots,a_n,b_n\), and edges \(ca_i,a_ib_i\) for \(1\le i\le n\). Its automorphism group contains \(S_n\), acting by simultaneous permutation of its two-edge arms. Let \(K_n=\mathcal M(T_n)\) be the **ordinary** simplicial complex of acyclic discrete vector fields on this tree. Then, as integral \(\mathbb Z[S_n]\)-modules,
\[
\widetilde H_j(K_n;\mathbb Z)\cong
\begin{cases}
\operatorname{sgn}\otimes\ker\bigl(\mathbb Z^n\xrightarrow{\sum}\mathbb Z\bigr),&j=n,\\
0,&j\ne n.
\end{cases}
\]
The symmetric group acts on \(\mathbb Z^n\) by permuting standard basis vectors, and \(\operatorname{sgn}\) denotes its rank-one sign lattice. Consequently its rational top-homology character is
\[
\chi_n(\sigma)=\operatorname{sgn}(\sigma)\bigl(f(\sigma)-1\bigr),
\]
where \(f(\sigma)\) is the number of fixed points of \(\sigma\) on the set of arms. Over \(\mathbb Q\), the top representation is the irreducible Specht module \(S^{(2,1^{n-2})}\). It has no \(S_n\)-invariant vector for \(n\ge3\). For \(n=2\), the sole top-homology generator is fixed by the arm interchange.

## Assumptions and scope
A primitive gradient vector-field element on a graph is an incidence \((v,e)\) of a vertex and an incident edge. A collection of such elements is a simplex when each vertex and each edge occurs in at most one incidence and the associated discrete vector field has no closed gradient path. Since \(T_n\) is a tree, every such matching is acyclic: a nontrivial closed gradient path would project to a cycle in the tree. All homology groups in the theorem are **reduced** with integral coefficients; all statements hold for every integer \(n\ge2\). The external prior theorem giving \(K_n\simeq\bigvee^{n-1}S^n\) is not asserted as new and is not needed for the integral representation proof.

## Proof
For each arm \(i\), abbreviate the four incidences by
\[
x_i=(c,ca_i),\quad y_i=(a_i,ca_i),\quad
z_i=(a_i,a_ib_i),\quad w_i=(b_i,a_ib_i).
\]
Within the set of incidences, the incompatible pairs are precisely \(\{x_i,x_j\}\) for distinct arms, together with \(\{x_i,y_i\},\{y_i,z_i\},\{z_i,w_i\}\) in each arm. This follows directly from sharing a vertex or edge of the Hasse incidence graph.

Let \(A_i\) be the induced subcomplex on \(\{y_i,z_i,w_i\}\). It is the disjoint union of the edge \(\{y_i,w_i\}\) and the isolated vertex \(z_i\), hence \(A_i\simeq S^0\). Removing all \(x_i\) yields
\[
B=A_1*A_2*\cdots*A_n\simeq S^{n-1}.
\]
The integral join-Künneth theorem gives \(\widetilde H_{n-1}(B;\mathbb Z)\cong\mathbb Z\) and vanishing in all other degrees. Choose its generator as the ordered join of the reduced degree-zero classes \([z_i]-[w_i]\). Swapping two degree-zero factors in the join changes orientation by \((-1)^{(0+1)(0+1)}=-1\), so an arm permutation \(\sigma\) acts on \(\widetilde H_{n-1}(B;\mathbb Z)\) by \(\operatorname{sgn}(\sigma)\).

For a fixed arm \(i\), the link of \(x_i\) in \(B\) is
\[
L_i=\{z_i,w_i\}*\bigast_{j\ne i}A_j,
\]
where \(\{z_i,w_i\}\) means the two-point discrete complex, **not** an edge. The inclusion of this two-point complex into \(A_i\) maps one vertex into each contractible component, hence is a homotopy equivalence. The inclusion \(L_i\hookrightarrow B\) is therefore a homotopy equivalence, and induces an isomorphism in reduced integral homology.

Because two distinct \(x_i\) cannot lie in a common face, \(K_n=B\cup\bigcup_i(x_i*L_i)\), and all intersections of the added cones lie in \(B\). Thus the relative quotient is the wedge of the cone quotients, \(K_n/B\cong\bigvee_i\Sigma L_i\), and
\[
\widetilde H_n(K_n,B;\mathbb Z)\cong\bigoplus_{i=1}^n\widetilde H_{n-1}(L_i;\mathbb Z)\cong\mathbb Z^n.
\]
All other relative reduced homology groups vanish. Identify the generator in the \(i\)-th summand with the unique generator that maps to the chosen generator of \(\widetilde H_{n-1}(B;\mathbb Z)\). The connecting homomorphism in the long exact sequence of the pair is then the augmentation \(\sum:\mathbb Z^n\to\mathbb Z\), which is surjective. Exactness proves that the only surviving reduced homology is its kernel in degree \(n\); in particular there is no torsion.

The identifications of the relative summands with the chosen orientation of \(B\) are natural under the arm permutations up to the common sign already computed for \(B\). Consequently \(\sigma\) acts on the relative group as the sign-twisted coordinate permutation. Its equivariant connecting map is the sign-twisted augmentation. Its kernel is the claimed integral module \(\operatorname{sgn}\otimes\ker(\sum)\).

Over characteristic zero, the augmentation kernel is the standard irreducible \(S^{(n-1,1)}\); tensoring by sign conjugates the partition, giving \(S^{(2,1^{n-2})}\). The trace of the coordinate permutation is \(f(\sigma)\) and that of its augmentation kernel is \(f(\sigma)-1\), proving the stated character. The irreducibility and nontriviality for \(n\ge3\) imply vanishing invariants. For \(n=2\), the sign tensor of the one-dimensional standard sign representation is trivial.

## Verification
The independent standard-library Python script `verify_morse_star.py` constructs the full Hasse incidence graph of the tree and enumerates its matching faces, without using the proof's join-and-cone decomposition. For each \(2\le n\le5\) and every one of the \(\sum_{n=2}^{5}n!=152\) arm permutations, it calculates the reduced signed Lefschetz trace by enumerating invariant faces and compares its degree-adjusted value with \(\operatorname{sgn}(\sigma)(f(\sigma)-1)\). It also computes all augmented boundary ranks over \(\mathbb F_2\) for \(n=2,3,4\), checking the predicted Betti numbers in every degree. These are finite consistency checks; the integral and all-parameter assertions follow from the preceding exact sequence, not the enumeration. Run `python3 verify_morse_star.py`; the expected success marker is `VERIFY_OK`.

## Relationship to prior work
Donovan and Scoville, *Star clusters in the Matching, Morse, and Generalized Morse complex*, first public July 27, 2022, Theorem 15 and Corollary 17, proved the **nonequivariant** homotopy equivalence \(\mathcal M(T_n)\simeq\bigvee^{n-1}S^n\). The existing rank \(n-1\), even together with the branch symmetry group, does not determine the induced integral group-ring module or its character. The present finding is the action of that symmetry group on the already-known top homology, obtained from a natural equivariant relative-chain exact sequence. The prior sphere-wedge equivalence is not claimed as new.

## Limitations
The result concerns these two-edge-arm trees and their natural arm-permutation subgroup only; it does not determine arbitrary automorphism actions for unrelated trees or complexes with longer unequal arms. The abstract homotopy equivalence is not asserted to be equivariant. The script checks only bounded finite cases and does not certify the all-parameter proof. No independent external audit has been performed.

## References
1. C. Donovan and N. A. Scoville, *Star clusters in the Matching, Morse, and Generalized Morse complex*, arXiv:2207.13780v1, July 27, 2022, Theorem 15 and Corollary 17. https://arxiv.org/html/2207.13780v1
2. C. Donovan and N. A. Scoville, *Star clusters in the matching, Morse, and generalized complex of discrete Morse functions*, New York Journal of Mathematics 29 (2023), 1393–1412. https://www.maths.tcd.ie/EMIS/journals/NYJM/NYJM/j/2023/29-54.html
