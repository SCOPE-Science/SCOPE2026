# Exact finite-field idempotent law for two-dimensional perfect evolution algebras

## Finding
Fix a prime power \(q\), choose \(A\) uniformly from \(\operatorname{GL}_2(\mathbb F_q)\), and equip \(\mathbb F_q^2\) with the evolution-algebra product having distinct natural basis elements multiply to zero and coordinate-square map \(x\mapsto A x^{[2]}\). Let \(N(A)\) be the number of **nonzero** elements satisfying \(A x^{[2]}=x\).

**Theorem.** For every odd prime power \(q\), the complete probability law is

\[
\begin{array}{c|cccc}
 j&0&1&2&3\\\hline
 \Pr(N(A)=j)&\frac13&\frac{q^2+1}{2q(q+1)}&
 \frac{q-1}{q(q+1)}&\frac{q^2-2q+3}{6q(q+1)}.
\end{array}
\]

For every even prime power \(q\), the law is instead
\[
 (\Pr(N=0),\Pr(N=1),\Pr(N=2),\Pr(N=3))
 =\left(\frac13,\frac12,0,\frac16\right).
\]
The even-characteristic branch is compatible with previously known Frobenius-linear fixed-space methods; **the odd-characteristic finite-field law is the new result**. In particular, the probability that a uniformly sampled labeled perfect two-dimensional evolution algebra has no nonzero idempotent is **exactly** \(1/3\) over *every finite field*, not merely in a large-field limit.

## Assumptions and scope
The sample space is the set of invertible \(2\times2\) matrices with equal probability, relative to a fixed ordered natural basis. This is not a uniform distribution on algebra isomorphism classes. Here \(x^{[2]}=(x_1^2,x_2^2)^T\), and the given matrix convention is exactly the requirement \(Ax^{[2]}=x\). The field \(\mathbb F_q\) may have any prime-power cardinality. Zero is always an idempotent but is excluded from \(N\). All probabilities refer to rational idempotents defined over \(\mathbb F_q\), not geometric roots with multiplicities over an algebraic closure.

## Proof
**1. Projectivization without multiplicity loss.** Put \(B=A^{-1}\). A nonzero idempotent is a nonzero solution of \(x^{[2]}=Bx\). On \(\mathbb P^1(\mathbb F_q)\), define the coordinatewise squaring map
\[
 s([u:v])=[u^2:v^2].
\]
If a direction \(L=[u:v]\) satisfies \(s(L)=[B(u,v)^T]\), then for any representative \(z\ne0\) there is a unique \(\lambda\ne0\) with \(z^{[2]}=\lambda Bz\). The unique nonzero scalar multiple of \(z\) solving the actual idempotent equation is \(\lambda^{-1}z\), because
\[
 (\lambda^{-1}z)^{[2]}=\lambda^{-1}Bz=B(\lambda^{-1}z).
\]
Conversely any nonzero solution determines such a direction. Thus \(N(A)\) counts exactly the projective points \(L\) with \(s(L)=b(L)\), where \(b\) is the projective class of \(B\). Every \(b\in\operatorname{PGL}_2(\mathbb F_q)\) has exactly \(q-1\) invertible matrix representatives, so choosing \(A\) uniformly is equivalent, for this statistic, to choosing \(b\) uniformly.

**2. Universal upper bound.** Write \(B=\left(\begin{smallmatrix}a&b_0\\c&d\end{smallmatrix}\right)\). The projective equality is the homogeneous cubic equation
\[
 c u^3+d u^2v-a uv^2-b_0v^3=0.
\]
Because \(B\) is invertible, its four coefficients are not all zero, so this is a nonzero binary cubic and has at most three distinct roots in \(\mathbb P^1(\mathbb F_q)\). Therefore \(N(A)\in\{0,1,2,3\}\), even when the cubic has repeated geometric roots.

**3. Factorial moments from sharp projective transitivity.** Set \(G=\operatorname{PGL}_2(\mathbb F_q)\), of order \(|G|=q(q^2-1)\). The action is sharply transitive on ordered triples of distinct projective points. Given distinct domain points \(L_1,\ldots,L_k\) for \(k\le3\), a projectivity \(b\) with \(b(L_i)=s(L_i)\) exists if and only if the target points \(s(L_i)\) are pairwise distinct. In that case, the number of possible \(b\)'s is \(q(q-1)\), \(q-1\), or \(1\), according as \(k=1,2,3\).

For each \(Y\in\mathbb P^1(\mathbb F_q)\), let \(w_Y=|s^{-1}(Y)|\) and let \(S_j=\sum_Y w_Y^j\). Then \(S_1=q+1\), the number of ordered domain pairs with distinct square images is \(S_1^2-S_2\), and the number of ordered triples with all square images distinct is \(S_1^3-3S_1S_2+2S_3\). Double counting incidence between projectivities and their fixed directions gives the first three falling-factorial moments:
\[
\begin{aligned}
 F_1&=\mathbb E[N]=\frac{S_1q(q-1)}{q(q^2-1)}=1,\\
 F_2&=\mathbb E[N(N-1)]=\frac{(S_1^2-S_2)(q-1)}{q(q^2-1)},\\
 F_3&=\mathbb E[N(N-1)(N-2)]=\frac{S_1^3-3S_1S_2+2S_3}{q(q^2-1)}.
\end{aligned}
\]

**4. Odd characteristic.** When \(q\) is odd, the map \(s\) has two singleton fibers (over \(0\) and \(\infty\)), and \((q-1)/2\) nonempty two-point fibers over the nonzero squares. The remaining target fibers are empty. Hence \(S_2=2q\) and \(S_3=4q-2\). Substitution gives
\[
 F_2=\frac{q^2+1}{q(q+1)},\qquad
 F_3=\frac{q^2-2q+3}{q(q+1)}.
\]
Writing \(p_j=\Pr(N=j)\), and using \(N\le3\), the triangular relations \(F_3=6p_3\), \(F_2=2p_2+6p_3\), \(F_1=p_1+2p_2+3p_3\), and \(\sum p_j=1\) give
\[
 p_3=F_3/6,\quad p_2=(F_2-F_3)/2,\quad
 p_1=F_1-F_2+F_3/2,\quad p_0=1-p_1-p_2-p_3.
\]
These simplify to the four claimed fractions, including \(p_0=1/3\).

**5. Even characteristic.** Squaring on \(\mathbb F_q\) is a field automorphism, so \(s\) permutes all \(q+1\) projective points and all nonempty fibers have weight one. Thus \(S_2=S_3=q+1\), whence \(F_1=F_2=F_3=1\). The same triangular inversion yields \((p_0,p_1,p_2,p_3)=(1/3,1/2,0,1/6)\). This also proves the universal \(p_0=1/3\) assertion. \(\square\)

## Verification
The reproducible standalone program `verify.py` uses explicit polynomial-basis arithmetic for prime-power fields. It enumerates **every** invertible structure matrix and **every** nonzero vector for \(q=2,3,4,5,7,8,9,11,16\), directly tests \(Ax^{[2]}=x\), and compares the observed frequencies with the theorem. The same program also computes projective-square fiber weights and compares the resulting second and third factorial moments with those from direct enumeration. All nine cases returned `PASS`, followed by `VERIFY_OK`.

Illustrative actual matrix counts in the order \((N=0,N=1,N=2,N=3)\) are \((16,20,8,4)\) for \(q=3\), \((160,208,64,48)\) for \(q=5\), \((1920,2624,512,704)\) for \(q=9\), and \((20400,30600,0,10200)\) for \(q=16\). Finite enumeration is corroborative; the general proof is the incidence argument above.

## Relationship to prior work
The October 2026 survey of Kaygorodov, Martín González and Viruel establishes the exact mean of one nonzero idempotent (Remark 23) and cites an asymptotic symmetric-group heuristic for rational roots, with the generic Galois statement proved in dimension two (Conjecture 2, its discussion). It does **not** state this finite-field probability law in the relevant inspected sections. The finite-field correction terms and constant exactly-one-third absence probability strengthen the stated asymptotic picture in dimension two, without claiming anything in higher dimensions.

The generic polynomial-system and idempotent-existence results of García-Martínez and Pérez-Rodríguez concern complex fields and do not count rational fixed points over \(\mathbb F_q\). The orbit enumeration of Wei and Zou counts **isomorphism classes of perfect algebras**, a different statistic from the number of rational idempotents in a uniformly chosen labeled algebra. Prior exact second-moment calculations in the same problem family do not give the third factorial moment; known geometric root-multiplicity strata do not give rational splitting statistics. Earlier characteristic-two fixed-space results cover the even branch but not the odd branch.

## Limitations
No claim is made for singular structure matrices, equal-weight sampling of isomorphism classes, or the full idempotent-count law in dimension greater than two. The proof counts rational distinct idempotents, not multiplicities of the geometric idempotent scheme. The originality comparison is based on the specified accessible sources and focused searches; a wider result concerning projective fixed-point statistics or binary cubics could indirectly subsume this theorem, and a definitive historical-priority certification has not been performed.

## References
1. I. Kaygorodov, C. Martín González and A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248v1 (first posted 2026-10-15), especially Remark 23 and Conjecture 2. https://arxiv.org/html/2610.22248v1
2. X. García-Martínez and A. Pérez-Rodríguez, *A note on complete evolution algebras*, arXiv:2512.12418 (first posted 2025-12-13), published in Archiv der Mathematik 126 (2026), sections 2 and 3.3. https://link.springer.com/article/10.1007/s00013-026-02251-0
3. Y. Wei and Y. M. Zou, *Isomorphism Classes of Idempotent Evolution Algebras*, arXiv:2310.12368v1 (first posted 2023-10-18), especially sections 1, 2 and 4. https://arxiv.org/pdf/2310.12368
