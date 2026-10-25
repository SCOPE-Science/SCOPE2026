# A uniform diagonal trace-class gap in quadratic four-torus metric cotype

## Finding
For every integer \(n\ge 2\), the squared quadratic metric-cotype test constant at modulus four has the exact Hilbert-space value
\[
\mathfrak C_H(4,n)^2=\frac{2n}{1-3^{-n}},
\]
whereas the Schatten trace class satisfies the constructive bound
\[
\mathfrak C_{S_1}(4,n)^2\ge\frac{6n}{2-3^{1-n}}.
\]
The ratio between the displayed trace-class lower bound and the exact Hilbert value is
\[
\frac{3(1-3^{-n})}{2-3^{1-n}}>1,
\]
and tends to \(3/2\) as \(n\to\infty\). This is a dimension-uniform strict separation already witnessed in the diagonal \(2\times2\) matrices. The trace-class inequality is a lower bound, not a claim of optimality.

## Assumptions and scope
For a complex normed space \(X\), a positive integer \(n\), and a nonconstant function \(f:\mathbb Z_4^n\to X\), define
\[
L_X(f)=\sum_{j=1}^n \mathbb E_x\|f(x+2e_j)-f(x)\|_X^2,
\qquad
S_X(f)=\mathbb E_{x,\varepsilon}\|f(x+\varepsilon)-f(x)\|_X^2,
\]
where \(x\) is uniformly distributed on \(\mathbb Z_4^n\), and independently each coordinate \(\varepsilon_j\) is uniform on \(\{-1,0,1\}\); additions are modulo four. Set \(\mathfrak C_X(4,n)^2=\sup_{S_X(f)>0}L_X(f)/S_X(f)\). All averages use probability normalization. The Hilbert assertion is for every nonzero complex Hilbert space; the trace-class assertion uses finite-rank operators and therefore holds in any Schatten trace class containing the \(2\times2\) diagonal subspace.

## Proof
**Exact Hilbert constant.** Expand a Hilbert-valued map in the orthonormal characters \(\chi_k(x)=\exp(\pi i\sum_j k_jx_j/2)\), \(k\in\mathbb Z_4^n\). Parseval reduces the quotient to a ratio of nonnegative sums of mode energies. For one frequency, let \(r\) be its number of odd coordinates. Its numerator multiplier is \(4r\). Put \(\beta(0)=1\), \(\beta(1)=\beta(3)=1/3\), \(\beta(2)=-1/3\). The denominator multiplier is \(2(1-\prod_j\beta(k_j))\). For \(r\ge1\), \(\prod_j\beta(k_j)\le 3^{-r}\), and hence the quotient does not exceed \(2r/(1-3^{-r})\). The function \(t\mapsto t/(1-3^{-t})\) is strictly increasing for positive \(t\): its derivative is positive by \(3^t>1+t\log3\). If \(r=0\) the numerator vanishes. Therefore every quotient is at most \(2n/(1-3^{-n})\). Equality is realized by the nonconstant character with every frequency \(k_j=1\), times a fixed unit Hilbert vector.

**The trace-class witness.** Let \(u:\mathbb Z_4\to\{\pm1\}\) take the values \((1,1,-1,-1)\), and put \(v(t)=u(t+1)\). Define
\[
h(x)=\prod_{j=2}^n u(x_j),\qquad F_n(x)=\operatorname{diag}(u(x_1)h(x),v(x_1)h(x)).
\]
The trace norm of a diagonal matrix is the sum of its diagonal absolute values. A half-turn in any coordinate changes both diagonal signs, so its trace-norm distance is \(4\), making \(L_{S_1}(F_n)=16n\).

For \(\varepsilon_1=\pm1\), exactly one of the two signs \(u(x_1),v(x_1)\) changes (and multiplying one endpoint by the possibly changed common factor \(h\) merely swaps which sign changes), so the trace-norm distance is \(2\). This event has probability \(2/3\). If \(\varepsilon_1=0\), the distance is \(4\) exactly when the common factor \(h\) reverses sign, and otherwise zero. For every \(j\ge2\), the independent random sign \(u(x_j+\varepsilon_j)/u(x_j)\) is negative with probability \(1/3\); thus its product is negative with probability \((1-3^{-(n-1)})/2\). Consequently
\[
S_{S_1}(F_n)=\frac23\cdot4+\frac13\cdot16\cdot\frac{1-3^{-(n-1)}}2
=\frac{16}3-\frac8{3^n}.
\]
Dividing yields \(L/S=6n/(2-3^{1-n})\), as asserted.

**Separation.** The ratio of this witness quotient to the optimal Hilbert quotient is \(3(1-3^{-n})/(2-3^{1-n})\). The numerator exceeds the denominator because \(3-3^{1-n}-(2-3^{1-n})=1\). Its limit is \(3/2\). Every assertion follows.

## Verification
The standalone `VERIFY.py` enumerates all \(x\in\mathbb Z_4^n\) and increments \(\varepsilon\in\{-1,0,1\}^n\) for \(n=2,3,4\) using exact rational arithmetic. It checks the long/short energies and the Hilbert character maximum by Fourier multipliers. These finite checks corroborate, but do not replace, the proof for every integer \(n\ge2\).

## Relationship to prior work
Mendel and Naor, *Metric cotype* (2008), introduced the metric-cotype inequalities on discrete tori and treated the qualitative distinctions between target geometries. Jiao, Luo, and Wu, *The Sharp Scale Inequality for the Schatten Trace Class* (arXiv:2610.21445v1, first public 2026-10-15), establish contemporary scale bounds for trace-class metric cotype, rather than this explicit exact Hilbert comparator and uniform two-coordinate Gray witness. Cheng, Wang, and Xiang, *Sharp Metric Cotype Inequalities for L1 via Nonlinear Cut Smoothing* (arXiv:2609.08749), study the related quadratic torus problem for \(L_1\); only the abstract and metadata, not complete full text, were retrievable, leaving a material priority uncertainty. The one-coordinate Gray/cycle test is elementary and already appears in earlier literature; the asserted contribution concerns the common \(n\)-dimensional product construction and its exact quantitative separation for all \(n\ge2\).

## Limitations
No equality with the optimal Schatten trace-class constant is claimed. The full 2026 Cheng–Wang–Xiang source could not be inspected and might contain an equivalent stronger construction. Publication priority therefore remains subject to full-text comparison and independent expert review. The finite verification covers only three small dimensions; the all-dimensional assertion is proved analytically.

## References
1. M. Mendel and A. Naor, *Metric cotype*, Ann. of Math. 168 (2008), 247–298; DOI: 10.4007/annals.2008.168.247.
2. Jiao, Luo, and Wu, *The Sharp Scale Inequality for the Schatten Trace Class*, arXiv:2610.21445v1 (first public 2026-10-15).
3. Q. Cheng, Y. Wang, and B. Xiang, *Sharp Metric Cotype Inequalities for L1 via Nonlinear Cut Smoothing*, arXiv:2609.08749 (first public 2026-09-08).
