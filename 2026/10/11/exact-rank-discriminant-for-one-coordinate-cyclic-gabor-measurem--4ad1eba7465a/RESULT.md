# Exact rank discriminant for one-coordinate cyclic Gabor measurements

## Finding

For every integer \(n\ge3\) and complex parameter \(z\), consider the unit vector
\[
g_{n,z}=\frac{(z,1,\ldots,1)}{\sqrt{n-1+|z|^2}}\in\mathbb C^n.
\]
Let \(R_n(z)\) be the complex dimension of the operator span of the \(n^2\) rank-one projectors onto the full time-frequency orbit of \(g_{n,z}\). Define, for a residue \(r\) modulo \(n\),
\[
C_n(r)=\sum_{\substack{d\mid\gcd(n,r)\\d<n}}d\,\varphi(n/d)-(n-1)\mathbf1_{r=0},
\]
where \(\varphi\) is Euler's totient and the indicator \(r=0\) means zero modulo \(n\). For \(z\ne1\), define \(c(z)=-(z-1)/(\overline z-1)\). If \(c(z)\) is an \(n\)-th root of unity, let \(r_n(z)\) be the unique residue with \(c(z)=e^{2\pi i r_n(z)/n}\); otherwise leave \(r_n(z)\) undefined and set its contribution to zero.

Then the **exact rank in every dimension and at every complex parameter** is
\[
\boxed{R_n(1)=n,\qquad
R_n(z)=n^2-(n-1)\mathbf1_{|z|=1}-(n-1)\mathbf1_{2\operatorname{Re}z=-(n-2)}
-\begin{cases}C_n(r_n(z)),&r_n(z)\text{ is defined},\\0,&\text{otherwise},\end{cases}\quad z\ne1.}
\]
The formula remains valid at intersections of the exceptional loci: defects from the three disjoint types of time-frequency labels add. Consequently, completeness fails precisely along two explicitly specified real loci and the phase lines through \(z=1\) carrying positive \(C_n\) multiplicity. The nontrivial congruence profile distinguishes prime and composite dimensions. In particular, for every real \(t\ne0\),
\[
R_n(1+it)=n^2-C_n(0),\qquad R_n(1+it)=n^2\ \Longleftrightarrow\ n\text{ is prime}.
\]
A fixed Gaussian-rational parameter works uniformly: \(R_n(2+2i)=n^2\) for every \(n\ge3\). These consequences belong to the same rank-classification theorem, not separate claims.

## Assumptions and scope

The index set is the cyclic group \(\mathbb Z_n\), the Hilbert space is \(\mathbb C^n\) with its standard Hermitian inner product, and \(n\) ranges over **all** integers at least three, not merely primes. For \(a,b\in\mathbb Z_n\), define \((T_af)(x)=f(x-a)\) and \((M_bf)(x)=\omega^{bx}f(x)\), where \(\omega=e^{2\pi i/n}\). The projectors are \(P_{a,b}=|M_bT_ag_{n,z}\rangle\langle M_bT_ag_{n,z}|\). Their span is taken over \(\mathbb C\), in the \(n^2\)-dimensional matrix space \(M_n(\mathbb C)\); its dimension equals the rank of their Hilbert--Schmidt Gram matrix. The effects \(P_{a,b}/n\) sum to the identity, so this is a minimal-outcome Weyl--Heisenberg POVM, and it is informationally complete exactly when \(R_n(z)=n^2\).

No assumption is made that \(z\) is real, nonzero, generic, or of unit modulus. The special parameter \(z=1\) is stated separately because the phase ratio is undefined. The statement is about **linear operator tomography**, which is stronger than injectivity of pure-state phase retrieval alone.

## Proof

**Step 1: the projector rank is a zero count.** For any unit vector \(g\in\mathbb C^n\), its displaced projectors form a covariant operator frame. The Weyl matrices \(M_bT_a\) are an orthogonal basis of \(M_n(\mathbb C)\). Conjugation by a Weyl matrix multiplies each such basis element by a scalar character. Therefore the operator-frame map
\[
\mathcal S(X)=\sum_{a,b\in\mathbb Z_n}\operatorname{tr}(XP_{a,b})P_{a,b}
\]
is diagonal in the Weyl basis. Its eigenvalue in the Weyl direction labelled by \((a,b)\) is \(n|\langle g,M_bT_ag\rangle|^2\): indeed, the \(n^2\) squared coefficients of that basis element against the projectors are identical, while its squared Hilbert--Schmidt norm is \(n\). The synthesis map and its adjoint show that this operator-frame map and the \(n^2\)-by-\(n^2\) projector Gram matrix have the same spectrum, zeros included. Thus \(R_n(z)\) is exactly the number of nonzero Weyl ambiguity coefficients. This spectral identification is already known; the calculation below is the parameter-specific contribution.

**Step 2: exact ambiguity coefficients.** Put \(v=(z,1,\ldots,1)\), \(D=n-1+|z|^2>0\), and define an unnormalized correlation with a harmless relabeling of the Weyl indices,
\[
B(a,b)=\sum_{x\in\mathbb Z_n}v(x)\overline{v(x-a)}\omega^{bx}.
\]
Because \(B(a,b)/D=\overline{\langle g_{n,z},M_{-b}T_ag_{n,z}\rangle}\), it has precisely the same zero labels, up to reflection in the frequency coordinate. Directly separating the exceptional sites \(x=0\) and \(x=a\) gives
\[
B(a,b)=\begin{cases}
D,&a=b=0,\\
|z|^2-1,&a=0,\ b\ne0,\\
n-2+2\operatorname{Re}z,&a\ne0,\ b=0,\\
(z-1)+(\overline z-1)\omega^{ab},&a\ne0,\ b\ne0.
\end{cases}
\]
For example, in the last case the constant-vector contribution is \(\sum_x\omega^{bx}=0\), and the two exceptional positions contribute \(z-1\) and \((\overline z-1)\omega^{ab}\). The first, always-nonzero entry proves that there is no missing identity direction. The next two lines give precisely \(n-1\) zero labels each when, respectively, \(|z|=1\) or \(2\operatorname{Re}z=-(n-2)\).

**Step 3: mixed-label degeneracies and their number.** When \(z\ne1\), write \(\delta=z-1\). Because \(\delta\ne0\), the mixed coefficient vanishes if and only if
\[
\omega^{ab}=-\delta/\overline\delta=c(z).
\]
The right-hand side has modulus one. It is either no \(n\)-th root of unity, in which case no mixed label vanishes, or a unique root \(\omega^r\). In the latter case we must count pairs \((a,b)\) with \(1\le a,b<n\) and \(ab\equiv r\pmod n\). For fixed \(a\) put \(d=\gcd(a,n)\). That congruence has exactly \(d\) solutions \(b\bmod n\) when \(d\mid r\), and none otherwise. There are exactly \(\varphi(n/d)\) nonzero residues \(a\) with that gcd, for each proper divisor \(d<n\). This yields \(\sum_{d\mid\gcd(n,r),\,d<n}d\varphi(n/d)\); when \(r=0\), exactly one of the counted solutions for **each** \(a\) is \(b=0\), which must be excluded, subtracting \(n-1\). This proves the asserted formula for \(C_n(r)\), including every composite and zero-divisor case. The three categories of index pairs in Step 2 are disjoint, so their zero multiplicities add without any inclusion-exclusion correction, even where the parameter loci intersect. This proves the full rank formula for \(z\ne1\).

**Step 4: the degenerate center.** For \(z=1\), all entries of \(g\) are equal. Its cyclic translates are the same ray, and the \(n\) modulations give an orthogonal Fourier basis. The projectors therefore have exactly \(n\) distinct orthogonal rank-one directions, proving \(R_n(1)=n\).

**Step 5: exact arithmetic consequences.** If \(z=1+it\), \(t\ne0\) is real, then \(|z|>1\), \(2\operatorname{Re}z=2>-(n-2)\), and \(c(z)=1\). The formula reduces to \(R_n(1+it)=n^2-C_n(0)\). But also
\[
C_n(0)=\sum_{a=1}^{n-1}(\gcd(a,n)-1).
\]
Every summand vanishes exactly when every nonzero residue is coprime to \(n\), which is equivalent to primality for \(n\ge3\).

Finally, at \(z=2+2i\) one has \(|z|^2=8\), \(2\operatorname{Re}z=4\), and
\[
c(z)=\frac{3-4i}{5},\qquad c(z)+c(z)^{-1}=\frac65.
\]
If this \(c(z)\) were a root of unity, both it and its inverse would be algebraic integers, so their sum would be a rational algebraic integer and hence an integer, contrary to \(6/5\). Therefore all mixed coefficients are nonzero, as are the axis coefficients; thus \(R_n(2+2i)=n^2\) for every \(n\ge3\). This finishes the proof.

## Verification

The accompanying `CHECK.py` uses only the Python standard library. Run `python3 CHECK.py` in the directory containing this file to compare the closed rank formula against directly constructed \(n^2\)-by-\(n^2\) matrices of vectorized rank-one projectors and independent complex Gaussian elimination, for each \(3\le n\le10\) at six specified complex parameters. It also checks the divisor count against every pair of nonzero residues for every residue \(r\in\mathbb Z_n\) in these dimensions. The performed run returned `PASS: 48 direct projector-span ranks and 52 congruence counts` and the stated primality/universal-seed checks. Those finite calculations are corroboration; the proof above establishes the result for unbounded \(n\) and all complex \(z\).

## Relationship to prior work

Goldberger--Kang--Okoudjou [1] prove the general Weyl-ambiguity criterion for informational completeness and classify several sparse-support rank patterns. Their Theorems 1--2 directly justify the spectral starting point of Step 1, but do **not** state this exact full-parameter, one-defect rank discriminant or its divisor-counted exceptional multiplicities. Bojarovska--Flinth [2] establish related Gabor phase-retrieval criteria and constructions but not this operator-span classification. Zhu--Wang [3] give explicit arbitrary-dimensional Weyl--Heisenberg informationally complete constructions and analyze, among others, the \(z=0\) odd-dimensional member (Appendix D) and the general real-fiducial even-dimensional obstruction; these previously known special cases are **not claimed as separate novel results here**. The distinction is the exact complex-parameter rank function simultaneously covering all dimensions, including composite-modulus zero-divisor multiplicities. The general ambiguity criterion alone is insufficient to supply the displayed closed divisor formula without the computation in Steps 2--3.

The closest published related calculations for two-sparse Gabor windows give operator-span capacity under a different, sparse-window hypothesis; they do not treat this near-constant, usually full-support, single-window family. No claim of priority beyond the checked sources is made.

## Limitations

The result is restricted to cyclic Weyl--Heisenberg orbits of the stated one-coordinate family; it does not classify arbitrary windows or projectors from other groups. Informational completeness is a linear rank assertion and does not itself guarantee uniform conditioning, SIC equiangularity, or robustness to noise. The finite numerical checks do not constitute a proof for all dimensions. Although the principal relevant papers and indexed records were compared, equivalent results in unindexed literature cannot be ruled out. Independent external validation has not been performed.

## References

[1] A. Goldberger, S. Kang, and K. A. Okoudjou, *Towards a classification of incomplete Gabor POVMs in* \(\mathbb C^d\), arXiv:2106.01509v1 (2021), Theorems 1--2 and Section 3.

[2] I. Bojarovska and A. Flinth, *Phase Retrieval from Gabor Measurements*, arXiv:1503.05800v2 (2015), Sections 2.2--2.4.

[3] X. Zhu and Y. Wang, *Uniformly Stable Minimal Weyl--Heisenberg Measurements Approaching the SIC Benchmark*, arXiv:2608.11850v1 (2026), Sections II--III and Appendix D.
