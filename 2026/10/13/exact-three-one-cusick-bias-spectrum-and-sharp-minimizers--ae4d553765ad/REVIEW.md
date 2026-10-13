# Self-review

## Correctness — PASS

The binary digit-addition identity counts total outgoing carries exactly. Under a budget of three carries, an outgoing carry beyond the third zero column after the highest nonzero digit is impossible, which proves the finite-residue formula rather than assuming it from sampled integers. Likewise an inter-one gap of at least four columns cannot transport any surviving carry to its later one, so the gap-clipping theorem reduces all infinitely many shifts to sixteen exact, explicitly given integer-state recurrences. The complete table was calculated with an independent finite deconvolution recurrence and direct complete-residue enumeration for each canonical shift. A standalone verifier reproduces every rational value and stress-tests 256 extra gap pairs. The minimum and equality cases follow from comparing all sixteen table cells. There are no unproved extrapolations from finite samples.

## Originality — PASS, with residual risk

The closest existing fixed-weight paper (Cheng, arXiv:2608.25899v1, especially pp. 1–3) defines \(F(k)\) and proves asymptotics for \(k\to\infty\), not the exact value at \(k=3\). The earlier first-exit paper (arXiv:2606.23398v1, pp. 1–6) proves a universal bound and explicitly computes a finite law for the single shift \(11\); neither that isolated example nor the recurrence itself is claimed here as original. Spiegelhofer–Wallner (arXiv:2005.07167v3, pp. 1–4) establish many-block theory and recurrence; Drmota–Kauers–Spiegelhofer (arXiv:1509.08623v2, pp. 1–5) tabulate small shifts and study asymptotics. Exact comparison of these implications and semantic/index searches did not reveal an all-gap weight-three spectrum theorem. Because old recurrences can be specialized to recover the result, an implicit or unindexed prior classification remains possible.

## Value — PASS

The exact invariant \(F(k)\) is a motivated object of a recent fixed-weight extremal problem. Its value \(F(3)=3/32\), together with the complete spectrum and all global minimizers over arbitrarily separated three-one shifts, is a natural full low-weight classification, not an arbitrary numerical cutoff. The structural four-column gap barrier makes a finite exact computation exhaustive over an infinite shift family. This supplies a benchmark for higher-weight questions without claiming a general higher-weight theorem.

Self-review: passed. Independent audit: not yet performed.
