# Exact least-core deficit in a binary plurality-voting ensemble

## Finding

Fix one binary-labeled test example and an ensemble of \(n=a+b\ge 2\) classifiers: \(a\) predict its correct label and \(b\) predict the incorrect label. With random tie-breaking, define each nonempty coalition's worth as its probability of predicting correctly. Under **signed, efficient, transferable-utility allocations** and the additive \(\varepsilon\)-core convention, the minimum nonnegative maximum coalitional deficit is exactly

\[
\varepsilon^*(a,b)=
\begin{cases}
0,&a=0,\\
\dfrac{a-1}{a},&b=0,\\
\dfrac{a}{a+1},&0<a<b,\\
\dfrac{2a-1}{2(a+1)},&a=b\ge 1,\\
\dfrac{a-1}{a+1},&b<a\le 2b+1,\\
\dfrac{a-b-1}{a-b},&a>2b+1.
\end{cases}
\]

Here \(a,b\) are nonnegative integers, and the second case necessarily has \(a\ge2\) because \(n\ge2\). In particular, with both prediction types present, the ordinary core is empty. The least-core obstruction changes at \(a=2b+1\): on one side the all-incorrect coalition and correct singleton coalitions give the sharp lower bound, while on the other a winning coalition containing all \(b\) incorrect and exactly \(b+1\) correct classifiers becomes decisive. Equality is shared at the transition.

A type-symmetric optimal allocation gives each correct classifier \(p\) and each incorrect classifier \(q\):

| Domain | \(p\) | \(q\) |
| --- | --- | --- |
| \(a=0\) | absent | \(0\) |
| \(b=0\) | \(1/a\) | absent |
| \(0<a<b\) | \(1/(a+1)\) | \(-a/[b(a+1)]\) |
| \(a=b\ge1\) | \(3/[2(a+1)]\) | \(-(2a-1)/[2b(a+1)]\) |
| \(b<a\le2b+1\) | \(2/(a+1)\) | \(-(a-1)/[b(a+1)]\) |
| \(a>2b+1\) | \(1/(a-b)\) | \(-1/(a-b)\) |

## Assumptions and scope

Let \(N=C\sqcup W\), where \(|C|=a\) and \(|W|=b\), and \(|N|=n\ge2\). The nonempty coalition \(S\) has \(c=|S\cap C|\) and \(d=|S\cap W|\) and worth

\[
v(S)=\begin{cases}
1,&c>d,\\
\tfrac12,&c=d>0,\\
0,&c<d,
\end{cases}
\qquad v(\varnothing)=0.
\]

For any allocation \(x\in\mathbb R^N\), write \(x(S)=\sum_{i\in S}x_i\). The least additive core deficit is

\[
\varepsilon^*(a,b)=\min\left\{\varepsilon\ge0:\,x(N)=v(N),\quad x(S)\ge v(S)-\varepsilon\quad\text{for every}\ \varnothing\ne S\subsetneq N\right\}.
\]

Negative individual credits are permitted. The whole grand coalition is excluded from the deficit constraints because efficiency fixes its excess at zero; the empty coalition is excluded as well. All ties between the two predicted labels are resolved uniformly. The result concerns **one test example**, not the average game over several examples, whose coalitional worth may lose the two-type symmetry. It does not address a nonnegative-imputation-restricted least core.

## Proof

**1. The first lower bound.** Assume \(a,b\ge1\) and put \(V=v(N)\in\{0,\tfrac12,1\}\). Every correct singleton \(\{i\}\) has worth \(1\), hence \(x_i\ge1-\varepsilon\). The coalition \(W\) of all incorrect classifiers is proper and has worth zero, so \(x(W)\ge-\varepsilon\). Efficiency therefore gives

\[
V=x(C)+x(W)\ge a(1-\varepsilon)-\varepsilon,
\qquad \varepsilon\ge\frac{a-V}{a+1}.
\tag{1}
\]

This yields the first three mixed-type expressions according as \(a<b\), \(a=b\), and \(a>b\).

**2. The second lower bound.** If \(a\ge b+2\), choose any subset \(R\subset C\) with \(|R|=b+1\). The coalition \(R\cup W\) is proper, winning, and has worth \(1\), while \(V=1\). Summing its \(\varepsilon\)-core inequalities over all such \(R\) and dividing by their number yields

\[
\frac{b+1}{a}x(C)+x(W)\ge1-\varepsilon.
\]

Substituting \(x(W)=1-x(C)\) gives \(\varepsilon\ge(a-b-1)x(C)/a\). From the correct singleton inequalities, \(x(C)\ge a(1-\varepsilon)\); thus

\[
\varepsilon\ge(a-b-1)(1-\varepsilon),\qquad
\varepsilon\ge\frac{a-b-1}{a-b}.
\tag{2}
\]

The bound in (2) exceeds (1), with \(V=1\), exactly when \(a>2b+1\); equality occurs when \(a=2b+1\). These are actual coalition constraints, so the lower bounds do not depend on symmetry of \(x\).

**3. Matching allocations for \(a,b\ge1\) with \(a\le2b+1\).** Choose \((p,q)\) from the corresponding three rows of the table. Direct substitution shows efficiency \(ap+bq=V\), \(p>0\), \(q<0\), \(p+q\ge0\), and

\[
1-p=-bq=\frac{a-V}{a+1}=:\varepsilon.
\]

For a coalition with \(c>d\), its payment satisfies \(cp+dq=(c-d)p+d(p+q)\ge p\), so its deficit is at most \(1-p=\varepsilon\). If \(c<d\), its payment is at least \(bq\), so its deficit is at most \(-bq=\varepsilon\). If \(c=d>0\), its payment is nonnegative and its deficit is at most \(\tfrac12\). In these regimes \(\varepsilon\ge\tfrac12\), except for \((a,b)=(1,1)\) and \((a,b)=(2,1)\). For \((1,1)\), there is no proper tied coalition. For \((2,1)\), its sole proper tied type is \((c,d)=(1,1)\), with payment \(p+q=\tfrac13\), hence deficit \(\tfrac16\le\varepsilon=\tfrac13\). Thus every proper coalition satisfies its inequality.

**4. Matching allocations for \(a>2b+1\).** Choose \(p=1/(a-b)\) and \(q=-p\). Then efficiency holds, since \(ap+bq=1=V\). Every winning coalition has payment \((c-d)p\ge p\), every losing coalition has payment \((c-d)p\ge-bp\), and every tied coalition has payment zero. Here \(a-b\ge3\), and the proposed deficit \(\varepsilon=1-p\) satisfies \(\varepsilon\ge bp\) because \(a\ge2b+1\), as well as \(\varepsilon\ge\tfrac12\). Therefore the claimed bound holds for all coalitions. The singleton correct and nearly balanced winning coalition lower bounds (1)--(2) prove optimality.

**5. Homogeneous cases.** When \(a=0\), every coalition has worth zero, and the zero allocation has deficit zero, optimal by \(\varepsilon\ge0\). When \(b=0\), every nonempty coalition is winning and \(V=1\). Adding the singleton constraints gives \(1\ge a(1-\varepsilon)\), hence \(\varepsilon\ge1-1/a\). The equal allocation \(x_i=1/a\) attains it because every nonempty coalition receives at least \(1/a\). This concludes all cases.

## Verification

The standalone `VERIFY.py` uses exact rational arithmetic to check efficiency, analytical lower-bound equality, and **every type-count coalition inequality** on all \(1088\) profiles \(0\le a,b\le32\) except \((0,0)\). It checked \(312544\) nontrivial coalition-type inequalities. Independently, it uses a full, **unsymmetrized** linear program with a separate unrestricted signed allocation variable for every classifier to check all \(54\) profiles with \(1\le a+b\le9\); the code executes the latter test when SciPy is available. These experiments only corroborate the exact proof and do not establish its infinite quantifiers.

Run `python VERIFY.py` in an environment with Python 3; SciPy is optional for the full linear-programming cross-check.

## Relationship to prior work

Sarpe, Georgakopoulos, and Gionis, *Exact power indices for plurality-voting ensembles* (arXiv:2610.17980v1, October 13, 2026), define the precise random-tie binary accuracy game above in their Eq. (2) and give exact Banzhaf and Shapley values in Theorems 4.1--4.2. Their objective is average marginal-contribution attribution; their formulas do not determine a minimax coalition deficit or give the phase boundary here. Their manuscript explicitly identifies studying further power indices as future work, but this result addresses the **least-core stability criterion**, not another power-index formula.

General least-core duality, including weighted variants, is established in the literature and general game-theory software can optimize a supplied finite game's least core. Such results are acknowledged; the contribution here is the **closed all-population formula and explicit sharp coalition certificates for this particular nonmonotone, tie-valued accuracy game**. Ordinary monotone weighted voting/simple-game power-index results do not directly imply it because this characteristic function rewards correct-label majority within each selected subensemble and is not a simple game.

## Limitations

This characterizes the optimal maximum deficit and constructs a type-symmetric optimizer; it does not characterize every nonsymmetric point in the least-core polytope or the nucleolus. It assumes transferable and possibly negative payoff credits, a single binary test example, uniformly random tie-breaking, and additive rather than relative coalition deficits. Results for positive allocations, multiclass models, or dataset averages require separate analysis. Literature comparisons do not establish publication priority over every unpublished or unindexed manuscript; independent scientific assessment is outstanding.

## References

1. I. Sarpe, T. Georgakopoulos, and A. Gionis, *Exact power indices for plurality-voting ensembles*, arXiv:2610.17980v1, first public October 13, 2026. https://arxiv.org/html/2610.17980v1
2. *Weighted nucleoli and dually essential coalitions*, *International Journal of Game Theory*, general definitions and dual least-core characterization. https://doi.org/10.1007/s00182-019-00689-x
3. TUGLab reference manual, `leastcore` function and definition of the additive \(\varepsilon\)-core. https://mirror.linux.duke.edu/cran/web/packages/TUGLab/refman/TUGLab.html
