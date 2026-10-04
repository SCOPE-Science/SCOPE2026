# Nonattainment and parameter rigidity at the sharp pseudo-hyperbolic Bloch constant

## Finding

Let \(f\) be a nonconstant locally univalent harmonic Bloch mapping in the unit disk. Write
\[
\mathcal B_f(z)=(1-|z|^2)\Lambda_f(z)
\]
and
\[
C_0=(4+2\sqrt5)e^{-(1+\sqrt5)/2}.
\]
For every pair of distinct points \(z,w\in\mathbb D\),
\[
\frac{|\mathcal B_f(z)-\mathcal B_f(w)|}
{\|f\|_{\mathscr B_s}\rho(z,w)}
<C_0.
\]
Thus the sharp constant \(C_0\) is not attained at any genuine two-point configuration.

There is also a rigidity statement for every extremizing sequence. Suppose
\[
\|f_j\|_{\mathscr B_s}=1,
\]
orient distinct pairs \((z_j,w_j)\) so that
\[
\mathcal B_{f_j}(w_j)\ge \mathcal B_{f_j}(z_j),
\]
and assume
\[
\frac{\mathcal B_{f_j}(w_j)-\mathcal B_{f_j}(z_j)}
{\rho(z_j,w_j)}
\longrightarrow C_0.
\]
Then
\[
\rho(z_j,w_j)\longrightarrow0
\]
and
\[
\mathcal B_{f_j}(w_j)\longrightarrow
\alpha_0
=
\frac{3+\sqrt5}{2}e^{-(1+\sqrt5)/2}.
\]
Hence all near-extremizers collapse to infinitesimal point pairs and approach one distinguished normalized Bloch level.

## Assumptions and scope

The mapping is locally univalent and harmonic, exactly as in the sharp theorem used below. The Bloch seminorm is
\[
\|f\|_{\mathscr B_s}
=
\sup_{\zeta\in\mathbb D}\mathcal B_f(\zeta).
\]
The pseudo-hyperbolic distance is
\[
\rho(z,w)
=
\left|\frac{z-w}{1-\overline wz}\right|.
\]

The nonattainment claim concerns distinct points. It does not contradict sharpness of \(C_0\): the source proves sharpness by a limiting construction in which the two points coalesce.

The rigidity statement records only the two scalar parameters forced by the sharp proof. It does not claim convergence of the mappings themselves after automorphisms, rotations, or additive normalizations.

## Proof

Normalize first to
\[
\|f\|_{\mathscr B_s}=1.
\]
Orient the pair so that
\[
\mathcal B_f(z_1)\le \mathcal B_f(z_2).
\]
The source sends \(z_2\) to \(0\) by a disk automorphism and writes the preimage of \(z_1\) as \(w\). Then
\[
\rho(z_1,z_2)=|w|
\]
and
\[
\alpha=\mathcal B_f(z_2)\in(0,1].
\]
The source introduces \(m(\alpha)\ge0\) by
\[
(1+m(\alpha))e^{-m(\alpha)}=\alpha
\]
and sets
\[
a=1+m(\alpha),
\qquad
x=\frac{2|w|}{1-|w|}.
\]
Thus
\[
a\ge1,
\qquad
x>0,
\qquad
\alpha=ae^{1-a},
\qquad
|w|=\frac{x}{x+2}.
\]

Its proof gives the exact majorization
\[
\frac{\mathcal B_f(z_2)-\mathcal B_f(z_1)}{|w|}
\le
P(a,x),
\]
where
\[
P(a,x)
=
ae^{1-a}
\frac{x+2}{x}
\left[1-(1+x)e^{-ax}\right].
\]
The auxiliary lemma proves
\[
\sup_{a\ge1,\ x>0}P(a,x)=C_0.
\]

We first strengthen the last statement to pointwise strictness:
\[
P(a,x)<C_0
\qquad(a\ge1,\ x>0).
\]
Indeed, the source proves that \(P\) has no critical point in the open region
\[
a>1,\qquad x>0.
\]
If \(P(a,x)=C_0\) at a point with \(a>1\), that point would be a global interior maximum and hence a critical point, a contradiction. If \(a=1\), the source computes
\[
\partial_a\log P(1,x)>0,
\]
so \(P\) increases when one moves right from the boundary \(a=1\); equality with the global supremum there would therefore force values larger than \(C_0\), again impossible. Hence \(P<C_0\) everywhere in the finite parameter domain.

For distinct \(z_1,z_2\) we have \(x>0\), so
\[
\frac{\mathcal B_f(z_2)-\mathcal B_f(z_1)}
{\rho(z_1,z_2)}
\le
P(a,x)
<
C_0.
\]
Scaling back by the Bloch seminorm proves nonattainment.

Now consider an extremizing sequence. Define
\[
\alpha_j=\mathcal B_{f_j}(w_j),
\qquad
a_j=1+m(\alpha_j),
\qquad
x_j=\frac{2\rho(z_j,w_j)}
{1-\rho(z_j,w_j)}.
\]
The same proof gives
\[
\frac{\mathcal B_{f_j}(w_j)-\mathcal B_{f_j}(z_j)}
{\rho(z_j,w_j)}
\le
P(a_j,x_j)
\le C_0.
\]
The left side tends to \(C_0\), so
\[
P(a_j,x_j)\longrightarrow C_0.
\]

The source supplies three boundary facts about \(P\):

1. as \(a\to\infty\),
\[
\sup_{x>0}P(a,x)\longrightarrow0;
\]

2. as \(x\to\infty\),
\[
\limsup_{x\to\infty}\sup_{a\ge1}P(a,x)\le1<C_0;
\]

3. on each compact \(a\)-interval,
\[
P(a,x)\longrightarrow
B(a)=2a(a-1)e^{1-a}
\]
uniformly as \(x\downarrow0\), and \(B\) has the unique maximizer
\[
a_0=\frac{3+\sqrt5}{2},
\qquad
B(a_0)=C_0.
\]

The first fact keeps \(a_j\) bounded. The second keeps \(x_j\) bounded above. If \(x_j\) failed to tend to zero, some subsequence would lie in a compact rectangle
\[
1\le a\le A,
\qquad
\delta\le x\le R.
\]
A further subsequence would converge to a finite point \((a_*,x_*)\), and continuity would give
\[
P(a_*,x_*)=C_0,
\]
contradicting pointwise strictness. Therefore
\[
x_j\to0.
\]

Because the \(a_j\) remain in a compact interval and \(P(\cdot,x)\to B\) uniformly there,
\[
B(a_j)\longrightarrow C_0.
\]
The uniqueness of the maximizer of \(B\) forces
\[
a_j\longrightarrow a_0.
\]
Finally,
\[
\rho(z_j,w_j)=\frac{x_j}{x_j+2}\longrightarrow0
\]
and
\[
\alpha_j=a_je^{1-a_j}
\longrightarrow
a_0e^{1-a_0}
=
\frac{3+\sqrt5}{2}e^{-(1+\sqrt5)/2}.
\]
This is the claimed rigidity.

## Verification

Every step uses the actual scalar majorant in the sharp proof. The critical source facts were checked directly in the full primary text:

- the transformation from a point pair to
\[
a=1+m(\alpha),
\qquad
x=\frac{2\rho}{1-\rho};
\]

- the bound of the normalized Bloch difference by \(P(a,x)\);

- absence of critical points of \(P\) in \(a>1,\ x>0\);

- positivity of the right derivative at \(a=1\);

- the large-\(a\) and large-\(x\) bounds;

- compact-uniform convergence
\[
P(a,x)\to B(a)
\]
as \(x\downarrow0\);

- the unique maximizer
\[
a_0=(3+\sqrt5)/2
\]
of \(B\);

- the sharpness family in the source, which approaches \(C_0\) precisely through \(x\downarrow0\) at \(a=a_0\).

No numerical sampling is used to prove strictness or sequence rigidity. Compactness and continuity supply the only subsequence argument.

## Relationship to prior work

The motivating 2026 paper proves the sharp constant
\[
C_0=(4+2\sqrt5)e^{-(1+\sqrt5)/2}
\]
for locally univalent harmonic Bloch mappings and demonstrates sharpness using an analytic function with pairs whose pseudo-hyperbolic separation tends to zero. The paper does not state that equality is impossible for every distinct pair, nor does it classify the scalar degeneration of arbitrary extremizing sequences.

Huang, Rasila, and Zhu previously proved pseudo-hyperbolic Lipschitz continuity for harmonic Bloch mappings with a larger nonsharp constant and posed the optimal-constant problem. That theorem establishes boundedness of the ratio, not behavior at the sharp boundary.

Chen, Hamada, and Zhu established the sharp analytic Bloch constant
\[
3\sqrt3/2
\]
in a related, but different, analytic problem. Their result does not imply the harmonic locally-univalent constant \(C_0\), its nonattainment, or the parameter rigidity above.

Targeted searches for nonattainment, extremizing sequences, near-saturation, and pseudo-hyperbolic Bloch rigidity did not locate a statement equivalent to the present one.

## Limitations

The theorem identifies forced degeneration of the source proof parameters, not a complete compactness theorem for the functions \(f_j\). In particular, it does not prove that every extremizing sequence converges, after normalization, to the source's explicit analytic sharpness function.

The result concerns the locally univalent harmonic Bloch theorem. It does not extend here to the source's \((K,K_0)\)-quasiregular Bloch-type estimates, whose constants are only asymptotically sharp in the stated parameter limit.

The literature comparison cannot rule out an equivalent observation expressed under substantially different extremal-function terminology, although none was found in the inspected primary source, the directly related earlier papers, or the targeted searches.

## References

1. S. Chen, H. Hamada, M. Huang, and L. Jin, *The sharp Lipschitz continuity problem with respect to the pseudo hyperbolic metric*, arXiv:2609.33140v1, 2026.
2. J. Huang, A. Rasila, and J.-F. Zhu, *Lipschitz property of harmonic mappings with respect to pseudo-hyperbolic metric*, Analysis Mathematica 48 (2022), 1069--1080; arXiv:2104.05976.
3. S. Chen, H. Hamada, and J.-F. Zhu, *Composition operators on Bloch and Hardy type spaces*, arXiv:2207.03788; Mathematische Zeitschrift 304 (2023), Article 25.
