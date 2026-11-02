# Scientific review

## Correctness — PASS

The first bias-corrected Adam-GC update is exactly $-\alpha h_i/(|h_i|+\varepsilon)$ for a centered gradient $h$. The positive/negative mass split and strict Jensen argument give $|\Delta\bar w|<\alpha(d-2)/d$ for every finite centered gradient in dimension $d\ge3$, with the constant approached by $(a,\ldots,a,-(d-1)a)$ as $a/\varepsilon\to\infty$. Every two-coordinate centered gradient has equal and opposite updates. The official final-delta-centralized variant preserves mean for the blocks to which its projection is applied.

The independent consistency checks include 4,214 exact-rational cases. They support, but do not replace, the all-dimensional analytic proof.

## Originality — PASS, qualified

The defining gradient-centralization paper already gives the optimizer update equations and proves an affine mean invariant for projected SGD/SGDM, not for its adaptive Adam update. Its official GC2 implementation already centers the final preconditioned delta and is not new. A later moment-centralization method still divides by coordinate-dependent denominators. The surviving novel mathematical contribution, to the best of the inspected literature, is the dimension-sharp first-step supremum over all centered gradients and the exact dimension-two exception, not the implementation or qualitative insight that adaptive scaling may break a mean constraint.

The relevant primary paper sections, official implementation source, and later moment-centralization algorithm were inspected directly. No matching sharp extremal result appeared in the searched published mathematical records. An unindexed implementation discussion containing the same short extremal inequality remains a priority risk.

## Value — PASS

The magnitude of a parameter update's departure from GC's affine weight-space constraint is a natural optimizer invariant. The exact sharp dimension law shows the onset and maximal possible violation under Adam preconditioning and precisely distinguishes prior final-update centralization. It is a worst-case, first-step diagnostic, not a claim about training quality or typical gradients.

## Mathematical limitations

The sharp theorem assumes positive learning rate, positive denominator regularizer, zero initial Adam moments and no weight decay. Later steps, alternate epsilon placements and other optimizer variants are outside this proof. Finite checks are not a formal proof and do not establish expert attestation.

## Primary scientific sources

Yong, Huang, Hua, Zhang, *Gradient Centralization: A New Optimization Technique for Deep Neural Networks*, ECCV 2020, §§3.3–4.1 and Algorithms 1–2. Official Gradient Centralization source `Adam.py` at commit `ed2a608ccdbb731301e00bf838c83821df1b8d70`. Sadu, Dubey, Sreeja, *Moment Centralization based Gradient Descent Optimizers for Convolutional Neural Networks*, arXiv:2207.09066v1, §2 and Algorithm 2.
