# Translation stabilizers and exact orbit census of even-base Cantor spectra

## Finding

Let \(b=2u\geq 2\) be any even integer, \(n\geq 1\), and \(N=b^n\). The finite two-digit Cantor set in the cyclic group \(G=\mathbb Z/N\mathbb Z\) is
\[
E_{b,n}=\left\{u\sum_{j=0}^{n-1}\epsilon_j b^j:\epsilon_j\in\{0,1\}\right\}\pmod N.
\]
A spectrum is an unordered set \(\Lambda\subset G\) of size \(2^n\) such that \(\{x\mapsto e^{2\pi i\lambda x/N}:\lambda\in\Lambda\}\) is an orthonormal basis for the normalized counting space on \(E_{b,n}\). Every spectrum corresponds uniquely to a full binary tree of depth \(n\) with one even and one odd base-\(b\) digit at each internal vertex. There are exactly
\[
T_{b,n}=u^{2(2^n-1)}
\]
individual spectra.

For \(0\leq s\leq n\), let \(H_s\leq G\) be the unique subgroup of order \(2^s\), and let \(F_s\) count spectra invariant under all translations in \(H_s\). Then \(F_0=T_{b,n}\). For \(1\leq s\leq n\),
\[
F_s=\begin{cases}
0,&b\equiv0\pmod4,\\
u^{2(2^{n-s}-1)+s2^{n-s}},&b\equiv2\pmod4.
\end{cases}
\]
Thus all spectra have trivial stabilizers when \(4\mid b\), whereas nontrivial stabilizers occur when \(b\equiv2\pmod4\). For \(b=2\), there is only one spectrum and its stabilizer is \(H_n\); for \(b>2\) with \(b\equiv2\pmod4\), every order \(2^s\), \(0\le s\le n\), occurs.

The number of spectra whose translation stabilizer is **exactly** \(H_s\) is \(F_s-F_{s+1}\) for \(0\leq s<n\), and \(F_n\) for \(s=n\). The number of their translation orbits is, respectively,
\[
\mathcal O_s=\frac{2^s(F_s-F_{s+1})}{b^n}\quad(0\le s<n),\qquad
\mathcal O_n=\frac{2^nF_n}{b^n}.
\]
In particular, the total number of spectra modulo frequency translation is exactly
\[
\boxed{\mathcal O_{b,n}=\frac{F_0+\sum_{s=1}^n2^{s-1}F_s}{b^n}.}
\]
For \(b=6\) and \(n=2\), there are \(729\) spectra with stabilizer-order distribution \(648,72,9\) at orders \(1,2,4\), respectively, giving \(18+4+1=23\) translation orbits.

## Assumptions and scope

The base is any positive even integer \(b\ge2\), including \(b=2\), and the level is any positive integer \(n\). All frequencies and translations are taken modulo \(N=b^n\); the time set consists of distinct residues and has cardinality \(2^n\). No statement about infinite-dimensional spectral completeness of a limiting fractal measure is made. A period of a spectrum is a group element \(t\) for which \(\Lambda+t=\Lambda\).

## Proof

**Fourier-zero and digit-tree lemma.** The normalized Fourier transform of the indicator of \(E_{b,n}\) at \(k\in G\) is
\[
2^{-n}\sum_{x\in E_{b,n}}e^{2\pi ikx/N}
=2^{-n}\prod_{j=0}^{n-1}\left(1+e^{2\pi ik/(2b^{n-1-j})}\right).
\]
The product vanishes exactly when there is \(0\le r<n\) for which \(b^r\mid k\) and \(k/b^r\) is odd, using an integer representative of \(k\); this does not depend on the representative because \(b\) is even. For two distinct base-\(b\) expansions, this is equivalent to the least digit at which they differ having opposite parity. Therefore pairwise-orthogonal frequencies can have at most one even and at most one odd child at every occupied digit prefix. A depth-\(n\) tree with \(2^n\) leaves attains this bound at every vertex. Conversely every such complete tree gives a basis, proving the stated characterization. Each internal vertex has \(u\) even and \(u\) odd choices; there are \(2^n-1\) internal vertices, proving \(T_{b,n}\).

**Possible translation stabilizers.** If \(\Lambda+t=\Lambda\), translation by \(t\) partitions \(\Lambda\) into cycles of length \(\operatorname{ord}(t)\). Thus \(\operatorname{ord}(t)\mid2^n\), so every stabilizer is one of the nested subgroups \(H_s\). When \(4\mid b\), the element \(N/2=b^{n-1}(b/2)\) has even leading nonzero base-\(b\) digit, so it is not a Fourier zero of \(E_{b,n}\). Every nontrivial \(H_s\) contains \(N/2\). Consequently no spectrum admits a nontrivial period and \(F_s=0\) for \(s\ge1\).

Now suppose \(b=2u\) with \(u\) odd. For every \(s\le n\), each nonzero member of \(H_s\) has the form \(k=(N/2^s)j\), \(1\le j<2^s\). Write \(j=2^rj'\) with \(j'\) odd and \(0\le r<s\). Then
\[
k=b^{n-s+r}u^{s-r}j',
\]
whose displayed quotient after dividing by \(b^{n-s+r}\) is odd. Thus all distinct elements of any \(H_s\)-coset are pairwise orthogonal frequencies.

Every \(H_s\)-coset has \(2^s\) points sharing the same low \(n-s\) base-\(b\) digits. If a spectrum is invariant under \(H_s\), it is a union of exactly \(2^{n-s}\) such cosets. By the binary-tree lemma, no fixed low-digit prefix of length \(n-s\) can contain more than \(2^s\) leaves, and the occupied prefixes themselves must make a full spectral binary tree of depth \(n-s\). Therefore exactly one \(H_s\)-coset is chosen over each of its \(2^{n-s}\) leaves. For any prescribed low prefix there are \(b^s/2^s=u^s\) such cosets. Since distinct low prefixes already provide orthogonality, all choices are independent. There are \(u^{2(2^{n-s}-1)}\) low-prefix trees and \(u^{s2^{n-s}}\) coset choices, establishing the formula for \(F_s\).

**Exact-period and orbit enumeration.** A spectrum stabilized by \(H_s\) but not \(H_{s+1}\) has stabilizer exactly \(H_s\), because all possible stabilizers are nested. The translation orbit of a spectrum with stabilizer order \(2^s\) has cardinality \(b^n/2^s\), giving each \(\mathcal O_s\). Alternatively, in Burnside's lemma there is one identity fixing \(F_0\) spectra, and exactly \(\varphi(2^s)=2^{s-1}\) elements of order \(2^s\), each fixing precisely \(F_s\); elements of any other order fix none. Averaging these fixed-set counts proves the total orbit formula.

## Verification

The standalone standard-library program `checker.py` generates all spectral trees for twelve small pairs of base and level, tests their pairwise Fourier-zero conditions, translation stabilizers, exact subgroup fixed counts, and orbit representatives. In eleven of those cases it additionally enumerates every subset of the requisite size independently to verify completeness. It reports `EXACT_OK` for all twelve cases, including \((b,n)=(6,2)\) and \((4,3)\). The optional `cyclotomic_check.py` verifies 194 Fourier cancellations exactly in cyclotomic integer arithmetic using SymPy, independently of the digit criterion. Computations test finite instances and are not relied upon as proofs of the universal formulas.

## Relationship to prior work

Jorgensen and Pedersen introduced the spectral base-four Cantor measure. Dutkay, Han and Sun later classified maximal orthogonal sets for that **infinite** measure by spectral labelings of an infinite binary tree; their Proposition 5.1 gives a recursive base-four construction. Thus the elementary parity-tree mechanism, especially in base four, is prior background rather than the asserted new contribution. Deng, Dong and Li establish compatible-pair tree structures for spectra of infinite self-affine measures, which further confirm that the tree language is prior. Malikiosis studies cyclic-group spectrality and tiling through mask-polynomial and cyclotomic methods. The present theorem concerns the finite cyclic spectrum **translation action**: the sharp congruence dichotomy in stabilizer existence, all fixed-subgroup counts, each stabilizer stratum, and the exact quotient-orbit enumeration for every even base and level. These are not stated by the compared results; an unlocated equivalent finite-cyclic reformulation remains a historical-priority risk.

## Limitations

The classification is for the particular two-digit, half-base self-similar set, not all spectral subsets of arbitrary cyclic groups. Its complete binary-tree component is closely related to earlier fractal spectral-labeling results. An independent literature audit and independent validation have not been performed. The enumerations do not imply spectral completeness for any infinite-limit measure, nor do the finite checks substitute for the proof.

## References

D. E. Dutkay, D. Han, Q. Sun, *On the spectra of a Cantor measure*, arXiv:0804.4497v1 (public 2008-04-28), https://arxiv.org/abs/0804.4497 ; open full text https://sciences.ucf.edu/math/qsun/wp-content/uploads/sites/10/2016/09/stspec.pdf , especially Theorem 3.3 and Proposition 5.1.

P. E. T. Jorgensen and S. Pedersen, *Dense analytic subspaces in fractal \(L^2\)-spaces*, Journal d'Analyse Mathématique **75** (1998), 185–228; foundational spectral Cantor example (bibliographic background, not a competing orbit classification).

Q.-R. Deng, X.-H. Dong, M.-T. Li, *Tree structure of spectra of spectral self-affine measures*, Journal of Functional Analysis **277** (2019), 937–957, https://doi.org/10.1016/j.jfa.2019.04.006 , especially Theorems 3.1 and 5.1.

R.-D. Malikiosis, *On the structure of spectral and tiling subsets of cyclic groups*, arXiv:2005.05800 (2020), https://arxiv.org/abs/2005.05800 , especially Theorems 1.4–1.5 and Section 2.
