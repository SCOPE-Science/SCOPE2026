# Ordered squarefree factorization coefficients of the affine generalized Möbius function

## Finding

Let \(f_c(m)=1+c(m-1)\) for positive integers \(c,m\). Define \(s_c(1)=1\) and, as in the generalized Möbius recurrence of Andrews, Kauffman and Sahoo [1],
\[
s_c(n)=1-n-\sum_{d=2}^{n-1}s_c(d)f_c(\lfloor n/d\rfloor)\qquad(n\ge2).
\]
For \(n=\prod_{i=1}^h p_i^{e_i}\ge2\) write \(K=\Omega(n)=\sum_i e_i\) and \(E=\max_i e_i\). Then the full polynomial in \(t=c-1\) is
\[
s_c(n)=(-1)^K\sum_{r=1}^K N_r(n)t^{r-1},
\]
where \(N_r(n)\) counts ordered factorizations of \(n\) into \(r\) squarefree integers greater than one. In particular,
\[
N_r(n)=\sum_{j=0}^r(-1)^{r-j}\binom rj\prod_i\binom j{e_i},\qquad
N_E(n)=\prod_i\binom E{e_i},\qquad N_K(n)=\frac{K!}{\prod_i e_i!}.
\]
The polynomial has degree \(K-1\), has vanishing order exactly \(E-1\) at \(c=1\), and has sign \((-1)^K\) for all integer \(c\ge2\). The coefficient formula applies also to composites with several distinct prime factors and repeated exponents.

## Proof

Add the terms with \(d=1\) and \(d=n\) to the recurrence. It becomes \(\sum_{d\le n}s_c(d)f_c(\lfloor n/d\rfloor)=1-n+f_c(n)\), valid also at \(n=1\). Subtract the corresponding identity at \(n-1\): for \(d<n\) the floor changes by one exactly when \(d\mid n\), in which case the affine input changes by \(c\). Thus
\[
s_c(n)=-1-c\sum_{1<d<n,\ d\mid n}s_c(d)\qquad(n\ge2).
\]
Let \(u\) be the constant-one function, \(\varepsilon\) the convolution identity, \(\mu\) the classical Möbius function, and \(L=\varepsilon-\mu\). The proper-divisor recurrence is the convolution identity \(s_c*(cu-t\varepsilon)=t u+(1-t)\varepsilon\). Convolving with \(\mu\) gives \(s_c*(\varepsilon+tL)=\varepsilon+(t-1)L\). Since \(L(1)=0\), the inverse is the geometric series in \(-tL\), coefficientwise finite on each integer. Consequently
\[
s_c=\varepsilon-\sum_{r\ge1}(-t)^{r-1}L^{*r}.
\]
For a squarefree factor \(d>1\), \(L(d)=(-1)^{\Omega(d)+1}\); for all other \(d\) it is zero. Each contributing ordered factorization therefore has the same sign \((-1)^{K+r}\) in \(L^{*r}(n)\). The expansion follows, and terms beyond \(r=K\) cannot occur.

For each \(p_i\), choose its \(e_i\) distinct slots among \(j\) allowed slots. Inclusion-exclusion over slots receiving no primes gives the stated formula for \(N_r(n)\) (take \(\binom j{e_i}=0\) when \(j<e_i\)). At least \(E\) slots are needed; at exactly \(E\) slots a prime with exponent \(E\) makes every slot nonempty. At \(K\) slots each slot is occupied by just one prime, giving the multinomial count. Both extreme coefficients are positive after removing the common sign, proving the degree, vanishing order and sign assertions.

## Relation to the affine prime criterion

The sharp fixed-input threshold is also established in [2] and is not asserted here as a separate new result. The coefficient formula gives a short proof: primes have only the length-one factorization and thus value \(-1\); composites with even \(K\) have positive values for \(c\ge2\); composites with odd \(K\ge3\) have magnitude at least \((c-1)^{K-1}\ge4\) for \(c\ge3\). At \(c=1\), \(s_1(30)=\mu(30)=-1\); at \(c=2\), only length three contributes for \(n=8\), so \(s_2(8)=-1\).

The framework and divisor conversion come from [1]. The fixed-function result is not justified by the composite-case argument in [1], which varies the admissible input. The squarefree generating function in [2] determines the expansion when all exponents are one, and [2] also treats prime powers and gives a congruence modulo \(c-1\) for general inputs. The full mixed-exponent coefficient formula and the exact multiplicity at \(c=1\) are the scope here. No computational speed advantage over primality algorithms or extension to nonlinear inputs is asserted.

## Verification

The accompanying standard-library `verify.py` compares the original floor recurrence, the proper-divisor recurrence and the displayed coefficient formula for \(1\le n\le300\) and five slopes. It checks coefficient signs and the extreme coefficients for \(2\le n\le2000\). These finite checks supplement the proof. The prime-test assertions in the checker are corollary checks, not claims of originality.

## References

1. G. E. Andrews, L. H. Kauffman and D. Sahoo, *A surprising generalization of the Möbius function*, [arXiv:2609.25628v1](https://arxiv.org/html/2609.25628v1), defining recurrence and Proposition 1.
2. *Sharp affine slope threshold for fixed-function Möbius primality*, [Resultary record](https://github.com/Resultary/2026/tree/main/2026/10/18/SCOPE-sharp-affine-slope-threshold-for-fixed-function-m-bius-primality--24815ca37533), proof §§1–4.
