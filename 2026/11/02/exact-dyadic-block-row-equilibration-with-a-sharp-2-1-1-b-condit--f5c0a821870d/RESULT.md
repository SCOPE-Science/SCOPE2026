# Exact dyadic block-row equilibration with a sharp \(2^{1-1/b}\) condition-number barrier

## Finding

Let \(M\in\mathbb R^{n\times n}\) be nonsingular, and let \(\mathcal I_1,\ldots,\mathcal I_b\) be a prescribed partition of its rows into \(b\ge1\) nonempty blocks. Set
\[
\alpha_q=\max_{i\in\mathcal I_q}\sum_{j=1}^n |M_{ij}|>0,
\qquad C_{\ell q}=\sum_{i\in\mathcal I_q}|(M^{-1})_{\ell i}|.
\]
For an integer exponent vector \(k\in\mathbb Z^b\), let \(D(k)\) have diagonal value \(2^{k_q}\) on block \(\mathcal I_q\). Write
\[
K_2=\min_{k\in\mathbb Z^b}\kappa_\infty(D(k)M),
\qquad K_*=\min_{d_1,\ldots,d_b>0}\kappa_\infty(D(d)M).
\]
The continuous optimum, which is an instance of classical row equilibration, is
\[
K_*=\max_{1\le\ell\le n}\sum_{q=1}^b \alpha_q C_{\ell q}.
\]
Define exactly \(b\) candidate exponent vectors by
\[
k_q^{(s)}=\max\{k\in\mathbb Z:2^k\alpha_q\le\alpha_s\},
\qquad 1\le q,s\le b.
\]
Then the **exact discrete optimum over all unbounded binary exponents** is
\[
\boxed{K_2=\min_{1\le s\le b}\left(\alpha_s\max_{1\le\ell\le n}
\sum_{q=1}^b2^{-k_q^{(s)}}C_{\ell q}\right).}
\]
Moreover the **sharp block-count loss** relative to continuous row equilibration is
\[
\boxed{1\le\frac{K_2}{K_*}\le2^{1-1/b}.}
\]
The upper bound is attained for each integer \(b\ge1\), every choice of positive block sizes, and the block-diagonal matrix
\[
M=\operatorname{diag}\bigl(I_{n_1},2^{1/b}I_{n_2},\ldots,
2^{(b-1)/b}I_{n_b}\bigr).
\]
Thus a single scalar block incurs no quantization penalty; for two blocks the worst factor is \(\sqrt2\), and as the number of blocks grows the optimal universal factor increases to \(2\) from below.

## Assumptions and scope

All matrices and condition numbers are exact real-arithmetic objects; \(\kappa_\infty(X)=\|X\|_\infty\|X^{-1}\|_\infty\). The block partition is fixed. Only **left** scalings by positive powers of two, constant on each block, are optimized; no column scaling or finite exponent range is allowed. The matrix is square and nonsingular, so every block maximum \(\alpha_q\) is positive. All claims are for arbitrary such matrices and all integers \(b\) with \(1\le b\le n\).

The discrete optimizer is determined by at most \(b\) explicit candidates, requiring no search over exponent vectors. Computing the formula uses the absolute row sums of \(M^{-1}\), not only the row norms of \(M\); it does not thereby promise a matrix-free practical implementation. The same mathematics works for any exact positive radix \(r>1\), with \(r\) replacing \(2\) throughout and sharp factor \(r^{1-1/b}\).

## Proof

**1. Objective reduction.** For a positive block scaling with block values \(d_q\), the infinity norms are
\[
\|D(d)M\|_\infty=\max_qd_q\alpha_q,
\quad
\|(D(d)M)^{-1}\|_\infty=
\max_\ell\sum_{q=1}^b\frac{C_{\ell q}}{d_q}.
\tag{1}
\]
The second identity uses \((DM)^{-1}=M^{-1}D^{-1}\). Set \(T=\max_qd_q\alpha_q\). Since \(d_q\le T/\alpha_q\), equation (1) implies
\[
\kappa_\infty(D(d)M)\ge\max_\ell\sum_q\alpha_q C_{\ell q}.
\]
Equality holds at \(d_q=1/\alpha_q\), proving the expression for \(K_*\).

**2. Exact finite discrete candidate reduction.** Fix any integer exponent vector \(k\), and select a block \(s\) achieving \(\max_q2^{k_q}\alpha_q\). Multiplying all block scales by the common power \(2^{-k_s}\) leaves the condition number invariant; hence assume \(k_s=0\), and then the maximal scaled block-row norm equals \(\alpha_s\). Every other coordinate satisfies \(2^{k_q}\alpha_q\le\alpha_s\), equivalently \(k_q\le k_q^{(s)}\). Increasing those exponents to \(k_q^{(s)}\) leaves the forward norm at \(\alpha_s\) and can only decrease the inverse norm in (1). Thus \(D(k^{(s)})\) is no worse than \(D(k)\). Conversely every candidate is admissible, so minimizing over the \(b\) candidates gives the exact integer optimum. Notice \(k_s^{(s)}=0\), fixing the normalization unambiguously.

**3. Universal upper bound.** On the unit circle, consider the \(b\) fractional parts of \(\log_2\alpha_1,\ldots,\log_2\alpha_b\), in circular order with repetitions. The \(b\) successive circular gaps sum to one, so some gap has length \(\Delta\ge1/b\). Cut the circle inside that largest gap. By adding suitable integers to the original logarithms, all lifted numbers \(\log_2(2^{k_q}\alpha_q)\) can be placed in a closed real interval of length \(1-\Delta\le1-1/b\). Consequently, with \(u_q=2^{k_q}\alpha_q\),
\[
\frac{U}{u}:=\frac{\max_qu_q}{\min_qu_q}\le2^{1-1/b}.
\]
Using (1) and \(d_q=u_q/\alpha_q\) gives
\[
\kappa_\infty(DM)
=U\max_\ell\sum_q\frac{\alpha_q C_{\ell q}}{u_q}
\le\frac{U}{u}\max_\ell\sum_q\alpha_q C_{\ell q}
\le2^{1-1/b}K_*.
\]
As \(K_2\le\kappa_\infty(DM)\) for this integer scaling, the desired inequality follows. The lower inequality holds because dyadic scalings form a subset of positive real scalings.

**4. Sharpness for every block count.** Choose the stated diagonal blocks with scalar coefficients \(\alpha_q=2^{(q-1)/b}\). For any dyadic scaling, the matrix and its inverse remain block diagonal, whence
\[
\kappa_\infty(DM)=\frac{\max_q2^{k_q}\alpha_q}{\min_q2^{k_q}\alpha_q}.
\]
The fractional logarithms of the \(b\) scaled block norms are exactly the equally spaced residues \(0,1/b,\ldots,(b-1)/b\), independent of integer exponents. Any real interval containing a representative of each residue has length at least \(1-1/b\): its omitted circular arc can contain at most one of the gaps between successive residues, and those gaps all have length \(1/b\). Therefore every admissible dyadic scaling has condition number at least \(2^{1-1/b}\). The candidate scaling in step 3 achieves equality. Meanwhile the continuous choice \(d_q=1/\alpha_q\) makes the matrix the identity and yields \(K_*=1\). This proves sharpness, including \(b=1\).

## Verification

The supplied standalone `check_scaling.py` uses only Python's standard library. It computes exact rational inverses by Gauss–Jordan elimination, forms the \(b\) candidates using integer comparisons rather than floating-point logarithms, and verifies equality of the candidate optimum with exhaustive bounded-exponent searches after quotienting by common shifts. It passed 168 nonsingular random rational instances (dimensions two through four), comparing 19,558 exponent vectors, plus nine numerical diagonal sharpness examples. The exact rational tests also check \(K_*\le K_2\le2^{1-1/b}K_*\). The proof above, not the finite checker, establishes the unbounded-exponent theorem and its all-dimension sharpness.

To reproduce, run `python3 check_scaling.py` in a directory containing that file. No input files or third-party packages are required.

## Relationship to prior work

The October 5, 2026 preprint by Lindquist, Appelhans, Jackson and Derlaga, *A Mixed-Precision Model for Matrix-Splitting Methods*, Corollary 2, explicitly permits power-of-two scalings constant on block rows and includes \(\kappa_\infty(DM)\) in its rounding-error bounds. It does not give the finite-candidate global minimization or a sharp penalty relative to unrestricted real scalings. The present result optimizes only that **one condition-number factor**, not the full error bound, which also contains other scaling-dependent factors.

Classical matrix equilibration and optimal norm scaling, including Bauer's and van der Sluis's work and Rump's 2003 continuous two-sided treatment, already encompass the continuous optimum as background; the continuous formula is not claimed as a novel general principle. LAPACK's `xGEEQUB` routines implement power-of-radix row and column scaling heuristics and explicitly do not guarantee condition-number minimization. The theorem here instead supplies a global optimum under a prescribed one-sided block-row restriction, together with an attained sharp worst-case loss. Shapiro's 1985 work concerns optimal block diagonal Euclidean-norm scaling and provides related background, not an identified dyadic infinity-norm formula.

## Limitations

The exponent set is all integers, so exponent overflow, underflow, subnormal values, finite-precision evaluation of row norms, and approximate inverses are outside scope. Only the left-scaled infinity condition number is minimized. Choosing this scaling need not minimize the original mixed-precision paper's entire iteration-error estimate or its pseudo-condition-number terms. The sharpness example uses exact real powers and does not imply that the bound is attained by matrices with finite binary floating-point entries. The relationship to older scaling folklore is a historical-priority uncertainty; a complete proof of uniqueness in the literature is not asserted.

## References

- N. Lindquist, D. Appelhans, C. W. Jackson and J. M. Derlaga, *A Mixed-Precision Model for Matrix-Splitting Methods*, arXiv:2610.06414v1 (publicly submitted 2026-10-05), especially Section 2, Corollary 2. https://arxiv.org/html/2610.06414v1
- S. M. Rump, *Optimal scaling for p-norms and componentwise distance to singularity*, IMA J. Numer. Anal. **23** (2003), 1–9. https://doi.org/10.1093/imanum/23.1.1
- A. Shapiro, *Optimal Block Diagonal \(l_2\)-Scaling of Matrices*, SIAM J. Numer. Anal. **22** (1985), 81–94. https://doi.org/10.1137/0722005
- LAPACK, *DGEEQUB: matrix equilibration with power-of-radix factors*, routine documentation. https://manpages.ubuntu.com/manpages/stonking/man3/geequb.3.html
- A. van der Sluis, *Condition numbers and equilibration of matrices*, Numer. Math. **14** (1969), 14–23. https://doi.org/10.1007/BF02165096
