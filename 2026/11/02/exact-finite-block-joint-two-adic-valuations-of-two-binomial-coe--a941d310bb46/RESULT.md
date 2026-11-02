# Exact finite-block joint two-adic valuations of two binomial coefficients

## Finding

For every integer \(L\geq0\), take an integer \(N\) uniformly from \(0\leq N<2^L\), and define
\[
X_L=\nu_2\!\left(\binom{2N}{N}\right),\qquad
Y_L=\nu_2\!\left(\binom{3N}{N}\right).
\]
Set \(P_L(u,v)=\mathbb E[u^{X_L}v^{Y_L}]\). Then the **complete joint valuation distribution**, including its multiplicities at every finite block length, is
\[
P_L(u,v)=2^{-L}(1,0,0)\,A(u,v)^L\begin{pmatrix}1\\1\\v\end{pmatrix},
\qquad
A(u,v)=\begin{pmatrix}1&u&0\\1&0&uv\\0&v&uv\end{pmatrix}.
\]
Equivalently its generating function in the block length is
\[
\sum_{L\geq0}P_L(u,v)z^L=
\frac{2\bigl[4+2u(1-v)z+u(uv^2-uv-v^2)z^2\bigr]}
{8-4(1+uv)z+2u(v-v^2-1)z^2+uv(u+v)z^3}.
\tag{1}
\]
The size-three transfer is minimal among linear representations over the field \(\mathbb Q(u,v)\) for the sequence of unnormalized polynomials \(2^LP_L(u,v)\).

The exact first and second moments for all \(L\geq0\) are
\[
\mathbb EX_L=\frac L2,\qquad \operatorname{Var}(X_L)=\frac L4,
\]
\[
\mathbb EY_L=\frac L2-\frac23+\frac{3+(-1)^L}{6\,2^L},
\]
\[
\operatorname{Cov}(X_L,Y_L)=\frac{5L}{12}-\frac49+
\frac{9+7(-1)^L}{36\,2^L},
\tag{2}
\]
\[
\operatorname{Var}(Y_L)=\frac{11L}{12}-\frac{14}{9}
+\frac{5+(-1)^L}{3\,2^L}
-\frac{5+3(-1)^L}{18\,4^L}.
\tag{3}
\]
In particular, formula (2) gives the **complete finite-length correction**, including its alternating boundary term, to the established asymptotic covariance \(5L/12+O(1)\). The leading covariance and the joint central limit theorem are known from earlier digit-sum theory and are not originality claims here.

## Assumptions and scope

We use \(\nu_2(m)\) for the exponent of two dividing a nonzero positive integer \(m\), and \(s_2(m)\) for its binary digit sum, with \(s_2(0)=0\). All coefficients of the above probability generating polynomials are exact nonnegative rational numbers. The case \(L=0\) means \(N=0\) with probability one and is included in every displayed identity. No primality assumptions beyond the fixed prime two, limiting process, or asymptotic approximation are used.

The distributional assertion is the complete bivariate coefficient statement: for any nonnegative integers \(a,b\),
\[
\Pr(X_L=a,Y_L=b)=[u^a v^b]P_L(u,v).
\]

## Proof

**Binary valuation and carry interpretation.** Legendre's formula gives
\[
\nu_2(m!)=m-s_2(m).
\]
Therefore for every \(n\geq0\),
\[
\nu_2\!\left(\binom{2n}{n}\right)=s_2(n),\qquad
\nu_2\!\left(\binom{3n}{n}\right)=2s_2(n)-s_2(3n).
\tag{4}
\]
The latter is the number of carries, including the final carry, in ordinary base-two addition of \(n\) to \(2n\), by Kummer's theorem (or by digit conservation in binary addition).

**Finite weighted carry transducer.** Write \(n=\sum_{i=0}^{L-1}b_i2^i\) with \(b_i\in\{0,1\}\), and put \(b_{-1}=0\). Let \(c_i\) be the carry entering column \(i\) when adding \(n+2n\), with \(c_0=0\). Introduce \(t_i=b_{i-1}+c_i\in\{0,1,2\}\). Then
\[
c_{i+1}=\left\lfloor\frac{t_i+b_i}{2}\right\rfloor,\qquad
 t_{i+1}=b_i+c_{i+1}.
\tag{5}
\]
Each input bit \(b_i\) contributes \(u^{b_i}v^{c_{i+1}}\). Summing the two possible input bits for each state yields the complete transition table
\[
\begin{array}{c|cc}
 t_i&b_i=0&b_i=1\\ \hline
 0&(t_{i+1},\text{weight})=(0,1)&(1,u)\\
 1&(0,1)&(2,uv)\\
 2&(1,v)&(2,uv)
\end{array}
\]
and hence exactly the matrix \(A(u,v)\) appearing above. All \(L\) input bits have weight \(u^{s_2(n)}\), and all carries up through column \(L-1\) have already been counted. After these bits, the single remaining possible carry is \(\lfloor t_L/2\rfloor\); no further carry can arise. Its terminal weight is \((1,1,v)^{\mathsf T}\). Thus summing the weights of all \(2^L\) binary inputs proves the transfer identity without missing a boundary carry.

**Rationality and exact coefficients.** Since the transfer is finite,
\[
\sum_{L\ge0}P_L(u,v)z^L=(1,0,0)
\left(I-\frac z2A(u,v)\right)^{-1}
\begin{pmatrix}1\\1\\v\end{pmatrix}.
\]
Directly expanding the determinant and cofactors gives exactly equation (1). This is an identity of rational functions over \(\mathbb Q(u,v,z)\) and, by formal power-series expansion at \(z=0\), proves every joint coefficient at every nonnegative integer length.

**Minimal state dimension.** Write \(F_L(u,v)=2^LP_L(u,v)\). The Hankel matrix \((F_{i+j})_{0\le i,j\le2}\) has the exact determinant
\[
-\,u^5v^2(v-1)^2(uv^2-v^2-2v-1),
\tag{6}
\]
which is nonzero over \(\mathbb Q(u,v)\); at \((u,v)=(2,3)\) it is \(-2304\). Any linear representation in dimension at most two would factor this Hankel matrix through a two-dimensional space and force its determinant to vanish. The displayed three-state realization therefore has the least possible dimension for the polynomial sequence over \(\mathbb Q(u,v)\). This does not claim minimality for each specialized numerical choice of \(u,v\).

**Exact moments, without finite extrapolation.** The first and second factorial moments and mixed moment follow by formal differentiation of (1), then specializing \(u=v=1\). Their complete rational generating functions are
\[
\sum_{L\ge0}\mathbb EX_Lz^L=\frac{z}{2(1-z)^2},\qquad
\sum_{L\ge0}\mathbb EY_Lz^L=\frac{z^2(4-z)}{2(2-z)(1-z)^2(2+z)},
\]
\[
\sum_{L\ge0}\mathbb E[X_L(X_L-1)]z^L=\frac{z^2}{2(1-z)^3},
\]
\[
\sum_{L\ge0}\mathbb E[Y_L(Y_L-1)]z^L=
\frac{z^2(z^4-8z^3+8z^2-8z+16)}{2(2-z)^2(1-z)^3(2+z)^2},
\]
\[
\sum_{L\ge0}\mathbb E[X_LY_L]z^L=
\frac{z^2(-z^4+2z^3+4z^2-28z+32)}{2(2-z)^2(1-z)^3(2+z)^2}.
\tag{7}
\]
Each expression is verified directly by differentiating the explicit numerator and denominator of (1). Expanding the geometric factors \((1-z)^{-1}\), \((1-z/2)^{-1}\) and \((1+z/2)^{-1}\) in (7), and using \(\operatorname{Var}(Z)=\mathbb E[Z(Z-1)]+\mathbb EZ-(\mathbb EZ)^2\) and \(\operatorname{Cov}(X,Y)=\mathbb E[XY]-\mathbb EX\,\mathbb EY\), gives (2), (3), and all the displayed mean and variance formulas for every \(L\ge0\). No distributional limit or numerical fit enters this derivation.

## Verification

The standalone `verify.py` file computes the finite weighted transducer in exact integer arithmetic, then independently enumerates all \(0\leq n<2^L\) for \(0\leq L\leq14\), evaluating binary digit sums and the factorial-valuation formula. It verifies equality of **complete joint multiplicity tables**, not only moments. It also checks all displayed mean, variance and covariance identities as exact fractions for \(0\le L\le15\) and evaluates the nonzero Hankel determinant certificate at \((u,v)=(2,3)\). Its successful output begins with `VERIFY_OK` and `HANKEL_NONZERO`. The infinite-length assertions rest on the algebraic transfer proof above, not on finite enumeration.

## Relationship to prior work

Kummer's carry theorem and Legendre's valuation formula are classical. Schmid (1984) and Schmidt (1983) investigated joint binary digit sums of integer multiples; in particular the asymptotic joint central limit law is prior work. Drmota and Krattenthaler (2018, arXiv:1803.02178, Theorem 1) explicitly give the asymptotic covariance matrix for general multiples and hence already imply the leading covariance and Gaussian behavior for the present pair. The present assertion is instead the exact finite dyadic-block **bivariate counting polynomial**, its generically minimal three-dimensional linear realization, and the complete alternating boundary terms in the finite moments. These do not follow from an asymptotic covariance statement alone.

Sun (2010, arXiv:1004.4623, Theorem 1.1) studies divisibilities involving these two binomial-coefficient families, but its divisibility statements do not determine their finite-block joint frequencies. A support-only classification of possible valuation pairs similarly does not imply their multiplicities within each dyadic block. Standard transfer-matrix methods themselves are not claimed as new.

Schmid's 1984 full text could not be inspected, although its metadata and descriptions in later works were available. This limits historical-priority confidence: an equivalent finite-block transfer formula, perhaps with different indexing, may have appeared there or in other old digital-sum literature. The comparison above is therefore not a claim of exhaustive historical uniqueness.

## Limitations

The theorem concerns two explicitly named binomial-coefficient families, the prime two, and sampling over complete dyadic initial intervals. It does not supply a corresponding exact formula for general multipliers or arbitrary truncated intervals. It does not establish a new central limit theorem or a new asymptotic leading covariance. A historical-priority review of some inaccessible older sources and an independent mathematical audit remain outstanding.

## References

1. J. Schmid, *The joint distribution of the binary digits of integer multiples*, Acta Arithmetica **43** (1984), 391–415, DOI 10.4064/aa-43-4-391-415. Full text unavailable during this examination.
2. W. M. Schmidt, *The joint distributions of the digits of certain integer s-tuples*, Studies in Pure Mathematics (1983), 605–622.
3. M. Drmota and C. Krattenthaler, *A joint central limit theorem for the sum-of-digits function, and asymptotic divisibility of Catalan-like sequences*, arXiv:1803.02178 (first posted 2018-03-06), especially Theorem 1 and its covariance formula.
4. Z.-W. Sun, *Products and sums divisible by central binomial coefficients*, arXiv:1004.4623 (first posted 2010-04-26), especially Theorem 1.1.
5. J. C. Chen, H.-K. Hwang and V. Zacharovas, *Distribution of the sum-of-digits function of random integers: a survey*, arXiv:1212.6697 (first posted 2012-12-30).
