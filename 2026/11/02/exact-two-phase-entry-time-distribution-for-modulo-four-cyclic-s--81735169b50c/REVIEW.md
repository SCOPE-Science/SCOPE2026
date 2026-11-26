# Independent mathematical audit

## correctness

PASS

The cyclic sum is multiplication by 1+x after a choice of shift orientation. Writing n=qh with h odd, the factors x^q−1 and Q=sum_{j=0}^{h−1}x^(jq) are comaximal modulo 2 (Q(1)=1 there), hence modulo 4. The Q factor is invertible for the dynamics and has 4^(n−q) elements, including the one-element factor if h=1. On the other factor, with y=1+x, v₂(binom(q,j))=v₂(q)−v₂(j) gives y^q=2y^(q/2). The monic quotient has basis y^0 through y^(q−1). Its higher powers fold to 2y^(q/2+j) for 0≤j<q/2 and vanish thereafter. The ideal y^t A has q−t free coordinates up to t=q/2, then q−t free and t−q/2 order-two coordinates up to t=q, then only 3q/2−t order-two coordinates up to t=3q/2. Thus the kernel fraction is the reciprocal of the asserted image size, including both transition points and t=0. First differences give the exact counts and the final mass 1/2; y^(3q/2−1)=2y^(q−1) is nonzero. The bounded tests described in VERIFICATION.md and verify.py were inspected, not replayed; the result is proved by the coordinate calculation in RESULT.md §§1–3. The Dular section-number error is bibliographic, not mathematical.

## originality

PASS

Pass for the full entrance-time profile, not for the already covered maximum. The available primary and catalogue statements do not supply the sequence of images of powers needed for the CDF. A same-day comparison confirms coverage of the maximum but does not establish equivalent coverage of the census.

## value

PASS

This is a complete transient population census for the standard modular Ducci operator, not just an improvement of a stopping-time bound. It distinguishes the early and late contraction scales, makes the exact frequency of worst-case vectors available, and shows which part of the tuple length matters for the entire normalized law. These facts are useful for the dynamics even when its maximum is known.

The dated certificate retains the supplied scientific assessment, sources and limitations.
