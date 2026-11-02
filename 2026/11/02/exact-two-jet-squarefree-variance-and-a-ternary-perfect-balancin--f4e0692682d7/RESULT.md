# Exact two-jet squarefree variance and a ternary perfect-balancing law

## Finding

Let \(q\) be an odd prime power and \(n\ge 2\). For each \(a\in\mathbb F_q^\times\) and \(u\in\mathbb F_q\), let \(C_{q,n}(a,u)\) count monic squarefree degree-\(n\) polynomials \(f\in\mathbb F_q[T]\) satisfying
\[
f(0)=a,\qquad f'(0)/f(0)=u.
\]
In other words, the congruence class of \(f\) modulo \(T^2\) is \(a(1+uT)\). Put \(M=q(q-1)\) and
\[
\mu_{q,n}=\frac{q^n-(-1)^n}{q(q+1)}.
\]
The **unnormalized variance across all invertible residue classes modulo \(T^2\)** is
\[
\boxed{\sum_{a\in\mathbb F_q^\times}\sum_{u\in\mathbb F_q}
(C_{q,n}(a,u)-\mu_{q,n})^2
=\frac{(q-3)q^{\lceil n/2\rceil}+q+1}{q}.}
\]
The normalized variance is the right-hand side divided by \(q(q-1)\).

There is a sharp, all-degree perfect-balancing classification: **all \(q(q-1)\) integers \(C_{q,n}(a,u)\) differ pairwise by at most one if and only if \(n=2\) or \(q=3\)**.

More precisely, at \(q=3\), identify \(\mathbb F_3^\times=\{1,-1\}\). For even \(n\), the four classes with \(a=-1\) or \(u=0\) have count \((3^n+3)/12\), and the remaining two have count \((3^n-9)/12\). For odd \(n\), the two classes with \(u=a\) have count \((3^n+9)/12\), and the remaining four have count \((3^n-3)/12\).

## Assumptions and scope

The field has odd characteristic, including nonprime finite fields. Degree \(n\) is any integer at least two. The leading coefficient is one, and the constant coefficient is required to be nonzero. The ratio \(f'(0)/f(0)\) is a member of the field, so its prescription is equivalent to fixing the coefficient of \(T\) together with the nonzero constant term. Squarefreeness means \(\gcd(f,f')=1\) in \(\mathbb F_q[T]\). The variance here is a **sum**, not the average over classes.

## Proof

**1. Characters of the two-jet group.** Multiplication of units modulo \(T^2\) identifies
\[
G=(\mathbb F_q[T]/T^2)^\times\cong\mathbb F_q^\times\times(\mathbb F_q,+),\qquad f\longmapsto (a=f(0),u=f'(0)/f(0)).
\]
For a multiplicative character \(\eta\) and additive character \(\psi\), let \(\chi(f)=\eta(a)\psi(u)\) when \(f(0)\ne0\), extended by zero otherwise. These \(M=q(q-1)\) characters are all the characters of \(G\).

Define the monic-polynomial series
\[
L_{\eta,\psi}(z)=\sum_{\substack{f\text{ monic}\\f(0)\ne0}}\eta(f(0))\psi(f'(0)/f(0))z^{\deg f}.
\]
For the trivial pair, \(L_{1,1}(z)=(1-z)/(1-qz)\). When \(\psi=1\) and \(\eta\ne1\), the sum over nonzero constant terms vanishes in every positive degree, so \(L_{\eta,1}(z)=1\). When \(\psi\ne1\), every degree at least two contributes zero: for each fixed nonzero constant term and all coefficients except that of \(T\), the latter ranges over the entire additive field, making the nontrivial \(\psi\)-sum vanish. The degree-one coefficient is
\[
J(\eta,\psi)=\sum_{a\in\mathbb F_q^\times}\eta(a)\psi(a^{-1}),\qquad L_{\eta,\psi}(z)=1+J(\eta,\psi)z.
\]
A change of variables to \(a^{-1}\) identifies \(J\) with an ordinary mixed Gauss sum. Thus for nontrivial \(\psi\),
\[
|J(1,\psi)|^2=1,\qquad |J(\eta,\psi)|^2=q\quad(\eta\ne1).
\]
These equalities also follow directly by expanding the squared sums and using additive-character orthogonality.

**2. Squarefree character coefficients.** Every monic polynomial with nonzero constant term uniquely factors as \(gh^2\), with \(g\) monic squarefree and \(h\) monic. Multiplicativity, including the vanishing on factors with zero constant term, yields the exact formal identity
\[
U_{\eta,\psi}(z):=\sum_{n\ge0}c_n(\eta,\psi)z^n
=\frac{L_{\eta,\psi}(z)}{L_{\eta^2,\psi^2}(z^2)},
\]
where \(c_n(\eta,\psi)\) is the \(\chi\)-weighted count of monic squarefree degree-\(n\) polynomials. This is the standard character generating-function identity used in squarefree arithmetic-progressions research.

For the trivial pair,
\[
U_{1,1}(z)=\frac{1-qz^2}{(1-qz)(1+z)},\qquad
c_n(1,1)=\frac{(q-1)(q^n-(-1)^n)}{q+1}\quad(n\ge1).
\]
Consequently \(\mu_{q,n}=c_n(1,1)/M\), exactly as stated.

For \(\psi=1\) and nontrivial \(\eta\), the nontrivial quadratic character \(\eta_2\) is the only character whose square is trivial. It contributes
\[
U_{\eta_2,1}(z)=\frac{1-qz^2}{1-z^2},\qquad
c_n(\eta_2,1)=\begin{cases}1-q,&n\ge2\text{ even},\\0,&n\text{ odd},\end{cases}
\]
and every other nontrivial \(\eta\) gives \(c_n(\eta,1)=0\) for \(n\ge2\).

For \(\psi\ne1\), odd characteristic ensures \(\psi^2\ne1\), so
\[
U_{\eta,\psi}(z)=\frac{1+J(\eta,\psi)z}{1+J(\eta^2,\psi^2)z^2}.
\]
Writing \(n=2m\) or \(n=2m+1\), we have, for \(m\ge1\),
\[
 c_{2m}(\eta,\psi)=(-J(\eta^2,\psi^2))^m,
\qquad
 c_{2m+1}(\eta,\psi)=J(\eta,\psi)(-J(\eta^2,\psi^2))^m.
\]
There are exactly two multiplicative characters with \(\eta^2=1\) and \(q-3\) with \(\eta^2\ne1\).

**3. Exact Parseval calculation.** Character orthogonality on \(G\) gives
\[
C_{q,n}(a,u)=\frac1M\sum_{\eta,\psi}c_n(\eta,\psi)\overline{\eta(a)\psi(u)}.
\]
Parseval therefore gives
\[
W_{q,n}=\sum_{a,u}(C_{q,n}(a,u)-\mu_{q,n})^2
=\frac1M\sum_{(\eta,\psi)\ne(1,1)}|c_n(\eta,\psi)|^2.
\]
For \(n=2m\ge2\), the \(q-1\) nontrivial additive characters contribute
\[
(q-1)\bigl(2+(q-3)q^m\bigr),
\]
and the single quadratic character with trivial additive part contributes \((q-1)^2\). For \(n=2m+1\ge3\), the entire nontrivial contribution is
\[
(q-1)\bigl(1+q+(q-3)q^{m+1}\bigr).
\]
Dividing by \(M=q(q-1)\) yields the boxed variance formula in both parities.

**4. Exactly balanced fibres.** When \(n=2\), prescribing \(a\) and \(u\) fixes the unique monic quadratic \(T^2+auT+a\). Each class therefore has zero or one squarefree polynomial, so is balanced for every odd \(q\).

When \(q=3\), write \(\omega=e^{2\pi i/3}\), and use the two characters \(\psi_j(u)=\omega^{ju}\) and the quadratic character \(\eta_2(a)=a\in\{1,-1\}\). The Gauss sums are \(J(1,\psi_j)=-1\) and \(J(\eta_2,\psi_j)=\omega^j-\omega^{-j}\). In even degree the nontrivial Fourier coefficients are \(c_n(\eta_2,1)=-2\) and \(c_n(\eta,\psi_j)=1\), yielding discrepancy \(+1/3\) for \(a=-1\) or \(u=0\) and \(-2/3\) otherwise. In odd degree at least three, \(c_n(\eta_2,1)=0\), \(c_n(1,\psi_j)=-1\), and \(c_n(\eta_2,\psi_j)=\omega^j-\omega^{-j}\), yielding discrepancy \(+2/3\) when \(u=a\), and \(-1/3\) otherwise. Adding \(\mu_{3,n}\) gives the two exact tables in the finding.

Conversely, for any \(M\) integers differing pairwise by at most one, the sum of their squared deviations from their mean is at most \(M/4\): if a proportion \(\theta\) take the larger of two adjacent values, their unnormalized variance is \(M\theta(1-\theta)\le M/4\). For \(q\ge5\), \(n\ge3\), our expression satisfies
\[
W_{q,n}\ge \frac{(q-3)q^2+q+1}{q}=q(q-3)+1+q^{-1}>\frac{q(q-1)}4=\frac M4.
\]
Thus perfect balancing is impossible for every \(q\ge5\) and \(n\ge3\). The classification follows.

## Verification

The standalone file `verify_squarefree_variance.py` independently enumerates monic polynomials, computes formal derivatives and polynomial greatest common divisors over finite prime and extension fields, tabulates \(C_{q,n}(a,u)\), and checks the exact rational variance and, for \(q=3\), the entire two-valued fibre table. Run `python3 verify_squarefree_variance.py`. The enumerated cases are \(q=3\) for degrees \(2\) through \(7\), \(q=5\) for degrees \(2\) through \(5\), \(q=7\) for degrees \(2\) through \(4\), \(q=11\) for degrees \(2,3\), and \(q=9\) for degrees \(2,3\), totaling 17 field/degree tests. These checks are finite corroboration, not a substitute for the proof of arbitrary \(q,n\).

## Relationship to prior work

Keating and Rudnick, *Squarefree polynomials and Möbius values in short intervals and arithmetic progressions* (arXiv:1504.03444v1; initial posting April 14, 2015), supply the general Dirichlet-character Parseval formula (their Eq. (10.3)) and the squarefree generating-function quotient (their Eq. (10.4)). Their Theorem 10.1 studies the large-field limit with **squarefree** moduli, whereas \(T^2\) is **not** squarefree. The first two proof steps here instantiate those known identities; the exact special-character evaluation, all-degree closed second moment, explicit ternary fibre pattern, and global perfect-balancing classification are the additional claims. The quoted general identities alone do not state these evaluated outcomes.

McGuire and Yılmaz (arXiv:1609.02314v1) treat irreducible-polynomial counts with two **leading** coefficients prescribed, not these squarefree counts for the constant and linear coefficients. Oppenheim and Shusterman (arXiv:1707.06528v1) establish squarefree-existence results in coefficient-restricted settings rather than this exact progression variance. The latter is supporting literature published after the historical source cutoff, not the provenance of the current motivating question. Equivalence to a wider, unlocated character-table formula remains a bibliographic risk.

## Limitations

The statement requires odd characteristic, a nonzero constant coefficient and degree at least two. It computes a second moment for general odd \(q\), not all individual fibres (except when \(q=3\)). It does not address higher powers of the modulus, multiple prescribed coefficients or analogous characteristic-two results. The proof is mathematical rather than a claim of independent audit or priority certification.

## References

1. J. P. Keating and Z. Rudnick, *Squarefree polynomials and Möbius values in short intervals and arithmetic progressions*, arXiv:1504.03444v1, April 14, 2015, Section 10, Equations (10.3) and (10.4), Theorem 10.1. https://arxiv.org/abs/1504.03444
2. G. McGuire and E. S. Yılmaz, *The Number of Irreducible Polynomials with the First Two Coefficients Fixed over Finite Fields of Odd Characteristic*, arXiv:1609.02314v1, September 8, 2016. https://arxiv.org/abs/1609.02314
3. B. Oppenheim and M. Shusterman, *Squarefree polynomials with prescribed coefficients*, arXiv:1707.06528v1, July 2017. https://arxiv.org/abs/1707.06528
