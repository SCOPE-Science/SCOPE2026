# Four-sparse Walsh spectra are controlled by affine dimension on \((\mathbb Z/2\mathbb Z)^d\)
## Finding
For every integer \(d\ge3\), let \(G=(\mathbb Z/2\mathbb Z)^d\) and use the unnormalized Fourier transform
\[
\widehat f(\xi)=\sum_{x\in G} f(x)(-1)^{\xi\cdot x}.
\]
Assume \(|\operatorname{supp}f|=4\), write \(S=\operatorname{supp}f\), and let
\[
H=\langle S-S\rangle,\qquad r=\dim_{\mathbb F_2}H.
\]
Then \(r\in\{2,3\}\). If \(r=2\), the attainable Fourier-support sizes on that fixed support are exactly
\[
\{1,2,3,4\}\,2^{d-2}.
\]
If \(r=3\), the attainable Fourier-support sizes on that fixed support are exactly
\[
\{5,6,7,8\}\,2^{d-3}.
\]
Therefore the complete exact-support-four spectrum is
\[
\bigl\{|\operatorname{supp}\widehat f|:|\operatorname{supp}f|=4\bigr\}
=\{2,4,5,6,7,8\}\,2^{d-3}.
\]

There are exactly two affine support types: an affine two-plane and an affine-independent four-point set. In the affine-independent case, normalize the support to \(\{0,e_1,e_2,e_3\}\). For nonzero coefficients \(a,b,c,d\), identify the eight restricted characters with \(\varepsilon=(\varepsilon_1,\varepsilon_2,\varepsilon_3)\in\{\pm1\}^3\); then the local Fourier values are
\[
L(\varepsilon)=a+b\varepsilon_1+c\varepsilon_2+d\varepsilon_3.
\]
Its exact zero set \(Z\) has \(|Z|\in\{0,1,2,3\}\). If \(|Z|=2\), the two cube vertices have Hamming distance \(2\). If \(|Z|=3\), the three vertices are pairwise at Hamming distance \(2\), equivalently they are three vertices of one parity tetrahedron. Conversely, every allowed pattern of these forms occurs.

## Assumptions and scope
The group is the elementary abelian two-group \((\mathbb Z/2\mathbb Z)^d\), the Fourier transform is unnormalized as displayed above, and the time-domain support has exactly four points with all four coefficients nonzero. The theorem concerns support cardinalities and, in the affine-independent case, exact local zero patterns. It does not classify coefficient orbits, phases beyond zero/nonzero status, or supports of cardinality other than four.

## Proof
Translate \(S\) so that one support point is \(0\). Then the other three support points generate \(H\), hence \(2\le r\le3\). The restriction map \(\widehat G\to\widehat H\) is surjective and each character of \(H\) has exactly \(2^{d-r}\) extensions to \(G\). Translation changes Fourier values only by nonzero character factors. Consequently
\[
|\operatorname{supp}\widehat f|=2^{d-r}\,|\operatorname{supp}\widehat{f_H}|,
\]
where \(f_H\) is the translated function regarded on \(H\). Thus only the two local cases \(r=2\) and \(r=3\) remain.

If \(r=2\), then the four support points are all of \(H\cong(\mathbb Z/2\mathbb Z)^2\). The local Walsh matrix is invertible. Fix any nonempty desired local Fourier support \(T\subseteq\widehat H\). Prescribe arbitrary nonzero Fourier values on \(T\) and zero values off \(T\). Each time-domain coefficient of the inverse transform is a nonzero linear functional of the values on \(T\). Over \(\mathbb C\), finitely many proper hyperplanes cannot cover the coefficient space, so the prescribed nonzero values can be chosen so that all four inverse-transform coefficients are nonzero. Hence every local support size \(1,2,3,4\) occurs.

If \(r=3\), an affine automorphism sends the support to \(\{0,e_1,e_2,e_3\}\). The local transform is the cube-affine function
\[
L(\varepsilon)=a+b\varepsilon_1+c\varepsilon_2+d\varepsilon_3,
\qquad abcd\ne0.
\]
Let \(Z=\{\varepsilon:L(\varepsilon)=0\}\). Two adjacent cube vertices cannot both lie in \(Z\), because subtracting their equations would force one of \(b,c,d\) to vanish. Two antipodal vertices cannot both lie in \(Z\), because adding their equations would force \(a=0\). Therefore every pair of distinct vertices in \(Z\) has Hamming distance \(2\). Four cube vertices that are pairwise at distance \(2\) form one parity tetrahedron; summing the four equations \(L(\varepsilon)=0\) over that tetrahedron gives \(4a=0\), again impossible. Hence \(|Z|\le3\), proving the local support lower bound \(8-|Z|\ge5\).

The restrictions on two- and three-point zero sets have already been proved by the distance argument. Sharpness is explicit. The coefficient choices
\[
(1,2,4,8),\qquad (1,2,3,-6),\qquad (1,-1,2,-2),\qquad (1,-1,-1,1)
\]
have respectively \(0,1,2,3\) local zeros. Cube coordinate permutations and sign changes move the one-zero example to any singleton, the two-zero example to any distance-two pair, and the three-zero example to any three vertices of a parity tetrahedron. Therefore all allowed exact zero patterns occur and the local support sizes are exactly \(8,7,6,5\). Multiplying by the extension factor \(2^{d-3}\) gives the asserted \(r=3\) list. Taking the union with the \(r=2\) list gives the global set \(\{2,4,5,6,7,8\}2^{d-3}\).

## Verification
The standalone checker `artifacts/verify.py` uses exact rational linear algebra. For the affine-independent local model it exhausts all \(2^8\) candidate zero sets and determines exact realizability by computing the rational nullspace and checking whether any required nonvanishing functional is identically zero there. It obtains exactly one empty pattern, eight singleton patterns, twelve distance-two pairs, eight three-point parity-tetrahedron patterns, and no pattern of size at least four. It also checks that every nonempty local Fourier support in the affine-plane model is compatible with four nonzero time coefficients. Finally it verifies that four-subsets have exactly the two stated affine-span types in dimensions \(3\) and \(4\), with orbit-size totals \(14+56\) and \(140+1680\), and prints `VERIFY_OK`.

The finite checker verifies the critical local classifications exactly; the theorem in arbitrary dimension additionally uses the analytic character-restriction argument proved above.

## Relationship to prior work
Bonami and Ghobber study exact uncertainty equality cases in selected finite Abelian families and formulate the exact-support sets \(E_0(k,\ell)\), but their complete families are \(\mathbb Z_p\times\mathbb Z_p\), \(\mathbb Z_{p^2}\), and \(\mathbb Z_p\times\mathbb Z_q\) for distinct primes. Apart from the four-element base group, this does not cover \((\mathbb Z/2\mathbb Z)^d\) for arbitrary \(d\), and their focus is the minimum Fourier support rather than the complete exact-support-four spectrum.

Krahmer, Pfander, and Rashkov give a general rank criterion for exact support pairs and numerical diagrams for all finite Abelian groups of order at most \(16\). Their diagram includes \((\mathbb Z/2\mathbb Z)^4\), so the bare \(d=4\) support-size cells are not claimed as new. The present statement is the dimension-free structural theorem: it identifies the two affine support types, gives the complete attainable list for every fixed support of either type, and classifies all local zero patterns in the affine-independent case.

The Donoho--Stark equality classification already explains the minimum cell \(2^{d-2}\): it occurs when the four-point support is an affine two-plane with character-type coefficients. That known minimum does not determine the intermediate cells or the affine-independent lower bound \(5\,2^{d-3}\).

## Limitations
The result is specific to four-sparse functions on elementary abelian two-groups. It does not classify five-point supports, general \(p\)-groups, or coefficient moduli. Although claim-specific searches and the inspected full texts found no equivalent theorem, a differently phrased result in older Walsh-transform or coding-theory literature remains a residual originality risk.

## References
1. A. Bonami and S. Ghobber, *Equality cases for the uncertainty principle in finite Abelian groups*, arXiv:1003.5060, first submitted 26 March 2010; Acta Sci. Math. (Szeged) 79 (2013), 507--528.
2. F. Krahmer, G. E. Pfander, and P. Rashkov, *Uncertainty in time--frequency representations on finite Abelian groups and applications*, arXiv:math/0611493, first submitted 16 November 2006; Appl. Comput. Harmon. Anal. 25 (2008), 209--225.
3. D. L. Donoho and P. B. Stark, *Uncertainty principles and signal recovery*, SIAM J. Appl. Math. 49 (1989), 906--931.
