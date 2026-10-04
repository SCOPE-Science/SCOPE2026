# A characteristic-three idempotent line in the quandle algebra of \(R_3\)
## Finding
Let \(K\) be a field and let \(R_3=\mathbb Z/3\mathbb Z\) be the dihedral quandle with operation \(i*j=2j-i\). The quandle algebra \(K[R_3]\) has basis \(e_0,e_1,e_2\) and multiplication \(e_i e_j=e_{2j-i}\), with subscripts modulo \(3\). Put \(w=e_0+e_1+e_2\).

If \(\operatorname{char}K\ne3\), the full set of idempotents is
\[
\left\{0,e_0,e_1,e_2,\frac{w}{3},e_0-\frac{w}{3},e_1-\frac{w}{3},e_2-\frac{w}{3}\right\}.
\]
Thus there are exactly eight idempotents over every such field, including characteristic \(2\).

If \(\operatorname{char}K=3\), the full set of idempotents is
\[
\{0\}\cup\left\{
\frac{u^2+u}{2}e_0+\frac{u^2-u}{2}e_1+(1-u^2)e_2: u\in K
\right\}.
\]
The nonzero part is therefore an affine line of augmentation-one idempotents. In particular, if \(K=\mathbb F_q\) has characteristic \(3\), then \(K[R_3]\) has exactly \(q+1\) idempotents.

## Assumptions and scope
The coefficient ring is a field. The result concerns the three-element dihedral quandle \(R_3\) and classifies \(K\)-rational idempotents in its quandle algebra. It does not assert a classification for larger dihedral quandles, general coefficient rings, or scheme-theoretic multiplicities of the idempotent equations.

The primary classification is MSC 2020 \(17\mathrm D99\), the primary code used in the established quandle-ring idempotent literature.

## Proof
Write
\[
x=a e_0+b e_1+c e_2.
\]
A direct use of \(e_i e_j=e_{2j-i}\) gives
\[
x^2=(a^2+2bc)e_0+(b^2+2ac)e_1+(c^2+2ab)e_2.
\]
Hence \(x^2=x\) is equivalent to
\[
a^2+2bc=a,\qquad b^2+2ac=b,\qquad c^2+2ab=c.\tag{1}
\]
Let \(s=a+b+c\). Summing (1) gives \(s^2=s\), so \(s\in\{0,1\}\). Subtracting consecutive equations in (1) yields
\[
(a-b)(s-1-3c)=0,
\]
\[
(b-c)(s-1-3a)=0,
\]
\[
(c-a)(s-1-3b)=0.\tag{2}
\]

Assume first that \(\operatorname{char}K\ne3\). If \(s=1\), equations (2) become
\[
(a-b)c=(b-c)a=(c-a)b=0.
\]
If \(abc\ne0\), then \(a=b=c=1/3\), giving \(w/3\). If one coordinate is zero, the displayed products force another coordinate to be zero, and \(s=1\) gives one of \(e_0,e_1,e_2\).

Now let \(s=0\). If \(a,b,c\) were pairwise distinct, (2) would force \(a=b=c=-1/3\), a contradiction. Thus two coordinates are equal. By symmetry take \(b=c=t\), so \(a=-2t\). The second equation of (1) becomes
\[
-3t^2-t=0,
\]
so \(t=0\) or \(t=-1/3\). The first choice gives \(0\); the second gives \(e_0-w/3\). Permuting coordinates gives the other two idempotents. This proves completeness in characteristic different from \(3\).

Assume now that \(\operatorname{char}K=3\). If \(s=0\), equations (2) force \(a=b=c\), and then any equation in (1) gives \(a=0\); hence \(x=0\). If \(s=1\), equations (2) are automatic. Substituting \(c=1-a-b\) into the first equation of (1) gives
\[
a^2+ab+b^2-a-b=0.
\]
In characteristic \(3\), \(a^2+ab+b^2=(a-b)^2\). Set \(u=a-b\). Then \(a+b=u^2\), and since \(2\) is invertible,
\[
a=\frac{u^2+u}{2},\qquad b=\frac{u^2-u}{2},\qquad c=1-u^2.
\]
Conversely these formulas satisfy (1), so they give every augmentation-one idempotent and prove the claimed affine-line parametrization.

## Verification
The proof is symbolic and valid over an arbitrary field. The accompanying exact checker independently enumerates every coefficient triple over \(\mathbb F_2,\mathbb F_3,\mathbb F_5,\mathbb F_7,\mathbb F_{11}\), and over \(\mathbb F_9\). It obtains eight idempotents in characteristics different from \(3\), four over \(\mathbb F_3\), and ten over \(\mathbb F_9\), exactly as predicted. Its recorded output ends with `CHECK_OK`.

## Relationship to prior work
Elhamdadi, Ta, and Virgin, arXiv:2609.03799v1, develop a Fourier-analytic approach to idempotents in quandle algebras and prove the integral idempotent conjecture for Takasaki quandles, including dihedral quandles. Their public abstract states an integral-coefficient result and does not state a coefficient-field classification for \(R_3\).

Bardakov and Elhamdadi, arXiv:2601.07057v1, is the closest inspected primary source. In its full public text, Proposition 4.2 computes powers of the augmentation ideal of \(R_3\), Corollary 4.3 rules out nonzero augmentation-zero idempotents in \(\mathbb Z[R_3]\), and Proposition 4.4 exhibits the single field-valued idempotent \(-\frac13(E_1+E_2)\) when the field characteristic is not \(3\). The paper does not state the complete eight-point classification for \(\operatorname{char}K\ne3\) or the characteristic-three affine line above.

Elhamdadi, Nunez, Singh, and Swain, DOI 10.1142/S0129167X23500118, studies idempotents in integral quandle rings and uses primary MSC 2020 \(17\mathrm D99\). Its scope and statements do not imply the coefficient-field boundary classified here.

## Limitations
The current claim is only about \(K\)-rational idempotents of \(K[R_3]\). It does not classify idempotents over nonfields, larger \(R_n\), or all Takasaki quandles, and it makes no assertion about the scheme structure of the polynomial solution set. A recent Fourier-analysis preprint was inspectable through its public metadata and abstract rather than its complete text; this leaves a small literature-overlap risk, recorded in the review.

## References
1. M. Elhamdadi, L. Ta, B. Virgin, *Fourier Analysis and Idempotents in Quandle Algebras*, arXiv:2609.03799v1, 2026.
2. V. Bardakov, M. Elhamdadi, *Idempotents and Powers of Ideals in Quandle Rings*, arXiv:2601.07057v1, 2026.
3. M. Elhamdadi, B. Nunez, M. Singh, D. Swain, *Idempotents, free products and quandle coverings*, International Journal of Mathematics 34 (2023), DOI 10.1142/S0129167X23500118.
