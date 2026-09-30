# Independent Audit — 2026/09/13/036

**Audit date:** 2026-09-28 (UTC)  
**Audited tree:** `c2b2d60d5dc923a2ac56501ae292875ea861c1e5`  
**Disposition:** **PASSED**

## Correctness

**Verdict:** PASS  
The presheaf-type obstruction is valid. In any nonempty model of DLO with an antitone involution, choose a with a<f(a); the open interval I(a)=(a,f(a)) is a proper f-closed DLO submodel. These intervals form a directed family and cover the model: for any b, choose a<min(b,f(b)), which forces b∈I(a). Hence the identity of a nonempty model cannot factor through any stage of this directed colimit, so no nonempty model is finitely presentable. The empty model is the only finitely presentable model if empty structures are allowed (otherwise fpMod is empty). There are nevertheless at least two nonisomorphic nonempty Set-models, for example Q with q↦−q and a fixed-point-free involution obtained by pairing the two rational cuts around an irrational. Therefore the classifying topos cannot be the presheaf topos on fpMod under either empty-model convention.

## Originality

**Verdict:** PASS  
The nearest general literature says ordinary decidable linear orders are of presheaf type and their homogeneous models are DLO; that result does not cover the expansion by an order-reversing involution and points in the opposite direction. Targeted searches for antitone/order-reversing involutions together with presheaf-type/classifying-topos terminology found no prior statement of the fp-triviality argument or the resulting non-presheaf classification. The directed-interval construction is a specific new obstruction, not a parameter substitution into the plain-linear-order theorem.

## Scientific value

**Verdict:** PASS  
This gives a clean structural boundary for a standard topos-theoretic classification program: a natural symmetry expansion of DLO destroys presheaf type because all nonempty models fail finite presentability. The obstruction is conceptual, applies to every model rather than a finite sample, and supplies explicit contrasting points, so it has standalone mathematical use beyond target triage.

## Evidence

- [Caramello, Topos-theoretic Fraïssé construction examples](https://www.oliviacaramello.com/Unification/Concrete%20examples/Fraisse.html): Shows ordinary decidable linear orders are of presheaf type and their homogeneous Set-models are DLO; it does not cover the antitone-involution expansion.
- [nLab, theory of presheaf type](https://ncatlab.org/nlab/show/theory+of+presheaf+type): General background on presheaf-type theories and finitely presentable models; no specific involutive-DLO result was located.

## Independent checks

- Re-derived f-closure, properness, directedness, and covering for the intervals I(a).
- Verified the fixed-point and fixed-point-free rational examples are nonisomorphic Set-models.
- Current main directory tree SHA exactly equals the assigned tree SHA; no GitHub writes were made.

## Limitations

- The argument is for the stated strict-order/coherent signature and the usual finitely-presentable-model criterion for presheaf type.
- No stronger classification of the classifying topos is claimed.

## Repository action

This audit is a guarded change-set only. Source tree `c2b2d60d5dc923a2ac56501ae292875ea861c1e5` still matches current `main`; no GitHub write was performed by this audit.
