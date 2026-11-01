# Independent mathematical audit

## correctness

PASS

PASS. Integer lattice points in tP_{n,a} (n>=5, a>=1) can be counted by conditioning on x_n or x_{n-1}; both methods yield L(t)=binom(at+n,n)+sum_{q=0}^{t-1}binom(aq+n-1,n-1) for all integer t>=0. This is a polynomial identity, since finite sums of polynomial summands are polynomials. Exact Bernoulli/Faulhaber extraction of coefficient t^{n-4}, with E_j=e_j(1,...,n-1), produces a^{n-5}/(n-1)! times Q_n(a), where Q_n(z)=E4/(n-4)+(E4/n+E3/2)z+((n-3)/12)E2 z²-[(n-1)(n-2)(n-3)/720]z⁴. The B3=0 term removes z³; B4=-1/30 gives the negative z⁴ coefficient. Descending nonzero coefficients of Q_n have signs -, +, +, +, hence Descartes yields at most one positive root counted with multiplicity; Q_n(0)>0 and Q_n(large)<0 ensure exactly one simple positive root rho_n. Q_n(1)>0 and a domain are checked. For E_j=n^{2j}/(2^j j!)+O(n^{2j-1}), setting z=c n^{4/3}, dividing by n^{25/3}, gives c/384-c⁴/720; root squeeze yields rho_n/n^{4/3}->(15/8)^{1/3}, and rounding changes o(1). Only this monomial coefficient is classified. Direct exact rational interpolation independently verified 18 n/a cases (n5..7), n5..7 integer thresholds 16,19,23, and supplied original code proves no universal statement by finite checks.

## originality

PASS

PASS, best of knowledge. Caicedo, Juhnke and Poullot (2025), same exact one-step family and coefficient, establish eventual negativity as a grows for each fixed n, and tabulate first negative integer parameters in dimensions 5 through 8. Their full primary paper does not give an exact four-term Q_n for every dimension, an exactly one-positive-root theorem or asymptotic threshold as n grows. These new claims sharpen the precise selected coefficient and are not implied by the earlier leading term or four-row table. Brändén–Solus (2019) gives unimodular triangulations for 0/1-difference lecture-hall sequences but no ordinary Ehrhart monomial coefficient sign cutoff. Recent followups and formula equivalences remain genuine risks.

## value

PASS

PASS. The 2025 paper identifies exactly this infinite one-step lecture-hall family as a source of Ehrhart negativity and only proves eventual failure at fixed dimension, motivating a sharp threshold. The new one-positive-root quartic identifies the exact first negative parameter for a genuinely natural coefficient in every dimension, including a nontrivial dimension scaling n^{4/3} with constant (15/8)^{1/3}. This is a complete natural sign-cutoff theorem rather than a textbook binomial-coefficient exercise or recomputed finite data. It deliberately leaves global coefficientwise positivity open.

The dated certificate retains the supplied scientific assessment, sources and limitations.
