# Exact three-element square-sum distribution over odd prime-power rings

## Finding

For an odd prime \(p\), an integer \(a\ge1\), and \(q=p^a\), let
\[
N_{p,a}(b)=\#\bigl\{S\subseteq\mathbb Z/q\mathbb Z:\ |S|=3,\ \sum_{x\in S}x^2=b\bmod q\bigr\}.
\]
Let \(\chi_p(u)\) be the Legendre symbol, with \(\chi_p(0)=0\). The following finite, depth-decreasing recursion gives **every** integer \(N_{p,a}(b)\).

Put \(A_0(0)=B_0(0)=1\). For \(a\ge1\), write \(A_a(b)\) for the number of ordered triples \((x,y,z)\) solving \(x^2+y^2+z^2=b\pmod{p^a}\), and \(B_a(b)\) for the number of ordered pairs \((x,z)\) solving \(2x^2+z^2=b\pmod{p^a}\). Their complete initial cases are
\[
A_1(b)=p^2+p\chi_p(-b),\qquad
B_1(b)=\begin{cases}
p+(p-1)\chi_p(-2),&p\mid b,\\
p-\chi_p(-2),&p\nmid b.
\end{cases}
\]
For \(a\ge2\), with \(b\) represented by its integer residue between \(0\) and \(p^a-1\),
\[
A_a(b)=\begin{cases}
p^{2a-2}\bigl(p^2+p\chi_p(-b)\bigr),&p\nmid b,\\
p^{2a-2}(p^2-1)+\mathbf1_{p^2\mid b}\,p^3A_{a-2}(b/p^2),&p\mid b,
\end{cases}
\]
\[
B_a(b)=\begin{cases}
p^{a-1}\bigl(p-\chi_p(-2)\bigr),&p\nmid b,\\
p^{a-1}(p-1)\bigl(1+\chi_p(-2)\bigr)+\mathbf1_{p^2\mid b}\,p^2B_{a-2}(b/p^2),&p\mid b.
\end{cases}
\]
The diagonal count \(C_a(b)=\#\{x\pmod{p^a}:3x^2=b\pmod{p^a}\}\) is explicit. If \(p\ge5\), then
\[
C_a(b)=\begin{cases}
p^{\lfloor a/2\rfloor},&b\equiv0\pmod{p^a},\\
0,&\nu_p(b)<a\text{ is odd},\\
p^t\bigl(1+\chi_p(3u)\bigr),&b=p^{2t}u,\quad p\nmid u,\quad 2t<a.
\end{cases}
\]
For the exceptional prime \(p=3\), the equally explicit form is
\[
C_a(b)=\begin{cases}
0,&3\nmid b,\\
3\,R_{a-1}(b/3),&3\mid b,
\end{cases}
\]
where \(R_0(0)=1\) and the ordinary square-root count modulo \(3^e\) for \(e\ge1\) is
\[
R_e(c)=\begin{cases}
3^{\lfloor e/2\rfloor},&c\equiv0\pmod{3^e},\\
0,&\nu_3(c)<e\text{ is odd},\\
3^t\bigl(1+\chi_3(v)\bigr),&c=3^{2t}v,\ 3\nmid v,\ 2t<e.
\end{cases}
\]
Then the exact answer is
\[
\boxed{N_{p,a}(b)=\frac{A_a(b)-3B_a(b)+2C_a(b)}6.}
\]
All evaluations terminate at depth \(0\) or \(1\).

For \(p\ge5\) and \(p\nmid b\), the answer simplifies to the explicit squareclass-biased formula
\[
\boxed{6N_{p,a}(b)=p^{2a}-3p^a+2+3p^{a-1}\chi_p(-2)
+p^{2a-1}\chi_p(-b)+2\chi_p(3b).}
\]
In particular, switching between unit squareclasses changes the count by
\[
\frac{p^{2a-1}\chi_p(-1)+2\chi_p(3)}3,
\]
which is nonzero for every \(p\ge5\), and the squareclass bias is therefore exact at all powers.

The square-sum support is completely classified:
\[
\{\textstyle\sum_{x\in S}x^2:|S|=3\}
=\begin{cases}
\{2\}\subseteq\mathbb Z/3\mathbb Z,&p^a=3,\\
\mathbb Z/p^a\mathbb Z,&p^a\ge5\text{ odd prime power}.
\end{cases}
\]

## Assumptions and scope

Subsets consist of three distinct **residue classes**; distinctness is not imposed on their squares. A target \(b\) is represented as a residue in the specified quotient ring. Every assertion is valid for every odd prime, all positive powers, and every target, including singular targets divisible by the prime. No statement concerns powers of \(2\) or a general composite modulus with several prime factors.

## Proof

**(1) Finite-field base counts.** For a nondegenerate ternary diagonal quadratic form over \(\mathbb F_p\), direct evaluation of the quadratic-character sum gives \(p^2+p\chi_p(-b)\) solutions. For completeness, fixing \(x,y\) and summing the number \(1+\chi_p(b-x^2-y^2)\) of possible \(z\) produces this standard count: additive-character orthogonality and \(G_p(t)^2=\chi_p(-1)p\) reduce the nontrivial Fourier modes to \(p\chi_p(-b)\). For \(2x^2+z^2=b\), the same character-sum identity gives \(p-\chi_p(-2)\) at nonzero \(b\), and \(p+(p-1)\chi_p(-2)\) at zero. These are the asserted base formulas.

**(2) Nonsingular lifting and singular branches.** At any solution of the ternary equation modulo \(p\) with some nonzero coordinate, one partial derivative \(2x_i\) is a unit. At every increase in exponent, that coordinate has a unique lift for each choice of the other two digits, giving exactly \(p^2\) lifts per existing solution. Thus a nonsingular class contributes \(p^{2(a-1)}\) solutions modulo \(p^a\). For the binary equation the corresponding factor is \(p^{a-1}\), since its coefficients \(2,1\) are units for odd \(p\). When \(p\nmid b\), all classes are nonsingular. When \(p\mid b\), exactly one residue-class tuple is singular, namely the all-zero tuple. Its complement has respectively \(p^2-1\) or \((p-1)(1+\chi_p(-2))\) residue-class solutions. The zero tuples admit no lift unless \(p^2\mid b\). In that case writing every coordinate as \(p\) times a new variable shows that the number of singular solutions is exactly \(p^3 A_{a-2}(b/p^2)\) or \(p^2 B_{a-2}(b/p^2)\), because the new variables each have one unused base-\(p\) digit. This proves every recurrence including its \(a=2\) boundary.

**(3) The repeated-coordinate correction.** Among ordered solutions \((x,y,z)\) of the ternary equation, each of the three coincidence events \(x=y\), \(x=z\), \(y=z\) has exactly \(B_a(b)\) solutions. Their pairwise intersections and the triple intersection all coincide with the single set \(x=y=z\), of size \(C_a(b)\). Inclusion–exclusion therefore leaves \(A_a(b)-3B_a(b)+2C_a(b)\) ordered solutions with pairwise distinct entries. The permutation action on these ordered triples is free and has orbits of size six. This establishes the division-by-six formula.

**(4) Explicit square roots, including \(p=3\).** For an odd prime \(p\), the number of roots of \(x^2=c\pmod{p^e}\) is \(p^{\lfloor e/2\rfloor}\) for \(c=0\), zero if \(\nu_p(c)\) is odd, and \(p^t(1+\chi_p(u))\) if \(c=p^{2t}u\) with \(u\) a unit. Indeed, the valuation of a root must be \(t\); dividing by \(p^{2t}\) leaves a unit square equation whose two roots Hensel-lift uniquely, and there are \(p^t\) redundant digits. When \(p\ne3\), multiply \(3x^2=b\) by the inverse of three; \(\chi_p(b/3)=\chi_p(3b)\). When \(p=3\), the congruence has no solutions unless \(3\mid b\), in which case it reduces to \(x^2=b/3\pmod{3^{a-1}}\) with three choices of the final digit. This proves the expressions for \(C_a\) and the unit-target closed form.

**(5) All targets are attained, apart from the minimal modulus.** For \(p\ge7\) and nonzero \(b\pmod p\), the base formulas give
\[
6N_{p,1}(b)=p^2-3p+3\chi_p(-2)+p\chi_p(-b)+2\chi_p(3b)
\ge p^2-4p-5>0.
\]
For \(b=0\), the count is \((p^2-1)/6\) if \(\chi_p(-2)=-1\), and \((p-1)(p-5)/6\) if \(\chi_p(-2)=1\), both positive when \(p\ge7\). For \(p=5\), direct substitution into the proved formula gives the five counts \(4,1,3,3,1\), all positive. Every distinct three-element solution modulo \(p\ge5\) has at least one nonzero coordinate; lifting that coordinate one digit at a time while fixing lifts of the other two gives a solution of every prescribed target modulo each higher power, with distinctness preserved modulo \(p\). For \(p=3\), the sole three-element subset modulo \(3\) is \(\{0,1,2\}\), whose squares sum to \(2\). Modulo \(9\), explicit distinct witnesses for target residues \(0,1,\dots,8\), respectively, are
\[
\{1,2,7\},\ \{0,1,3\},\ \{0,1,8\},\ \{1,2,4\},\ \{0,2,3\},\
\{0,1,2\},\ \{1,2,8\},\ \{0,3,4\},\ \{0,1,4\}.
\]
Each witness contains a coordinate not divisible by three; the derivative with respect to that coordinate is a unit, so it lifts to any prescribed target modulo every higher power while remaining distinct modulo \(9\). This proves the exact support classification. \(\square\)

## Verification

The accompanying `verify_counts.py` uses only the Python standard library. It executes the recursive formulas and exhaustively enumerates all distinct three-element subsets for \((p,a)=(3,1),(3,2),(3,3),(3,4),(5,1),(5,2),(7,1),(7,2),(11,1),(11,2),(13,1),(13,2)\). It checks every target in those rings, total count \(\binom{p^a}{3}\), support, and the unit-target simplification. Running this exact script on the delivered bytes printed `VERIFY_OK`. These finite checks are supplementary; the preceding proof covers all odd prime powers.

## Relationship to prior work

Li and Wan introduced the polynomial subset-sum count \(N_f(D,k,b)\) for finite commutative rings and obtained asymptotic bounds, explicitly including prime-power modulus [1]. Here \(D\) is the entire residue ring, \(k=3\), and \(f(x)=x^2\), yielding an exact formula for **all** target residues, including singular prime-power branches, and a complete image classification. The available abstract of [1] gives bounds rather than this formula, but its complete preprint could not be examined; this is a stated originality risk, not asserted noncoverage of unread pages. Lai, Marino, Robinson and Wan treat first and second moment constraints over **finite fields**, discussing earlier exact finite-field results [2]; those results may contain the \(a=1\) case, so no claim of novelty is made for the prime-field base distribution in isolation. Ding and Zhou analyze distinct power-value subset sums over Galois rings of characteristic \(p^2\) [3], which is not the same as distinct arguments mapped through \(x^2\), and their abstract offers asymptotic estimates rather than the displayed all-exponent counting law.

## Limitations

The result concerns three-element subsets only, odd prime-power moduli only, and the specific polynomial \(x^2\). The formulas for unrestricted quadratic representations and the distinct-coordinate inclusion–exclusion step are classical tools. The original full text of [1] and full text of [3] were unavailable in this review, so an equivalent or dominating formula in those or other sources remains a literature risk. All claims are independent of the numerical enumeration, and independent audit is not claimed here.

## References

[1] J. Li and D. Wan, “Counting polynomial subset sums,” arXiv:1507.06329v1 (first posted 2015-07-22); subsequently *Ramanujan Journal* 47 (2018), 67–84. DOI 10.1007/s11139-018-0020-0.

[2] T. Lai, A. Marino, A. Robinson, and D. Wan, “Moment subset sums over finite fields,” *Finite Fields and Their Applications* 59 (2019), article 101607. DOI 10.1016/j.ffa.2019.101607.

[3] Y. Ding and H. Zhou, “Subset sums over Galois rings,” *Journal of Number Theory* 205 (2019), 148–169. DOI 10.1016/j.jnt.2019.05.004.
