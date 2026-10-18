# Exact unit-congruence fibers and sharp representation minima for a ternary quadratic form

## Finding
For \(n\ge2\), let \(U_n=(\mathbb Z/n\mathbb Z)^\times\) and define the ordered representation count
\[
R_n(d,m)=\#\{(a,b,c)\in U_n^3:a^2+b^2-dc^2\equiv m\pmod n\}.
\]
An explicit formula determines **every fiber** \(R_n(d,m)\), its exact minimum as \(m\) varies, and the distribution's behavior under prime-power lifting. This quantitative statement strengthens the previously published existence criterion for unit-special parameters, without claiming that criterion as new.

For odd primes \(p\), let \(\chi=\chi_p\) be the quadratic character extended by \(\chi(0)=0\); set \(\varepsilon=\chi(-1)\), \(\alpha=\chi(d)\), and \(z=\chi(m)\). Define
\[
F_p(d,m)=\begin{cases}
p^2-3p+3+\varepsilon+2\alpha+z\bigl(\alpha(p+\varepsilon)+2\bigr),&p\nmid d,\ p\nmid m,\\
(p-1)(p-2-2\alpha-\varepsilon),&p\nmid d,\ p\mid m,\\
(p-1)(p-2-\varepsilon-2z),&p\mid d,\ p\nmid m,\\
(p-1)^2(1+\varepsilon),&p\mid d,\ p\mid m.
\end{cases}
\]
For \(e\ge1\), put \(t=\min(e,3)\), and set
\[
F_{2^e}(d,m)=\begin{cases}
2^{3(e-1)-\max(e-3,0)},&m\equiv2-d\pmod{2^t},\\
0,&\text{otherwise}.
\end{cases}
\]
Then for any prime-power factorization \(n=2^{e_2}\prod_{p\ \mathrm{odd}}p^{e_p}\), omitting the factor for \(2\) when \(n\) is odd, the exact formula is
\[
\boxed{R_n(d,m)=F_{2^{e_2}}(d,m)\prod_{p\ \mathrm{odd},\ p\mid n}p^{2(e_p-1)}F_p(d,m).}
\]

The **sharp worst-target counts** are as follows. With \(M_p(d)=\min_{m\bmod p}F_p(d,m)\),
\[
\boxed{M_p(d)=\begin{cases}
0,&p=3,\\
8,&p=5,\ \chi_5(d)=-1,\\
0,&p=5,\ \chi_5(d)\ne-1,\\
(p-1)(p-3),&p\ge7,\ p\equiv3\pmod4,\ p\nmid d,\\
0,&p\ge7,\ p\equiv3\pmod4,\ p\mid d,\\
(p-1)(p-3),&p\ge13,\ p\equiv1\pmod4,\ \chi_p(d)=-1,\\
(p-1)(p-5),&p\ge13,\ p\equiv1\pmod4,\ \chi_p(d)\ne-1.
\end{cases}}
\]
For every \(e\ge1\), \(\min_m F_{2^e}(d,m)=0\), and for odd \(p\), \(\min_mR_{p^e}(d,m)=p^{2(e-1)}M_p(d)\). By CRT, for any \(n\) the global minimum is the product of these local minima.

## Assumptions and scope
All inputs \(n\ge2,d,m\) are integers, and all three variables must be units; triples are **ordered**. The character \(\chi_p\) is zero at zero. No hypothesis that \(d\) is a unit is made; this matters when primes divide \(d\). A factor with exponent zero is omitted, rather than using the dyadic formula at \(e=0\).

## Proof
**1. Two-squares count.** Fix an odd prime \(p\). For each \(t\in\mathbb F_p\), the number of unrestricted pairs solving \(x^2+y^2=t\) is
\[
B_p(t)=\begin{cases}p-\varepsilon,&t\ne0,\\p+(p-1)\varepsilon,&t=0.\end{cases}
\]
To prove it, use \(B_p(t)=\sum_x\bigl(1+\chi(t-x^2)\bigr)\). For \(t\ne0\), \(\sum_x\chi(x^2-t)=-1\); for \(t=0\), the corresponding sum is \((p-1)\). Multiplication by \(\chi(-1)=\varepsilon\) yields the displayed formula. More generally, when \(d\not\equiv0\), the number of unrestricted pairs solving \(x^2-dy^2=t\) is \(p-\chi(d)\) for \(t\ne0\) and \(p+(p-1)\chi(d)\) for \(t=0\). These statements also follow from the same quadratic-character sum and are proved by that substitution.

**2. Unrestricted ternary count.** If \(p\nmid d\), write \(T_p(m)=\#\{(a,b,c)\in\mathbb F_p^3:a^2+b^2-dc^2=m\}\). Since the binary count is \(p-\varepsilon+p\varepsilon\mathbf1_{t=0}\), summing over \(c\) counts the roots of \(m+dc^2=0\). Their number is \(1+\chi(-m/d)\), including the zero-target case by \(\chi(0)=0\). Thus
\[
T_p(m)=p^2+p\chi(d)\chi(m).
\]
At \(m=0\), this is \(p^2\), as expected for a nondegenerate ternary quadratic form in odd dimension.

**3. Exact exclusion of zero coordinates.** Apply inclusion-exclusion to the hyperplanes \(a=0\), \(b=0\), and \(c=0\). Each of the first two hyperplanes has the binary \(x^2-dy^2=m\) count, while the third has the binary \(x^2+y^2=m\) count. When \(p\nmid d\), the three pairwise intersections have respective counts \(1+\chi(-m/d)\), \(1+\chi(m)\), and \(1+\chi(m)\); the triple intersection contributes \(1\) only for \(m=0\). Explicit substitution yields exactly the first two lines of \(F_p(d,m)\). If \(p\mid d\), the variable \(c\) is free but must be nonzero, so
\[
F_p(d,m)=(p-1)\left[B_p(m)-2(1+\chi(m))+\mathbf1_{m=0}\right],
\]
which gives the final two lines. All cases, including zero parameters and targets, have therefore been counted.

**4. Odd prime-power lifting.** At every unit triple modulo an odd prime, the derivative with respect to \(b\) of \(a^2+b^2-dc^2\) is \(2b\), a unit. To lift a solution from modulus \(p^j\) to a specified target \(m\pmod{p^{j+1}}\), choose arbitrary lifts of \(a,c\) (\(p^2\) choices); the \(b\)-increment is uniquely determined modulo \(p\). Thus each solution has exactly \(p^2\) lifts, proving
\[
R_{p^e}(d,m)=p^{2(e-1)}F_p(d,m)
\]
for every \(e\ge1\), with \(m\) reduced modulo \(p\) in the right-hand character expressions.

**5. Dyadic fibers.** For \(e\ge1\), every odd square is congruent to \(1\pmod{2^{\min(e,3)}}\). Conversely the odd squares modulo \(2^e\) comprise the full congruence class of \(1\) modulo \(2^{\min(e,3)}\); the squaring map on units has constant fiber size, so its pushforward of uniform counting measure is uniform on that class. Sums and differences of three independent such square values therefore distribute uniformly over the additive coset \(2-d+2^{\min(e,3)}\mathbb Z/2^e\mathbb Z\). Of the \(2^{3(e-1)}\) ordered unit triples, exactly \(2^{e-\min(e,3)}\) target classes are attained, with equal multiplicity. This proves the stated dyadic formula, including \(e=1,2\).

**6. Sharp minima.** The odd-prime expression is constant on each of the two nonzero quadratic-character classes of \(m\), plus a third value for \(m=0\). These three classes are all nonempty for every odd prime. Comparing their three explicitly listed values proves the piecewise minimum formula: \(p=3,5\) give the exceptional rows; \(p\equiv3\pmod4\), \(p\ge7\), gives \((p-1)(p-3)\) for either nonzero character of \(d\), but zero at \(d=0\); and \(p\equiv1\pmod4\), \(p\ge13\), gives \((p-1)(p-3)\) for nonsquare \(d\), otherwise \((p-1)(p-5)\). The dyadic formula has unattained targets, so its minimum is zero. Finally the Chinese remainder theorem gives a bijection of the full solution fibers, and the independent choice of local target classes shows that the minimum of the product is the product of local minima. This completes the proof.

## Verification
The accompanying standalone `verify_counts.py` independently evaluates all claimed fiber formulas via (i) direct ordered triple enumeration and (ii) a separate convolution of the two-unit-square table with the third square. It checks 575 modulus/parameter profiles, the sum \(\sum_mR_n(d,m)=\varphi(n)^3\), and every local minimum for odd primes through \(47\). Running `python verify_counts.py` prints `VERIFY_OK`. These finite checks validate boundary examples and implementation; the preceding proof, not enumeration, establishes the theorem for infinitely many moduli.

## Relationship to prior work
Harrington and Gross (2015, Theorem 5) characterized precisely when \(R_n(d,m)>0\) for **every** target; their Theorem 7 characterizes existence of a sum of two unit squares. Their paper does not report complete target-wise representation multiplicities, minimum positive fiber sizes, the uniform lift factor \(p^{2(e-1)}\), or the dyadic fiber multiplicities stated here. The current formulas *recover* their known unit-special criterion as the statement that the computed minimum is positive: no factor \(2\) or \(3\); no prime divisor of \(d\) with residue \(3\pmod4\); and at prime \(5\), \(d\) must be a nonresidue. Harrington, Jones, and Lamarche (2014) examine two-square existence; Nowicki and Lam (2015) consider representations over integers, not this finite unit-triple distribution. The proof uses classical quadratic character sums and CRT, and does not claim these tools as new.

## Limitations
The result concerns ordered triples of **units**, rather than merely nonzero squares in \(\mathbb Z/n\mathbb Z\), and it does not count integer (rather than residue-class) solutions. An earlier exact character-sum calculation not found in the inspected literature may overlap this classification. The method is elementary; the novelty assessment concerns its complete fiber and worst-target statements in this previously studied constrained setting, not the classical character identities.

## References
1. J. Harrington and S. S. Gross, “Special Numbers in the Ring Zn,” *Journal of Integer Sequences* **18** (2015), Article 15.11.3, published November 25, 2015. https://www.maths.tcd.ie/EMIS/journals/JIS/VOL18/Harrington/harr5.pdf
2. J. Harrington, L. Jones, and A. Lamarche, “Representing Integers as the Sum of Two Squares in the Ring Zn,” *Journal of Integer Sequences* **17** (2014), Article 14.7.4; preprint arXiv:1404.0187. https://arxiv.org/abs/1404.0187
3. A. Nowicki, “The Numbers a²+b²−dc²,” *Journal of Integer Sequences* **18** (2015), Article 15.2.3. https://cs.uwaterloo.ca/journals/JIS/VOL18/Nowicki/nowicki3.pdf
4. P. C.-H. Lam, “Representation of Integers Using a²+b²−dc²,” *Journal of Integer Sequences* **18** (2015), Article 15.8.6. https://cs.uwaterloo.ca/journals/JIS/VOL18/Lam/lam2.pdf
