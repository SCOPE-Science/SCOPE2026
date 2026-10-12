# Exact correction of the spectral relaxation behind a geometric-discord negativity threshold

## Finding

Rana and Parashar study the proposed inequality between normalized Hilbert--Schmidt geometric discord and squared negativity for \(2\otimes3\) states. In Section III they reduce part of the discussion to an eigenvalue relaxation and use the auxiliary optimization
\[
g(x,y)=\sum_{i=1}^n(x_i^2-x_i y_i),\qquad x_i,y_i\ge0,
\]
under the fixed-sum constraints \(\sum_i x_i=a\) and \(\sum_i y_i=b\). The paper states that the minimum occurs at equal coordinates \(x_i=a/n\) and \(y_i=b/n\).

The exact minimum is instead
\[
G_n(a,b)=
\begin{cases}
\dfrac{4a^2-4ab-(n-1)b^2}{4n},&0\le b\le2a,\\[4pt]
a(a-b),&b\ge2a.
\end{cases}
\]
For \(0<b\le2a\), the paper's equal-coordinate value is
\[
\frac{a^2-ab}n,
\]
and exceeds the true minimum by
\[
\frac{(n-1)b^2}{4n}>0.
\]

This matters directly for the displayed spectral relaxation used in the paper. For every \(0<N\le1\), define
\[
\lambda=(1,N/6,N/6,N/6,-N/4,-N/4),\qquad
\xi=(1,0,0,0,0,0).
\]
These spectra obey the paper's ordering assumptions and satisfy
\[
|\lambda_5|+|\lambda_6|=N/2,
\qquad
\sum_{i=1}^4\lambda_i=1+N/2,
\qquad
\sum_{i=1}^6\xi_i=1,
\]
as well as its Eq. (9), in fact with equality:
\[
\sum_{i=1}^6\xi_i^2=1=\sum_{i=1}^6\lambda_i\xi_i.
\]
Nevertheless the right-hand side of Eq. (12) becomes
\[
\sum_{i=1}^6(\lambda_i^2-\lambda_i\xi_i)-\frac{N^2}2
=-\frac{7N^2}{24}.
\]
The claimed subsequent lower bound is
\[
\frac{N(2-5N)}{16},
\]
and the difference between the displayed Eq. (12) value and that claimed bound is
\[
\frac{N(N-6)}{48}<0
\]
throughout \(0<N\le1\). Hence the asserted \(N=2/5\) threshold does not follow from the paper's displayed spectral relaxation. In fact this relaxation already permits a negative Eq. (12) objective for every positive \(N\) in the witness range.

## Assumptions and scope

The auxiliary optimization is purely finite-dimensional: \(n\ge2\), \(a,b\ge0\), and all coordinates are real and nonnegative. The spectral witness addresses exactly the necessary eigenvalue constraints displayed in Section III of Rana--Parashar. It is not asserted that every displayed pair \((\lambda,\xi)\) is realized by a physical state and its optimal classical--quantum approximation; the source itself warns that its spectral constraints are only a subset of necessary conditions.

The result therefore corrects the relaxation argument and the quantitative \(2/5\) heuristic, not the paper's independent numerical or explicit physical counterexamples. It also does not reinstate the geometric-discord-versus-negativity conjecture, which the paper and later literature disprove by genuine states.

## Proof

Fix \(x\). Because \(y_i\ge0\) and \(\sum_i y_i=b\), maximizing \(x\cdot y\) places all \(y\)-mass on an index attaining \(M=\max_i x_i\). Thus
\[
\min_y g(x,y)=\sum_i x_i^2-bM.
\]
Now fix \(M\in[a/n,a]\) and relabel so \(x_1=M\). Among the remaining \(n-1\) nonnegative coordinates with sum \(a-M\), convexity of the square gives the smallest squared norm when they are equal. This is feasible because \((a-M)/(n-1)\le M\) exactly when \(M\ge a/n\). Hence the problem reduces to
\[
\phi(M)=M^2+\frac{(a-M)^2}{n-1}-bM,
\qquad \frac an\le M\le a.
\]
This is strictly convex and has stationary point
\[
M_0=\frac{2a+(n-1)b}{2n}.
\]
If \(0\le b\le2a\), then \(M_0\le a\), so substitution yields
\[
\phi(M_0)=\frac{4a^2-4ab-(n-1)b^2}{4n}.
\]
A minimizer is, up to permutation,
\[
x_1=M_0,
\qquad
x_2=\cdots=x_n=\frac{2a-b}{2n},
\qquad
y_1=b,
\qquad
y_2=\cdots=y_n=0.
\]
If \(b\ge2a\), then the stationary point lies at or beyond the right endpoint, so convexity forces the minimum at \(M=a\), giving \(a(a-b)\), attained by \(x=(a,0,\ldots,0)\) and \(y=(b,0,\ldots,0)\).

The six-eigenvalue witness is checked by direct substitution. The ordering holds for \(0<N\le1\), all three fixed-sum constraints hold exactly, and Eq. (9) is saturated. Its Eq. (12) objective is
\[
3\frac{N^2}{36}+2\frac{N^2}{16}-\frac{N^2}2=-\frac{7N^2}{24}.
\]
Subtracting the claimed lower bound gives \(N(N-6)/48\), which is strictly negative on the stated interval.

## Verification

The standalone script `verify_relaxation.py` uses exact rational arithmetic. It verifies the displayed spectral constraints for rational test values of \(N\), reconstructs the Eq. (12) objective exactly, checks its polynomial identity \(-7N^2/24\), and checks the difference \(N(N-6)/48\) from the paper's claimed bound. The analytic minimization above, rather than finite sampling, proves the all-parameter statement.

The source text was checked at the point where Eqs. (7)--(12) and the Lagrange-multiplier assertion occur. The first public version is arXiv:1207.5523v1, dated 2012-07-23. MSC2020 code 81P43 is specifically “Quantum discord,” placing the finding in quantum theory.

## Relationship to prior work

Rana and Parashar are the direct source of the relaxation and the \(2/5\) heuristic. Their paper goes on to give actual counterexamples to the geometric-discord lower-bound conjecture, so those counterexamples do not depend on the corrected simplex statement.

Bag, Dey, and Osaka later give analytic families of \(2\otimes3\) counterexamples and bounds for the difference between squared negativity and geometric discord. Their abstract treats the physical-state comparison, not the simplex minimization or the correction of the Section III threshold argument. Targeted searches for the Lagrange step, the \(2/5\) threshold, exact aliases of the objective, and correction/erratum language did not locate a published statement equivalent to the exact simplex minimum plus the all-\(N\) spectral witness above.

## Limitations

The spectra used to invalidate the relaxed lower-bound chain are not claimed to be spectra of a realizable state/optimal-classical-state pair. That is unnecessary for the stated correction because the source's derivation purports to follow from the displayed relaxed constraints alone. The result does not classify physical states by negativity, does not compute geometric discord for a new family, and does not challenge the source's explicit physical counterexamples.

The literature search cannot exclude an obscure or poorly indexed correction. A later paper may contain the same elementary optimization without emphasizing the Rana--Parashar threshold. That residual bibliographic risk is recorded separately from the exact mathematical proof.

## References

1. S. Rana and P. Parashar, “Entanglement is not a lower bound for geometric discord,” arXiv:1207.5523v1; Phys. Rev. A 86, 030302(R) (2012), DOI 10.1103/PhysRevA.86.030302.
2. P. Bag, S. Dey, and H. Osaka, “Comparing Geometric Discord and Negativity for Bipartite States,” arXiv:1812.11156; Phys. Lett. A 383 (2019) 125973.
3. MSC2020, 81P43: Quantum discord.
