# Jacobi-sum spectrum and a field-size dichotomy for two-point discriminant biases

## Finding

Let \(q\) be any odd prime power and \(n\ge2\). For \(a,b\in\mathbb F_q^\times\), let \(N_+(n;a,b)\) (respectively \(N_-(n;a,b)\)) count monic polynomials \(f\in\mathbb F_q[X]\) of degree \(n\) satisfying \(f(0)=a\), \(f(1)=b\), with a nonzero square (respectively nonsquare) discriminant. The following formulas give **every** such fibre, including the exclusion of zero discriminants.

Let \(\mathcal X\) denote all multiplicative characters of \(\mathbb F_q^\times\), each extended by zero at zero, even the trivial character \(\mathbf1\). For \(\alpha,\beta\in\mathcal X\), define
\[
J_{\alpha,\beta}=\sum_{c\in\mathbb F_q\setminus\{0,-1\}}\alpha(c)\beta(c+1),\qquad
L_{\alpha,\beta}(T)=\begin{cases}
(1-T)^2/(1-qT),&\alpha=\beta=\mathbf1,\\
1+J_{\alpha,\beta}T,&\text{otherwise}.
\end{cases}
\]
Here \([T^n]\) extracts a formal power-series coefficient. Then
\[
\boxed{N_\pm(n;a,b)=\frac{1}{2(q-1)^2}\sum_{\alpha,\beta\in\mathcal X}\overline{\alpha(a)\beta(b)}[T^n]\left(\frac{L_{\alpha,\beta}(T)}{L_{\alpha^2,\beta^2}(T^2)}\ \pm\ \frac{(-1)^n}{L_{\alpha,\beta}(T)}\right).}
\]
In particular, their difference \(B_{n,q}(a,b)=N_+(n;a,b)-N_-(n;a,b)\) has the explicit Jacobi-sum spectrum
\[
\boxed{B_{n,q}(a,b)=\frac{(-1)^n}{(q-1)^2}\left(1-(q-1)n+\sum_{(\alpha,\beta)\ne(\mathbf1,\mathbf1)}\overline{\alpha(a)\beta(b)}(-J_{\alpha,\beta})^n\right).}
\]

The bias has a **sharp field-size dichotomy**. For \(q=3\), let \(\varepsilon\) denote the quadratic character on \(\mathbb F_3^\times\). Then
\[
B_{n,3}(a,b)=\frac{(-1)^n}{4}\bigl(1-2n+(-1)^n\varepsilon(a)+\varepsilon(b)+\varepsilon(a)\varepsilon(b)\bigr),
\qquad \max_{a,b}|B_{n,3}(a,b)|=\left\lceil\frac n2\right\rceil.
\]
For **every** odd \(q\ge5\),
\[
\boxed{\frac{q^{n/2}}{(q-1)^2}\le\max_{a,b}|B_{n,q}(a,b)|\le q^{n/2}+\frac{n}{q-1}.}
\]
Thus for each fixed odd \(q\ge5\), the largest conditioned bias grows as \(\Theta_q(q^{n/2})\), whereas for \(q=3\) it grows linearly.

## Assumptions and scope

The field order \(q\) is an odd prime power (not necessarily prime), \(n\ge2\) is an integer, and \(a,b\) are individually **nonzero** elements of the field. The two evaluation conditions at \(0\) and \(1\) are independent for all such \(n\). The discriminant is the standard monic-polynomial discriminant, and a zero discriminant is counted in neither \(N_+\) nor \(N_-\). Complex conjugation in the character sum denotes inverse multiplicative characters and leads to a rational integer count. The trivial character is extended by zero at zero exactly as every other character.

## Proof

**1. Two-point character series.** For each monic \(f\), put \(\eta_{\alpha,\beta}(f)=\alpha(f(0))\beta(f(1))\). This is multiplicative and is zero when \(X(X-1)\) divides \(f\). Its Euler series \(L_{\alpha,\beta}(T)=\sum_{f\ \mathrm{monic}}\eta_{\alpha,\beta}(f)T^{\deg f}\) has constant coefficient \(1\). In degree one, write \(f=X+c\): its coefficient is \(J_{\alpha,\beta}\). For each degree \(d\ge2\), the affine linear map from its free coefficients to \((f(0),f(1))\) is surjective with every ordered pair having exactly \(q^{d-2}\) preimages. Hence for nontrivial \((\alpha,\beta)\) the coefficient is \(q^{d-2}(\sum_u\alpha(u))(\sum_v\beta(v))=0\). For the trivial pair, there are \((q-1)^2q^{d-2}\) monic polynomials not divisible by either \(X\) or \(X-1\). Summing \(1+(q-2)T+(q-1)^2\sum_{d\ge2}q^{d-2}T^d\) gives \((1-T)^2/(1-qT)\), proving both branches.

**2. Squarefree and signed Euler products.** Let \(\mu(f)\) be the polynomial Möbius function: \(0\) for nonsquarefree \(f\), and \((-1)^r\) for a product of \(r\) distinct monic irreducibles. Formal Euler products over irreducibles other than \(X\) and \(X-1\) imply exactly
\[
\sum_{f\ \mathrm{monic}}\mu(f)\eta_{\alpha,\beta}(f)T^{\deg f}=L_{\alpha,\beta}(T)^{-1},
\quad
\sum_{f\ \mathrm{monic}}\mu(f)^2\eta_{\alpha,\beta}(f)T^{\deg f}=\frac{L_{\alpha,\beta}(T)}{L_{\alpha^2,\beta^2}(T^2)}.
\]
The squarefree identity follows prime by prime from \(1+z=(1-z^2)/(1-z)\). All manipulations are formal and require no convergence.

**3. Fibres and discriminants.** Multiplicative-character orthogonality recovers the restriction \(f(0)=a\), \(f(1)=b\) by multiplying the \((\alpha,\beta)\) series by \(\overline{\alpha(a)\beta(b)}\), summing, and dividing by \((q-1)^2\). For monic \(f\) in odd characteristic, Pellet's discriminant identity (also called the Stickelberger–Swan parity formula) states
\[
\chi_q(\operatorname{Disc}f)=(-1)^n\mu(f),
\]
where the quadratic character \(\chi_q\) has value zero at zero. A squarefree polynomial contributes \(1\) to the sum of the two squareclass indicators, and its sign to their difference. The two Euler identities and orthogonality therefore give the announced \(N_\pm\) formula. Extracting \([T^n]\) from \(L_{\mathbf1,\mathbf1}(T)^{-1}=(1-qT)/(1-T)^2\) gives \(1-(q-1)n\) for \(n\ge2\), and extracting it from \((1+JT)^{-1}\) gives \((-J)^n\), proving the explicit bias formula.

**4. The exceptional field.** For \(q=3\) the character group has two elements \(\mathbf1,\varepsilon\). Only \(c=1\) remains in the Jacobi sum; explicitly \(J_{\varepsilon,\mathbf1}=1\) and \(J_{\mathbf1,\varepsilon}=J_{\varepsilon,\varepsilon}=-1\). Substitution gives the displayed four-value formula. If \(n\) is even, three choices of \((\varepsilon(a),\varepsilon(b))\) give bias \(-n/2\), and the fourth gives \(1-n/2\). If \(n\) is odd, one choice gives bias \((n+1)/2\), the other three give \((n-1)/2\). Thus in both cases the sharp maximum absolute value is \(\lceil n/2\rceil\).

**5. Exponential growth for larger fields.** If \(q\ge5\), choose a generator \(\rho\) of the cyclic group \(\mathcal X\), so \(\rho\), \(\rho\) and \(\rho^2\) are all nontrivial. The standard Gauss-sum identity for Jacobi sums gives \(|J_{\rho,\rho}|=\sqrt q\). The double finite Fourier transform of \(B_{n,q}\) at \((\rho,\rho)\) is exactly \((-1)^n(-J_{\rho,\rho})^n\), of modulus \(q^{n/2}\). Since the transform sums \((q-1)^2\) values each bounded by their largest absolute value, the lower bound follows. For the upper bound, every nontrivial-pair Jacobi sum has modulus at most \(\sqrt q\) (and degenerate cases have modulus at most \(1\)); apply the triangle inequality to the explicit bias formula. Since \(|1-(q-1)n|=(q-1)n-1\) for \(n\ge2\), the upper bound is at most \(((q-1)^2-1)q^{n/2}/(q-1)^2+n/(q-1)\le q^{n/2}+n/(q-1)\). This proves every assertion.

## Verification

Run `python3 verify.py` using Python's standard library. The script constructs \(\mathbb F_3,\mathbb F_5,\mathbb F_7\), and \(\mathbb F_9\) independently, enumerates complete polynomial fibres, computes discriminants using an exact Sylvester determinant, and independently predicts them with the two formal character-Euler series. Tested degree cutoffs are respectively \(7,5,4,4\); the script compares \(388\) degree/value fibres arising from \(11,828\) directly enumerated polynomials and tests the exact \(q=3\) formula and field-size bounds. Computed data are finite corroboration; the proof above covers all odd prime powers and every degree at least two.

## Relationship to prior work

Almousa and Wood (2012 preprint) count finite-field polynomials with given root-multiplicity patterns without these two evaluation constraints. Chan, Kwon and Seaman (2018 preprint) study the unconditional distribution of finite-field discriminants; their unconditional distribution does not determine a conditional distribution at \(f(0)=a,f(1)=b\). Lalín and Larocque (2016) count **irreducible** polynomials with two prescribed **leading coefficients**, rather than squarefree discriminant classes under two prescribed values. The standard polynomial Möbius/discriminant identity and Jacobi-sum magnitude formula are classical tools, not claimed as new. The proposed contribution is the explicit two-point **complete squareclass fibre** formula and its exact linear-versus-exponential field-size transition. A more general classical character-L-function result for modulus \(X(X-1)\) might implicitly subsume these formulas; the comparison is not exhaustive.

## Limitations

There is no claim of originality for the underlying Euler-product, Jacobi-sum or discriminant parity identities. The result excludes characteristic two, zero prescribed evaluations, and degree one. It counts only square versus nonsquare **nonzero** discriminants, not the individual values of discriminants and not irreducible polynomials alone. The upper and lower bias bounds are of the same exponential order for each fixed \(q\), not generally equal. No independent audit or exhaustive literature certification has been performed.

## References

1. A. Almousa and M. M. Wood, *Counting polynomials over finite fields with given root multiplicities*, arXiv:1210.0472v1 (first posted 2012-10-01), https://arxiv.org/abs/1210.0472.
2. J. Chan, S. Kwon and M. Seaman, *On the Distribution of Discriminants over a Finite Field*, arXiv:1812.06231v1 (2018), https://arxiv.org/abs/1812.06231.
3. M. Lalín and O. Larocque, *The Number of Irreducible Polynomials with the First Two Prescribed Coefficients over a Finite Field*, Rocky Mountain Journal of Mathematics 46 (2016), 1587–1618, doi:10.1216/rmj-2016-46-5-1587.
4. Classical identities: polynomial Möbius Euler products; Pellet–Stickelberger–Swan formula; Gauss and Jacobi sums.
