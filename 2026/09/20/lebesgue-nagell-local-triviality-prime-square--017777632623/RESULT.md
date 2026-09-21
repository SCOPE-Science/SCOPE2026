# Prime-square local rigidity for 31 unresolved exponents in the Lebesgue–Nagell equation

## Statement

Let
\[
\mathcal P=\{19,37,41,47,61,67,89,113,229,239,331,373,379,383,397,401,431,
479,503,593,613,617,643,691,719,787,811,877,881,907,911\}.
\]

### Theorem

For every prime \(p\in\mathcal P\), every integer solution of
\[
x^2-2=y^p
\]
satisfies
\[
y\equiv -1\pmod p,
\qquad
x\equiv \pm1\pmod{p^2}.
\]
In particular, Katz and Pratt's local-triviality conjecture holds for these 31 primes.

These primes lie among the 84 exponents \(17\le p\le 911\),
\(p\equiv13,17,19,23\pmod{24}\), that remain after the unconditional global
reductions of Chen and Katz–Pratt. The theorem is local: it does not rule out a
nontrivial integer solution for any of these exponents.

## Context

The equation \(x^2-2=y^n\) appears as an unresolved Lebesgue–Nagell problem in the
2020 survey of Le and Soydan. For odd prime exponents, Chen proved the desired
global conclusion for \(p\equiv1,5,7,11\pmod{24}\). Katz and Pratt subsequently
proved it for \(p>911\), leaving 84 prime exponents after the known small cases.
They also formulated the weaker local conjecture that every solution satisfies
\(x\equiv\pm1\pmod p\) and \(y\equiv-1\pmod p\), and obtained only the more modest
general restrictions \(x\not\equiv0\pmod p\), \(y\not\equiv0\pmod p\).

For \(p\ge17\), Katz and Pratt reduce every solution, after possibly replacing
\(x\) by \(-x\), to the single Thue equation
\[
F_p(a,b)=1,
\]
where
\[
F_p(a,b)=\sum_{k=0}^{p}\binom pk
 2^{\lfloor k/2\rfloor}a^{p-k}b^k.
\tag{1}
\]
The observation below extracts additional information from this equation modulo
\(p^2\).

## Prime-square rigidity lemma

Let \(p\) be an odd prime and put
\[
\varepsilon_p=\left(\frac2p\right)\in\{\pm1\}.
\]
Then:

1. Modulo \(p\), equation (1) is the single affine condition
   \[
   a+\varepsilon_p b\equiv1\pmod p.
   \tag{2}
   \]

2. The residue of \(F_p(a,b)\pmod{p^2}\) depends only on
   \((a,b)\pmod p\). Equivalently, for all integers \(A,B\),
   \[
   F_p(a+pA,b+pB)\equiv F_p(a,b)\pmod{p^2}.
   \tag{3}
   \]

### Proof

For \(0<k<p\), \(p\mid\binom pk\). Hence modulo \(p\) only the endpoint terms
of (1) survive:
\[
F_p(a,b)\equiv a^p+2^{(p-1)/2}b^p
\equiv a+\varepsilon_pb\pmod p,
\]
by Fermat's theorem and Euler's criterion. This proves (2).

Every coefficient occurring in either partial derivative
\(\partial F_p/\partial a\) or \(\partial F_p/\partial b\) is divisible by \(p\):
for the two endpoint derivatives the factor is visibly \(p\), while every
interior term contains \(\binom pk\). Taylor expansion with increments \(pA,pB\)
therefore gives
\[
F_p(a+pA,b+pB)\equiv F_p(a,b)
+pA\frac{\partial F_p}{\partial a}(a,b)
+pB\frac{\partial F_p}{\partial b}(a,b)
\equiv F_p(a,b)\pmod{p^2},
\]
since all terms of total increment degree at least two already contain \(p^2\).
This proves (3). ∎

Thus an exact integer solution of (1) can exist in a residue class modulo \(p\)
only if, for
\[
b\equiv\varepsilon_p(1-a)\pmod p,
\tag{4}
\]
one has
\[
F_p(a,b)\equiv1\pmod{p^2}.
\tag{5}
\]
There are only \(p\) pairs to test.

## Exact finite verification

For each of the 84 residual prime exponents \(17\le p\le911\),
\(p\equiv13,17,19,23\pmod{24}\), all pairs given by (4) were checked exactly.
For precisely the 31 primes in \(\mathcal P\), condition (5) has the unique
solution
\[
(a,b)\equiv(1,0)\pmod p.
\tag{6}
\]

The verification is performed in two arithmetically different forms and asserts
that their outputs agree. The direct form evaluates (1) modulo \(p^2\). The second
uses the identity obtained by writing
\[
(a+b\sqrt2)^p=U+V\sqrt2:
\qquad
F_p(a,b)=U+V,
\]
so it computes by binary exponentiation in
\((\mathbb Z/p^2\mathbb Z)[\sqrt2]\). The complete branch counts for all 84
exponents are recorded in `artifacts/verification.txt`.

## Proof of the theorem

The trivial solutions \((x,y)=(\pm1,-1)\) satisfy the conclusion, so suppose a
nontrivial solution exists for some \(p\in\mathcal P\).

Katz and Pratt's Theorem 5.3 gives unit exponent \(r=\pm1\) for every
\(17\le p<20000\). Their reduction in Section 3 then permits, after possibly
replacing \(x\) by \(-x\), the normalization \(r=1\), so there are integers
\(a,b\) satisfying (1). By the prime-square rigidity lemma and the exact finite
verification, (6) follows.

For the normalized solution, Katz and Pratt's Theorem 7.7 gives
\[
x-1\equiv\left(\frac2p\right)b\equiv0\pmod p.
\]
Undoing the possible sign change shows that the original solution satisfies
\[
x\equiv\pm1\pmod p.
\]
Reducing \(x^2-2=y^p\) modulo \(p\) and using \(y^p\equiv y\pmod p\) yields
\[
y\equiv x^2-2\equiv-1\pmod p.
\]
Finally, Katz and Pratt's Theorem 2.3 then upgrades the congruence for \(x\) to
\[
x\equiv\pm1\pmod{p^2}.
\]
This proves the theorem. ∎

## Limitations

This is a partial local result, not a solution of the Lebesgue–Nagell equation.
For the other 53 currently residual prime exponents, the test modulo \(p^2\) has
more than one compatible residue class, so this argument alone does not prove
local triviality there. The list \(\mathcal P\) is computer-assisted but finite,
exact, and reproducible; the mathematical reduction to the finite test is proved
above.

Originality is stated to the best of our knowledge. The most directly relevant
current source is Katz and Pratt's 2026 paper: its Conjecture 8.1 asks for local
triviality, Proposition 8.2 gives only nonvanishing modulo \(p\), and Theorem 10.1
leaves the number of Thue solutions modulo \(p^s\) for \(s>1\) in the form
\(p^s d\) with an unspecified positive integer \(d\). Searches for the exact
congruence conclusion, prime-square formulation, and equivalent Thue-equation
formulations did not locate prior coverage. Because the relevant paper was revised
recently, residual bibliographic risk remains.

## Reproducibility

Run

```text
python3 artifacts/verify.py
```

using Python 3. The program uses only the Python standard library and exact integer
arithmetic. Its deterministic expected output is recorded in
`artifacts/verification.txt`.

## References

1. M. Le and G. Soydan, *A brief survey on the generalized
   Lebesgue-Ramanujan-Nagell equation*, Surveys in Mathematics and its
   Applications 15 (2020), 473–523. https://arxiv.org/abs/2001.09617
2. I. Chen, *On the equations \(a^2-2b^6=c^p\) and \(a^2-2=c^p\)*,
   LMS Journal of Computation and Mathematics 15 (2012), 158–171.
   https://doi.org/10.1112/S146115701200006X
3. E. Katz and K. Pratt, *On the Lebesgue–Nagell equation
   \(x^2-2=y^p\)*, The Ramanujan Journal 69 (2026), no. 3, Paper 75.
   https://doi.org/10.1007/s11139-026-01334-4
   Current arXiv version: https://arxiv.org/abs/2507.12397
4. E. Katz and K. Pratt, accompanying computation repository.
   https://github.com/ethanhkatz/Lebesgue-Nagell-code
