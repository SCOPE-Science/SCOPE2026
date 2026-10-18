# A supersingular genus-four Artin–Schreier curve with minimal geometric automorphism group

## Finding

Let \(X/\mathbb F_3\) be the smooth projective model of
\[
 y^3-y=x^5+x^4+x^2.
\]
Its genus is \(4\), its \(3\)-rank is \(0\), and its full geometric automorphism group is \(C_3\). Its zeta function is
\[
 Z(X,T)=\frac{P_X(T)}{(1-T)(1-3T)},\quad
 P_X(T)=(1+3T^2)(1+3T+3T^2)(1+3T^2+9T^4).
\]
Equivalently,
\[
 P_X(T)=1+3T+9T^2+18T^3+36T^4+54T^5+81T^6+81T^7+81T^8.
\]
The Newton polygon of the Jacobian has all eight slopes \(1/2\), hence the Jacobian is supersingular. Among supersingular Artin–Schreier curves in characteristic \(3\) having geometric automorphism group exactly \(C_3\), genus \(4\) is minimal.

## Assumptions and scope

The base field is \(\mathbb F_3\); geometric automorphisms and supersingularity are considered after extension to an algebraic closure. The curve is the smooth projective *normalization* of its displayed affine plane model; its unique place above the pole at infinity is counted in each finite-field point count. The word supersingular means that all Newton slopes of its Jacobian are \(1/2\); it does not assert the stronger superspecial property.

## Proof

**1. Genus, rank, and automorphisms.** The polynomial on the right has a unique pole at infinity of order \(5\), prime to \(3\). The Artin–Schreier extension is geometrically connected, with a unique rational point above infinity. Riemann–Hurwitz and Deuring–Shafarevich for this one-pole cover give
\[
 g(X)=\frac{(3-1)(5-1)}2=4,\qquad \gamma(X)=0.
\]
Tafazolian–Kazemifard, Lemma 3.3, establishes for this *exact equation* that \(\operatorname{Aut}_{\overline{\mathbb F}_3}(X)=C_3\). For completeness, their rigidity argument applies since this is not a Valentini–Madan exceptional cover, so every geometric automorphism descends to \(x\mapsto Ax+B\), acting on \(y\) as \(y\mapsto uy+cx+\delta\), where \(A\ne0\) and \(u\in\mathbb F_3^\times\). Comparing coefficients of degrees \(5,4,2\) in the Artin–Schreier equation gives
\[
 u=A^5,\qquad A^4(1+2B)=u,\qquad A^2(1+B^3)=u.
\]
Thus \(A=1+2B\) and \(A^3=1+B^3\). Cubing the first identity also yields \(A^3=1+2B^3\), so \(B=0\), \(A=u=1\). The remaining Artin–Schreier equation forces \(c=0\) and \(\delta\in\mathbb F_3\); these three translations constitute the whole automorphism group.

**2. Exact point counts.** For \(n=1,2,3,4\), exhaustively enumerate all pairs \((x,y)\in\mathbb F_{3^n}^2\) that satisfy the affine equation, then add its single rational point at infinity. Using the explicitly irreducible defining polynomials
\[
 t,\quad t^2+1,\quad t^3+2t+1,\quad t^4+t+2
\]
for the four extension fields, the resulting counts are
\[
 \begin{array}{c|rrrr}n&1&2&3&4\\\hline
 \#X(\mathbb F_{3^n})&7&19&28&91.
 \end{array}
\]
The accompanying certificate constructs each field from scratch, verifies its modulus is irreducible by trial division by every monic polynomial up to half its degree, tests every affine pair directly, and independently checks the counts by the trace-zero characterization of \(y^3-y\).

**3. Zeta function and slopes.** Put \(S_n=3^n+1-\#X(\mathbb F_{3^n})\). The first four values are \((-3,-9,0,-9)\). For \(P_X(T)=\sum_{j=0}^8 c_jT^j\), \(c_0=1\), Newton's identities
\[
 k c_k=-\sum_{j=1}^{k}c_{k-j}S_j \qquad(1\le k\le4)
\]
give \((c_1,c_2,c_3,c_4)=(3,9,18,36)\). The Weil functional equation for a genus-four curve over \(\mathbb F_3\) gives \(c_{8-j}=3^{4-j}c_j\) for \(0\le j\le4\), hence the full numerator displayed above. The three-factor identity follows by direct multiplication. Each coefficient satisfies
\[
 v_3(c_j)\ge j/2\qquad(0\le j\le8),
\]
where \(v_3(0)=\infty\) conventionally (all displayed coefficients are nonzero), while the endpoints are \((0,0)\) and \((8,4)\). Therefore the lower Newton polygon is the single segment of slope \(1/2\): the Jacobian is supersingular.

**4. Minimal genus.** Every supersingular curve has \(3\)-rank zero. Tafazolian–Kazemifard's sharp numerical classification (Theorem 1.1) rules out \(3\)-rank-zero Artin–Schreier curves with full geometric group \(C_3\) in genera \(1\), \(2\), or \(3\). A smooth genus-zero curve over an algebraic closure has the infinite automorphism group \(\mathrm{PGL}_2\). Thus genus \(4\) is the first possibility, realized by \(X\).

## Verification

Run `python3 check_supersingular_as.py` with standard-library Python 3. It returns `EXACT_CERTIFICATE_PASS` after reproducing the four complete finite-field counts, their trace cross-checks, Newton identities, Weil reciprocity, factorization, and slope inequalities. Its printed point counts are \(7,19,28,91\) and its coefficient vector is \((1,3,9,18,36,54,81,81,81)\). The mathematical justification for extending four counts to the degree-eight polynomial is the Weil functional equation, **not** an assumption based on finite experimentation.

## Relationship to prior work

The explicit curve and its minimal automorphism group already occur in Tafazolian–Kazemifard (2026, Lemma 3.3). Their Question 7.5 explicitly asks which genera permit supersingular Artin–Schreier curves with only the deck automorphisms. The new assertion is the exact zeta numerator/Newton polygon of their model and the resulting sharp genus-four answer in characteristic \(3\). Duque-Rosero et al. classify genus-three/four Artin–Schreier standard forms and reconstructing moduli invariants, including the genus-four characteristic-three family containing this model, but do not compute this numerator or its Newton polygon. Dragutinović studies supersingular genus-four moduli and bounds the dimensions of their Artin–Schreier strata, but does not identify the present prime-field model or establish the minimal full-\(C_3\) supersingular case. Earlier genus-four supersingularity constructions do not supply this simultaneous automorphism constraint. The additive-polynomial supersingular families of Bouw et al., and Zhu's explicit examples, do not cover this degree-five characteristic-three equation.

## Limitations

The result establishes one explicit *supersingular*, not necessarily superspecial, curve and sharp minimal genus for characteristic \(3\). It does not classify all such curves, their \(a\)-numbers, or the analogous minimal genera in other characteristics. Potential matching unindexed finite-field curve tables remain a literature risk. The certificate is exhaustive only over the four specified finite extensions; the infinite-field Newton-polygon conclusion uses standard genus-four zeta-function theorems and an exact polynomial valuation argument. No independent external validation is claimed.

## References

1. S. Tafazolian and A. Kazemifard, *Artin–Schreier Curves of Prescribed \(p\)-Rank Without Extra Automorphisms*, arXiv:2610.13279v1, 9 October 2026, Theorem 1.1, Lemma 3.3, Question 7.5. https://arxiv.org/html/2610.13279v1
2. J. Duque-Rosero, H. Goodson, E. Lorenzo García, B. Malmskog and R. Scheidler, *On Invariants of Artin–Schreier Curves*, arXiv:2401.08843v2, §§3–4. https://arxiv.org/pdf/2401.08843
3. D. Dragutinović, *Oort's Conjecture and Automorphisms of Supersingular Curves of Genus Four*, arXiv:2405.01282, §3.1. https://arxiv.org/pdf/2405.01282
4. H. Zhu, *Some Families of Supersingular Artin–Schreier Curves in Characteristic Greater Than Two*, arXiv:0809.0104. https://arxiv.org/pdf/0809.0104
5. I. Bouw et al., *Zeta Functions of a Class of Artin–Schreier Curves with Many Automorphisms*, arXiv:1410.7031. https://arxiv.org/pdf/1410.7031
