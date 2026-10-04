# Exact spectrum multiplicities for four-point spectral sets in \(\mathbb Z_{4p}\)
## Finding
For every odd prime \(p\), a four-element subset \(A\subset\mathbb Z_{4p}\) is spectral exactly when it is a transversal modulo \(4\). Such an \(A\) has exactly \(p^4\), \(p^2\), or \(p\) spectra. The value is \(p^4\) exactly for \(A=t+p\mathbb Z_4\); it is \(p^2\) exactly for the non-coset antipodal form \(A=\{x,x+2p,y,y+2p\}\) with \(x-y\) odd; otherwise it is \(p\), and the spectra are exactly the translates \(t+p\mathbb Z_4\).
## Assumptions and scope
A spectrum is a four-set \(B\) whose character matrix \((e^{2\pi iab/(4p)})_{a\in A,b\in B}\) has orthogonal columns. Spectra are counted as literal subsets. The theorem covers every odd prime \(p\).
## Proof
Let \(\zeta=e^{2\pi i/(4p)}\) and \(M_A(d)=\sum_{a\in A}\zeta^{da}\). Orthogonality is equivalent to \(M_A(b-b')=0\) for distinct \(b,b'\in B\), and spectral pairs are symmetric. If \(4\mid d\), a vanishing sum would be a sum of four \(p\)-th roots. Its multiplicity polynomial of degree below \(p\) would be divisible by \(1+X+\cdots+X^{p-1}\), forcing \(p\mid4\), impossible. Hence both members of a spectral pair are transversals modulo \(4\). Conversely every such \(A\) has each translate \(t+p\mathbb Z_4\) as a spectrum.

For \(4\nmid d\), decompose each \(4p\)-th root into a fourth root times a \(p\)-th root and group by residues modulo \(p\). Irreducibility of \(1+X+\cdots+X^{p-1}\) over \(\mathbb Q(i)\) forces the Gaussian-integer coefficient of every residue fiber to be the same. It must be zero: for \(p\ge5\) an empty fiber exists, while for \(p=3\) the only no-empty pattern is \(2+1+1\), and two fourth roots cannot sum to a single fourth root. Thus every occupied fiber cancels internally.

A two-point fiber cancels for odd \(d\) exactly when its points differ by \(2p\), and for \(d\equiv2\pmod4\) exactly when they differ by \(p\) or \(3p\). Therefore a subgroup coset has every non-multiple-of-four difference as a zero, giving all \(p^4\) transversals as spectra. A non-coset antipodal two-pair set has zero differences exactly at the odd residues together with \(2p\); any four-clique there consists of one even and one odd antipodal pair, giving \(p^2\) spectra. In every other case, adjacent residue classes in a spectral \(B\) can differ only by \(p\) or \(3p\), so all four points of \(B\) are congruent modulo \(p\), giving exactly the \(p\) translates of \(p\mathbb Z_4\).
## Verification
The included exact verifier works in \(\mathbb Q(i,\zeta_p)\) and exhausts all modulo-four transversals for \(p=3,5,7\). It returns the histograms \(\{3:72,9:6,81:3\}\), \(\{5:600,25:20,625:5\}\), and \(\{7:2352,49:42,2401:7\}\), then `VERIFY_OK`. This is corroborative; the universal theorem is analytic.
## Relationship to prior work
Bose--Madan provides the archive spectral-periodicity anchor. Malikiosis gives the finite-cyclic difference-set criterion, symmetry of spectral pairs, and broad Fuglede-type results for two-prime cyclic groups. The inspected statements do not enumerate all spectra of a fixed four-point set or give the \(p,p^2,p^4\) trichotomy.
## Limitations
The theorem is specific to four-point subsets of \(\mathbb Z_{4p}\) for odd prime \(p\), and counts literal spectra rather than affine-equivalence classes. An equivalent older statement may exist under factorization, Hadamard-pair, or mask-polynomial terminology.
## References
1. D. Bose and S. Madan, *Spectrum is periodic for n-Intervals*, arXiv:1002.4525, first submitted 2010-02-24.
2. R. D. Malikiosis, *On the structure of spectral and tiling subsets of cyclic groups*, arXiv:2005.05800; DOI 10.1017/fms.2022.14.
