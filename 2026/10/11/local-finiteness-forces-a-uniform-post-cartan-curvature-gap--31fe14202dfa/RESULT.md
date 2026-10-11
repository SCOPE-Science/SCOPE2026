# Local finiteness forces a uniform post-Cartan curvature gap

## Finding

For an integer
\[
n\ge5,
\]
let
\[
\mathcal E_n^{(3)}
\]
denote the set of constants
\[
S=|A|^2
\]
realized by closed connected embedded minimal hypersurfaces
\[
M^n\subset S^{n+1}(1)
\]
for which both \(S\) and
\[
f_3=\operatorname{tr}(A^3)
\]
are constant.

There exists a number
\[
\delta_n>0,
\]
depending only on \(n\), such that every
\[
S\in\mathcal E_n^{(3)},\qquad S>n,
\]
satisfies
\[
\boxed{
S=2n
\quad\text{or}\quad
S\ge2n+\delta_n.
}
\]

Moreover,
\[
S=2n
\]
occurs if and only if
\[
n\in\{6,12,24\},
\]
and every equality image is a minimal Cartan isoparametric hypersurface with three principal curvatures.

Hence, in every dimension
\[
n\ge5,\qquad n\notin\{6,12,24\},
\]
the sharp second-gap theorem automatically upgrades, on the embedded constant-\(f_3\) class, to a strictly larger dimension-dependent gap:
\[
\boxed{
S>n
\quad\Longrightarrow\quad
S\ge2n+\delta_n.
}
\]

A concrete admissible definition is
\[
\boxed{
\delta_n
=
\min\!\left(
\{s-2n:
s\in\mathcal E_n^{(3)},\
2n<s\le2n+1\}
\cup\{1\}
\right).
}
\]

Thus the Cartan curvature level is not merely an endpoint of the second gap: within this embedded class it is an isolated spectral level, uniformly in topology and in the constant value of \(f_3\).

## Assumptions and scope

The hypersurface is closed, connected, smooth, embedded, and minimal in the unit sphere. The quantities
\[
S=|A|^2
\quad\text{and}\quad
f_3=\operatorname{tr}(A^3)
\]
are spatially constant.

The embeddedness assumption is essential to the local-finiteness theorem used here. The sharp second-gap theorem itself applies more broadly to immersions, but the post-\(2n\) isolation proved here is asserted only for the embedded class.

The constant \(\delta_n\) is existential and dimension-dependent. No explicit numerical lower bound for it is claimed.

The statement is restricted to
\[
n\ge5.
\]
This avoids importing separate low-dimensional classification theorems into the claim.

## Proof

Tan, Tang, Xie, and Yan prove that for each fixed \(n\ge2\) and every finite
\[
\Lambda\ge0,
\]
the set
\[
\mathcal E_n^{(3)}\cap[0,\Lambda]
\]
is finite.

Fix
\[
n\ge5.
\]
Apply that theorem with
\[
\Lambda=2n+1.
\]
Then
\[
F_n
=
\mathcal E_n^{(3)}\cap(2n,2n+1]
\]
is finite. Therefore the set
\[
D_n
=
\{s-2n:s\in F_n\}\cup\{1\}
\]
is a nonempty finite set of positive real numbers. Define
\[
\delta_n=\min D_n.
\]
It follows immediately that
\[
\delta_n>0.
\]

Now let
\[
S\in\mathcal E_n^{(3)}
\]
with
\[
S>2n.
\]
If
\[
S\le2n+1,
\]
then
\[
S-2n\in D_n
\]
and hence
\[
S-2n\ge\delta_n.
\]
If instead
\[
S>2n+1,
\]
then
\[
S-2n>1\ge\delta_n.
\]
Thus every admissible value strictly above \(2n\) satisfies
\[
S\ge2n+\delta_n.
\]

Ge, Tan, Yan, and Zhang prove, under the same constant-\(S\), constant-\(f_3\) assumptions and for
\[
n\ge5,
\]
that
\[
S>n
\quad\Longrightarrow\quad
S\ge2n.
\]
They also prove that equality
\[
S=2n
\]
holds exactly when the image is a minimal Cartan isoparametric hypersurface with three principal curvatures, and that these equality cases occur only in dimensions
\[
n\in\{6,12,24\}.
\]

Combining the sharp second-gap theorem with the preceding isolation of all values strictly above \(2n\) gives
\[
S>n
\quad\Longrightarrow\quad
S=2n
\ \text{or}\
S\ge2n+\delta_n.
\]
The equality classification gives the remaining assertions.

## Verification

The proof has no numerical or finite-enumeration component.

The first source was inspected in full around its definition of
\[
\mathcal E_n^{(3)}
\]
and Theorem 1.1, which states finiteness of
\[
\mathcal E_n^{(3)}\cap[0,\Lambda]
\]
for every finite \(\Lambda\).

The second source was inspected in full around Theorem 1.1 and its introduction. It states the sharp implication
\[
S>n\Longrightarrow S\ge2n
\]
for \(n\ge5\), and classifies the equality images as the minimal Cartan hypersurfaces, occurring in dimensions
\[
6,\ 12,\ 24
\]
in the stated range.

The only new proof step is set-theoretic: a finite subset of
\[
(2n,2n+1]
\]
has a positive minimum distance from \(2n\), after adjoining the harmless fallback value \(1\).

No claim is made that the displayed \(\delta_n\) is explicitly computable from the currently available theorems, or that it is the largest possible post-Cartan gap.

## Relationship to prior work

The local-finiteness paper proves a global discreteness statement for the embedded constant-\(f_3\) class: for fixed dimension, only finitely many admissible \(S\)-values occur in every bounded interval. Its introduction distinguishes this from pinching theorems, which locate the first few admissible levels.

The later second-gap paper proves the exact location of the next level above \(n\): no admissible value lies in
\[
(n,2n),
\]
and the endpoint
\[
2n
\]
is realized precisely by the Cartan \(g=3\) examples in the allowed dimensions.

The two inspected primary texts discuss these ingredients separately. The later paper explicitly cites local finiteness as background, but its stated consequence at the upper endpoint is only
\[
S>2n
\]
outside the Cartan dimensions. It does not state a dimension-dependent uniform positive distance above \(2n\).

The present result combines the global local-finiteness theorem with the sharp endpoint classification to convert that strict inequality into a uniform post-Cartan gap. Targeted searches for a post-Cartan gap, an isolated \(2n\) level, and an \(\varepsilon_n\)-strengthening under constant cubic trace did not locate a published statement of this consequence.

## Limitations

The theorem supplies existence of
\[
\delta_n>0
\]
but no explicit numerical estimate.

It does not identify the next admissible curvature value above \(2n\), nor assert that such a value exists.

The conclusion uses embedded local finiteness and therefore does not extend, from the cited results alone, to arbitrary immersed hypersurfaces.

Nothing is asserted about hypersurfaces for which \(f_3\) is nonconstant.

## References

1. Huixin Tan, Zizhou Tang, Yuquan Xie, and Wenjiao Yan, *Chern's Conjecture with Constant Cubic Trace*, arXiv:2609.03711v1, first submitted 3 September 2026.
2. Jianquan Ge, Huixin Tan, Wenjiao Yan, and Yunheng Zhang, *The Second Gap and Rigidity in Chern's Conjecture with Constant Cubic Trace*, arXiv:2609.27661v1, first submitted 23 September 2026.
