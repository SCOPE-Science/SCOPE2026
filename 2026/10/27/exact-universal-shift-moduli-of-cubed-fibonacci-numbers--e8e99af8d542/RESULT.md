# Exact universal shift moduli of cubed Fibonacci numbers

## Finding

Let \(F_0=0\), \(F_1=1\), and \(F_{n+2}=F_{n+1}+F_n\). Write \(L_m=F_{m-1}+F_{m+1}\) for the Lucas numbers, with \(L_0=2\). For every integer \(k\ge1\), define the positive integer
\[
D(k)=\gcd_{n\ge0}\lvert F_{n+k}^{3}-F_n^{3}\rvert.
\]
Then, for odd \(k\), \(D(k)=2\) when \(k\equiv3\pmod6\), and \(D(k)=1\) otherwise. For \(k=2m\),
\[
D(2m)=\begin{cases}
L_m,&m\text{ odd},\\
F_m,&m\equiv2\pmod4,\\
3F_m,&m\equiv0\pmod4.
\end{cases}
\]
Equivalently, \(D(k)\) is the greatest positive modulus for which \(F_{n+k}^3\equiv F_n^3\pmod{D(k)}\) for all nonnegative \(n\). For instance, \(D(8)=9\): cubing introduces a shift period of \(8\) modulo \(9\), whereas the unpowered Fibonacci sequence has period \(24\) modulo \(9\).

## Assumptions and scope

All variables \(k,m,n\) are integers in the ranges stated above. Congruences and divisibility are over the ordinary integers; no primitivity assumption is made about the shift \(k\). The greatest common divisor is positive and is taken over every \(n\ge0\). This is a statement about congruence moduli for shifted *cubes* of Fibonacci numbers, not about sums of consecutive cubes.

## Proof

Fix \(k\ge1\). Let \(a=F_{k-1}\), \(b=F_k\), so \(\gcd(a,b)=1\), and use the Fibonacci addition formula
\[
F_{n+k}=aF_n+bF_{n+1}.
\]
The shift difference is the evaluation at \((F_n,F_{n+1})\) of the integral binary cubic
\[
P(X,Y)=(aX+bY)^3-X^3.
\]
Its four coefficients are \(a^3-1\), \(3a^2b\), \(3ab^2\), and \(b^3\). Denote their positive gcd by \(c\). Clearly \(c\mid D(k)\).

The sequence \(u_n=F_n^3\) satisfies the monic fourth-order recurrence whose characteristic polynomial is
\[
(t^2-4t-1)(t^2+t-1)=t^4-3t^3-6t^2+3t+1.
\]
This follows directly by cubing the Binet expression: the four characteristic roots are \(\alpha^3,-\alpha,-\beta,\beta^3\) for \(\alpha\beta=-1\) and \(\alpha+\beta=1\). Differences of translates satisfy the same recurrence. Consequently \(D(k)\) equals the gcd of its values at \(n=0,1,2,3\).

The four evaluation points \((F_n,F_{n+1})\) are \((0,1),(1,1),(1,2),(2,3)\). The coefficient-to-value matrix for the monomials \(X^3,X^2Y,XY^2,Y^3\) is
\[
\begin{pmatrix}0&0&0&1\\1&1&1&1\\1&2&4&8\\8&12&18&27\end{pmatrix},
\]
whose determinant has absolute value \(2\). Integer adjugate inversion therefore shows \(c\mid D(k)\mid2c\). In particular, the odd-prime valuations of \(c\) and \(D(k)\) agree; only an extra factor of \(2\) must be excluded.

Cassini's identity gives \(a^2\equiv(-1)^k\pmod b\). If \(k\) is odd, a prime dividing \(b\) and \(a^3-1\) must divide \(2\): from \(a^2=-1\), the identity \(a^3=1\) forces \(a=-1\) and then \(2=0\). Since \(F_k\) is even exactly when \(3\mid k\), the coefficient gcd is \(c=1\) unless \(k\equiv3\pmod6\), in which case \(c=2\). In the former case \(F_k^3\) is odd, so \(D(k)=1\). In the latter, the Fibonacci recurrence modulo \(4\) (period \(6\)) yields \(F_{k+1}\equiv3\pmod4\), so \(F_{k+1}^3-1\) has exactly one factor \(2\); hence \(D(k)=2\).

For even \(k=2m\), Cassini gives \(a^2\equiv1\pmod b\), and therefore \(a^3\equiv a\pmod b\). Let \(h=\gcd(a-1,b)=\gcd(a^3-1,b)\). The standard doubling and addition identities give
\[
F_{2m}=F_mL_m,\qquad
F_{2m-1}-1=\begin{cases}
L_mF_{m-1},&m\text{ odd},\\
F_mL_{m-1},&m\text{ even}.
\end{cases}
\]
Because consecutive Fibonacci terms and consecutive Lucas terms are each coprime, these identities show \(h=L_m\) for odd \(m\), and \(h=F_m\) for even \(m\).

For every prime \(p\ne3\) dividing \(b\), the coefficients imply \(v_p(c)=v_p(h)\): multiplication by \(3\) does not change this valuation, and coprimality of \(a,b\) ensures that the middle coefficients cannot reduce the minimum below \(\min(v_p(a^3-1),v_p(b))\). A prime not dividing \(b\) cannot divide \(c\). For \(p=3\), the extra factor in the middle coefficients can matter only if \(3\mid b\), or equivalently \(4\mid k\). When \(k\equiv4\pmod8\), one has \(a\equiv-1\pmod3\), and the coefficient \(a^3-1\) is not divisible by \(3\); there is no correction. When \(8\mid k\), we have \(a\equiv1\pmod3\), \(m\equiv0\pmod4\), and \(3\mid F_m\) while \(3\nmid L_{m-1}L_m\). Thus
\[
v_3(a-1)=v_3(b)=v_3(F_m),\qquad
v_3(a^3-1)=v_3(a-1)+1.
\]
The last identity follows from \(a^2+a+1\equiv3\pmod9\) for \(a\equiv1\pmod3\), including the case \(a=1\) by direct valuation interpretation; for \(k\ge8\) here \(a>1\). The coefficients then give \(v_3(c)=v_3(h)+1\). Therefore \(c=h\) unless \(8\mid k\), in which case \(c=3h\). Substituting \(h\) gives the three displayed even-shift cases.

It remains to exclude the possible extra factor of \(2\) in \(D(k)\). If \(3\nmid k\) then \(F_k\) is odd and the value at \(n=0\) is odd, so \(D(k)=c\). For even \(k\) with \(3\mid k\), write \(k=2m\). In both parity cases of \(m\), the identities above and Fibonacci/Lucas parity yield \(v_2(a-1)=v_2(c)\) and \(v_2(b)>v_2(c)\). Indeed, when \(m\) is odd and \(3\mid m\), \(F_{m-1}\) is odd, \(v_2(F_m)=1\), and \(L_m\) contains the full valuation of \(c\); when \(m\) is even and \(3\mid m\), \(L_{m-1}\) is odd and \(v_2(L_m)=1\), with \(F_m\) containing the full valuation of \(c\). Thus \(F_{k+1}=a+b\) satisfies \(v_2(F_{k+1}-1)=v_2(c)\); since \(F_{k+1}\) is odd, its cube differs from \(1\) by exactly the same power of \(2\). This value at \(n=1\) forces \(v_2(D(k))=v_2(c)\). We conclude \(D(k)=c\) for all \(k\), proving the formula. \(\square\)

## Verification

The standalone script `verify.py` checks the complete coefficient identity, the determinant-two evaluation matrix, the exact Fibonacci-cube recurrence on a wide finite interval, and the theorem for every shift \(1\le k\le500\) by two independent calculations: the coefficient-content gcd and the four-shift-value gcd. Run `python3 verify.py` with Python 3 and no third-party dependencies. It prints `VERIFY_OK k=1..500, four-shift gcd and coefficient content agree with formula`. The proof above, not this finite test, establishes all positive shifts.

## Relationship to prior work

Wall (1960) develops periods of the original Fibonacci sequence modulo integers. Čerin (2013) studies factors of sums of consecutive Fibonacci and Lucas terms, including related square identities; this is not a formula for universal shift moduli of Fibonacci cubes. Barbero–Cerruti–Murru (2011 open preprint) develop transformations of linear recurrence sequences. Mbirika–Spilker (2022) determine gcds of sums of consecutive squares of generalized Fibonacci numbers. Those results concern different invariants or powers; none of the inspected relevant portions supplies the displayed four-class exact cubic-shift modulus formula. No publication-priority conclusion follows solely from unsuccessful keyword searches.

## Limitations

The theorem does not characterize the least period for every prescribed modulus without additional inversion of its divisibility conditions. The supplied computation verifies only shifts at most \(500\). A logically equivalent result may appear in unindexed or previously unnoticed literature, so originality remains subject to further independent bibliographic review. No independent mathematical audit has been performed.

## References

1. D. D. Wall, “Fibonacci series modulo \(m\),” *American Mathematical Monthly* 67 (1960), 525–532.
2. S. Barbero, U. Cerruti, and N. Murru, “Transforming Recurrent Sequences by Using the Binomial and Invert Operators,” arXiv:1105.2143v1 (posted 2011-05-11), https://arxiv.org/pdf/1105.2143.
3. Z. Čerin, “On factors of sums of consecutive Fibonacci and Lucas numbers,” *Annales Mathematicae et Informaticae* 41 (2013), 19–25, https://real-j.mtak.hu/22311/1/AnnMathInf_41_2013.pdf.
4. A. Mbirika and J. Spilker, “GCD of sums of \(k\) consecutive squares of generalized Fibonacci numbers,” arXiv:2204.12626, https://arxiv.org/pdf/2204.12626.
