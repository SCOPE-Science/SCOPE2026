# Strict uniform half-mass gap above the mean for \(F\) distributions
## Finding
For every real \(\kappa>1\), if \(X_{d_1,d_2}\) has the central \(F\) distribution with integer \(d_1\ge1\) and integer \(d_2\ge3\), then
\[
\inf_{d_1\ge1,\ d_2\ge3} \Pr\!\left\{X_{d_1,d_2}\le \kappa\,\mathbb E X_{d_1,d_2}\right\}>\frac12.
\]
This proves the strict-infimum conjecture stated in Remark 2.4 of Zhou, Lu, and Hu.

## Assumptions and scope
Only the central \(F\) family is considered. The numerator and denominator degrees of freedom are integers with \(d_1\ge1\) and \(d_2>2\), so the expectation exists. Fix \(\kappa>1\). Put
\[
a=\frac{d_1}2,\qquad b=\frac{d_2}2,
\qquad q_\kappa(a,b)=\frac{\kappa a}{\kappa a+b-1}.
\]
The usual beta representation of the \(F\) distribution gives
\[
P_\kappa(a,b):=\Pr\!\left\{X_{d_1,d_2}\le\kappa\,\mathbb E X_{d_1,d_2}\right\}
=I_{q_\kappa(a,b)}(a,b).
\]
Here \(a\) ranges over the positive half-integers and \(b\) over the half-integers at least \(3/2\). The published theorem used below is the pointwise statement \(P_1(a,b)>1/2\) on this lattice.

## Proof
Let \(U_{a,b}\sim\operatorname{Beta}(a,b)\). Then \(P_\kappa(a,b)=\Pr\{U_{a,b}\le q_\kappa(a,b)\}\). Since \(q_\kappa(a,b)\) is strictly increasing in \(\kappa\), the published \(\kappa=1\) theorem implies \(P_\kappa(a,b)>1/2\) at every finite lattice point. It remains to rule out a sequence of lattice points whose probabilities decrease to \(1/2\).

Assume for contradiction that the infimum is \(1/2\), and choose \((a_n,b_n)\) with \(P_\kappa(a_n,b_n)\to1/2\). Because both parameter sets are discrete, after passing to subsequences each coordinate is either constant or tends to infinity. There are four cases.

If both coordinates are constant, the limit is a single finite value, already strictly larger than \(1/2\), a contradiction.

Suppose \(a_n=a\) is fixed and \(b_n\to\infty\). The beta-to-gamma boundary limit gives
\[
b_n U_{a,b_n}\Rightarrow G_a,\qquad G_a\sim\operatorname{Gamma}(a,1),
\]
while
\[
b_n q_\kappa(a,b_n)\longrightarrow\kappa a.
\]
Hence
\[
P_\kappa(a,b_n)\longrightarrow \Pr\{G_a\le\kappa a\}.
\]
At \(\kappa=1\), the same limit together with \(P_1(a,b_n)>1/2\) shows \(\Pr\{G_a\le a\}\ge1/2\). The gamma density is positive on \((0,\infty)\), so \(\kappa a>a\) implies
\[
\Pr\{G_a\le\kappa a\}>\Pr\{G_a\le a\}\ge\frac12.
\]
Thus this case cannot have limit \(1/2\).

Suppose instead that \(b_n=b\) is fixed and \(a_n\to\infty\). By beta symmetry and the same boundary limit,
\[
a_n(1-U_{a_n,b})\Rightarrow G_b,\qquad G_b\sim\operatorname{Gamma}(b,1),
\]
and
\[
a_n(1-q_\kappa(a_n,b))\longrightarrow\frac{b-1}{\kappa}.
\]
Therefore
\[
P_\kappa(a_n,b)\longrightarrow \Pr\!\left\{G_b\ge\frac{b-1}{\kappa}\right\}.
\]
At \(\kappa=1\), the corresponding limit is at least \(1/2\). Since \((b-1)/\kappa<b-1\) and the gamma density is positive, the displayed tail probability is strictly larger than its \(\kappa=1\) limit and hence strictly larger than \(1/2\).

Finally suppose \(a_n\to\infty\) and \(b_n\to\infty\). For \(U=U_{a,b}\),
\[
\mu=\mathbb E U=\frac{a}{a+b},\qquad
\operatorname{Var}(U)=\frac{ab}{(a+b)^2(a+b+1)},
\]
and direct algebra gives
\[
q_\kappa(a,b)-\mu
=\frac{a((\kappa-1)b+1)}{(a+b)(\kappa a+b-1)}.
\]
Consequently
\[
\frac{(q_\kappa-\mu)^2}{\operatorname{Var}(U)}
=\frac{a((\kappa-1)b+1)^2(a+b+1)}{b(\kappa a+b-1)^2}
\ge \frac{(\kappa-1)^2}{\kappa^2}\frac{ab}{a+b}
\ge \frac{(\kappa-1)^2}{2\kappa^2}\min(a,b).
\]
The last quantity tends to infinity. Chebyshev's inequality therefore gives
\[
\Pr\{U>q_\kappa(a,b)\}
\le\frac{\operatorname{Var}(U)}{(q_\kappa(a,b)-\mu)^2}\longrightarrow0,
\]
so \(P_\kappa(a_n,b_n)\to1\), again impossible.

Every subsequential escape pattern is excluded. Hence no sequence can approach \(1/2\), and the infimum is strictly greater than \(1/2\).

For completeness, the beta-to-gamma limit used above follows directly by rescaling the beta density: for fixed \(a>0\), the density of \(bU_{a,b}\) converges pointwise to \(y^{a-1}e^{-y}/\Gamma(a)\). Because the limiting density integrates to one, Scheffé's lemma upgrades this to total-variation convergence; the reflected statement follows by exchanging the beta parameters. The thresholds converge to continuity points of the gamma law.

## Verification
The proof is analytic and does not infer an infinite statement from a finite experiment. The bundled `verify.py` checks with exact rational arithmetic the algebraic identity for \(q_\kappa-\mu\), the three lower bounds used in the Chebyshev step, monotonicity of the threshold in \(\kappa\), and the two boundary-threshold identities on a representative grid. Running `python3 verify.py` returns `VERIFY_OK`. These checks are safeguards for algebra only; the compactness and weak-convergence argument above is the proof.

The only non-elementary published premise is the strict finite-parameter inequality at \(\kappa=1\), stated in Theorem 1.1 of the lead source and proved there in Section 2.1. The new argument does not assume the conjectured uniform gap.

## Relationship to prior work
Zhou, Lu, and Hu prove that the infimum equals \(1/2\) at \(\kappa=1\), that every finite parameter pair has probability strictly above \(1/2\) for \(\kappa\ge1\), and only the non-strict uniform bound for \(\kappa>1\). Their Remark 2.4 explicitly conjectures the strict uniform inequality proved here and states that they do not have a proof. Their numerical table samples finite parameter ranges but cannot rule out an escaping sequence; the argument above does exactly that by classifying all parameter-boundary regimes.

The Gamma-family infimum theorem of Sun, Hu, and Sun is related background but concerns a one-shape-family limit problem rather than this two-parameter \(F\)-distribution lattice. It does not imply the four-regime compactness argument or the strict \(F\)-infimum statement.

## Limitations
The result is qualitative: for each fixed \(\kappa>1\) it proves existence of a positive gap above \(1/2\) but does not give the sharp gap, identify the minimizing pair, or determine how the gap behaves as \(\kappa\downarrow1\). It applies to the integer-degree central \(F\) family used in the source; no claim is made for arbitrary real degrees of freedom or for noncentral \(F\) laws.

## References
1. Q. Zhou, P. Lu, and Z.-C. Hu, “A study on the \(F\)-distribution motivated by Chvátal's theorem,” arXiv:2409.09420v1, first public 2024-09-14. See Theorem 1.1, Section 2, and Remark 2.4.
2. P. Sun, Z.-C. Hu, and W. Sun, “The infimum values of two probability functions for the Gamma distribution,” Journal of Inequalities and Applications 2024:5, DOI 10.1186/s13660-024-03081-w.
