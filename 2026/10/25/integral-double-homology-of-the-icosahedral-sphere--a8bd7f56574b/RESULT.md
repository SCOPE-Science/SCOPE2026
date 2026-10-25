# Integral double homology of the icosahedral sphere

## Finding

Let \(K\) be the boundary complex of the icosahedron and \(Z_K\) its moment-angle complex. Over \(\mathbb Z\), its bigraded double homology is torsion-free and is \(\mathbb Z\) in bidegrees \((0,0),(-1,4),(-8,20),(-9,24)\), \(\mathbb Z^{10}\) in bidegrees \((-4,10),(-5,14)\), and zero elsewhere. The total rank is \(24\).

## Assumptions and scope

The complex \(K\) is the simplicial boundary of a regular icosahedron. It has \(12\) vertices, \(30\) edges, and \(20\) triangular faces. The moment-angle complex \(Z_K\) is formed from this finite simplicial complex. All homology groups and all inclusion-induced maps in the computation use integer coefficients.

For every vertex subset \(J\subseteq V(K)\), write \(K_J\) for the full subcomplex on \(J\). The claim concerns only the integral double homology of this one \(K\); it does not classify other sphere triangulations or determine any symmetry representation.

## Proof

For each \(q\) and each \(0\leq \ell\leq12\), form
\[
C^\ell_q=\bigoplus_{\substack{J\subseteq V(K)\\|J|=\ell}}\widetilde H_q(K_J;\mathbb Z).
\]
The differential \(\delta_\ell:C^\ell_q\to C^{\ell+1}_q\) is the alternating sum of the maps induced by \(K_J\hookrightarrow K_{J\cup\{x\}}\), with sign \((-1)^{|\{y\in J:y<x\}|}\) for \(x\notin J\), using the vertex order in the verification script. This is the standard subset-poset model of double homology. In the usual bigrading,
\[
HH_{q+1-\ell,\,2\ell}(Z_K;\mathbb Z)=H^\ell(C^\bullet_q).
\]

The computation enumerates all \(2^{12}=4096\) subsets. Each \(K_J\) is a subcomplex of a triangulated \(2\)-sphere. Thus \(\widetilde H_0(K_J;\mathbb Z)\) and \(\widetilde H_1(K_J;\mathbb Z)\) are free abelian, while \(\widetilde H_2(K_J;\mathbb Z)\) is \(\mathbb Z\) only when \(J=V(K)\) and is zero for every proper subcomplex. The freeness of \(\widetilde H_1\) also follows from Alexander duality: its rank is determined by the finite set of components of the complement in \(S^2\).

For each subset with nonzero reduced \(H_0\) or \(H_1\), exact Smith normal decompositions give integral cycle bases and quotient bases. The boundary-coordinate matrices have only unit nonzero invariant factors. These bases determine the integer matrices of all \(6504\) nonzero-dimension inclusion maps used by the computation. The two endpoint groups are \(\mathbb Z\) from \(\widetilde H_{-1}(K_\varnothing;\mathbb Z)\) at \(\ell=0\), and \(\mathbb Z\) from \(\widetilde H_2(K;\mathbb Z)\) at \(\ell=12\).

The script verifies \(\delta_{\ell+1}\delta_\ell=0\) exactly. For each of the \(26\) differentials in reduced homology degrees \(q=0,1\), integer row/column elimination using only pivots \(+1\) or \(-1\) exhausts the matrix and leaves an all-zero residual. Consequently every nonzero Smith factor of every differential is \(1\). Each differential image is therefore a primitive sublattice, so the resulting cohomology groups have no torsion.

The nontrivial chain dimensions and differential ranks are:

| Reduced degree \(q\) | Subset size \(\ell\) | \(\dim C^\ell_q\) | \(\operatorname{rank}\delta_\ell\) |
|---:|---:|---:|---:|
| \(0\) | \(2,3,4,5,6,7\) | \(36,160,315,300,112,12\) | \(35,125,190,100,12,0\) |
| \(1\) | \(5,6,7,8,9,10\) | \(12,112,300,315,160,36\) | \(12,100,190,125,35,0\) |

Using
\[
\operatorname{rank}H^\ell(C^\bullet_q)
=\dim C^\ell_q-\operatorname{rank}\delta_\ell-\operatorname{rank}\delta_{\ell-1},
\]
the only nonzero groups in these two reduced degrees have ranks \(1\) at \((q,\ell)=(0,2)\) and \((1,10)\), and rank \(10\) at \((0,5)\) and \((1,7)\). Including the two endpoint groups and converting to the usual bigrading gives exactly
\[
\begin{aligned}
HH_{0,0}(Z_K;\mathbb Z)&\cong\mathbb Z,\\
HH_{-1,4}(Z_K;\mathbb Z)&\cong\mathbb Z,\\
HH_{-4,10}(Z_K;\mathbb Z)&\cong\mathbb Z^{10},\\
HH_{-5,14}(Z_K;\mathbb Z)&\cong\mathbb Z^{10},\\
HH_{-8,20}(Z_K;\mathbb Z)&\cong\mathbb Z,\\
HH_{-9,24}(Z_K;\mathbb Z)&\cong\mathbb Z,
\end{aligned}
\]
with every other bidegree zero. The machine-readable ranks and the exact computation are supplied in `COMPUTATION.json` and `verify_icosahedral_double_homology.py`.

## Verification

The verification script was run from its packaged path and completed successfully. It checks the face counts, all \(4096\) subsets, the integral bases for the relevant induced-subcomplex homology groups, all inclusion-induced maps, the identity \(\delta^2=0\), and unit-pivot exhaustion of every global differential. The resulting total rank is \(24\).

This is an exhaustive calculation for one finite complex, not an inference from a partial enumeration. No claim is made about the integral double homology of arbitrary sphere triangulations.

## Relationship to prior work

Valenzuela Ruiz, *Sphere Triangulations and their Double Homology* (arXiv:2405.00990), reports the icosahedron calculation over \(\mathbb F_2\), with the same six nonzero bidegrees and ranks. That calculation does not determine the integral groups: equal ranks over \(\mathbb F_2\) alone do not rule out integral torsion. The present result supplies the integer coefficient groups and an exact torsion-freeness check.

The paper's general formula for non-primitive sphere triangulations does not apply to the primitive icosahedral sphere. Its minimum-degree formula does not apply either, since the icosahedron has minimum vertex degree \(5\), whereas that formula assumes degree \(n+1=3\) for a \(2\)-sphere. The paper's simplex-deletion theorem concerns a different complex and does not imply the integral calculation above.

A later comparison of double, über, and poset homology identifies equivalent poset-cohomology formulations and gives isomorphisms in broad bidegree ranges, but it does not compute these groups for the icosahedron. The exact integer ranks and the absence of torsion remain specific to the calculation supplied here.

## Limitations

The result concerns only the boundary complex of the icosahedron. It does not classify the possible double-homology ranks of \(2\)-sphere triangulations, establish a general torsion-freeness theorem, compute an equivariant action, or infer a homotopy type for \(Z_K\). The first arXiv version's PDF endpoint was unavailable, but its HTML full text was inspected; the later PDF version was also inspected.

## References

- Carlos Gabriel Valenzuela Ruiz, “Sphere Triangulations and their Double Homology,” arXiv:2405.00990, first posted 2024-05-02. https://arxiv.org/abs/2405.00990
- Carlos Gabriel Valenzuela Ruiz, “Double, über and poset homology,” arXiv:2510.10424, first posted 2025-10-12. https://arxiv.org/abs/2510.10424
