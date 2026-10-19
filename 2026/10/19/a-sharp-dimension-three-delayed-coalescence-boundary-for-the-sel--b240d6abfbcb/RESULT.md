# A sharp dimension-three delayed-coalescence boundary for the self-power escort map

## Finding

For an integer \(n\ge 3\), let \(\Delta_{n-1}=\{p\in[0,1]^n:\sum_{i=1}^n p_i=1\}\). Consider the discrete-time self-power escort transformation
\[
T_n(p)_i=\frac{h(p_i)}{\sum_{j=1}^n h(p_j)},\qquad
h(x)=\exp(x\log x),\quad h(0)=1.
\]
Here and below \(0\log0=0\). Two distinct trajectories *first coalesce at time* \(k\ge1\) if \(T_n^k(p)=T_n^k(q)\) but \(T_n^{k-1}(p)\ne T_n^{k-1}(q)\).

**Theorem (sharp dimension transition).**

1. For every \(n\ge4\), the restriction of \(T_n\) to its first-step image \(T_n(\Delta_{n-1})\) is injective. In particular, for every \(p,q\in\Delta_{n-1}\) and integer \(k\ge1\),
\[
T_n^k(p)=T_n^k(q)\quad\Longleftrightarrow\quad T_n(p)=T_n(q).
\]
Distinct trajectories therefore never first coalesce at a time greater than one.

2. For \(n=3\), an **open interval of nonuniform target states** on the permutation-symmetric line has at least two distinct preimages *within the first-step image*. More explicitly, define
\[
P(s)=\left(s,\frac{1-s}{2},\frac{1-s}{2}\right),\qquad
F(s)=\frac{s^s}{s^s+2((1-s)/2)^{(1-s)/2}},
\]
with continuous endpoint values. Let \(z=\sqrt2-1\), and let \(s_*\) be the unique root of
\[
e^3s^2(1-s)=2\quad\text{in }(1/3,z).
\]
For every
\[
y\in\left(F(s_*),\,\min\{F(z),1/3\}\right),
\]
there are distinct \(p,q\in\Delta_2\) for which
\[
T_3(p)\ne T_3(q),\qquad T_3^2(p)=T_3^2(q)=P(y).
\]
Consequently, dimension three admits a continuum of genuine second-step merger targets despite global convergence to the uniform state. The interval above is nonempty and excludes the uniform target.

## Assumptions and scope

All coordinates are labelled and nonnegative, and no stochastic perturbation or external exponent parameter is used. The continuous convention \(h(0)=1\) matters: boundary points are activated in one iteration. The first assertion concerns only integers \(n\ge4\), while the existence assertion concerns exactly three coordinates and a symmetry-invariant one-dimensional family. Neither assertion claims global injectivity on the *whole* simplex; indeed several distinct initial states may share their first image. No claim is made about all possible merger depths in dimension three.

## Proof

**Step 1: a strict monotonicity region reached after one step.** Since \(-1/e\le x\log x\le0\) for \(0\le x\le1\),
\[
e^{-1/e}\le h(x)\le1,\qquad
\frac{e^{-1/e}}n\le T_n(p)_i\le\frac{e^{1/e}}n.
\]
These bounds apply to *every* first image, and therefore to every subsequent image. To show that the upper bound is strictly below \(1/e\) for \(n\ge4\), it suffices to prove \(e^{1+1/e}<4\). For an entirely elementary strict verification, use
\[
e>1+1+\tfrac12+\tfrac16=\tfrac83,
\qquad
\log2=2\sum_{j=0}^\infty\frac{3^{-(2j+1)}}{2j+1}
>2\left(\tfrac13+\tfrac1{81}\right).
\]
Consequently
\[
\log4>\frac{112}{81}>\frac{11}{8}>1+\frac1e,
\]
so the required inequality holds. Thus, for every \(n\ge4\), all coordinates of every first image belong strictly to \((0,1/e)\).

**Step 2: injectivity below the scalar minimum.** Put \(f(x)=x\log x\). Its derivative \(f'(x)=1+\log x\) is strictly negative on \((0,1/e)\). Suppose that \(a,b\in\Delta_{n-1}\) have all coordinates in this interval and satisfy \(T_n(a)=T_n(b)\). Equality of normalized positive weights implies a common multiplier \(\lambda>0\), so
\[
f(a_i)-f(b_i)=\log\lambda\qquad\text{for every }i.
\]
If \(\log\lambda>0\), strict decrease forces \(a_i<b_i\) for every index, contradicting equality of coordinate sums. If \(\log\lambda<0\), it similarly forces \(a_i>b_i\) everywhere. Hence \(\log\lambda=0\), and strict decrease gives \(a=b\). The map is therefore injective on its first image when \(n\ge4\). For \(k\ge2\), apply this injectivity successively to the pairs of points at times \(k-1,k-2,\dots,1\) to obtain the first assertion. The reverse implication follows by applying further iterations.

**Step 3: invariant symmetric line in three coordinates.** Direct substitution yields \(T_3(P(s))=P(F(s))\). In particular,
\[
F(0)=\frac1{1+\sqrt2}=z,
\qquad F(1/3)=1/3.
\]
Continuity therefore shows that every \(P(s)\) with \(s\in[1/3,z]\) lies in the image \(T_3(\Delta_2)\): simply take a suitable preimage \(P(u)\), \(u\in[0,1/3]\).

**Step 4: a fold *inside that image*.** On \((0,1)\), differentiation of the log-odds gives
\[
\frac{d}{ds}\log\frac{F(s)}{1-F(s)}
=\frac32+\log s+\frac12\log\frac{1-s}{2}=:g(s).
\]
The logistic derivative is positive, so \(F'(s)\) has the sign of \(g(s)\). Moreover
\[
g'(s)=\frac{2-3s}{2s(1-s)}>0\quad\text{for }s\in[1/3,z],
\]
and
\[
2g(s)=\log\!\left(\frac{e^3s^2(1-s)}2\right).
\]
At \(s=1/3\), \(2g(1/3)=3-3\log3<0\), since \(e<3\). At \(s=z\), direct algebra gives
\[
z^2(1-z)=10-7\sqrt2>\frac1{10},
\]
where the final inequality is equivalent to \(99>70\sqrt2\), verified by \(9801>9800\). Also \(e^3>\sum_{j=0}^8 3^j/j!=89641/4480>20\). Therefore \(e^3z^2(1-z)>2\), so \(g(z)>0\). By strict monotonicity, \(g\) has a unique zero \(s_*\in(1/3,z)\). Hence \(F\) decreases strictly on \([1/3,s_*]\) and increases strictly on \([s_*,z]\), with a strict minimum at \(s_*\).

**Step 5: every target in an open interval merges.** Take any \(y\in(F(s_*),\min\{F(z),1/3\})\). Strict monotonicity and the intermediate-value theorem give two distinct scalars
\[
a\in(1/3,s_*),\qquad b\in(s_*,z),\qquad F(a)=F(b)=y.
\]
Both \(P(a)\) and \(P(b)\) belong to \(T_3(\Delta_2)\) by Step 3: choose \(u,v\in[0,1/3]\) with \(F(u)=a\) and \(F(v)=b\). Then, setting \(p=P(u)\), \(q=P(v)\),
\[
T_3(p)=P(a)\ne P(b)=T_3(q),
\qquad T_3^2(p)=P(y)=T_3^2(q).
\]
The endpoint inequalities in the definition of \(y\) ensure the interval is nonempty and \(y<1/3\), so the coalescence targets are nonuniform. This completes the proof. \(\square\)

## Verification

The standalone `VERIFY.py` uses only the Python standard library and reproduces a representative fold and two-step merger with bisection. It checks the two scalar derivative signs and the dimension-four core inequality, then verifies that distinct first images agree after the next update to floating-point accuracy. To run: `python VERIFY.py`. Example outputs include \(s_*\approx0.411252770579\), a nonuniform target \(y\approx0.332129325852\), first-image separation approximately \(0.004177616509\), and second-image discrepancy below \(10^{-14}\). This computation is illustrative; the assertions for all inputs, dimensions and infinitely many targets follow from Steps 1–5, not from finite sampling.

## Relationship to prior work

Lei Zhou, *Self-Power Escort Dynamics on the Probability Simplex*, version 1, posted May 8, 2026, proves one-step core entrance, global Hilbert-metric convergence, local normal forms, and a **complete classification of the fiber of the uniform point under one step**. In particular, its Proposition 2 supplies the broad core bounds used in Step 1 and its Theorem 4 classifies one-step uniformizers. The present theorem instead concerns whether **different first images can subsequently become equal at a nonuniform state**, and whether two images can collide after time one. A one-step fiber classification at the uniform equilibrium neither states nor determines these nonuniform delayed mergers. The high-dimensional no-new-merger conclusion uses the core bound and a simplex normalization argument; the dimension-three counterphenomenon requires the additional fold and exact sign analysis in Steps 3–5.

The general theory of unimodal interval maps and normalized positive maps provides contextual language for folds and injectivity; no assertion is made that these techniques are themselves new. Searches for normalized self-power escort images, eventual injectivity, delayed merging, fibers and aliases did not identify a directly covering theorem. Search absence is not a mathematical proof of priority.

## Limitations

The three-dimensional construction is confined to a permutation-symmetric invariant line; it does not classify all fibers or all possible first-coalescence times in \(\Delta_2\). The transition is specific to the self-power escort map with the continuous boundary rule, not a universal statement about general escort transforms. The dimension-four conclusion is a logical consequence of the known regularizing bounds together with a new injectivity argument, while the delicate dimensional obstruction in three coordinates is the distinct added content. Bibliographic priority has been checked against the directly motivating full text and indexed related mathematical records, but no exhaustive proof of novelty is possible.

## References

1. Lei Zhou, *Self-Power Escort Dynamics on the Probability Simplex*, Preprints.org, version 1, posted 2026-05-08, https://www.preprints.org/manuscript/202605.0532 (Sections 2–4 and 6, especially Proposition 2 and Theorem 4).
2. J. Milnor and W. Thurston, *On iterated maps of the interval*, in *Dynamical Systems (College Park, MD, 1986–87)*, Lecture Notes in Mathematics 1342, Springer (1988). General background on folding and interval iteration only; it does not discuss the specific escort map.
