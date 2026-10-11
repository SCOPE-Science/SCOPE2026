# Six-frequency rigidity for positively weighted Fourier frames on antipodal triples

## Finding
Fix any odd prime \(p\ge3\), put \(G=\mathbb Z_{2p}\), and let \(A=\{a,a+p,c\}\subset G\) with \(c\notin\{a,a+p\}\). For \(\lambda\in G\), write \(e_\lambda(t)=\exp(2\pi i\lambda t/(2p))\). We call a set of pairwise distinct frequencies \(\Lambda\subset G\) **positively tight** if strictly positive real numbers \(w_\lambda\) exist such that
\[
\sum_{\lambda\in\Lambda}w_\lambda e_\lambda|_A(e_\lambda|_A)^*=W I_3,\qquad W=\sum_{\lambda\in\Lambda}w_\lambda>0.
\]
Here the vectors are unnormalized; equivalently \(\{\sqrt{w_\lambda/W}\,e_\lambda|_A\}_{\lambda\in\Lambda}\) is a Parseval frame in \(\mathbb C^A\).

**Theorem.** The minimum possible cardinality \(|\Lambda|\) is exactly \(6\). For each fixed \(A\), exactly
\[
\boxed{\left(\frac{p(p^2-1)}{24}\right)^2}
\]
frequency sets attain this minimum. Every minimizing set and every positive weighting of it are completely described below; for each support its positive weighting is unique up to common positive scale.

After a position translation and a group automorphism, \(A\) can be taken to \(\{0,p,1\}\). In these coordinates a minimizing support contains exactly three even and three odd frequencies. Write the three chosen frequency indices in either parity as \(2u+\epsilon\), with \(\epsilon\in\{0,1\}\), \(u\in\mathbb Z_p\). Sort the three \(u\)-indices cyclically, and let \(h_0,h_1,h_2\) be their positive cyclic gaps, summing to \(p\). Then **the complete classification** is
\[
1\le h_0,h_1,h_2\le (p-1)/2
\]
for **each** parity independently. The positive weights for one triple, in the sorted order \(u_0,u_1,u_2\), are in the ratio
\[
\sin(2\pi h_1/p):\sin(2\pi h_2/p):\sin(2\pi h_0/p).
\]
Normalize the total weight of each parity to \(W/2\). This supplies the unique positive weights for the chosen six-frequency support, up to the common factor \(W\).

## Assumptions and scope
The primality of \(p\) is used in the affine reduction and in the equal-weight contrast. The weights are arbitrary strictly positive **real** numbers, the frequencies are distinct modulo \(2p\), and the vectors are evaluated on precisely the stated three distinct sites. Zero weights are not counted as frequencies. Counts are of labeled subsets \(\Lambda\), without quotienting by frequency translations or automorphisms. No assertion is made about other three-site geometries or composite odd moduli.

## Proof
**Affine reduction.** Exactly one of \(c-a\) and \(c-(a+p)\) is odd. Neither is divisible by \(p\): otherwise \(c\) would equal \(a\) or \(a+p\). Thus one of these differences is a unit modulo \(2p\). Translate the corresponding endpoint to \(0\) and multiply by the inverse difference; the three points become \(\{0,p,1\}\), since any unit modulo \(2p\) is odd and fixes \(p\). Multiplication of all frequencies by the inverse dual automorphism permutes \(G\), preserving support cardinality and weights. It therefore suffices to prove the canonical case.

**Exact tightness criterion.** Put \(\zeta=\exp(2\pi i/(2p))\) and let
\[
M_\epsilon=\sum_{\substack{\lambda\in\Lambda\\\lambda\equiv\epsilon\;(2)}}w_\lambda,
\qquad
Z_\epsilon=\sum_{\substack{\lambda\in\Lambda\\\lambda\equiv\epsilon\;(2)}}w_\lambda\zeta^\lambda.
\]
The Gram diagonal is \(W\) automatically. The three unordered differences of sites in \(\{0,p,1\}\) are \(1,p,p-1\). Their three Fourier moments vanish precisely when
\[
Z_0+Z_1=0,\qquad M_0-M_1=0,\qquad
\overline{Z_0-Z_1}=0.
\]
Indeed, \(\zeta^{\lambda(p-1)}=(-1)^\lambda\zeta^{-\lambda}\). Hence the necessary and sufficient criterion is
\[
\boxed{Z_0=Z_1=0,\quad M_0=M_1=W/2.}
\]
This is an identity over \(\mathbb C\), with no approximation or enumeration.

**Positive-triangle lemma.** The phases \(\zeta^{2u+\epsilon}\), with \(u\in\mathbb Z_p\), are the vertices of a rotated regular \(p\)-gon. Because \(p\) is odd, no two such phases are antipodal, and a strictly positive sum of one or two cannot vanish. Therefore each parity needs at least three frequencies and \(|\Lambda|\ge6\).

For three distinct points of a circle without antipodal pairs, the origin admits a strictly positive barycentric representation if and only if it is in the interior of their triangle, equivalently if all three successive angular gaps are strictly smaller than \(\pi\). With \(p\) odd this is exactly \(1\le h_j\le(p-1)/2\) for every gap. For such a triangle the single affine relation is unique after fixing total mass: oriented planar determinants give the positive barycentric weights as the three sines displayed in the finding (each associated to the opposite angular gap). A two-dimensional independent pair of difference vectors makes this solution unique. Choosing a triangle separately in each parity and normalizing their masses equally proves existence of six-frequency frames and exhausts all six-frequency supports and weights. For all \(p=2k+1\) one explicit admissible triangle has frequency indices \(\{0,k,2k\}\) in either parity, whose gaps are \(k,k,1\).

**Exact count.** Write \(p=2k+1\). The ordered gap triples are positive integers \((h_0,h_1,h_2)\), each at most \(k\), with sum \(2k+1\). Inclusion-exclusion gives
\[
\binom{2k}{2}-3\binom{k}{2}=\frac{k(k+1)}2
\]
such triples (with \(\binom{1}{2}=0\)). A starting vertex can be chosen in \(p\) ways, and each unlabeled triangle is thereby counted three times. Consequently one parity has exactly
\[
T_p=\frac p3\cdot\frac{k(k+1)}2=\frac{p(p^2-1)}{24}
\]
admissible triangle supports. The two parities are independent, giving exactly \(T_p^2\) minimizing six-frequency supports.

**Equal-weight comparison.** If all selected frequencies have equal positive weights, then the criterion gives \(\sum_{u\in E}\exp(2\pi iu/p)=\sum_{u\in O}\exp(2\pi iu/p)=0\) for nonempty parity index subsets \(E,O\subset\mathbb Z_p\), after a harmless common rotation. For prime \(p\), the minimal polynomial \(1+X+\cdots+X^{p-1}\) of a primitive \(p\)-th root shows that a nonempty \(0\)-\(1\) polynomial vanishing at this root must have every coefficient \(1\). Thus both parity classes must contain every \(p\) frequencies: the equal-weight minimum is \(2p\), attained by the whole Fourier family. This comparison is separate from the positive-weight cardinality minimization and demonstrates its gain when \(p>3\).

## Verification
The standalone Python standard-library checker `check_weighted.py` independently solves for real barycentric weights using a \(2\times2\) determinant, compares the positivity test with the cyclic gap inequalities for every triple, and directly evaluates all nine entries of the complex \(3\times3\) weighted frame operator for every classified six-frequency support. It checks the primes \(3,5,7,11\). The observed numbers of admissible triangles per parity are respectively \(1,5,14,55\), and the numbers of verified optimal supports are \(1,25,196,3025\), comprising \(29223\) direct complex Gram-entry comparisons. The checker executes in ordinary Python 3 without dependencies; run `python3 check_weighted.py` from the package directory. These tests corroborate, but do not replace, the unrestricted proof.

## Relationship to prior work
Malikiosis's 2020 preprint analyzes the structure of spectral subsets and tiling subsets of finite cyclic groups through orthogonal **bases**, equal-cardinality spectra and integer mask-polynomial vanishing. Dutkay and Ranasinghe's weighted Fourier frame work supplies the general finite matrix-isometry equation for weights in an iterated-function-system setting, but not the present sharp six-frequency lower bound, triangular support criterion, uniqueness or squared counting formula. Ferguson–Mayeli–Sothanaphan study conditioning of **Riesz bases** in finite abelian groups rather than sparse positively weighted redundant tight frames. The 1995 Lam–Leung theory treats vanishing sums of roots of unity with **integer coefficients**; such results do not imply a count or weights for arbitrary strictly positive real coefficients. Classical planar convexity supplies the triangle criterion but not, without this Fourier-moment reduction and counting, the global spectral-frame classification.

## Limitations
The statement assumes one antipodal pair in a three-point sampling set and an odd prime half-order. It classifies six-frequency **minimizers**, not the full family of larger positive-weight tight frames, and does not assert optimal numerical conditioning beyond tightness. The independent audit of mathematical correctness and exhaustive bibliographic novelty has not been carried out. Equivalent unindexed results on finite positive trigonometric quadrature remain possible.

## References
- R. D. Malikiosis, *On the structure of spectral and tiling subsets of cyclic groups*, arXiv:2005.05800 (first posted 2020-05-12), Forum of Mathematics, Sigma 10 (2022), e23, doi:10.1017/fms.2022.14.
- D. E. Dutkay and R. Ranasinghe, *Weighted Fourier Frames on Self-Affine Measures*, arXiv:1710.01224 (2017), Journal of Mathematical Analysis and Applications 462 (2018), 1032–1047.
- S. Ferguson, A. Mayeli and N. Sothanaphan, *Riesz bases of exponentials and multi-tiling in finite abelian groups*, arXiv:1904.04487 (2019).
- T. Y. Lam and K. H. Leung, *On vanishing sums of roots of unity*, arXiv:math/9511209 (1995).
