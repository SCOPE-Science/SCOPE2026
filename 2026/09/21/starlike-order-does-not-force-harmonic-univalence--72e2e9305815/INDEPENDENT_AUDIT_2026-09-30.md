# Independent audit — 2026-09-30

**Record:** `2026/09/21/starlike-order-does-not-force-harmonic-univalence--72e2e9305815`  
**Repository:** `SCOPE-Science/SCOPE2026` at `253a0fe5d0217455660a277f9adb940030e567ad`  
**Audited tree:** `b2a6fc911d32b1beff425ab94cfb69776a776612`  
**Disposition:** **PASSED**

## Correctness

**PASS.** The construction has g'=z h', so the dilatation is omega(z)=z and Na<1 makes h' zero-free, giving positive Jacobian in the disk. The identity zh'/h-beta=(1-beta)(1-w)/(1-aw) has positive real part for |w|<1 and approaches zero radially as w->1, proving exact starlike order beta. For H=h-g, H'=(1-z)h'. The Taylor expansion at z=1 and the implicit-function theorem yield a nonreal real-level branch x(y)=c y^2+O(y^4), c=N(1-beta)/(3beta). The stated N condition is exactly c>1/2, placing the branch inside the disk; real coefficients then pair conjugate points with the same harmonic value. The nonunivalence proof is therefore sound.

## Originality

**PASS (literature-bounded).** Zhu--Huang (2015) explicitly leave the sharp starlike-order threshold open, while Nagpal--Ravichandran supply an order-zero counterexample and Hotta--Michalski study related locally one-to-one classes. Targeted searches did not locate a prior family giving counterexamples for every beta<1. Yavuz's 2009 Janowski-starlike paper is potentially adjacent, but its repository full text is embargoed until 2030 and was not read; available metadata describes a univalent sufficient subclass rather than the universal negative threshold. The verdict is pass with this explicit literature limitation.

## Scientific value

**PASS.** The result resolves the qualitative threshold question below the endpoint: increasing starlike order alone, even arbitrarily close to one, cannot force global harmonic univalence. The counterexamples are explicit and identify a geometric boundary-fold mechanism.

## Literature and evidence

- Zhu and Huang, The Distortion Theorems for Harmonic Mappings with Analytic Parts Convex or Starlike Functions of Order beta: https://doi.org/10.1155/2015/460191
- Nagpal and Ravichandran, Starlikeness, convexity and close-to-convexity of harmonic mappings: https://arxiv.org/abs/1207.3404
- Hotta and Michalski, Locally one-to-one harmonic functions with starlike analytic part: https://arxiv.org/abs/1404.1826
- Yavuz, Harmonic univalent functions with Janowski starlike analytic part: https://openaccess.iku.edu.tr/entities/publication/8c18390e-307d-40dc-9fc3-29365e174a3a

## Limitations

- The theorem rules out criteria based only on starlike order; additional hypotheses may restore univalence.
- The Yavuz 2009 full text was unavailable because the repository copy is embargoed until 2030 and was not claimed as read.
- Differently parameterized harmonic-univalence literature remains a residual priority risk.

This audit was performed independently of the same-model review. GitHub was used only as evidence; no repository write was made by the auditor.
