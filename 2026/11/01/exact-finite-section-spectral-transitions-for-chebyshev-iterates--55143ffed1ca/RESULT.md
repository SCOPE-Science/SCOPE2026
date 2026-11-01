# Exact finite-section spectral transitions for Chebyshev iterates

## Finding

Let \(d\geq2\) be an integer, \(n\geq1\), and \(m=d^n\). For the dynamical map \(F_d(x)=(1-T_d(1-2x))/2\) of \([0,1]\), let \(\nu\) be the arcsine invariant probability measure and \(P_K\) the orthogonal projection onto the first \(K\) normalized Chebyshev polynomials in \(L^2(\nu)\). The finite observable

\[
B_{m,K}=P_K M_{F_d^{\circ n}} P_K\big|_{\operatorname{ran}P_K}
\]

has the *complete explicit spectrum* below for every integer \(K\geq1\). In particular, the following sharp visibility law holds:

\[
\bigl\|B_{m,K}-\tfrac12 I_K\bigr\|_{\rm op}
=\begin{cases}
0,&1\leq K\leq\lceil m/2\rceil,\\
1/4,&\lceil m/2\rceil<K\leq m,\\
1/(2\sqrt2),&K=m+1.
\end{cases}
\]

For \(1\leq K\leq m\), put
\(p=\max\{0,K-\lfloor m/2\rfloor-1\}\) and
\(c={\mathbf{1}}_{\{2\mid m,\ K>m/2\}}\). The eigenvalues of \(B_{m,K}\), with multiplicity, are exactly

\[
\tfrac14\ \text{(multiplicity }p+c\text{)},\qquad
\tfrac12\ \text{(multiplicity }K-2p-c\text{)},\qquad
\tfrac34\ \text{(multiplicity }p\text{)}.
\]

The empirical spectral distribution \(\nu_{m,K}^{\rm spec}\) of \(B_{m,K}\) satisfies the quantitative arcsine comparison

\[
\sup_{0\leq t\leq1}\left|\nu_{m,K}^{\rm spec}([0,t])-
\frac2\pi\arcsin\sqrt t\right|
\leq\frac{\lfloor m/2\rfloor+1}{K}.
\]

Thus if \(K/m\to\infty\), the spectral law tends to the arcsine distribution, whereas if \(K/m\to0\), it is eventually the point mass at \(1/2\). For \(K/m\to c_0\in(1/2,1]\), the limit consists of atoms of weights \(1-1/(2c_0)\) at each of \(1/4,3/4\) and \(1/c_0-1\) at \(1/2\). At \(c_0=1/2\) the limit is the point mass at \(1/2\).

For \(d=2\), \(F_d(x)=4x(1-x)\): a rank \(K\) invariant-measure Chebyshev observer cannot distinguish its \(n\)-th multiplication observable from the scalar \(1/2\) until \(K>\lceil 2^{n-1}\rceil\). The full multiplication operator nevertheless remains at distance exactly \(1/2\) from the scalar, in operator norm, at every time.

## Assumptions and scope

Define the degree-\(j\) Chebyshev polynomial of the first kind by \(T_j(\cos\theta)=\cos(j\theta)\). The state space is \([0,1]\) with invariant probability

\[
\mathrm d\nu(x)=\frac{\mathrm dx}{\pi\sqrt{x(1-x)}}.
\]

Set \(e_0(x)=1\), \(e_j(x)=\sqrt2\,T_j(1-2x)\) for \(j\geq1\). These form a complete orthonormal basis of \(L^2([0,1],\nu)\), and \(P_K\) projects onto \(\operatorname{span}\{e_0,\ldots,e_{K-1}\}\). Here \(M_g\) means multiplication by the bounded function \(g\), and compression is performed *after* composition of the scalar map, not by iterating a compressed matrix.

For clarity, the complete all-\(K\) spectral formula is stated in terms of \(C_{m,K}=I_K-2B_{m,K}\). For each residue \(r\) write

\[
N_r=\#\{j\in\{1,\ldots,K-1\}:j\equiv r\pmod m\}.
\]

Define \(L_0=1+\lfloor(K-1)/m\rfloor\). The eigenvalues of \(C_{m,K}\), with multiplicities, are the disjoint union of the following multiset families, omitting empty families:

1. The \(L_0\) values \(\cos((2j-1)\pi/(2L_0))\), \(1\leq j\leq L_0\).
2. For each integer \(1\leq r<m/2\), with \(L_r=N_r+N_{m-r}\), the \(L_r\) values \(\cos(j\pi/(L_r+1))\), \(1\leq j\leq L_r\).
3. If \(m\) is even, with \(L_*=N_{m/2}\), the \(L_*\) values \(\cos((2j-1)\pi/(2L_*+1))\), \(1\leq j\leq L_*\).

The eigenvalues of \(B_{m,K}\) are \((1-\lambda)/2\) as \(\lambda\) runs through this multiset. All counting statements include multiplicity and hold for arbitrary finite \(K\), not merely \(K\leq m\).

## Proof

**Conjugacy and invariance.** Put \(y=1-2x=\cos\theta\). The map becomes \(y\mapsto T_d(y)\); hence its \(n\)-th iterate is \(T_m(y)\), and the observed coordinate is \((1-T_m(y))/2\). The arcsine law of \(y\) corresponds to uniform \(\theta\in[0,\pi]\); since integer cosine multiplication preserves that pushforward law, \(\nu\) is invariant. Consequently \(C_{m,K}\) is precisely the compression of multiplication by \(T_m(y)\).

**Matrix entries.** The identity \(2T_iT_j=T_{i+j}+T_{|i-j|}\), together with Chebyshev orthogonality, gives for \(1\leq i,j<K\)

\[
(C_{m,K})_{ij}=\frac12\bigl({\mathbf{1}}_{\{|i-j|=m\}}+{\mathbf{1}}_{\{i+j=m\}}\bigr),
\]

and \((C_{m,K})_{0j}=(C_{m,K})_{j0}=2^{-1/2}{\mathbf{1}}_{\{j=m\}}\) for \(j\geq1\), while \((C_{m,K})_{00}=0\). In particular, a diagonal entry of \(1/2\) occurs at \(i=j=m/2\) when \(m\) is even.

**Block structure and full spectrum.** The graph of nonzero off-diagonal entries has one component on \(0,m,2m,\ldots\) (with first edge weight \(1/\sqrt2\), later edges \(1/2\)); a path on the union of each residue class \(r\pmod m\) and its reflected class \(m-r\pmod m\), where \(1\leq r<m/2\) (all edges \(1/2\)); and, for even \(m\), a path in class \(m/2\), whose first vertex has a self-loop of weight \(1/2\). Consecutive prefix truncation means no such path has a missing interior vertex. These components exhaust \(\{0,\ldots,K-1\}\).

For the component through zero, the monic characteristic polynomial is \(2^{1-L_0}T_{L_0}(z)\), so its eigenvalues are the first displayed cosine grid. For each ordinary path, the monic characteristic polynomial is \(2^{-L_r}U_{L_r}(z)\), with \(U_j\) the Chebyshev polynomial of the second kind; its zeros give the second grid. For the even central path, the monic characteristic polynomial is \(2^{-L_*}(U_{L_*}(z)-U_{L_*-1}(z))\), yielding the third grid. For an empty component the characteristic polynomial is \(1\), with no roots. This gives every finite eigenvalue exactly.

**Sharp low-resolution transitions.** For \(K\leq m\), the zero-residue component has length one. Every nonzero paired residue component has length at most two and the central component (when present) has length at most one. The paired two-vertex blocks have eigenvalues \(\pm1/2\); the central singleton has eigenvalue \(+1/2\); all remaining singletons have eigenvalue zero. A pair exists for each \(r\) satisfying \(m-K<r<K\) and \(1\leq r<m/2\), giving exactly \(p\) pairs. The central singleton gives \(c\). These counts yield the stated three-level spectrum and the first two norm regimes. When \(K=m+1\), the zero-residue component has length two, with eigenvalues \(\pm1/\sqrt2\), and all other components have largest absolute eigenvalue at most \(1/2\). This gives the third norm value.

**Quantitative spectral limit.** Write each block eigenvalue as \(\lambda=\cos\theta\). The angles in the three block types are respectively the midpoint grid \((2j-1)\pi/(2L)\), the interior grid \(j\pi/(L+1)\), and the shifted grid \((2j-1)\pi/(2L+1)\). Each length-\(L\) grid has empirical distribution function within \(1/L\) of uniform measure on \([0,\pi]\); this follows by comparing each ordered grid point with the adjacent fractions \((j-1)/L\) and \(j/L\). For \(B=(1-\cos\theta)/2\), the uniform angular law pushes forward to \(2\arcsin\sqrt t/\pi\) on \([0,1]\). Weighting each component by its size gives an error at most \(1/K\) per component. There are no more than \(\lfloor m/2\rfloor+1\) components, proving the displayed CDF bound. It gives the \(K/m\to\infty\) limit. The three-atom critical-scale limit follows directly from \(p/K\to1-1/(2c_0)\) and \(c/K\to0\) when \(1/2<c_0\leq1\). If \(K/m\to0\), the exact scalar regime eventually applies.

Finally, \(T_m\) attains \(\pm1\) and does so arbitrarily close to sets of positive arcsine measure, so the full multiplier \(M_{(1-T_m)/2}\) remains exactly \(1/2\) away from \((1/2)I\) in operator norm. This contrasts with the *finite compression* disappearing for \(K\leq\lceil m/2\rceil\).

## Verification

The attached standalone file `verify.py` constructs every compression matrix directly from its orthogonality entries and computes its eigenvalues independently of the block formulas. It passed 1,392 finite matrix/specification/cutoff/discrepancy comparisons for \(2\leq m\leq25\), seven independent Chebyshev-quadrature reconstruction tests, and eight logistic-iterate visibility checks. These are finite checks only; the displayed derivation proves the unrestricted theorem. Execute with `python verify.py` using Python and NumPy.

## Relationship to prior work

Janowicz and Orłowski, arXiv:2607.19159 (first submitted July 21, 2026), establish fixed-index matrix-element convergence for the logistic \(r=4\) map in a *shifted Legendre basis with Lebesgue measure*. Their formulas and cautions do not assert all-rank spectral information or a rank-dependent visibility threshold. The theorem here changes to the *invariant arcsine measure* with its Chebyshev basis, and computes the complete finite-section spectrum, including the resolution-scale phase change; it does not reinterpret their Lebesgue-basis result as the same finite section.

The Toeplitz-plus-Hankel Chebyshev Gram entry formula in Gumerov, Rigg, and Slevinsky, arXiv:2412.17663, Section 4, provides a general established route to the matrix entries used here. The Chebyshev multiplication identity itself is classical (DLMF 18.18.21). The additional result here is the simultaneous all-rank residue-path diagonalization, its sharp \(m/2\) and \(m+1\) boundaries, and the two noncommuting spectral-scaling limits. It is not claimed that the matrix entries or standard tridiagonal cosine zeros are new individually.

## Limitations

This is a finite-section spectral classification for integer Chebyshev maps and the invariant arcsine Hilbert space. It is not a statement about arbitrary parameters of the logistic family, the Lebesgue-Legendre compressions used in the motivating paper, or numerical quadrature artifacts. The invariant-measure change is essential. The theorem makes no assertion about unrelated operator-valued matrix recurrences, spectral convergence of arbitrary discretizations, or uniqueness in historical literature. Historical priority remains open to independent verification, particularly for specialized Toeplitz-plus-Hankel finite-section spectral results.

## References

- Maciej Janowicz and Arkadiusz Orłowski, *Quantum logistic map considered as discrete-time Heisenberg equation*, arXiv:2607.19159, version first submitted 2026-07-21; Sections 2.3 and 4.2. https://arxiv.org/abs/2607.19159
- Karim Gumerov, Samantha Rigg, and Richard Mikaël Slevinsky, *Fast measure modification of orthogonal polynomials via matrices with displacement structure*, arXiv:2412.17663, first submitted 2024-12-23; Section 4 and equation (8). https://arxiv.org/abs/2412.17663
- NIST Digital Library of Mathematical Functions, Section 18.18.21 (Chebyshev product linearization). https://dlmf.nist.gov/18.18
