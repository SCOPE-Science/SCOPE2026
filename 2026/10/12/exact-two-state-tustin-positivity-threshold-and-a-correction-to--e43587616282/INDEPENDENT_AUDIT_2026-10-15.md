# Independent mathematical audit

## correctness

PASS

For any Hurwitz Metzler A, M=I-hA/2 is an invertible M-matrix with nonnegative inverse and T_h=2M^{-1}-I. Thus only diagonal inequalities matter. For 2 states, direct inversion gives common denominator 1+(a+d)h/2+Delta h²/4 and two diagonal numerators 1±(a-d)h/2-Delta h²/4, so positivity iff 1-|a-d|h/2-Delta h²/4≥0 and h≤4/(|a-d|+sqrt((a+d)²-4bc)). Independently calculated the diagonal A=diag(-10,-1), h=1/2 counterexample: alpha=4 and Delta=10≤16, but T=diag(-3/7,3/5). Independently verified the coupled threshold case a=d=1,b=3/4,c=1. The ratio to the conservative h≤2/max(a,d) diverges for a=d=1,b=c→1-. This is an exact algebraic proof for all h≥0, not inference from numerical samples.

## originality

PASS

The 2010 Zappavigna–Colaneri–Kirkland–Shorten paper itself prints both correct two-state diagonal numerators but makes the false intermediate leap Delta≤alpha² ⇒ nonnegativity. Its later alpha≥max(a,d) condition is correct and conservative. The 2012 follow-up gives sufficient bounds but not the sharp corrected iff; Fallat–Tsatsomeros supplies the Cayley algebra. A prior Resultary reversible Markov-chain resolvent result overlaps with the general resolvent-diagonal equivalence, which is not claimed independently as novel, but does not settle this strictly Hurwitz general two-state threshold, published error, or arbitrarily large improvement. PASS novelty belongs to exact new correction/refinement, with residual risk of an earlier equivalent 2×2 Cayley calculation.

## value

PASS

A mathematically consequential positivity mistake in a published discretization criterion is corrected by an exact necessary and sufficient two-state sampling boundary, while retaining the validity of the subsequent conservative theorem. The explicit unbounded conservatism ratio provides structural insight for strongly coupled positive systems; this is more than a numeric adjustment and avoids claiming a higher-dimensional closed form.

The dated certificate retains the supplied scientific assessment, sources and limitations.
