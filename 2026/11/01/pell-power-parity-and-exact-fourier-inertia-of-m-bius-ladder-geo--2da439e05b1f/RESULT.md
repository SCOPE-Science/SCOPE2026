# Exact distance determinants of Möbius ladders: a Pell square and a power of two

## Finding

Let \(M_{2n}\), for \(n\ge3\), be the undirected graph on \(\mathbb Z/(2n)\mathbb Z\) with edges of increments \(\pm1\) and \(n\). Let \(D_n\) be its ordinary shortest-path distance matrix with unit edge lengths. Put
\[
R_n=\left\lfloor\frac{n^2+2n-1}{2}\right\rfloor,
\qquad P_m=\frac{(1+\sqrt2)^m+(1-\sqrt2)^m}{2}.
\]
Here \(R_n\) is the row sum of \(D_n\) and \(P_m\) is the half-Pell–Lucas sequence, with \(P_1=1\), \(P_2=3\) and \(P_m=2P_{m-1}+P_{m-2}\). The signed determinant satisfies
\[
\boxed{\det D_n=\begin{cases}
(-1)^{(n+1)/2}R_n 2^{2n-2}, & n\text{ odd},\\
-R_n P_{n/2}^{\,2}, & n\text{ even}.
\end{cases}}
\]
Thus the integer determinant divided by the eigenvalue of the constant character is a signed power of two at odd order parameter \(n\), and the negative of a Pell–Lucas square (using the half-Pell–Lucas convention) at even \(n\).

## Assumptions and scope

This is the determinant of the integer matrix of ordinary graph distances, not a resistance-distance, adjacency or Laplacian determinant. Characters of the cyclic vertex set index eigenvalues with their full multiplicities. The contribution is the exact product evaluation for the determinant. The individual Fourier multipliers are included as inputs to the product calculation, not as a separate originality claim.

## Proof

**Distance row and Fourier factors.** Steps commute on the cyclic vertex set, and two chord steps have net increment zero modulo \(2n\). A shortest path therefore uses zero or one chord, giving
\[
d(0,j)=\min\{j,2n-j,1+|n-j|\},\qquad 0\le j<2n.
\]
Write \(L=\lfloor(n+1)/2\rfloor\). The level \(d(0,j)\ge 1\) consists of all \(j\ne0\); the level \(d(0,j)\ge t\) for \(2\le t\le L\) consists of the intervals \([t,n-t+1]\) and \([n+t-1,2n-t]\) of integers. Summing their sizes gives \(\lambda_0=2n-1+\sum_{t=2}^L 2(n-2t+2)=R_n\).

For a nonzero frequency \(k\), put \(x=\pi k/(2n)\) and \(z=e^{-2ix}\). The matrix is circulant. The first level contributes \(-1\) to its eigenvalue \(\lambda_k\); the other levels contribute
\[
z^{t-1}(z+(-1)^k)\frac{1-z^{n-2t+2}}{1-z}.
\]
This last expression is \(-2\cos(2(t-1)x)\) for odd \(k\), and \(-2\cot x\sin(2(t-1)x)\) for even \(k\). The finite cosine sum gives \(-\sin((2L-1)x)/\sin x\) for \(\lambda_k\) when \(k\) is odd. The sine sum gives \(-1-\cot x\,[\cos x-\cos((2L-1)x)]/\sin x\) when \(k\) is even. Substituting \((2L-1)=n\) for odd \(n\), or \(n-1\) for even \(n\), gives the factors used below:
\[
\begin{array}{c|cc}
 & k\text{ odd} & k=2h\ne0 \\
\hline
n\text{ odd} & (-1)^{(k+1)/2}\csc x & -1/(1+(-1)^h\cos x)\\
n\text{ even} & (-1)^{(k+1)/2}\cot x &
\begin{cases}-1,&h\text{ even},\\-1-2\cot^2 x,&h\text{ odd}.\end{cases}
\end{array}
\]

**Odd \(n\).** Taking the absolute values of the factors at \(1\) in \(z^n+1\) gives
\(\prod_{j=1}^n\sin((2j-1)\pi/(2n))=2^{1-n}\).
For \(k=2j-1\) the sign is \((-1)^j\), so the odd-frequency product is \((-1)^{(n+1)/2}2^{n-1}\). For the even frequencies, the denominator at an odd \(h\) is \(2\sin^2(\pi h/(2n))\); an even \(h\) has the same denominator as the odd index \(n-h\). The sine product over odd \(h\) with \(1\le h<n\) equals \(2^{-(n-1)/2}\), by pairing indices in the full odd-sine product and dropping the central factor \(1\). Thus the denominator product is \(2^{n-1}(2^{-(n-1)/2})^4=2^{1-n}\). The sign is positive because \(n-1\) is even. Including \(\lambda_0\) gives the odd formula.

**Even \(n=2m\).** Conjugate odd frequencies \(k,2n-k\) give squares. On the representatives \(1\le k<n\) with \(k\) odd, the positive cotangents at \(k\) and \(n-k\) are reciprocal, with any unpaired central cotangent equal to \(1\). The entire odd-frequency product is therefore \(1\). The \(n-1\) nonzero even frequencies are negative and an odd \(h=k/2\) gives absolute value \((3+\cos(\pi h/m))/(1-\cos(\pi h/m))\). Their signed product is
\[
-\prod_{\substack{1\le h<2m\\h\text{ odd}}}
\frac{3+\cos(\pi h/m)}{1-\cos(\pi h/m)}.
\]
The numbers \(c_h=\cos(\pi h/m)\) for these odd \(h\) are precisely the roots of \(T_m(X)+1\) with multiplicity, where \(T_m(\cos\theta)=\cos(m\theta)\). Interior roots occur twice, as follows by expanding about the corresponding angles, and the root \(-1\) when \(m\) is odd occurs once. Evaluating at \(-3\) and \(1\) cancels the leading coefficient and gives
\[
\prod_h\frac{3+c_h}{1-c_h}
=(-1)^m\frac{T_m(-3)+1}{T_m(1)+1}
=\frac{T_m(3)+(-1)^m}{2}.
\]
With \(r=1+\sqrt2\) and \(s=1-\sqrt2\), one has \(r^2=3+\sqrt8\), \(s^2=3-\sqrt8\), hence \(r^{2m}+s^{2m}=2T_m(3)\) and \(rs=-1\). The last product equals \(((r^m+s^m)/2)^2=P_m^2\). Including the constant character proves the result.

## Verification

The companion `check_mobius.py` constructs distance matrices by breadth-first search and includes exact integer determinant comparisons for \(3\le n\le16\). The first four exact values, at \(n=3,4,5,6\), are \(112,-99,-4352,-1127\). This finite comparison tests the formula in both parities; the proof of the product evaluation is for all \(n\ge3\).

## Relationship to prior work

*Exact quadratic embedding constants and maximizing Fourier modes of Möbius ladders* gives equivalent all-frequency nonconstant formulas for the same geodesic distance matrix in proof step 3. In particular, its odd-\(n\) even-frequency factor \(((-1)^h\cos x-1)/\sin^2 x\) is \(-1/(1+(-1)^h\cos x)\), and splitting its even-\(n\) expression by the parity of \(h\) gives the two displayed values. Nonsingularity, the eigenvalue signs and the obstruction to 1-negative type are not claimed as separate contributions here. The spectral statement computes individual factors rather than their evaluated product. The odd sine factorization and the even Chebyshev quotient give that product, with an explicit arithmetic parity law not supplied by the quadratic embedding constant.

Ilić's integral circulant graphs use gcd-defined generator sets; this is not the full opposite-chord family. Aalipour et al. give exact distance determinants for other graph families. Azimi and Farrokhi's Möbius-ladder formulas involve resistance and Laplacian pseudoinverses. Neither cyclic Fourier diagonalization nor the elementary trigonometric product identities are claimed as new.

## Limitations

This result concerns only unit-edge Möbius ladders and ordinary distances. It neither establishes a determinant formula for arbitrary graphs with a chord generator nor treats weighted or resistance distances. The comparisons above do not exclude an equivalent evaluated formula in other literature or fix priority among related spectral calculations.

## References

- *Exact quadratic embedding constants and maximizing Fourier modes of Möbius ladders*, Finding and proof step 3, https://github.com/Resultary/2026/blob/main/2026/11/2/SCOPE-exact-quadratic-embedding-constants-and-maximizing-fourier-modes--e4d98a43c5a0/RESULT.md
- A. Ilić, *Distance spectra and Distance energy of Integral Circulant Graphs*, arXiv:1104.1097.
- G. Aalipour et al., *On the distance spectra of graphs*, arXiv:1509.01196.
- A. Azimi and M. Farrokhi D. G., *Explicit formulas for matrices associated to ladder, circular ladder, and Möbius ladder graphs*, arXiv:2306.10497v1.
