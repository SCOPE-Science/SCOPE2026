# Sharp second-order Gram stability for the planar three-vector signed-sum extremizer

## Finding
For three unit vectors \(u_1,u_2,u_3\in\\mathbb R^2\), put
\[
M(u_1,u_2,u_3)=\\max_{\\varepsilon_i\\in\\{-1,1\\}}\\left\\|\\sum_{i=1}^3\\varepsilon_i u_i\\right\\|^2.
\]
Measure distance from the centered equilateral equality class by the sign-invariant Gram defect
\[
\\Delta_*=\\min_{\\sigma_i\\in\\{-1,1\\}}
\\left(\\sum_{1\\le i<j\\le3}
\\left(\\langle\\sigma_i u_i,\\sigma_j u_j\\rangle+\\frac12\\right)^2\\right)^{1/2}.
\]
There are constants \(\\delta_0>0\) and \(C<\\infty\) such that whenever \(0<\\Delta_*<\\delta_0\),
\[
M\\ge 4+\\sqrt{\\frac83}\\,\\Delta_*-\\frac29\\Delta_*^2-C\\Delta_*^3.
\]
The two displayed coefficients are jointly sharp. For
\[
u_1=(1,0),\\qquad
u_2=(\\cos\\theta,\\sin\\theta),\\qquad
u_3=(\\cos\\theta,-\\sin\\theta),\\qquad
\\theta=\\frac{2\\pi}3-\\eta,
\]
with \(\\eta\\downarrow0\),
\[
M=4+\\sqrt{\\frac83}\\,\\Delta_*-\\frac29\\Delta_*^2+O(\\Delta_*^3).
\]
Equivalently,
\[
\\max_{\\varepsilon_i=\\pm1}\\left\\|\\sum_i\\varepsilon_i u_i\\right\\|
\\ge 2+\\frac{\\Delta_*}{\\sqrt6}-\\frac7{72}\\Delta_*^2+O(\\Delta_*^3),
\]
with the same sharp first two coefficients in the local lower envelope.

## Assumptions and scope
The statement is local around the planar equality class and uses only Euclidean unit vectors. The minimum over independent sign changes makes \(\\Delta_*\) invariant under exactly the sign symmetry of the signed-sum objective. The result is not a global stability inequality away from the equilateral class, and it does not assert a dimension-greater-than-two analogue.

## Proof
Choose signs realizing \(\\Delta_*\). For sufficiently small \(\\Delta_*\), write
\[
a=\\langle u_1,u_2\\rangle=-\\frac12+x,\\quad
b=\\langle u_1,u_3\\rangle=-\\frac12+y,\\quad
c=\\langle u_2,u_3\\rangle=-\\frac12+z,
\]
with
\[
s=x+y+z,\\qquad \\Delta^2=x^2+y^2+z^2=\\Delta_*^2.
\]
Because three vectors lie in \(\\mathbb R^2\), their Gram determinant vanishes. Expanding that determinant gives the exact identity
\[
3s=\\Delta^2+s^2-4xyz. \\tag{1}
\]
Initially \(|s|\\le\\sqrt3\\,\\Delta\). Substitution into (1), together with \(|xyz|\\le\\Delta^3/(3\\sqrt3)\), first yields \(s=O(\\Delta^2)\) and then
\[
s=\\frac13\\Delta^2+O(\\Delta^3). \\tag{2}
\]

The four squared signed-sum values, modulo global sign, are
\[
3+2(a+b+c),\\quad 3+2(a-b-c),\\quad 3+2(-a+b-c),\\quad 3+2(-a-b+c).
\]
Near the equilateral point the first is close to zero and the other three are close to four. Hence, with \(m=\\max\\{x,y,z\\}\),
\[
M=4+4m-2s. \\tag{3}
\]
Put \(q_i=x_i-s/3\), where \((x_1,x_2,x_3)=(x,y,z)\). Then \(q_1+q_2+q_3=0\), so the sharp elementary inequality
\[
\\max_i q_i\\ge\\frac1{\\sqrt6}\\left(\\sum_i q_i^2\\right)^{1/2}
\]
holds; equality occurs when two coordinates are equal and positive and the third is their negative double. Therefore
\[
m\\ge\\frac{s}{3}+\\frac1{\\sqrt6}\\sqrt{\\Delta^2-\\frac{s^2}{3}.
\]
Using (2) in (3) gives, uniformly,
\[
M-4\\ge\\sqrt{\\frac83}\\,\\Delta-\\frac29\\Delta^2+O(\\Delta^3),
\]
which has the stated rigorous one-sided interpretation after shrinking the neighborhood.

For sharpness, take the symmetric family in the finding. Then
\[
x=y=\\cos\\theta+\\frac12,\\qquad z=\\cos(2\\theta)+\\frac12,
\]
and the two equal coordinates are the active maxima in (3). Direct Taylor expansion gives
\[
\\Delta^2=\\frac92\\eta^2-\\frac{3\\sqrt3}2\\eta^3-\\frac{27}8\\eta^4+O(\\eta^5),
\]
while
\[
M-4=-2z=2\\sqrt3\\,\\eta-2\\eta^2-\\frac{4\\sqrt3}3\\eta^3+O(\\eta^4).
\]
Eliminating \(\\eta\) yields
\[
M-4=\\sqrt{\\frac83}\\,\\Delta-\\frac29\\Delta^2+O(\\Delta^3),
\]
so neither the leading coefficient nor, after fixing it, the quadratic coefficient can be improved uniformly.

## Verification
The algebraic certificate `verify.py` checks the exact Gram-determinant identity, the four signed-sum formulas after the equilateral shift, and the sharp family Taylor identity through quadratic order in \(\\Delta_*\). Its finite symbolic checks support the displayed algebra; the uniform asymptotic conclusion itself is proved analytically above from the exact determinant identity and the sharp zero-sum three-coordinate inequality.

## Relationship to prior work
Pinasco proves that for \(d+1\) Euclidean unit vectors in \(\\mathbb R^d\), the smallest possible longest signed sum is \(\\sqrt{d+2}\), and classifies equality. In \(d=2\) this gives the minimum value \(2\) and the centered equilateral equality class. Grundbacher independently gives the sharp planar signed-sum bound for arbitrary numbers of vectors through a polygonal circumradius argument. The inspected statements and proofs establish the extremal value and equality configurations, but do not give the local deficit-versus-Gram-defect expansion above. Joós and Lángi develop related zonotope isoperimetry and cite general geometric stability literature; their results do not state this three-vector Gram-metric coefficient pair.

## Limitations
This is a local quantitative refinement, not a global estimate in \(\\Delta_*\). No claim is made that Gram distance is the only natural stability metric. The literature comparison cannot exclude an unindexed stability theorem formulated in a different metric that, after a nontrivial conversion, might reproduce these exact coefficients; this remains the main originality risk.

## References
1. D. Pinasco, *Large signed sums of unit vectors: the first linearly dependent case*, arXiv:2609.21101v1, 2026.
2. F. Grundbacher, *A Sharp Bound on Large Planar Signed Vector Sums*, arXiv:2502.13752v1, 2025; later expanded under the title *Large Signed Sums and the Polarization Constant of Convex Bodies*.
3. A. Joós and Z. Lángi, *Isoperimetric problems for zonotopes*, Mathematika 69 (2023), 508–534, DOI 10.1112/mtk.12191.
