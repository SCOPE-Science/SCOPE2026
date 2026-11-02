# Sharp parity-dependent real-zero threshold and escape law for two-gap Hermite mixtures

## Finding

Let \(\operatorname{He}_n\) be the monic probabilists' Hermite polynomial, characterized by \(\operatorname{He}_0=1\), \(\operatorname{He}_1(x)=x\), and
\[
\operatorname{He}_n(x)=x\operatorname{He}_{n-1}(x)-(n-1)\operatorname{He}_{n-2}(x).
\]
For an integer \(n\ge 2\) and real \(b\), put
\[
Q_{n,b}(x)=\operatorname{He}_n(x)+b\operatorname{He}_{n-2}(x),\quad
b_c(n)=\begin{cases}n-1,&n\text{ even},\\n,&n\text{ odd}.\end{cases}
\]
The complete zero classification is as follows.

1. If \(b<b_c(n)\), all \(n\) zeros of \(Q_{n,b}\) are real and simple.
2. If \(b=b_c(n)\), zero is a root of multiplicity two when \(n\) is even and multiplicity three when \(n\) is odd; the remaining roots are real, simple and nonzero.
3. If \(b>b_c(n)\), there are precisely two simple nonreal zeros \(\pm i y_n(b)\) with \(y_n(b)>0\); all remaining \(n-2\) zeros are real and simple. For odd \(n\), one of these remaining zeros is zero.

The imaginary radius \(y_n(b)\) is strictly increasing and real-analytic for \(b>b_c(n)\). Moreover, its square \(y_n(b)^2\) is convex in \(b\), strictly convex when \(n\ge4\); its derivative increases from \(c_n\) to \(1\) (and is identically one for degrees two and three). Writing \(\varepsilon=b-b_c(n)>0\) and
\[
c_n=\begin{cases}(n-1)^{-1},&n\text{ even},\\3/n,&n\text{ odd},\end{cases}
\]
one has the **sharp global escape bounds**
\[
\boxed{\quad c_n\varepsilon\ \le\ y_n(b)^2\ \le\ \varepsilon.\quad}
\]
For \(n=2,3\) both inequalities are equalities. For \(n\ge4\), both are strict, and their coefficients are optimal in the respective limits \(b\downarrow b_c(n)\) and \(b\to\infty\). More precisely,
\[
y_n(b)^2=c_n\varepsilon+O_n(\varepsilon^2)\quad (\varepsilon\downarrow0),
\qquad y_n(b)^2=b-2n+3+O_n(b^{-1})\quad (b\to\infty).
\]

## Assumptions and scope

The parameter \(b\) is real, \(n\) is any fixed integer at least two, and all roots are counted with algebraic multiplicity. The polynomials use the probabilists' normalization, not the physicists' Hermite normalization. Strict inequalities are asserted where stated; no uniformity in \(n\) is claimed for the asymptotic remainders.

## Proof

Write \(n=2m+\delta\), with \(m\ge1\) and \(\delta\in\{0,1\}\). Put \(\alpha=\delta-\tfrac12\) and \(t=x^2/2\). The standard exact Hermite--Laguerre identities give
\[
Q_{n,b}(x)=(-1)^m2^m m!\,x^\delta
\left[L_m^\alpha(t)-\frac{b}{2m}L_{m-1}^\alpha(t)\right].\tag{1}
\]
For \(\alpha>-1\), the zeros of consecutive Laguerre polynomials \(L_m^\alpha\) and \(L_{m-1}^\alpha\) are simple, strictly positive and interlacing. Hence every real linear combination \(L_m^\alpha-dL_{m-1}^\alpha\) has \(m\) distinct real zeros, with at least \(m-1\) positive. The last zero is nonpositive precisely when
\[
\frac{L_m^\alpha(-s)}{L_{m-1}^\alpha(-s)}=d
\quad\text{for some }s\ge0.\tag{2}
\]
The denominator is strictly positive at \(-s\) for every \(s\ge0\).

Set \(p_j(t)=(-1)^j j!L_j^\alpha(t)\), so that these are monic orthogonal polynomials with positive zero sets. Consecutive interlacing gives the partial-fraction identity
\[
\frac{p_m(t)}{p_{m-1}(t)}
=t-(2m-1+\alpha)-\sum_{j=1}^{m-1}\frac{w_j}{t-\lambda_j},
\quad \lambda_j>0,\ w_j>0.\tag{3}
\]
Here the sum is empty if \(m=1\). The coefficients \(w_j>0\) follow either from the Christoffel--Darboux identity or from the negative residues of the ratio of consecutive monic orthogonal polynomials at each pole. Consequently the unique coefficient \(b\) associated with a nonpositive Laguerre root \(t=-s\) is
\[
B_m(s)=2m\frac{L_m^\alpha(-s)}{L_{m-1}^\alpha(-s)}
=2s+2(2m-1+\alpha)-2\sum_{j=1}^{m-1}\frac{w_j}{s+\lambda_j}.\tag{4}
\]
In particular,
\[
B_m'(s)=2+2\sum_{j=1}^{m-1}\frac{w_j}{(s+\lambda_j)^2}>0,
\quad B_m''(s)=-4\sum_{j=1}^{m-1}\frac{w_j}{(s+\lambda_j)^3}\le0.\tag{5}
\]
The equalities \(L_j^\alpha(0)=\binom{j+\alpha}{j}\) give
\[
B_m(0)=2(m+\alpha)=\begin{cases}n-1,&\delta=0,\\n,&\delta=1.\end{cases}\tag{6}
\]
Since \(B_m\) increases strictly from this value to infinity, equation (2) has no nonpositive root for \(b<b_c(n)\), exactly a zero root for equality, and exactly one strictly negative root \(-s\) for \(b>b_c(n)\). Combining this with the interlacing and (1) proves the entire zero classification, including simplicity away from zero. At equality the Laguerre zero is simple, producing multiplicity \(2+\delta\) at \(x=0\).

For \(b>b_c(n)\), define \(s=s(b)>0\) by \(B_m(s)=b\). Then \(y_n(b)^2=2s\). By (5), \(B_m\) is strictly increasing and analytic, hence \(y_n\) is strictly increasing and analytic. Since \(B_m\) is concave, its inverse \(s(b)\) is convex, strictly so for \(m>1\). Furthermore \(d(y_n(b)^2)/db=2/B_m'(s)\), which increases from \(c_n\) toward one. Differentiating the Laguerre quotient at zero, using
\[
\frac{(L_j^\alpha)'(0)}{L_j^\alpha(0)}=-\frac{j}{\alpha+1},
\]
yields
\[
B_m'(0)=\frac{2(m+\alpha)}{\alpha+1}.
\]
Together with (5), this gives for every \(s>0\)
\[
2s\le B_m(s)-B_m(0)\le \frac{2(m+\alpha)}{\alpha+1}s.
\]
Substituting \(\varepsilon=B_m(s)-B_m(0)\) and \(y_n(b)^2=2s\) yields the claimed bounds, with \(c_n=(\alpha+1)/(m+\alpha)\). They are strict for \(m>1\), since the weights are positive. Taylor expansion at \(s=0\) gives the small-\(\varepsilon\) law. Finally, from (4),
\[
B_m(s)=2s+2(2m-1+\alpha)+O_{m,\alpha}(s^{-1})
\quad (s\to\infty),
\]
so \(y_n(b)^2=b-2(2m-1+\alpha)+O_n(b^{-1})=b-2n+3+O_n(b^{-1})\). These two limits prove the sharpness of both global coefficients.

## Verification

The accompanying `CHECK.py` verifies the exact Hermite--Laguerre polynomial identity for degrees two through fourteen and a family of real parameters, checks the multiplicities and threshold from exact polynomial arithmetic, and compares the nonreal zero count and escape bounds with high-precision computed zeros. Its `CHECK_OK 195` result is supplementary. The proof above, based on interlacing, a positive-residue partial fraction identity and explicit endpoint derivatives, establishes the universal statement without relying on finite tests.

## Relationship to prior work

Li and Gutman (2000) proved a general sufficient condition: \(\operatorname{He}_n+b\operatorname{He}_{n-m}\) is real-rooted for all \(m\) and all \(|b|\le n-1\). In the second-gap case, their theorem does not give the exact parity-dependent upper threshold, the two-imaginary-zero classification beyond it, or the sharp escape bounds. Durán's 2025 Hermite study establishes eventual real-rootedness of fixed-coefficient finite linear combinations, and Durán's 2025 Laguerre study develops general real-zero mechanisms for normalized Laguerre combinations. Their results do not state the complete finite-degree phase boundary and the global quantitative escape bounds in the present normalization. The general consecutive-polynomial interlacing result used here is classical and is not claimed as new.

## Limitations

Only the second-gap pair \(\operatorname{He}_n\), \(\operatorname{He}_{n-2}\) is classified. There is no claim for other gaps, complex coefficients, or other orthogonal families. The sharper two-sided escape bounds depend on the Laguerre ratio structure. An unindexed earlier specialization of the Laguerre ratio argument remains a residual originality risk.

## References

1. X. Li and I. Gutman, *Elementary Proof of the Reality of the Zeros of \(\beta\)-Polynomials of Complete Graphs*, Kragujevac J. Math. 22 (2000), 49–56. https://imi.pmf.kg.ac.rs/kjm/pub/12616764800831_kjom2206.pdf.
2. A. J. Durán, *Zeros of linear combinations of Hermite polynomials*, arXiv:2505.15330, first posted May 21, 2025. https://arxiv.org/pdf/2505.15330.
3. A. J. Durán, *Zeros of linear combinations of Laguerre polynomials*, arXiv:2507.22425, first posted July 30, 2025. https://arxiv.org/pdf/2507.22425.
4. A. J. Durán, *Zeros of Linear Combinations of Orthogonal Polynomials*, Mediterranean J. Math. 23 (2026), article 148, initial preprint arXiv:2505.11956 dated May 17, 2025. https://doi.org/10.1007/s00009-026-03145-9.
