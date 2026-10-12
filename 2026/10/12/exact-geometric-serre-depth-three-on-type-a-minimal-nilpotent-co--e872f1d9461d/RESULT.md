# Exact geometric Serre depth three on type-A minimal nilpotent cones
## Finding
For every integer \(n\ge4\), set
\[
X_n=\{A\in M_n(\mathbb C):A^2=0,\ \operatorname{rk}A\le1\}
=\overline{\mathcal O_{\min}}\subset\mathfrak{sl}_n
\]
and equip \(X_n\) with the natural two-stratum Whitney stratification
\[
X_n=\{0\}\sqcup U_n,\qquad U_n=\mathcal O_{\min}.
\]
With \(\mathbb C\)-coefficients, the constant constructible sheaf \(\mathbb C_{X_n}\) has exact geometric Serre depth three:
\[
\mathbb C_{X_n}\text{ satisfies }S_3\text{ but not }S_4.
\]
In addition, the geometric maximal Cohen--Macaulay category for this stratification has no nonzero objects.

Xu computes the \(n=3\) case explicitly. Thus, combining that base case with the argument below, both conclusions hold uniformly for every \(n\ge3\).

## Assumptions and scope
Geometric Serre conditions and geometric maximal Cohen--Macaulay objects are used in the sense of arXiv:2610.01146v1, with the ordinary constructible \(t\)-structure and Verdier duality. Coefficients are \(\mathbb C\). The stratification is exactly the orbit stratification \(\{0\}\sqcup\mathcal O_{\min}\).

The statement is about constructible sheaves, not coherent sheaves. This distinction matters: coherent maximal Cohen--Macaulay sheaves on the same minimal orbit closures form rich families, as studied in arXiv:2605.26565v1.

## Proof
The cone \(X_n\) is contractible. Its punctured cone \(U_n\) is the minimal nilpotent orbit. In type \(A_{n-1}\), the standard resolution is
\[
T^*\mathbb P^{n-1}\longrightarrow X_n,
\]
and it restricts to an isomorphism away from the zero section and the cone vertex. Equivalently,
\[
U_n\simeq T^*\mathbb P^{n-1}\setminus\mathbb P^{n-1}.
\]
After choosing a Hermitian metric, this punctured vector bundle deformation retracts onto its unit-sphere bundle with fiber \(S^{2n-3}\).

For \(n\ge3\), both the base \(\mathbb P^{n-1}\) and the fiber \(S^{2n-3}\) are simply connected, so \(U_n\) is simply connected. In degrees below the fiber dimension, the Serre--Gysin sequence identifies the cohomology with that of the base. In particular,
\[
H^1(U_n;\mathbb C)=0,\qquad H^2(U_n;\mathbb C)\cong\mathbb C.
\]
This is also the first part of Juteau's integral type-\(A_{n-1}\) cohomology table, which gives \(H^2(U_n;\mathbb Z)\cong\mathbb Z\) for \(n\ge3\).

Let \(i:\{0\}\hookrightarrow X_n\). Since \(X_n\) is a contractible cone and \(U_n=X_n\setminus\{0\}\) is connected, the localization sequence gives
\[
H^q(i^!\mathbb C_{X_n})=0\quad(q<3),
\qquad
H^3(i^!\mathbb C_{X_n})\cong H^2(U_n;\mathbb C)\cong\mathbb C.
\]
Xu's Proposition 3.3 characterizes \(S_d\) by these shriek-restriction bounds. The real codimension of the vertex is
\[
\operatorname{codim}_{\mathbb R}\{0\}=4(n-1)>3.
\]
Therefore the vanishing through degree two proves \(S_3\), while the nonzero degree-three group disproves \(S_4\).

It remains to classify possible geometric maximal Cohen--Macaulay sheaves. Any such sheaf is in particular \(S_2\). Xu's Proposition 3.5 says, once the constant sheaf is \(S_2\), that every \(S_2\) sheaf for this stratification is
\[
j_*^\circ\mathcal L
\]
for a local system \(\mathcal L\) on \(U_n\). Since \(\pi_1(U_n)=1\), every finite-rank local system is constant. Since punctured cone neighborhoods are connected, \(j_*^\circ\mathbb C_{U_n}\cong\mathbb C_{X_n}\). Hence every \(S_2\) sheaf is a finite direct sum of \(\mathbb C_{X_n}\). Every nonzero such direct sum still has nonzero \(H^3(i^!-)\), so it fails \(S_4\) and therefore cannot be maximal Cohen--Macaulay. Thus the geometric maximal Cohen--Macaulay category has no nonzero objects.

## Verification
The proof has two independent inputs that were checked directly in the cited full texts. First, arXiv:2610.01146v1 gives the local \(S_d\) criterion, the \(S_2\) pushforward classification, and the explicit \(n=3\) minimal-nilpotent example. Second, arXiv:0704.3417v2 gives the type-\(A_{n-1}\) cohomology of the minimal nilpotent orbit and a cotangent-bundle description in type \(A\).

The accompanying `verify.py` is a regression check for the dimension and low-degree ranges used in the uniform argument. It is not a substitute for the topological proof.

## Relationship to prior work
Xu's 2026 paper on geometric Serre conditions treats exactly \(X_3=\mathcal N_{3,1}\) as an example: it computes \(H^3(i^!\mathbb C_{X_3})\cong\mathbb C\), states that the constant sheaf is \(S_3\), and observes that the smooth stratum is simply connected. It does not state the uniform type-\(A\) result for \(n\ge4\).

Juteau computes the integral cohomology of minimal nilpotent orbits uniformly and, in type \(A_{n-1}\), obtains \(H^2(U_n;\mathbb Z)\cong\mathbb Z\) for \(n\ge3\). That work predates geometric Serre conditions and does not formulate constructible \(S_d\)-depth or a geometric maximal Cohen--Macaulay category.

A separate 2026 paper of Xu studies coherent, equivariant maximal Cohen--Macaulay sheaves on these same algebraic singularities and exhibits many such sheaves. It concerns the coherent category rather than the constructible geometric category. The vanishing result here therefore gives a categorical contrast rather than contradicting that classification.

## Limitations
The zero-category conclusion depends on the natural two-stratum Whitney stratification and on \(\mathbb C\)-coefficients. Refining the stratification or changing coefficients can change the local-system category and the relevant low-degree topology. No claim is made for other Lie types. The originality comparison is subject to the possibility that the same synthesis of the 2007 cohomology calculation with the new 2026 geometric-Serre formalism appears in unindexed material.

## References
1. Shang Xu, *Verdier-Type Category, Geometric Serre's conditions and perversity*, arXiv:2610.01146v1, 1 October 2026.
2. Daniel Juteau, *Cohomology of the minimal nilpotent orbit*, Transformation Groups 13 (2008), 355--387, arXiv:0704.3417v2, DOI 10.1007/s00031-008-9009-x.
3. Shang Xu, *Equivariant Maximal Cohen-Macaulay sheaves on the minimal orbit closures*, arXiv:2605.26565v1, 26 May 2026.
