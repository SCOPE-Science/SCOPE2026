# The resistant-phage reproduction number in a CRISPR chemostat is missing an adsorption factor

## Finding

In the CRISPR/Cas chemostat model of Shu, Fu, and Wang, the displayed basic reproduction number for the resistant-bacteria/phage subsystem omits one factor of the adsorption rate \(k\).

The model contains successful infection of resistant bacteria at rate
\[
k'MP=\kappa kMP,
\]
while free phage are removed by adsorption at rate
\[
kMP.
\]
At the phage-free resistant equilibrium
\[
E_2=(\lambda_2,0,R^0-\lambda_2,0,0),
\qquad
\lambda_2=\frac{Da}{\mu m-D},
\]
put
\[
M_2=R^0-\lambda_2.
\]
The infected-cell/phage linearization on \((I,P)\) has the new-infection and transition matrices
\[
F=
\begin{pmatrix}
0&\kappa kM_2\\
0&0
\end{pmatrix},
\qquad
V=
\begin{pmatrix}
D+\delta&0\\
-b\delta&D+kM_2
\end{pmatrix}.
\]
Consequently
\[
\widehat{\mathcal R}_0^M
=
\rho(FV^{-1})
=
\sqrt{
\frac{b\delta\kappa kM_2}
{(D+\delta)(D+kM_2)}
}.
\]
The source instead displays
\[
\mathcal R_{0,\mathrm{print}}^M
=
\sqrt{
\frac{b\delta\kappa M_2}
{(D+\delta)(D+kM_2)}
},
\]
with the numerator missing \(k\).

The source's later equilibrium algebra reveals the same correction internally. It defines
\[
A_2=\frac{b\delta\kappa}{D+\delta}-1
\]
and uses
\[
G(\lambda_2)
=
-D+kA_2M_2
=
(D+kM_2)\bigl((\mathcal R_0^M)^2-1\bigr).
\]
Expanding the left side gives
\[
-D-kM_2+\frac{b\delta\kappa kM_2}{D+\delta},
\]
which equals the right side exactly when \(\mathcal R_0^M\) is replaced by \(\widehat{\mathcal R}_0^M\). With the printed definition, the identity fails for general \(k\).

The distinction changes the literal threshold classification. Consider
\[
D=\delta=1,\qquad
b=10,\qquad
k=\frac1{100},\qquad
\kappa=\frac12,
\]
\[
\mu=\frac12,\qquad
m=4,\qquad
a=1,\qquad
R^0=11,\qquad
\epsilon=\frac12.
\]
For the Monod growth law
\[
f(R)=\frac{mR}{a+R},
\]
the resistant break-even nutrient concentration is
\[
\lambda_2
=
\frac{Da}{\mu m-D}
=
1,
\]
so
\[
M_2=10.
\]
The source's displayed formula gives
\[
(\mathcal R_{0,\mathrm{print}}^M)^2
=
\frac{250}{11}>1,
\]
whereas the corrected next-generation number gives
\[
(\widehat{\mathcal R}_0^M)^2
=
\frac5{22}<1.
\]

Directly, the resistant-phage invasion block is
\[
J_{IP}
=
\begin{pmatrix}
-(D+\delta)&\kappa kM_2\\
b\delta&-(D+kM_2)
\end{pmatrix}
=
\begin{pmatrix}
-2&\frac1{20}\\
10&-\frac{11}{10}
\end{pmatrix}.
\]
Its trace is
\[
-\frac{31}{10}<0
\]
and its determinant is
\[
\frac{17}{10}>0.
\]
Thus both eigenvalues have negative real part and small phage perturbations decay at \(E_2\), despite the printed value exceeding one.

The discrepancy also invalidates the positive-equilibrium implication if the displayed threshold is read literally. The source's resistant-phage equilibrium equations require
\[
kA_2M_3=D.
\]
For the chosen parameters,
\[
A_2
=
\frac{b\delta\kappa}{D+\delta}-1
=
\frac32,
\]
hence
\[
M_3=\frac{D}{kA_2}=\frac{200}{3}.
\]
But positivity of the same equilibrium requires
\[
\mu f(R_3)>D,
\]
so
\[
R_3>\lambda_2=1.
\]
Its nutrient balance gives
\[
M_3
=
\frac{D(R^0-R_3)}{\mu f(R_3)}
<
R^0-R_3
<
10,
\]
contradicting
\[
M_3=\frac{200}{3}.
\]
Therefore no positive resistant-phage equilibrium of the source's stated form exists for this parameter choice, although its displayed \(\mathcal R_0^M\) is greater than one.

## Assumptions and scope

The calculation concerns the exact chemostat model printed in the source, with
\[
k'=\kappa k,\qquad
0<\kappa\le1,\qquad
0<\mu<1,
\]
and Monod growth
\[
f(R)=\frac{mR}{a+R}.
\]

The counterexample uses strictly positive parameters and satisfies the source's resistant-bacteria existence assumptions:
\[
\mu m>D
\]
and
\[
\mu f(R^0)>D.
\]
Indeed,
\[
\mu m=2>1=D,
\qquad
\mu f(11)=\frac{11}{6}>1.
\]

The claim is deliberately source-specific. It does not claim that every later calculation in the article uses the erroneous formula. In fact, the source's later \(G(\lambda_2)\) identity and its ratio formulas are algebraically consistent with the corrected threshold, which is evidence that the omission may be a displayed-formula defect rather than an error propagated through every computation.

## Proof

At \(E_2\), the susceptible-bacteria coordinate is zero and the resistant-bacteria coordinate is \(M_2\). To first order, the infected-cell and phage equations are
\[
\dot I
=
-(D+\delta)I+\kappa kM_2P,
\]
\[
\dot P
=
b\delta I-(D+kM_2)P.
\]
A standard new-infection/transition split is therefore
\[
F=
\begin{pmatrix}
0&\kappa kM_2\\
0&0
\end{pmatrix},
\]
\[
V=
\begin{pmatrix}
D+\delta&0\\
-b\delta&D+kM_2
\end{pmatrix}.
\]
Since
\[
V^{-1}
=
\begin{pmatrix}
\frac1{D+\delta}&0\\[4pt]
\frac{b\delta}{(D+\delta)(D+kM_2)}
&
\frac1{D+kM_2}
\end{pmatrix},
\]
the matrix \(FV^{-1}\) has nonzero eigenvalue
\[
\frac{b\delta\kappa kM_2}{(D+\delta)(D+kM_2)}.
\]
The conventional two-stage reproduction number used by the source is its square root, yielding
\[
\widehat{\mathcal R}_0^M
=
\sqrt{
\frac{b\delta\kappa kM_2}
{(D+\delta)(D+kM_2)}
}.
\]

The same correction follows without any next-generation convention by comparing the source's own formulas. With
\[
A_2=\frac{b\delta\kappa}{D+\delta}-1,
\]
one has
\[
-D+kA_2M_2
=
-D-kM_2+\frac{b\delta\kappa kM_2}{D+\delta}.
\]
On the other hand,
\[
(D+kM_2)
\left(
\frac{b\delta\kappa kM_2}{(D+\delta)(D+kM_2)}
-1
\right)
\]
is exactly the same expression. Dropping \(k\) from the numerator destroys the identity.

For the exact witness,
\[
M_2=10,
\qquad
D+kM_2=\frac{11}{10}.
\]
Hence
\[
(\mathcal R_{0,\mathrm{print}}^M)^2
=
\frac{10\cdot1\cdot(1/2)\cdot10}
{2\cdot(11/10)}
=
\frac{250}{11},
\]
while
\[
(\widehat{\mathcal R}_0^M)^2
=
\frac{10\cdot1\cdot(1/2)\cdot(1/100)\cdot10}
{2\cdot(11/10)}
=
\frac5{22}.
\]

The direct invasion matrix has
\[
\operatorname{tr}J_{IP}
=
-2-\frac{11}{10}
=
-\frac{31}{10}
\]
and
\[
\det J_{IP}
=
2\cdot\frac{11}{10}
-
10\cdot\frac1{20}
=
\frac{17}{10}.
\]
Thus its eigenvalues lie in the open left half-plane.

Finally, the source's positive resistant-phage equilibrium balance
\[
kA_2M_3=D
\]
forces
\[
M_3=\frac{200}{3}.
\]
At any such positive equilibrium the phage balance implies
\[
\mu f(R_3)>D,
\]
so monotonicity of the Monod law gives
\[
R_3>\lambda_2=1.
\]
The nutrient/resistant-bacteria balance gives
\[
M_3
=
\frac{D(R^0-R_3)}{\mu f(R_3)}.
\]
Because
\[
\mu f(R_3)>D,
\]
the prefactor is less than one, and therefore
\[
M_3<R^0-R_3<10.
\]
This contradicts
\[
M_3=\frac{200}{3}.
\]
The literal printed implication \(\mathcal R_0^M>1\Rightarrow\) existence of the stated positive resistant-phage equilibrium is therefore false, while the corrected threshold is consistent with nonexistence.

## Verification

The bundled `verify.py` uses exact rational arithmetic.

It verifies the break-even concentrations and source assumptions for the witness, the printed and corrected reproduction-number squares, the source's \(G(\lambda_2)\) identity under both definitions, the trace and determinant of the direct invasion block, and the incompatible bounds on \(M_3\).

The script returns `VERIFY_OK`. The exact algebra, rather than a numerical trajectory experiment, establishes the claim.

## Relationship to prior work

Van den Driessche and Watmough provide the standard next-generation framework in which new infections are separated from transitions and removals. Applying that framework to the two infected coordinates of this model produces the missing adsorption factor directly.

Han and Smith study the predecessor chemostat problem with bacteriophage-sensitive and bacteriophage-resistant bacteria. That work motivates the ecological setting but does not contain the CRISPR success factor \(\kappa\) or the source-specific displayed formula examined here.

Targeted searches by the exact DOI and title, by the resistant reproduction-number formula, by the combination of \(\kappa\), adsorption, and the \(G(\lambda_2)\) identity, and by correction or erratum terminology did not locate a published repair of this specific omission.

## Limitations

The finding establishes a missing factor in the displayed resistant-phage reproduction number and an exact counterexample to reading the associated threshold theorem with that displayed definition.

It does not show that all later numerical results are wrong. Several later formulas in the source are already consistent with the corrected expression, so the practical effect may be localized to the printed definition and statements that refer to it literally.

The counterexample concerns invasion of phage into the resistant-only equilibrium and existence of the source's resistant-phage equilibrium. It does not assert stability of the full resistant-only equilibrium against every other biological perturbation, such as introduction of sensitive bacteria.

An unindexed author correction or informal clarification could exist outside the searched literature.

## References

1. M. Shu, R. Fu, W. Wang, “A bacteriophage model based on CRISPR/Cas immune system in a chemostat,” Mathematical Biosciences and Engineering 14 (2017). DOI: 10.3934/mbe.2017070.
2. P. van den Driessche, J. Watmough, “Reproduction numbers and sub-threshold endemic equilibria for compartmental models of disease transmission,” Mathematical Biosciences 180 (2002), 29–48. DOI: 10.1016/S0025-5564(02)00108-6.
3. K. Han, H. L. Smith, “Bacteriophage-resistant and bacteriophage-sensitive bacteria in a chemostat,” Mathematical Biosciences and Engineering 9 (2012), 737–765. DOI: 10.3934/mbe.2012.9.737.
