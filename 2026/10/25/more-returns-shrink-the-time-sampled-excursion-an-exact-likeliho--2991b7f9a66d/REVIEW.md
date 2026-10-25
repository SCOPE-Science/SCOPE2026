# Scientific review

## Correctness — PASS

The walk model and semilength convention are defined at the sample-path level. The Catalan-product weight for conditioned excursion lengths is the established first-return enumeration; Lagrange inversion supplies the explicit normalizer, and its adjacent-rank quotient is a monotone fractional-linear function of the remaining mass. This yields a genuine cross-product likelihood-ratio comparison including support boundaries. Conditional independent excursion signs yield the exact positive-sem duration variance relation, and the density-limit proof includes a uniform geometric tail bound, rather than inferring moment convergence from weak convergence alone. Independent exhaustive balanced-walk enumeration and exact rational checks in `verify.py` completed 43,394 assertions.

## Originality — PASS (priority provisional)

The closest primary comparison is Serlet's 2014 paper: its equations (5)–(8) already give the complete Catalan-product counting law for excursion lengths conditioned on the return count. Those formulas supply an essential premise and imply the explicit mass law after a size-bias operation, but the inspected analysis concerns a few-zero invariance principle and does not state or establish cross-count likelihood-ratio dominance. Csáki–Hu (2003) and Lindell–Holst (2007) study ranked excursion distributions rather than this monotone time-sampling order. The exact ordering, its strict all-return-count variance consequence, and the linear-density constant are the assessed new combination. A previously published general renewal-composition monotonicity theorem or allocation limit could subsume parts of this finding; broad Janson allocation literature was not completely inspected. This review does not assert conclusive worldwide priority.

## Mathematical value — PASS

Conditioning a bridge on its return count is natural in excursion theory, pinned-polymer models, and plane-forest encodings. The strict likelihood-ratio order is stronger than variance monotonicity and simultaneously controls every increasing statistic of the excursion experienced by a time-sampled observer. Its effect on positive-excursion occupation variability gives a complete finite return-count hierarchy with sharp endpoints; the density-scale constant describes the contrasting extensive-return regime. This structural order is not evident from the separate marginal bridge law or few-zero invariance principles.

## Limitations and closest work

The law applies only to fair, nearest-neighbor, tied-down walks. The positive-excursion semiduration is defined by complete excursion intervals, not by a pointwise above-zero clock-time count. Finite tests are not used as an all-size proof. Serlet's enumeration overlaps the formula-level groundwork substantially. General renewal ordering results and the complete allocation literature remain an originality risk; no independent scientific audit was conducted.

Self-review: passed. Independent audit: not yet performed.
