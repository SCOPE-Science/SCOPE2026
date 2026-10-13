# An exact asymptotic for the 3-mod-8 reciprocal divisor-sum class
## Finding
Let
\[
A=\{0\}\cup\{n\ge1:\sigma(n)\text{ is odd}\},
\]
and let \(B\subseteq\mathbb N_0\) be the reciprocal set characterized by
\[
A(q)B(q)=1
\]
in \(\mathbb F_2[[q]]\). Define
\[
B_3(X)=\#\{n\le X:n\in B,\ n\equiv3\pmod 8\}.
\]
Then
\[
B_3(X)\sim \frac{\pi^2}{32}\frac{X}{\log X}.
\]
Equivalently, the counting function of OEIS A192717 has this asymptotic.

## Assumptions and scope
Here \(\sigma(n)\) is the sum-of-divisors function, and \(A(q)\) and \(B(q)\) are ordinary generating functions with coefficients reduced modulo \(2\).

Cooper and Riasanovsky identify the \(3\pmod 8\) part of \(B\) exactly as
\[
\{p^e k^2:
p\text{ prime},\ p\equiv3\pmod8,\ e\equiv1\pmod4,\ k\text{ odd},\ p\nmid k\}.
\]
The same set is OEIS A192717. That characterization is the starting point; the new statement is the first-order counting asymptotic with its explicit constant.

The analytic input is the prime number theorem in the fixed progression \(3\pmod8\),
\[
\pi(y;8,3)\sim \frac{y}{4\log y},
\]
together with the standard Chebyshev upper bound
\[
\pi(y)\ll \frac{y}{\log y}.
\]

## Proof
Every member of the displayed structural set has a unique representation
\[
n=p^{4j+1}k^2,
\qquad
j\ge0,
\]
with \(p\equiv3\pmod8\), \(k\) odd, and \(p\nmid k\). Indeed, \(p\) is the unique prime occurring to an odd exponent in \(n\).

First consider \(j\ge1\). Ignoring the parity and coprimality restrictions only enlarges the count, so the number of these terms up to \(X\) is at most
\[
\sum_{j\ge1}\sum_p
\left\lfloor\sqrt{\frac{X}{p^{4j+1}}}\right\rfloor
\le
\sqrt X
\sum_p\sum_{j\ge1}p^{-(4j+1)/2}.
\]
The double series converges, because
\[
\sum_p\sum_{j\ge1}p^{-(4j+1)/2}
=
\sum_p\frac{p^{-5/2}}{1-p^{-2}}
<\infty.
\]
Hence all exponents \(e\ge5\) contribute only
\[
O(\sqrt X).
\tag{1}
\]

It remains to count the dominant layer \(e=1\). If the condition \(p\nmid k\) is temporarily dropped, its counting function is
\[
M(X)
=
\sum_{\substack{k\le\sqrt{X/3}\\k\text{ odd}}}
\pi(X/k^2;8,3).
\tag{2}
\]
The dropped pairs satisfy \(p\mid k\), so writing \(k=p\ell\) bounds their number by
\[
\sum_p\sqrt{\frac{X}{p^3}}
=
O(\sqrt X).
\tag{3}
\]
Thus the true \(e=1\) count equals \(M(X)+O(\sqrt X)\).

We now evaluate \(M(X)\). For each fixed odd \(k\), the prime number theorem in arithmetic progressions gives
\[
\frac{\log X}{X}\,
\pi(X/k^2;8,3)
\longrightarrow
\frac{1}{4k^2}.
\tag{4}
\]
To justify summing these limits, split (2) at \(k=X^{1/4}\). For
\[
k\le X^{1/4},
\]
we have \(X/k^2\ge X^{1/2}\), and the Chebyshev bound gives a summable majorant
\[
\frac{\log X}{X}\pi(X/k^2;8,3)
\ll \frac1{k^2}.
\]
For
\[
k>X^{1/4},
\]
the trivial estimate \(\pi(y)\le y\) yields
\[
\frac{\log X}{X}
\sum_{k>X^{1/4}}\pi(X/k^2;8,3)
\le
\log X\sum_{k>X^{1/4}}\frac1{k^2}
=
o(1).
\]
Dominated convergence in the first range, followed by the vanishing tail, therefore gives
\[
\frac{\log X}{X}M(X)
\longrightarrow
\frac14
\sum_{\substack{k\ge1\\k\text{ odd}}}\frac1{k^2}.
\]
Finally,
\[
\sum_{\substack{k\ge1\\k\text{ odd}}}\frac1{k^2}
=
\left(1-\frac14\right)\zeta(2)
=
\frac{\pi^2}{8},
\]
so
\[
M(X)\sim\frac{\pi^2}{32}\frac{X}{\log X}.
\tag{5}
\]
The error terms in (1) and (3) are \(O(\sqrt X)=o(X/\log X)\). Combining them with (5) proves the claim.

## Verification
The attached `verify.py` independently checks the finite combinatorial interface used by the proof.

It constructs the reciprocal power series directly over \(\mathbb F_2\) through \(30000\) from the fact that \(\sigma(n)\) is odd exactly for squares and twice squares. For every \(n\le30000\) with \(n\equiv3\pmod8\), it verifies exact agreement between the reciprocal coefficient and the structural criterion
\[
n=p^{4j+1}k^2,
\qquad
p\equiv3\pmod8,
\qquad
k\text{ odd},
\qquad
p\nmid k.
\]
It also counts the structural class through \(10^6\).

This finite replay checks the normalization and the use of the published characterization. It is not evidence for the infinite asymptotic, which follows from the proof above.

## Relationship to prior work
Cooper and Riasanovsky prove that the \(3\pmod8\) reciprocal class has natural density zero and give its exact prime-square structural description. They do not state a first-order counting asymptotic for that class. OEIS A192717 records the same structural set and its equivalent quadratic-form and reciprocal-set descriptions, but likewise gives no asymptotic counting formula.

The earlier Cooper--Eichhorn--O'Bryant paper develops the general theory of reciprocal binary power series and densities for several other sets. Its stated results do not provide the present progression-specific asymptotic.

Targeted searches for A192717 together with “asymptotic,” for the equivalent odd-representation formulation using \(x^2+2y^2\), for the squarefree-kernel formulation, and for the explicit constant \(\pi^2/32\) found the structural sources but no theorem implying this count.

## Limitations
This theorem quantifies only the vanishing \(3\pmod8\) component of the reciprocal set. It does not resolve the paper's conjecture that the full reciprocal set has density \(1/32\); that conjecture is controlled by the distinct \(7\pmod{16}\) component.

The proof depends on the published exact characterization of the \(3\pmod8\) class and on standard prime-distribution results for the fixed progression \(3\pmod8\). It gives a first-order asymptotic but no explicit error term.

An equivalent asymptotic could exist in unindexed notes or literature under the quadratic-form formulation; targeted searches did not locate one.

## References
1. J. N. Cooper and A. W. N. Riasanovsky, “On the Reciprocal of the Binary Generating Function for the Sum of Divisors,” *Journal of Integer Sequences* 16 (2013), Article 13.1.8.
2. OEIS Foundation, A192717, “Positive integers of the form \((p^e)(k^2)\) for \(p\) prime congruent to \(3\pmod8\), \(e\equiv1\pmod4\), and \(k\) odd and coprime to \(p\).”
3. J. N. Cooper, D. Eichhorn, and K. O'Bryant, “Reciprocals of Binary Power Series,” *International Journal of Number Theory* 2 (2006), 499–522; arXiv:math/0506496.
