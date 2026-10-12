# Complete automorphism-conjugacy orbits of derivations of the three-dimensional Heisenberg Lie algebra

## Finding
Let \(k\) be any field and \(H=kx\oplus ky\oplus kz\) the three-dimensional Heisenberg Lie algebra, with alternating bracket determined by \([x,y]=z\) and all brackets with \(z\) zero. Automorphisms act on ordinary derivations by conjugation. In the basis \((x,y,z)\), write
\[
D(A,u)=\begin{pmatrix}A&0\\u&\operatorname{tr}A\end{pmatrix},\qquad A\in M_2(k),\quad u\in k^{1\times2},
\]
and set \(W_A=\operatorname{row}(A-(\operatorname{tr}A)I_2)\).

**Theorem.** Every derivation is uniquely of this form. Two derivations \(D(A,u)\) and \(D(A',u')\) lie in the same \(\operatorname{Aut}_k(H)\)-orbit if and only if \(A,A'\) are similar and, after identifying the blocks by a similarity, either both rows lie in \(W_A\) or both lie outside \(W_A\). A nonsingular \(A\) has one orbit above its similarity class; a singular \(A\) has exactly two.

For a finite field \(k=\mathbb F_q\), this gives the exact number
\[
\boxed{\#(\operatorname{Der}(H)/\operatorname{Aut}(H))=(q+1)^2.}
\]
More precisely, with each table row describing *each individual* \(2\times2\) similarity class of its type, the numbers of similarity classes, and the sizes of its one or two derivation-orbits, are:

| Rational canonical type of \(A\) | Number of types | Orbit sizes per type |
| --- | ---: | --- |
| Zero matrix | \(1\) | \(1,\ q^2-1\) |
| One nilpotent block of size two | \(1\) | \(q(q^2-1),\ q(q-1)(q^2-1)\) |
| Distinct eigenvalues \(0,\lambda\), \(\lambda\ne0\) | \(q-1\) | \(q^2(q+1),\ q^2(q-1)(q+1)\) |
| Nonzero scalar matrix \(\lambda I\) | \(q-1\) | \(q^2\) |
| Nonzero Jordan block of size two | \(q-1\) | \(q^2(q^2-1)\) |
| Two distinct nonzero eigenvalues | \((q-1)(q-2)/2\) | \(q^3(q+1)\) |
| Irreducible quadratic block | \((q^2-q)/2\) | \(q^3(q-1)\) |

For each singular block the first listed orbit is the row-space stratum, and the second its complement; each nonsingular block has one orbit. The two-orbit distinction is an exact resonance at \(\det A=0\), not a restriction on the characteristic.

## Assumptions and scope
The bracket is alternating even in characteristic two, with \([y,x]=-[x,y]\). The derivations are **ordinary** \(k\)-linear derivations, satisfying \(D([a,b])=[D(a),b]+[a,D(b)]\); no restricted \(p\)-mapping is chosen. All finite fields, including nonprime fields and characteristic two, are included. The classification is by the full group of \(k\)-linear Lie algebra automorphisms, with no scaling of derivations allowed.

## Proof
**1. Derivations and automorphisms.** The derived subalgebra and center both equal \(kz\). A derivation preserves the derived subalgebra. Write \(D(x)\) and \(D(y)\) with quotient block \(A\) and arbitrary central row \(u\). Applying \(D\) to \([x,y]=z\) forces \(D(z)=(\operatorname{tr}A)z\). Conversely these matrices satisfy the derivation identity on every pair of basis elements. Similarly the full automorphism group consists precisely of
\[
P(B,v)=\begin{pmatrix}B&0\\v&\det B\end{pmatrix},\qquad B\in\mathrm{GL}_2(k),\quad v\in k^{1\times2}.
\]
Indeed the induced map on the two-dimensional quotient may be any invertible \(B\), the bracket forces the action on \(z\) to be \(\det B\), and the central row is free.

**2. Conjugation.** Direct block multiplication yields
\[
P(B,v)D(A,u)P(B,v)^{-1}
=D\left(BAB^{-1},\ \big[v(A-(\operatorname{tr}A)I_2)+(\det B)u\big]B^{-1}\right).
\]
Consequently, after fixing the similarity class of \(A\), varying \(v\) removes precisely the translation subspace \(W_A\). The row quotient \(k^{1\times2}/W_A\) is acted on by the centralizer \(C_{\mathrm{GL}_2(k)}(A)\) through \(u\mapsto(\det B)uB^{-1}\). Thus the number of derivative orbits above a similarity class is exactly the number of centralizer orbits on this quotient; it remains to classify those.

**3. Resonance, all fields.** The elementary identity \(\det(A-(\operatorname{tr}A)I_2)=\det A\) is valid over every field. If \(\det A\ne0\) the row quotient is zero: one orbit. If \(\det A=0\) and \(A\ne0\), the matrix \(A-(\operatorname{tr}A)I_2\) has rank one. Indeed if it were zero, \(A=tI_2\) and \(t=\operatorname{tr}A=2t\), hence \(t=0\), a contradiction in any characteristic. The quotient is therefore one-dimensional. Scalar matrices \(B=aI_2\), for \(a\in k^\times\), lie in the centralizer and act on this quotient by multiplication by \(a\), since \(\det(aI_2)(aI_2)^{-1}=aI_2\). Its zero and nonzero elements form exactly two orbits. Finally, if \(A=0\), then \(W_A=0\), and the action on all rows is \(u\mapsto(\det B)uB^{-1}\). This action is transitive on the nonzero rows: in dimension two the determinant-twisted contragredient is equivalent to the standard \(\mathrm{GL}_2(k)\) action via the nondegenerate alternating form. Thus here also there are exactly two orbits. These cases exhaust all fields and prove the equivalence criterion.

**4. Individual sizes.** Let \(s(A)\) be the size of the similarity class of \(A\) in \(M_2(\mathbb F_q)\), and put \(r(A)=\operatorname{rank}(A-(\operatorname{tr}A)I_2)\). The two stratum sizes, when both are present, are
\[
s(A)q^{r(A)}\quad\text{and}\quad s(A)(q^2-q^{r(A)}).
\]
If \(A\) is nonsingular, \(r(A)=2\) and only the first expression occurs. This follows because for each matrix in the similarity class, exactly \(q^{r(A)}\) rows lie in its translated row space and all other rows form the second orbit.

The familiar centralizer orders of the seven rational canonical types yield \(s(A)=1\) for scalars, \(q^2-1\) for nontrivial Jordan blocks, \(q(q+1)\) for distinct rational eigenvalues, and \(q(q-1)\) for irreducible quadratics, giving the displayed table. There are exactly \(q+1\) singular similarity classes (zero, a nilpotent block, and \(q-1\) semisimple blocks with eigenvalues \(0,\lambda\ne0\)), while the total number of \(2\times2\) similarity classes over \(\mathbb F_q\) is \(q^2+q\). Consequently there are \((q^2-1)+2(q+1)=(q+1)^2\) derivation-orbits. The seven table types partition all \(q^4\) choices of \(A\), and multiplying each similarity-class size by \(q^2\) recovers all \(q^6\) derivations; this independently checks the orbit-size sum.

## Verification
A self-contained Python 3 program `verify.py` enumerates the *actual* action of the full automorphism group on every derivation and compares all resulting orbit sizes with the independently calculated centralizer/row-rank formula for \(q=2,3,4,5\). For \(q=2,3\), it also independently enumerates all \(3\times3\) matrices and rederives the entire derivation and automorphism matrix descriptions from the defining bracket identities, rather than assuming these identities in the census. It implements \(\mathbb F_4\) as a quadratic extension. Run `python verify.py` from the directory containing this file and `verify.py`; it prints `VERIFY_OK` on success. The all-field theorem is established by the preceding symbolic proof, not by those finite computations.

## Relationship to prior work
Feldvoss–Siciliano–Weigel prove existence theorems for **restricted** outer derivations of nilpotent restricted Lie algebras and discuss a characteristic-two Heisenberg exception. A restricted derivation respects a chosen \(p\)-mapping, whereas the present orbit theorem studies *all ordinary derivations*, without a \(p\)-mapping; that paper does not give the finite-field orbit number or the conjugation table. Dath's 2015 thesis describes derivation matrices and selected normal forms for controllability systems on **real** Heisenberg groups; these are not the complete orbits of individual derivations over arbitrary finite fields. La Rosa–Mancini describe derivation Lie algebras of two-step nilpotent Leibniz algebras over characteristic different from two; their structural matrix formulas likewise do not provide this finite-field conjugacy census. Standard similarity classifications are used as inputs, not claimed as new. The structural novelty claimed here is the exhaustive split of each matrix similarity class by the central-shear resonance and its full individual finite-field orbit-size distribution.

## Limitations
No corresponding formula is asserted for restricted derivations of a chosen \(p\)-Lie algebra, for higher-dimensional Heisenberg Lie algebras, or for similarity under arbitrary \(\mathrm{GL}_3\) rather than Lie automorphisms. Overlap with real-flow normal forms or differently phrased moduli classifications remains possible; absence from searches is not proof of novelty. No independent audit or external certification has been performed.

## References
1. J. Feldvoss, S. Siciliano, T. Weigel, *Outer restricted derivations of nilpotent restricted Lie algebras*, arXiv:1102.2629 (v1 submitted 2011-02-13), https://arxiv.org/abs/1102.2629.
2. M. R. Dath, *Contribution à l'étude de la contrôlabilité des systèmes linéaires sur les groupes de Lie nilpotents et résolubles*, doctoral thesis, 2015, especially pp. 25–28, 34–35, 51–55, https://www.mcours.net/cours/pdf/hascl2/bbgrhss2clic1049.pdf.
3. G. La Rosa, M. Mancini, *Derivations of two-step nilpotent algebras*, arXiv:2301.11058, https://arxiv.org/abs/2301.11058.
