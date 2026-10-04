# Exact Fourier-support spectrum on ternary affine parallelograms
## Finding
Let \(d\ge 2\), let \(G=\mathbb F_3^d\), and let \(f:G\to\mathbb C\) have support exactly
\[
S=x+\{0,u,v,u+v\},
\]
where \(u,v\in\mathbb F_3^d\) are linearly independent and all four values of \(f\) on \(S\) are nonzero. Then the attainable Fourier-support sizes are exactly
\[
|\operatorname{supp}\widehat f|\in \{4,6,7,8,9\}\,3^{d-2}.
\]
Every listed size occurs on every affine parallelogram support. In particular, \(5\cdot 3^{d-2}\) is impossible on this support class even though both neighboring local sizes \(4\cdot 3^{d-2}\) and \(6\cdot 3^{d-2}\) occur.

## Assumptions and scope
The Fourier transform may use any standard nonzero normalization; only its support is relevant. Translation of \(S\) changes Fourier values by phases, and an invertible linear change of variables permutes frequencies, so it suffices to treat \(S=\{0,e_1,e_2,e_1+e_2\}\). The claim concerns precisely affine parallelogram supports with four nonzero complex coefficients; it does not classify arbitrary four-point supports in \(\mathbb F_3^d\).

## Proof
Write \(\omega=\exp(2\pi i/3)\). After the normalization above, the Fourier transform depends on the first two frequency coordinates through
\[
P(X,Y)=a+bX+cY+dXY,
\]
where \(a,b,c,d\in\mathbb C^\times\) and \(X,Y\in\{1,\omega,\omega^2\}\). Each of the nine local values is repeated for exactly \(3^{d-2}\) frequencies.

Fix \(X\). Then
\[
P(X,Y)=(a+bX)+(c+dX)Y.
\]
Unless this expression is identically zero as a function of \(Y\), it has at most one zero among the three third roots of unity. Hence, if no full row is zero, the local zero count is at most three.

Suppose a full row \(X=\alpha\) is zero. Then \(a+b\alpha=0\) and \(c+d\alpha=0\), and therefore
\[
P(X,Y)=(X-\alpha)(b+dY).
\]
If \(-b/d\) is not a third root of unity, exactly the row \(X=\alpha\) vanishes and the local zero count is three. If \(-b/d\) is a third root of unity, one full row and one full column vanish, giving exactly \(3+3-1=5\) zeros. Thus four local zeros are impossible, and the only possible local zero counts are \(0,1,2,3,5\).

All five possibilities occur with nonzero coefficients. Direct substitution on the nine pairs of third roots gives local zero counts \(0,1,2,3,5\), respectively, for
\[
(a,b,c,d)=(1,1,1,1),\quad(-4,-3,3,4),\quad(-4,-3,-3,1),\quad(1,1,-1,-1),\quad(1,-1,-1,1).
\]
Hence the local support sizes are exactly \(9,8,7,6,4\), and multiplication by \(3^{d-2}\) proves the stated spectrum.

## Verification
The standalone verifier `artifacts/verify.py` performs exact arithmetic in \(\mathbb Q(\omega)\), checks the five witness coefficient vectors, and examines all \(\binom94=126\) four-row subsets of the local Fourier evaluation matrix. Whenever four prescribed zeros admit a one-dimensional nullspace with all four physical coefficients nonzero, the exact calculation finds five actual zeros, corroborating the analytic exclusion of a four-zero pattern. The verifier prints `VERIFY_OK` on success. The finite calculation is corroborative; the proof above establishes the result for every \(d\ge2\).

## Relationship to prior work
Delvaux and Van Barel study rank-deficient submatrices of Kronecker products of Fourier matrices and explicitly analyze the \(F_3\otimes F_3\) structure. Their principal invariant is the Hamming number, which gives extremal output-support sizes; their report also notes that its Hamming-number characterization does not characterize uniqueness of the relevant rank-deficient submatrices. The fixed four-column affine-parallelogram spectrum \(\{4,6,7,8,9\}\), including the forbidden intermediate size \(5\), is therefore not implied by the inspected Hamming-number statements.

Bonami and Ghobber classify equality cases for minimum-support uncertainty problems in \(\mathbb Z_p\times\mathbb Z_p\), including \(p=3\). Those equality cases determine extremal support behavior rather than the complete list of Fourier-support sizes for a fixed four-point affine parallelogram. Thus their results do not imply the full spectrum above.

## Limitations
The argument uses the bilinear form forced by a four-point affine parallelogram. It does not give the Fourier-support spectrum for affine-independent or other four-point configurations in odd characteristic, nor does it classify coefficient vectors beyond the support-size alternatives. A residual literature risk is that an equivalent fixed-submatrix statement may exist under Fourier-matroid or rank-pattern terminology not used in the inspected sources.

## References
1. S. Delvaux and M. Van Barel, *Rank-deficient submatrices of Kronecker products of Fourier matrices*, KU Leuven Report TW 477, 15 November 2006; later published in *Linear Algebra and its Applications* 426 (2007), 349–367, DOI 10.1016/j.laa.2007.05.009.
2. A. Bonami and S. Ghobber, *Equality cases for the uncertainty principle in finite Abelian groups*, arXiv:1003.5060v1, 26 March 2010.
