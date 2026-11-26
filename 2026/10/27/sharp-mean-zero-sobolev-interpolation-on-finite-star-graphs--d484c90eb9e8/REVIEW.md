# Independent mathematical audit

## correctness

PASS

Normalize a nonzero leaf value to 1 by complex scaling. Given the center c, the other leaves have prescribed mean; replacing them by it strictly decreases both quadratics unless already equal. The imaginary part of c adds a positive multiple of its square to both quadratics, so the optimal c is real. The reduced quadratics are exactly M_n and E_n. Independent symbolic differentiation and discriminant factorization reproduce p_n and its strictly negative discriminant (the remaining polynomial has positive coefficients at n=2+m), including p_n(-1/n)=-(n^2-1)^2/n^2 and p_n(0)=2n. Coercivity then makes the unique root the global minimum. At the center, fixed-value averaging gives n/(n+1)^(3/2), strictly below the coefficient of the trial leaf witness (n/(n+1))^(3/2). The optimizer's other magnitudes are less than 1 even at n=2; the strict averaging conditions and symmetry therefore give precisely all equality cases. Both reduced quadratic minima exceed 1. With h=1/n, h^3 p_(1/h)(c) is analytic with c-derivative 1 at the origin; c=-2h^2+4h^3-10h^4+O(h^5). Independent substitution gives M_n E_n=1+2h+3h^2+O(h^4), whose inverse square root is 1-h+2h^3+O(h^4). The independent n=2 value is 0.584928489376185786… .

## originality

PASS

Credit the general sharp Green-function envelope and earlier exact path and cycle evaluations. The distinct supported result is the exact discrete-star specialization including unique optimizer, global dominance of leaves, the equality profile and the cubic high-valence correction. The strongest continuum star hit concerns a different functional and notion of mean.

## value

PASS

Stars give a canonical family with arbitrarily large degree contrast. The exact sharp point-evaluation product constant and all extremizers settle which orbit controls the bound and give a usable benchmark for localized graph inequalities. The first nontrivial correction beyond 1−1/n and vanishing quadratic term distinguish a precise invariant across the whole family, rather than an isolated sample or a restated resolvent bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
