# A sharp \(\sqrt{2}\) obstruction for compact operators with Hilbert domain

## Finding

For every infinite-dimensional real or complex Hilbert space \(H\) and every nonzero Banach space \(X\), there is a fixed countable sequence of rank-one operators \(R_n\in S_{\mathcal K(H,X)}\) for which
\[
\sup_{\substack{S\in\mathcal K(H,X)\\ \|S\|\le 1}}
\inf_{n\ge 1}\|S+R_n\|=\sqrt{2}.
\]
Consequently, \(\mathcal K(H,X)\) fails \(\omega_1\)-octahedrality, with this sequence giving the explicit gap \(2-\sqrt{2}\).

## Assumptions and scope

Let \(H\) be an infinite-dimensional real or complex Hilbert space and \(X\ne\{0\}\) a Banach space. Choose an orthonormal sequence \((e_n)_{n\ge0}\subset H\), a vector \(z\in S_X\), and the Riesz coordinate functionals \(f_n(x)=\langle x,e_n\rangle\in S_{H^*}\), using the convention that the inner product is linear in its first argument. Then the \(f_n\) are orthonormal in \(H^*\). Define
\[
R_nx=f_n(x)z,\qquad n\ge1.
\]
Each \(R_n\) is rank one and has norm one. The supremum in the finding is over all compact operators \(S:H\to X\) with \(\|S\|\le1\). The exact constant is asserted for this specified sequence, not as a minimization over every possible countable witness family.

## Proof

Fix \(S\in\mathcal K(H,X)\) with \(\|S\|\le1\). The orthonormal sequence \((e_n)\) is weakly null, so compactness gives \(\|Se_n\|\to0\).

For any \(x\in S_H\), write \(x=a e_n+u\), where \(a=f_n(x)\), \(u\perp e_n\), and \(\|u\|=\sqrt{1-|a|^2}\). Then
\[
(S+R_n)x=a(z+Se_n)+Su,
\]
hence
\[
\|(S+R_n)x\|
\le |a|\,\|z+Se_n\|+\|S\|\sqrt{1-|a|^2}.
\]
For \(A,B\ge0\),
\[
\max_{0\le t\le1}\bigl(At+B\sqrt{1-t^2}\bigr)=\sqrt{A^2+B^2},
\]
by Cauchy--Schwarz, with equality at a unit vector proportional to \((A,B)\). Taking the supremum over \(x\in S_H\) therefore yields
\[
\|S+R_n\|\le\sqrt{\|z+Se_n\|^2+\|S\|^2}.
\]
As \(n\to\infty\), the right-hand side tends to \(\sqrt{1+\|S\|^2}\le\sqrt2\). Thus
\[
\inf_{n\ge1}\|S+R_n\|\le\sqrt2
\]
for every compact contraction \(S\).

To prove sharpness, set \(S_0x=f_0(x)z\). This is a rank-one compact operator of norm one. Since \(f_0\) and \(f_n\) correspond to orthogonal unit vectors in \(H\), \(\|f_0+f_n\|=\sqrt2\), and consequently
\[
\|S_0+R_n\|=\|(f_0+f_n)\otimes z\|=\sqrt2
\quad\text{for every }n\ge1.
\]
The upper bound and this attaining example prove the stated supremum exactly.

Finally, \(\omega_1\)-octahedrality would require a unit operator \(S\) for which \(\|S+R_n\|>\sqrt2\) for every \(n\), by taking the tolerance \(2-\sqrt2\). The bound just proved rules this out.

## Verification

The only limit used is \(\|Se_n\|\to0\), which follows because a compact operator maps weakly null sequences to norm-null sequences. The scalar maximization is exact and follows from Cauchy--Schwarz; no numerical approximation or finite enumeration is used. Sharpness is witnessed by the explicit rank-one operator \(S_0\).

## Relationship to prior work

Rueda Zoca's 2026 paper on transfinite octahedrality proves qualitatively that \(\mathcal K(Y,X)\) is not \(\omega_1\)-octahedral when \(Y\) is infinite-dimensional and uniformly convex. The present result specializes to Hilbert domains and gives a different, explicit orthonormal probe sequence with an exact minimax value \(\sqrt2\). The inspected theorem and corollary do not state this sharp value. Rueda Zoca's 2023/2024 work on universally octahedral operator spaces treats a finite-dimensional uniformly convex domain in its key quantitative lemma and does not provide this compact-operator minimax identity.

## Limitations

The result is specific to Hilbert domains and compact perturbations. It does not claim the same constant for arbitrary uniformly convex Banach domains, for noncompact \(S\), or for every possible countable sequence in the unit sphere. The value \(\sqrt2\) is sharp for the explicit sequence constructed above.

## References

1. Abraham Rueda Zoca, “Transfinite octahedrality in spaces of operators,” arXiv:2609.24414v1, first submitted 2026-09-21. The arXiv record lists MSC 46B04 first.
2. Abraham Rueda Zoca, “Banach spaces which always produce octahedral spaces of operators,” *Collectanea Mathematica* 75 (2024), 437--451. DOI: 10.1007/s13348-023-00394-9.
