# Disproof: a spin b⁺=1 H⁺-reversing bound does not force the expected Floer local classes

## Context

Let W be a compact oriented spin 4-manifold with boundary Y an integer homology
sphere, b₁(W)=0, b⁺(W)=1, σ(W)<0. Let f:W→W be orientation-preserving,
spin-preserving, reversing the orientation of H⁺(W), and restricting to an
orientation-preserving diffeomorphism φ:Y→Y. The admitted target question asks
whether this data implies

h_τ(Y,φ) ≠ 0 and h_{ι∘τ}(Y,ι∘φ) = 0

in the τ / ι∘τ-local equivalence group, where τ is the map induced by φ on
CF⁻(Y) and ι is the conjugation involution. This generalizes the type of
Floer-theoretic extension obstruction studied in cork and involutive Heegaard
Floer theory (Dai–Hedden–Mallick; Hendricks–Manolescu–Zemke).

## Definitions

- N denotes the −E₈ plumbing: compact, oriented, simply connected, spin,
  intersection form −E₈, boundary P the Poincaré integer homology sphere.
- S = S²×S² with its unique spin structure; H denotes its intersection form
  [[0,1],[1,0]] with positive line ℝ·(1,1).
- r:S²→S² is a reflection (e.g. (x,y,z)↦(−x,y,z)); g = r×r:S→S.
- h_τ(Y,φ) = [(CF⁻(Y),τ)] and h_{ι∘τ}(Y,ι∘φ) = [(CF⁻(Y),ι∘τ)] are the
  equivariant local-equivalence classes; [(C,τ)]↦[C] is the forgetful map to
  ordinary local equivalence. d(Y) is the Ozsváth–Szabó correction term.

## Result

**Answer: No. The implication is false.** The pair

W = N # S, f = id_N # g

satisfies every geometric hypothesis, has ∂W = P, b₁(W)=0, b⁺(W)=1,
σ(W)=−8<0, f orientation- and spin-preserving, H⁺-reversing, with
φ = f|_P = id_P, yet

h_τ(P,id) ≠ 0 and h_{ι∘τ}(P,ι) ≠ 0,

so the claimed conjunction “≠0 and =0” fails. In particular the required
vanishing h_{ι∘τ}=0 does not hold.

## Proof / evidence

1. **Topology of W.** Interior connected sum gives intersection form
   Q_W = (−E₈)⊕H, hence b⁺(W)=0+1=1 and σ(W)=−8+0=−8. W is compact oriented
   spin with ∂W=P and b₁(W)=0. Eigenvalue computation confirms b⁺=1, σ=−8;
   see `artifacts/counterexample_linear_algebra.py`.
2. **The diffeomorphism.** g=r×r is an orientation-preserving involution
   (deg r=−1, so deg g=(−1)²=+1) acting on H₂(S;ℤ)≅ℤ² as diag(−1,−1)=−id,
   negating the positive vector (1,1). S is simply connected so its spin
   structure is unique and preserved by g. The fixed set of g is the torus
   S¹×S¹, hence nonempty; near a fixed point a small ball B⊂S is g-invariant,
   allowing the equivariant connected sum f=id_N#g. Since H¹(W;ℤ/2)=0, W has
   a unique spin structure, preserved by f. By construction f is the identity
   near ∂W, so φ=id_P.
3. **H⁺-reversal.** Q_W(v_e+v_h)=−‖v_e‖²+Q_H(v_h), so positivity is controlled
   by the H summand; f_*=id⊕(−id) sends the positive line ℝ·(1,1) to its
   negative, reversing the orientation of H⁺(W).
4. **Floer consequence.** With φ=id, τ≃id and ι∘τ≃ι, so the classes are
   [(CF⁻(P),id)] and [(CF⁻(P),ι)]. Equivariant local maps are in particular
   ordinary local maps, so equivariant vanishing implies ordinary vanishing.
   Contrapositively, ordinary nontriviality forces both equivariant classes
   nonzero. The Poincaré sphere has d(P)=±2≠0 (either orientation, standard
   plumbing computation), so [CF⁻(P)]≠0 ordinarily. Hence both equivariant
   classes are nonzero, contradicting the claimed vanishing.

## Limitations

The disproof uses standard cited computations as black boxes: the −E₈ plumbing
is spin with integer-homology-sphere boundary; S²×S² has a unique spin
structure; d of either orientation of the Poincaré sphere is ±2
(Ozsváth–Szabó); equivariant connected-sum gluing uses an invariant ball from
an averaged metric near a fixed point. No new Floer computation beyond the
forgetful-homomorphism argument is claimed.

## Reproducibility

Run `artifacts/counterexample_linear_algebra.py` (requires numpy) to verify
Q=(−E₈)⊕H has b⁺=1, σ=−8, −E₈ negative-definite, and −id on the H summand
negates the positive line. The Floer step follows from the cited d-invariant
value and the forgetful-map argument above.

## References

- I. Dai, M. Hedden, A. Mallick, Corks, involutions, and Heegaard Floer
  homology, J. Eur. Math. Soc. (2022); arXiv:2002.02326.
- K. Hendricks, C. Manolescu, Involutive Heegaard Floer homology,
  Duke Math. J. (2017).
- K. Hendricks, J. Hom, T. Lidman, Applications of involutive Heegaard Floer
  homology, J. Inst. Math. Jussieu.
- I. Dai, C. Manolescu, Involutive Heegaard Floer homology and plumbed
  three-manifolds, J. Inst. Math. Jussieu.
- P. Ozsváth, Z. Szabó, Absolutely graded Floer homologies and intersection
  forms for four-manifolds with boundary.
