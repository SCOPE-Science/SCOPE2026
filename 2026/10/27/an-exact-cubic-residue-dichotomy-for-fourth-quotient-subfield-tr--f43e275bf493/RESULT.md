# An exact cubic-residue dichotomy for fourth-quotient subfield translates

## Finding
Let \(q\equiv7\pmod{12}\) be any prime power, let \(F=\mathbb F_q\), let \(E=\mathbb F_{q^2}\), and put
\[
d=\frac{3(q+1)}4,\qquad H=(E^\times)^d,\qquad S=F+(H\cup\{0\}).
\]
The integer \(d\) divides \(q^2-1\). Then the exact cardinality is
\[
|S|=\begin{cases}
\frac{q(q+2)}3,& 2^{(q-1)/3}=1\text{ in }F,\\
\frac{q(2q+1)}3,& 2^{(q-1)/3}\ne1\text{ in }F.
\end{cases}
\]
In particular, \(S\ne E\) in either case. Its complement has respectively \(2q(q-1)/3\) or \(q(q-1)/3\) elements.

There is an exact, stronger representation law. Write \(R(x)=|\{(a,h)\in F\times(H\cup\{0\}):x=a+h\}|\). Let \(C=(F^\times)^3\). Choose a generator \(h\) of \(H\), choose any nonzero \(F\)-linear \(\pi:E\to F\) with kernel \(F\), and set \(u=\pi(h)\) and \(T=h+h^q\). Then \(u,T\ne0\), and the complete representation law is
\[
R(x)=\begin{cases}
(q+2)/3,&\pi(x)=0,\\
3,&\pi(x)\in uC\text{ and }2\in C,\\
2,&\pi(x)\in uC\text{ and }2\notin C,\\
1,&\pi(x)\in TuC\text{ and }2\notin C,\\
0,&\text{otherwise}.
\end{cases}
\]

## Assumptions and scope
Every quantifier concerns **all** finite fields of odd prime-power order \(q\equiv7\pmod{12}\), not merely prime fields. Cubicity is taken in \(F^\times\). The expression \(F+(H\cup\{0\})\) is a set sum, while \(R\) counts ordered pairs. There are no hypotheses on the characteristic beyond this congruence, and no claims about other congruence classes.

## Proof
1. Since \(q\equiv7\pmod{12}\), both \(3\mid(q-1)\) and \(4\mid(q+1)\). Consequently \(d\mid(q-1)(q+1)\), and \(|H|=4(q-1)/3\). By cyclicity of the multiplicative groups,
\[
H\cap F^\times=C,\qquad |C|=(q-1)/3.
\]
The quotient \(H/C\) has order four. Any generator \(h\) gives the disjoint decomposition
\[
H=C\,\sqcup\,hC\,\sqcup\,h^2C\,\sqcup\,h^3C.
\]
The subfield is the kernel of \(\pi\), so \(u=\pi(h)\ne0\).

2. The element \(\zeta=h^{q-1}\) has multiplicative order four, so \(\zeta+\zeta^{-1}=0\). With \(T=h+h^q\in F\) and \(N=h^{q+1}\in H\cap F^\times=C\),
\[
\frac{T^2}{N}=(1+\zeta)(1+\zeta^{-1})=2.
\]
Thus \(T\ne0\), \(T^2=2N\), and \(T\in C\) if and only if \(2\in C\), since the order-three quotient \(F^\times/C\) has injective squaring. The latter is equivalent to \(2^{(q-1)/3}=1\) in \(F\).

3. The quadratic identity \(h^2-Th+N=0\) gives \(\pi(h^2)=Tu\). Also \(h^{-1}=(T-h)/N\) gives
\[
\pi(h^3)=h^4\pi(h^{-1})=-\frac{h^4}{N}u.
\]
Now \(h^4/N\in C\), while \(-1\in C\) because \(|C|=(q-1)/3\) is even. Therefore the images of the four multiplicative cosets of \(C\) in \(H\) are respectively
\[
\pi(C)=\{0\},\quad\pi(hC)=uC,\quad\pi(h^2C)=TuC,\quad\pi(h^3C)=uC.
\]
On each of the last three cosets, \(\pi\) is a bijection onto the indicated cubic coset. On \(C\cup\{0\}\), the projection is zero on exactly \((q-1)/3+1\) elements.

4. For each \(x\in E\), the assignment \(h'\mapsto(x-h',h')\) bijects \(\{h'\in H\cup\{0\}:\pi(h')=\pi(x)\}\) with the representations counted by \(R(x)\). Step 3 gives the definitive piecewise formula in Finding. Distinct cubic cosets in \(F^\times\) are disjoint, each of size \((q-1)/3\), and every fiber of \(\pi\) has size \(q\). Hence \(|S|=q(1+(q-1)/3)\) or \(q(1+2(q-1)/3)\), as stated. Both are strictly smaller than \(q^2\), completing the proof.

## Verification
Run `python3 verify.py` with Python 3 and no dependencies. It constructs each quadratic extension as a polynomial quotient, certifies a primitive multiplicative generator by exact exponentiation, enumerates the relevant subgroup and every translate, and checks the full representation profile and both cardinalities for base primes \(7,19,31,43,67,79,103\). It also checks \(T^2=2N\) exactly in each field. The script's successful terminal line is `CERTIFICATE_OK 7 complete quadratic-prime-field enumerations`. These finite checks corroborate, but do not replace, the algebraic proof for all prime powers.

## Relationship to prior work
Zhou and Wu, *Covering finite fields by translates of multiplicative subgroups*, arXiv:2610.25228v1 (public October 18, 2026), Proposition 5.3, give a necessary projection bound for covering by subfield translates; Example 5.4 treats a different, quotient-order-three family with quadratic-residue behavior. The present exact cardinality and multiplicity law treats the next natural quotient order, four, where a cubic-residue condition on \(2\) controls the answer. Martin and Yip, *Distribution of power residues over shifted subfields and maximal cliques in generalized Paley graphs*, arXiv:2403.04312, Theorems 1.2–1.3, give character-sum estimates for individual shifted subfields; these do not provide this exact index-varying distribution. Zhou, Danchev and Wu, arXiv:2512.16942, derive broad covering bounds for sums of special subsets, not this exact distribution.

## Limitations
This theorem applies only when \(q\equiv7\pmod{12}\) and \(d=3(q+1)/4\). It does not decide analogous cardinalities at other indices or all translate sets. The finite verifier tests prime bases only; the extension to nonprime prime-power bases is algebraic. Exhaustive identification of every equivalent unpublished or unindexed table is not possible, and independent mathematical validation has not been performed.

## References
1. J. Zhou and H. Wu, *Covering finite fields by translates of multiplicative subgroups*, arXiv:2610.25228v1 (2026-10-18), Sections 1 and 5. https://arxiv.org/abs/2610.25228
2. G. Martin and C. H. Yip, *Distribution of power residues over shifted subfields and maximal cliques in generalized Paley graphs*, arXiv:2403.04312, Theorems 1.2–1.3. https://arxiv.org/abs/2403.04312
3. J. Zhou, P. V. Danchev and H. Wu, *Finite fields whose members are the sum of a potent and a 5-potent*, arXiv:2512.16942, Theorem 2.1. https://arxiv.org/abs/2512.16942
