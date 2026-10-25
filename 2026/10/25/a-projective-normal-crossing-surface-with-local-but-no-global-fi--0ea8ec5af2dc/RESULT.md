# A projective normal-crossing surface with local but no global first-order deformations

## Finding

Work over \(\mathbb C\). Let \(S=\mathbb F_1=\operatorname{Bl}_p\mathbb P^2\), and let \(E\cong\mathbb P^1\) be its exceptional curve. Identify the exceptional curves in two copies \(S_1,S_2\) by the identity and form the projective pushout \(X=S_1\cup_E S_2\). Then \(X\) is a simple-normal-crossing surface and

\[
\mathcal T_X^1:=\mathcal E xt^1_{\mathcal O_X}(\Omega_X^1,\mathcal O_X)\cong\mathcal O_E(-2)\ne0,
\qquad
\operatorname{Ext}^1_{\mathcal O_X}(\Omega_X^1,\mathcal O_X)=0.
\]

Thus the local first-order deformation sheaf has positive-dimensional support, but the global first-order deformation space vanishes.

## Assumptions and scope

The base field is \(\mathbb C\). The curve \(E\) is the exceptional \((-1)\)-curve on each copy of \(\mathbb F_1\), so its normal bundle in either component is \(\mathcal O_E(-1)\). The pushout is taken in schemes, identifying the two Cartier divisors and their structure sheaves. The claim concerns first-order deformations of the projective scheme \(X\) itself, represented by the global group \(\operatorname{Ext}^1_{\mathcal O_X}(\Omega_X^1,\mathcal O_X)\). It makes no claim about deformations of the affine cone over \(X\).

## Proof

**Projectivity and the normal-crossing structure.** The pushout of the two smooth surfaces along the identified Cartier divisors has local model \(uv=0\) along \(E\), hence is simple normal crossing. By adjunction, \((-K_S)\cdot E=1\), so \((-K_S)|_E\cong\mathcal O_E(1)\). The two ample anticanonical line bundles therefore glue to a line bundle \(L\) on \(X\). Its pullback to the finite normalization \(S_1\sqcup S_2\to X\) is ample; ampleness descends under a finite surjective morphism, so \(L\) is ample and \(X\) is projective.

**The local deformation sheaf.** For a simple normal-crossing union of two smooth components meeting along \(E\), the double-locus formula gives
\[
\mathcal T_X^1\cong N_{E/S_1}\otimes N_{E/S_2}.
\]
Each normal bundle is \(\mathcal O_E(-1)\), hence \(\mathcal T_X^1\cong\mathcal O_E(-2)\). This is a nonzero sheaf supported on the one-dimensional curve \(E\), while \(H^0(X,\mathcal T_X^1)=H^0(\mathbb P^1,\mathcal O(-2))=0\).

**Vanishing of \(H^1(X,T_X)\).** Write \(T_S(-\log E)\) for vector fields on \(S\) tangent to \(E\). The standard tangent sequence is
\[
0\longrightarrow T_S(-\log E)\longrightarrow T_S\longrightarrow N_{E/S}\longrightarrow0.
\]
First, \(H^1(S,T_S)=0\). Indeed, for the ruling \(\pi:S\to\mathbb P^1\), the relative tangent bundle satisfies
\[
\pi_*T_{S/\mathbb P^1}\cong\mathcal O\oplus\mathcal O(1)\oplus\mathcal O(-1),
\qquad R^1\pi_*T_{S/\mathbb P^1}=0.
\]
Thus \(H^1(S,T_{S/\mathbb P^1})=0\). Also \(H^1(S,\pi^*T_{\mathbb P^1})=H^1(\mathbb P^1,\mathcal O(2))=0\); the relative tangent sequence gives \(H^1(S,T_S)=0\). Since \(H^0(E,N_{E/S})=H^0(\mathbb P^1,\mathcal O(-1))=0\), the tangent sequence above implies \(H^1(S,T_S(-\log E))=0\).

The restriction map \(H^0(S,T_S(-\log E))\to H^0(E,T_E)\) is surjective: projective automorphisms of \(\mathbb P^2\) fixing \(p\) lift to the blow-up and induce all projective automorphisms of \(E\cong\mathbb P^1\). The tangent sheaf of the pushout consequently fits into the exact sequence
\[
0\longrightarrow T_X\longrightarrow T_{S_1}(-\log E)\oplus T_{S_2}(-\log E)
\longrightarrow T_E\longrightarrow0,
\]
where the last map is the difference of the two restrictions. The preceding vanishing and surjectivity give \(H^1(X,T_X)=0\).

**Global first-order deformations.** Since \(X\) is locally complete intersection, the local-to-global Ext sequence contains
\[
0\longrightarrow H^1(X,T_X)\longrightarrow
\operatorname{Ext}^1_{\mathcal O_X}(\Omega_X^1,\mathcal O_X)
\longrightarrow H^0(X,\mathcal T_X^1)\longrightarrow H^2(X,T_X).
\]
Both groups adjacent to the global Ext group on the left vanish: \(H^1(X,T_X)=0\) and \(H^0(X,\mathcal T_X^1)=0\). Exactness forces \(\operatorname{Ext}^1_{\mathcal O_X}(\Omega_X^1,\mathcal O_X)=0\), as claimed.

## Verification

The computation uses only the normal bundle of the exceptional curve, the relative tangent sequence of \(\mathbb F_1\to\mathbb P^1\), and the local-to-global Ext sequence. The key values are \(N_{E/S_i}=\mathcal O_E(-1)\), \(H^0(E,\mathcal O_E(-2))=0\), and \(H^1(X,T_X)=0\). No finite enumeration is used. The conclusion is about the global first-order deformation group of \(X\), not about higher-order deformations or the affine cone.

## Relationship to prior work

Nisse, *On infinitesimal deformations of singular varieties I*, Lemma 4.2, §4.2, states a projective implication from positive-dimensional support of \(\mathcal T_X^1\) to nonvanishing of a global \(T^1\), and its argument passes through a positively twisted Ext group and then discusses the affine cone. The example here shows that the implication does not hold for \(\operatorname{Ext}^1_{\mathcal O_X}(\Omega_X^1,\mathcal O_X)\) on the projective scheme itself: the local sheaf is nonzero, but its global sections and the global Ext group vanish. This does not address the separate deformation space of the affine cone or the affine case.

Tziolas, *First order deformations of schemes with normal crossing singularities*, Theorem 1.1, supplies the double-locus formula for \(\mathcal T_X^1\). The normal-bundle product is exactly what yields \(\mathcal O_E(-2)\) in this example. The comparison is at the level of statements and implications, not merely matching terminology.

## Limitations

This is one projective simple-normal-crossing example. It refutes the stated implication without additional hypotheses; it does not claim that positive-dimensional local deformation support usually fails to globalize, nor that every deformation of the affine cone is trivial. It establishes only first-order global rigidity for \(X\), not formal or analytic rigidity to all orders.

## References

1. Mounir Nisse, “On infinitesimal deformations of singular varieties I,” arXiv:2512.13203v1, submitted 2025-12-15, especially §4, Lemma 4.2 and Remark 4.3. https://arxiv.org/abs/2512.13203
2. Nikolaos Tziolas, “First order deformations of schemes with normal crossing singularities,” arXiv:1007.3038v1, especially Theorem 1.1 and Corollary 2.3. https://arxiv.org/abs/1007.3038
