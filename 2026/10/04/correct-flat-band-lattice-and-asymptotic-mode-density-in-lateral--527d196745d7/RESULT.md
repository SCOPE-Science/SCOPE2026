# Correct flat-band lattice and asymptotic mode density in laterally coupled magnetic layers

## Finding

Consider the magnetic Hamiltonian on two adjacent hard-wall layers coupled through a straight interface window, with magnetic field \(B>0\). Suppose the widths are commensurate:
\[
d_1=ps,\qquad d_2=qs,
\]
where \(p,q\in\mathbb N\) are coprime and \(s>0\).

At zero window width the cross-section is disconnected, so the Hamiltonian is the orthogonal direct sum of the two single-layer Hamiltonians. Its spectral labels are therefore the union
\[
E^{(j)}_{n,m}
=
B(2n+1)+\left(\frac{\pi m}{d_j}\right)^2,
\qquad
j\in\{1,2\},\quad n\in\mathbb N_0,\quad m\in\mathbb N.
\]
This is incompatible with the expression in Eq. (3.3a) of the primary source, which adds transverse energies from both layers.

For every finite interface window, the surviving flat bands singled out by the commensurability condition in Theorem 3.2 are exactly
\[
E_{n,r}
=
B(2n+1)+\left(\frac{\pi r}{s}\right)^2,
\qquad
n\in\mathbb N_0,\quad r\in\mathbb N.
\]
Indeed, the matching condition \(m_1/m_2=d_1/d_2\) is equivalent to \(m_1=pr\) and \(m_2=qr\).

Let \(N_{\mathrm{flat}}(E)\) count branch labels \((n,r)\) satisfying \(E_{n,r}\le E\). Then
\[
N_{\mathrm{flat}}(E)
=
\frac{s}{3\pi B}E^{3/2}+O(E).
\]
For the two decoupled layers, let \(N_{\mathrm{dec}}(E)\) count branch labels in their union, with multiplicity from the two summands. Then
\[
N_{\mathrm{dec}}(E)
=
\frac{s(p+q)}{3\pi B}E^{3/2}+O(E),
\]
and hence
\[
\lim_{E\to\infty}
\frac{N_{\mathrm{flat}}(E)}{N_{\mathrm{dec}}(E)}
=
\frac1{p+q}.
\]

## Assumptions and scope

The magnetic field satisfies \(B>0\). The layer widths are positive and written in lowest commensurate form \(d_1=ps\), \(d_2=qs\), with \(p,q\in\mathbb N\), \(\gcd(p,q)=1\), and \(s>0\). The coupling window is the straight window of the primary model and may have any finite nonnegative half-width.

The counting functions count quantum-number branch labels, not distinct numerical energy values. If \(B\) and \((\pi/s)^2\) satisfy additional arithmetic relations, different labels may give the same numerical energy; those coincidences are deliberately retained in the count.

## Proof

At zero window width the cross-section is the disjoint union of two strips. Therefore
\[
H_0(p)=H_0^{(1)}(p)\oplus H_0^{(2)}(p).
\]
Each summand separates into the shifted harmonic oscillator in the longitudinal coordinate and a one-dimensional Dirichlet Laplacian in the transverse coordinate. Thus the spectrum of the direct sum is the union of
\[
B(2n+1)+\left(\frac{\pi m}{d_1}\right)^2
\quad\text{and}\quad
B(2n+1)+\left(\frac{\pi m}{d_2}\right)^2.
\]
A direct sum cannot acquire an eigenvalue equal to the sum of one transverse eigenvalue from each disconnected component. This establishes the corrected decoupled labeling.

For positive window width, the primary source proves that a flat band survives exactly when
\[
\frac{m_1}{m_2}=\frac{d_1}{d_2}.
\]
Because \(d_1/d_2=p/q\) is in lowest terms, all positive integer solutions are
\[
m_1=pr,\qquad m_2=qr,\qquad r\in\mathbb N.
\]
The corresponding transverse wave number is common to the two sides:
\[
\frac{\pi m_1}{d_1}
=
\frac{\pi m_2}{d_2}
=
\frac{\pi r}{s}.
\]
Equivalently, on the full transverse interval one may use
\[
\chi_r(z)=\sin\!\left(\frac{\pi r z}{s}\right).
\]
It vanishes at \(z=-d_2\), \(z=0\), and \(z=d_1\), and its derivative is continuous through \(z=0\). Hence it satisfies the coupled-domain condition for every finite window and
\[
-\chi_r''=
\left(\frac{\pi r}{s}\right)^2\chi_r.
\]
Tensoring with the shifted Landau oscillator gives exactly
\[
E_{n,r}
=
B(2n+1)+\left(\frac{\pi r}{s}\right)^2.
\]

For the count, set
\[
R(E)=
\left\lfloor
\frac{s}{\pi}\sqrt{E-B}
\right\rfloor
\]
when \(E>B\). Then
\[
N_{\mathrm{flat}}(E)
=
\sum_{r=1}^{R(E)}
\left\lfloor
\frac{E-(\pi r/s)^2+B}{2B}
\right\rfloor.
\]
Replacing each floor by its argument produces an error \(O(R(E))=O(E^{1/2})\). Using
\[
\sum_{r=1}^R r^2
=
\frac{R(R+1)(2R+1)}6
\]
and \(R(E)=(s/\pi)E^{1/2}+O(1)\) gives
\[
N_{\mathrm{flat}}(E)
=
\frac{s}{3\pi B}E^{3/2}+O(E).
\]
The same calculation for a single disconnected layer of width \(d\) gives
\[
N_d(E)=\frac{d}{3\pi B}E^{3/2}+O(E).
\]
Adding the two summands with \(d_1+d_2=s(p+q)\) proves the stated formula for \(N_{\mathrm{dec}}(E)\) and the limiting ratio \(1/(p+q)\).

## Verification

The direct-sum correction follows from the geometry of the closed interface and the separated single-layer spectrum. The flat-band lattice follows independently from the source's matching condition and from the explicit transverse function \(\chi_r\).

A standalone checker recomputes the branch counts for several coprime width ratios, tests the interface zeros and common transverse wave numbers, and compares the normalized counts with the proved leading constants. These finite checks are corroborative only; the asymptotic statement is proved by the exact floor-sum calculation above.

## Relationship to prior work

The primary source derives the single-layer energies
\[
B(2n+1)+\left(\frac{\pi m}{d}\right)^2,
\]
states in Theorem 3.2 that flat bands survive precisely for matching pairs with \(m_1/m_2=d_1/d_2\), and proves this by smooth continuation of modes that vanish on the interface. It also states in the symmetric case that the surviving flat bands are the single-layer values. However, its displayed Eq. (3.3a) for the decoupled unequal-width system adds two transverse squares, which conflicts with the direct-sum geometry and with these neighboring statements.

The source does not state the explicit coprime lattice \(E_{n,r}\), the branch-count asymptotic, or the limiting fraction \(1/(p+q)\). The leading-density statement quantifies, at the level of mode labels, how much of the decoupled flat spectrum survives lateral coupling.

## Limitations

The theorem counts branch labels with multiplicity and does not assert an asymptotic for distinct numerical energies. It does not determine widths or crossings of the absolutely continuous bands, the number of open gaps, or the behavior under random perturbations. The originality search did not locate a published erratum or an equivalent counting law, but an unindexed correction or author note could reduce the originality of the correction component.

## References

1. P. Exner, *Magnetic transport in laterally coupled layers*, arXiv:2207.01252v1 (2022), later published in *Physica Scripta* 97, 104004. DOI: 10.1088/1402-4896/ac925e.
2. P. Exner and S. Spitzkopf, *Magnetic transport due to a translationally invariant potential obstacle*, arXiv:2410.16036v1 (2024), for a distinct later magnetic-transport geometry.
