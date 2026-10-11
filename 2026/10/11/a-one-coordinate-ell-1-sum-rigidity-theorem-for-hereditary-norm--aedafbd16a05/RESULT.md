# A one-coordinate \(\ell_1\)-sum rigidity theorem for hereditary norm attainment
## Finding
Let \(E\) be a real Banach sequence lattice with a finite or countably infinite normalized \(1\)-unconditional Schauder basis \((e_i)_{i\in I}\) and coordinatewise order. Form the Banach lattice
\[
X=E\oplus_1\mathbb R,
\qquad
\|(u,t)\|_X=\|u\|_E+|t|.
\]
Then
\[
\boxed{\ X\text{ has HNAp }\Longleftrightarrow E\text{ is coordinatewise }\ell_1(I).\ }
\tag{1}
\]
Here the right-hand side means, precisely, that every finitely supported real family satisfies
\[
\boxed{\ \left\|\sum_i a_i e_i\right\|_E=\sum_i|a_i|.\ }
\tag{2}
\]
A single added scalar \(\ell_1\)-summand thus preserves hereditary norm attainment within this class only when the original norm was already additive on disjoint positive coordinates.

In particular, every normalized absolute norm on \(\mathbb R^2\) has hereditary norm attainment by Acosta--Soleimani-Mourchehkhorti, but its scalar \(\ell_1\)-extension has the property **only** if the original plane is \(\ell_1^2\).

## Assumptions and scope
All Banach spaces and functionals are real. A normalized \(1\)-unconditional Schauder basis is used with its natural coordinatewise lattice order, \(\|e_i\|_E=1\) for every index, and finite-support vectors are norm dense in \(E\). The index set \(I\) is finite or countably infinite.

For any Banach lattice \(Z\), write \(z^+\), \(z^-\) for its lattice positive and negative parts, and likewise \(h^+\), \(h^-\) in \(Z^*\). According to Acosta--Soleimani-Mourchehkhorti's Definition 2.1, \(Z\) has the *hereditary norm-attaining property* (HNAp) if, whenever \(z\in Z\), \(h\in Z^*\) and
\[
h(z)=\|h\|\,\|z\|,
\]
one has **both**
\[
h^+(z^+)=\|h^+\|\,\|z^+\|
\quad\text{and}\quad
h^-(z^-)=\|h^-\|\,\|z^-\|.
\tag{3}
\]
We do not identify this property with the separately defined Bishop--Phelps--Bollobás property for positive functionals.

The dual of \(X\) is \(X^*=E^*\oplus_\infty\mathbb R\), with
\[
\|(f,s)\|_{X^*}=\max\{\|f\|_{E^*},|s|\}.
\tag{4}
\]

## Proof
**Step 1: nonadditivity supplies a positive witness.** For every finite-support vector, normalization and the triangle inequality give
\[
\left\|\sum_i a_i e_i\right\|_E\le\sum_i|a_i|.
\tag{5}
\]
If equality held in (5) for every finite-support vector, completion from the dense basis span would identify \(E\) isometrically and as an ordered lattice with \(\ell_1(I)\). Hence, unless \(E\) is the right-hand side of (1), there is a positive finite-support vector
\[
a=\sum_i a_i e_i\ge0,
\qquad
\|a\|_E=1,
\qquad
\sum_i a_i>1.
\tag{6}
\]
To see the positivity in (6), replace a witness by its coordinatewise modulus; unconditionality preserves its norm.

By the Hahn--Banach theorem, choose a real norming functional \(f_0\in S_{E^*}\) with \(f_0(a)=1\). Its lattice modulus \(f=|f_0|\) is positive and satisfies
\[
\|f\|_{E^*}=1,
\qquad
f(a)\ge|f_0(a)|=1.
\]
The upper bound from duality is \(f(a)\le1\), so
\[
f(a)=1.
\tag{7}
\]
For each coordinate \(i\), put \(f_i=f(e_i)\). Positivity and normalization imply
\[
0\le f_i\le1.
\tag{8}
\]
If \(f_i=1\) for every \(i\) such that \(a_i>0\), equations (6)--(7) would give
\[
1=f(a)=\sum_i a_i>1,
\]
a contradiction. Therefore there is an index \(i_0\) with
\[
a_{i_0}>0,
\qquad
f_{i_0}<1.
\tag{9}
\]

**Step 2: a sign flip and one scalar coordinate force failure.** Let \(S:E\to E\) be the coordinate sign isometry defined by
\[
(Su)_{i_0}=u_{i_0},
\qquad
(Su)_j=-u_j\quad(j\ne i_0).
\tag{10}
\]
This is a surjective norm isometry by unconditionality. Define
\[
x=(Sa,0)\in X,
\qquad
F=(S^*f,1)\in X^*.
\tag{11}
\]
By (4), (7), and (10),
\[
\|x\|_X=\|F\|_{X^*}=1,
\qquad
F(x)=f(a)=1.
\tag{12}
\]
Thus \(F\) **attains its norm** at \(x\).

Because \(a\ge0\) and every coordinate other than \(i_0\) was sign-flipped, the positive part of \(x\) is
\[
x^+=(a_{i_0}e_{i_0},0),
\qquad
\|x^+\|_X=a_{i_0}.
\tag{13}
\]
The positive dual part is
\[
F^+=(f_{i_0}e_{i_0}^*,1).
\tag{14}
\]
Indeed, \(f\ge0\), the functional \(S^*f\) is positive on coordinate \(i_0\) and negative on all other coordinates, and the coordinate projections are lattice band projections. The density of finitely supported vectors ensures that these coordinate identities uniquely determine functionals on \(E\). By (4), (8), and (14),
\[
\|F^+\|_{X^*}=\max\{f_{i_0},1\}=1.
\tag{15}
\]
But (9), (13), and (14) imply
\[
F^+(x^+)=a_{i_0}f_{i_0}
<a_{i_0}=\|F^+\|\,\|x^+\|_X.
\tag{16}
\]
The positive identity in the definition (3) fails. Hence \(X\) does **not** have HNAp whenever \(E\) is not coordinatewise \(\ell_1\).

**Step 3: additivity suffices.** Conversely, suppose (2) holds. The map sending every basis coordinate and the extra scalar coordinate to a distinct coordinate identifies
\[
X=\ell_1(I\sqcup\{*\})
\]
as a Banach lattice. Let \(x\in S_X\), \(F\in S_{X^*}=S_{\ell_\infty}\) and \(F(x)=1\). Since
\[
\sum_k F_kx_k
\le\sum_k|F_k|\,|x_k|
\le\sum_k|x_k|=1,
\]
both inequalities are equalities. At every coordinate with \(x_k>0\), necessarily \(F_k=1\), and at every coordinate with \(x_k<0\), necessarily \(F_k=-1\). Thus, whenever \(x^+\ne0\),
\[
F^+(x^+)=\|x^+\|_1
=\|F^+\|_\infty\,\|x^+\|_1;
\]
if \(x^+=0\), the equality is trivial. The same argument with negative parts gives
\[
F^-(x^-)=\|F^-\|_\infty\,\|x^-\|_1.
\]
Scaling handles arbitrary norm-attaining pairs. Therefore \(X\) has HNAp, proving (1).

## Verification
The bundled `verify.py` checks exact rational witnesses for several geometrically different nonadditive absolute norms: a square, a Euclidean plane with rational unit coordinates, an octagonal norm, and a three-dimensional sum-of-two-largest norm. It checks every stated unit norm, supporting functional, coordinate sign pattern, dual positivity and the strict positive-part defect in rational arithmetic where applicable. It also checks the coordinatewise \(\ell_1\) equality mechanism in finite dimensions.

The finite cases illustrate (16) but do not prove the universal statement. The proof for **all** finite or countably infinite normalized \(1\)-unconditional Schauder bases is the analytic argument (5)--(16).

## Relationship to prior work
Acosta and Soleimani-Mourchehkhorti introduced HNAp in Definition 2.1 of their 2021 preprint. Their Proposition 3.4 proves HNAp for **every** absolute norm on \(\mathbb R^2\). Their Example 3.5 constructs **one** normalized three-dimensional absolute norm without HNAp by adjoining a scalar \(\ell_1\)-coordinate to a particular octagonal plane. Neither statement classifies what happens for **every** scalar \(\ell_1\)-extension, nor gives the necessary-and-sufficient condition (2) for arbitrary finite or infinite normalized \(1\)-unconditional sequence lattices.

The present theorem identifies an exact structural obstruction behind that isolated example. It shows that nonadditivity on positive disjoint basis coordinates is both necessary and sufficient for failure upon adjoining one scalar coordinate. It includes the source's example but is not merely its parameter substitution: it settles all absolute norms, all finite dimensions, and countable Schauder-basis lattices uniformly.

Work on the approximate hyperplane series property and on Bishop--Phelps--Bollobás properties of operators under absolute sums concerns different properties. In particular, finite-dimensional positive-functional Bishop--Phelps--Bollobás conclusions do not imply HNAp.

## Limitations
The theorem requires a normalized \(1\)-unconditional Schauder basis and the coordinatewise order. It does not claim a corresponding classification for atomless Banach lattices or sequence lattices such as full \(\ell_\infty\) with no Schauder basis of coordinate vectors.

The statement concerns HNAp, not the Bishop--Phelps--Bollobás property for positive functionals. The latter holds in finite-dimensional Banach lattices even when HNAp fails.

Searches of bibliographic literature and a semantic mathematical-results index cannot establish absolute priority. An equivalent characterization may appear under other terminology, especially abstract \(AL\)-space or norm additivity conditions. Independent validation has not been performed.

## References
1. M. D. Acosta and M. Soleimani-Mourchehkhorti, “Bishop--Phelps--Bollobás Property for Positive Functionals,” arXiv:2106.05935v1, first made public 10 June 2021. Definition 2.1, Proposition 3.4 and Example 3.5. Primary MSC 46B20.
2. M. D. Acosta, M. Mastyło and M. Soleimani-Mourchehkhorti, “The Bishop--Phelps--Bollobás and approximate hyperplane series properties,” arXiv:1708.08679v1 (2017). Context for operator-oriented absolute sums; not a source for the HNAp classification.
