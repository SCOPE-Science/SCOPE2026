# Exact Gaussian mixed-norm circle means and the two-monomial transition

## Finding

Fix \(\alpha>0\). For an entire function \(f\), put
\[
M_2(f,r)=\left(\frac1{2\pi}\int_0^{2\pi}|f(re^{i\theta})|^2\,d\theta\right)^{1/2},
\qquad
\|f\|_{2,4,\alpha}^4=4\alpha\int_0^\infty M_2(f,t)^4e^{-2\alpha t^2}\,t\,dt.
\]
For every \(r\geq0\), let \(C_\alpha(r)\) be the smallest number satisfying
\[
M_2(f,r)\leq C_\alpha(r)\,\|f\|_{2,4,\alpha}
\]
for every entire function with finite right-hand norm. Set \(s=\alpha r^2\), \(n=\lfloor s\rfloor\), and \(c=n+\tfrac12\). Then the exact best constant is
\[
\boxed{C_\alpha(r)^4=\frac{(2s)^{2n}}{(2n)!}
\begin{cases}
1,&n\leq s\leq n+\frac12,\\[3pt]
1+\displaystyle\frac{2(s-n-\frac12)^2}{n+\frac12},
& n+\frac12<s<n+1.
\end{cases}}
\]
At \(s=0\), the factor \((2s)^0\) means \(1\). All nonzero equality functions are classified:

* If \(n\leq s\leq n+\frac12\), they are precisely \(f(z)=A z^n\), with \(A\ne0\).
* If \(n+\frac12<s<n+1\), they are precisely \(f(z)=A z^n+B z^{n+1}\) with both coefficients nonzero and
\[
\boxed{\frac{|B|^2}{|A|^2}
=\frac{\alpha(s-n-\frac12)}{(n+\frac12)(n+1-s)}.}
\]
The phases of \(A,B\) are unrestricted. In particular, on the upper half of each unit interval of \(s\), no monomial attains the best constant: two consecutive degrees are required.

## Assumptions and scope

The Gaussian parameter \(\alpha\) is any positive real number; \(r\) is any nonnegative real radius. The angular exponent is exactly \(2\) and the outer radial exponent exactly \(4\). The norm above is normalized so that \(\|1\|_{2,4,\alpha}=1\). A zero-norm function is necessarily zero. Extremizers are classified among all entire functions with finite norm, not just polynomials. The formula concerns circular \(L^2\)-means, not point evaluations \(|f(z)|\).

## Proof

**1. Reduction to a positive-coefficient cone.** Write the Taylor expansion \(f(z)=\sum_{k\geq0}a_kz^k\) and define
\[
x_k=|a_k|^2\alpha^{-k}\geq0,
\qquad P(u)=\sum_{k\geq0}x_ku^k.
\]
Angular orthogonality and monotone convergence yield \(M_2(f,r)^2=P(s)\). Substituting \(u=\alpha t^2\) in the prescribed norm gives the exact identity
\[
\|f\|_{2,4,\alpha}^4
=2\int_0^\infty P(u)^2e^{-2u}\,du.
\]
Thus the fourth power of the ratio to be maximized is
\[
\mathscr R_s(P)=\frac{P(s)^2}{2\langle P,P\rangle},
\quad
\langle U,V\rangle=\int_0^\infty U(u)V(u)e^{-2u}\,du.
\]
All sums and integrals below are well defined by positivity and the finite norm; their exchanges follow from Tonelli's theorem.

**2. Moment ratios.** The exponential moments are
\[
 m_j:=\langle u^j,1\rangle=\frac{j!}{2^{j+1}}\qquad(j\geq0).
\]
Let \(s>0\) be fixed, and choose a polynomial \(Q\) with nonnegative coefficients, positive for \(u>0\). Define
\[
p_k=\frac{\langle u^k,Q\rangle}{s^k}\quad (k\geq0).
\]
The moments \(v_k=\langle u^k,Q\rangle\) satisfy
\[
v_{k+1}^2<v_kv_{k+2}.
\]
Indeed this is strict Cauchy--Schwarz under the positive measure \(Q(u)e^{-2u}\,du\), which is not supported on a single point. Hence the consecutive ratios \(p_{k+1}/p_k\) are strictly increasing with \(k\). A sequence of this type has its smallest value at the index or adjacent indices at which its ratio crosses \(1\).

**3. Construct the matching certificate.** With \(n=\lfloor s\rfloor\):

If \(n\leq s\leq n+\frac12\), set \(Q(u)=u^n\). Directly,
\[
\frac{p_{k+1}}{p_k}=\frac{k+n+1}{2s}.
\]
It is at most \(1\) at \(k=n-1\) (when \(n\geq1\)), and at least \(1\) at \(k=n\). Thus \(p_k\geq p_n\) for every \(k\). At an integer or half-integer one neighboring index may tie, which does not change the equality classification below.

If \(n+\frac12<s<n+1\), abbreviate \(c=n+\frac12\), \(d=n+1\), and put
\[
a=c(d-s)>0,\quad b=s-c>0,\qquad Q(u)=u^n(a+bu).
\]
The exact moments give
\[
\frac{p_{n+1}}{p_n}
=\frac{ac+bcd}{s(a+bc)}=1,
\]
since \(a(s-c)=bc(d-s)\). Strict log-convexity then implies \(p_k\geq p_n=p_{n+1}\) for all nonnegative integers \(k\).

In either case, all indices in the support of \(Q\) minimize \(p_k\), so their common minimal value is
\[
p_* =\frac{\langle Q,Q\rangle}{Q(s)}.
\]
For a general positive-coefficient \(P\) of finite energy, positivity implies
\[
\langle P,Q\rangle
=\sum_{k\geq0}x_k\langle u^k,Q\rangle
\geq p_*P(s).
\]
Cauchy--Schwarz gives
\[
\langle P,Q\rangle^2\leq
\langle P,P\rangle\langle Q,Q\rangle.
\]
Combining, one obtains the sharp bound
\[
\mathscr R_s(P)\leq\frac{Q(s)^2}{2\langle Q,Q\rangle}.
\]
Every positive-coefficient polynomial \(Q\) constructed above is realized by an entire polynomial \(f\): choose its Taylor magnitudes from \(|a_k|^2=\alpha^k x_k\). Equality holds for positive multiples of \(Q\). Conversely, equality in Cauchy--Schwarz forces \(P\) to be proportional to \(Q\) almost everywhere under the exponential measure, hence as an entire positive-coefficient power series by analyticity. Consequently there are no other extremizers, including at the endpoint ties.

**4. Evaluate the certificate.** For \(Q(u)=u^n\),
\[
\frac{Q(s)^2}{2\langle Q,Q\rangle}
=\frac{(2s)^{2n}}{(2n)!}.
\]
For \(Q(u)=u^n(a+bu)\), the above moments yield
\[
\langle Q,Q\rangle
=\frac{(2n)!}{2^{2n+1}}
\big(a^2+2cab+cdb^2\big),
\]
and the special coefficients satisfy
\[
a+bs=\frac c2+(s-c)^2,
\qquad a^2+2cab+cdb^2=\frac c2(a+bs).
\]
Substitution yields precisely
\[
\frac{Q(s)^2}{2\langle Q,Q\rangle}
=\frac{(2s)^{2n}}{(2n)!}
\left(1+\frac{2(s-c)^2}{c}\right).
\]
Since \(x_{n+1}/x_n=b/a\) in the mixed case and \(x_k=|a_k|^2\alpha^{-k}\), the stated coefficient ratio follows. For \(s=0\), the origin value is controlled sharply by the constant function: \(P(0)^2\leq2\langle P,P\rangle\), with equality only for constants. This completes the proof.

## Verification

The standalone \(\texttt{CHECKER.py}\) uses Python's exact rational arithmetic and factorial moments, without external dependencies. It verifies \(560\) positive-coefficient test inequalities, \(56\) closed-form certificate identities, \(80\) tight supporting-moment identities, \(16\) boundary identities, and the origin value. The checker is finite consistency evidence only; strict moment log-convexity, the supporting-certificate construction, and Cauchy--Schwarz establish the theorem for every radius and every entire function.

To reproduce: run \(\texttt{python3 CHECKER.py}\) from a folder containing this file and the included checker. No data files are needed.

## Relationship to prior work

Fang and Tien's *Sharp Gaussian Mixed-Norm Theory for Fock Spaces* (arXiv:2609.26821v1) develops the general Gaussian radial--angular Fock theory. Theorem 1.1 proves the optimal **growth order** of circular means, while Lemma 2.2 and Corollary 2.3 use monomial tests to recover that order up to constants. Those results neither give the best radius-by-radius constant nor identify the nonmonomial optimizer regions. The present equality calculation makes the first non-Hilbert outer exponent fully quantitative for the angular Hilbert case. The authors' companion study of sampling and interpolation (arXiv:2609.23572v1) uses the same norm normalization and concerns sampling geometry, not this extremal problem.

## Limitations

Only the angular exponent \(2\) and radial exponent \(4\) are covered; the argument uses the fact that the radial fourth power becomes a quadratic energy in the nonnegative Taylor-coefficient squares. No analogous complete classification for other exponent pairs follows automatically. The coefficient phases are arbitrary because angular \(L^2\) means depend only on coefficient magnitudes. An unindexed equivalent theorem in older positive-coefficient moment-extremal literature cannot be ruled out by the literature comparisons alone. No independent audit has been performed.

## References

1. Xiang Fang and Pham Trong Tien, *Sharp Gaussian Mixed-Norm Theory for Fock Spaces*, arXiv:2609.26821v1, first publicly submitted 20 September 2026. https://arxiv.org/html/2609.26821v1 . Relevant items: definition in Section 1.3, Theorem 1.1, Lemma 2.2, Corollary 2.3.
2. Xiang Fang and Pham Trong Tien, *Sampling and Interpolation in Gaussian Mixed-Norm Fock Spaces*, arXiv:2609.23572v1, first publicly submitted 20 September 2026. https://arxiv.org/html/2609.23572v1 . Relevant items: normalization in Section 1.1 and sampling/interpolation theorems.
