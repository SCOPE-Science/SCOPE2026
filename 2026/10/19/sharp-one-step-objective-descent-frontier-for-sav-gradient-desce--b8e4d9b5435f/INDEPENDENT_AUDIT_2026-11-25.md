# Independent mathematical audit

## correctness

PASS

For the initialized first step, write t=x², u=t−1 and α=h/(1+hβ), where β=2tu²/(1+u²). Then x⁺=x(1−αu) and (r⁺)²=r²/(1+hβ)². The equilibria t=0,1 are fixed; otherwise β>0. For t≥2, 0<αu<1/2 (with ≤1/2 for its large-h bound), so 0<(x⁺)²<t and strict quartic descent follows. For 0<t<2, t≠1, h≤1, the sign of x is preserved and comparison with the equal-energy partner 2−t gives α≤2/[t+sqrt(t(2−t))], equivalently h d(u)≤2. For u<0 we have d(u)<2; for 0<u<1, d''(u)=−(1−u²)^(-3/2)+8(u−1)(u²+4u+1)/(1+u²)^3<0, with d'(0)=1 and d'(1−)=−∞. This proves the cutoff and all equality cases up to the cutoff; the same maximizer gives expansion up to h=1 and the multiplier 1−2h at a minimum gives an expanding initialization for every h>1. Along x=sqrt(1−ε), h=ε^(-3), 1+hβ~2/ε and x⁺~1/(2ε), giving the stated objective and auxiliary asymptotics.

## originality

PASS

Credit the unrelaxed update and modified-energy law to Liu–Shen–Zhang, and the qualitative original-energy defect to established SAV literature. The supported distinct contribution is the quantitative sharp all-initialization frontier and equality structure for this quartic step, together with the divergent first-step separation. Neither the same-update quadratic recurrence nor the nearby relaxed first-step rank criterion covers it.

## value

PASS

The double well is a natural minimal nonconvex test of whether the unconditional auxiliary-energy guarantee controls the actual objective. An exact global cutoff strictly below the local threshold rules out inferring universal descent from linear stability, and the divergence construction rules out even a qualitative bound of original by improved auxiliary behavior for large first steps. Both conclusions are useful for testing first-step safeguards.

The dated certificate retains the supplied scientific assessment, sources and limitations.
