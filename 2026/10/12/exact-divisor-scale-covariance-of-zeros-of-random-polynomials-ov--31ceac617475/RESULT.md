# Exact divisor-scale covariance of multivariate polynomial zeros over finite residue rings

## Finding

Let \(m\ge2\), \(n\ge2\), and \(R=\mathbb Z/m\mathbb Z\). Let \(E\subseteq\mathbb Z_{\ge0}^n\) be finite and contain the zero vector and all coordinate vectors. Choose independent uniform \(C_e\in R\) for \(e\in E\) and set \(F(x)=\sum_{e\in E}C_e x^e\). For \(a,b\in R^n\), write
\[
g(a,b)=\gcd(m,a_1-b_1,\ldots,a_n-b_n),\qquad I_a=\mathbf 1_{\{F(a)=0\}}.
\]
Using any integer representatives for the differences gives the same gcd. Then
\[
\mathbb E I_a=1/m,\qquad \mathbb P(I_a=I_b=1)=g(a,b)/m^2,
\qquad \operatorname{Cov}(I_a,I_b)=(g(a,b)-1)/m^2.
\]
This includes \(a=b\). It holds for every allowed monomial support, independently of its higher-degree terms.

For arbitrary subsets \(A,B\subseteq R^n\), not necessarily disjoint, let \(N_A=\sum_{a\in A}I_a\). For \(d\mid m\) and \(u\in(\mathbb Z/d\mathbb Z)^n\), let \(A_d(u)=|\{a\in A:a\equiv u\pmod d\}|\) and define \(B_d(u)\) likewise. Then the covariance is the sum of positive-weight congruence-scale terms
\[
\boxed{\operatorname{Cov}(N_A,N_B)=\frac{1}{m^2}
\sum_{\substack{d\mid m\\d>1}}\varphi(d)
\sum_{u\in(\mathbb Z/d\mathbb Z)^n} A_d(u)B_d(u),}
\]
where \(\varphi\) is Euler's totient. In particular, subset-count covariances are nonnegative. For \(K=N_{R^n}\),
\[
\mathbb E K=m^{n-1},\qquad
\operatorname{Var}(K)=m^{2n-2}\sum_{\substack{d\mid m\\d>1}}\frac{\varphi(d)}{d^n}.
\]
For \(m=p^k\) this variance is \(p^{2k(n-1)}(1-1/p)\sum_{j=1}^k p^{-j(n-1)}\).

## Assumptions and scope

Uniformity is over the entire ring, and constant and coordinate-linear coefficients must be free and independent of all other coefficients. No assumption of independence of the induced monomial *functions* on the grid is required. Uniform total-degree-at-most and individual-degree-at-most families with any bound at least one are included. The theorem does not assert joint independence or association of the zero indicators, prescribe higher moments, or settle degree stabilization of the distribution.

## Proof

Consider the additive evaluation map \(R^E\to R^2\), \((C_e)_e\mapsto(F(a),F(b))\). Every monomial takes congruent values at \(a\) and \(b\) modulo \(g=g(a,b)\), so its image lies in the subgroup \(M=\{(u,v):v-u\in gR\}\). Conversely the constant column is \((1,1)\), and subtracting \(a_i(1,1)\) from the \(i\)-th coordinate-linear column gives \((0,b_i-a_i)\). The coordinate differences generate the ideal \(gR\) by Bézout's identity. Together these columns generate \(M\), so the image is exactly \(M\). The uniform coefficient vector maps to the uniform element of \(M\) since all fibers have the same size. The first component is uniform on \(R\), and \(|M|=m(m/g)\). This gives the one-point and joint-zero probabilities. At \(a=b\), the image is just the diagonal, with \(g=m\); at \(g=1\), it is all of \(R^2\).

The identity \(g-1=\sum_{d\mid g,\ d>1}\varphi(d)\) expresses the covariance kernel as a sum over the congruences \(a\equiv b\pmod d\) with \(d\mid m\), \(d>1\). Summing over ordered pairs \((a,b)\in A\times B\) groups the contributions at each scale into \(\sum_u A_d(u)B_d(u)\). For the full grid there are \(d^n\) congruence classes with equal occupancy \((m/d)^n\), giving the variance formula. The expectation is the number of points times \(1/m\). In the prime-power case the divisors greater than one are \(p^j\), \(1\le j\le k\), with \(\varphi(p^j)=p^j(1-1/p)\).

## Relation to univariate and other earlier results

Monagan and Tuncer, *Counting roots of polynomials and roots of resultants over finite rings* (arXiv:1609.08712v1), Theorem 1 and its proof on pp. 6–7, give the gcd pair kernel and full root-count variance over every modulus for uniform **monic univariate** polynomials of degree greater than one. The variance is \(\sum_{d\mid m,d>1}\varphi(d)/d\), equivalently their gcd-sum formula; their table in Remark 1 gives this variance with numerator indexed as OEIS A006579. The univariate variance \(k(1-1/p)\) is not presented here as new. In fact, exactly the same univariate pair count works for any prescribed top coefficient when the constant and linear coefficients are free: upon fixing the higher coefficients, the two root conditions first specify one constant coefficient and impose a linear congruence of index \(m/g\) on the linear coefficient.

In Jain, Moon and Wu's arXiv:2308.14580v1, Conjecture 5.7 uses independent uniform coefficients with individual degree bounded by \(d\); it states the prime-power mean and, in one variable with \(d>1\), the variance \(k(1-1/p)\), separately from distribution stabilization. The one-point mean above gives its expectation for \(d\ge1\); the earlier univariate pair count and the same free-coefficient reasoning give the variance part. Neither fact is the originality claim here. The contribution is the simultaneous **multivariate** evaluation ideal and the resulting divisor-scale covariance for arbitrary subsets over every modulus. The multiple coordinate differences, not just a single location difference, jointly determine all pair counts. In contrast, Caruso's p-adic Haar root densities and Evans's p-adic random-system moments concern actual zeros in p-adic domains, not the zeros of these finite congruences.

## Reproducibility

The accompanying \(\texttt{verify.py}\) can be run with Python 3 and the standard library. It exhaustively compares measured and predicted pair probabilities and full-grid variances for the stated finite examples, including affine and quadratic bivariate models and one affine trivariate model; its univariate cases are comparison checks. It also checks the variance for a specified proper subset of each grid, not every mixed pair of subsets. Output from this finite check does not substitute for the additive-image and congruence-class proof, which supplies the general mixed covariance. For exact examples, the mean and variance are respectively \(4,6\) at \((m,n)=(4,2)\) and \(6,19\) at \((6,2)\).

## References

1. M. Monagan and B. Tuncer, *Counting roots of polynomials and roots of resultants over finite rings*, arXiv:1609.08712v1, Theorem 1, its proof, and Remark 1.
2. R. Jain, H.-B. Moon, and P. Wu, *Distribution of the number of zeros of polynomials over a finite field*, arXiv:2308.14580v1, Section 5, Conjecture 5.7; *Involve* 18 (2025), 707–718, doi:10.2140/involve.2025.18.707.
3. X. Caruso, *Where are the zeroes of a random p-adic polynomial?*, arXiv:2110.03942.
4. S. N. Evans, *The expected number of zeros of a random system of p-adic polynomials*, *Electron. Commun. Probab.* 11 (2006), 278–290.
