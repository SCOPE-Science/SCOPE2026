# Sharp oscillation contraction of Jacobi-weighted Bernstein–Durrmeyer kernels

## Finding
For every integer \(n\geq1\) and \(a,b>0\), the positive Jacobi-weighted Bernstein–Durrmeyer operator \(D_{n,a,b}\), defined below, has **exact** oscillation-seminorm contraction coefficient
\[
\delta_{n,a,b}=I_{c_n}(a,b+n)-I_{c_n}(a+n,b),\qquad
c_n=\frac{R_n^{1/n}}{1+R_n^{1/n}},\quad
R_n=\frac{B(n+a,b)}{B(a,n+b)}.
\]
Here \(I_c\) is the regularized incomplete beta function. The sharp pair of evaluation locations is the two endpoints \(0\) and \(1\), even for asymmetric Jacobi weights. The exact one-step contraction **defect** is
\[
1-\delta_{n,a,b}=I_{c_n}(n+a,b)+I_{1-c_n}(n+b,a).
\]
For fixed \(a,b>0\),
\[
1-\delta_{n,a,b}\sim
\frac{2^{2-a-b}}{\sqrt{\Gamma(a)\Gamma(b)}}
 n^{(a+b)/2-1}2^{-n}.
\]
In the unweighted case \(a=b=1\), the finite-degree identity simplifies to \(\delta_{n,1,1}=1-2^{-n}\). The centered \(L^2\) spectral contraction factor is instead \(\lambda_1=n/(n+a+b)\), with spectral gap \((a+b)/(n+a+b)\). Thus the sharp one-step oscillation contraction defect is exponentially smaller than that spectral gap; more precisely,
\[
\frac{1-\lambda_1}{1-\delta_{n,a,b}}
\sim (a+b)2^{a+b-2}\sqrt{\Gamma(a)\Gamma(b)}
\frac{2^n}{n^{(a+b)/2}}.
\]

## Assumptions and scope
Let \(\mu_{a,b}\) be the beta probability measure on \([0,1]\) with density \(y^{a-1}(1-y)^{b-1}/B(a,b)\). Write \(p_{n,k}(x)=\binom nk x^k(1-x)^{n-k}\), and denote the beta density with parameters \(u,v>0\) by \(q_{u,v}\). Define the Markov operator on bounded Borel real-valued functions by
\[
(D_{n,a,b}f)(x)=\sum_{k=0}^n p_{n,k}(x)
\int_0^1 f(y)q_{a+k,b+n-k}(y)\,dy.
\]
Let \(P_x\) be the probability law of its output kernel at \(x\in[0,1]\). Define \(\operatorname{osc}(f)=\sup f-\inf f\), and the total-variation distance of probabilities as \(d_{\rm TV}(P,Q)=\sup_A|P(A)-Q(A)|\). Then
\[
\delta_{n,a,b}=\sup_{\operatorname{osc}(f)\le1}\operatorname{osc}(D_{n,a,b}f)
=\sup_{x,z\in[0,1]}d_{\rm TV}(P_x,P_z).
\]
All asymptotics hold as the integer \(n\to\infty\) with the two positive beta parameters fixed; no uniformity near \(a=0\) or \(b=0\) is asserted. The \(L^2\) spectral statement concerns the centered subspace of \(L^2(\mu_{a,b})\).

## Proof
**1. Total positivity and stochastic ordering.** Put \(q_k=q_{a+k,b+n-k}\). For integers \(k<l\), the quotient \(q_l(y)/q_k(y)\) is a positive constant times \((y/(1-y))^{l-k}\), strictly increasing in \(y\in(0,1)\). Likewise the binomial family \(p_{n,k}(x)\) has nonnegative two-by-two minors in the ordered variables \(x,k\). Their composition
\[
K(x,y)=\sum_{k=0}^n p_{n,k}(x)q_k(y)
\]
has nonnegative two-by-two minors by expansion over pairs \(k<l\): each summand is the product of the corresponding nonnegative minors. Hence for \(x<z\) in the interior, \(K(z,y)/K(x,y)\) is nondecreasing in \(y\). By continuity the same single-crossing property holds for boundary inputs. Since both kernels integrate to one, their densities differ in sign at most once, with the lower-input law dominating first. Consequently
\[
d_{\rm TV}(P_x,P_z)=\max_{t\in[0,1]}\big(F_x(t)-F_z(t)\big),\qquad x<z,
\]
where \(F_x\) is the distribution function. Alternatively, the one-crossing conclusion follows directly by the two TP2 compositions without assuming strict positivity of the binomial weights at the endpoints.

Each \(q_{k+1}\) has monotone likelihood ratio above \(q_k\), hence is stochastically greater. The binomial variable \(K_x\sim\operatorname{Bin}(n,x)\) is stochastically increasing in \(x\). Therefore \(F_x(t)\) is nonincreasing in \(x\), for every \(t\). For \(0\le x<z\le1\), the sandwich
\[
0\le F_x(t)-F_z(t)\le F_0(t)-F_1(t)
\]
shows that the **global** supremum is achieved at \((x,z)=(0,1)\).

**2. Exact boundary crossing.** At the endpoints the densities are \(q_0=q_{a,b+n}\) and \(q_n=q_{a+n,b}\). Their ratio satisfies
\[
\frac{q_n(y)}{q_0(y)}
=\frac{B(a,b+n)}{B(a+n,b)}
\left(\frac{y}{1-y}\right)^n.
\]
It increases from zero to infinity and equals one precisely when \(y=c_n\) as stated. Integrating the positive part of \(q_0-q_n\) up to that crossing proves
\(\delta=I_{c_n}(a,b+n)-I_{c_n}(a+n,b)\).
The equivalent two-tail overlap formula follows from \(I_{c}(u,v)+I_{1-c}(v,u)=1\). For \(a=b=1\), both endpoint laws have crossing \(1/2\) and their overlap equals \(2^{-n}\).

**3. Exponential defect and prefactor.** The gamma-ratio asymptotics for fixed positive parameters give
\[
\log R_n=(a-b)\log n+\log\Gamma(b)-\log\Gamma(a)+O(n^{-1}),
\]
so
\[
c_n=\tfrac12+\frac{(a-b)\log n+\log\Gamma(b)-\log\Gamma(a)}{4n}
+o(n^{-1}).
\]
For \(c=c_n\), integration by the endpoint version of Laplace's method, uniformly for \(c\to1/2\), yields
\[
I_c(n+a,b)\sim\frac{c^{n+a}(1-c)^{b-1}}{nB(n+a,b)},
\quad
I_{1-c}(n+b,a)\sim\frac{(1-c)^{n+b}c^{a-1}}{nB(n+b,a)}.
\]
The beta normalizers satisfy \(B(n+a,b)\sim\Gamma(b)n^{-b}\) and \(B(n+b,a)\sim\Gamma(a)n^{-a}\). Substituting the displayed crossing expansion shows **each** tail is asymptotic to
\[
\frac{2^{1-a-b}}{\sqrt{\Gamma(a)\Gamma(b)}}
 n^{(a+b)/2-1}2^{-n}.
\]
Summing them establishes the announced leading equivalent. The estimates hold because the endpoint-logarithmic derivative of each integrand is \(n/c+O(1)\) or \(n/(1-c)+O(1)\), and both endpoints remain inside a fixed compact subinterval of \((0,1)\).

**4. Spectral comparison.** Reversibility follows from the symmetric positive kernel relative to \(\mu_{a,b}\):
\[
D_{n,a,b}f(x)=\int f(y)\sum_{k=0}^n
\frac{p_{n,k}(x)p_{n,k}(y)}{\int p_{n,k}\,d\mu_{a,b}}
\,d\mu_{a,b}(y).
\]
This representation also gives positivity as a quadratic form. For each integer \(0\le j\le n\), the beta moment conditional on the binomial index is \((a+k)^{\overline j}/(n+a+b)^{\overline j}\). Binomial factorial moments show that \(D\) preserves polynomial degree and that its leading coefficient on degree \(j\) is \(\lambda_j=n^{\underline j}/(n+a+b)^{\overline j}\). By symmetry, the monic Jacobi polynomial of each degree is an eigenfunction of this value; the operator has rank \(n+1\) and vanishes on the remaining orthogonal complement. The sequence \(\lambda_j\) strictly decreases for \(j\ge1\), giving \(\lambda_1=n/(n+a+b)\) as the centered \(L^2\) norm. Combining its gap with step 3 proves the ratio claimed.

## Verification
The accompanying standalone Python program `check_durrmeyer.py` runs **527 finite assertions** on beta crossings, endpoint integral identities, sampled interior-pair domination, positivity of TP2 minors, spectral first moments, the uniform-parameter formula, and representative asymptotics. It requires Python with SciPy and NumPy; execute `python check_durrmeyer.py`. These are independent finite consistency tests, not substitutes for the four analytical steps above.

## Relationship to prior work
Berdysheva and Jetter (available online November 22, 2009) establish the general Bernstein–Durrmeyer integral kernel, Jacobi-weight specialization, and its already-known orthogonal polynomial spectral eigenvalues. Their Section 3.2.2 covers the \(L^2\) spectrum used here as **prior input**, not as a new result. Abel, Ivan, and Păltănea (2013) study geometric series and inverse approximation results for related genuine Durrmeyer operators, rather than the worst-case total-variation contraction of the Jacobi kernel. The separate Markov-kernel oscillation formula, endpoint optimizer, and exact two-parameter exponential prefactor are the claims advanced here. Classical bounds for operators on functions of bounded variation are not automatically the total-variation distance between two Markov transition probabilities.

## Limitations
The asymptotic prefactor assumes fixed \(a,b>0\). This result does not determine sharp total-variation distances after arbitrary iterations, nor provide a dimension-uniform multivariate extension. The 1995 Adell–de la Cal article's abstract mentions total variation in approximation comparisons; its complete text was not inspected, leaving a historical-priority risk for related statements. An equivalent older result under Dobrushin coefficient, strong ergodicity, or beta-mixture terminology cannot be ruled out without further historical verification. No independent mathematical audit has been performed.

## References
1. E. E. Berdysheva and K. Jetter, *Multivariate Bernstein–Durrmeyer operators with arbitrary weight functions*, Journal of Approximation Theory 162 (2010), 576–598; first available online 2009-11-22; DOI: https://doi.org/10.1016/j.jat.2009.11.005.
2. U. Abel, M. Ivan, and R. Păltănea, *Geometric series of positive linear operators and inverse Voronovskaya theorem*, arXiv:1304.5721, first posted 2013-04-21; https://arxiv.org/abs/1304.5721.
3. J. A. Adell and J. de la Cal, *Bernstein–Durrmeyer operators*, Computers & Mathematics with Applications 30 (1995); DOI: https://doi.org/10.1016/0898-1221(95)00081-X; abstract compared, full text unavailable in this examination.
