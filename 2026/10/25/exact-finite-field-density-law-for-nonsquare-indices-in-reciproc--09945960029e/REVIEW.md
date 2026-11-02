# Independent mathematical audit

## correctness

PASS

PASS: Writing t_n=(x0+...+x_n)/h=u_n/v_n in coprime terms gives (u_next,v_next)=(u²+v²,uv) and Q_(j+1)=(u_(j-1)+v_(j-1))²/gcd(h,u_j). If an odd prime divides the gcd its numerator is p-coprime, giving negative valuation; p=2 forces odd valuation after reduction. At each p^alpha||h, only x0 of exact p-valuation alpha produces a nonzero finite-field start; the other two valuation cases escape and cannot cause a later bad index. First T_p(r)=r+r^-1 zero occurs at most once, depth<=p-1; one seed residue mod p^(alpha+1) corresponds to each nonzero starting r. CRT makes these local outcomes independent. Idempotent multiplication precisely corrects collisions of the SAME index from different primes. Independently recomputed first-zero basins p=5 and p=29 and all 21025 CRT classes for h=145, confirming 17493,3512,20 and 12 colliding indices. Source CHECK.py was inspected; finite checks support, not replace, the arbitrary-h proof.

## originality

PASS

On the inspected primary sources and independent comparison, the specified new exact evaluation/classification is not supplied by a stronger known theorem; scope and residual priority limitations are stated explicitly. The theorem converts the local orbit first-hit mechanism into the probability law of a set of indices. This is the same arithmetic problem as the motivating paper, not a different recurrence or a renamed parameter. Known local dynamics are core inputs, not a stronger theorem implying the density without extra residue weights and collisions. The claim settles an explicitly published open quantitative question rather than rephrasing its first-hit criterion.

## value

PASS

PASS: Answers the motivating authors’ explicitly asked distribution question for every h and strengthens it to complete exact failure-index sets; nontrivial collision correction is necessary already at h=145. A natural infinite arithmetic-dynamics density classification with a finite residue algorithm, not a merely arbitrary finite slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
