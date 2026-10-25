# Independent mathematical audit

## correctness

PASS

PASS: The one-step expected squared projector is p0I+p1P1+p2P2; its top eigenvalue is p0+(s+sqrt(r^2 s^2+(1-r^2)d^2))/2. The self-adjoint positive covariance operator H -> p0H+sum p_i P_iHP_i acts on span(P1,P2) with Perron eigenvalue p0+(s+sqrt(r^4 s^2+(1-r^4)d^2))/2, with the remaining eigenvalue p0. Positivity and trace comparison justify limit of worst-initial-error k-th roots without interchanging supremum. For s>0, both uniquely optimize at d=0; the remaining objectives are affine in batch mass t, with slope zeros at the two asserted thresholds. Exact rational independent projector calculations at w=4,c=1,r=3/5 gave one-step R_single=4/5, R_batch=3/4 and 2-step singleton maximum 68/125 vs batch 9/16, supporting the asymptotic rates Q_single=17/25 and Q_batch=3/4. Checks do not prove universal real inequalities by enumeration.

## originality

PASS

PASS (best knowledge): Earlier batch-sampling Kaczmarz analysis gives general convergence rate bounds and trainable distributions but is not shown to identify the exact four-mask, fixed-expected-cost, two-objective optimizer split. Mutny et al. 2020 use determinantal block sampling for a different method. A particularly plausible 2026 coordinate-descent companion was available in abstract only and could have an equivalent special case; best-knowledge novelty retains this material risk.

## value

PASS

PASS: A sharp interval in which the law optimal for first-step error is strictly inferior for long-run mean-square error establishes a meaningful modeling and algorithmic boundary. The equal expected-work constraint and explicit idle mask are clearly scoped; no hardware-runtime claim or nonempty-batch claim is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
