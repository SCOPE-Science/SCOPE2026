# The liver-free fixed point is a source throughout the positive boundary-equilibrium regime
## Finding
For the discrete hepatitis-C map of Khan, Yaqoob, and Alsaadi, let the liver-free fixed point be \\(L=(0,0)\\). In the parameter regime \\(0<g<1\\), \\(0<\\zeta<1\\), and \\(h>0\\), which is precisely the regime in which the source separately allows the disease-free state \\((1-g,0)\\) and the total-infection state \\((0,1-\\zeta)\\) to be nonnegative, \\(L\\) is a hyperbolic source for every positive step size.

The source instead states that \\(L\\) is a sink whenever
\[
h>\\max\\left\\{\\frac{2}{g-1},\\frac{2}{\\zeta-1}\\right\\}.
\]
Because both denominators are negative in the stated regime, this printed inequality is automatically true for every \\(h>0\\). Thus the printed sink label is opposite to the local dynamics forced by the source's own Jacobian.

## Assumptions and scope
The claim concerns only the liver-free fixed point of the published two-dimensional map (1.6), with \\(0<g<1\\), \\(0<\\zeta<1\\), and \\(h>0\\). No condition on \\(b\\) or \\(\\alpha\\) is needed because those parameters drop out of the Jacobian at \\(L\\).

A hyperbolic source means that both eigenvalues of the Jacobian have modulus strictly greater than one. The statement is local. It does not assert global divergence of all biologically admissible trajectories, and it does not alter the source's separate calculations at the partial-infection fixed point.

## Proof
The source gives the Jacobian at \\(L\\) as
\[
J_L=\\begin{pmatrix}
1+h-gh&0\\\\
0&1+h-h\\zeta
\\end{pmatrix},
\]
so its two multipliers are
\[
\\lambda_1=1+h(1-g),\\qquad \\lambda_2=1+h(1-\\zeta).
\]
If \\(0<g<1\\) and \\(h>0\\), then \\(h(1-g)>0\\), hence \\(\\lambda_1>1\\). Likewise, \\(0<\\zeta<1\\) gives \\(h(1-\\zeta)>0\\), hence \\(\\lambda_2>1\\). Therefore \\( |\\lambda_1|>1\\) and \\( |\\lambda_2|>1\\), so \\(L\\) is a hyperbolic source.

For comparison with the printed classification, \\(g-1<0\\) and \\(\\zeta-1<0\\), hence
\[
\\frac{2}{g-1}<0,\\qquad \\frac{2}{\\zeta-1}<0.
\]
Every \\(h>0\\) therefore satisfies the source's displayed sink inequality. The algebraic source/sink conclusion and that displayed inequality cannot both be correct on this domain; the eigenvalue test fixes the direction unambiguously.

As an exact witness, take \\(g=1/2\\), \\(\\zeta=1/3\\), and \\(h=1\\). Then
\[
(\\lambda_1,\\lambda_2)=\\left(\\frac32,\\frac53\\right),
\]
whereas the source's two printed threshold values are \\(-4\\) and \\(-3\\). Thus the printed sink condition is satisfied even though both multipliers lie strictly outside the unit disk.

## Verification
The source's displayed map, fixed-point conditions, Jacobian, multipliers, and source/sink classification were read directly from the article. The bundled `verify.py` evaluates the exact rational witness and confirms that the printed sink inequality holds while both multiplier moduli exceed one.

The universal part of the result is not based on numerical sampling: it is the direct sign argument \\(1-g>0\\) and \\(1-\\zeta>0\\) applied to the exact multiplier formulas.

## Relationship to prior work
The motivating article explicitly prints both the correct diagonal Jacobian and the incompatible sink condition. Searches by title, DOI, fixed-point name, multiplier formulas, and equivalent source/sink wording did not locate a published correction of this specific liver-free classification.

A 2024 paper by Khan and Younis and a 2025 follow-up by Khan, Younis, and Alsulami also study two-dimensional discrete HCV models, but the accessible materials describe different model formulations and parameterizations; they do not provide an implication that resolves this source-specific contradiction. A published-findings database search likewise returned only results on unrelated discrete or biological systems.

## Limitations
This finding corrects the local topological type of the liver-free fixed point only on \\(0<g<1\\), \\(0<\\zeta<1\\), \\(h>0\\). It does not classify every possible sign regime for \\(g\\) and \\(\\zeta\\), does not establish a global basin statement, and does not assess the partial-infection Neimark-Sacker calculation. The full text of one later related HCV article was not openly available in the inspected source, so comparison with that article is limited to its abstract and exposed first-page/figure material; no decisive covering implication was found there.

## References
1. A. Q. Khan, A. Yaqoob, and A. Alsaadi, “Neimark-Sacker bifurcation, chaos, and local stability of a discrete Hepatitis C virus model,” *AIMS Mathematics* 9 (2024), 31985–32013. DOI: 10.3934/math.20241537.
2. A. Q. Khan and S. Younis, “Chaos and bifurcations of a two-dimensional hepatitis C virus model with hepatocyte homeostasis,” *Chaos* 34 (2024), 063113. DOI: 10.1063/5.0203886.
3. A. Q. Khan, S. Younis, and I. M. Alsulami, “Two-Dimensional Hepatitis C Virus Model With Chaos, Stability, and Bifurcations,” *Mathematical Methods in the Applied Sciences* 48 (2025), 13325–13343. DOI: 10.1002/mma.11105.
