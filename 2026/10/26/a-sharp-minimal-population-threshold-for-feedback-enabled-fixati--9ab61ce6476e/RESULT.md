# A sharp minimal-population threshold for feedback-enabled fixation

## Finding

Consider a continuous-time birth–death population with two types and absorbing mutant counts \(i=0\) and \(i=N\). For \(N=3\), all birth rates at the two transient counts are \(1\). The two fixed environments have death-to-birth ratios \( (x,y)\) and \( (y,x)\) at mutant counts \(i=1,2\), where \(0<x<y\). The environment switches according to the current mutant count: at \(i=1\), the rates are \( +\to-:e\) and \( -\to+:M\); at \(i=2\), they are \( +\to-:M\) and \( -\to+:e\), with \(e,M>0\).

Starting from one mutant in environment \(+\), the fixation probability exceeds both fixed-environment fixation probabilities if and only if

\[
F(x,y,e,M)=xM^2+(xy-e)M-e(e+1)(y+1)>0.
\]

Equivalently, the exact threshold is \(M>M_*\), where

\[
M_* = \frac{e-xy+\sqrt{(xy-e)^2+4xe(e+1)(y+1)}}{2x}.
\]

The cutoff in population size is sharp: for \(N=2\), with one transient mutant-count state and unit birth rates, no switching rule between the two environments can make fixation exceed the better fixed-environment probability. Thus \(N=3\) is the smallest population size in this model class permitting a feedback-enabled advantage.

## Assumptions and scope

The process is a finite continuous-time Markov chain. Mutant count \(i\) changes by one at a time; \(i=0\) is extinction and \(i=N\) is fixation. For \(N=3\), the birth rates \(W^+_{i,\sigma}=1\) for \(i=1,2\) and both environments \(\sigma\in\{+,-\}\). Death rates are \(W^-_{1,+}=x\), \(W^-_{2,+}=y\), \(W^-_{1,-}=y\), and \(W^-_{2,-}=x\). The environment transition rates depend on \(i\) exactly as specified in the finding. Rates are positive and time-homogeneous conditional on the joint state \((i,\sigma)\).

The comparison freezes the environment in \( + \) or \( - \) while keeping the same birth and death rates. Since \(x<y\), the better frozen environment is \( + \). The claim concerns fixation probability from \(i=1\), initially in environment \( + \); it does not claim an advantage for every initial environment or for stationary random initialization.

## Proof

For a fixed environment, the standard birth–death recurrence for increments \(d_i=\phi_i-\phi_{i-1}\) is \(d_{i+1}=(W^-_i/W^+_i)d_i\). With \(N=3\), this gives

\[
\phi^{\mathrm{stat}}_{1,+}=\frac{1}{1+x+xy},\qquad
\phi^{\mathrm{stat}}_{1,-}=\frac{1}{1+y+xy}.
\]

For \(N=2\), let the death-to-birth ratios in the two environments be \(x<y\), and let the switching rates be \(\alpha\) from \( + \) to \( - \) and \(\beta\) from \( - \) to \( + \). If \(u,v\) are fixation probabilities starting in \( +,-\), the backward equations are

\[
(1+x+\alpha)u=1+\alpha v,\qquad
(1+y+\beta)v=1+\beta u.
\]

Writing \(D_2=\alpha y+\alpha+\beta x+\beta+xy+x+y+1>0\), elimination gives

\[
u-\frac{1}{1+x}=\frac{\alpha(x-y)}{(1+x)D_2},\qquad
v-\frac{1}{1+x}=\frac{(x-y)(\alpha+x+1)}{(1+x)D_2}.
\]

Both differences are nonpositive. Thus no choice of switching rates improves on the better frozen environment when there is only one transient population state.

For \(N=3\), put \(u=\phi_{1,+}\), \(v=\phi_{2,+}\), \(w=\phi_{1,-}\), and \(z=\phi_{2,-}\). The four backward equations are

\[
\begin{aligned}
(1+x+e)u-v-ew&=0,\\
-yu+(1+y+M)v-Mz&=1,\\
-Mu+(1+y+M)w-z&=0,\\
-ev-xw+(1+x+e)z&=1.
\end{aligned}
\]

Let \(A\) be the coefficient matrix in this system and \(\Delta=\det A\). Each row is strictly diagonally dominant, with positive diagonal and nonpositive off-diagonal entries; hence \(A\) is a nonsingular \(M\)-matrix and \(\Delta>0\). Exact elimination (equivalently, Cramer's rule followed by factorization) yields

\[
u-\frac{1}{1+x+xy}=\frac{(y-x)\,[xM^2+(xy-e)M-e(e+1)(y+1)]}{(1+x+xy)\Delta}.
\]

Because \(y-x>0\), \(\Delta>0\), and the frozen \( + \) probability is larger than the frozen \( - \) probability, the switching model beats both frozen environments exactly when \(F(x,y,e,M)>0\). The quadratic \(F\), as a function of \(M\), has negative constant term and positive leading coefficient, so it has exactly one positive root, the displayed \(M_*\).

For the exact example \(x=2\), \(y=3\), \(e=1/10\), and \(M=10\), the four-state system gives \(u=181/1373\). The frozen probabilities are \(1/9\) and \(1/10\), and \(F=6464/25>0\). This verifies strict advantage while both environments disfavor the mutant at each transient count, because both death-to-birth ratios exceed \(1\).

## Verification

The embedded standard-library Python script solves the four backward equations using exact rational arithmetic and checks the representative probability, both frozen-environment values, the threshold polynomial, and the two-state comparison. This computation checks the example, not the universal claim by finite sampling; the parameter-wide statements follow from the algebraic derivations above. No biological parameter fitting or stochastic simulation is used.

## Relationship to prior work

Ashcroft, Altrock, and Galla develop exact fixation formulas for finite birth–death populations in fluctuating environments, but their environmental Markov chain is assumed to evolve independently of population state. Their model therefore does not include switching rates conditioned on mutant count, which is the essential feature here. Wienand, Frey, and Mobilia couple demographic noise to a randomly switching carrying capacity; their environment still switches exogenously, and their model does not yield the state-conditioned threshold above. The present result is a small, exact feedback benchmark, not a claim that environmental switching advantages in general are new.

## Limitations

The theorem is exact for the specified two-environment birth–death family and the stated initial condition. It does not classify arbitrary rate matrices, larger populations, more than two environments, or biological mechanisms that would generate the chosen feedback rates. The three-individual cutoff is a minimal mathematical benchmark rather than an empirical estimate. Literature searches cannot rule out every equivalent result in unindexed or differently named sources; the closest inspected literature uses exogenous switching, leaving broader state-dependent-switching literature as a residual risk.

## References

1. P. Ashcroft, P. M. Altrock, and T. Galla, “Fixation in finite populations evolving in fluctuating environments,” *Journal of the Royal Society Interface* 11 (2014), 20140663. First public preprint: 21 June 2014. https://arxiv.org/abs/1406.5619 ; full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC4191092/.
2. K. Wienand, E. Frey, and M. Mobilia, “Evolution of a Fluctuating Population in a Randomly Switching Environment,” arXiv:1708.08841 (2017). https://arxiv.org/abs/1708.08841.
