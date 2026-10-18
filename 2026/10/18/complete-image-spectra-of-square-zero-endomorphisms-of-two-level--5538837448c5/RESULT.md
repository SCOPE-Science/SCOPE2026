# Complete image spectra of square-zero endomorphisms of two-level finite abelian groups

## Finding
Let \(p\) be any prime, \(b\geq2\) an integer, and \(G=C_{p^2}\oplus C_{p^b}\). For each finite abelian \(p\)-group \(H\), let \(N_{p,b}(H)\) be the number of endomorphisms \(T:G\to G\) with \(T^2=0\) and \(\operatorname{im}T\cong H\). The complete spectrum is as follows; every unlisted image type has count zero.

The zero image has count \(N_{p,b}(0)=1\). For cyclic images,
\[
N_{p,b}(C_p)=(p+1)(p^2-1),\qquad
N_{p,b}(C_{p^2})=\begin{cases}
p^2(p^2-1),&b=2,\\
2p^3(p-1),&b=3,\\
3p^3(p-1),&b\ge4.
\end{cases}
\]
For every \(j\ge3\),
\[
N_{p,b}(C_{p^j})=p^j\begin{cases}
(p-1)(3p-2),&2j\le b,\\
2(p-1)^2,&2j=b+1,\\
(p-1)^2,&2j=b+2,\\
0,&2j>b+2.
\end{cases}
\]
The noncyclic images are exactly of type \(C_p\oplus C_{p^j}\), with
\[
N_{p,b}(C_p\oplus C_{p^j})=\begin{cases}
p(p-1)(p^2-1),&j=1,\\
(p-1)^2p^{j+1},&2\le j\le\lfloor b/2\rfloor,\\
0,&j>\lfloor b/2\rfloor.
\end{cases}
\]
In particular, if \(s=\lfloor b/2\rfloor\), the number having **noncyclic image** is \(p(p-1)(p^{s+1}-1)\), and the total number is
\[
\boxed{\#\{T\in\operatorname{End}(G):T^2=0\}=\begin{cases}
(2p^2-1)p^{b/2+1},&b\text{ even},\\
(3p-2)p^{(b+3)/2},&b\text{ odd}.
\end{cases}}
\]

## Assumptions and scope
The direct-sum notation \(C_{p^a}=\mathbb Z/p^a\mathbb Z\) specifies the additive groups; no base field or characteristic restriction beyond \(p\) being prime is needed. Images are classified **as abstract abelian groups**, not as subgroups with labeled generators. All counts refer to individual labeled group endomorphisms and include the zero map. The results are valid for every \(p\) and \(b\ge2\). The case \(b=1\) is not part of the statement.

## Proof
**1. Image factorization principle.** For any finite abelian group \(G\) and subgroup \(H\le G\), the endomorphisms \(T\) with \(T^2=0\) and exact image \(H\) correspond bijectively to surjective homomorphisms \(\overline T:G/H\twoheadrightarrow H\), via \(T=\iota_H\overline T\pi_H\). This is because \(\operatorname{im}T\subseteq\ker T\) exactly when \(T^2=0\). Thus
\[
N_{p,b}(K)=\sum_{\substack{H\le G\\H\cong K}}\#\operatorname{Sur}(G/H,H).
\tag{1}
\]

**2. Noncyclic images.** A rank-two target \(H\) requires \(G/H\) to have two generators, hence \(H\subseteq pG\). Since \(pG\cong C_p\oplus C_{p^{b-1}}\) and \(H\) has rank two, \(H[p]=G[p]\), so the full first summand \(pC_{p^2}\) lies in \(H\). Therefore for some \(1\le j\le b-1\) the subgroup is uniquely
\[
H_j=pC_{p^2}\oplus p^{b-j}C_{p^b}\cong C_p\oplus C_{p^j},\quad G/H_j\cong C_p\oplus C_{p^{b-j}}.
\]
A surjection onto \(H_j\) exists exactly when \(j\le b-j\). For \(j=1\), the reduction modulo \(p\) is an invertible two-by-two matrix, giving \(\#\operatorname{GL}_2(\mathbb F_p)=p(p-1)(p^2-1)\) maps. For \(j\ge2\), the reduction is triangular with nonzero diagonal, and the unrestricted higher digits give \((p-1)^2p^{j+1}\) maps. Summing over \(j\) yields
\[
p(p-1)(p^2-1)+(p-1)^2\sum_{j=2}^{\lfloor b/2\rfloor}p^{j+1}
=p(p-1)(p^{\lfloor b/2\rfloor+1}-1).
\]
In particular, no image with two cyclic summands each of exponent at least \(p^2\) is possible.

**3. Cyclic order \(p\).** The order-\(p\) subgroups of \(G\) are the \(p+1\) lines in \(G[p]\). Each is contained in \(pG\) when \(b\ge2\), so \(G/H\) has two generators and precisely \(p^2-1\) surjections to \(H\cong C_p\). This gives the first cyclic coefficient.

**4. Cyclic order \(p^2\).** Such subgroups split into two disjoint classes. The \(p^2\) graphs \(H=\langle(1,\lambda p^{b-2})\rangle\), \(\lambda\in\mathbb Z/p^2\mathbb Z\), have \(G/H\cong C_{p^b}\), hence each has \(p^2-p\) surjections to \(H\). The remaining \(p\) subgroups are \(H=\langle(p\mu,p^{b-2})\rangle\), \(\mu\in\mathbb Z/p\mathbb Z\). When \(b=2\), their quotients are cyclic of order \(p^2\), with \(p^2-p\) surjections each. When \(b=3\), all quotients have type \(C_{p^2}\oplus C_p\), with \(p^2(p-1)\) surjections each. When \(b\ge4\), the quotient for \(\mu=0\) has type \(C_{p^2}\oplus C_{p^{b-2}}\), with \(p^4-p^2\) surjections, whereas each of the other \(p-1\) quotients has type \(C_p\oplus C_{p^{b-1}}\), with \(p^2(p-1)\) surjections. Addition proves all three cases for \(N_{p,b}(C_{p^2})\).

**5. Cyclic order \(p^j\) for \(j\ge3\).** Every such subgroup projects isomorphically onto the unique order-\(p^j\) subgroup in the second factor, so it is uniquely
\[
H=\langle(x,p^{b-j})\rangle,\quad x\in C_{p^2}.
\]
Write \(\operatorname{ord}(x)=p^a\), with \(a\in\{0,1,2\}\); the numbers of choices for \(x\) are respectively \(w_0=1\), \(w_1=p-1\), \(w_2=p^2-p\). For \(t\in\{j-1,j\}\), define \(L_t=\max\{a,0,t-b+j\}\). Since \(t\ge2\), the first summand of \(p^tG\) vanishes, and direct intersection counting gives
\[
|H+p^tG|=p^{b-t+L_t},\qquad
\#\operatorname{Hom}(G/H,C_{p^t})=\frac{|G|}{|H+p^tG|}=p^{t+2-L_t}.
\]
The number of surjections \(G/H\twoheadrightarrow C_{p^j}\) is the number of homomorphisms to \(C_{p^j}\) minus those landing in its subgroup \(pC_{p^j}\cong C_{p^{j-1}}\). Therefore
\[
N_{p,b}(C_{p^j})=\sum_{a=0}^{2}w_a\bigl(p^{j+2-L_j}-p^{j+1-L_{j-1}}\bigr).
\tag{2}
\]
If \(2j-b\le0\), this equals \((p-1)(3p-2)p^j\). At \(2j-b=1\) it equals \(2(p-1)^2p^j\); at \(2j-b=2\), \((p-1)^2p^j\); and at \(2j-b\ge3\), zero. This proves the remaining cyclic coefficients.

**6. Summation.** For \(b=2,3\) the displayed coefficients sum directly to the asserted totals. For \(b=2s\) or \(b=2s+1\) with \(s\ge2\), sum the common coefficients for image orders one and two, the geometric progression \((p-1)(3p-2)\sum_{j=3}^{s}p^j\), the top cyclic boundary coefficient (respectively \((p-1)^2p^{s+1}\) and \(2(p-1)^2p^{s+1}\)), and the noncyclic total \(p(p-1)(p^{s+1}-1)\). Using \(\sum_{j=3}^{s}p^j=(p^{s+1}-p^3)/(p-1)\) yields exactly \((2p^2-1)p^{s+1}\) and \((3p-2)p^{s+2}\), respectively.

## Verification
The accompanying standard-library Python file `verify.py` independently enumerates all endomorphisms using their generator images
\[
T=\begin{pmatrix}a&c\\p^{b-2}d&e\end{pmatrix},\quad a,c,d\in\mathbb Z/p^2\mathbb Z,\ e\in\mathbb Z/p^b\mathbb Z.
\]
It tests the four congruences for \(T^2=0\), constructs the subgroup generated by the two columns, obtains its isomorphism type from order and exponent, and compares the complete histogram and total with the displayed formulas. The successful finite tests cover \(p=2\) with \(2\le b\le10\), \(p=3\) with \(2\le b\le7\), and \(p=5\) with \(2\le b\le4\). These checks are finite corroboration, not the proof for all primes and exponents.

## Relationship to prior work
Hillar and Rhea give the general endomorphism-ring matrix representation for finite abelian \(p\)-groups; the coordinate model used by the verifier is a specialization of their Theorem 3.3. Hall-polynomial theory gives systematic counts of subgroups with specified group and quotient types and hence a general computational route to (1). Schmidmeier's Theorem 1 supplies a Hall-polynomial formula, not the present explicit square-zero image spectra. Crabb counts nilpotent linear endomorphisms of vector spaces over finite fields, a different ambient category and without the order-two constraint. The present claim is the stated closed, parity-sensitive spectrum for the mixed-exponent type \((2,b)\), not any of these underlying frameworks or the shorter-exponent type \((1,b)\).

## Limitations
No claim is made about conjugacy classes of endomorphisms, non-square-zero nilpotent maps, arbitrary higher-rank finite abelian groups, or the case \(b=1\). The formulas are proved for all primes, not guessed from small examples. They may also be derivable by specializing general Hall-polynomial methods; literature priority for an equivalent specialized closed expression has not been independently certified.

## References
1. Christopher J. Hillar and Darren L. Rhea, *Automorphisms of Finite Abelian Groups*, arXiv:math/0605185v1, 8 May 2006, especially Theorem 3.3, https://arxiv.org/pdf/math/0605185.
2. Markus Schmidmeier, *Hall Polynomials via Automorphisms of Short Exact Sequences*, arXiv:0910.1962v1, 11 October 2009, especially Theorem 1, https://arxiv.org/pdf/0910.1962.
3. M. C. Crabb, *Counting nilpotent endomorphisms*, Finite Fields and Their Applications 12 (2006), 151–154, DOI:10.1016/j.ffa.2005.03.001 (abstract examined; full text not obtained).
