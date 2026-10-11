# The radius-12 local correction for the eight-dimensional reciprocal Hardy field is cutoff-optimal
## Finding
Let \(\widehat a_8\) denote the rational reciprocal edge field introduced for dimension eight in arXiv:2610.05421v1. For an integer \(R\ge 1\), define
\[
S_R=\{x\in\mathbb Z^8:1\le |x|^2\le R\}.
\]
A radial finite gluing of this fixed exterior field is obtained from a positive function \(h:S_R\to(0,\infty)\) by setting \(a_{xy}=h(y)/h(x)\) when \(x,y\in S_R\), and \(a_{xy}=\widehat a_8(|x|^2,|y|^2)\) on every other nearest-neighbor edge with nonzero endpoints. Write
\[
V(x)=16-\sum_{y\sim x,\ y\ne0}a_{xy}.
\]
Then the smallest radius for which such a gluing can satisfy
\[
V(x)\ge \frac{9}{|x|^2}\qquad(x\ne0)
\]
is exactly \(R=12\). The construction in arXiv:2610.05421v1 gives existence at \(R=12\); no gluing of the stated form exists for \(R\le11\).

## Assumptions and scope
The conclusion is about the specific rational exterior field \(\widehat a_8\) of arXiv:2610.05421v1 and the paper's ratio-gluing mechanism. It is not a claim that every proof of the sharp eight-dimensional Hardy inequality must modify all vertices through squared radius \(12\), nor that the resulting Hardy weight is critical or pointwise optimal. The correction function \(h\) is allowed to be completely arbitrary and need not initially have any symmetry.

## Proof
For \(R\le10\), the lattice point \(x=(3,1,1,0,0,0,0,0)\) has \(|x|^2=11\), so every incident nonzero edge is fixed by the exterior formula. Direct exact substitution in the paper's polynomials \(P,Q\) gives
\[
V(x)=\frac{2781931677110309401598615851751229574528}{3413484844310465480119326896335674988035}
<\frac9{11},
\]
with deficit
\[
\frac9{11}-V(x)=\frac{120115150580785903489167697757549572507}{37548333287415120281312595859692424868385}>0.
\]
Hence \(R\le10\) is impossible.

It remains to rule out \(R=11\). The local inequalities are linear after multiplication by \(h(x)>0\). Put
\[
D_x=16-\frac9{|x|^2}-\sum_{y\sim x,\ |y|^2>11}\widehat a_8(|x|^2,|y|^2).
\]
For \(x\in S_{11}\), the condition \(V(x)\ge9/|x|^2\) is equivalent to
\[
D_xh(x)-\sum_{y\sim x,\ y\in S_{11}}h(y)\ge0.
\]
Averaging \(h\) over signed coordinate permutations preserves positivity and these inequalities, so it suffices to consider the 23 symmetry classes in \(S_{11}\). Let \(o_x\) be the size of the orbit of a representative \(x\), and let \(m_{xy}\) be the number of neighbors of class \(y\) of a fixed representative of class \(x\). The identity \(o_xm_{xy}=o_ym_{yx}\) makes the matrix
\[
L_{xx}=o_xD_x,\qquad L_{xy}=-o_xm_{xy}\quad(x\ne y)
\]
symmetric. A positive gluing would give \(Lh\ge0\).

For a symmetric matrix with nonpositive off-diagonal entries, \(h>0\) and \(Lh\ge0\) imply positive semidefiniteness. Indeed, with \(z_i=h_iw_i\),
\[
z^{\mathsf T}Lz
=\sum_{i<j}c_{ij}h_ih_j(w_i-w_j)^2
+\sum_i h_i(Lh)_iw_i^2\ge0,
\]
where \(c_{ij}=-L_{ij}\ge0\).

Index the 23 classes by increasing squared norm in the order printed by `verify_cutoff.py`. For
\[
z=(591,286,161,137,104,89,74,64,56,49,44,43,39,36,43,34,32,35,29,27,29,25,23)
\]
exact rational arithmetic gives
\[
z^{\mathsf T}Lz=
-\frac{4941330518990889652315877160276773708087370436319202321690429390653783570610997940240436801602}{5138952112206332908386509457548617555468212537519642055015378031597097617037276088097099625}<0.
\]
This contradicts the necessary positive-semidefiniteness and rules out \(R=11\).

For \(R=12\), the 26 positive integer values in Table 4 of arXiv:2610.05421v1 provide a gluing with strict inequalities. Re-evaluating those 26 local inequalities directly with exact fractions gives minimum local margin \(3/2019151\); the paper's exterior proposition gives strict positivity for \(|x|^2\ge13\). Therefore \(R=12\) is both sufficient and necessary.

## Verification
The standalone script `verify_cutoff.py` reconstructs the polynomials \(P,Q\), the rational field \(\widehat a_8\), all signed-permutation classes through squared radius \(12\), the published 26 local values, the \(R\le10\) witness, and the full \(23\times23\) rational matrix certificate for \(R=11\). It uses only Python's exact `Fraction` arithmetic. The script was executed from the packaged path and all assertions passed.

The exterior assertion for \(|x|^2\ge13\) is not re-proved computationally; it is the symbolic polynomial estimate in Proposition 6.2 of the focal source, whose displayed derivation was inspected. No finite enumeration is used as a substitute for that infinite exterior theorem.

## Relationship to prior work
Alpay proves the sharp value \(\lambda_8=9\) by using the same exterior field and a local correction on \(S_{12}\), but does not state that the cutoff \(12\) is minimal for this gluing mechanism. The paper explicitly leaves finding a simpler dimension-eight field and local correction as a further problem. The earlier three-dimensional reciprocal-edge construction arXiv:2608.25262v1 and Lizama's arXiv:2608.30831v1 do not contain this dimension-eight finite-gluing cutoff.

The present result is a method-level optimality statement: merely shrinking the support of the local correction while retaining the focal exterior field cannot simplify the proof. Any reduction below radius \(12\) must change the exterior field, the gluing architecture, or the pointwise certification strategy.

## Limitations
The statement does not establish global optimality of the reciprocal field, local correction values, or Hardy weight. It also does not exclude a different reciprocal field or a non-ratio proof that uses a smaller exceptional set. The originality assessment is limited by the very recent date of the focal source and the possibility of unindexed independent calculations.

## References
1. Natanael Alpay, *Sharp discrete Hardy constants in low dimensions*, arXiv:2610.05421v1, 2026.
2. Natanael Alpay, *The sharp discrete Hardy inequality on \(\mathbb Z^3\)*, arXiv:2608.25262v1, 2026.
3. Carlos Lizama, *Sharp discrete Hardy constants in dimensions three and four and strict upper bounds from dimension nine*, arXiv:2608.30831v1, 2026.
