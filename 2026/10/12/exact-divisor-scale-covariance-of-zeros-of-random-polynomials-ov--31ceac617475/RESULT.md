# Exact divisor-scale covariance of zeros of random polynomials over finite residue rings

## Finding

Let \(m\ge2\) and \(n\ge1\) be integers and let \(R=\mathbb Z/m\mathbb Z\). Fix any finite collection \(E\subset\mathbb Z_{\ge0}^{n}\) of distinct monomial exponent vectors containing \(0\) and all standard coordinate vectors. Choose mutually independent uniform coefficients \(C_e\in R\) for \(e\in E\), and form the random polynomial
\[
F(x)=\sum_{e\in E}C_e x_1^{e_1}\cdots x_n^{e_n}.
\]
For each \(a\in R^n\), let \(I_a=\mathbf1_{\{F(a)=0\}}\), and for each subset \(A\subseteq R^n\) put \(N_A=\sum_{a\in A}I_a\). Let \(\varphi\) denote Euler's totient function.

**Theorem (exact spatial covariance and root-count variance).** For every \(a,b\in R^n\), write
\[
g(a,b)=\gcd(m,a_1-b_1,\ldots,a_n-b_n),
\]
using any integer representatives. Then, with no degree assumption beyond inclusion of the constant and coordinate-linear monomials,
\[
\mathbb E I_a=\frac1m,\qquad
\Pr(I_a=I_b=1)=\frac{g(a,b)}{m^2},\qquad
\operatorname{Cov}(I_a,I_b)=\frac{g(a,b)-1}{m^2}.
\]
The equal-point case \(a=b\) is included. For arbitrary subsets \(A,B\subseteq R^n\), define the occupancy of a residue class by
\[
A_d(u)=|\{a\in A:a\equiv u\pmod d\}|,
\quad u\in(\mathbb Z/d\mathbb Z)^n,
\]
and analogously \(B_d(u)\). The **exact divisor-scale decomposition** is
\[
\boxed{\operatorname{Cov}(N_A,N_B)
=\frac1{m^2}\sum_{\substack{d\mid m\\d>1}}\varphi(d)
\sum_{u\in(\mathbb Z/d\mathbb Z)^n}A_d(u)B_d(u).}
\]
In particular, every two subset root counts have nonnegative covariance. Taking \(A=B=R^n\) and writing \(K=N_{R^n}\) yields
\[
\boxed{\mathbb E K=m^{n-1},\qquad
\operatorname{Var}(K)=m^{2n-2}
\sum_{\substack{d\mid m\\d>1}}\frac{\varphi(d)}{d^n}.}
\]
For a prime power \(m=p^k\), this becomes
\[
\operatorname{Var}(K)=p^{2k(n-1)}
\left(1-\frac1p\right)\sum_{j=1}^{k}p^{-j(n-1)}.
\]
For one variable, the resulting identity is
\[
\boxed{\operatorname{Var}(K)=k\left(1-\frac1p\right)}
\quad(n=1,\ m=p^k),
\]
valid already when the random polynomial includes just its constant and linear terms. This proves the **mean and univariate variance assertions** of Conjecture 5.7 of Jain, Moon and Wu for all prime powers and all coefficient ensembles described above. It does *not* address their separate distribution-stabilization assertion.

## Assumptions and scope

All random coefficients range independently and uniformly over the **entire** finite ring \(R\); monomial functions need not be linearly independent as functions on \(R^n\). The polynomial family must include the constant and all \(n\) linear monomials with free coefficients. In particular, the conclusion applies to uniform total-degree-at-most-\(D\) and individual-degree-at-most-\(D\) families for every integer \(D\ge1\). It does not assert the formula for monic ensembles, restricted leading coefficients, models with nonuniform or dependent coefficients, or families missing a coordinate-linear term. Moduli need not be prime powers, and subsets \(A,B\) need not be disjoint.

## Proof

**1. Uniformity at one evaluation.** Fix \(a\in R^n\). After fixing all coefficients except the constant coefficient \(C_0\), the value \(F(a)=C_0+H(a)\) is uniform over \(R\). Thus \(\Pr(F(a)=0)=1/m\). More generally, the uniform constant coefficient makes \(F(a)\) independent of every random variable determined by the remaining coefficients, including \(F(b)-F(a)\).

**2. The difference lies in a canonical ideal.** For fixed \(a,b\), set \(h_i=b_i-a_i\in R\). For each monomial and hence for every polynomial over \(R\), the telescoping identity for products and powers shows that its evaluation difference at \(b\) and \(a\) belongs to the ideal \((h_1,\ldots,h_n)\) of \(R\). In the cyclic ring \(R\), this ideal equals \(gR\), where \(g=g(a,b)\) is a divisor of \(m\).

**3. The difference is exactly uniform on that ideal.** Holding all coefficients of degree at least two fixed, the random difference is of the form
\[
F(b)-F(a)=\sum_{i=1}^n h_iC_{e_i}+T,
\]
where the fixed shift \(T\) belongs to \(gR\) by step 2. The homomorphism \(R^n\to gR\), \((c_i)\mapsto\sum_i h_ic_i\), is surjective because the \(h_i\) generate \(gR\). Since its fibers have equal size, the linear sum is uniform on \(gR\); adding \(T\in gR\) preserves uniformity. Thus \(F(b)-F(a)\) is uniform over the additive subgroup \(gR\), which has \(m/g\) elements. By step 1 this difference is independent of \(F(a)\). Consequently
\[
\Pr(F(a)=F(b)=0)=\Pr(F(a)=0)\Pr(F(b)-F(a)=0)
=\frac1m\frac{g}{m}.
\]
Subtracting \(\mathbb E I_a\mathbb E I_b=1/m^2\) gives the claimed covariance. When \(a=b\), \(g=m\) and the same calculation correctly gives \(\operatorname{Var}(I_a)=(m-1)/m^2\).

**4. Resolve covariance into congruence scales.** The classical divisor identity \(\sum_{d\mid t}\varphi(d)=t\), applied to \(t=g(a,b)\), gives
\[
g(a,b)-1=\sum_{\substack{d\mid m\\d>1}}\varphi(d)
\mathbf1_{\{a\equiv b\pmod d\}}.
\]
Sum the point-indicator covariances over ordered pairs \((a,b)\in A\times B\). Grouping pairs by their common class \(u\pmod d\) gives the asserted exact covariance formula. Every summand is nonnegative.

**5. Sum over the entire grid.** There are \(m^n\) points in \(R^n\), so \(\mathbb E K=m^{n-1}\). For each divisor \(d\mid m\), there are \(d^n\) residue classes in \(R^n\pmod d\), each of size \((m/d)^n\). Their squared occupancy sum is
\[
d^n\left(\frac md\right)^{2n}=\frac{m^{2n}}{d^n}.
\]
Inserting this in step 4 gives \(\operatorname{Var}(K)=m^{2n-2}\sum_{d\mid m,d>1}\varphi(d)/d^n\), as claimed.

**6. Specialize to prime powers.** For \(m=p^k\), the proper nontrivial divisors have the form \(p^j\), \(1\le j\le k\), and \(\varphi(p^j)=p^j(1-1/p)\). This yields the displayed finite geometric sum. When \(n=1\), each summand equals \(1-1/p\), proving the univariate identity.

## Verification

The standalone dependency-free program `verify.py` enumerates all coefficient arrays for ten finite polynomial ensembles, including affine and quadratic models and composite moduli \(4,6,8,9\). It checks all pointwise marginals, all \(2{,}754\) ordered point-pair probabilities/covariances, all aggregate mean and variance identities, and exact covariance identities for specified proper subsets. It enumerates \(5{,}998\) polynomials in total and checks \(116\) further divisor identities for moduli through \(30\) and dimensions through \(4\). Every comparison uses integer arithmetic or Python's rational `Fraction`, with no floating-point tolerance. Run `python3 verify.py` beside this file; successful execution terminates with `PASS`. These finite checks provide reproducibility but are **not** the proof for arbitrary \(m,n,E\), which is step 1 through step 6 above.

For illustration, the exact formula gives \(\mathbb EK=4\), \(\operatorname{Var}(K)=6\) when \(m=4,n=2\), and \(\mathbb EK=6\), \(\operatorname{Var}(K)=19\) when \(m=6,n=2\), independent of which permitted higher monomials are present.

## Relationship to prior work

Jain, Moon and Wu, *Distribution of the number of zeros of polynomials over a finite field* (first public preprint 28 August 2023; journal publication 2025), prove finite-field distribution results and state in their Section 5, Conjecture 5.7, the prime-power mean and one-variable variance formulas together with a **separate** stabilization conjecture. Their explicit finite-field probability-generating function does not yield the composite-modulus result by field substitution: a finite field of order \(p^k\) and the residue ring \(\mathbb Z/p^k\mathbb Z\) have different evaluation dependence. The present theorem proves precisely the mean and variance assertions while also giving an arbitrary-modulus and multivariate covariance decomposition.

Bhargava, Cremona, Fisher and Gajović study counts of actual roots in the \(p\)-adic field of polynomials sampled with \(p\)-adic coefficients; that count is a different random variable from the number of solutions **modulo** \(p^k\). Evans studies simultaneous zeros of random systems over the \(p\)-adics, again not the finite-ring congruence-root covariance kernel. Classical totient divisor identities are used openly; no novelty is claimed for them individually.

## Limitations

No claim is made about the full probability distribution, higher moments, limiting distribution in polynomial degree, or independence/association of the complete zero-indicator family. Nonnegative pairwise and subset-count covariances alone do not imply association. The theorem requires free, independent, uniform constant and linear coefficients; dropping those conditions can invalidate it. Priority remains subject to independent literature confirmation, particularly older literature on finite-ring random polynomial evaluation, and the separately published revision of the originating article was not fully inspected. The proof is mathematical but has not undergone independent validation.

## References

1. R. Jain, H.-B. Moon and P. Wu, *Distribution of the number of zeros of polynomials over a finite field*, arXiv:2308.14580v1 (first public 2023-08-28), Section 5, Conjecture 5.7. https://arxiv.org/abs/2308.14580 ; journal version: *Involve* **18** (2025), 707–718, DOI: 10.2140/involve.2025.18.707.
2. M. Bhargava, J. Cremona, T. Fisher and S. Gajović, *The density of polynomials of degree n over \(\mathbb Z_p\) having exactly r roots in \(\mathbb Q_p\)*, arXiv:2101.09590, *Proc. Lond. Math. Soc.* **124** (2022), 713–736. https://arxiv.org/abs/2101.09590 .
3. S. N. Evans, *The expected number of zeros of a random system of \(p\)-adic polynomials*, *Electron. Commun. Probab.* **11** (2006), 278–290. https://www.stat.berkeley.edu/~evans/699.pdf .
