# Conjugations yield non-bicircular generalized bi-circular idempotents

## Statement

Let \(X\) be a nonzero complex normed space admitting a conjugation, i.e. a conjugate-linear surjective isometry \(J:X\to X\) with \(J^2=I\). Fix distinct \(\lambda_1,\lambda_2\in\mathbb T\) and define
\[
P_1=\frac{J-\lambda_2 I}{\lambda_1-\lambda_2},\qquad
P_2=\frac{\lambda_1 I-J}{\lambda_1-\lambda_2}.
\]
Then \(P_1,P_2\) are distinct nonzero real-linear idempotents satisfying
\[
P_1+P_2=I,\qquad P_1P_2=P_2P_1=0,
\]
and
\[
\lambda_1P_1+\lambda_2P_2=J.
\]
Thus \(\{P_1,P_2\}\) is a family of generalized bi-circular idempotents for every distinct phase pair \((\lambda_1,\lambda_2)\).

More precisely, for \(\alpha,\beta\in\mathbb T\),
\[
S_{\alpha,\beta}:=\alpha P_1+\beta P_2
\]
is an isometry if and only if
\[
\alpha=\beta
\quad\text{or}\quad
\frac{\alpha}{\beta}=\frac{\lambda_1}{\lambda_2}.
\]
Consequently, for distinct phases the associated pair is not bi-circular: only one relative phase class gives an isometry.

On \(C^1[0,1]\) with
\[
\|f\|_\sigma=|f(0)|+\|f'\|_\infty,
\]
pointwise conjugation \(Jf=\overline f\) is such a conjugation. Choosing
\[
\lambda_1=1,\qquad \lambda_2=i
\]
gives an explicit generalized bi-circular family with \(\lambda_1+\lambda_2=1+i\ne0\) which is not bi-circular. This contradicts the dichotomy asserted in the abstract of arXiv:2609.18967v1 and, more specifically, contradicts its Theorem 3.4 for Form IV isometries.

## Proof

Put \(\delta=\lambda_1-\lambda_2\). Since \(|\lambda_1|=|\lambda_2|=1\),
\[
\overline\delta
=\overline{\lambda_1}-\overline{\lambda_2}
=-\frac{\delta}{\lambda_1\lambda_2}.
\]
Using conjugate-linearity of \(J\),
\[
JP_1x
=\frac{x-\overline{\lambda_2}Jx}{\overline\delta}
=\lambda_1\frac{Jx-\lambda_2x}{\delta}
=\lambda_1P_1x.
\]
Similarly \(JP_2=\lambda_2P_2\). The displayed definitions immediately give \(P_1+P_2=I\). Hence
\[
P_1P_2
=\frac{JP_2-\lambda_2P_2}{\delta}=0,
\]
and similarly \(P_2P_1=0\). Since \(P_1+P_2=I\), it follows that \(P_1^2=P_1\) and \(P_2^2=P_2\). Neither idempotent can vanish on a nonzero complex space: for example \(P_1=0\) would imply \(J=\lambda_2I\), incompatible with conjugate-linearity after applying both sides to \(ix\) for nonzero \(x\). Finally,
\[
\lambda_1P_1+\lambda_2P_2=J,
\]
so the associated map is a surjective isometry.

For the exact phase classification, write
\[
S_{\alpha,\beta}=aJ+bI,
\]
where
\[
a=\frac{\alpha-\beta}{\lambda_1-\lambda_2},\qquad
b=\frac{\beta\lambda_1-\alpha\lambda_2}{\lambda_1-\lambda_2}.
\]
Every conjugation has a nonzero fixed vector \(u\): if \(x+Jx\ne0\), take \(u=x+Jx\); otherwise \(Jx=-x\) and \(u=ix\) is fixed. On the complex line \(\mathbb Cu\),
\[
J(zu)=\overline z\,u,
\]
so
\[
S_{\alpha,\beta}(zu)=(a\overline z+bz)u.
\]
If \(S_{\alpha,\beta}\) is an isometry, then for every real \(t\),
\[
|ae^{-it}+be^{it}|=1.
\]
Squaring the modulus shows that
\[
|a|^2+|b|^2+2\operatorname{Re}(a\overline b e^{-2it})
\]
is independent of \(t\), hence \(a\overline b=0\). Thus either \(a=0\), equivalently \(\alpha=\beta\), or \(b=0\), equivalently
\[
\beta\lambda_1=\alpha\lambda_2
\quad\Longleftrightarrow\quad
\frac{\alpha}{\beta}=\frac{\lambda_1}{\lambda_2}.
\]
Conversely, if \(\alpha=\beta\), then \(S_{\alpha,\beta}=\alpha I\); if \(\alpha/\beta=\lambda_1/\lambda_2\), then \((\alpha,\beta)=\gamma(\lambda_1,\lambda_2)\) for some \(\gamma\in\mathbb T\), so \(S_{\alpha,\beta}=\gamma J\). Both are isometries.

## Explicit counterexample on \(C^1[0,1]\)

Let \(Jf=\overline f\), \(\lambda_1=1\), and \(\lambda_2=i\). Then
\[
P_1f=\frac{\overline f-if}{1-i},\qquad
P_2f=\frac{f-\overline f}{1-i},
\]
and
\[
P_1+iP_2=J.
\]
Thus \(\{P_1,P_2\}\) is a generalized bi-circular family with \(1+i\ne0\). It is not bi-circular. Indeed, choose the distinct phases \(\alpha=1\), \(\beta=-1\), and the constant function \(f\equiv i\). Then
\[
P_1(i)=1,\qquad P_2(i)=i-1,
\]
so
\[
(P_1-P_2)(i)=2-i.
\]
Therefore
\[
\|i\|_\sigma=1,
\qquad
\|(P_1-P_2)(i)\|_\sigma=|2-i|=\sqrt5,
\]
and \(P_1-P_2\) is not an isometry.

Pointwise conjugation is a Form IV isometry in the notation of arXiv:2609.18967v1: it is obtained from \(T(0)=0\), \(c=1\), \(\beta\equiv1\), and \(\phi=\mathrm{id}\). These parameters satisfy
\[
\beta(t)\overline{\beta(\phi(t))}=1,
\qquad
\phi^2(t)=t,
\]
which are exactly the conditions appearing in Theorem 3.4. Nevertheless the resulting idempotent family above is not bi-circular. The final implication in that theorem therefore does not follow from those conditions.

## Context and significance

The current arXiv version states that a generalized bi-circular family on this \(C^1[0,1]\) space must either arise from opposite phases \(\lambda_1+\lambda_2=0\) or be bi-circular. The example above has neither property. The obstruction is structural rather than special to differentiable functions: conjugate-linearity changes scalars by complex conjugation, so a real-linear isometry can have the required two real eigenspaces for an arbitrary pair of unit phases without making every phase recombination isometric.

Earlier literature already shows that generalized bi-circular projections/idempotents can be subtler than an average-of-identity-and-reflection picture. In particular, Abubaker--Botelho--Jamison give generalized bi-circular projections not representable as the average of the identity with an isometric reflection, and Botelho--Miura published a 2019 corrigendum explaining that an earlier classification on differentiable-function spaces had omitted an additional case. Those works are prior context; the claim here is specifically that the current dichotomy and Theorem 3.4 of arXiv:2609.18967v1 are contradicted by the conjugation construction above.

## Limitations

This finding does not provide a corrected complete classification of all generalized bi-circular idempotents on \(C^1[0,1]\), and it does not assess every theorem in arXiv:2609.18967v1. It only disproves the stated dichotomy and the Form IV conclusion described above. The general conjugation construction is elementary and is not claimed to be new as an abstract operator-theoretic device. The full text of the 2019 corrigendum was not inspected here; its accessible abstract confirms an earlier omitted-case correction, so it remains possible that a closely related concrete construction already appears there. That possibility affects novelty of the mechanism, not the validity of the counterexample to the current v1 statement.

## References

1. H. Kumar, H. Kumar, A. Bin Abu Baker, *Structure of Generalized bi-circular idempotents and isometric reflections on C^1[0,1]*, arXiv:2609.18967v1.
2. A. B. Abubaker, F. Botelho, J. Jamison, *Representation of Generalized Bi-Circular Projections on Banach Spaces*, Acta Sci. Math. (Szeged) 80 (2014), 591--601; arXiv:1208.2012.
3. F. Botelho, T. Miura, *Corrigendum to “Examples of generalized bi-circular idempotents on spaces of continuously differentiable functions”*, J. Math. Anal. Appl. 474 (2019), 1481--1487, DOI: 10.1016/j.jmaa.2019.02.032.
