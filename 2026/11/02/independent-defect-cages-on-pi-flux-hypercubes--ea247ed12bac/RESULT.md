# Independent defect cages on \(\pi\)-flux hypercubes

## Finding

For every integer \(d\ge 2\), a signed nearest-neighbor Hamiltonian on the binary hypercube \(Q_d\), with magnetic flux \(\pi\) through every square, has precisely two flat energies \(\pm\sqrt d\). Replacing the hopping on any **induced matching** of edges by individually weaker nonnegative hopping strengths produces independent, compact defect cages and an explicit full spectrum.

Write \(F=\{e_1,\dots,e_k\}\) for an induced matching: its edges have disjoint endpoints, and no endpoint of one edge is adjacent to an endpoint of another. The signed hopping on edge \(e\) is multiplied by \(1-\alpha_e\), with \(0<\alpha_e\le1\). Define

\[
L_\pm(\alpha)=\frac{\sqrt{\alpha^2+4(d-\alpha)}\pm\alpha}{2}.
\]

The spectrum, **as a multiset**, consists of \(\pm\sqrt d\), each with multiplicity \(2^{d-1}-2k\), together with the four values

\[
-L_+(\alpha_e),\quad -L_-(\alpha_e),\quad
L_-(\alpha_e),\quad L_+(\alpha_e)
\]

for every \(e\in F\). These four defect energies may coincide between different edges; the displayed multiplicities are counted accordingly. For full bond deletion, \(\alpha_e=1\), the four values are \(\pm(\sqrt{4d-3}+1)/2\) and \(\pm(\sqrt{4d-3}-1)/2\).

Each affected edge supports a four-dimensional invariant subspace, and different such subspaces are mutually orthogonal and dynamically decoupled. Any wave packet initially supported on an altered edge stays, at **all real times**, within the union of the two radius-one vertex stars of that edge: exactly \(2d\) vertices, independently of the full size \(2^d\). This statement also applies to a superposition initially supported on just one edge. The disjointness condition is essential for the independent-cage conclusion, as an explicit counterexample below shows.

## Assumptions and scope

The vertex set of \(Q_d\) is \(\{0,1\}^d\), with computational basis \(\{|x\rangle\}\). Coordinates are indexed by \(j\in\{0,\ldots,d-1\}\), and \(e_j\) is the corresponding binary unit vector. Define Hermitian signed coordinate flips by

\[
\Gamma_j|x\rangle=(-1)^{\sum_{\ell<j}x_\ell}|x\oplus e_j\rangle,
\qquad H_0=\sum_{j=0}^{d-1}\Gamma_j.
\]

Every hopping has magnitude one. Around each elementary four-cycle the product of its four hopping signs is \(-1\). For each \(e=\{u,v\}\in F\), let \(\varepsilon_e=\langle u|H_0|v\rangle\in\{-1,1\}\). The perturbed Hermitian Hamiltonian is

\[
H=H_0-\sum_{e=\{u,v\}\in F}\alpha_e\varepsilon_e
 (|u\rangle\langle v|+|v\rangle\langle u|).
\]

No onsite potentials or other hopping modifications are assumed. The claim concerns the finite one-excitation Hamiltonian, its eigenvalue multiplicities, and unitary dynamics \(e^{-itH}\); it is not a claim about noise, capture, or interacting particles.

## Proof

**1. Flat unperturbed spectrum.** Directly from the sign convention, \(\Gamma_j^2=I\) and \(\Gamma_j\Gamma_\ell=-\Gamma_\ell\Gamma_j\) for distinct indices. Therefore \(H_0^2=dI\). As \(H_0\) has zero diagonal, its trace vanishes, so its eigenvalues \(\sqrt d\) and \(-\sqrt d\) each have multiplicity \(2^{d-1}\).

**2. Four-dimensional cage of one edge.** Let \(e=\{u,v\}\in F\), put \(p=|u\rangle\) and \(q=\varepsilon_e|v\rangle\), and define

\[
W_e=\operatorname{span}\{p,q,H_0p,H_0q\}.
\]

In the ordered spanning list, the Gram matrix is

\[
G_e=\begin{pmatrix}1&0&0&1\\0&1&1&0\\0&1&d&0\\1&0&0&d\end{pmatrix},
\qquad \det G_e=(d-1)^2>0.
\]

Thus \(\dim W_e=4\). The identity \(H_0^2=dI\) shows that \(W_e\) is invariant under \(H_0\).

**3. Independent cages.** If distinct edges \(e,f\in F\) have no adjacent endpoints, the inner products between an endpoint of \(e\) and one of \(f\) vanish, as do those between an endpoint and the \(H_0\)-image of an endpoint on the other edge. The inner products between two such images vanish by \(H_0^2=dI\). Hence \(W_e\perp W_f\). Moreover, every edge modification is supported on its two endpoint basis vectors, so its perturbation annihilates \(W_f\) whenever \(e\ne f\). Consequently all \(W_e\) and their common orthogonal complement are invariant under the full \(H\). The complement has the unmodified action \(H_0\).

**4. Exact defect spectrum.** In the basis \((p,q,H_0p,H_0q)\), the restriction of \(H\) to \(W_e\) has matrix

\[
B_e=\begin{pmatrix}
0&-\alpha_e&d-\alpha_e&0\\
-\alpha_e&0&0&d-\alpha_e\\
1&0&0&0\\0&1&0&0
\end{pmatrix}.
\]

Its characteristic polynomial factors as

\[
\det(zI-B_e)=
(z^2+\alpha_e z+\alpha_e-d)
(z^2-\alpha_e z+\alpha_e-d).
\]

Since \(d\ge2\) and \(0<\alpha_e\le1\), both roots in each sign pair are nonzero and have the values stated above. On \(W_e\), the original \(H_0\) has two positive and two negative eigenvalues: its trace is zero and \(H_0^2=dI\). Removing these \(2k\) positive and \(2k\) negative eigenvalues leaves \(2^{d-1}-2k\) of each on the complement, proving the full multiset formula.

**5. Compact support and sharpness of separation.** Each of \(p,q,H_0p,H_0q\) is supported inside the two closed radius-one neighborhoods of \(u\) and \(v\). These neighborhoods share exactly the endpoints and otherwise have distinct vertices, so their union has \(2d\) vertices. Invariance of \(W_e\) proves the time-dependent caging claim.

The induced-matching hypothesis cannot simply be replaced by vertex-disjointness. In \(Q_3\), delete both edges \(\{000,001\}\) and \(\{010,011\}\), whose endpoints have cross-adjacencies. The resulting full characteristic polynomial is \((z^4-5z^2+5)^2\), instead of the product \((z^2-1)^2(z^2-4)^2\) obtained for the induced pair \(\{000,001\}\), \(\{110,111\}\). Thus there is no general factorization into isolated one-edge defect spectra for non-induced pairs.

## Verification

The standalone program `check_defect_cages.py` builds the signed Hamiltonian directly from the displayed definition. It uses exact integer matrix multiplication to test \(H_0^2=dI\), symbolic algebra for the \(4\times4\) characteristic factorization and the three-cube boundary example, and independent numerical Hermitian diagonalization for dimensions \(2\) through \(8\), multiple induced placements and multiple hopping strengths. The recorded output is `checks.txt`. It also verifies local support, four-dimensional rank, and inter-cage orthogonality with direct matrix calculations. Numerical comparisons are corroboration, not the infinite-family proof; the analytical steps above establish all dimensions and all allowed strengths.

Run from the package root using `python check_defect_cages.py` with Python 3, NumPy, and SymPy installed. No data files or external services are needed.

## Relationship to prior work

Vidal, Mosseri and Douçot (1998) introduced magnetic Aharonov–Bohm cages and flat-band confinement on special two-dimensional tilings. That establishes the physical context, not the present signed hypercube defect-matching spectrum. Vidal, Mosseri and Bellissard (1998) treated tight-binding Hamiltonians on hypercubes, but their coordinate translations commute; the present \(\pi\)-flux generators anticommute. Their spectrum and transport results therefore do not imply this theorem. Vidal, Butaud, Douçot and Mosseri (2001) investigated disorder, tile flips and the breakup of magnetic cages on dice-like tilings, primarily with diagonal disorder, rather than the exact survival and decoupling of selected edge defects on signed hypercubes.

The elementary anticommuting-generator identity and general invariant-subspace linear algebra are standard. The claim of interest is their combination into the complete **arbitrarily sized induced-matching defect spectrum**, including variable edge strengths, multiplicities, compact-cage decoupling, and a counterexample to weakening the geometric hypothesis. A comprehensive historical-priority judgment remains unperformed; a specific risk is unlocated work on frustrated hypercube bond defects or general compact-localized-state perturbation theorems.

## Limitations

The result assumes precisely one magnetic sign convention with \(\pi\) flux on every square, nonnegative weakening of induced-matching edges, and no other defects. It does not cover generic onsite disorder, arbitrary edge faults, interactions, thermalization or nonunitary dynamics. Its four-dimensional cages do not imply that arbitrary initial states are confined to a single cage; the complete Hilbert space is a direct sum of the stated defect sectors and a flat-spectrum complement. Finite computations cannot determine historical novelty or independently certify the proof.

## References

- J. Vidal, R. Mosseri, B. Douçot, *Aharonov–Bohm cages in two-dimensional structures*, arXiv:cond-mat/9806068v1, first posted 1998-06-05. https://arxiv.org/abs/cond-mat/9806068
- J. Vidal, R. Mosseri, J. Bellissard, *Spectrum and diffusion for a class of tight-binding models on hypercubes*, arXiv:cond-mat/9811323v1, first posted 1998-11-23. https://arxiv.org/abs/cond-mat/9811323
- J. Vidal, P. Butaud, B. Douçot, R. Mosseri, *How to escape Aharonov–Bohm cages?*, arXiv:cond-mat/0103611v1, first posted 2001-03-29. https://arxiv.org/abs/cond-mat/0103611
