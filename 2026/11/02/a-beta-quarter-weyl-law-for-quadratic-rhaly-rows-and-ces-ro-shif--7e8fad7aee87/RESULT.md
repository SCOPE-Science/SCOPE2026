# A beta-quarter Weyl law for quadratic Rhaly rows and Cesàro shift defects

## Finding

Put \(\mathcal H=\ell^2(\mathbb N_0)\). For a complex sequence \(a=(a_n)_{n\ge0}\), define the Rhaly (terraced) matrix by
\[
(R_a x)_n=a_n\sum_{j=0}^{n}x_j.
\]
Suppose
\[
\lim_{n\to\infty}(n+1)^2|a_n|=c\quad\text{with }0<c<\infty.
\]
Then \(R_a\) is trace class and has the **sharp singular-value Weyl law**
\[
\boxed{\lim_{j\to\infty}j^2s_j(R_a)=c\,\mathfrak b^2,\qquad
\mathfrak b=\frac{\mathrm B(1/4,1/2)}{\pi\sqrt 2}=1.18034059901609\ldots.}
\]
Here singular values \(s_j\) are decreasing and numbered starting at one, and \(\mathrm B\) is the Euler beta function. Thus, for every \(p>0\),
\[
R_a\in\mathcal S_p\quad\Longleftrightarrow\quad p>\frac12,
\qquad
\lim_{N\to\infty}\frac{1}{\log N}\sum_{j=1}^N s_j(|R_a|^{1/2})=\sqrt c\,\mathfrak b.
\]
The statement concerns an infinite sequence of singular values: it is not an extrapolation from finite compressions. The arbitrary row phases in \(a_n\) have no effect on these singular values.

For the discrete Cesàro operator \(C\) and unilateral forward shift \(S\), given by
\[
(Cx)_n=\frac{1}{n+1}\sum_{j=0}^n x_j,\qquad Se_j=e_{j+1},
\]
every integer \(k\ge1\) yields a concrete trace-class shift-conjugation defect
\[
D_k=C-S^{*k}CS^k=R_{a^{(k)}},\qquad
a^{(k)}_n=\frac{k}{(n+1)(n+k+1)}.
\]
Consequently
\[
\boxed{\lim_{j\to\infty}j^2s_j(D_k)=k\mathfrak b^2,\qquad
\operatorname{Tr}(D_k)=H_k=\sum_{r=1}^k\frac1r.}
\]
The same strict Schatten threshold and critical logarithmic law hold for each \(D_k\), with \(c=k\). The Cesàro identity is a naturally motivated corollary; the general quadratic-row law is the main result.

## Assumptions and scope

The Hilbert space is complex and separable with its standard coordinate inner product. The coefficient assumption is an ordinary limit of nonnegative moduli; no regularity, monotonicity, or prescribed phases are required. Finitely many coefficients may be arbitrary. For \(p<1\), \(\mathcal S_p\) denotes the standard Schatten quasi-ideal. The beta integral is \(\mathrm B(x,y)=\int_0^1t^{x-1}(1-t)^{y-1}\,dt\), with \(x,y>0\).

We write \(N(t;T)=\#\{j\ge1:s_j(T)>t\}\) for \(t>0\). Equalities involving \(N\) use this strict convention; threshold boundary choices do not affect the asymptotic limits. Finite-rank perturbations change \(N(t;\cdot)\) by at most their rank. A norm perturbation of size \(\eta t\) squeezes counts between the levels \((1+\eta)t\) and \((1-\eta)t\).

## Proof

**1. Trace-class reduction.** Let \(u_n=\sum_{j=0}^n e_j\). Coordinatewise,
\[
R_a=\sum_{n=0}^\infty a_n\,|e_n\rangle\langle u_n|,
\qquad \|a_n|e_n\rangle\langle u_n|\|_1=|a_n|\sqrt{n+1}.
\]
The series converges in trace norm because \(|a_n|=O((n+1)^{-2})\). Since a diagonal unitary on the output changes \(a_n\) to \(|a_n|\), and zeros or arbitrary early rows are finite-rank modifications, we may use nonnegative rows for the counting asymptotic. This also verifies the relevant operator domain and compactness.

**2. Exact finite-block spectrum.** For \(m\ge1\), let \(L_m\) be the \(m\times m\) lower-triangular matrix with entry \(1\) on and below its diagonal. Its inverse is the first-difference matrix, so \((L_m^{-1})^*L_m^{-1}\) is tridiagonal: its diagonal is \(2\) except for a final \(1\), and every adjacent off-diagonal entry equals \(-1\). Solving its three-term eigenvector recurrence with a left Dirichlet and right free boundary gives, exactly,
\[
s_j(L_m)=\frac1{2\sin\!\left(\frac{(2j-1)\pi}{4m+2}\right)},\quad 1\le j\le m.
\]
Consequently, for a fixed \(x>0\) and threshold \(x^2\), the fraction of singular values of \(L_m\) exceeding \(x^2\) tends to
\[
F(x)=\frac1\pi\bigl|\{\theta\in(0,\pi):2\sin(\theta/2)<x^{-2}\}\bigr|.
\]
Equivalently \(F(x)=1\) if \(x\le1/\sqrt2\), while \(F(x)=\frac2\pi\arcsin(1/(2x^2))\) if \(x>1/\sqrt2\). In particular \(F(x)=O(x^{-2})\) at infinity.

**3. Count the bulk, with error controlled.** Fix \(\varepsilon>0\), \(L>\varepsilon\), \(\delta>0\) and set \(t=c/R^2\), with \(R\to\infty\). Split the row and column indices in \([\varepsilon R,LR)\) into consecutive blocks of length at most \(\delta R\) (rounding endpoints to integers). On a block based at \(xR\), \(x\in[\varepsilon,L]\), our coefficient limit gives uniformly
\[
\frac{R^2|a_n|}{c}=x^{-2}+O_{\varepsilon,L}(\delta)+o_R(1),
\]
where the \(O(\delta)\) is uniform on the chosen compact interval. The diagonal compression to this block is \(\operatorname{diag}(a_n)L_m\). Its singular values are bracketed, by the min-max principle, between the minimum and maximum row modulus times the singular values in step 2. Hence, first sending \(R\to\infty\) for fixed \(\delta\) and then \(\delta\downarrow0\), the sum of the singular-value counts of the bulk diagonal blocks at level \(t\), divided by \(R\), tends to
\[
\int_\varepsilon^L F(x)\,dx.
\]
The convergence is unchanged at thresholds \((1\pm\eta)t\), provided the parameter \(\eta>0\) is subsequently sent to zero; this follows by continuity of the distribution function away from a zero-measure threshold set.

**4. Justify discarding cross-block terms and both ends.** For any contiguous partition into blocks, the strictly lower *interblock* portion of the terraced matrix has rank at most the number of blocks: on any output block, all earlier input blocks enter through one scalar sum and the one output vector of coefficients on that block. The indices below \(\varepsilon R\) add rank at most \(\lceil\varepsilon R\rceil\).

For the upper indices starting at \(LR\), use dyadic blocks \([X,2X)\) up to \(X\asymp M R^2\), where \(M>1\) is fixed and large. On each such block \(|a_n|\le Cc/X^2\), its length is at most \(X\), and step 2 together with \(\sin z\ge2z/\pi\) for \(0\le z\le\pi/2\) gives \(s_j(L_m)\le(m+1)/j\). Thus for any fixed \(\eta\in(0,1)\), the number of its singular values above \((1-\eta)t\) is bounded by \(C_\eta R^2/X\), and summing the geometric series gives an upper contribution \(C_\eta R/L\). The number of these blocks is \(O(\log R)\), hence their cross-block rank is \(o(R)\).

Finally, the entire operator consisting of rows with index at least \(M R^2\), including their columns from the beginning, has Hilbert--Schmidt norm at most
\[
\left(\sum_{n\ge\lfloor MR^2\rfloor}(n+1)|a_n|^2\right)^{1/2}
\le \frac{C c}{M R^2}=\frac C M t.
\]
Choose \(M\) sufficiently large for this norm to be at most \(\eta t\). The finite-rank and norm counting perturbation inequalities now sandwich the full count between the bulk counts, subject to errors at most \(\varepsilon R+C_\eta R/L+o(R)\). First let \(R\to\infty\), then \(\delta\downarrow0\), \(\varepsilon\downarrow0\), \(L\uparrow\infty\), \(\eta\downarrow0\) (with a sufficiently large \(M\) for the chosen \(\eta\)). The integrable bound on \(F\) yields
\[
\lim_{R\to\infty}\frac{N(c/R^2;R_a)}R=\int_0^\infty F(x)\,dx.
\]
There is no use of a finite truncation as an infinite-dimensional proof: the two end estimates and finite-rank interblock decomposition control the entire infinite matrix.

**5. Evaluate the constant and invert the count.** By Tonelli's theorem,
\[
\int_0^\infty F(x)\,dx
=\frac1\pi\int_0^\pi [2\sin(\theta/2)]^{-1/2}\,d\theta
=\frac{\mathrm B(1/4,1/2)}{\pi\sqrt2}=\mathfrak b.
\]
The strict counting asymptotic \(N(t;R_a)\sim\mathfrak b\sqrt{c/t}\) as \(t\downarrow0\) is equivalent, by monotone inversion, to \(s_j(R_a)\sim c\mathfrak b^2/j^2\). Comparison with the \(p\)-series proves the exact Schatten threshold. Taking square roots and the harmonic-sum asymptotic proves the critical logarithmic coefficient.

**6. Cesàro application.** In the standard basis, \((S^{*k}CS^k)_{nj}=(n+k+1)^{-1}\) for \(j\le n\), and zero otherwise. Subtraction therefore produces precisely the row sequence \(a_n^{(k)}\). Its quadratic-row constant is \(k\). The trace is the sum of diagonal entries, and telescoping gives
\[
\sum_{n\ge0}\left(\frac1{n+1}-\frac1{n+k+1}\right)=H_k.
\]
All announced conclusions follow.

## Verification

The attached `verify.py` implements exact rational coefficient checks of the Cesàro difference, checks the complete finite-block singular values against direct matrix singular-value decompositions, tests an independent tridiagonal inverse calculation for finite compressions, and numerically tests the beta integral and moderate-rank finite truncations. Execute using `python3 verify.py` with NumPy and SciPy installed. Its tests are finite and do **not** certify the global Weyl law; the analytical block, tail, and counting argument above does.

## Relationship to prior work

Bellavita and Stylogiannis (2026) establish a discrete Mellin calculus for Cesàro-type operators and Hilbert--Schmidt remainder statements. Sang (2026) records Barría and Halmos's earlier Hilbert--Schmidt theorem for the first shift-conjugation difference. Neither inspected 2026 paper gives the singular-value coefficient or the critical \(\mathcal S_{1/2}\) boundary of that difference. Bellavita, Dellepiane, and Stylogiannis (2025), Theorem 1.3, characterize membership of Rhaly matrices in \(\mathcal S_q\) for \(q>1\); the theorem here addresses a more rapidly decaying natural row family with a sharp coefficient and the non-Banach quasi-ideal boundary \(p=1/2\). The finite-block technique and use of standard singular-value interlacing are classical tools and are not asserted to be new individually.

## Limitations

The row hypothesis requires a **positive finite quadratic modulus limit**; it does not cover slowly varying oscillations without a limit, other powers, or arbitrary Rhaly symbols. It supplies asymptotic rather than exact individual singular values. The original Barría--Halmos (1982) article was not accessible in full, leaving a possibility of implicit precedent. Older weighted discrete Hardy spectral asymptotics could imply the same constant under different terminology; definitive publication priority needs further independent literature review. Independent mathematical validation has not been carried out.

## References

1. C. Bellavita and G. Stylogiannis, *A discrete Mellin calculus in the Toeplitz algebra*, arXiv:2609.09453v1 (first submitted 8 September 2026), https://arxiv.org/abs/2609.09453.
2. Y. Sang, *The Cesàro Operator is in the Toeplitz Algebra*, arXiv:2608.25740v1 (first submitted 26 August 2026), https://arxiv.org/abs/2608.25740.
3. C. Bellavita, E. Dellepiane, and G. Stylogiannis, *Boundedness, compactness and Schatten class for Rhaly matrices*, arXiv:2503.21930 (first submitted 27 March 2025), https://arxiv.org/abs/2503.21930.
4. J. Barría and P. R. Halmos, *Asymptotic Toeplitz operators*, Transactions of the American Mathematical Society **273** (1982), 621--630. Historical result cited through reference 2; original full text not inspected.
