# Exact four-atom feasibility polytope for two uniform marginals

## Finding
Let \(\mathcal D^U_2\) be the set of distributions of \(X+Y\) when \(X\) and \(Y\) are each \(\operatorname{Unif}[0,1]\), with no independence assumption. Let \(F\) be a probability law supported on
\[
\left\{\frac14,\frac34,\frac54,\frac74\right\},
\]
and write its masses in increasing support order as \((p_0,p_1,p_2,p_3)\). Then
\[
F\in\mathcal D^U_2
\quad\Longleftrightarrow\quad
\mathbb E_F Z=1,\qquad p_0\le\frac14,\qquad p_3\le\frac14.
\]
Equivalently, every feasible mass vector, and only a feasible mass vector, has the form
\[
(p_0,p_1,p_2,p_3)
=
\left(\alpha,\frac12-2\alpha+\delta,\frac12+\alpha-2\delta,\delta\right),
\qquad 0\le\alpha,\delta\le\frac14.
\]
Thus the feasible family is exactly a rectangle in the two outer-atom masses.

## Assumptions and scope
The marginals are exactly standard uniform distributions on \([0,1]\); their dependence is arbitrary. The target law is only assumed to be supported on the displayed four-point arithmetic progression; some masses may vanish. Membership itself forces mean \(1\), because each marginal has mean \(1/2\).

This support is the first centered four-point lattice of the form \(1+\{-3,-1,1,3\}/m\) for which all four offsets can occur in the common-fractional-part reduction: \(m=4\). It is therefore a minimal genuinely four-atomic lattice case immediately beyond the bi-atomic and equidistant tri-atomic cases previously characterized for two standard-uniform marginals.

## Proof
Necessity of the mean is immediate. Assume next that \(F\in\mathcal D^U_2\), so there are \(X,Y\sim\operatorname{Unif}[0,1]\) with \(Z=X+Y\sim F\). Define
\[
A=4X,\qquad B=4(1-Y).
\]
Both \(A\) and \(B\) are uniform on \([0,4]\), and
\[
A-B=4(Z-1)\in\{-3,-1,1,3\}\quad\text{almost surely}.
\]
Hence the fractional parts of \(A\) and \(B\) agree almost surely. Ignoring the null endpoint event, write
\[
A=I+U,\qquad B=J+U,
\]
where \(I,J\in\{0,1,2,3\}\) and \(U\in[0,1)\) is the common fractional part.

For any Borel set \(E\subset[0,1)\), uniformity of \(A\) gives
\[
\Pr\{I=i,\ U\in E\}=\frac{|E|}{4},
\]
and the same statement holds for \(J\). Therefore, for almost every \(u\), a regular conditional matrix
\[
q_{ij}(u)=\Pr\{I=i,J=j\mid U=u\}
\]
has every row sum and every column sum equal to \(1/4\). Since \(I-J=A-B\) only takes the four odd values \(-3,-1,1,3\), all entries on the other diagonals vanish almost everywhere. In particular,
\[
p_0=\Pr\{I-J=-3\}=\int_0^1 q_{03}(u)\,du\le\frac14,
\]
and similarly
\[
p_3=\Pr\{I-J=3\}=\int_0^1 q_{30}(u)\,du\le\frac14.
\]
This proves the necessary outer-mass inequalities.

Conversely, suppose \(F\) has mean \(1\), and put \(\alpha=p_0\), \(\delta=p_3\), with \(0\le\alpha,\delta\le1/4\). Total mass and the mean equation force
\[
p_1=\frac12-2\alpha+\delta,
\qquad
p_2=\frac12+\alpha-2\delta.
\]
These are nonnegative throughout the stated rectangle. Define the probability matrix
\[
Q=
\begin{pmatrix}
0&\frac14-\alpha&0&\alpha\\
\frac14-\delta&0&\delta&0\\
0&\alpha&0&\frac14-\alpha\\
\delta&0&\frac14-\delta&0
\end{pmatrix}.
\]
Every row sum and column sum of \(Q\) is \(1/4\). Choose \((I,J)\) with joint probabilities \(Q_{ij}\), independently choose \(U\sim\operatorname{Unif}[0,1)\), and set
\[
A=I+U,\qquad B=J+U,\qquad X=\frac A4,\qquad Y=1-\frac B4.
\]
The row and column sums show that \(A\) and \(B\) are uniform on \([0,4]\), hence \(X,Y\sim\operatorname{Unif}[0,1]\). Moreover,
\[
X+Y=1+\frac{I-J}4.
\]
The four diagonal totals of \(Q\) are
\[
\Pr\{I-J=-3\}=\alpha,
\]
\[
\Pr\{I-J=-1\}=2\left(\frac14-\alpha\right)+\delta
=\frac12-2\alpha+\delta,
\]
\[
\Pr\{I-J=1\}=\alpha+2\left(\frac14-\delta\right)
=\frac12+\alpha-2\delta,
\]
and
\[
\Pr\{I-J=3\}=\delta.
\]
Thus \(X+Y\sim F\), proving sufficiency and the complete characterization.

## Verification
The proof is analytic and does not rely on finite enumeration. A supplemental exact-rational checker verifies the affine mass formulas, nonnegativity over a rational grid in the full feasible rectangle, all row and column sums of the displayed coupling matrix, and the four diagonal totals. Its successful output is included as `verification_output.txt`.

The boundary cases \(\alpha=0\), \(\delta=0\), \(\alpha=1/4\), and \(\delta=1/4\) require no limiting argument: the same matrix remains nonnegative and defines a valid coupling, with some entries equal to zero.

## Relationship to prior work
Mao, Wang and Wang study exactly the set \(\mathcal D^U_2\) of aggregate laws of two standard uniform marginals. Their introduction states that a complete determination in dimension two remains unclear, and Section 3 gives discrete characterizations for bi-atomic laws and for equidistant tri-atomic laws (Theorems 3.4 and 3.5 in the arXiv text). The four-point family here is not covered by those statements. Their paper also treats continuous-density subclasses, which do not include the discrete target considered here.

Wang and Wang characterize joint mixability for tuples of uniform distributions and several continuous-density classes. That theory is an important structural precursor, but it does not state the present four-atom target-sum criterion: here the third distribution in the equivalent joint-mixability formulation is discrete.

Classical Makarov--Rüschendorf bounds determine sharp pointwise bounds for the distribution function of a sum with fixed marginals. Those bounds explain the necessity of the outer inequalities from another direction, but pointwise sharpness does not in general imply simultaneous attainability of an entire target distribution. The result above supplies that simultaneous sufficiency for this four-point support and gives an explicit coupling for every feasible mass vector.

## Limitations
No claim is made for arbitrary four-atomic supports, for other lattice spacings, or for more than two marginals. The characterization is specific to the displayed quarter-grid support. The originality search did not locate an equivalent published statement, but an elementary equivalent construction could exist under transportation-polytope, shuffle-of-min, or rearrangement terminology.

## References
1. T. Mao, B. Wang and R. Wang, *Sums of Standard Uniform Random Variables*, arXiv:1811.11981; Journal of Applied Probability 56 (2019), 918--936. DOI: 10.1017/jpr.2019.52.
2. B. Wang and R. Wang, *Joint Mixability*, Mathematics of Operations Research 41 (2016), 808--826. DOI: 10.1287/moor.2015.0755.
3. G. D. Makarov, *Estimates for the Distribution Function of a Sum of Two Random Variables When the Marginal Distributions are Fixed*, Theory of Probability and Its Applications 26 (1982), 803--806. DOI: 10.1137/1126086.
