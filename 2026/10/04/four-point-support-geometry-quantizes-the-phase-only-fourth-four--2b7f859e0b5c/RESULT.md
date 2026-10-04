# Four-point support geometry quantizes the phase-only fourth Fourier moment

## Finding
Let \(p\ge11\) be prime and let \(A\subset\mathbb Z_p\) have four elements. For unimodular coefficients \((c_a)_{a\in A}\), define
\[
\mathcal M_A(c)=\frac1p\sum_{k\in\mathbb Z_p}\left|\sum_{a\in A}c_a e^{2\pi iak/p}\right|^4,
\qquad |c_a|=1,
\]
and let \(\mathcal M(A)=\min_c\mathcal M_A(c)\).

For a nonzero difference class \([d]=\{d,-d\}\), put
\[
\nu_A([d])=\#\bigl\{\{a,b\}\subset A:a-b\in\{d,-d\}\bigr\}.
\]
Write \(\lambda(A)\) for the multiset of positive values of \(\nu_A([d])\). Then
\[
\begin{array}{c|c}
\lambda(A)&\mathcal M(A)\\ \hline
(3,2,1)&19\\
(2,2,1,1)&20\\
(2,1,1,1,1)&24\\
(1,1,1,1,1,1)&28.
\end{array}
\]
These are the only possibilities when \(p\ge11\). The first profile occurs exactly when
\[
A=\{x,x+d,x+2d,x+3d\},\qquad d\ne0.
\]
Hence every four-point support satisfies \(\mathcal M(A)\ge19\), with equality exactly for affine four-term arithmetic progressions. Since \(\|c\|_2^2=4\), the corresponding phase-only merit factor
\[
\frac{16}{\mathcal M(A)-16}
\]
is at most \(16/3\), with equality exactly in the same case.

## Assumptions and scope
The group is the prime cyclic group \(\mathbb Z_p\) with \(p\ge11\). The support has exactly four distinct points. All four nonzero coefficients have one common magnitude, normalized to \(1\). The Fourier transform is the unnormalized character sum appearing in the definition of \(\mathcal M_A(c)\), while the outer average is normalized by \(1/p\).

The restriction \(p\ge11\) is structural rather than cosmetic. At \(p=7\), four-point difference sets create an additional repeated-difference profile and can achieve fourth moment \(16\); the theorem does not assert a classification for \(p=5\) or \(p=7\).

## Proof
For \(d\in\mathbb Z_p\), define the coefficient autocorrelation
\[
R_d=\sum_{\substack{a,b\in A\\a-b=d}}c_a\overline{c_b}.
\]
Character orthogonality gives the exact identity
\[
\mathcal M_A(c)=\sum_{d\in\mathbb Z_p}|R_d|^2.
\]
Here \(R_0=4\), and \(R_{-d}=\overline{R_d}\). Thus each nonzero difference class \([d]\) contributes \(2|R_d|^2\).

There are six unordered pairs in \(A\), so the positive multiplicities in \(\lambda(A)\) sum to \(6\). A multiplicity \(3\) forces three successive translates by one nonzero difference inside a four-point set. Because a nonzero element of \(\mathbb Z_p\) has order \(p>4\), those three edges form a path, hence \(A\) is an affine four-term arithmetic progression. Its difference profile is then exactly \((3,2,1)\).

If no multiplicity is \(3\), a profile \((2,2,2)\) cannot occur for \(p\ge11\). If all three doubled difference classes came from disjoint edge-pairs, the three perfect matchings of the four vertices would all have equal absolute differences; the corresponding three signed linear relations force two vertices to coincide in odd characteristic. Therefore some doubled class comes from adjacent edges, so after an affine change of variables \(A=\{0,1,2,t\}\). To obtain profile \((2,2,2)\), the class \([1]\) must remain doubled, one of \([t],[t-1],[t-2]\) must equal \([2]\), and the other two must coincide. The only nondegenerate possibilities are \(t=4\) or \(t=-2\), and then the last coincidence requires \([4]=[3]\), which forces \(p=7\). Thus for \(p\ge11\) only
\[
(3,2,1),\quad(2,2,1,1),\quad(2,1,1,1,1),\quad(1,1,1,1,1,1)
\]
remain.

For profile \((1,1,1,1,1,1)\), every nonzero autocorrelation contains one unimodular term, so
\[
\mathcal M(A)=16+12=28.
\]
For profile \((2,1,1,1,1)\), the doubled class must come from a three-term arithmetic progression; a matching-type collision would automatically create a second doubled class. Normalize the progression to \(\{0,1,2\}\) and choose coefficients \((1,1,-1)\) there. The doubled autocorrelation vanishes, while the four singleton classes each contribute \(2\), giving \(24\).

For profile \((2,2,1,1)\), both doubled autocorrelations can vanish simultaneously. If one doubled class consists of disjoint pairs, write the support as \(\{0,d,t,t+d\}\) and use coefficients \((1,1,1,-1)\) in that order. If both doubled classes arise from adjacent edges, the support is affinely equivalent to \(\{0,1,2,4\}\), and coefficients \((1,1,-1,-1)\) cancel both. Only two singleton classes remain, so the minimum is \(16+4=20\).

It remains to minimize on an affine four-term progression. Normalize the support to \(\{0,1,2,3\}\) and write
\[
x_j=c_j\overline{c_{j-1}},\qquad j=1,2,3.
\]
Then
\[
R_1=x_1+x_2+x_3,\qquad R_2=x_2(x_1+x_3),\qquad |R_3|=1.
\]
Multiplying the coefficient vector by a character rotates all three \(x_j\) by one common phase without changing the moment, so take \(x_1=1\). Put \(z=x_3\), \(y=x_2\), and \(r=|1+z|\in[0,2]\). For fixed \(z\), the best unit \(y\) points opposite \(1+z\), hence
\[
|1+y+z|^2+|1+z|^2\ge(r-1)^2+r^2
=2\left(r-\frac12\right)^2+\frac12.
\]
Therefore
\[
\mathcal M(A)\ge16+2\left(\frac12+1\right)=19.
\]
Equality occurs when \(|1+z|=1/2\) and \(y=-(1+z)/|1+z|\). For example, take
\[
z=-\frac78+\frac{\sqrt{15}}8i,\qquad y=-2(1+z),
\]
so that \(|z|=|y|=1\), and use the coefficient vector
\[
(1,1,y,yz).
\]
Then \(x_1=1\), \(x_2=y\), \(x_3=z\), and the fourth moment is exactly \(19\).

## Verification
The standalone script `artifacts/verify.py` exhaustively enumerates all four-point supports for the primes \(11,13,17,19,23,29,31\) and confirms that only the four stated difference profiles occur. It also checks the explicit phase constructions for a representative of every profile, verifies the progression extremizer numerically to high precision, and confirms the predicted moment through the autocorrelation identity.

The finite computation is corroborative only. The universal claim for all primes \(p\ge11\) is proved by the difference-profile argument and exact autocorrelation minimization above.

## Relationship to prior work
Schmidt's paper *On a problem due to Littlewood concerning polynomials with unimodular coefficients* studies how small \(L^4\) norms and merit factors can be for long unimodular polynomials. Its equation expressing the fourth norm as a sum of squared aperiodic autocorrelations is the direct analytic ancestor of the identity used here. The paper treats consecutive full supports and asymptotic families; it does not classify arbitrary four-point supports in prime cyclic groups or optimize the phases exactly for each additive support geometry.

Jedwab, Katz, and Schmidt study small \(L^4\) norms for binary Littlewood polynomials, again on consecutive supports and in an asymptotic regime. Their results do not imply the four-valued exact finite classification above, which allows complex unimodular phases and lets the support geometry vary.

The earlier Newman--Byrnes paper concerns \(\{\pm1\}\)-coefficient polynomials. Only bibliographic metadata and the publisher abstract were available in the present comparison; this leaves a residual risk concerning any isolated small-degree calculation there. Its advertised scope is nevertheless binary coefficient polynomials rather than an arbitrary-support prime-cyclic classification.

## Limitations
No statement is made for \(p=5\) or \(p=7\), for composite cyclic groups, for supports of cardinality other than four, or for unequal coefficient magnitudes. The proof classifies the minimum fourth moment, not all critical points or all minimizing phase vectors in the non-progression profiles.

The originality comparison is strongest against the inspected unimodular-polynomial and Littlewood-polynomial literature. A residual terminology risk remains for older sequence-design work that might encode the same four-point calculation in correlation language without emphasizing sparse support geometry.

## References
1. K.-U. Schmidt, *On a problem due to Littlewood concerning polynomials with unimodular coefficients*, arXiv:1302.2766v1, first posted 2013-02-12; J. Fourier Anal. Appl. 19 (2013), 457--466. The manuscript states primary MSC 42A05 and 11B83.
2. J. Jedwab, D. J. Katz, and K.-U. Schmidt, *Littlewood polynomials with small L4 norm*, Adv. Math. 241 (2013), 127--136, doi:10.1016/j.aim.2013.03.015.
3. D. J. Newman and J. S. Byrnes, *The L4 Norm of a Polynomial with Coefficients ± 1*, Amer. Math. Monthly 97 (1990), 42--45, doi:10.1080/00029890.1990.11995544.
