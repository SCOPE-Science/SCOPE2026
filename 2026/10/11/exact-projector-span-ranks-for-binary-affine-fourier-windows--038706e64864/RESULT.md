# Exact projector-span ranks for binary affine Fourier windows

## Finding
For every binary finite field \(F=\mathbb F_q\) of order \(q=2^n\), \(n\ge2\), we give the exact complex-linear rank of an affine group orbit of rank-one projectors, for a continuous two-real-parameter family of Fourier windows. This includes an explicit matrix-recovering window for every such field, and identifies an exceptional phase-alignment locus.

Let \(s=(q-2)/2\), and, for \(z\in\mathbb C\), set
\[
d_q(z)=\begin{cases}q-1,&|z|\ne1,\\1,&|z|=1,\end{cases}
\qquad
r_q(z)=\begin{cases}s,&\operatorname{Re}z\ne1,\\1,&\operatorname{Re}z=1\end{cases}
+s\,\mathbf 1_{\{\operatorname{Im}z\ne0\}}.
\]
The precise projector-span rank is
\[
\boxed{R_q(z)=d_q(z)+(q-1)r_q(z).}
\]
Full complex matrix recovery, equivalently \(R_q(z)=(q-1)^2\), holds exactly when \(|z|\ne1\), \(\operatorname{Im}z\ne0\), and either \(q=4\) or \(\operatorname{Re}z\ne1\). Thus \(z=2+i\) yields full matrix recovery for every \(q\ge4\), whereas \(z=2\) yields the strict rank \(q(q-1)/2\).

## Assumptions and scope
Equip \(\mathbb C^F\) with the counting inner product, linear in its first argument. Write
\[
H_0=\{f:F\to\mathbb C:\sum_{x\in F}f(x)=0\},
\quad\dim_{\mathbb C}H_0=q-1.
\]
Let \(\psi(t)=(-1)^{\operatorname{Tr}_{F/\mathbb F_2}(t)}\) and use unitary Fourier coordinates \(\widehat f(a)=q^{-1/2}\sum_x f(x)\psi(ax)\). Fix \(z\in\mathbb C\) and define \(\phi_z\in H_0\) through
\[
\widehat\phi_z(0)=0,\qquad
\widehat\phi_z(1)=z,\qquad
\widehat\phi_z(a)=1\quad(a\in F^\times\setminus\{1\}).
\]
Equivalently, for every \(x\in F\),
\[
\phi_z(x)=q^{-1/2}\bigl(q\,\mathbf 1_{\{x=0\}}-1+(z-1)\psi(x)\bigr).
\]
The affine group \(G=F\rtimes F^\times\) acts unitarily by \((\pi(k,l)f)(x)=f(l^{-1}(x-k))\). Define \(P_{k,l}\) to be the rank-one operator \(v\mapsto\langle v,\pi(k,l)\phi_z\rangle\pi(k,l)\phi_z\), for \(k\in F\), \(l\in F^\times\), and define
\[
R_q(z)=\dim_{\mathbb C}\operatorname{span}\{P_{k,l}:k\in F,\ l\in F^\times\}\subseteq\operatorname{End}_{\mathbb C}(H_0).
\]
These are unnormalized positive rank-one operators, possibly repeated if a stabilizer is present; normalization does not alter their span. The theorem concerns complex matrix recovery from linear orbit measurements, and therefore implies ordinary phase retrieval whenever the orbit spans the full matrix algebra.

## Proof
**Translation-block decomposition.** In nonzero Fourier coordinates \(a,b\in F^\times\), the orbit window is \(\widehat{\pi(k,l)\phi_z}(a)=\psi(ak)h_z(al)\), where \(h_z\) has the Fourier values above. Consequently,
\[
(P_{k,l})_{a,b}=\psi((a+b)k)h_z(al)\overline{h_z(bl)}.
\]
Orthogonality of additive characters implies that Fourier transforming the family of projectors in the translation variable \(k\) decomposes its span into \(q\) independent subspaces, one for each \(d=a+b\in F\). In characteristic two the \(d=0\) block is diagonal, and each nonzero \(d\) has \(q-2\) matrix positions; there are \(q-1\) nonzero difference blocks. Their ranks are computed separately below. The invertible Fourier change of basis leaves the total dimension unchanged.

**Diagonal block.** For \(d=0\), the \((l,a)\)-entry is \(|h_z(al)|^2\). Since multiplication permutes \(F^\times\), the resulting square matrix is \(J+(|z|^2-1)\Pi\), where \(J\) is the all-ones matrix and \(\Pi\) is a permutation matrix. Reorder columns to obtain \(J+(|z|^2-1)I\). The eigenvalue on constants is \(q-2+|z|^2>0\); on the zero-sum subspace it is \(|z|^2-1\). Therefore its rank is precisely \(d_q(z)\).

**Every nonzero block.** Fix \(d\ne0\) and write \(a=dx\), \(b=d(x+1)\) with \(x\in F\setminus\{0,1\}\). Reindex the row \(l\in F^\times\) by \(t=(dl)^{-1}\). Then
\[
B_{t,x}=1+(z-1)\mathbf1_{\{t=x\}}+(\overline z-1)\mathbf1_{\{t=x+1\}},\quad t\in F^\times,\ x\in F\setminus\{0,1\}.
\]
The involution \(x\mapsto x+1\) partitions the \(q-2\) columns into \(s=(q-2)/2\) pairs and partitions the rows other than \(t=1\) into matching pairs. On each pair, the exceptional two-by-two part is
\[
\begin{pmatrix}z-1&\overline z-1\\\overline z-1&z-1\end{pmatrix}.
\]
Use the sum and difference of the two columns in each pair. The antisymmetric columns have disjoint nonzero signed row-pair supports, each proportional to \(z-\overline z=2i\operatorname{Im}z\). They contribute rank \(s\) if \(\operatorname{Im}z\ne0\) and rank zero otherwise. The symmetric columns take equal values on each row pair; the unmatched row \(t=1\) sees their common nonzero background. If \(z+\overline z-2=2(\operatorname{Re}z-1)\ne0\), inspecting the unmatched row and then the individual row pairs proves these \(s\) columns independent. If \(\operatorname{Re}z=1\), all symmetric columns are equal, of rank one. Symmetric and antisymmetric images intersect trivially, since their row-pair parity differs. Thus the rank of every nonzero block is exactly \(r_q(z)\). Summing the blocks proves the stated formula.

**Full recovery and explicit contrast.** Since the diagonal block has at most \(q-1\) dimensions and each nonzero block at most \(q-2=2s\), full rank requires and suffices for \(d_q(z)=q-1\) and \(r_q(z)=2s\). The claimed conditions follow, noting that \(s=1\) only for \(q=4\); when \(s>1\), the symmetric rank must be \(s\), not one. The fixed choice \(z=2+i\) fulfills every condition. For \(z=2\), \(d_q(z)=q-1\) and \(r_q(z)=s\), so \(R_q(2)=(q-1)(s+1)=q(q-1)/2\). If the projectors span \(\operatorname{End}_{\mathbb C}(H_0)\), the trace-dual measurement functionals separate all complex matrices, hence also all signal rank-one matrices, giving phase retrieval up to global phase.

## Verification
The standalone script `verification/check_affine_binary.py` uses only the Python standard library. It constructs the actual affine-orbit projector measurement matrices in Fourier coordinates, reduces Gaussian integer coefficients modulo \(1009\) under \(i\mapsto469\), and computes modular ranks directly. It separately computes the diagonal and one nonzero-translation block. Running `python verification/check_affine_binary.py` checks five window parameters \(z=2+i,2,1+i,i,1\) in each of \(\mathbb F_4,\mathbb F_8,\mathbb F_{16}\): all fifteen modular ranks agree with the theorem, with full dimensions \(9,49,225\) for \(z=2+i\). For these chosen Gaussian-integer windows, modular agreement is a finite consistency check; the preceding algebra establishes the unrestricted complex-rank identity for every \(z\) and every \(n\ge2\).

## Relationship to prior work
Bartusel, Führ and Oussa established matrix-recovering affine orbits and explicit window criteria in prime fields, providing the natural motivating problem. The present classification instead treats all fields of characteristic two with extension degree at least two, and determines the exact complex matrix-span rank on every complex one-frequency perturbation of the flat nonzero Fourier window. Li's later results address sharp conditioning of matrix recovery over **odd** prime powers with real two-/three-level windows; their cited hypotheses do not cover this characteristic-two complex phase classification. These comparisons concern mathematical implications, not title matching; a formulation in broader unpublished or unindexed finite-group frame literature remains possible.

## Limitations
This theorem does not bound the least nonzero singular value, noise amplification, or the conditioning of linear reconstruction. A window whose projector span is deficient may still support a weaker phase-retrieval property; no converse to the sufficient full-span criterion is asserted. The numerical checker is not an infinite-field proof. No independent external mathematical audit is claimed.

## References
1. D. Bartusel, H. Führ and V. Oussa, *Phase retrieval for affine groups over prime fields*, arXiv:2109.07123, first posted 2021-09-15, especially Section 6.
2. D. Li, *Sharp Conditioning for Matrix Recovery by Finite Affine Orbits*, arXiv:2609.09619, first posted 2026-09-09; the stated theorem concerns odd prime powers.
