# A nondegenerate Abelian-square factor-count law for binary words with two ones

## Finding

Let \(W_n\) be uniformly sampled from the \(\binom n2\) binary words of length \(n\ge2\) containing exactly two ones. Let \(S(w)\) count **distinct, literal, nonempty contiguous factors** of \(w\) that are Abelian squares (their two equal-length halves have the same numbers of zeros and ones). Define the positive-part operation \(t_+=\max(t,0)\), and for nonnegative \(p,q,r\) with \(p+q+r=1\), put

\[
\mathcal A(p,q,r)=pr-\frac12(p-q)_+^2-\frac12(r-q)_+^2
+\frac12(p-q-r)_+^2+\frac12(r-q-p)_+^2.
\]

If \((P,Q,R)\) is uniform on the two-dimensional simplex \(\{(p,q,r):p,q,r\ge0,\ p+q+r=1\}\) (equivalently, Dirichlet with all three parameters equal to one), then

\[
\boxed{\frac{S(W_n)}{n^2}\xrightarrow{\mathrm d}\mathcal L
:=\frac12\mathcal A(P,Q,R).}
\]

The limit is not a constant, and its first two moments are exact:

\[
\boxed{\mathbb E\mathcal L=\frac1{48},\qquad
\mathbb E\mathcal L^2=\frac5{6912},\qquad
\operatorname{Var}(\mathcal L)=\frac1{3456}.}
\]

The first two moments of \(S(W_n)/n^2\) converge to the displayed moments. Thus random sparse words retain order-\(n^2\) absolute fluctuations in distinct Abelian-square factor counts; this differs from a concentration-to-a-single-constant conclusion.

## Assumptions and scope

Every relevant word is uniquely of the form \(w=0^a1\,0^b1\,0^c\), with \(a,b,c\ge0\) and \(a+b+c=n-2\). Distinctness refers to literal binary factors: two occurrences of the same string count once. The random model is uniform at *fixed Hamming weight two*, not a Bernoulli or unrestricted random-string model. The statement holds along all positive integers \(n\to\infty\); the finite count formula below includes boundary gaps of length zero.

For \(a,b,c\ge0\), write \(T(a,b,c)\) for the number of distinct Abelian-square factors containing both ones. Then

\[
T(a,b,c)=\sum_{u=0}^a\sum_{v=0}^c
\mathbf1\{\lvert u-v\rvert\le b,\ u+v+b\equiv0\pmod2\},
\qquad
S(w)=T(a,b,c)+\left\lfloor\frac{\max(a,b,c)}2\right\rfloor.
\]

## Proof

**Factor classification.** An Abelian square has an even number of ones. Since the ambient word contains only two, a relevant factor has either zero or two ones. The zero-one-free Abelian squares are precisely \(0^{2},0^4,\ldots,0^{2\lfloor\max(a,b,c)/2\rfloor}\). Any factor containing both ones has the unique representation \(0^u1\,0^b1\,0^v\), with \(0\le u\le a\) and \(0\le v\le c\). Its midpoint separates the two ones exactly when its length is even and the two inequalities \(\lvert u-v\rvert\le b\) hold. This yields the finite formula above. Each such factor has a unique occurrence, since both occurrences of the letter one must lie inside it.

**Uniform lattice-to-area comparison.** Put \(N=n-2\) and \((p,q,r)=(a/N,b/N,c/N)\) when \(N>0\). The associated continuous strip area is

\[
\mathcal A(p,q,r)=\int_0^p\!\int_0^r
\mathbf1_{\{\lvert u-v\rvert\le q\}}\,dv\,du.
\]

For each integer \(u\), the permitted integers \(v\) are an interval, and exactly one parity is selected. The count of this parity differs from half the interval's lattice-point count by at most one. Summing over \(u\), then comparing the strip's integer cross-sections to their continuous lengths, gives the **uniform** estimate

\[
\left\lvert T(a,b,c)-\frac{N^2}{2}\mathcal A\left(\frac aN,\frac bN,\frac cN\right)\right\rvert\le C(N+1)
\]

for an absolute constant \(C\). The zero-only count is at most \(n/2\). The strip-area closed formula in the finding follows by subtracting the two triangular regions where \(u-v>q\) and \(v-u>q\), with corrections where those triangles extend beyond the rectangle.

**Weak limit and moments.** The \(\binom n2\) equally likely gap triples are precisely all weak compositions of \(N\) into three parts, and their rescalings converge to the uniform area distribution on the simplex. Continuity of \(\mathcal A\) and the uniform \(O(n)\) count error prove the stated convergence in distribution. The normalized count is uniformly bounded, so its first and second moments converge as well.

For an exact evaluation of the limiting moments, eliminate \(q=1-p-r\) and restrict by symmetry to \(p\le r\). In the following table, use \(x=p\), \(z=r\), \(y=1-x-z\),
\[
B_0=xz,\quad B_1=B_0-\tfrac12(z-y)^2,\quad
B_2=B_1-\tfrac12(x-y)^2,\quad H=\tfrac12(2z-1)^2.
\]

| Range for \(z\) | Range for \(x\) | \(\mathcal A\) on this region |
|---|---|---|
| \([0,1/3]\) | \([0,z]\) | \(B_0\) |
| \([1/3,1/2]\) | \([0,1-2z]\) | \(B_0\) |
| \([1/3,1/2]\) | \([1-2z,(1-z)/2]\) | \(B_1\) |
| \([1/3,1/2]\) | \([(1-z)/2,z]\) | \(B_2\) |
| \([1/2,1]\) | \([0,(1-z)/2]\) | \(B_1+H\) |
| \([1/2,1]\) | \([(1-z)/2,1-z]\) | \(B_2+H\) |

These six regions partition the half-simplex, except for boundaries of zero area. The uniform simplex density is two, and reflection across \(x=z\) doubles the integral once more. Direct polynomial integration, with the exact-rational replay in `moment_certificate.py`, yields

\[
\mathbb E[\mathcal A(P,Q,R)]=4\sum_{j=1}^6\iint_{D_j}\mathcal A\,dx\,dz=\frac1{24},
\qquad
\mathbb E[\mathcal A(P,Q,R)^2]=4\sum_{j=1}^6\iint_{D_j}\mathcal A^2\,dx\,dz=\frac5{1728}.
\]

Dividing by two for \(\mathcal L\) gives the claimed mean and second moment; subtracting the squared mean gives \(1/3456\), which is strictly positive.

**Finite first-moment cross-check.** For each half-length \(\ell\), an Abelian square containing both ones has one marked position in each half, giving \(\ell^2\) patterns. The containing length-\(n\) word is determined by the factor placement, of which there are \(n-2\ell+1\). As every two-one factor has a unique placement in any two-one word,

\[
\sum_{\lvert w\rvert=n,\ \lvert w\rvert_1=2}T(w)
=\sum_{\ell=1}^{\lfloor n/2\rfloor}\ell^2(n-2\ell+1).
\]

For \(n=2m\) this sum equals \(m(m+1)(m^2+m+1)/6\); for \(n=2m+1\), it equals \(m(m+1)^2(m+2)/6\). Division by \(\binom n2 n^2\) independently recovers the limiting mean \(1/48\). This identity is a verification check, not an alternative proof of the variance.

## Verification

Run `python3 verify.py` to compare the exact factor formula against independent literal-substring enumeration for every length from 2 through 33, together with 2,500 longer random examples and parity-diagonal-strip counts. Run `python3 moment_certificate.py` for a standard-library-only, exact-rational integration of all six polynomial regions and the final moment identities. Both scripts require no third-party packages. Their finite checks corroborate the unrestricted statements; the infinite conclusion uses the proof and the rational integral identities above.

## Relationship to prior work

The earlier general bound that binary words can contain quadratically many distinct Abelian squares includes a two-marker construction; it does **not** provide this uniform fixed-weight-two limit distribution or its variance. A deterministic sharp leading constant and strip count for five-run words were also previously available and are **not claimed as new** here. Work on algorithmic detection of Abelian periods and on Abelian-square-rich infinite words studies different sampling questions. The novelty asserted here is the specified *distributional law and its exact nonzero fluctuation constant*, conditional on exactly two ones.

## Limitations

The model excludes words with any other number of ones; no assertion is made for iid Bernoulli words, for arbitrary fixed density or for longer Abelian powers. The limit distribution is given as an explicit pushforward of a Dirichlet law, rather than a piecewise elementary formula for its cumulative distribution function. The scientific priority comparison is based on the cited accessible literature and may miss an unindexed equivalent derivation. No independent mathematical validation has been performed.

## References

- M. Crochemore et al., *A Note on Efficient Computation of All Abelian Periods in a String* (first public arXiv version, 2012-08-16), https://arxiv.org/abs/1208.3313.
- T. Kociumaka, J. Radoszewski, W. Rytter, T. Waleń, *Maximum Number of Distinct and Nonequivalent Nonstandard Squares in a Word*, DLT 2014, pp. 215–226, https://mimuw.edu.pl/~kociumaka/assets/pdf/files/dlt2014.pdf.
- T. Kociumaka, J. Radoszewski, W. Rytter, *Fast Algorithms for Abelian Periods in Words and Greatest Common Divisor Queries*, STACS 2013, https://doi.org/10.4230/LIPIcs.STACS.2013.245.
- G. Fici, F. Mignosi, J. Shallit, *Abelian-Square-Rich Words*, arXiv first public version 2017-01-04, https://arxiv.org/abs/1701.00948.
