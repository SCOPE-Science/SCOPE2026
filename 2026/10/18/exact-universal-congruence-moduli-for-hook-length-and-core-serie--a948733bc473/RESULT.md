# Exact universal congruence moduli for hook-length and core series

## Finding

Let \(t\ge 2\) be an integer and write
\[
A(x)=\prod_{j\ge1}(1-x^j),\qquad
F_{t^2}(x)=A(x)^{t^2-1}=\sum_{n\ge0}a_t(n)x^n,
\qquad C_t(x)=\frac{A(x^t)^t}{A(x)}=\sum_{n\ge0}b_t(n)x^n.
\]
Define the content \(g_t\) of the coefficient difference to be the positive greatest common divisor
\[
g_t=\gcd\{\lvert a_t(n)-b_t(n)\rvert:n\ge0\}.
\]
Then **the exact universal congruence modulus** is
\[
\boxed{g_t=\begin{cases}
p^{a+1},&t=p^a\text{ for a prime }p\text{ and integer }a\ge1,\\
1,&t\text{ has at least two distinct prime factors}.
\end{cases}}
\]
More precisely, for \(t=p^a\) and \(d=p^{a-1}\),
\[
a_t(n)-b_t(n)\equiv0\pmod{p^{a+2}}\quad(0\le n<d),\qquad
a_t(d)-b_t(d)\equiv-p^{a+1}\pmod{p^{a+2}}.
\]
Thus the strengthening from modulus \(p^{a+1}\) to \(p^{a+2}\) first fails at **exactly** degree \(p^{a-1}\). If \(p\mid t\) with \(t=p^a m\), \(a\ge1\), \(m>1\), and \(p\nmid m\), the first failure modulo \(p\) instead occurs at degree \(p^{2a}\), with difference congruent to \(-m^2\) there; this non-prime-power behavior is included for completeness and accords with the motivating literature.

## Assumptions and scope

All products and congruences are coefficientwise in \(\mathbb Z[[x]]\). Powers of the Euler product are nonnegative integral powers. The content is well defined: the degree-one coefficient of \(F_{t^2}-C_t\) is \(-t^2\), and therefore not all its coefficients vanish. The theorem applies to **all** integers \(t\ge2\) and **all** nonnegative coefficient indices, with no numerical cutoff.

## Proof

**1. Remove the common unit.** Put
\[
H_t(x)=A(x)\bigl(F_{t^2}(x)-C_t(x)\bigr)
=A(x)^{t^2}-A(x^t)^t.
\]
Since \(A(0)=1\) and \(A(x),A(x)^{-1}\in\mathbb Z[[x]]\), multiplication by \(A\) preserves the set of positive integers dividing **all** coefficients, hence preserves their gcd. It also preserves the degree and leading residue of the first nonzero coefficient modulo any fixed modulus: the constant coefficient of \(A\) is \(1\).

**2. A lifting fact.** For any \(U,V\in\mathbb Z[[x]]\), prime \(p\), and \(s\ge1\),
\[
U\equiv V\pmod{p^s}\quad\Longrightarrow\quad
U^p\equiv V^p\pmod{p^{s+1}}.
\]
Indeed, write \(U=V+p^sR\) and expand. The linear cross term contains \(p^{s+1}\); for \(2\le j<p\) the term with \(R^j\) contains \(\binom pj p^{sj}\), divisible by \(p^{s+1}\); and the final term contains \(p^{sp}\), also divisible by \(p^{s+1}\). For \(p=2\), the middle range is empty and the same argument holds.

**3. Prime-power divisibility.** Suppose \(t=p^a\). The formal-series Frobenius identity yields
\[
A(x)^{p^a}\equiv A(x^{p^a})\pmod p.
\]
Applying the lifting fact successively \(a\) times gives
\[
H_{p^a}(x)=\bigl(A(x)^{p^a}\bigr)^{p^a}
-A(x^{p^a})^{p^a}\equiv0\pmod{p^{a+1}}.
\]
This is a coefficientwise congruence in the entire infinite formal series, not merely a finite truncation.

**4. Sharpness and the first obstruction.** Put \(N=p^{2a}\) and \(d=p^{a-1}\). For every \(1\le j\le N\),
\[
\nu_p\left(\binom Nj\right)=2a-\nu_p(j).
\]
To see this, use \(\binom Nj=(N/j)\binom{N-1}{j-1}\) and
\(\binom{N-1}{j-1}\equiv(-1)^{j-1}\pmod p\), since
\((1+x)^{N-1}\equiv (1+x^N)/(1+x)\pmod p\) through degree \(N-1\).

Expand the product \(A(x)^N=\prod_{m\ge1}(1-x^m)^N\). For a positive coefficient of degree \(n<d\), every nonconstant factor uses a binomial index \(1\le j\le n<d\), and therefore \(\nu_p(j)\le a-2\). Each such binomial coefficient is divisible by \(p^{a+2}\), so all coefficients of positive degree \(n<d\) are divisible by \(p^{a+2}\). The statement for \(a=1\) is vacuous because \(d=1\).

At degree \(d\), the sole term potentially not divisible by \(p^{a+2}\) takes exactly \(d\) copies of \(x\) from the \(m=1\) factor: it is \((-1)^d\binom Nd\). All other contributing monomials use only positive indices \(j<d\) and thus vanish modulo \(p^{a+2}\). Further,
\[
(-1)^d\binom Nd\equiv-p^{a+1}\pmod{p^{a+2}},
\]
because \(N/d=p^{a+1}\) and \(\binom{N-1}{d-1}\equiv(-1)^{d-1}\pmod p\). The series \(A(x^{p^a})^{p^a}\) has no nonconstant term before degree \(p^a>d\). Thus \(H_{p^a}\), and therefore \(F_{p^{2a}}-C_{p^a}\), has exactly the asserted degree-\(d\) leading residue modulo \(p^{a+2}\). It follows that the valuation of its global content is exactly \(a+1\).

Finally \([x]H_t=-t^2\), hence no prime outside the prime support of \(t\) can divide the global content. This gives \(g_{p^a}=p^{a+1}\).

**5. Parameters with several prime factors.** Fix a prime \(p\mid t\) and write \(t=p^a m\), where \(a\ge1\), \(m>1\), and \(p\nmid m\). Reducing the two terms of \(H_t\) modulo \(p\) by Frobenius gives
\[
H_t(x)\equiv A(x^{p^{2a}})^{m^2}
- A(x^{p^{2a}m})^m\pmod p.
\]
All positive coefficients of degree below \(p^{2a}\) vanish modulo \(p\), whereas the coefficient in degree \(p^{2a}\) is \(-m^2\), nonzero modulo \(p\). Therefore no prime factor of \(t\) divides the content, and \([x]H_t=-t^2\) excludes primes not dividing \(t\). Consequently \(g_t=1\). This completes the classification. \(\square\)

## Verification

The standalone file `verify.py` computes exact coefficients of both numerator products using their logarithmic derivatives, and independently expands finite Euler products for selected parameters. Run `python3 verify.py` with a standard Python 3 interpreter; no additional modules are needed. The saved output is `certificate_output.txt`. Checks covered 16 prime powers and 26 integers with at least two distinct prime factors, including the predicted first obstruction indices: 5,637 modular coefficient tests and 460 independent finite-product coefficient comparisons passed. These computations verify examples only; the five steps above prove the infinite claims.

## Relationship to prior work

Sharma's 2026 prime-power dichotomy proves global congruence modulo \(t=p^a\) and the stronger prime case modulo \(p^2\), and identifies non-prime-power failure modulo prime divisors of \(t\). Section 5 points toward possible higher-order lifts. The present claim upgrades the entire prime-power family to the **exact maximal common modulus** \(p^{a+1}\), identifies its **first failure degree** at the next modulus, and combines this with the established non-prime-power dichotomy into an exact content classification. The new prime-power bound is not supplied by the cited \(p^a\) result alone. Han and Ono establish zero-set equivalence for the parameter \(t=3\); this does not imply coefficientwise sharp content. Classical tables give particular Euler-product coefficients but not the all-parameter theorem.

## Limitations

No claim is made about a maximal modulus for any proper subsequence of indices, a signed coefficient formula, or additional prime-power lifting after restricting degrees. This establishes coefficientwise congruence and its exact common modulus, not an identity of the series. Published literature may contain an earlier equivalent formulation not located in the searches; the exact single-series coefficients and stronger subsequence congruences remain outside scope.

## References

- M. Sharma, *A Prime-Power Dichotomy for Nekrasov--Okounkov Hook Lengths and \(t\)-Core Partitions* (2026), arXiv:2610.01422v1, https://arxiv.org/html/2610.01422v1.
- G.-N. Han and K. Ono, *Hook Lengths and 3-Cores* (2008 preprint; journal version 2011), arXiv:0805.2461v1, https://arxiv.org/html/0805.2461v1.
- G.-N. Han, *The Nekrasov-Okounkov hook length formula: refinement, elementary proof, extension and applications*, Ann. Inst. Fourier **60** (2010), https://doi.org/10.5802/aif.2515.
- OEIS A000731, Euler product of exponent eight, https://oeis.org/A000731; OEIS A033687, 3-core partition counting coefficients, https://oeis.org/A033687.
