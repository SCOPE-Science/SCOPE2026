# Strict centerward growth of the numerical radius of a single-defect weighted shift

## Finding

For every integer \(n\ge4\), every real \(r>1\), and every integer \(1\le k<\lfloor n/2\rfloor\), the complex Hilbert-space numerical radii of finite weighted shifts satisfy
\[
w(S_{n,k}(r))<w(S_{n,k+1}(r)).
\]
Here \(S_{n,k}(r)\) has an exceptional positive weight \(r\) on its \(k\)-th consecutive link and unit weights on all other links. Reversing the link order leaves the radius unchanged. Thus the position or (for even-order paths) the unique central link maximizes the radius, with equality between positions only under reflection. For \(1<r<2\), the strict comparison answers the conjecture in the remark following Theorem 2.2 of Chien and Sheu [1].

An exact polynomial identity explains the comparison. With \(Q_j(\lambda)=U_j(\lambda/2)\), the monic rescaled Chebyshev polynomial of degree \(j\), and \(P_{n,k}(\lambda)=\det(\lambda I-S_{n,k}(r)-S_{n,k}(r)^*)\),
\[
P_{n,k+1}(\lambda)-P_{n,k}(\lambda)=-(r^2-1)Q_{n-2k-2}(\lambda).
\]

## Assumptions and scope

Work in \(\mathbb C^n\) with the usual inner product. The shift is the matrix with entries \((S_{n,k}(r))_{i+1,i}=r\) when \(i=k\), \((S_{n,k}(r))_{i+1,i}=1\) for every other \(1\le i<n\), and zero elsewhere. The numerical radius is \(w(S)=\sup_{\|x\|_2=1}|\langle Sx,x\rangle|\). The hypotheses are \(n\ge4\), \(r>1\), and \(1\le k<\lfloor n/2\rfloor\); the shift is finite and nilpotent, and the underlying scalar field is complex. The conclusion is strict for every admissible real \(r\), not merely asymptotic or numerical. When \(r=1\), all positions have equal radius and strictness is impossible.

## Proof

1. Let \(J_{n,k}=S_{n,k}(r)+S_{n,k}(r)^*\), a real symmetric nonnegative tridiagonal matrix whose adjacent off-diagonal entries are \(1\) except for the \(k\)-th, which is \(r\). The rotational diagonal-unitary symmetry of a weighted shift implies \(w(S_{n,k}(r))=\lambda_{n,k}/2\), where \(\lambda_{n,k}=\lambda_{\max}(J_{n,k})\). Indeed each Hermitian part \(\operatorname{Re}(e^{it}S_{n,k}(r))\) is unitarily similar to \(J_{n,k}/2\), and maximizing its largest eigenvalue over \(t\) gives the numerical radius.

2. Define \(Q_0=1\), \(Q_1(\lambda)=\lambda\) and \(Q_j(\lambda)=\lambda Q_{j-1}(\lambda)-Q_{j-2}(\lambda)\). These satisfy \(Q_j(\lambda)=U_j(\lambda/2)\). Expanding the tridiagonal determinant in the square of the exceptional edge gives the exact polynomial identity
\[
P_{n,k}(\lambda)=Q_n(\lambda)-(r^2-1)Q_{k-1}(\lambda)Q_{n-k-1}(\lambda).
\]
For clarity, the coefficient of the squared \(k\)-th edge in the continuant is the negative product of the determinants of the path components on \(k-1\) and \(n-k-1\) vertices. The unperturbed determinant is \(Q_n\).

3. The Chebyshev product identity
\[
Q_k Q_{n-k-2}-Q_{k-1}Q_{n-k-1}=Q_{n-2k-2}
\]
holds for every allowed \(k\). It follows immediately by the recurrence (or by \(U_j(\cos\theta)=\sin((j+1)\theta)/\sin\theta\), initially away from its removable singularities). Subtracting the formula in step 2 at adjacent edge positions yields
\[
P_{n,k+1}(\lambda)=P_{n,k}(\lambda)-(r^2-1)Q_{n-2k-2}(\lambda).
\]

4. Write \(\lambda_0=2\cos(\pi/(n+1))\), the largest eigenvalue of the unit-weight path. Its positive Perron vector makes the Rayleigh quotient strictly larger when any edge weight is changed from \(1\) to \(r>1\). Hence \(\lambda_{n,k}>\lambda_0\). Put \(j=n-2k-2\), which is a nonnegative integer strictly smaller than \(n\). For \(j=0\), \(Q_j\equiv1\). For \(j\ge1\), every zero of \(Q_j\) is of the form \(2\cos(m\pi/(j+1))\), \(1\le m\le j\). Its largest zero is strictly less than \(\lambda_0\) because \(j+1<n+1\). Since \(Q_j\) is monic, \(Q_j(\lambda_{n,k})>0\).

5. Evaluate the exact identity at the largest root \(\lambda_{n,k}\) of \(P_{n,k}\):
\[
P_{n,k+1}(\lambda_{n,k})=-(r^2-1)Q_{n-2k-2}(\lambda_{n,k})<0.
\]
Because \(P_{n,k+1}\) is a monic real polynomial tending to \(+\infty\) at \(+\infty\), it has a real root strictly above \(\lambda_{n,k}\). Its largest eigenvalue therefore satisfies \(\lambda_{n,k+1}>\lambda_{n,k}\), which proves the theorem. Link reversal maps position \(k\) to \(n-k\), giving the final classification. \(\square\)

## Verification

The standalone standard-library program `verify.py` checks the continuant formula and the Chebyshev product identity using exact rational polynomial arithmetic, for all \(4\le n\le24\) and the specified tested weights, and tests sample eigenvalue inequalities by a positive-definiteness/LDL bisection. On replay it reports 1486 exact polynomial assertions and 372 numerical spectral comparisons. These finite checks are supplementary: the five-step argument above proves the all-dimensions and all-real-parameters assertion. Reproduce with `python3 verify.py` from this package.

## Relationship to prior work

Chien and Sheu [1], Theorem 2.2 and its following remark, prove the centerward ordering for \(0<r<1\) in the reversed direction and for \(r\ge2\) in the asserted direction. They explicitly conjecture the missing strict inequality for \(1<r<2\), with a size-four example. The present proof establishes their proposed relation in that range and, by the same identity, for all \(r>1\). The original paper supplies a characteristic-polynomial representation, but does not derive the short positive-difference argument for the previously unaddressed range.

Vandanjav and Undrakh [2] study **two consecutive exceptional links** and give comparisons for other parameter ranges; that is a different weighting pattern, not an implication of the current one-exceptional-link result. Chang and Wang [3] characterize maximizers when weights are permuted on weighted cyclic shifts and also study infinite shifts. A global permutation maximum, even with one zero weight to encode a nilpotent shift, does not by itself establish the strict inequality for *each successive move toward the center*. Their rearrangement framework is important related work; any stronger unstated implication would be a residual priority risk.

## Limitations

The theorem concerns one nonunit link in an otherwise unit-weight, finite complex Hilbert-space shift; no conclusion is asserted for several defect weights, indefinite signs without unitary reduction, infinite-dimensional shifts, or non-Hilbert \(\ell_p\) numerical radii. The proof is self-contained but does not establish exhaustive bibliographic priority: a general older spectral rearrangement theorem could imply the strict chain. Independent mathematical assessment has not been performed.

## References

[1] M.-T. Chien and H.-A. Sheu, “The numerical radii of weighted shift matrices and operators,” *Operators and Matrices* **7** (2013), 197–204, doi:10.7153/oam-07-11, full article: https://files.ele-math.com/articles/oam-07-11.pdf (especially Theorem 2.2 and its following remark).

[2] A. Vandanjav and B. Undrakh, “On the numerical range of some weighted shift matrices and operators,” *Linear Algebra and its Applications* **449** (2014), 76–88, doi:10.1016/j.laa.2014.02.018 (especially §2, Theorems 2.1–2.2).

[3] C.-T. Chang and K.-Z. Wang, “Maximizing numerical radii of weighted shifts under weight permutations,” *Journal of Mathematical Analysis and Applications* **394** (2012), 592–602, doi:10.1016/j.jmaa.2012.04.039 (permutation maximizers, distinct from every-step monotonicity).
