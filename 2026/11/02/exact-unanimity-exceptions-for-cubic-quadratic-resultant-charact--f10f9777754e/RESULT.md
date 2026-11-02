# Exact unanimity exceptions for cubic--quadratic resultant characters over finite fields

## Finding
Let \(q\) be any odd prime power and \(c\in\mathbb F_q^\times\). Write \(\chi\) for the quadratic character, extended by \(\chi(0)=0\), and let
\[
 \mathcal Q_q=\{X^2+v:\ v\in\mathbb F_q,\ \chi(-v)=-1\}.
\]
This is precisely the family of monic irreducible trace-zero quadratics and has size \((q-1)/2\). Define the *resultant signature* of \(c\) on \(\mathcal Q_q\) by the characters \(\chi(\operatorname{Res}_X(X^3+c,g))\) as \(g\) varies. The signature is **unanimous** if these characters are all equal.

**Theorem (complete odd-characteristic classification).** The signature is unanimous if and only if
\[
 \begin{array}{c|c}
 q&\text{condition on }c\\ \hline
 3&\text{every nonzero }c\\
 7&\text{every nonzero }c\\
 13&c\text{ is not a cube in }\mathbb F_{13}^\times\\
 19&c\text{ is a cube in }\mathbb F_{19}^\times.
 \end{array}
\]
No resultant appearing in this statement vanishes. Hence for every odd prime power \(q\ge23\), and also for every other excluded \((q,c)\), there are **both** square and nonsquare resultants among the tests \(g\in\mathcal Q_q\). In particular, \(19\) is the largest field size admitting unanimity.

## Assumptions and scope
Fields may have prime or proper prime-power cardinality, including characteristic three. The cubic \(X^3+c\) is monic with \(c\ne0\); no irreducibility or separability of the cubic is assumed. Only irreducible quadratics with linear coefficient zero are tested. A square/nonsquare refers to the nonzero square class in \(\mathbb F_q\), not irreducibility of the cubic.

## Proof
**1. Resultant reduction and nonvanishing.** In \(\mathbb F_q[X]/(X^2+v)\), the class \(\alpha\) of \(X\) satisfies \(\alpha^2=-v\), so
\[
 \operatorname{Res}_X(X^3+c,X^2+v)=(c-v\alpha)(c+v\alpha)=c^2+v^3.
\]
If \(c^2+v^3=0\), then \(\chi(-v)=\chi(-v^3)=\chi(c^2)=1\), contradicting irreducibility. Therefore the character is always \(\pm1\).

Let \(N=(q-1)/2\) and let the signed bias be
\[
 D_q(c)=\sum_{v:\chi(-v)=-1}\chi(v^3+c^2).
\]
Unanimity is exactly \(\lvert D_q(c)\rvert=N\). Put \(e=\chi(-1)\),
\[
 H=\sum_{x\in\mathbb F_q}\chi(x^3+c^2),\qquad
 K=\sum_{x\in\mathbb F_q}\chi(1+c^2x^3).
\]
For \(x\ne0\), inversion gives \(\chi(x(x^3+c^2))=\chi(1+c^2x^{-3})\), because \(x(x^3+c^2)=x^4(1+c^2x^{-3})\). The contribution at zero vanishes on the left and equals one in \(K\). Since the irreducible-quadratic indicator for \(v\ne0\) is \((1-e\chi(v))/2\), we obtain the exact identity
\[
 \boxed{D_q(c)=\frac{H-e(K-1)-1}{2}.}\tag{1}
\]

**2. Bijective cube map.** If \(3\nmid q-1\), the cube map permutes \(\mathbb F_q\). This includes all fields of characteristic three and all \(q\equiv2\pmod3\). Thus \(H=K=0\), and (1) reduces to
\[
 D_q(c)=\frac{e-1}{2}\in\{-1,0\}.
\]
Unanimity requires \(N\le1\), hence \(q=3\); there \(e=-1\) and \(N=1\), so it does occur.

**3. Cubic characters and a universal bound.** Now assume \(3\mid q-1\). Choose a character \(\psi\) of exact order three, let \(\bar\psi\) be its complex conjugate, and put
\[
 J=\sum_{t\in\mathbb F_q}\psi(t)\chi(1+t),\qquad w=\psi(c^2)\in\{1,\omega,\omega^2\},
\]
where \(\omega\) is a primitive complex cube root of unity. The characters \(\psi,\chi,\psi\chi\) are nontrivial, so the standard Jacobi-sum identity gives \(\lvert J\rvert=\sqrt q\). Counting cube roots of each element as \(1+\psi(t)+\bar\psi(t)\) (also at zero, by extension) yields
\[
 H=wJ+\bar w\bar J,\qquad K=\bar w J+w\bar J.
\]
Therefore
\[
 D_q(c)=
 \begin{cases}
 (w-\bar w)(J-\bar J)/2,&e=1,\\
 (w+\bar w)(J+\bar J)/2-1,&e=-1.
 \end{cases}\tag{2}
\]
When \(e=1\), the field size is \(q\equiv1\pmod{12}\). If \(w=1\), then \(D_q(c)=0\). Otherwise \(\lvert D_q(c)\rvert\le\sqrt{3q}\). Unanimity demands \((q-1)/2\le\sqrt{3q}\), whence \(q\le7+4\sqrt3<14\). The only odd prime power congruent to one modulo twelve in this range is \(q=13\).

When \(e=-1\), the field size is \(q\equiv7\pmod{12}\). If \(w=1\), (2) implies \(\lvert D_q(c)\rvert\le2\sqrt q+1\). Hence unanimity gives \((q-1)/2\le2\sqrt q+1\), which implies \(\sqrt q\le2+\sqrt7\) and \(q<22\): only \(q=7,19\) remain. If \(w\ne1\), then \(w+\bar w=-1\), so \(\lvert D_q(c)\rvert\le\sqrt q+1\); unanimity implies \(\sqrt q\le3\), leaving only \(q=7\).

**4. Exact small-field decisions.** In each surviving field, \(D_q(c)\) is constant on the cosets of cubes, because (2) depends on \(c\) only through \(w\). Directly summing \(\chi(v^3+c^2)\) over \(\chi(-v)=-1\) gives the following complete values, with coset representatives listed in order:
\[
\begin{array}{c|c|c|c}
q&c\text{ representatives}&D_q(c)&N\\\hline
7&(1,2,4)&(3,-3,-3)&3\\
13&(1,2,4)&(0,6,-6)&6\\
19&(1,2,4)&(-9,3,3)&9.
\end{array}
\]
For these fields, \(1\) represents the cube subgroup and \(2,4\) represent its two other cosets. Hence the uniformity conditions in the statement follow. Combined with Step 2 and all exhaustive cutoffs in Step 3, this proves the theorem for every odd prime power. \(\square\)

## Verification
The standalone `verify_unanimity.py` computes quadratic characters and full trace-zero irreducible test families directly over eighteen finite fields, including quadratic extensions of prime fields. It checks every nonzero \(c\), the nonvanishing assertion, both signs, and the complete exceptional classification. Its expected final line is `VERIFY_OK fields=18 parameter_classes=572`. The finite tests are independent corroboration; the proof above covers all odd prime powers.

## Relationship to prior work
Character sums \(\sum\chi(x^3+b)\) and \(\sum\chi(x(x^3+b))\) and their evaluation by cubic Jacobi sums are classical; Berndt and Evans (1979), especially their Theorems 2.6--2.8 and §6, give broader formulas for those constituent sums. Those formulas and the Jacobi-sum square-root bound are used as established tools, not claimed as new. Gómez-Pérez, Nicolás, Ostafe, and Sadornil (arXiv:1206.4979v1, June 21, 2012) discuss resultant characters and polynomial stability for a different purpose. The finding here is the *all-odd-prime-power extremal classification* of unanimous resultants for the trace-zero irreducible-quadratic test family, including the exceptional field size \(19\). No inspected source stated this restricted-resultant classification; the possibility of an equivalent statement embedded in older cyclotomic/Jacobsthal literature remains an acknowledged priority risk.

## Limitations
This concerns only pure cubics and the natural trace-zero test subfamily, not arbitrary cubic coefficients or all quadratic test polynomials. The result is an extremal yes/no classification, not a formula for the complete sign distribution for every parameter. The case \(q=3\) has only one test quadratic and is intrinsically trivial; the substantive exceptional fields are \(7,13,19\). Classical character-sum formulas substantially overlap the proof ingredients. Independent mathematical validation has not been performed.

## References
- B. C. Berndt and R. J. Evans, *Sums of Gauss, Eisenstein, Jacobi, Jacobsthal, and Brewer*, Illinois Journal of Mathematics 23 (1979), 374--437, doi:10.1215/ijm/1256048104; especially §2 and §6.
- D. Gómez-Pérez, A. P. Nicolás, A. Ostafe, and D. Sadornil, *Stable Polynomials over Finite Fields*, arXiv:1206.4979v1, first public version 2012-06-21; later published in Revista Matemática Iberoamericana 30 (2014), 523--535.
- B. C. Berndt, R. J. Evans, and K. S. Williams, *Gauss and Jacobi Sums*, Wiley, 1998, background on the standard Jacobi-sum magnitude identity.
