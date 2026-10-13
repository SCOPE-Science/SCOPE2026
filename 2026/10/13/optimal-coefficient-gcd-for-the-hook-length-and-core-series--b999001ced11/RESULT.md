# Optimal coefficient gcd for the hook-length and core series

## Finding
For each integer \(t\ge 2\), write
\[
E(x)=\prod_{j\ge1}(1-x^j),\qquad
F_t(x)=E(x)^{t^2-1}=\sum_{n\ge0}a_t(n)x^n,
\]
\[
C_t(x)=\frac{E(x^t)^t}{E(x)}=\sum_{n\ge0}b_t(n)x^n,
\qquad d_t(n)=a_t(n)-b_t(n).
\]
These are, respectively, the Nekrasov--Okounkov specialization at the square parameter \(t^2\), the generating series for \(t\)-core partitions, and their coefficient difference. Define the **coefficient content**
\[
g(t)=\gcd\{d_t(n):n\ge0\},
\]
where the nonnegative generator of the ideal of differences is intended; it is nonzero since \(d_t(1)=-t^2\).

**Theorem (exact content, including the first sharp obstruction).** For every \(t\ge2\),
\[
\boxed{g(t)=
\begin{cases}
p^{a+1},&t=p^a\quad(p\text{ prime},\ a\ge1),\\
1,&t\text{ has at least two distinct prime factors}.
\end{cases}}
\]
More precisely:

* If \(t=p^a\) and \(h=p^{a-1}\), then \(d_t(n)\equiv0\pmod{p^{a+1}}\) for every \(n\ge0\), while
\[
 d_t(n)\equiv0\pmod{p^{a+2}}\ (0\le n<h),\qquad
 \boxed{d_t(h)\equiv-p^{a+1}\pmod{p^{a+2}}.}
\]
In particular, \(h\) is the first coefficient index witnessing the optimality of the universal modulus.
* If \(t=p^a m\), \(p\nmid m\), \(m>1\), and \(h=p^{2a}\), then
\[
 d_t(n)\equiv0\pmod p\ (0\le n<h),\qquad
 \boxed{d_t(h)\equiv-m^2\pmod p.}
\]
Thus \(h\) is the first failure index modulo \(p\) for each prime factor \(p\) of a non-prime-power \(t\).

## Assumptions and scope
All products and congruences are identities in \(\mathbb Z[[x]]\), with coefficientwise reduction modulo positive integer powers of primes. No analytic convergence, modularity assumption, or finite truncation hypothesis is needed. The integer \(t\) ranges over **all** \(t\ge2\); primes include \(p=2\). The definitions of \(F_t\) and \(C_t\) above fix the indexing throughout: \(F_t\) has exponent \(t^2-1\), not \(t-1\). The coefficient gcd uses every \(n\ge0\).

## Proof
Put \(E_j(x)=E(x^{p^j})\) for a fixed prime \(p\). We first use two elementary formal-series facts.

**Frobenius:** if \(A(x)\in 1+x\mathbb Z[[x]]\), then
\[
 A(x)^{p^r}\equiv A(x^{p^r})\pmod p
 \qquad(r\ge0).
\]
Indeed, reduction modulo \(p\) is a ring homomorphism and the \(p\)-th-power map is Frobenius; iterate it.

**Integral lifting:** if \(B(x)\in1+p^s\mathbb Z[[x]]\) for \(s\ge1\), then
\[
 B(x)^p\in1+p^{s+1}\mathbb Z[[x]],
\qquad B(x)^{p^r}\in1+p^{s+r}\mathbb Z[[x]].
\]
For the first inclusion, expand \((1+p^s V)^p\). The linear term has valuation at least \(s+1\), the intermediate binomial coefficients are multiples of \(p\), and the last term is divisible by \(p^{sp}\), which is at least \(p^{s+1}\), including \(p=2\). Induct on \(r\).

**Prime-power case.** Let \(t=p^a\), \(a\ge1\), and set
\[
 H(x)=\frac{E(x)^{p^a}}{E(x^{p^a})},\qquad
 R(x)=\frac{F_t(x)}{C_t(x)}=H(x)^{p^a}.
\]
The Frobenius congruence gives \(H\in1+p\mathbb Z[[x]]\); lifting gives \(R\in1+p^{a+1}\mathbb Z[[x]]\). Because \(C_t\in1+x\mathbb Z[[x]]\), it follows that \(F_t-C_t=C_t(R-1)\) is divisible by \(p^{a+1}\) coefficientwise.

To locate the first optimality witness, set \(h=p^{a-1}\). Frobenius gives \(E(x)^{p^{a-1}}\equiv E(x^h)\pmod p\). Raising this congruence to the \(p\)-th power increases the precision to \(p^2\), so
\[
 H(x)=\frac{E(x)^{p^a}}{E(x^{ph})}
 \equiv\frac{E(x^h)^p}{E(x^{ph})}\pmod{p^2}.
\]
Since \(E(y)=1-y+O(y^2)\) and \(p\ge2\), the quotient on the right is \(1-py+O(y^2)\) with \(y=x^h\). Thus all coefficients of \(H-1\) below degree \(h\) are divisible by \(p^2\), whereas \([x^h]H\equiv-p\pmod{p^2}\).

Work modulo \(x^{h+1}\). Write
\[
 H(x)=L(x)(1+u x^h)\pmod{x^{h+1}},
\]
where \(L(0)=1\), every nonconstant coefficient of \(L\) is divisible by \(p^2\), and \(u=[x^h]H\equiv-p\pmod{p^2}\). Lifting implies \(L^{p^a}\equiv1\pmod{p^{a+2}}\), while \((1+ux^h)^{p^a}\equiv 1+p^a u x^h\pmod{x^{h+1}}\). Consequently,
\[
 [x^n](R-1)\equiv0\pmod{p^{a+2}}\quad(0\le n<h),
\]
\[
 [x^h](R-1)\equiv-p^{a+1}\pmod{p^{a+2}}.
\]
Multiplication by \(C_t\), whose constant coefficient is \(1\), preserves these statements for \(d_t(n)=[x^n]C_t(R-1)\). Thus the gcd has \(p\)-adic valuation exactly \(a+1\), with earliest witness \(h\). No other prime can divide the gcd because \(d_t(1)=-t^2\). This proves \(g(p^a)=p^{a+1}\).

**Non-prime-power case.** Let \(p\mid t\) and write \(t=p^a m\) with \(a\ge1\), \(p\nmid m\), \(m>1\). Define \(R=F_t/C_t=E(x)^{t^2}/E(x^t)^t\). Frobenius in characteristic \(p\) yields
\[
 R(x)\equiv\frac{E(x^{p^{2a}})^{m^2}}{E(x^{p^{2a}m})^m}\pmod p.
\]
With \(y=x^{p^{2a}}\), this becomes \(E(y)^{m^2}/E(y^m)^m\equiv1-m^2y+O(y^2)\pmod p\), because \(m>1\). Hence every coefficient below \(p^{2a}\) in \(R-1\) vanishes modulo \(p\), and the coefficient at that index is \(-m^2\not\equiv0\pmod p\). Multiplication by \(C_t\), a series with constant term \(1\), gives the claimed first obstruction for \(d_t\).

Finally, \(d_t(1)=-t^2\), so any prime dividing \(g(t)\) must divide \(t\). For each such prime in the non-prime-power case, the witness above proves that \(p\nmid g(t)\). Therefore \(g(t)=1\). This completes the proof. \(\square\)

## Verification
A standalone standard-library script, `verify.py`, computes the two coefficient sequences using independent logarithmic-derivative recurrences. For \(2\le t\le40\) it compares the finite coefficient gcd with the exact formula, verifies the first failures at every prime factor, and checks the stronger prime-power congruence through a nontrivial finite range. For \(2\le t\le7\), it additionally compares the recurrences with direct multiplication of finite Euler products. Run with `python3 verify.py`; expected output is supplied in `verification_output.txt`.

The coefficient recurrences used are, with \(\sigma_1(k)=\sum_{d\mid k}d\),
\[
 n a_t(n)=-(t^2-1)\sum_{k=1}^n\sigma_1(k)a_t(n-k),
\]
\[
 n b_t(n)=\sum_{k=1}^n
 \left(\sigma_1(k)-t^2\mathbf1_{t\mid k}\sigma_1(k/t)\right)b_t(n-k).
\]
All computations are over exact integers. These tests are consistency checks, not proofs for unbounded \(t\) or \(n\); the formal-series argument above supplies the infinite proof.

## Relationship to prior work
Sharma, *A Prime-Power Dichotomy for Nekrasov--Okounkov Hook Lengths and \(t\)-Core Partitions* (arXiv:2610.01422v1, first public 2026-10-01), proves universal equality modulo \(t\) exactly when \(t\) is a prime power, and modulo \(p^2\) for the prime specialization \(t=p\). Its Section 3 treats composite non-prime-power failure and its Section 4 exhibits a failure index bounded by \(p^{2a}\). That paper does **not** state or prove the optimal uniform modulus \(p^{a+1}\) for every exponent \(a\), its sharp first obstruction at \(p^{a-1}\), or the complete integer coefficient content \(g(t)\). The non-prime-power part here is included to make the content classification exhaustive and is not claimed as independently new.

Han and Ono, *Hook Lengths and 3-Cores* (arXiv:0805.2461; Annals of Combinatorics 15 (2011), 305–312), establish equality of zero sets for \(F_9\) and \(C_3\), rather than an optimal congruence for all prime powers. Their formulas and the classical Nekrasov--Okounkov identity justify the natural objects under comparison. The exact exponent and earliest failure for arbitrary prime-power \(t\) are the added contributions.

## Limitations
The statement concerns the **common gcd of all coefficients** of these two fixed generating series; it does not describe valuations of individual coefficients beyond the earliest sharp witness, nor any analytic zero-set correspondence at general \(t\). It uses coefficientwise congruence, not equality of series. Novelty comparisons are limited to the inspected primary sources and searchable published records; a logically equivalent formulation in other literature could exist. No independent expert audit is asserted.

## References
1. M. Sharma, *A Prime-Power Dichotomy for Nekrasov--Okounkov Hook Lengths and \(t\)-Core Partitions*, arXiv:2610.01422v1 (2026-10-01), https://arxiv.org/html/2610.01422v1. Primary MSC: 11P83, 11P84.
2. G.-N. Han and K. Ono, *Hook Lengths and 3-Cores*, arXiv:0805.2461 (2008); *Annals of Combinatorics* **15** (2011), 305–312, https://uva.theopenscholar.com/files/ken-ono/files/117_8.pdf.
3. G.-N. Han, *The Nekrasov–Okounkov hook length formula: Refinement, elementary proof, extensions and applications*, *Annales de l'Institut Fourier* **60** (2010), 1–29 (background identity, cited in [1] and [2]).
