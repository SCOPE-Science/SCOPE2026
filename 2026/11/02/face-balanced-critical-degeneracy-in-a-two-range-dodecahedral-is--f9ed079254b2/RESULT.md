# Face-balanced critical degeneracy in a two-range dodecahedral Ising antiferromagnet

## Finding

For the 20-spin dodecahedral Ising antiferromagnet with competing nearest- and second-neighbor interactions, the ground energy has exactly one positive-coupling transition. Let \(r=J_2/J_1\). Then
\[
\frac{E_0(r)}{J_1}=\begin{cases}
-18+12r,&0<r<1/2,\\
-12,&r=1/2,\\
-2-20r,&r>1/2.
\end{cases}
\]
At \(r=1/2\), the ground-state space comprises exactly \(9250\) configurations: those with exactly two or three positive spins on *each* of the twelve pentagonal faces. The whole ground-state magnetization census is:

| Coupling ratio | Magnetization \(M\) and number of states | Total states |
|---|---|---|
| \(0<r<1/2\) | \(M=\pm4:5\) each; \(M=0:240\) | \(250\) |
| \(r=1/2\) | \(M=\pm4:25\) each; \(M=\pm2:1800\) each; \(M=0:5600\) | \(9250\) |
| \(r>1/2\) | \(M=0:720\) | \(720\) |

With a weak uniform field coupled as \(-hM\), put \(\chi(T)=\left.\partial_h\langle M\rangle_{T,h}\right|_{h=0}\), with \(k_B=1\). The exact zero-temperature Curie coefficients are
\[
\lim_{T\downarrow0}T\chi(T)=\begin{cases}
16/25,&0<r<1/2,\\
304/185,&r=1/2,\\
0,&r>1/2.
\end{cases}
\]
Thus the competing interaction produces a sharp, large finite-size residual-entropy peak and an enhanced response at the transition, not just a change in a single minimizing spin pattern.

## Assumptions and scope

Define the dodecahedral graph explicitly as the generalized Petersen graph \(GP(10,2)\). Its vertices are \(a_i,b_i\) for \(i\in\mathbb Z/10\mathbb Z\), and its thirty edges are \(a_ia_{i+1}\), \(a_ib_i\), and \(b_ib_{i+2}\), with indices modulo ten. Put a classical Ising spin \(\sigma_v\in\{-1,+1\}\) on every vertex. Let \(E_1\) be the set of unordered nearest-neighbor edges and \(E_2\) the sixty unordered vertex pairs at graph distance exactly two. Define \(S_1=\sum_{\{u,v\}\in E_1}\sigma_u\sigma_v\), \(S_2=\sum_{\{u,v\}\in E_2}\sigma_u\sigma_v\), \(M=\sum_v\sigma_v\), and \(H=J_1S_1+J_2S_2-hM\), where \(J_1,J_2>0\). The energy and ground-state statements concern \(h=0\); the susceptibility concerns the derivative at \(h=0\) and \(T>0\) before the limit \(T\downarrow0\). No thermodynamic-limit transition is claimed for this finite graph.

## Proof

**Pentagonal-face lower bound.** There are precisely twelve pentagonal faces. Each of the thirty nearest-neighbor edges belongs to two faces, while each of the sixty graph-distance-two pairs lies in one face. For each face \(f\), write \(Q_f=\sum_{v\in f}\sigma_v\). Expanding the square gives
\[
S_1+\tfrac12 S_2=\tfrac14\sum_f(Q_f^2-5)=:C.
\]
Since every face has five spins, \(Q_f\) is odd, so \(Q_f^2\ge1\). Hence \(C\ge-12\), with equality precisely when \(Q_f=\pm1\) on every pentagon, equivalently exactly two or three positive spins per face.

**Independent lower bounds.** Each odd pentagon has at least one aligned nearest-neighbor edge, hence its sum of five spin products is at least \(-3\). Every nearest-neighbor edge is counted twice, so \(S_1\ge-18\). The three neighbors of each graph vertex make a triangle in the graph-distance-two interaction graph; the three products on this triangle sum to at least \(-1\). Every distance-two pair has a unique common neighbor, because the dodecahedral graph has no triangles or quadrilaterals. Therefore \(S_2\ge-20\). Equality holds in the latter bound exactly when the three neighbors of every vertex are not all of one sign.

**All positive coupling ratios.** For \(0<r<1/2\), write \(S_1+rS_2=(1-2r)S_1+2rC\). The preceding bounds yield \(S_1+rS_2\ge-18+12r\), with equality precisely when \(S_1=-18\) and \(C=-12\). For \(r>1/2\), write \(S_1+rS_2=C+(r-1/2)S_2\), giving \(S_1+rS_2\ge-2-20r\), with equality precisely when \(C=-12\) and \(S_2=-20\). At the critical value \(r=1/2\), the ground energy is \(C=-12\), with exactly the face-balance criterion above. Existence and every equality-case multiplicity are proved by the exhaustive *finite* integer enumeration described below; no limiting inference from numerical examples is used.

**Exact census and susceptibility.** The supplied checker generates all thirty edges and all sixty distinct distance-two pairs directly from \(GP(10,2)\), verifies the twelve faces and their incidences, and enumerates each integer mask \(0\le m<2^{20}\). One pass counts configurations meeting the analytic equality conditions and groups them by \(M\); another pass independently computes the exact pair energies and minimizes them at ratios \(1/4,1/2,1\). Both passes give the multiplicities stated in the Finding, and the analytical comparison above proves that these equality classes hold throughout their entire open parameter intervals. With the zero-field spin-flip symmetry, \(\langle M\rangle=0\), and the fluctuation identity gives \(T\chi(T)=\langle M^2\rangle\) when \(k_B=1\). In the zero-temperature limit, the Gibbs measure is uniform on the finite ground-state set. For the lower-coupling ground set \(\sum M^2=2\cdot5\cdot16=160\) across \(250\) states; at criticality it is \(2\cdot25\cdot16+2\cdot1800\cdot4=15200\) across \(9250\) states; and in the high-coupling phase it is zero. These yield \(16/25,304/185,0\), respectively.

## Verification

Execute `python3 verify_dodecahedron.py` with Python 3.8 or newer. The script depends only on Python's standard library; it checks all \(1,048,576\) possible spin configurations with exact integer arithmetic, reproducing the face and graph-pair incidences, all three magnetization tables, and exact reference energies. Its second energy calculation uses the direct nearest- and next-nearest-neighbor spin products rather than the face-balance test. The three sample ratios suffice to verify the exact enumerated equality-case sets because the analytical lower bounds already prove these sets remain optimal on the entire open intervals. The checker is a *finite exhaustive certificate* for this finite graph, not a proof about larger fullerenes.

## Relationship to prior work

Strečka, Karľová and Madaras (2015) studied magnetization and magnetocaloric effects for regular Ising polyhedra with *nearest-neighbor exchange only*. Their dodecahedral zero-field results imply the \(r\downarrow0\) ground-state energy \(-18J_1\) and its \(250\)-state degeneracy, which are not claimed as new. The present result concerns the competing second-neighbor exchange, its exactly face-balanced \(9250\)-state degeneracy, the complete coupling-dependent ground-state classification, and the exact zero-field Curie coefficients. Stephenson and Betts (1970) studied antiferromagnetic next-nearest-neighbor exchange on multiple lattice types; the accessible abstract establishes broad prior work on competing interactions and critical coupling ratios, but does not establish an exact dodecahedral census. An equivalent specific finite-graph classification in another source remains possible; this has not been independently audited.

## Limitations

The statement assumes \(20\) classical Ising spins on the undistorted dodecahedral graph, homogeneous positive exchanges on all and only graph-distance-one and graph-distance-two pairs, zero applied field for the ground-state classification, and no quantum fluctuations. It does not claim a bulk thermodynamic phase transition, experimentally measured material properties, higher-neighbor couplings, or results for general fullerene families. The counting claim is finite and exhaustive, but historical-priority verification remains provisional.

## References

1. J. Strečka, K. Karľová and T. Madaras, *Giant magnetocaloric effect, magnetization plateaux and jumps of the regular Ising polyhedra*, arXiv:1502.04449, first public 16 February 2015. https://arxiv.org/abs/1502.04449
2. J. Stephenson and D. D. Betts, *Ising Model with Antiferromagnetic Next-Nearest-Neighbor Coupling. II. Ground States and Phase Diagrams*, *Physical Review B* **2**, 2702 (1970). https://doi.org/10.1103/PhysRevB.2.2702
