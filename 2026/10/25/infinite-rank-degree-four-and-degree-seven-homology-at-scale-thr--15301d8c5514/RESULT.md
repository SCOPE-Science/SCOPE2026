# Infinite-rank degree-four and degree-seven homology at scale three on integer lattices

## Finding

For every integer \(n\ge5\), equip \(\mathbb Z^n\) with the Manhattan metric \(d_1(x,y)=\sum_{i=1}^n|x_i-y_i|\), and let \(K_n=\operatorname{VR}_{\le3}(\mathbb Z^n,d_1)\) be the simplicial complex whose finite simplices have diameter at most \(3\). Then

\[
\operatorname{rank}\widetilde H_4(K_n;\mathbb Z)=\operatorname{rank}\widetilde H_7(K_n;\mathbb Z)=\aleph_0.
\]

More precisely, for each \(d\in\{4,7\}\), the group \(\widetilde H_d(K_n;\mathbb Z)\) contains a split direct summand \(\bigoplus_{k\ge0}\mathbb Z^{b_d(n)}\), where

\[
b_4(n)=\sum_{i=4}^{n-1}2^{i-4}\binom{i}{4},\qquad b_7(n)=2^{n-4}\binom{n}{4}.
\]

## Assumptions and scope

The scale convention is inclusive: a finite set is a simplex when every pair of its vertices is at Manhattan distance at most \(3\). Homology is reduced simplicial homology with integer coefficients. The theorem is asserted for all integers \(n\ge5\). It does not claim that these homology groups are torsion-free, that other reduced homology groups vanish, or that \(K_n\) is a wedge of spheres.

## Proof

Let \(Q_n=\{0,1\}^n\subset\mathbb Z^n\). Its induced subcomplex \(L_n=\operatorname{VR}_{\le3}(Q_n,d_1)\) is isometric to the scale-three Vietoris–Rips complex of the binary hypercube graph. Feng's homotopy classification gives, for \(n\ge5\),

\[
L_n\simeq\bigvee^{b_7(n)}S^7\;\vee\;\bigvee^{b_4(n)}S^4.
\]

For each integer \(k\ge0\), translate this cube to \(C_k=\{3k,3k+1\}^n\), and write \(L_{n,k}=\operatorname{VR}_{\le3}(C_k,d_1)\). Translation identifies every \(L_{n,k}\) with \(L_n\).

Define \(c_k:\mathbb Z^n\to C_k\) coordinatewise by clamping each coordinate to the interval \([3k,3k+1]\cap\mathbb Z\):

\[
(c_k(x))_i=\min(3k+1,\max(3k,x_i)).
\]

Each coordinate clamp is \(1\)-Lipschitz on \(\mathbb Z\), so \(c_k\) is \(1\)-Lipschitz for \(d_1\). It therefore induces a simplicial map \(r_k:K_n\to L_{n,k}\). This map fixes \(C_k\), hence is a retraction on \(L_{n,k}\). If \(j<k\), every coordinate of every vertex in \(C_j\) is at most \(3k-2\), so \(c_k\) sends all of \(C_j\) to the same lower corner of \(C_k\). If \(j>k\), every coordinate of every vertex in \(C_j\) is at least \(3k+3\), so \(c_k\) sends all of \(C_j\) to the same upper corner. Consequently, for every positive degree \(d\), the induced map \((r_k)_*\) is the identity on \(\widetilde H_d(L_{n,k};\mathbb Z)\) and is zero on \(\widetilde H_d(L_{n,j};\mathbb Z)\) whenever \(j\ne k\).

Consider the homomorphism induced by inclusions,

\[
\Psi_d:\bigoplus_{k\ge0}\widetilde H_d(L_{n,k};\mathbb Z)\longrightarrow\widetilde H_d(K_n;\mathbb Z).
\]

The coordinate retractions define a map in the reverse direction by \(\Phi_d([z])=((r_k)_*[z])_{k\ge0}\). This tuple has finite support: a simplicial cycle is a finite chain, and for all sufficiently large \(k\), every vertex appearing in that chain lies below every coordinate interval \([3k,3k+1]\), so \(r_k\) maps the whole chain to a single vertex and its positive-dimensional reduced homology class to zero. Thus \(\Phi_d\) is well-defined with target the direct sum. The diagonal and off-diagonal retraction properties above give \(\Phi_d\Psi_d=\mathrm{id}\). Hence \(\Psi_d\) is split injective, and its image is a direct summand isomorphic to \(\bigoplus_{k\ge0}\mathbb Z^{b_d(n)}\) for \(d=4,7\).

Finally, \(K_n\) has countably many vertices and therefore countably many finite simplices. Its simplicial chain groups, and hence its homology groups, are countable. The split free summands prove that the ranks in degrees \(4\) and \(7\) are infinite; countability makes each rank exactly \(\aleph_0\). This completes the proof.

## Verification

The cited hypercube theorem supplies the two sphere multiplicities for every \(n\ge5\); both are positive in this range. The retraction argument is uniform in \(n\) and uses only the coordinatewise \(1\)-Lipschitz property of clamping. The finite-chain argument is needed to show that the family of retractions lands in a direct sum rather than a direct product. For the boundary check \(n=5\), the formula gives \(b_4(5)=1\) and \(b_7(5)=10\); each separated translated cube therefore contributes a nonzero free summand in both degrees. No finite enumeration is used as a substitute for the uniform proof.

## Relationship to prior work

Gupta, Sarkar, and Shukla established the scale-two homotopy type of \(\operatorname{VR}(\mathbb Z^n;2)\), proved simple connectivity at scales at least \(2\), and asked whether the scale-three complex is homotopy equivalent to a countable wedge of \(4\)- and \(7\)-spheres (Question 5.2). They also record that the inclusion of the binary cube into the integer lattice induces an injection on homology. Feng proved the exact scale-three homotopy type of the binary hypercube, with the multiplicities used above. The present claim adds a split family of infinitely many independent copies, using translated cubes and explicit retractions. It proves the predicted infinite ranks in the two degrees but not the proposed full wedge decomposition.

## Limitations

No assertion is made about torsion in \(\widetilde H_4\) or \(\widetilde H_7\), vanishing of homology in other degrees, higher homotopy groups, or the integral homotopy type of \(K_n\). In particular, countably infinite rank in these two degrees is necessary for the cited wedge conjecture but is not sufficient to prove it. The result uses the published scale-three hypercube classification as an input.

## References

1. R. K. Gupta, S. Sarkar, and S. Shukla, “On the Vietoris-Rips Complexes of Integer Lattices,” arXiv:2511.04238v1 (first public version: 6 November 2025), especially the introduction and Question 5.2.
2. Z. Feng, “Homotopy types of Vietoris-Rips complexes of Hypercube Graphs,” arXiv:2305.07084v1 (11 May 2023), scale-three classification for \(n\ge5\).
