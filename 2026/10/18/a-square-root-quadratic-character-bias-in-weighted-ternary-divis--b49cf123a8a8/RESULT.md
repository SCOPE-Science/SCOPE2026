# A square-root quadratic-character bias in weighted ternary divisor means

## Finding
Let \(d_3(n)\) count ordered triples of positive integers whose product is \(n\), and set \(D_3(n)=d_3(n)/3^{\omega(n)}\), including \(D_3(1)=1\). For fixed \(q\ge1\) and \(a\) coprime to \(q\), put \(\theta_q=\varphi(q)/q\), and let \(\chi_0\) be the principal character modulo \(q\). A sum over \(\chi^2=\chi_0\) ranges over all quadratic and principal characters modulo \(q\).

Define the multiplicative function \(c\) by \(c(1)=1\) and, for every prime \(p\),
\[
c(p)=c(p^2)=0,\quad c(p^3)=\frac43,\quad c(p^j)=\frac23\quad(j\ge4).
\]
For a Dirichlet character \(\chi\) modulo \(q\), write
\[
G_\chi(s)=\sum_{m\ge1}\frac{c(m)\chi(m)}{m^s}
=\prod_p\left(1+\frac{4\chi(p)^3}{3p^{3s}}+\frac{2\chi(p)^4}{3p^{4s}(1-\chi(p)p^{-s})}\right).
\]
This product is absolutely convergent for \(\Re s>1/3\). Then, as \(x\to\infty\), for each fixed positive modulus \(q\), reduced residue \(a\), and \(\varepsilon>0\),
\[
\boxed{\begin{aligned}
\sum_{\substack{n\le x\\n\equiv a\pmod q}}D_3(n)
={}&\frac{\theta_q}{\varphi(q)}L(2,\chi_0)G_{\chi_0}(1)x\\
&+\frac{\theta_q}{\varphi(q)}\sqrt{x}
\sum_{\substack{\chi\bmod q\\\chi^2=\chi_0}}
\overline{\chi(a)}L(1/2,\chi)G_\chi(1/2)
+O_{q,\varepsilon}(x^{1/3+\varepsilon}).
\end{aligned}}
\]
Here \(L(s,\chi_0)\) is understood by meromorphic continuation at \(s=1/2\). When \(q=1\), the unique principal character is intended.

In particular, for the real character \(\chi_{-3}\) modulo \(3\),
\[
\boxed{\sum_{\substack{n\le x\\n\equiv1\pmod3}}D_3(n)
-\sum_{\substack{n\le x\\n\equiv2\pmod3}}D_3(n)
=\frac23L(1/2,\chi_{-3})G_{\chi_{-3}}(1/2)\sqrt{x}
+O_\varepsilon(x^{1/3+\varepsilon}),}
\]
and the displayed square-root coefficient is strictly positive. Thus the two reduced residue classes have a definite, eventually positive, square-root discrepancy even though their linear main terms agree.

## Assumptions and scope
The order of the divisor function is exactly three, \(q\) is fixed independently of \(x\), and only residues relatively prime to \(q\) are considered. The error constant may depend on \(q\) and \(\varepsilon\). The statement makes no assertion about a growing modulus, higher ordered divisor functions, or non-coprime residue classes.

## Proof
**1. Exact convolution.** For \(j\ge1\), the prime-power coefficient is \(D_3(p^j)=\binom{j+2}{2}/3\), with constant coefficient one. Its generating series satisfies
\[
\sum_{j\ge0}D_3(p^j)t^j
=\frac{1}{(1-t)(1-t^2)}\left(1+\frac43t^3+\frac{2t^4}{3(1-t)}\right).
\]
This follows by multiplication of rational functions; expanding verifies every coefficient, including the first two. Since \(c\) is multiplicative, coefficient comparison yields the exact Dirichlet convolution identity
\[
D_3=\mathbf1*\mathbf1_{\mathrm{square}}*c,
\]
where \(\mathbf1_{\mathrm{square}}(n)=1\) if \(n\) is a positive square and zero otherwise. On twisting by any character, its Dirichlet series becomes
\[
\sum_{n\ge1}\frac{D_3(n)\chi(n)}{n^s}
=L(s,\chi)L(2s,\chi^2)G_\chi(s)\quad(\Re s>1).
\]
All \(c(n)\) are nonnegative. Because its first nonzero local term has exponent three, the series \(G_\chi\) converges absolutely for every \(\Re s>1/3\).

**2. A twisted square-divisor hyperbola.** Define
\[
T_\chi(X)=\sum_{uv^2\le X}\chi(u)\chi(v)^2,
\quad A_\chi(y)=\sum_{u\le y}\chi(u),\quad B_{\chi^2}(y)=\sum_{v\le y}\chi(v)^2.
\]
Set \(y=z=X^{1/3}\). Partition the hyperbola into \(v\le y\), \(u\le z\), and their intersection, obtaining the exact identity
\[
T_\chi(X)=\sum_{v\le y}\chi(v)^2 A_\chi(X/v^2)
+\sum_{u\le z}\chi(u)B_{\chi^2}(\sqrt{X/u})
-A_\chi(z)B_{\chi^2}(y).
\]
For a nonprincipal character \(\psi\) modulo fixed \(q\), its partial sums are \(O_q(1)\), while \(A_{\chi_0}(Y)=\theta_qY+O_q(1)\). Elementary partial summation gives
\[
\sum_{u\le z}\frac{\psi(u)}{\sqrt u}
= L(1/2,\psi)+\mathbf1_{\psi=\chi_0}\,2\theta_q\sqrt z
+O_q(z^{-1/2}),
\]
and
\[
\sum_{v\le y}\frac{\chi_0(v)}{v^2}
=L(2,\chi_0)-\theta_q/y+O_q(y^{-2}).
\]
The value of \(L(1/2,\psi)\) in these identities is the analytic continuation of the Dirichlet series, equivalently the constant term in the partial-summation asymptotic. Inserting the estimates into the exact hyperbola identity yields
\[
T_\chi(X)=\mathbf1_{\chi=\chi_0}\theta_qL(2,\chi_0)X
+\mathbf1_{\chi^2=\chi_0}\theta_qL(1/2,\chi)\sqrt X
+O_q(X^{1/3}).
\]
For the principal character, the apparent \(X^{2/3}\) contributions cancel explicitly: the three regions contribute \(-\theta_q^2X^{2/3}\), \(+2\theta_q^2X^{2/3}\), and \(-\theta_q^2X^{2/3}\). When \(\chi\) is nonprincipal quadratic only the square-root contribution remains; when \(\chi^2\) is nonprincipal all three regions contribute \(O_q(X^{1/3})\). These cases exhaust all characters.

**3. Convolution and remainder.** The exact convolution from step 1 implies
\[
\sum_{n\le x}D_3(n)\chi(n)
=\sum_{m\le x}c(m)\chi(m)T_\chi(x/m).
\]
For each \(\varepsilon>0\), absolute convergence of \(G_\chi(1/3+\varepsilon)\) bounds the total remainder by
\[
x^{1/3+\varepsilon}\sum_{m\le x}\frac{c(m)}{m^{1/3+\varepsilon}}=O_{q,\varepsilon}(x^{1/3+\varepsilon}).
\]
Extending the two main-term sums over \(m\) to infinity incurs an error of the same size: the tails beyond \(x\) of \(\sum c(m)/m\) and \(\sum c(m)/\sqrt m\) are respectively \(O_\varepsilon(x^{-2/3+\varepsilon})\) and \(O_\varepsilon(x^{-1/6+\varepsilon})\), by the same convergent weighted sum (choose \(\varepsilon<1/6\), with larger values following from a smaller exponent). This proves the character-twisted two-term formula. Applying character orthogonality over the reduced residue classes gives the stated asymptotic.

**4. Strict sign of the modulus-three bias.** Subtract the \(a=2\) result from \(a=1\) for \(q=3\). The principal terms cancel, and the nonprincipal quadratic character contributes a factor two. The real value
\[
L(1/2,\chi_{-3})=\sum_{j\ge0}\left(\frac1{\sqrt{3j+1}}-\frac1{\sqrt{3j+2}}\right)>0
\]
is strictly positive by termwise pairing. For any real \(-1<t<1\), the local Euler factor admits the form
\[
1+\frac43t^3+\frac{2t^4}{3(1-t)}
=(1-t^2)\left(1+\frac{t^2(3-2t)}{3(1-t)^2}\right)>0.
\]
Set \(t=\chi_{-3}(p)/\sqrt p\), including \(t=0\) for primes dividing the modulus. The absolutely convergent Euler product is positive. Thus the square-root coefficient is strictly positive, completing the proof.

## Verification
The supplied standalone `verify.py` recomputes \(D_3(n)\) exactly by integer factorization and independently via the triple convolution, checks all values through \(20{,}000\), and evaluates a nontrivial modulus-three progression difference. Its output is a finite consistency check, not a proof of the asymptotic formula. The infinite argument is the four-step proof above.

## Relationship to prior work
M. Karras, *On the Mean Value of \(D_k(n)\) in Arithmetic Progressions*, arXiv:2602.12371, first public on 12 February 2026, studies the same normalized ordered-divisor functions and supplies leading-order asymptotics for reduced progressions. The relevant leading-term theorem has an error of order \(O_{k,q,\varepsilon}(x^{1/2+\varepsilon})\), which does not resolve an explicit nonzero secondary term of size \(\sqrt x\). Earlier work of Karras and Derbal and of Bouakkaz and Derbal addresses analogous leading means, with the latter focusing on the ordinary divisor function. The present finding isolates the ternary case where an exact square-divisor factorization permits a power-saving secondary asymptotic and identifies its quadratic-character origin.

## Limitations
This result is established only for \(D_3\) and fixed reduced progressions, not arbitrary \(D_k\) or growing \(q\). Earlier general convolution results may imply portions of the statement implicitly; no absolute novelty guarantee is claimed. A self-review has been performed, but independent mathematical validation has not been performed. The explicit bound \(O_{q,\varepsilon}(x^{1/3+\varepsilon})\) is not claimed to be optimal.

## References
1. Meselem Karras, *On the Mean Value of \(D_k(n)\) in Arithmetic Progressions*, arXiv:2602.12371 (2026), https://arxiv.org/abs/2602.12371 .
2. M. Karras and A. Derbal, *Mean value of an arithmetic function associated with the Piltz divisor function*, Asian-European Journal of Mathematics 13 (2020), article 2050062, DOI:10.1142/S179355712050062X.
3. Ouarda Bouakkaz and Abdallah Derbal, *The mean value of the function \(d(n)/d^*(n)\) in arithmetic progressions* (2023), cited in Karras (2026).
