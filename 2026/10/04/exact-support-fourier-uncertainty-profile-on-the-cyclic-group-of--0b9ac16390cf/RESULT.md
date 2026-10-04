# Exact-support Fourier uncertainty profile on the cyclic group of order twelve
## Finding
For a nonzero function \(f:\mathbb Z_{12}\to\mathbb C\), define
\[
\mu_{12}(k)=\min\bigl\{|\operatorname{supp}(\widehat f)|:|\operatorname{supp}(f)|=k\bigr\}.
\]
Then
\[
(\mu_{12}(1),\ldots,\mu_{12}(12))=(12,6,4,3,4,2,4,2,2,2,2,1).
\]
The exact-support minimum is therefore nonmonotone: it rises from \(3\) to \(4\) between \(k=4\) and \(k=5\), and from \(2\) to \(4\) between \(k=6\) and \(k=7\).

For comparison, the usual Meshulam/Delvaux--Van Barel profile allowing \(|\operatorname{supp}(f)|\le k\) is
\[
(12,6,4,3,3,2,2,2,2,2,2,1).
\]
Thus exact-support penalties occur precisely at \(k=5\) and \(k=7\).

## Assumptions and scope
Use the unnormalized discrete Fourier transform
\[
\widehat f(r)=\sum_{x\in\mathbb Z_{12}}f(x)\zeta_{12}^{rx},\qquad \zeta_{12}=e^{2\pi i/12}.
\]
Support cardinality is unchanged by the normalization convention. The claim concerns exact support size, not the standard monotone quantity obtained by permitting smaller supports.

## Proof
Meshulam's divisor-interpolation theorem gives a lower bound for Fourier support at every support size. Delvaux and Van Barel characterize the associated monotone Hamming number \(H_{F_n}(k)\), defined using time support of size at most \(k\). Their theorem gives
\[
H_{F_{12}}(k)=(12,6,4,3,3,2,2,2,2,2,2,1).
\]
Hence \(\mu_{12}(k)\ge H_{F_{12}}(k)\).

Explicit cyclotomic witnesses attain this lower bound for all \(k\) except \(5\) and \(7\). For \(k=5\), one witness has time support \(\{0,2,4,6,8\}\) and Fourier support \(\{4,5,10,11\}\). For \(k=7\), one witness has time support \(\{0,1,2,5,6,8,9\}\) and Fourier support \(\{6,8,9,11\}\). The supplied verifier contains and checks the exact coefficients.

It remains to exclude Fourier support of size at most \(3\) for exact time-support sizes \(5\) and \(7\). For \(S\subset\mathbb Z_{12}\) and a nine-point Fourier-zero set \(Z\subset\mathbb Z_{12}\), let
\[
A_{Z,S}=(\zeta_{12}^{rs})_{r\in Z,\ s\in S}.
\]
A function with exact support \(S\) and zeros on \(Z\) exists exactly when \(\ker A_{Z,S}\) contains a vector with every coordinate nonzero. Over \(\mathbb C\), such a vector exists exactly when no coordinate functional vanishes identically on the kernel.

The verifier exhausts \(\binom{12}{5}\binom{12}{9}=174240\) pairs for \(k=5\), and the same number for \(k=7\). It first uses reductions modulo \(13\), \(37\), and \(61\), each with a primitive twelfth root, solely to certify full column rank. Only \(96\) pairs remain for \(k=5\) and \(1680\) for \(k=7\). These are resolved exactly in \(\mathbb Q[\zeta_{12}]=\mathbb Q[z]/(z^4-z^2+1)\). Every remaining \(k=5\) matrix has rank \(4\), every remaining \(k=7\) matrix has rank \(6\), and each one-dimensional kernel has at least one coordinate identically zero. Thus exact support \(5\) or \(7\) cannot coexist with Fourier support at most \(3\), proving the table.

## Verification
Run `python verify_z12_exact_support.py`. The script uses only the Python standard library. It checks all twelve witnesses, reconstructs the monotone Hamming profile from the published characterization, and performs the complete \(348480\)-pair obstruction census. Successful replay ends with `VERIFY_OK`.

## Relationship to prior work
Meshulam proved the divisor-interpolation lower bound for finite abelian groups. Delvaux and Van Barel characterized the monotone Hamming number with the explicit constraint that time support have size at most \(k\); that result does not determine the equality-constrained profile above.

Bonami and Ghobber explicitly distinguish exact-support equality cases from Meshulam's monotone function. Their complete classifications cover \(\mathbb Z_p\times\mathbb Z_p\), \(\mathbb Z_{p^2}\), and \(\mathbb Z_p\times\mathbb Z_q\) for distinct primes. They do not give the mixed group \(\mathbb Z_4\times\mathbb Z_3\cong\mathbb Z_{12}\) profile above. The present result supplies that complete twelve-point exact-support profile and identifies its two strict penalties.

## Limitations
This is a finite classification only for \(\mathbb Z_{12}\). It does not provide a general formula for exact-support uncertainty at arbitrary composite orders. Targeted searches found no source stating this exact table, but search failure is not proof that no differently phrased prior result exists.

## References
1. R. Meshulam, *An uncertainty inequality for finite abelian groups*, arXiv:math/0312407, first posted 2003-12-22.
2. S. Delvaux and M. Van Barel, *Rank-deficient submatrices of Kronecker products of Fourier matrices*, Report TW 477, K.U. Leuven, November 2006; Linear Algebra Appl. 426 (2007), 349--367.
3. A. Bonami and S. Ghobber, *Equality cases for the uncertainty principle in finite Abelian groups*, arXiv:1003.5060, first posted 2010-03-26; Acta Sci. Math. (Szeged) 79 (2013), 507--528.
