# Likelihood-ratio monotonicity of singleton coupons at collection completion

## Finding
Let \(q\ge2\) coupon types be sampled independently and uniformly, and let \(T\) be the first draw by which all \(q\) types have appeared. Write \(S\) for the number of types seen exactly once by time \(T\). For every integer \(t\ge q\), the conditional law of \(S\) given \(T=t+1\) is no larger than its law given \(T=t\) in monotone likelihood-ratio order:
\[
 S\mid(T=t+1)\ \le_{\mathrm{lr}}\ S\mid(T=t).
\]
Equivalently, for \(t<u\) and \(s<r\), the joint mass \(p_{t,s}=\Pr(T=t,S=s)\) satisfies the reverse order-two minor inequality
\[
 p_{t,s}p_{u,r}\le p_{t,r}p_{u,s}.
\]
The ordering includes zero-probability boundary cells in the conventional cross-product sense and implies ordinary stochastic ordering. Furthermore, writing \(H_q=\sum_{j=1}^q1/j\) and \(H_q^{(2)}=\sum_{j=1}^q1/j^2\),
\[
 \operatorname{Cov}(T,S)=q\bigl(H_q^{(2)}-H_q\bigr)
 =-q\sum_{j=2}^q\frac{j-1}{j^2}<0.
\]
The exact joint mass itself is previously known (Myers--Wilf, 2003); what is asserted here is its global likelihood-ratio ordering and the displayed compact covariance identity.

## Assumptions and scope
The alphabet has \(q\ge2\) equally likely symbols; draws are independent, continued to first complete collection. Each \(t\ge q\) has positive probability as a completion time. The singleton count is taken **at completion**, not at a predetermined number of draws. No assertion is made for unequal symbol probabilities. Order \(X\le_{\mathrm{lr}}Y\) here means all cross-products \(f_X(s)f_Y(r)\ge f_X(r)f_Y(s)\) for \(s<r\), allowing zeros.

## Proof
**1. Reduce stopping to a surjection.** The final draw reveals a previously missing type. Conditional on \(T=t\), the final type is uniform, and the preceding \(\ell=t-1\) draws form a uniform word onto the other \(m=q-1\) types. If \(J=S-1\) counts singleton types in that word, its unnormalised mass is
\[
 C_{\ell,j}=\binom mj\ell!\,[z^{\ell}]z^j F(z)^{m-j},
 \qquad F(z)=e^z-1-z=\sum_{a\ge2}\frac{z^a}{a!}.
\]
The factor \(z\) denotes one occurrence, while \(F\) denotes two or more. The coefficient equals the number of length-\(\ell\) surjections having exactly \(j\) singleton fibers. For \(j=m\) it is positive only at \(\ell=m\), so its comparisons with \(j=m-1\) have the required orientation automatically.

**2. Log-concavity lemma.** The coefficient sequence of \(F\) is supported on the consecutive integers \(a\ge2\) and is log-concave: \((1/a!)^2\ge(1/(a-1)!)(1/(a+1)!)\). Convolution preserves the no-internal-zeros log-concavity of nonnegative sequences: form their Toeplitz matrices; log-concavity is equivalent to nonnegativity of every order-two Toeplitz minor, and the Cauchy--Binet formula preserves these minors under matrix products. Hence the coefficient sequence of \(U(z)=z^jF(z)^{m-j-1}\) is log-concave whenever \(0\le j\le m-2\). Let \(u_v=[z^v]U(z)\). The adjacent-column ratio is
\[
 \frac{C_{\ell,j+1}}{C_{\ell,j}}
 =\frac{m-j}{j+1}
 \left(\sum_{a\ge2}\frac1{a!}\frac{u_{\ell-a}}{u_{\ell-1}}\right)^{-1}
\]
when the denominator and numerator are positive. For each fixed \(a\ge2\), log-concavity makes \(u_{\ell-a}/u_{\ell-1}\) nondecreasing with \(\ell\) wherever the denominator is positive, with zeros entering monotonically from the left. Thus the sum is nondecreasing and the column ratio is nonincreasing. The support bounds \(\max(0,2m-\ell)\le j\le m-1\) for \(\ell>m\), with \(j=m\) only at \(\ell=m\), handle the zero cells. Multiplying adjacent-column ratios establishes the claimed reverse order-two minor inequality for all \(\ell<\ell'\) and \(j<j'\). Normalisation of rows and the shift \(S=J+1\) do not change it.

**3. Covariance identity.** Let \(G_q(z)=\mathbb E[z^T]=q!(z/q)^q\prod_{h=1}^{q-1}(1-hz/q)^{-1}\). For a specified type, either it is the final coupon (contributing \(G_q(z)/q\) to \(\mathbb E[z^T\mathbf 1_{\{\text{type singleton}\}}]\)), or it occurs exactly once before a different final coupon. With \(k=q-2\), \(v=z/q\), and \(B_k(v)=v^k\prod_{h=1}^k(1-hv)^{-1}\), the latter contribution is
\[
 (q-1)(q-2)!\,v^2\bigl(B_k(v)+vB_k'(v)\bigr).
\]
By symmetry, \(\mathbb E[z^TS]=G_q(z)+q(q-1)(q-2)!v^2(B_k(v)+vB_k'(v))\). Evaluate this expression and its first derivative at \(z=1\), using
\[
 B_k(1/q)=\frac1{(q-1)!},\quad
 \left.\frac{vB_k'(v)}{B_k(v)}\right|_{v=1/q}=q(H_q-1)-1,
\]
and the derivative of the logarithmic derivative, obtained by differentiating the finite product. One obtains
\[
 \mathbb E[S]=H_q,\qquad
 \mathbb E[TS]=q\left(H_q^2-H_q+H_q^{(2)}\right).
\]
The elementary geometric waiting-time decomposition gives \(\mathbb E[T]=qH_q\). Subtraction proves the covariance identity, and strict negativity follows because \(1/j^2<1/j\) for every \(j\ge2\).

## Verification
The independent standalone Python file `verify.py` checks the previously published joint mass against a direct occupancy-state recurrence, verifies the reverse two-by-two minors exactly for \(2\le q\le9\) and \(q\le t<u\le55\), and directly enumerates complete words for \(q\le4\), \(t\le8\). Truncated stopping-time moment sums provide an additional numerical check on the closed covariance formula. These finite checks supplement the all-parameter proof and do not establish it themselves.

## Relationship to prior work
Myers and Wilf (2003, Section 4, formula (46)) give exactly the joint mass \(\Pr(T=t,S=s)\) in terms of associated Stirling numbers and marginalise over stopping times. The proof above deliberately **does not claim** that enumeration as new. It establishes a global likelihood-ratio order across completion times and evaluates a mixed moment not presented in their Section 4. Barbour and Gnedin (2008) treat different fixed-time infinite-box occupancy fluctuations, not the finite stopped-sampling cross-time order. Standard log-concavity/convolution machinery supplies one critical inequality tool; the nontrivial comparison is the assembly of the conditional stopping-law kernel and its global minor signs.

## Limitations
This is an analytical consequence of a known exact joint enumeration; it should not be read as a new distribution formula, a result for nonuniform coupons, an independence statement, or an independently audited priority claim. If a stronger earlier result on total positivity of singleton surjections exists, it might already imply the likelihood-ratio theorem. Numerical checks do not replace the coefficient proof. For \(q=1\), both variables are deterministic and the strict covariance inequality does not apply.

## References
1. Amy N. Myers and Herbert S. Wilf, *Some New Aspects of the Coupon-Collector's Problem*, 2003, arXiv:math/0304229v1 (submitted 2003-04-16), Section 4, formula (46). https://arxiv.org/html/math/0304229v1
2. A. D. Barbour and A. V. Gnedin, *Small Counts in the Infinite Occupancy Scheme*, arXiv:0809.4387v1 (submitted 2008-09-25). https://arxiv.org/html/0809.4387v1
