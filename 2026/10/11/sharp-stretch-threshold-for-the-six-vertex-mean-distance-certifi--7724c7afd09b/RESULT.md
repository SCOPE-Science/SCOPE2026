# Sharp stretch threshold for the six-vertex mean-distance certificate

## Finding
For
\[
K_{{L,\\varepsilon}}=\\{{(Lt,x,y):0\\le t\\le1,\\ |x|\\le t,\\ |y|\\le \\varepsilon(1-2t/3)\\}}\\subset\\mathbb R^3,
\]
let \(\\Delta(K)\) be the expected distance between two independent volume-uniform points and \(\\theta(K)\) the expected distance between two independent surface-uniform boundary points. Shen's exact axial calculation gives the volume-coordinate Gini mean difference
\[
\\mathcal D_{{\rm vol}}=\\frac{{246}}{{875}}.
\]
Write \(g_{{L,\\varepsilon}}\) for the exact Gini mean difference of the boundary axial coordinate and
\[
U(L,\\varepsilon)=g_{{L,\\varepsilon}}+\\frac{{2\\sqrt{{1+\\varepsilon^2}}}}L.
\]
The source's projection-diameter lemma gives
\[
\\frac{{\\Delta(K_{{L,\\varepsilon}})}}L\\ge\\frac{{246}}{{875}},
\\qquad
\\frac{{\\theta(K_{{L,\\varepsilon}})}}L\\le U(L,\\varepsilon).
\]
The sharp threshold for this certificate is
\[
\\inf_{{\\varepsilon>0}}U(L,\\varepsilon)=\\frac4{{15}}+\\frac2L,
\]
with unattained infimum. Therefore there exists \(\\varepsilon>0\) for which these two bounds alone prove \(\\Delta(K_{{L,\\varepsilon}})>\\theta(K_{{L,\\varepsilon}})\) if and only if
\[
L>\\frac{{2625}}{{19}}=138.157894\\ldots.
\]
In particular, the published numerical stretch \(L=1000\) is far from necessary for its own elementary certificate: every stretch strictly above \(2625/19\) works with sufficiently small positive \(\\varepsilon\).

## Assumptions and scope
Here \(L>0\) and \(\\varepsilon>0\), so \(K_{{L,\\varepsilon}}\) is a full-dimensional six-vertex convex polytope. The claim uses exactly the axial Gini formulas and the projection-versus-transverse-diameter estimate from the cited source. It determines the sharp \(L\)-threshold for that proof certificate. It does not determine the smallest \(L\) for which the actual inequality \(\\Delta(K_{{L,\\varepsilon}})>\\theta(K_{{L,\\varepsilon}})\) holds somewhere in this family.

## Proof
Put
\[
S=\\sqrt{{L^2+1}},\\qquad
 a=\\varepsilon S,
\]
\[
 b=\\sqrt{{L^2+\\frac{4\\varepsilon^2}{9}}}-\\frac{{2\\varepsilon S}}3,
\\qquad
D=a+\\frac b2+\\frac{\\varepsilon}3,
\]
and
\[
\\alpha=\\frac aD,\\qquad \\beta=\\frac b{{2D}}.
\]
Shen's exact boundary computation gives
\[
g_{{L,\\varepsilon}}
=\\alpha+\\frac{2\\beta}{3}-\\frac{2\\alpha^2}{3}
-\\alpha\\beta-\\frac{2\\beta^2}{5}.
\]
The terminal-face atom has mass \(\\gamma=\\varepsilon/(3D)\). Hence
\[
\\alpha+\\beta+\\gamma=1,
\\qquad
\\gamma=\\frac{\\alpha}{3S},
\]
so
\[
\\beta=1-\\alpha\\left(1+\\frac1{{3S}}\\right).
\]
Substitution and collection give the exact identity
\[
g_{{L,\\varepsilon}}-\\frac4{{15}}
=\\frac{\\alpha}{45S^2}
\\left(6S^2+2S-\\alpha(3S^2-3S+2)\\right).
\]
Also
\[
D=\\frac{2\\varepsilon S}{3}+\\frac{\\varepsilon}{3}
+\\frac12\\sqrt{{L^2+\\frac{4\\varepsilon^2}{9}}}
>\\frac{\\varepsilon(2S+1)}3,
\]
therefore
\[
0<\\alpha<\\frac{{3S}}{{2S+1}}<\\frac32.
\]
Since \(S>1\),
\[
6S^2+2S-\\alpha(3S^2-3S+2)
>
6S^2+2S-\\frac32(3S^2-3S+2)
=\\frac{3S^2+13S-6}{2}>0.
\]
Thus \(g_{{L,\\varepsilon}}>4/15\) for every positive \(\\varepsilon\). Consequently
\[
U(L,\\varepsilon)>\\frac4{{15}}+\\frac2L.
\]
On the other hand, as \(\\varepsilon\\downarrow0\), one has \(\\alpha\\to0\), \(\\beta\\to1\), hence \(g_{{L,\\varepsilon}}\\to4/15\), while \(2\\sqrt{{1+\\varepsilon^2}}/L\\to2/L\). This proves the stated unattained infimum.

Finally,
\[
\\frac{{246}}{{875}}-\\frac4{{15}}=\\frac{{38}}{{2625}}.
\]
Therefore
\[
\\frac4{{15}}+\\frac2L<\\frac{{246}}{{875}}
\]
holds exactly when \(L>2625/19\). If this strict inequality holds, continuity supplies all sufficiently small positive \(\\varepsilon\) with \(U(L,\\varepsilon)<246/875\), and the source's two one-sided estimates prove \(\\Delta>\\theta\). If \(L\\le2625/19\), the strict lower bound on \(U\) rules out certification by the same two estimates for every positive \(\\varepsilon\).

## Verification
The included `verify.py` checks the rational polynomial identity after the substitution for \(\\beta\), verifies the exact threshold arithmetic
\[
\\frac{{246}}{{875}}-\\frac4{{15}}=\\frac{{38}}{{2625}},
\\qquad
\\frac2{{38/2625}}=\\frac{{2625}}{{19}},
\]
and checks the positivity reduction at \(\\alpha=3/2\). These computations are consistency checks; the universal result is the analytic argument above.

## Relationship to prior work
Shen's preprint gives the family \(K_{{L,\\varepsilon}}\), computes the exact interior axial Gini value \(246/875\), derives the exact boundary axial law \(g_{{L,\\varepsilon}}\), and exhibits the numerical choice \(L=1000\), \(\\varepsilon=1/100\). It also proves that every \(0<\\varepsilon<\\varepsilon_*\) yields counterexamples for all sufficiently large \(L\), but it does not give a finite sharp stretch threshold for its projection-diameter certificate. The argument here keeps the source's same two one-sided distance bounds and determines exactly when they can succeed.

Lotnikov independently constructs a different centrally symmetric three-dimensional family using a monotone section-area/perimeter ratio and anisotropic stretching. That broader construction proves existence for sufficiently large stretch but does not analyze Shen's six-vertex family or imply the constant \(2625/19\).

## Limitations
The constant \(2625/19\) is not claimed to be the true geometric threshold for the family. It is the exact threshold for the certificate consisting of the axial lower bound on \(\\Delta/L\) and the axial-plus-transverse-diameter upper bound on \(\\theta/L\). A direct evaluation or sharper estimate of the full Euclidean mean distances could potentially yield counterexamples at smaller \(L\).

## References
1. Eric Shen, *The Zaporozhets--Tarasov Conjecture on Mean Distances*, arXiv:2608.06470, first submitted 2026-08-06; relevant material: Section 4, especially Lemma 4.1, Example 4.2/Theorem 4.3, and the asymptotic criterion following the example.
2. A. S. Lotnikov, *Mean distance between points inside and on the boundary of a convex body*, arXiv:2608.14848, 2026; relevant material: Sections 8.1--8.2 and the author note distinguishing the independent construction from Shen's.
