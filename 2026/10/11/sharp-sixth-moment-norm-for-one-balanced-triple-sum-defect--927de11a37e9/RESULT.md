# Sharp sixth-moment norm for one balanced triple-sum defect
## Finding
Let \(\Gamma\) be a discrete abelian group and let
\[
\Lambda=\{\lambda_0,\lambda_1,\lambda_2,\lambda_3\}\subset\Gamma
\]
consist of four distinct elements. Assume that the map from size-three multisets in \(\Lambda\) to their group sum has exactly one nonsingleton fiber and, after relabeling, that fiber is
\[
2\lambda_0+\lambda_3=\lambda_1+2\lambda_2.
\]
For
\[
F=\sum_{j=0}^3 c_j\lambda_j
\]
on the compact dual \(\widehat\Gamma\), with normalized Haar measure, the sharp inequality is
\[
\|F\|_6\le K\left(\sum_{j=0}^3|c_j|^2\right)^{1/2},
\qquad
K^6=\frac{97\sqrt{97}-260}{162}.
\]
Numerically, \(K^6=4.292217325766804\ldots\) and \(K=1.274814370731655\ldots\).

Put
\[
p_*=\frac{\sqrt{97}-5}9,
\qquad
q_*=\frac{14-\sqrt{97}}9.
\]
For a nonzero coefficient family equality holds exactly when, with \(S=\sum_j|c_j|^2\),
\[
|c_0|^2=|c_2|^2=\frac{p_*S}2,
\qquad
|c_1|^2=|c_3|^2=\frac{q_*S}2,
\]
and the unique resonant products have the same phase:
\[
2\arg c_0+\arg c_3-\arg c_1-2\arg c_2\equiv0\pmod{2\pi}.
\]

A concrete integer example is \(\Lambda=\{0,1,4,9\}\subset\mathbb Z\), because among the twenty size-three multisets there is exactly one repeated sum,
\[
0+0+9=1+4+4.
\]
Thus the same sharp constant and complete extremizer description hold for four-term trigonometric polynomials with this support.

## Assumptions and scope
A size-three multiset permits repetition. The hypothesis is exact: apart from permutations within a multiset and the displayed equality, no two size-three multisets drawn from \(\Lambda\) have the same sum in \(\Gamma\). The group need not be torsion-free; all torsion effects are already excluded by this hypothesis.

The result concerns the \(L^2\)-to-\(L^6\) norm for one balanced triple-sum defect of multiplicity type \(2+1=1+2\). It does not cover the different defect type \(2+1=3\), several simultaneous triple-sum collisions, or finite quotients in which additional congruence collisions appear.

## Proof
Write
\[
x_j=|c_j|^2,
\qquad
S=\sum_{j=0}^3x_j.
\]
If all size-three sums were distinct, Parseval applied to \(F^3\) would give the independent-Steinhaus sixth-moment polynomial
\[
H(x)=\sum_{\alpha_0+\cdots+\alpha_3=3}
\left(\frac{3!}{\alpha_0!\cdots\alpha_3!}\right)^2
\prod_{j=0}^3x_j^{\alpha_j}
=6S^3-9S\sum_jx_j^2+4\sum_jx_j^3.
\]
The unique collision combines the Fourier coefficients \(3c_0^2c_3\) and \(3c_1c_2^2\). Hence the exact identity is
\[
\|F\|_6^6
=H(x)+18\operatorname{Re}\!\left(c_0^2c_3\overline{c_1c_2^2}\right).
\]
Therefore
\[
\|F\|_6^6
\le H(x)+18x_0x_2\sqrt{x_1x_3},
\]
with equality exactly when the displayed phase condition holds whenever all four coefficients are nonzero.

By homogeneity set \(S=1\). Put
\[
p=x_0+x_2,
\qquad
q=x_1+x_3=1-p,
\qquad
u=x_0x_2,
\qquad
v=x_1x_3.
\]
For fixed \(p,q\), the part of \(H\) involving \(x_0,x_2\) is
\[
-9p^2+4p^3+(18-12p)u,
\]
and the analogous part for \(x_1,x_3\) is
\[
-9q^2+4q^3+(18-12q)v.
\]
The resonant term is \(18u\sqrt v\). Since \(0\le p,q\le1\), both coefficients \(18-12p\) and \(18-12q\) are strictly positive. Thus, for fixed pair sums, the objective is strictly increasing in both products \(u\) and \(v\). Consequently every maximizer satisfies
\[
x_0=x_2=\frac p2,
\qquad
x_1=x_3=\frac q2.
\]
Substitution leaves the one-variable cubic
\[
\Phi(p)
=\frac52+6p-\frac{15}4p^2-\frac94p^3,
\qquad 0\le p\le1.
\]
Its derivative is
\[
\Phi'(p)=-\frac34\left(9p^2+10p-8\right).
\]
The quadratic has exactly one root in \([0,1]\), namely \(p_*=(\sqrt{97}-5)/9\). The derivative is positive before \(p_*\) and negative after it, so \(p_*\) is the unique global maximizer. Direct substitution gives
\[
\Phi(p_*)=\frac{97\sqrt{97}-260}{162}.
\]
Because \(0<p_*<1\), all four extremal magnitudes are nonzero. The strict pair-balancing steps force the stated magnitudes, and equality in the resonant real-part bound forces exactly the stated phase congruence. This proves sharpness and the complete equality classification.

## Verification
The bundled `verify.py` uses exact rational arithmetic and an exact quadratic-field representation for \(\mathbb Q(\sqrt{97})\). It checks the twenty size-three multisets of \(\{0,1,4,9\}\), verifies that \(0+0+9=1+4+4\) is the sole collision, verifies the normalized sixth-moment formula by direct convolution on deterministic test vectors, checks that \(p_*\) solves \(9p^2+10p-8=0\), and checks the exact value \((97\sqrt{97}-260)/162\). It reports `VERIFY_OK`.

The finite-support enumeration is exhaustive for the concrete four-point example. The general theorem itself is analytic and is not inferred from numerical sampling.

## Relationship to prior work
Michels studies \(\Lambda(p)\)-sets on compact abelian groups and explicitly defines the optimal constants \(K_p(\Lambda)\); this supplies the classical thin-set framework in which the present sharp finite \(p=6\) constant lives. The inspected paper characterizes infinite sets through operator-ideal limit order and does not evaluate a four-character support with a specified triple-sum defect.

Peskir proves Schur-concavity for even moments of sums of independent complex Steinhaus variables. That result exactly controls the collision-free baseline \(H(x)\), but independence removes the deterministic resonant cross term. It therefore does not imply the present defect constant or the unequal two-pair extremal magnitudes.

Related exact results for the three-frequency defect \(2+1=3\), a Boolean rectangular product spectrum, and fourth-moment single pair-sum defects have different hypotheses. None has the present balanced \(2+1=1+2\) triple-collision profile, and their constants and equality equations differ.

## Limitations
The theorem is conditional on there being exactly one nontrivial size-three multiset collision and on that collision having the balanced multiplicity pattern \(2+1=1+2\). Additional relations can create further cross terms and invalidate the one-variable reduction.

The literature search cannot exclude an older equivalent formula hidden under different terminology for finite \(\Lambda(6)\) sets, three-fold additive energy, or resonant trigonometric polynomials. The two most directly relevant full texts inspected do not contain the stated constant or equality classification.

## References
C. Michels, “\(\Lambda(p)\)-sets and the limit order of operator ideals,” arXiv:math/9904176v1, first submitted 1999-04-30. Primary MSC includes 43A46.

G. Peskir, “Best Constants in Kahane-Khintchine Inequalities for Complex Steinhaus Functions,” *Proceedings of the American Mathematical Society* 123 (1995), 3101–3111, DOI 10.1090/S0002-9939-1995-1283561-0.
