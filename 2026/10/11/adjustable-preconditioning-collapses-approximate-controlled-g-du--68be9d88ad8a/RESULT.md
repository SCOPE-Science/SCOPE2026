# Adjustable preconditioning collapses approximate controlled \(g\)-duality to exact \(g\)-duality
## Finding
Let \(F=(f_j)\) be a \(C\)-controlled frame on a Hilbert space \(H\), let \(G=(g_j)\) be a Bessel sequence, let \(T_C\) denote the controlled synthesis operator of \(F\), and let \(U\) denote the synthesis operator of \(G\). Put
\[
R=T_CU^*.
\]
Definition 3.4 of Ramezani calls \(G\) an approximate \(C\)-controlled \(g\)-dual when there is an invertible operator \(A\) such that
\[
\|I-RA\|<1.
\]
This condition is equivalent to invertibility of \(R\), hence equivalent to exact \(C\)-controlled \(g\)-duality. Therefore the adjustable operator \(A\) collapses the proposed approximate notion to the exact one.

Two consequences in Corollary 3.8 do not follow. Part (iii), which asserts ordinary approximate \(C\)-controlled duality, is false. The Neumann-series formula in part (i) is also false without a closeness condition on the unpreconditioned mixed operator.
## Assumptions and scope
The argument uses exactly the Hilbert-space setting and operator conventions of the source. The family \(F\) is a \(C\)-controlled frame, \(G\) is Bessel, \(C\) is invertible, and \(T_C\) and \(U\) are bounded synthesis operators. No positivity or commutation assumption beyond those already needed to speak about the source's controlled frame is used in the equivalence.

The result concerns Definition 3.4 and Corollary 3.8 of the cited paper. It does not dispute the standard fixed-operator notion of approximate duality, where the reconstruction defect itself is required to have norm less than one.
## Proof
Assume first that Definition 3.4 holds, so some invertible \(A\) satisfies
\[
\|I-RA\|<1.
\]
By the Neumann lemma, \(RA\) is invertible. Since \(A\) is invertible,
\[
R=(RA)A^-1
\]
is invertible. With \(B=R^-1\), one has
\[
RB=I,
\]
which is exactly the reconstruction identity for a \(C\)-controlled \(g\)-dual associated with \(B\).

Conversely, if \(G\) is an exact \(C\)-controlled \(g\)-dual of \(F\), then for some invertible \(B\),
\[
RB=I.
\]
Taking \(A=B\) gives \(\|I-RA\|=0<1\). Thus the approximate class in Definition 3.4 and the exact controlled \(g\)-dual class coincide.

For the failure of Corollary 3.8(iii), take
\[
H=\mathbb C,\qquad C=I,\qquad f_1=1,\qquad g_1=3.
\]
The one-vector family \(F=(1)\) is Parseval, \(G=(3)\) is Bessel, and
\[
R=T_CU^*=3I.
\]
Choosing \(A=I/3\) gives
\[
\|I-RA\|=0,
\]
so \(G\) is an approximate \(C\)-controlled \(g\)-dual in Definition 3.4. However ordinary approximate \(C\)-controlled duality requires
\[
\|I-R\|<1,
\]
and here \(\|I-R\|=2\). Hence Corollary 3.8(iii) is false.

The same example disproves the displayed Neumann expansion in Corollary 3.8(i). Since \(UT_C^*=3I\), its left-hand side is well defined, but the claimed series contains
\[
(I-UT_C^*)^n=(-2)^nI,
\]
so it diverges in operator norm and on the nonzero vector \(g_1\). The exact dual \((UT_C^*)^-1g_1\) remains valid; what fails is the unjustified series representation.
## Verification
Every step is an operator identity. The only analytic input is the standard Neumann lemma: \(\|I-X\|<1\) implies that \(X\) is invertible. The scalar witness can be checked directly: the preconditioned defect is zero, the unpreconditioned defect has norm \(2\), and the proposed Neumann terms grow in magnitude.

The source's full text was inspected at Definitions 3.3--3.4, Theorems 3.5 and 3.7, and Corollary 3.8. The primary classification is 42C15, and the verified public publication date is 2022-04-01.
## Relationship to prior work
Christensen and Laugesen distinguish approximate duals from pseudo-duals: approximate duality requires the fixed mixed reconstruction operator to lie within norm \(1\) of the identity, whereas pseudo-duality only requires invertibility. Their Neumann expansion is stated under the fixed-operator norm condition. Ramezani's free invertible factor \(A\) changes this geometry: existence of such an \(A\) is exactly invertibility of the mixed operator, so the proposed approximate \(g\)-dual notion has the strength of pseudo-duality and, in the controlled setting, of exact \(g\)-duality.

Targeted searches for the exact paper, Corollary 3.8, the mixed-operator formulation, and the Neumann-series issue did not locate a published correction stating this equivalence or the scalar counterexample.
## Limitations
The result does not say that every exact controlled \(g\)-dual is an ordinary approximate controlled dual. The scalar example shows the opposite. Nor does it claim that a Neumann series can never converge when \(\|I-R\|\ge1\); it only shows that Definition 3.4 does not provide the hypothesis needed for the printed expansion, and that the expansion can diverge.

An unindexed erratum, thesis remark, or informal correction could contain the same observation.
## References
1. S. M. Ramezani, *Controlled g-dual frames and their approximates in Hilbert spaces*, Hacettepe Journal of Mathematics and Statistics 51 (2022), 421--429, DOI 10.15672/hujms.784819.
2. O. Christensen and R. S. Laugesen, *Approximately dual frame pairs in Hilbert spaces and applications to Gabor frames*, arXiv:0811.3588v1; later published in Sampling Theory in Signal and Image Processing.
