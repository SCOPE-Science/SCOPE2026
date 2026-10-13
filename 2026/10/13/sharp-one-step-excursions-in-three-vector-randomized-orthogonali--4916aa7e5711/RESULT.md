# Sharp one-step excursions in three-vector randomized orthogonalization

## Finding
Let \(B\in\mathbb R^{3\times3}\) be symmetric positive definite, and define the diagonal-normalized inverse-trace potential
\[
\Gamma(B)=\sum_{i=1}^{3} B_{ii}(B^{-1})_{ii}-3\geq0.
\]
Select uniformly one of the three unordered index pairs \(J\subset\{1,2,3\}\), \(|J|=2\). Make any invertible real change of basis supported on \(J\) that renders the corresponding two-by-two principal block diagonal, obtaining \(B'\). The following assertions hold **for every** such \(B\) and every permitted within-pair change of basis:

1. If \(\Gamma(B)>0\), then \(\Gamma(B')/\Gamma(B)<4/3\) deterministically, while \(\mathbb P\{\Gamma(B')>\Gamma(B)\}\leq 1/3\).
2. The factor \(4/3\) is the sharp unattained supremum of \(\Gamma(B')/\Gamma(B)\) over positive-definite inputs with positive initial potential and legal pivots. The upward-pivot probability \(1/3\) is attained, including by an open set of inputs.
3. More precisely, for every fixed threshold \(1\leq t<4/3\),
\[
\sup_{B\succ0:\,\Gamma(B)>0}\mathbb P\!\left\{\frac{\Gamma(B')}{\Gamma(B)}>t\right\}=\frac13,
\]
whereas the probability vanishes for every \(t\geq4/3\). In dimension two a legal pair step always makes the potential zero, so dimension three is the smallest dimension with an upward excursion.

For diagonal \(B\), every permitted pivot leaves \(\Gamma(B')=0\). The classical expected one-step identity \(\mathbb E[\Gamma(B')\mid B]=\frac23\Gamma(B)\) is **not** asserted to be new.

## Assumptions and scope
All matrices are real, symmetric and strictly positive definite. A legal pair transformation has the form \(B'=T^{\mathsf T}BT\), where \(T\) is invertible, equals the identity outside the two chosen coordinates, and the chosen principal two-by-two block of \(B'\) is diagonal. No orthogonality or triangularity is assumed for \(T\). Uniform randomness refers only to the three unordered pivot pairs; the new bounds do not depend on which legal transformation diagonalizes a selected block. Arithmetic and probabilities are exact. Positive definiteness, rather than positive semidefiniteness, is essential for all inverses and the strict ceiling.

## Proof
**Exact pair update, independently derived.** Write \(J=\{i,j\}\). Because the transformation is supported on \(J\), the diagonal contributions \(B_{kk}(B^{-1})_{kk}\) for \(k\notin J\) are unchanged. The sum of the two new contributions is
\[
\operatorname{tr}\bigl(B'_{JJ}(B'^{-1})_{JJ}\bigr)
=\operatorname{tr}\bigl(B_{JJ}(B^{-1})_{JJ}\bigr),
\]
because the new principal block is diagonal and the new principal inverse block is the contragredient transform of the old one. Subtracting the old two diagonal contributions gives the exact identity
\[
\Gamma(B')-\Gamma(B)=2B_{ij}(B^{-1})_{ij}. \tag{1}
\]
This identity is also established in Detherage--Shah, Lemma 4.1; the derivation here fixes the admissible transformation class explicitly.

**Correlation reduction and positivity.** Let \(D\) be the positive diagonal of \(B\), and set \(R=D^{-1/2}BD^{-1/2}\). Both \(\Gamma(B)=\Gamma(R)\) and the products \(B_{ij}(B^{-1})_{ij}=R_{ij}(R^{-1})_{ij}\) are invariant under this diagonal congruence. Thus take
\[
R=\begin{pmatrix}1&a&b\\a&1&c\\b&c&1\end{pmatrix},
\qquad
\Delta=\det R=1-a^2-b^2-c^2+2abc>0.
\]
Every correlation satisfies \(|a|,|b|,|c|<1\). Direct cofactor expansion yields
\[
\Gamma(R)=\frac{2H}{\Delta},\quad
H=a^2+b^2+c^2-3abc,
\quad
\frac{\Gamma(R')-\Gamma(R)}{\Gamma(R)}=
\frac{a(bc-a)}{H} \tag{2}
\]
for pivot \(\{1,2\}\). The other pairs follow cyclically. Also \(\Gamma(R)=\operatorname{tr}(R^{-1})-3\geq0\) by convexity of reciprocation and \(\operatorname{tr}(R)=3\); equality requires \(R=I\). Therefore \(H>0\) whenever \(\Gamma>0\).

**At most one upward pair.** The three possible potential increases have signs of \(abc-a^2\), \(abc-b^2\), and \(abc-c^2\). If \(abc\leq0\), none can increase. If \(abc>0\), diagonal sign changes reduce without changing these signs to \(a,b,c>0\). An increase for pair \(\{1,2\}\) requires \(a<bc\). If additionally pair \(\{1,3\}\) increased, then \(b<ac\), implying \(ab<ab\,c^2\), contradicting \(c^2<1\). The other pair combinations are symmetric. Hence among the three equally likely pairs at most one increases: the probability is at most \(1/3\).

**Sharp amplification ceiling.** It remains to bound the ratio in the only nontrivial case of an upward pair. After sign changes and relabeling assume \(0<a<bc\) with \(a,b,c>0\). Put \(z=bc\) and \(d=(b-c)^2\geq0\). From \(\Delta=(1-a)(1+a-2z)-d>0\) and \(a<1\) we get
\[
a<z<\frac{1+a}{2}.
\]
Formula (2) becomes
\[
\frac{\Gamma'}{\Gamma}-1
=\frac{a(z-a)}{a^2+d+(2-3a)z}
\leq\frac{a(z-a)}{a^2+(2-3a)z}. \tag{3}
\]
The denominator after dropping \(d\) stays positive throughout this interval: if \(a\leq2/3\) this is immediate, and if \(a>2/3\) its minimum is the positive endpoint value \((1-a)(a+2)/2\). For fixed \(0<a<1\), the right-hand side of (3) has strictly positive derivative
\[
\frac{2a^2(1-a)}{\bigl(a^2+(2-3a)z\bigr)^2}>0.
\]
Thus substituting the unattainable upper endpoint yields
\[
\frac{\Gamma'}{\Gamma}-1
<\frac{a}{a+2}<\frac13,
\]
proving the strict ceiling. Nonincreasing pairs already satisfy the bound.

**Exact sharpness and full upward tail.** For \(0<h<1/3\), choose
\[
a=1-4h+3h^2,\qquad b=c=1-h.
\]
Then the correlation matrix is strictly positive definite, since \(1-a^2>0\) and \(\Delta=h^3(4-3h)>0\). Its auxiliary term is \(H=6h(1-h)^2>0\). Only the pair with correlation \(a\) increases, and an exact simplification of (2) gives
\[
\frac{\Gamma'}{\Gamma}=\frac43-h.
\]
Consequently the supremum of the amplification factor is \(4/3\), and for each \(1\leq t<4/3\) sufficiently small \(h\) yields probability exactly \(1/3\) of crossing \(t\); all other pairs are nonincreasing. For \(t\geq4/3\), the strict ceiling makes that probability zero. A simple separate probability witness is \((a,b,c)=(1/8,1/2,1/2)\), whose determinant is \(35/64>0\); only the \(a\)-pair increases. Since these inequalities are strict and depend continuously on the entries within the positive-definite cone, the probability witness persists on a nonempty open set.

In dimension two, the only available pair diagonalizes the entire matrix, making \(\Gamma'=0\). This proves minimality and completes the theorem.

## Verification
Run `python3 verify.py` using only Python's standard library. The checker constructs each legal pair step directly by an invertible elementary basis change, forms the transformed full three-by-three matrix, computes its inverse cofactor-by-cofactor over exact rational numbers, and checks the pair update identity, sharp inequality, and number of increasing pivot pairs on 2,351 positive-definite correlation matrices from a rational grid (7,053 exact pivot transformations). It separately checks five rational near-extremizers and the explicit one-third probability witness. It prints `VERIFY_OK` if all checks succeed. These finite tests independently verify formulae and examples; the universal statement and sharp supremum are established by the proof above, not by enumeration.

## Relationship to prior work
Detherage and Shah, *Matrix Factorizations with Uniformly Random Pivoting* (arXiv:2505.02023, first public 2025-05-04), introduced this diagonal-inverse-trace potential and proved the general deterministic pair update and expected linear contraction in Sections 3--4. Their Remark 5 explicitly notes that this potential need not decrease on each step. The present theorem determines the exact sharp **three-dimensional pathwise amplification bound and complete upward one-step tail**, which are neither consequences of their expectation alone nor explicitly provided by the inspected manuscript. The algebraic update identity itself is credited and not presented as new.

The earlier Detherage--Shah *A Kaczmarz-Inspired Method for Orthogonalization* (arXiv:2411.16101, Section 2.1) proves a monotone *logarithmic volume* potential for its one-sided normalized update; monotonicity of that different potential does not imply monotonicity or the sharp bound for \(\Gamma\). Steinerberger, *Kaczmarz Kac Walk* (arXiv:2411.06614, Section 1.3), analyzes expected directional norm evolution for the related row-update process, not the present inverse-trace excursion law. An unindexed equivalent classification remains a residual originality risk.

## Limitations
The sharp constant and one-third tail are proved only in the **real three-dimensional** positive-definite setting under a uniform unordered pair choice; they do not claim general dimensions, complex Hermitian matrices, multistep tails, or finite-precision stability. The high-amplification extremizers become nearly singular, so their exact arithmetic behavior need not persist in low-precision implementations. No independent validation or additional convergence theorem is claimed.

## References
1. I. Detherage and R. Shah, *Matrix Factorizations with Uniformly Random Pivoting*, arXiv:2505.02023v4, Section 3.2, Lemmas 4.1--4.2, Remark 5. https://arxiv.org/html/2505.02023v4
2. I. Detherage and R. Shah, *A Kaczmarz-Inspired Method for Orthogonalization*, arXiv:2411.16101v3, Section 2.1. https://arxiv.org/pdf/2411.16101
3. S. Steinerberger, *Kaczmarz Kac Walk*, arXiv:2411.06614v1, Section 1.3. https://arxiv.org/pdf/2411.06614
