# The maximal member and point-count spectrum of a bi-cubic genus-four Hurwitz family over \(\mathbb F_{25}\)

## Finding
Let \(k=\mathbb F_{25}\) and \(\lambda\in k\setminus\{0,1\}\). Define the smooth projective curve \(C_\lambda\) by normalizing the function field
\[
k(x,u,v),\qquad u^3=x(x-1),\qquad v^3=x-\lambda.
\]
All \(23\) members have genus \(4\), and their complete point-count spectrum \((N,\text{number of marked parameters with }N\text{ points})\) is
\[
(15,4),\ (33,4),\ (39,4),\ (42,6),\ (48,2),\ (60,2),\ (66,1).
\]
The sole marked parameter with \(66\) points is \(\lambda=3\). Thus \(C_3\) meets the Hasse–Weil upper bound \(25+1+2(4)(5)=66\), and it is the unique maximal member **within this marked family** over \(k\).

## Assumptions and scope
Work over \(k=\mathbb F_5[\alpha]/(\alpha^2-2)\). Parameters range through **all** \(23\) elements of \(k\setminus\{0,1\}\). Smoothness refers to the normalization of the indicated function field, not the naive affine complete intersection at branch points. Distinct marked parameters need not represent distinct geometric-isomorphism classes. No claim is made about uniqueness of genus-four maximal curves outside this family or maximality over a different finite field.

## Proof
The classes of \(x(x-1)\) and \(x-\lambda\) in \(\overline{k}(x)^*/\overline{k}(x)^{*3}\) are independent: their valuations at \(x=0\) and \(x=\lambda\), respectively, separate them. Hence the geometric function-field extension has degree \(9\) and Galois group \((\mathbb Z/3\mathbb Z)^2\). Its branch points are exactly \(0,1,\lambda,\infty\); at each branch point the inertia order is \(3\). Tame Riemann–Hurwitz therefore gives
\[
2g(C_\lambda)-2=9(-2)+4\cdot9(1-1/3)=6,
\qquad g(C_\lambda)=4.
\]
There are three geometric points over infinity, all \(k\)-rational. Indeed with \(t=1/x\), the local ratio satisfies
\[
(u/v^2)^3=\frac{1-t}{(1-\lambda t)^2},
\]
whose residue is \(1\). The three distinct cube roots of unity belong to \(k\), because \(3\) divides \(25-1\). Tameness ensures that these give the three reduced rational branches.

Define \(r(c)=\#\{w\in k:w^3=c\}\), taking values \(0,1,3\). For a finite \(x\), the independent equations admit precisely \(r(x(x-1))r(x-\lambda)\) solutions. Thus the **exact** formula is
\[
\#C_\lambda(k)=3+\sum_{x\in k}r(x(x-1))r(x-\lambda).
\]
Represent \(a+b\alpha\in k\) by the integer \(a+5b\) with \(0\le a,b\le4\). The eight nonzero cubes in this encoding are \(1,2,3,4,5,10,15,20\), and every nonzero cube has exactly three cube roots. Substituting all \(25\) field elements into the displayed identity gives the complete parameter-value table below; a standalone checker independently reconstructs the field, performs the cube-root summation, and directly enumerates all affine triples.

| Point count | Encoded parameters \(a+5b\) |
|---|---|
| \(15\) | \(5,6,20,21\) |
| \(33\) | \(10,11,15,16\) |
| \(39\) | \(7,9,22,24\) |
| \(42\) | \(8,12,14,17,19,23\) |
| \(48\) | \(2,4\) |
| \(60\) | \(13,18\) |
| \(66\) | \(3\) |

This exhaustive table covers all \(23\) admissible marked parameters. For \(\lambda=3\), it yields \(63\) affine rational points and three points over infinity, hence \(66\) total. Hasse–Weil bounds every smooth genus-four curve over \(k\) by \(25+1+2\cdot4\cdot5=66\), proving maximality and uniqueness **within the displayed family**.

As an independent check on the maximal case, the three positive-genus quotient curves
\[
u^3=x(x-1),\qquad w^3=x(x-1)(x-3),\qquad z^3=x(x-1)(x-3)^2
\]
have point counts \(36,36,46\) and genera \(1,1,2\), respectively. The usual character/idempotent decomposition gives the point-count relation \(\#C_3(k)=36+36+46-2(25+1)=66\). The main finite-field proof does not depend on this decomposition.

## Verification
Run `python3 verify_f25.py` with a standard Python 3 interpreter. The program proves its finite field arithmetic consistent by testing nonzero inverses, all distributive triples, and all associative triples. It evaluates the above formula and also independently enumerates ordered affine triples for every admissible parameter. Exact assertions verify the full spectrum, unique maximizer, and three quotient counts. This finite enumeration is exhaustive because the parameter set has exactly \(23\) elements and the field exactly \(25\); it is not used to infer claims over infinitely many parameters or extensions of the field.

## Relationship to prior work
The family lies in the classical theory of tame abelian covers of the projective line, investigated systematically by Bouw and Bouw–Wewers [1,2]. Hasegawa [3] studies superspeciality of the genus-two cyclic quotient \(z^3=x(x-1)(x-\lambda)^2\). That genus-two superspeciality criterion is **prior art**, not the claimed contribution here; it does not itself state the point-count spectrum for the distinct degree-nine, genus-four family. Howe [4] studies constructions of genus-four curves with many points, but its explicit cover construction uses double covers of genus-two curves rather than the two independent cubic equations above. The proposed contribution is the complete, model-specific \(\mathbb F_{25}\) marked-parameter spectrum and sharp arithmetic maximum, not the existence of maximal genus-four curves in general.

## Limitations
This is an exact finite-field classification for the given marked family, not a geometric-isomorphism census. Hasegawa's relevant full text was not available for a whole-document comparison; an unlocated earlier specialized computation or tabulation might cover these numbers. The numerical part is checked independently by two exhaustive finite methods, but no independent scientific audit or historical-priority adjudication has been performed. The quotient counts do not establish universal factorization formulas in other characteristics.

## References
[1] I. Bouw and S. Wewers, *Reduction of covers and Hurwitz spaces*, arXiv:math/0005120 (first posted 2000-05-11).
[2] I. Bouw, *The p-rank of ramified covers of curves*, Compositio Mathematica 126 (2001), 295–322.
[3] T. Hasegawa, *Some remarks on superspecial and ordinary curves of low genus*, Mathematische Nachrichten 286 (2013), 17–33, doi:10.1002/mana.201010024.
[4] E. Howe, *Quickly constructing curves of genus 4 with many points*, arXiv:1506.04478 (first posted 2015-06-15).
