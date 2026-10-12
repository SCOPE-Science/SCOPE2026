# Self-review

## Correctness
PASS. The primary source equations for the nontranslation-invariant \(k=3\) branch give
\[
\lambda xy(x+y)=1,\qquad x^2+y^2+xy=x+y.
\]
With \(a=x+y\), these imply \(xy=a(a-1)\) and \(\lambda=1/[a^2(a-1)]\). Substitution into the source formulas for the two-step Markov eigenvalue and \(\kappa\) gives the exact identity
\[
s_2=\kappa=(a-1)^2.
\]
The independent hard-core estimate \(\gamma\le\lambda/(1+\lambda)\) then yields an increasing certificate
\[
F(t)=\frac{9t^2}{1+t(1+t)^2},\qquad 0<t<\frac13,
\]
whose sharp supremum is \(27/43<1\). The proof uses exact algebra; finite replay is only corroborative.

## Originality
PASS. The primary paper proves extremality but, for the order-three branch, retains a Cardano representation and uses computer plots to justify monotonicity of the reconstruction inequalities. Full-text comparison found no statement of \(s_2=\kappa=(a-1)^2\) or the uniform \(27/43\) certificate. The general Martinelli--Sinclair--Weitz theorem supplies only the model-wide bound on \(\gamma\), not the branch-specific collapse. A related broader countable-state boundary-law parameterization does not imply the exact Markov/reconstruction identities without additional analysis.

Residual risk: an equivalent algebraic simplification could exist in weakly indexed notes or under different variables. Searches for the source identifier, exact eigenvalue form, constant \(27/43\), periodic hard-core reconstruction aliases, and implication-equivalent statements did not locate such a result.

## Value
PASS. The quantity \(\kappa\gamma\) is exactly the reconstruction parameter used to establish extremality of the periodic phases. Replacing a graphical monotonicity step by a closed branch coordinate, an exact second eigenvalue, and a uniform margin \(1-27/43=16/43\) provides structural information about how far the entire periodic branch lies inside this sufficient extremality regime.

## Closest literature and limitations
The closest source is Rozikov--Khakimov--Makhammadaliev, arXiv:2111.11163v1 / DOI:10.22363/2413-3639-2022-68-1-95-109. The general disagreement estimate comes from Martinelli--Sinclair--Weitz, DOI:10.1002/rsa.20132. The claim is not extended beyond order \(3\), and no optimality statement is made for general reconstruction thresholds.

Self-review: passed. Independent audit: not yet performed.
