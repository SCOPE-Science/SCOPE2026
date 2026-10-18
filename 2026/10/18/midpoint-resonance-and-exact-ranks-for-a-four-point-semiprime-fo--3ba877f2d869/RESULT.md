# Midpoint resonance and exact ranks for a four-point semiprime Fourier aperture

## Finding
For every odd prime \(p\), let \(G=\mathbb Z_2\times\mathbb F_p\) with the unnormalized character matrix
\[
H_{(\epsilon,x),(\eta,y)}=(-1)^{\epsilon\eta}\exp(2\pi i xy/p).
\]
Choose \(c\in\mathbb F_p\), \(a\in\mathbb F_p^\times\), and \(\epsilon\in\mathbb Z_2\), and consider the *centered four-point aperture*
\[
A=\{(\epsilon,c),(1-\epsilon,c),(\epsilon,c+a),(\epsilon,c-a)\}.
\]
For every four-element frequency set \(B\subset G\), write \(B_0=\{y:(0,y)\in B\}\) and \(B_1=\{y:(1,y)\in B\}\). Then the \(4\times4\) matrix \(H[A,B]\) has **rank four** precisely in the following cases:

1. \((|B_0|,|B_1|)\) is \((3,1)\) or \((1,3)\);
2. \((|B_0|,|B_1|)=(2,2)\) and \(\sum_{y\in B_0}y\ne\sum_{y\in B_1}y\) in \(\mathbb F_p\).

All other four-element frequency sets give **rank exactly three**: they are either parity-homogeneous (four frequencies in one parity class) or have two frequencies in each parity class with equal pair sums.

The exact number of rank-three partners of every such \(A\) is
\[
\boxed{N_3(p)=2\binom p4+\frac{p(p-1)^2}{4}},
\]
with \(\binom p4=0\) when \(p=3\). The remaining \(\binom{2p}{4}-N_3(p)\) frequency sets have rank four; no smaller rank occurs. There are exactly \(p(p-1)\) distinct centered apertures of the indicated form.

**Every balanced rank-three partner has no proportional pair of rows or columns.** Thus exactly \(p(p-1)^2/4\) rank-three partners exhibit nontrivial singularity without a proportional row or column, for every odd prime \(p\).

## Assumptions and scope
All rank statements are over \(\mathbb C\). The prime \(p\) is any odd prime, with no large-prime hypothesis. Fourier entries have modulus one and are unnormalized; rescaling the whole Fourier matrix does not change ranks. The pairing above identifies the character matrix of \(\mathbb Z_{2p}\) up to invertible reindexing of rows and columns through the Chinese remainder theorem. The theorem classifies *all* four-frequency partners of the stated centered aperture family, not all four-point apertures.

A different nonzero choice of \(a\), translation of \(c\), or exchange of the two parity classes changes rows and/or columns only by nonzero diagonal factors and bijective frequency reindexing, preserving the rank rule and partner multiplicities. Thus it suffices to prove the case \(\epsilon=c=0\) and \(a\ne0\).

## Proof
Set \(\zeta=\exp(2\pi i/p)\), and order the four row indices as \((0,0),(1,0),(0,a),(0,-a)\). The rows of \(H[A,B]\) are, in that order, the constant row, the parity-sign row, the \(a\)-th Fourier row, and the \((-a)\)-th Fourier row.

**Homogeneous frequencies.** If all four frequencies have the same parity, the constant row and the parity-sign row are proportional, so the rank is at most three. The three distinct projected row coordinates \(0,a,-a\) and any three of the four distinct projected frequency coordinates form a nonsingular \(3\times3\) minor: writing \(x_j=\zeta^{a y_j}\), its rows are \(1,x_j,x_j^{-1}\); multiplying column \(j\) by \(x_j\) produces a three-by-three Vandermonde matrix with distinct nonzero nodes. Therefore the rank is exactly three. This case is empty at \(p=3\).

**Three-versus-one frequencies.** If the parity counts are three and one, a nonzero linear combination of the first two rows isolates the singleton column, while another combination is supported on the three-column majority block. Expanding along that singleton reduces invertibility to the \(3\times3\) prime-order Fourier minor indexed by projected row coordinates \(0,a,-a\) and by the three distinct projected majority frequencies. The same elementary three-by-three Vandermonde argument makes this minor nonzero. Hence the rank is four.

**Two-versus-two frequencies.** Write \(B_0=\{u,v\}\), \(B_1=\{s,t\}\), with \(u\ne v\) and \(s\ne t\). Adding and subtracting the constant and parity-sign rows, then eliminating their first coordinate within each two-column parity block, shows that the rank is two plus the rank of
\[
K=\begin{pmatrix}
\zeta^{au}-\zeta^{av}&\zeta^{as}-\zeta^{at}\\
\zeta^{-au}-\zeta^{-av}&\zeta^{-as}-\zeta^{-at}
\end{pmatrix}.
\]
Both entries in its first row are nonzero, and
\[
\det K=(\zeta^{au}-\zeta^{av})(\zeta^{as}-\zeta^{at})
\bigl(\zeta^{-a(u+v)}-\zeta^{-a(s+t)}\bigr).
\]
Because \(a\ne0\) and \(\zeta\) has order \(p\), the determinant vanishes if and only if \(u+v=s+t\) in \(\mathbb F_p\). When it vanishes, \(K\) still has rank one. The original matrix consequently has rank exactly three or four as asserted.

**Counting.** There are \(2\binom p4\) parity-homogeneous frequency sets. For each fixed sum in \(\mathbb F_p\), there are \((p-1)/2\) unordered pairs of *distinct* residues with that sum. Thus equal-sum balanced partners number
\[
p\left(\frac{p-1}{2}\right)^2=\frac{p(p-1)^2}{4}.
\]
The homogeneous and balanced cases are disjoint. In any balanced frequency set, *all four columns are pairwise nonproportional*: columns of different parity have different ratios at the two repeated-coordinate rows, whereas columns of the same parity have distinct projected frequencies and hence different ratios between rows with projected coordinates \(0\) and \(a\). Similarly, *all four rows are pairwise nonproportional*: a pair of rows with different projected coordinates has distinct ratios at the two frequency columns of either fixed parity, and the two repeated-coordinate rows have ratios \(1\) and \(-1\) on the two parity classes. These arguments require only \(p\) odd and the two distinct projected frequencies in each parity class. Hence every balanced singular partner, including pairs with \(B_0=B_1\), has no proportional rows or columns. Its exact count is \(p(p-1)^2/4\).

Finally, \(c\) is the unique repeated projected row coordinate, \(\epsilon\) the parity class containing three rows, and the unordered choice \(\{a,-a\}\) has \((p-1)/2\) possibilities. There are \(2p(p-1)/2=p(p-1)\) different centered apertures.

## Verification
The standalone standard-library script `checker.py` constructs every \(4\times4\) minor for the representative aperture and every four-frequency subset when \(p\in\{3,5,7,11,13\}\). It performs exact determinant arithmetic in \(\mathbb Z[\zeta_p]\): each permutation contributes an integer multiple of a power of \(\zeta_p\), reduced modulo \(X^p-1\). A determinant is zero exactly when its \(p\) coefficient entries are all equal, by the minimal polynomial \(1+X+\cdots+X^{p-1}\). It independently compares exact zeros with the parity-and-sum criterion and with the counting formula, and tests proportionality of every row pair and column pair by exact phase-ratio labels.

The respective total four-frequency choices are \(15,210,1001,7315,14950\); the singular counts are \(3,30,133,935,1898\), and the nonproportional singular counts are \(3,20,63,275,468\). All assertions tested by the script succeed and it ends in `CHECK_PASS`. The proof above, not this finite replay, covers every odd prime.

Run with `python3 checker.py` in a directory containing the supplied script. No external library or dataset is needed.

## Relationship to prior work
Caragea and Lee's *On the principal minors of Fourier matrices* (arXiv:2409.09793, first posted 2024-09-15) proves square-free nonvanishing for two- and three-point **principal** minors. The present statement concerns arbitrary four-column partners of a fixed four-row support and includes singular nonprincipal minors. Their result does not imply the stated midpoint test or counts.

Loukaki's *Chebotarev's theorem for cyclic groups of order pq and an uncertainty principle* (DOI 10.1112/blms.70192) proves nonvanishing when the row and column parity-class cardinalities match in the \(2p\) case. For the centered aperture, that covers the three-versus-one frequencies; it does not decide the two-versus-two class, where the new equality-of-sums resonance separates singular and nonsingular partners.

Delvaux and Van Barel's *Rank-deficient submatrices of Kronecker products of Fourier matrices* (report TW477, November 2006; DOI 10.1016/j.laa.2007.05.009) constructs maximal rank-deficient blocks using subgroup tilings and studies Hamming numbers, not the exact four-frequency partner rank distribution for this centered row support. Two further published computations on four-point indicator supports and on phase-only Fourier zeros for Cartesian rectangles use different coefficients and different questions; their zero-count statements do not imply this arbitrary-nullvector rank classification.

## Limitations
The classification is specific to centered apertures with one antipodal pair and two symmetric points in a common parity class, and to odd prime moduli. It does not classify arbitrary four-point supports on cyclic semiprimes or say that all rank-deficient minors arise from midpoint resonance. The partner counts do not give quantitative conditioning for nonsingular minors. The literature comparison is not an independent originality audit, and an equivalent older formulation under sparse interpolation terminology remains a residual risk.

## References
1. A. Caragea and D. G. Lee, *On the principal minors of Fourier matrices*, arXiv:2409.09793, version 1 posted 2024-09-15; latest consulted version 4, 2025-04-20. https://arxiv.org/abs/2409.09793
2. M. Loukaki, *Chebotarev's theorem for cyclic groups of order pq and an uncertainty principle*, *Bulletin of the London Mathematical Society* 57 (2025), 3841–3856. DOI: 10.1112/blms.70192. https://doi.org/10.1112/blms.70192
3. S. Delvaux and M. Van Barel, *Rank-deficient submatrices of Kronecker products of Fourier matrices*, report TW477 (November 2006); *Linear Algebra and Its Applications* 426 (2007), 349–367. https://www.cs.kuleuven.be/publicaties/rapporten/tw/TW477.pdf
4. *Four-point indicator Fourier-support trichotomy on cyclic semiprime groups*, publicly accessible mathematical result: https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-four-point-indicator-fourier-support-trichotomy-on-cyclic-semipr--590958c70885
5. *Phase-only Fourier-zero spectrum of a four-point rectangle on cyclic product groups*, publicly accessible mathematical result: https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-phase-only-fourier-zero-spectrum-of-a-four-point-rectangle-on-cy--b51ecb1779fe
