# Every higher Segre dual has ambient Euler characteristic
## Finding
Let
\[
t\ge3,
\]
let \(V_i\) be complex vector spaces with
\[
m_i=\dim V_i\ge2,
\qquad
1\le i\le t,
\]
and let
\[
X
=
\operatorname{Seg}
\left(
\mathbb P(V_1)\times\cdots\times\mathbb P(V_t)
\right)
\subset
\mathbb P(V_1\otimes\cdots\otimes V_t).
\]
Put
\[
M=\prod_{i=1}^{t}m_i.
\]
Let
\[
X^\vee
\subset
\mathbb P((V_1\otimes\cdots\otimes V_t)^*)
\]
be the projective dual variety.

Then
\[
\boxed{
\chi_{\mathrm{top}}(X^\vee)=M.
}
\]
Since the ambient dual projective space is \(\mathbb P^{M-1}\), this is equivalently
\[
\boxed{
\chi_{\mathrm{top}}(X^\vee)
=
\chi_{\mathrm{top}}(\mathbb P^{M-1}).
}
\]

If
\[
U
=
\mathbb P((V_1\otimes\cdots\otimes V_t)^*)\setminus X^\vee,
\]
then constructible additivity gives
\[
\boxed{
\chi_c(U)=0.
}
\]

The statement does not require the dual to be a hypersurface. In the nondefective formats, where the dual is the hyperdeterminant hypersurface, it says that the hyperdeterminant has exactly the ambient Euler characteristic.

## Assumptions and scope
The base field is \(\mathbb C\).

Every factor has positive projective dimension. The theorem is stated for at least three factors because the two-factor case is the classical matrix-determinantal situation; the higher-tensor case is the new scope considered here.

The projective dual is the closure of the set of hyperplanes containing the tangent space to \(X\) at a smooth point. For a Segre variety, every point is smooth.

The Euler characteristic of the projective dual is ordinary topological Euler characteristic. The complement is quasi-projective, so its invariant is compactly supported Euler characteristic.

## Proof
Choose bases
\[
e_{i,0},\ldots,e_{i,m_i-1}
\]
of the \(V_i\). Assign a distinct nonnegative integer \(q(i,j)\) to every basis vector and let a one-parameter subgroup \(\mathbb C^*\) act by
\[
z\cdot e_{i,j}=z^{2^{q(i,j)}}e_{i,j}.
\]

A tensor-coordinate basis vector
\[
e_{1,j_1}\otimes\cdots\otimes e_{t,j_t}
\]
has weight
\[
\sum_{i=1}^{t}2^{q(i,j_i)}.
\]
Distinct coordinate tensors have distinct weights by uniqueness of binary expansion. The induced weights on the dual coordinate functionals are their negatives and are again pairwise distinct. Hence the fixed locus of the ambient dual projective space consists exactly of its \(M\) coordinate points.

Fix one such coordinate functional
\[
\phi
=
\ell_1\otimes\cdots\otimes\ell_t,
\]
where each \(\ell_i\) is a dual basis vector. We show that the corresponding hyperplane is tangent to the Segre variety.

Because
\[
\dim V_1,\dim V_2\ge2,
\]
choose nonzero vectors
\[
v_1\in\ker\ell_1,
\qquad
v_2\in\ker\ell_2.
\]
For every
\[
i\ge3,
\]
choose \(v_i\) with
\[
\ell_i(v_i)\ne0.
\]
Let
\[
p=[v_1\otimes\cdots\otimes v_t]\in X.
\]
The affine tangent space to the Segre cone at a representative of \(p\) is the sum of the spaces obtained by varying one tensor factor at a time:
\[
\sum_{i=1}^{t}
 v_1\otimes\cdots\otimes V_i\otimes\cdots\otimes v_t.
\]

The functional \(\phi\) vanishes on every summand. If the first factor varies, the second factor still contributes
\[
\ell_2(v_2)=0.
\]
If the second factor varies, the first contributes
\[
\ell_1(v_1)=0.
\]
If any later factor varies, both zero factors remain. Therefore the hyperplane \(\{\phi=0\}\) contains the projective tangent space \(T_pX\). Hence
\[
[\phi]\in X^\vee.
\]

Thus every ambient fixed point lies in the projective dual. Conversely, any fixed point of the invariant subvariety \(X^\vee\) is an ambient fixed point. Therefore
\[
(X^\vee)^{\mathbb C^*}
=
\{\text{all }M\text{ dual coordinate points}\}.
\]

For a complex algebraic variety \(Y\) with an algebraic \(\mathbb C^*\)-action,
\[
\chi_c(Y)=\chi_c(Y^{\mathbb C^*}).
\]
A singularity-free proof removes the fixed locus and applies a finite Rosenlicht stratification to the complement. After refining by stabilizer type, each nonfixed stratum is a locally trivial bundle whose fiber is a finite quotient of \(\mathbb C^*\), hence has compactly supported Euler characteristic zero. Additivity leaves only the fixed locus.

Since \(X^\vee\) is projective,
\[
\chi_{\mathrm{top}}(X^\vee)
=
\chi_c(X^\vee)
=
M.
\]
Finally,
\[
\chi_c(U)
=
\chi_{\mathrm{top}}(\mathbb P^{M-1})
-
\chi_{\mathrm{top}}(X^\vee)
=
M-M
=
0.
\]

## Verification
The bundled checker tests the finite combinatorial ingredients used by the proof for every format with
\[
3\le t\le5,
\qquad
2\le m_i\le4.
\]

It assigns disjoint powers of two to all basis coordinates and verifies that every tensor-coordinate weight is distinct. It also verifies, coordinate by coordinate, that two factors always have nontrivial kernels available for the explicit tangent-point construction.

These computations are regression evidence only. The theorem for all formats follows from uniqueness of binary expansion, the explicit tangent-space calculation, and Euler localization.

## Relationship to prior work
Segre dual varieties and hyperdeterminants are classical. Ottaviani develops the projective-dual interpretation of the hyperdeterminant, gives the tangent-space description of Segre varieties, and recalls the exact criterion for a Segre dual to be a hypersurface. Kaji studies the dual varieties of products of two or more projective spaces and gives the same nondefectivity criterion in projective-geometric form.

The present theorem concerns a different invariant: the ordinary Euler characteristic of the dual variety itself, including dual-defective formats. Targeted searches in projective-dual, hyperdeterminant, characteristic-class, and torus-fixed-point language did not locate the all-format Euler formula.

For two factors, the dual is a generic determinantal rank locus, so its Euler characteristic is already controlled by the matrix-determinantal case. The theorem is therefore stated for at least three factors, where the dual geometry is genuinely multilinear.

## Limitations
Euler characteristic is coarse. Equality with the ambient projective-space value does not imply that the projective dual has the ambient homology, dimension, singularities, or complement topology.

The vanishing
\[
\chi_c(U)=0
\]
does not mean that the complement is topologically simple; hyperdeterminant complements can have rich geometry.

The localization proof is short once the tangent behavior of coordinate multilinear forms is noticed. An older or unindexed observation in equivariant or characteristic-class treatments of hyperdeterminants remains a residual novelty risk.

## References
Giorgio Ottaviani, *Introduction to the hyperdeterminant and to the rank of multidimensional matrices*, arXiv:1301.0472, first submitted 3 January 2013.

Hajime Kaji, *On the Duals of Segre Varieties*, *Geometriae Dedicata* 99 (2003), 221--229, DOI 10.1023/A:1024968503486.
