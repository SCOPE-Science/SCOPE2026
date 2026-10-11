# Universal escape direction and exact superexponential scale for an even-degree secant model

## Finding
For every nonzero real \(a\) and every even integer \(d\ge 2\), consider
\[
T_{a,d}(x,y)=\bigl(y-a(x+y)^d,\;y-2a(x+y)^d\bigr).
\]
Every forward orbit \((x_n,y_n)=T_{a,d}^{n}(x_0,y_0)\) satisfies exactly one of the following alternatives: it converges to the origin, or both coordinates diverge with sign opposite to \(a\). In the latter case, writing \(r_n=|x_n+y_n|\),
\[
\frac{(x_n,y_n)}{x_n+y_n}\longrightarrow\left(\frac13,\frac23\right),
\qquad
r_{n+1}=3|a|r_n^d\bigl(1+O(r_n^{1-d})\bigr).
\]
There is a uniquely determined positive number
\[
H(x_0,y_0)=\lim_{n\to\infty}\frac{\log r_n}{d^n}>0
\]
for each escaping orbit, and the exact multiplicative escape-scale asymptotic is
\[
r_n=(3|a|)^{-1/(d-1)}\exp\bigl(H(x_0,y_0)d^n+o(1)\bigr).
\]
The universal prefactor is independent of the escaping initial condition; the positive escape height \(H\) is not.

## Assumptions and scope
The phase space is \(\mathbb R^2\), the time variable \(n\) is a nonnegative integer, the degree \(d\) is even and at least two, and \(a\in\mathbb R\setminus\{0\}\). No other regularity, transversality, or genericity assumptions are made, including on the initial point. For \(a>0\) the escaping direction is the negative ray \((1,2)\); for \(a<0\) it is the positive ray. These are statements about the exact truncated polynomial model, not about the original secant algorithm from which the model arose. The estimates concern sufficiently large iterations of escaping orbits; they do not give a uniform finite onset time for arbitrary initial data.

## Proof
**Sign reduction.** For even \(d\), setting \(b=|a|>0\) gives \(T_{-b,d}(-x,-y)=-T_{b,d}(x,y)\). It is therefore enough to consider \(a>0\). Write \(s_n=x_n+y_n\). The exact second-coordinate recurrence is
\[
y_{n+1}=y_n-2a s_n^d\le y_n.
\]
If the monotone sequence \((y_n)\) is bounded below, it has a finite limit \(L\). Summing the recurrence shows \(\sum_{n\ge0}s_n^d<\infty\) and hence \(s_n\to0\). Thus \(x_n=s_n-y_n\to-L\). On the other hand, the first-coordinate recurrence \(x_{n+1}=y_n-a s_n^d\to L\); hence \(L=-L=0\), so both coordinates tend to zero. If \((y_n)\) is not bounded below, then \(y_n\to-\infty\), and \(x_{n+1}\le y_n\) forces \(x_n\to-\infty\) as well. This proves the global dichotomy without asserting anything about the rate of convergence on the basin.

**Exact recurrence at infinity.** For an escaping orbit, fix an index after which \(x_n,y_n<0\), so \(r_n=-s_n>0\). Define \(z_n=x_n-y_n\). The two coordinate recurrences give, for \(n\ge1\),
\[
z_n=a r_{n-1}^d\ge0,\qquad
r_{n+1}=r_n+z_n+3a r_n^d.
\]
Consequently \(r_n\ge 3a r_{n-1}^d\), so \(0\le z_n\le r_n/3\). For sufficiently large \(n\),
\[
r_{n+1}=3a r_n^d(1+e_n),\quad
e_n=\frac{r_n+z_n}{3a r_n^d},\quad
0<e_n\le\frac4{9a}r_n^{1-d}\longrightarrow0.
\]
The coordinate formulas also imply
\[
x_{n+1}=-a r_n^d+O(r_n),\qquad
y_{n+1}=-2a r_n^d+O(r_n),
\]
where \(|y_n|\le r_n\) for sufficiently large \(n\). Dividing by their sum proves the universal limiting direction, with coordinate errors of order \(r_n^{1-d}\).

**Exact escape height and prefactor.** Let \(c=3a\) and put \(w_n=\log r_n+\log c/(d-1)\). The preceding exact recurrence gives
\[
w_{n+1}=d w_n+\log(1+e_n).
\]
Since \(e_n\to0\), the correction terms are bounded. Therefore \(d^{-n}w_n\) has a finite limit \(H\), as follows by summing the convergent series of increments \(d^{-n-1}\log(1+e_n)\). Since \(r_n\to\infty\), we may start sufficiently late with \(w_n>0\), and the corrections are strictly positive; hence \(H>0\). More precisely,
\[
H d^n-w_n=\sum_{k=n}^{\infty}d^{n-k-1}\log(1+e_k)\longrightarrow0,
\]
because the tail is bounded by \(\sup_{k\ge n}\log(1+e_k)/(d-1)\). Thus
\[
\log r_n=H d^n-\frac{\log(3a)}{d-1}+o(1),
\]
which proves the asserted exact prefactor. Reflecting all coordinates proves the result for \(a<0\), with \(a\) replaced by \(|a|\) in the absolute-value escape scale. Every limit and estimate above applies to the actual iterates, not to a formal asymptotic recurrence.

## Verification
The companion standalone script `verify_escape.py` executes exact-integer iterations for the parameter pairs \((a,d)\in\{(1,2),(-1,2),(1,4),(-1,4),(2,2),(-2,2)\}\), checks both coordinate recurrences, the exact signed conjugacy, and the recurrence for \(r_n\) and \(z_n\), and checks finite-iterate convergence of direction and escape-height estimates. The script is corroborative: the proof above establishes the all-initial-condition and all-even-degree statements analytically. It does not use sampled trajectories to assert exhaustive basin coverage.

## Relationship to prior work
Fontich, Garijo, and Jarque introduced this precise model and proved the structure of its basin and boundary for even degree; their Theorem A(a) states that the attracting basin is a compact topological disk bounded by the stable manifold of the origin. Their Section 4, Lemma 4.1, already observes monotonicity of the coordinates, and Lemmas 4.2--4.3 establish basin criteria. The bounded-orbit half of the dichotomy is a direct strengthening of these elementary estimates and is not claimed alone as the novelty. The additional contribution is the **global quantitative behavior of every escaping real orbit**: a single oriented limiting ray, exact degree-\(d\) logarithmic escape height, and the nontrivial universal leading multiplicative constant.

The companion paper arXiv:2405.08812v1 specializes to odd \(d\ge3\) and studies homoclinic intersections and chaotic basin boundaries, not this even-degree escape asymptotic. General polynomial dynamics at infinity may admit Green-function-like constructions, but the present argument gives direct real-global alternatives and precise constants for a degenerate leading homogeneous map without asserting that a generic compactification theorem is new.

## Limitations
This theorem is not a statement about the untruncated secant map or about odd degrees. The escape height is defined through the orbit, not through a closed-form elementary expression in its initial coordinates. No universal rate for orbits converging to the origin, and no location of the basin boundary beyond the original authors' result, is claimed. General polynomial-dynamics methods may cover some normalized-escape behavior abstractly, and independent literature-priority review remains outstanding. Finite checker runs do not replace the all-degree proof.

## References

1. E. Fontich, A. Garijo, X. Jarque, "On the basin of attraction of a critical three-cycle of a model for the secant map," arXiv:2405.08791v1 (first posted 14 May 2024), https://arxiv.org/html/2405.08791v1. Theorem A(a) and Section 4, especially Lemmas 4.1--4.3.
2. E. Fontich, A. Garijo, X. Jarque, "Chaotic dynamics at the boundary of a basin of attraction via non-transversal intersections for a non-global smooth diffeomorphism," arXiv:2405.08812v1 (14 May 2024), https://arxiv.org/html/2405.08812v1. Its standing hypotheses concern odd degree.
3. C. Favre, M. Jonsson, "Dynamical compactifications of \(\mathbb C^2\)," Annals of Mathematics 173 (2011), 211--249, https://annals.math.princeton.edu/2011/173-1/p06. Background on complex polynomial escape and Green functions, not a quoted theorem giving the present real orbit classification.
