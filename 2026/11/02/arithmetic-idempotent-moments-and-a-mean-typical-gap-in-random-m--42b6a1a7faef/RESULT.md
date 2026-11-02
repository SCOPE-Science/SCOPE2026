# Arithmetic idempotent moments and a mean–typical gap in random monomial evolution algebras

## Finding
Fix any prime power \(q\ge2\). Independently choose a uniformly random permutation \(\sigma\in S_n\) and independent uniform scalars \(a_1,\ldots,a_n\in\mathbb F_q^\times\). Form the (generally nonassociative) evolution algebra \(E\) with natural basis \(e_1,\ldots,e_n\), \(e_i e_j=0\) for \(i\ne j\), and \(e_i^2=a_i e_{\sigma(i)}\). Its structure matrix is invertible, so \(E^2=E\). Let \(I_{n,q}=|\{x\in E:x^2=x\}|\), **including zero**. This is uniform sampling of labeled, invertible *monomial structure matrices*, not uniform sampling of isomorphism classes or of all invertible matrices.

**Theorem.** For each integer \(\ell\ge1\), set \(g_\ell=\gcd(2^\ell-1,q-1)\). Conditional on the cycle lengths of \(\sigma\), the contributions to \(I_{n,q}\) are independent: a cycle of length \(\ell\) contributes \(Y_\ell=1+g_\ell\) with probability \(1/g_\ell\), and \(Y_\ell=1\) otherwise, and \(I_{n,q}\) is their product. Thus, for each integer \(r\ge0\), as an identity of formal power series,
\[
\sum_{n\ge0}\mathbb E[I_{n,q}^{\,r}]z^n
=\exp\!\left(\sum_{\ell\ge1}\frac{z^\ell}{\ell}
\left[1+\frac{(1+g_\ell)^r-1}{g_\ell}\right]\right).
\]
The \(n=0\) term is defined to be \(1\). In particular, **for every** \(q\ge2\) and \(n\ge1\),
\[
\boxed{\mathbb E I_{n,q}=n+1.}
\]

For the second moment, write \(m\) for the odd part of \(q-1\). For every divisor \(d>1\) of \(m\), write \(h_d=\operatorname{ord}_d(2)\), and let \(\varphi\) be Euler's totient. Then
\[
\boxed{\sum_{n\ge0}\mathbb E[I_{n,q}^{\,2}]z^n
=(1-z)^{-4}\prod_{\substack{d\mid m\\d>1}}
(1-z^{h_d})^{-\varphi(d)/h_d}.}
\]
Set \(\delta_q=\sum_{d\mid m,\,d>1}\varphi(d)/h_d\) and \(C_q=\prod_{d\mid m,\,d>1}h_d^{-\varphi(d)/h_d}\), with empty products equal to \(1\). For each **fixed** prime power \(q\),
\[
\boxed{\mathbb E[I_{n,q}^{\,2}]\sim\operatorname{Var}(I_{n,q})
\sim \frac{C_q}{\Gamma(4+\delta_q)}n^{3+\delta_q}.}
\]

Define \(H=1\) when \(m=1\), and otherwise \(H=\operatorname{ord}_m(2)\). With \(\mu_j=\log(1+g_j)/g_j\), put
\[
\kappa_q=\frac1H\sum_{j=1}^{H}\mu_j.
\]
Then \(0<\kappa_q\le\log2<1\), and
\[
\boxed{\frac{\log I_{n,q}}{\log n}\xrightarrow[n\to\infty]{L^2}\kappa_q}
\qquad(n\ge2).
\]
Hence the typical number of idempotents is \(n^{\kappa_q+o_{\mathbb P}(1)}\), whereas its expectation is \(n+1\). This is a sharp mean–typical discrepancy within the specified natural ensemble.

For \(q=4\), there is also a parity-sensitive, exact **idempotent-free** probability (meaning no nonzero idempotents):
\[
\boxed{\mathbb P(I_{n,4}=1)=
\begin{cases}
0,&n\text{ odd},\\
(1/3)_k/k!,&n=2k,
\end{cases}}
\]
where \((1/3)_k=(1/3)(4/3)\cdots((3k-2)/3)\). Consequently \(\mathbb P(I_{2k,4}=1)\sim k^{-2/3}/\Gamma(1/3)\), and \(\kappa_4=(5/6)\log2\).

## Assumptions and scope
All algebraic operations are over \(\mathbb F_q\), for any prime power \(q\ge2\); characteristic two is included. The finite-dimensional algebra need not be associative. Both the permutation and nonzero coefficients are chosen independently and uniformly for each \(n\). Idempotent **elements** are distinct from the property \(E^2=E\), sometimes also called an “idempotent” evolution algebra. All asymptotics take \(n\to\infty\) with \(q\) fixed. The underlying probability space consists of \(n!(q-1)^n\) equally likely labeled structure matrices.

## Proof
**1. Exact cycle law.** For a cycle \(i_1\to\cdots\to i_\ell\to i_1\) of \(\sigma\), the idempotence equations are \(x_{i_{j+1}}=a_{i_j}x_{i_j}^2\). Because the \(a_i\) are nonzero, either all coordinates on this cycle vanish or none vanish. Iterating from \(x_{i_1}\) around the cycle gives \(x_{i_1}=\beta x_{i_1}^{2^\ell}\), where \(\beta\in\mathbb F_q^\times\) is a monomial in the cycle's coefficients. The exponent of the last coefficient introduced in this forward iteration is \(1\). Therefore \(\beta\) is uniformly distributed on \(\mathbb F_q^\times\) as the coefficients vary independently and uniformly, even after conditioning on all other coefficients. The cyclic group \(\mathbb F_q^\times\) has order \(q-1\); the equation \(x_{i_1}^{2^\ell-1}=\beta^{-1}\) has exactly \(g_\ell\) nonzero solutions when \(\beta^{-1}\) lies in the image of the power map, and none otherwise. That image has index \(g_\ell\). Each nonzero initial solution determines the remaining coordinates uniquely. Distinct cycles involve disjoint independent coefficients and equations. Hence the stated product law is exact.

**2. Moment generating function.** For a cycle of length \(\ell\), \(\mathbb E(Y_\ell^r)=1+((1+g_\ell)^r-1)/g_\ell\). The standard labeled permutation cycle decomposition gives the stated formal exponential identity; no limit or sampling approximation is involved. For \(r=1\), every cycle weight equals \(2\), and the series becomes \(\exp(2\sum_{\ell\ge1}z^\ell/\ell)=(1-z)^{-2}\). The coefficient of \(z^n\) is \(n+1\).

**3. Arithmetic second moment.** For \(r=2\), the cycle weight is \(3+g_\ell\). Since \(2^\ell-1\) is odd, \(g_\ell=\gcd(2^\ell-1,m)\). The classical identity \(t=\sum_{d\mid t}\varphi(d)\) implies
\[
g_\ell=\sum_{d\mid m}\varphi(d)\mathbf1_{h_d\mid\ell},
\]
where the \(d=1\) term means \(h_1=1\). Substitute this into \(\exp(\sum (3+g_\ell)z^\ell/\ell)\), and use \(\sum_{j\ge1}z^{hj}/(hj)=-(1/h)\log(1-z^h)\), obtaining the finite Euler product.

For real \(z\uparrow1\), each factor \(1-z^{h_d}\sim h_d(1-z)\), so the second-moment series has the singular behavior \(C_q(1-z)^{-4-\delta_q}\). Since this is a finite product of negative rational powers of \(1-z^h\) and \(h_d\) is fixed, standard coefficient transfer at roots of unity applies: \(z=1\) contributes \(C_q n^{3+\delta_q}/\Gamma(4+\delta_q)\), and every other root of unity has strictly smaller local singular exponent (the \((1-z)^{-4}\) factor is analytic and nonzero away from \(1\)). Thus the displayed coefficient asymptotic holds. Finally \((\mathbb EI_{n,q})^2=(n+1)^2=o(n^{3+\delta_q})\), proving the same asymptotic for the variance.

**4. Typical logarithmic count.** Let \(C_\ell\) be the number of \(\ell\)-cycles of the uniformly random permutation. Set \(L=\log I_{n,q}\). Conditional on the cycle structure, the logarithms of the cycle factors are independent, bounded between \(0\) and \(\log q\), with means \(\mu_\ell\). Thus
\[
\mathbb E L=\sum_{\ell\le n}\frac{\mu_\ell}{\ell},\qquad
\mathbb E\operatorname{Var}(L\mid\sigma)
\le(\log q)^2\sum_{\ell\le n}\frac1\ell.
\]
For a uniform permutation, \(\mathbb EC_\ell=1/\ell\), \(\operatorname{Var}(C_\ell)\le1/\ell\), and \(\operatorname{Cov}(C_\ell,C_j)\le0\) for distinct \(\ell,j\) (the joint factorial moment is \(1/(\ell j)\) if \(\ell+j\le n\), and \(0\) otherwise). Since all \(\mu_\ell\ge0\),
\[
\operatorname{Var}(\mathbb E[L\mid\sigma])
=\operatorname{Var}\left(\sum_{\ell\le n}\mu_\ell C_\ell\right)
\le(\log q)^2\sum_{\ell\le n}\frac1\ell.
\]
The law of total variance gives \(\operatorname{Var}(L)=O_q(\log n)\). The sequence \(g_\ell\) is periodic with period \(H\), because its divisors are controlled by powers of \(2\) modulo the odd integer \(m\). Consequently \(\mu_\ell\) is periodic with period \(H\), and harmonic summation yields \(\mathbb EL=\kappa_q\log n+O_q(1)\). Divide the mean-square error by \((\log n)^2\). Finally, \(\log(1+t)/t\) decreases for \(t\ge1\), and \(1\le g_\ell\le q-1\), so \(0<\kappa_q\le\log2<1\).

**5. The \(q=4\) zero-only event.** Here \(g_\ell=1\) when \(\ell\) is odd, and \(g_\ell=3\) when \(\ell\) is even. An odd cycle always contributes \(2\), whereas an even cycle contributes \(1\) with probability \(2/3\). Hence the probability of \(I_{n,4}=1\) is the coefficient of \(z^n\) in \(\exp((2/3)\sum_{j\ge1}z^{2j}/(2j))=(1-z^2)^{-1/3}\). Expanding by the generalized binomial theorem proves the exact formula, and the gamma-function ratio gives the asymptotic. The logarithmic cycle means are \(\log2\) at odd lengths and \((\log4)/3\) at even lengths, hence \(\kappa_4=(5/6)\log2\).

## Verification
The standalone direct-enumeration program `verify.py` enumerates all labeled weighted-permutation algebras in dimensions \(1\le n\le4\) over \(\mathbb F_2,\mathbb F_3,\mathbb F_4\) and dimensions \(1\le n\le3\) over \(\mathbb F_5,\mathbb F_7,\mathbb F_8\). It enumerates **every vector** of each algebra, computes \(x^2\) directly using its multiplication table, and tests \(x^2=x\). It compares the first two exact ensemble moments with the independent permutation-cycle-index recurrence; the \(\mathbb F_4\) calculation also checks the exact odd/even zero-only probabilities. The program terminates with `VERIFY_OK`. Finite checks do not establish the infinite asymptotic claims; the proof above does.

For \(q=4\), the first few second moments are \(4,11,24,46\) in dimensions \(1,2,3,4\). For \(q=2,3,5\) in the checked ranges, \(m=1\), and the second moment is \(\binom{n+3}{3}\).

## Relationship to prior work
Khudoyberdiyev, Omirov and Qaralleh (arXiv:1307.0993v1, 3 July 2013), §3, introduced the weighted-permutation evolution algebra and established its decomposition over the complex/characteristic-zero setting. Their cycle decomposition, existence of idempotent elements, and algebra-isomorphism observations are not asserted as new here. They do not treat uniform finite-field monomial ensembles, exact moment generating functions, or a logarithmic typical-size law. Their characteristic-zero rescaling uses extraction of roots and does not remove finite-field power-map obstructions.

Narkuziyev (arXiv:2005.05793v1, 9 May 2020), §4, considers idempotent solutions for a *two-permutation* real-coefficient family and certain low-dimensional cases. The present one-permutation finite-field random model, its arithmetic distributions and asymptotics are different. The elementary factor \(\gcd(2^\ell-1,q-1)\) also occurs in established homomorphism counts for **unweighted** permutation-cycle evolution algebras. That familiar cyclic root-count factor and the all-unit-coefficient special case are not claimed as new. A random weighted model must additionally determine which coefficients give roots, how those events couple through random permutation cycles, and the resulting full moment and typical-value laws.

Wei and Zou (arXiv:2310.12368v1, 18 October 2023), §§1–3, establish finite-field counts of **isomorphism classes of perfect evolution algebras** using a monomial group action on invertible structure matrices. Their object of enumeration is not the distribution of idempotent **elements** under the uniform monomial-matrix model. This finite-field enumeration is the principal motivating source.

Kaygorodov, Martín González and Viruel (arXiv:2610.22248v1, 15 October 2026), Remark 23, obtain mean \(1\) for the number of **nonzero** idempotent elements when the structure matrix is uniform in the *whole* \(\operatorname{GL}_n(\mathbb F_q)\). That result does not imply the present subensemble law: the monomial ensemble is strictly smaller and has mean \(n\) nonzero idempotents. Classical permutation cycle-index and finite cyclic-group power-map identities are used as established tools, not claimed as new.

## Limitations
This result counts **all idempotent elements including zero**, not the number of idempotent basis vectors or the number of idempotent isomorphism types. It applies to the explicitly defined uniform labeled monomial ensemble and fixed \(q\) asymptotics; changing the sampling measure can change every conclusion. There is no assertion of a Gaussian limit, rates of convergence, or comparable statements for all invertible matrices. Published-priority searches reduce but cannot eliminate the risk of a general unlocated cycle-index theorem specializing to these moment laws. The verification is mathematical and computational within the stated scope, not an external or independent audit.

## References
1. A. Kh. Khudoyberdiyev, B. A. Omirov and I. Qaralleh, *Few remarks on evolution algebras*, arXiv:1307.0993v1 (2013), https://arxiv.org/abs/1307.0993 .
2. B. A. Narkuziyev, *Some remarks on evolution algebras corresponding to permutations*, arXiv:2005.05793v1 (2020), https://arxiv.org/abs/2005.05793 .
3. Y. Wei and Y. M. Zou, *Isomorphism Classes of Idempotent Evolution Algebras*, arXiv:2310.12368v1 (2023), https://arxiv.org/abs/2310.12368 .
4. I. Kaygorodov, C. Martín González and A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248v1 (2026), https://arxiv.org/abs/2610.22248 .
