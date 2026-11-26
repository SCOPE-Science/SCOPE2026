# Independent mathematical audit

## correctness

PASS

Each raw weight is m/(m+s_j)−m/(m+s_j+n_j); completeness and strict radial order make the denominator telescope to S/(m+S). For b=a+n, set F=P/(n/S). Then F−1=((c−a)m−ab)/((m+a)(m+b)), and F' has numerator (a−c)m²+2abm+Sab over a positive denominator. For a>0 the derivative stays positive at and below c=a; above c=a the quadratic has opposite-sign roots, with the positive root m* given in the Finding because ab+S(c−a)=c(n+c). The positive root exceeds the baseline crossover ab/(c−a). At the positive finite maximum the equation F=λ has a double root and λ>1. Its discriminant gives the two stated signed radical values; the larger value exceeds S/n (since b(n+c)−ac=nS), hence its double root is negative because λ(a+b)>S. The smaller value is the attained peak. Substituting ε=c−a into the exact peak location gives εm*→2ab, and substituting this into F−1 gives (F(m*)−1)/ε²→1/(4ab). For a=0, cancellation leaves n(m+S)/(S(m+n)), strictly decreasing unless c=0, when it is 1. The farthest case c=0<a is covered by the positive derivative. The exact (1,1,8) shares at m=2 follow by telescoping or direct evaluation and give (2/5,1/5,2/5). The new bounded script `python /workspace/independent_reproduction.py` independently checks derivative and discriminant identities and the example's factor 2; the proof is not a finite sample. The frozen checker was inspected, not executed.

## originality

PASS

Credit the entire normalized share formula to the existing model: it is a direct re-expression of Masucci et al. The distinct claim on inspected evidence is the complete outer-vs-inner criterion and its peak and onset for one fixed destination as source mass varies. The analysis uses elementary calculus, not a new mobility law or a new monotonicity technique. I found no prior statement or stronger comparative-statics result covering this classification in the actual passages compared.

## value

PASS

This is a modest but natural complete classification of a model observable, not just evaluation of a known formula at chosen parameters. Finite normalization can remove a peak that exists for the raw radiation weight. The balance of opportunity mass beyond vs before a fixed site, independently of its own mass, decides which sites overshoot the limiting share; the onset calculation distinguishes a peak arriving from infinity from one emerging at finite origin size. Those are usable structural constraints when interpreting the normalized model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
