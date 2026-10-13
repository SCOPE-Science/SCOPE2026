# The projective principal-minor variety has ambient Euler characteristic
## Finding
For every integer
\[
n\ge4,
\]
let
\[
\mathcal V_n\subset\mathbb P((\mathbb C^2)^{\otimes n})\cong\mathbb P^{2^n-1}
\]
be the projective principal-minor variety introduced by Lin and Sturmfels. Equivalently, this is the projective variety of determinantal points studied earlier by Borodin and Rains.

Then
\[
\boxed{
\chi_{\mathrm{top}}(\mathcal V_n)=2^n.
}
\]
Thus the projective principal-minor variety has exactly the same ordinary Euler characteristic as its ambient projective space:
\[
\boxed{
\chi_{\mathrm{top}}(\mathcal V_n)
=
\chi_{\mathrm{top}}(\mathbb P^{2^n-1}).
}
\]
Equivalently,
\[
\boxed{
\chi_c\!\left(\mathbb P^{2^n-1}\setminus\mathcal V_n\right)=0.
}
\]

The same identity also holds for \(n=1,2,3\); in those dimensions the determinantal-point variety is the whole ambient projective space. The nontrivial content begins at \(n=4\), where \(\mathcal V_4\subset\mathbb P^{15}\) is the codimension-two degree-\(28\) node component of the \(2\times2\times2\times2\) hyperdeterminant singular locus.

## Assumptions and scope
Everything is over \(\mathbb C\).

Lin and Sturmfels define a projective map by taking two \(n\times n\) matrices \(A,B\), viewing \((A,B)\) as an \(n\times2n\) matrix, and setting
\[
\phi(A,B)_I
=
\det(A_I\,B_{[n]\setminus I})
\qquad(I\subseteq[n]),
\]
where the selected \(n\) columns use column \(i\) from \(A\) when \(i\in I\) and column \(i\) from \(B\) otherwise. Their image is a closed affine cone, hence determines the projective variety \(\mathcal V_n\).

The theorem concerns ordinary topological Euler characteristic of this projective variety and compactly supported Euler characteristic of its complement. It does not determine Betti numbers, Hodge numbers, intersection cohomology, singularities, degree, or the defining ideal.

## Proof
Lin and Sturmfels record that \(\mathcal V_n\) is invariant under the natural action of
\[
G=\operatorname{GL}_2(\mathbb C)^n
\]
on
\[
(\mathbb C^2)^{\otimes n}.
\]
Borodin and Rains prove the same invariance for their determinantal-point variety.

Choose, in the \(i\)-th \(\operatorname{GL}_2\)-factor, the one-parameter subgroup
\[
\lambda_i(t)=
\begin{pmatrix}
t^{2^{i-1}}&0\\
0&1
\end{pmatrix}.
\]
Their product gives a one-parameter subgroup
\[
\lambda:\mathbb C^*\longrightarrow G.
\]
On the standard tensor basis indexed by subsets
\[
I\subseteq[n],
\]
the weight is
\[
w_I=\sum_{i\in I}2^{i-1}.
\]
Binary expansion makes all \(2^n\) weights distinct. Therefore the fixed locus of the ambient projective space is exactly the set of its \(2^n\) tensor-coordinate points
\[
[e_I],\qquad I\subseteq[n].
\]

Every one of these coordinate points belongs to \(\mathcal V_n\). Indeed, take diagonal matrices
\[
A=\operatorname{diag}(a_1,\ldots,a_n),
\qquad
B=\operatorname{diag}(b_1,\ldots,b_n).
\]
Then
\[
\phi(A,B)_I
=
\prod_{i\in I}a_i
\prod_{i\notin I}b_i.
\]
Hence diagonal pairs trace out the standard Segre variety
\[
(\mathbb P^1)^n
\hookrightarrow
\mathbb P((\mathbb C^2)^{\otimes n})
\]
inside \(\mathcal V_n\). In particular, for a prescribed subset \(I_0\), choosing
\[
(a_i,b_i)=
\begin{cases}
(1,0),&i\in I_0,\\
(0,1),&i\notin I_0
\end{cases}
\]
gives exactly the coordinate point \([e_{I_0}]\).

Because \(\mathcal V_n\) is \(\lambda\)-invariant, its fixed locus is the intersection with the ambient fixed locus. Since every ambient fixed point lies in \(\mathcal V_n\),
\[
\mathcal V_n^{\mathbb C^*}
=
\{[e_I]:I\subseteq[n]\},
\]
so
\[
\#\mathcal V_n^{\mathbb C^*}=2^n.
\]

For any complex algebraic variety carrying an algebraic \(\mathbb C^*\)-action,
\[
\chi_c(X)=\chi_c(X^{\mathbb C^*}).
\]
Since \(\mathcal V_n\) is projective,
\[
\chi_{\mathrm{top}}(\mathcal V_n)=\chi_c(\mathcal V_n)=2^n.
\]
Finally,
\[
\chi_{\mathrm{top}}(\mathbb P^{2^n-1})=2^n,
\]
so additivity of \(\chi_c\) yields
\[
\chi_c\!\left(\mathbb P^{2^n-1}\setminus\mathcal V_n\right)=0.
\]

## Verification
The bundled checker independently verifies two finite ingredients of the proof.

First, for every
\[
1\le n\le16,
\]
it checks that the powers-of-two one-parameter subgroup gives pairwise distinct weights on all \(2^n\) tensor-coordinate lines.

Second, for every
\[
1\le n\le10
\]
and every target subset \(I_0\subseteq[n]\), it evaluates the diagonal specialization
\[
\phi(A,B)_I
=
\prod_{i\in I}a_i\prod_{i\notin I}b_i
\]
with \((a_i,b_i)=(1,0)\) on \(I_0\) and \((0,1)\) outside \(I_0\), confirming that exactly the coordinate \(I_0\) survives.

These finite checks are regression evidence only. The all-parameter theorem is proved by binary uniqueness, the exact diagonal formula, group invariance, and Euler localization.

## Relationship to prior work
Borodin and Rains introduced the projective determinantal-point variety and proved its invariance under \(\operatorname{GL}_2(\mathbb C)^n\rtimes S_n\). They also proved that it fills the ambient space for \(n\le3\), determined its dimension in all dimensions, and characterized the first nontrivial case \(n=4\) as the node component of the hyperdeterminant singular locus.

Lin and Sturmfels independently developed the projective principal-minor model, explicitly defined the polynomial map \(\phi\), proved that its image is a closed cone, recorded the same \(\operatorname{GL}_2^n\)-invariance, and studied the difficult defining ideal. Their full text contains no occurrence of “Euler”, “Poincaré”, “topolog”, or “fixed point”. The Borodin--Rains full text likewise contains no Euler- or Poincaré-type computation.

Targeted semantic-database and web searches for the principal-minor variety, determinantal points, Euler characteristic, topology, Poincaré polynomial, and torus fixed points did not locate the formula above.

A previously known special object is the projective variety of principal minors of symmetric matrices. It is a proper subvariety of the general projective principal-minor variety in the nontrivial range and also has Euler characteristic \(2^n\). That equality does not imply the present theorem: Euler characteristic is not monotone under inclusion, and the general principal-minor variety has substantially larger dimension and a different defining ideal. The present fixed-locus argument establishes the invariant directly for the general determinantal-point variety.

## Limitations
Euler characteristic is a coarse invariant. Equality with the ambient Euler characteristic does not imply homotopy equivalence, equality of Betti or Hodge numbers, or equality of motives.

The complement can be highly nontrivial despite its vanishing compactly supported Euler characteristic.

The proof is short once the \(\operatorname{GL}_2^n\)-invariance and the diagonal Segre locus are put together. An unindexed or folklore observation therefore remains a residual originality risk.

## References
Alexei Borodin and Eric M. Rains, *Eynard--Mehta theorem, Schur process, and their Pfaffian analogs*, arXiv:math-ph/0409059, first submitted 21 September 2004; *Journal of Statistical Physics* 121 (2005), 291--317, DOI 10.1007/s10955-005-7583-z.

Shaowei Lin and Bernd Sturmfels, *Polynomial relations among principal minors of a \(4\times4\)-matrix*, arXiv:0812.0601, first submitted 2 December 2008; *Journal of Algebra* 322 (2009), 4121--4131, DOI 10.1016/j.jalgebra.2009.06.026.
