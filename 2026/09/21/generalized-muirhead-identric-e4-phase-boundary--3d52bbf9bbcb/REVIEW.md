# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS.

The proof was rederived from the definitions after the homogeneous normalization
\[
x=g e^{-z},\qquad y=g e^z.
\]
This gives exactly
\[
M/g=\cosh(dz)^{1/s},
\qquad
I/g=e^{z\coth z-1},
\]
with \(s=a+b\) and \(d=|a-b|\). In the \(E_4\) region the condition
\(2d^2-3s+1<0\) forces \(s>0\), so multiplying by \(s\) does not reverse
signs. Also \(ab=(s^2-d^2)/4<0\) is equivalent there to \(s<d\). These
checks give the exact cross-section
\[
\sqrt{2/5}<d<1,\qquad
(2d^2+1)/3<s<\min\{d,3d^2/2\}.
\]

The endpoint expansions were independently checked:
\[
R_d(z)=\frac{3d^2}{2}
+\frac{d^2(2-5d^2)}{20}z^2+O(z^4)
\]
at zero, and
\[
R_d(z)-d=
\frac{d-\log2+\log(1+e^{-2dz})-2dz/(e^{2z}-1)}
{z\coth z-1}
\]
at infinity. The first formula makes the upper endpoint penetrable for
\(d<2/3\); the second makes it penetrable for \(2/3\le d<\log2\).

The lower bound \(C(d)>L(d)\) does not come from numerics: setting
\(s=L(d)\) lands exactly on the already proved \(E_1\) boundary in the
2010 primary source, where the comparison is strict for every unequal pair.
Both compactified endpoint values are also strictly above \(L(d)\), so the
infimum has a uniform positive gap. At \(d=\sqrt{2/5}\) the same source
boundary gives strict positivity at every finite ratio while the diagonal
limit equals \(3/5\).

For \(d\ge\log2\), the proof uses only the sharp power-mean upper bound
\(I<P_{\log2}\), quoted explicitly as equation (1.8) in the 2010 primary
source, together with monotonicity of power means. This gives
\(R_d(z)>d\) at every finite \(z\) and \(C(d)=d\) from the limit at infinity.

Continuity of \(C\) follows after compactifying \(z\in(0,\infty)\); the
extended \(R_d\) is jointly continuous. Strict increase follows because
\(R_d\) is pointwise strictly increasing in \(d\), including both compactified
endpoints. The phase classification is then an immediate exact consequence
of
\[
\operatorname{sgn}\log(M/I)=\operatorname{sgn}(R_d-s).
\]

The explicit mixed-sign point
\[
(a,b)=\left(199/300,-1/300\right)
\]
was checked with exact rational arithmetic. At \(y/x=64\), a truncated
\(\operatorname{arctanh}\) series with a geometric tail bound proves
\[
\log(M/I)
<
-\frac{43568079809}{14910328125000}<0.
\]
The supplementary script reproduces this exact certificate and numerical
sanity checks, but no numerical computation is used as a substitute for the
general proof.

## Originality

PASS, to the best of our knowledge.

The primary source was inspected directly, including Theorem 1.1 and
Remark 3.1. Remark 3.1 defines the complementary \(E_4\) region by the
three inequalities used in the result and explicitly leaves that case as
an open problem.

Current-status searches used the exact paper title and DOI, the terms
“generalized Muirhead” and “identric mean,” the \(E_4\) label, the two
algebraic boundary expressions
\(3(a-b)^2-2(a+b)\) and \(2(a-b)^2-3(a+b)+1\), the transformed
hyperbolic ratio \(\log\cosh(dz)/(z\coth z-1)\), and combinations of the
source authors with later comparison-inequality literature. No located
source states the phase curve \(C(d)\), the complete \(d\ge\log2\) positive
subregion, or the lower-\(d\) split between global and mixed behavior.

Several nearby later sources were checked for coverage. Chu–Shi–Jiang
(2011) treats sharp inequalities involving the ordinary power mean,
arithmetic mean and identric mean. Zhao–Chu (2015) classifies the
two-parameter generalized Muirhead mean against the logarithmic mean; its
published abstract gives conditions in terms of its own \(\omega_1,\omega_2\).
On the present \(E_4\) region that result is consistent with \(M>L\), but
\(L<I\), so it does not decide the Muirhead–identric comparison. Later papers found in citation searches concern other named means or structural
Schur-convexity properties rather than the \(E_4\) identric comparison. A 2026
paper on an *invariant* Muirhead mean was also checked as a current-status
indicator; it studies a different mean construction and does not supply the
present identric comparison.

Residual risk remains. The 2010 article is reported by Springer as having
a small citation set, but web indexing did not expose every citing full text
in a uniform way. The Zhao–Chu 2015 publisher PDF was not retrievable during this review,
although its detailed bilingual abstract and theorem-region definitions were
accessible from indexed sources. A differently notated solution in an unindexed note, thesis, or
non-English source could therefore have been missed. This is a residual
originality risk, not evidence of prior coverage.

## Value

PASS.

The result supplies a sharp necessary-and-sufficient phase criterion for
the entire parameter region explicitly left untreated in the 2010 paper.
It identifies a simple large subregion, \(d\ge\log2\), where the global
inequality is always positive, proves that every lower-\(d\) cross-section
contains both a nonempty global-positive interval and a nonempty mixed-sign
interval, and gives a continuous strictly increasing separating curve with
controlled endpoints. The explicit interior mixed-sign example also shows
that the unresolved region is not uniform.

## Limitations

- The sharp phase boundary is variational; no elementary closed form for
  \(C(d)\) is proved on \((\sqrt{2/5},\log2)\).
- Uniqueness of the minimizing ratio is not established.
- The result does not alter the already classified \(E_1,E_2,E_3\) regions.
- Literature coverage is substantial but not exhaustive; originality is
  to the best of our knowledge.
- Independent audit has not been performed.
