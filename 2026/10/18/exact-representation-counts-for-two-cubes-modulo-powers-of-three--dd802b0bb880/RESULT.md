# Exact representation counts for two cubes modulo powers of three

## Finding
For each integer \(n\ge 0\) and each residue \(r\in\mathbb Z/3^n\mathbb Z\), put
\[
N_n(r)=\#\{(x,y)\in(\mathbb Z/3^n\mathbb Z)^2:x^3+y^3\equiv r\pmod{3^n}\}.
\]
For the modulus \(1\), set \(N_0(0)=1\). The complete representation-count law is as follows. For \(n=1\), \(N_1(r)=3\) for each of the three residues. For every \(n\ge2\), with \(q=3^n\),
\[
N_n(r)=\begin{cases}
2q,&r\equiv1,-1\pmod9,\\
q,&r\equiv2,-2\pmod9,\\
0,&r\equiv3,4,5,6\pmod9,\\
27,&n=2\text{ and }r\equiv0\pmod9,\\
2q+81\,\mathbf1_{27\mid r}N_{n-3}(r/27),&n\ge3\text{ and }r\equiv0\pmod9.
\end{cases}
\]
In the last line, choose the representative \(0\le r<3^n\); if \(27\mid r\), the argument \(r/27\) is taken modulo \(3^{n-3}\). This is a finite, terminating recursion and hence an exact formula for **every** target residue.

In particular, for \(n\ge2\),
\[
N_n(1)=2\cdot3^n.
\]
This establishes the three-power formula proposed in a dated 2018 conjecture associated with OEIS A087412. A residue modulo \(3^n\), \(n\ge2\), is a sum of two cubes if and only if its reduction modulo \(9\) belongs to \(\{0,1,2,7,8\}\).

## Assumptions and scope
The variables \(x,y\) are **ordered** and range independently over all residues modulo \(3^n\), including zero and nonunits. Cubes are ordinary integer cubes reduced modulo the modulus. The theorem is for exactly the prime-power moduli \(3^n\), not for arbitrary moduli or integer (rather than congruence) solutions. The recurrence counts each ordered pair exactly once.

## Proof
**Unit cube lemma.** For \(n\ge2\), the cube map on \((\mathbb Z/3^n\mathbb Z)^\times\) has image exactly the classes congruent to \(1\) or \(-1\) modulo \(9\), and every element of its image has exactly three cube roots. Indeed, the unit group is cyclic of order \(2\cdot3^{n-1}\); its cube map has a kernel of size three. Every unit cube is \(\pm1\pmod9\), and the number of such unit residues is \(2\cdot3^{n-2}\), exactly the image size. There are \(3^{n-1}\) units of each sign class modulo \(9\). A nonunit has cube divisible by \(27\).

Consequently, if \(r\equiv\pm1\pmod9\), exactly one of \(x,y\) must be a unit and the other is divisible by \(3\). There are two orientations, \(3^{n-1}\) choices for the nonunit, and three choices for the unit cube root, giving \(2\cdot3^n\). If \(r\equiv\pm2\pmod9\), both cubes must have the same sign, giving \(3^{n-1}\cdot3=3^n\). The four residues \(3,4,5,6\pmod9\) cannot be sums of two classes from \(\{0,1,-1\}\), so their counts vanish.

For \(r\equiv0\pmod9\), the solutions split disjointly into pairs of units of opposite signs and pairs with both coordinates divisible by \(3\). In the unit-unit case fix a unit \(x\) and write \(y=-x+3t\), with \(t\) ranging modulo \(3^{n-1}\). Then
\[
x^3+y^3=9H_x(t),\qquad H_x(t)=t(x^2-3xt+3t^2).
\]
The derivative \(H'_x(t)=x^2-6xt+9t^2\equiv x^2\not\equiv0\pmod3\), while \(H_x(t)\equiv x^2t\pmod3\). Thus \(H_x\) induces a permutation modulo every power of \(3\): it is bijective modulo \(3\), and the nonzero derivative gives a unique Hensel lift of every preimage one power at a time. When \(n\ge2\), each congruence \(H_x(t)\equiv r/9\pmod{3^{n-2}}\) has exactly three solutions \(t\pmod{3^{n-1}}\). There are \(2\cdot3^{n-1}\) choices for the unit \(x\), hence exactly \(2\cdot3^n\) opposite-unit solutions.

For \(n=2\), there are three multiples of \(3\) modulo \(9\), giving nine additional nonunit-nonunit solutions. Thus \(N_2(0)=18+9=27\). If \(n\ge3\), write \(x=3u\), \(y=3v\) with \(u,v\) independently modulo \(3^{n-1}\). The congruence is impossible unless \(27\mid r\). In that event it becomes
\[
u^3+v^3\equiv r/27\pmod{3^{n-3}}.
\]
Each solution at modulus \(3^{n-3}\) has \(3^2\) lifts for \(u\) and independently \(3^2\) for \(v\), contributing \(3^4N_{n-3}(r/27)=81N_{n-3}(r/27)\). This proves the recursion. Finally, modulo \(3\) the identity \(z^3\equiv z\) implies exactly three ordered solutions for each target, proving the initial case.

## Verification
The accompanying `verify.py` calculates the cube-residue frequency table independently, forms its exact cyclic self-convolution using integer arithmetic, and compares **every** target with the formula at all moduli \(3^n\) for \(1\le n\le8\). It also verifies the total count \(\sum_rN_n(r)=3^{2n}\). Run it using `python3 verify.py`; a successful run prints `PASS total_target_checks=9840`. These finite checks are not used as proof of the universal claim.

## Relationship to prior work
The July 17, 2018 formula note for OEIS A087412 expressly labels \(a(3^e)=2\cdot3^e\) for \(e>1\) a **conjecture**, while defining \(a(m)\) to count solutions of \(x^3+y^3\equiv1\pmod m\). The present theorem proves that statement and treats every target residue, not only \(1\). Another sequence, OEIS A087786, already gives an explicit prime-power formula for the zero-target difference-of-cubes congruence; replacing one variable by its negative makes that exactly the zero-target **sum** branch here. That branch is included for completeness but is not claimed as separately novel.

Eckford Cohen's 1955 study of cubic congruence representation counts assumes the prime is \(1\pmod3\), so its principal formula does not treat the ramified prime \(3\). Finch and Sebah's study of squares and cubes modulo integers gives root-of-unity and cube-image counts, not the full two-cube convolution distribution. Monsky's 2023 treatment concerns rational solutions of fixed sum-of-two-cubes equations rather than counts of all pairs modulo \(3^n\).

## Limitations
The result is local and does not produce integer or rational representations of any prescribed positive integer. It does not determine representation numbers for other prime powers, or independently improve the already-known zero-target formula. The originality comparison cannot exclude uncatalogued local-density calculations that may imply the same rule. The proof uses the standard cyclicity of unit groups of odd prime-power moduli and elementary Hensel lifting.

## References
- OEIS A087412, "Number of solutions to \(x^3+y^3\equiv1\pmod n\)," formula comment dated 2018-07-17: https://oeis.org/A087412.
- OEIS A087786, "Number of solutions to \(x^3-y^3\equiv0\pmod n\)," prime-power formula comment dated 2018-07-17: https://oeis.org/A087786.
- Eckford Cohen, "The number of solutions of certain cubic congruences," *Pacific Journal of Mathematics* 5 (1955), 877–889: https://msp.org/pjm/1955/5-6/pjm-v5-n6-p05-p.pdf.
- Steven Finch and Pascal Sebah, "Squares and Cubes Modulo \(n\)," arXiv:math/0604465, first publicly posted 2006-04-21: https://arxiv.org/html/math/0604465v3.
- Paul Monsky, "The sum of two cubes problem—an approach that's classroom friendly," arXiv:2309.00162, first posted 2023-08-31: https://arxiv.org/html/2309.00162v1.
