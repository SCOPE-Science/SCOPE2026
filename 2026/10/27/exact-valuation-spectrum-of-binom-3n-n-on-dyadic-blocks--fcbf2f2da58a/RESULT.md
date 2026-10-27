# Exact valuation spectrum of \(\binom{3n}{n}\) on dyadic blocks

## Finding
For every integer \(L\ge0\), define
\[
P_L(u)=\sum_{0\le n<2^L}u^{\nu_2\!\left(\binom{3n}{n}\right)}.
\]
The complete finite-block valuation distribution is determined by
\[
\boxed{\sum_{L\ge0}P_L(u)z^L=\frac{(1+z)(1-uz)}{1-(1+u)z+(u-u^2-1)z^2+u(u+1)z^3}.}
\]
Equivalently, \(P_0(u)=1\), \(P_1(u)=2\), \(P_2(u)=3+u^2\), and for every \(L\ge3\),
\[
P_L(u)=(1+u)P_{L-1}(u)+(u^2-u+1)P_{L-2}(u)-u(u+1)P_{L-3}(u).
\]
If \(N_L\) is uniform on \(\{0,1,\ldots,2^L-1\}\) and \(X_L=\nu_2\bigl(\binom{3N_L}{N_L}\bigr)\), then for all \(L\ge0\),
\[
\boxed{\mathbb E X_L=\frac L2-\frac23+\frac{\frac12+\frac16(-1)^L}{2^L},}
\]
\[
\boxed{\operatorname{Var}X_L=\frac{11L}{12}-\frac{14}{9}+\frac{5+(-1)^L}{3\cdot2^L}-\frac{(3+(-1)^L)^2}{36\cdot4^L}.}
\]
Moreover, as \(L\to\infty\),
\[
\boxed{\frac{X_L-L/2}{\sqrt{11L/12}}\ \Longrightarrow\ \mathcal N(0,1).}
\]

## Assumptions and scope
The binomial coefficient is the usual integer \(\binom{3n}{n}\); \(\nu_2\) denotes its exponent of \(2\); \(s_2(n)\) is the number of ones in the ordinary binary expansion with \(s_2(0)=0\). All counts include \(n=0\). The polynomial \(P_L\) has nonnegative integer coefficients, and \(P_L(1)=2^L\). The formulas cover every integer \(L\ge0\), not arbitrary intervals or other prime valuations. The central limit theorem concerns the uniform distribution on the indicated dyadic block.

## Proof
**Digit identity.** Legendre's factorial valuation gives \(\nu_2(k!)=k-s_2(k)\), so, identically for \(n\ge0\),
\[
\nu_2\!\left(\binom{3n}{n}\right)=2s_2(n)-s_2(3n).
\]
Write \(n=\sum_{i=0}^{L-1}x_i2^i\) with \(x_i\in\{0,1\}\). Multiplication by \(3\), reading from least significant bit, has carry states \(c\in\{0,1,2\}\). Given incoming carry \(c\) and digit \(x\), the output digit is \(y=(3x+c)\bmod2\) and outgoing carry is \(d=\lfloor(3x+c)/2\rfloor\). The transition contributes \(2x-y\) to the digit-sum difference. At the end, the remaining carry contributes \(-s_2(c)\). Thus the exact exponent is the sum of all transition outputs plus the terminal output, with no discarded leading digits.

**Transfer and rational series.** Give each transition weight \(u^{2x-y}\) and each terminal state weight \(u^{-s_2(c)}\). In state order \(0,1,2\) the resulting matrix and terminal column are
\[
M(u)=\begin{pmatrix}1&u&0\\u^{-1}&0&u^2\\0&1&u\end{pmatrix},\qquad
v(u)=\begin{pmatrix}1\\u^{-1}\\u^{-1}\end{pmatrix}.
\]
Since the initial carry is zero, the digit bijection gives the exact polynomial identity
\[
P_L(u)=e_0^{\mathsf T}M(u)^L v(u).
\]
The Laurent factors merely account for intermediate carries; the final expression is the asserted integral polynomial. Summing the matrix geometric series \(e_0^{\mathsf T}(I-zM(u))^{-1}v(u)\), and computing the displayed three-by-three determinant and first-row cofactors, yields exactly the stated rational function. Equating powers of \(z\) gives the recurrence and initial conditions. These algebraic identities hold over \(\mathbb Q(u,z)\), hence determine all finite blocks, not just a range of tested indices.

**Exact moments.** Differentiating the rational identity at \(u=1\) gives \(P_L'(1)=\sum_n X_L(n)\) and \(P_L''(1)=\sum_n X_L(n)(X_L(n)-1)\). The factors in the denominators after specialization are powers of \(1-2z\), \(1-z\), and \(1+z\). Explicitly, the differentiated series have the partial fractions
\[
\left.\frac{\partial G}{\partial u}\right|_{u=1}=-\frac{7}{6(1-2z)}+\frac1{2(1-2z)^2}+\frac1{6(1+z)}+\frac1{2(1-z)},
\]
\[
\left.\frac{\partial^2G}{\partial u^2}\right|_{u=1}=\frac1{18(1-2z)}-\frac1{(1-2z)^2}+\frac1{2(1-2z)^3}-\frac2{9(1+z)}+\frac1{6(1+z)^2}+\frac1{2(1-z)^2}.
\]
Coefficient extraction from these identities gives the displayed first and second moments after dividing by \(2^L\). In particular, \(\operatorname{Var}X_L= P_L''(1)/2^L+P_L'(1)/2^L-(P_L'(1)/2^L)^2\); the identities remain valid for \(L=0,1\).

**Gaussian limit.** For \(u\) in a complex neighborhood of \(1\), the matrix \(M(u)\) is an analytic family. At \(u=1\), \(M(1)\) is primitive and has eigenvalues \(2,1,-1\). Its Perron eigenvalue therefore continues analytically to a simple eigenvalue \(\lambda(u)\), while all other eigenvalues stay uniformly smaller in modulus for \(u\) near \(1\). The characteristic polynomial is
\[
F(t,u)=t^3-(1+u)t^2+(-u^2+u-1)t+u^2+u.
\]
Implicit differentiation of \(F(\lambda(u),u)=0\) at \((t,u)=(2,1)\) gives \(\lambda'(1)=1\) and \(\lambda''(1)=4/3\). Therefore, for \(u=e^w\),
\[
\left.\frac{d}{dw}\log\frac{\lambda(e^w)}2\right|_{w=0}=\frac12,\qquad
\left.\frac{d^2}{dw^2}\log\frac{\lambda(e^w)}2\right|_{w=0}=\frac{11}{12}>0.
\]
Analytic spectral decomposition, with the nonzero analytic leading coefficient fixed at \(w=0\), shows the centered moment-generating functions converge under \(w=it/\sqrt{11L/12}\) to \(e^{-t^2/2}\). Lévy's continuity theorem gives the asserted normal convergence. The bounded terminal carry affects only lower-order cumulants.

## Verification
The accompanying standalone `verify.py` enumerates valuations by direct binary digit sums through \(L=12\), constructs all polynomial coefficients independently by the recurrence, checks normalization, and verifies the exact rational moment formulas with integer and rational arithmetic. It also checks the digit-transition matrix and terminal correction across arbitrary binary input words through \(L=9\). These computations test the formulas on finite domains; they are not substitutes for the all-\(L\) transfer identity and analytic proof.

## Relationship to prior work
Kummer's theorem and Legendre's digit-sum identity are classical and account for the valuation representation. OEIS A077459 (entered December 2002) studies equality of \(s_2(n)\) and \(s_2(3n)\), including a 2004 comment comparing two binomial valuations. OEIS A036556 records the parity class of \(\nu_2\!\left(\binom{3n}{n}\right)\) in a 2004 comment. These are single-level or congruence conditions and neither source displays the complete finite-block polynomial generating function or exact moments above. Barat and Grabner (2001) treat distributions of binomial valuations and digital functions generally; their abstract is strongly relevant, but the full paper could not be inspected. Heuberger, Kropf and Wagner (2014), and Heuberger, Kropf and Prodinger (2015), develop general finite-transducer variance and limit theorems, which provide a broader framework for asymptotic normality. The contribution here is specifically the closed valuation distribution for this \(3n\)-family, its exact finite-depth mean and variance, and its evaluated Gaussian constants, not the abstract transducer central limit theorem itself.

## Limitations
This theorem does not concern non-dyadic windows or the distribution of valuations at primes other than \(2\). The full text of Barat and Grabner (2001), a plausible stronger priority source, was not accessible. A general finite-transducer theorem could yield the Gaussian limit by specialization; the novelty assessment therefore rests on the explicit family-specific exact generating function and moment formulas, subject to additional literature verification. No independent mathematical audit or exhaustive priority search is claimed.

## References
- E. E. Kummer, *Über die Ergänzungssätze zu den allgemeinen Reciprocitätsgesetzen*, J. reine angew. Math. 44 (1852), 93–146.
- OEIS A077459, *Numbers k such that k and 3*k have the same digital binary sum*, original entry December 1, 2002; https://oeis.org/A077459 .
- OEIS A036556, *Integers which when multiplied by 3 have an odd number of 1's in their binary expansion*; https://oeis.org/A036556 .
- G. Barat and P. J. Grabner, *Distribution of Binomial Coefficients and Digital Functions*, J. London Math. Soc. 64 (2001), 523–547; https://doi.org/10.1112/S0024610701002630 .
- C. Heuberger, S. Kropf and S. Wagner, *Variances and Covariances in the Central Limit Theorem for the Output of a Transducer*, 2014; https://arxiv.org/abs/1404.3680 .
- C. Heuberger, S. Kropf and H. Prodinger, *Output Sum of Transducers: Limiting Distribution and Periodic Fluctuation*, Electronic J. Combin. 22(2) (2015), P2.19; https://doi.org/10.37236/5026 .
