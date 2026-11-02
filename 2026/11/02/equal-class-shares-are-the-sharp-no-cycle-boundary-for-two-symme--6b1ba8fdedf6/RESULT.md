# Equal class shares are the sharp no-cycle boundary for two symmetric-link preference populations

## Finding

**Theorem (sharp two-class majority boundary).** Let \(I\) be any finite set of at least three alternatives. Let \(F:\mathbb R\to(0,1)\) be continuous and strictly increasing, with \(F(-z)=1-F(z)\), \(\lim_{z\to-\infty}F(z)=0\), and \(\lim_{z\to+\infty}F(z)=1\). For class scores \((u_i)_{i\in I},(v_i)_{i\in I}\in\mathbb R^I\) and class share \(w\in[0,1]\), define

\[
P_{ij}(w)=wF(u_i-u_j)+(1-w)F(v_i-v_j),\qquad i\ne j.
\]

The pairwise majority relation \(i\succeq_w j\) defined by \(P_{ij}(w)\ge\tfrac12\), with equality as indifference, is a weak order **for every choice of scores and every finite alternative set** if and only if

\[
\boxed{w\in\{0,\tfrac12,1\}.}
\]

At equal class shares the complete pairwise relation, including ties, is represented by the additive scores:

\[
\boxed{\operatorname{sgn}(P_{ij}(1/2)-\tfrac12)
=\operatorname{sgn}((u_i+v_i)-(u_j+v_j)).}
\]

For every \(0<w<1\) with \(w\ne\tfrac12\), there exist **three alternatives** and two class score vectors producing a strict Condorcet cycle \(A\succ_w B\succ_w C\succ_w A\). Thus the class-share exception is sharp for each admissible link, not merely for some specially chosen noise law. Three alternatives and two classes are minimal for this phenomenon within the stated model.

## Assumptions and scope

Each pair is compared using one randomly drawn latent class: class 1 has probability \(w\) and follows the same symmetric increasing difference link \(F\) at every pair, while class 2 has probability \(1-w\) and uses that same link on its own scores. The class draw may differ across pairwise observations; the assertion concerns the exact population choice probabilities, not a finite-sample voting realization. A common symmetric link covers two-component Bradley–Terry–Luce models (logistic link) and common-variance Thurstone models (Gaussian link). Different links or asymmetric class-specific noise are outside the theorem.

A weak order means a complete, transitive relation; the majority indifference relation must be transitive too. All claims permit equal scores and exact majority ties. The fixed-share iff quantifies over *all* score vectors and all finite sets with at least three alternatives. It does not assert a cycle for every score assignment at an unequal share.

## Proof

**1. The equal-share identity.** Symmetry implies \(F(0)=\tfrac12\). Set \(G(z)=F(z)-\tfrac12\). Then \(G\) is odd and strictly increasing. For arbitrary real \(a,b\),

\[
\operatorname{sgn}(G(a)+G(b))
=\operatorname{sgn}(G(a)-G(-b))
=\operatorname{sgn}(a+b),
\]

where zero is included in the equivalence. Apply this with \(a=u_i-u_j\), \(b=v_i-v_j\) to obtain the boxed sign identity. Hence majority comparison at \(w=\tfrac12\) is exactly comparison of \(u_i+v_i\), a weak order. At \(w=0\) or \(w=1\), the strict monotonicity of \(F\) similarly gives the individual class's score order.

**2. An explicit strict cycle at every other share.** Swapping class names replaces \(w\) by \(1-w\), so it suffices to consider \(0<w<\tfrac12\). Put

\[
h=\frac{1}{2(1-w)}\in(\tfrac12,1),\qquad
z=F^{-1}(h)>0.
\]

Because \(F\) is continuous strictly increasing onto \((0,1)\), the inverse exists. Choose \(d\) strictly between \(z/2\) and \(z\). For a positive parameter \(K\), give the three alternatives the two class-score vectors

\[
(u_A,u_B,u_C)=(2K,K,0),\qquad
(v_A,v_B,v_C)=(0,d,2d).
\]

The three directed pairwise majority probabilities are

\[
\begin{aligned}
P_{AB}=P_{BC}&=wF(K)+(1-w)F(-d),\\
P_{CA}&=wF(-2K)+(1-w)F(2d).
\end{aligned}
\]

The first quantity converges as \(K\to\infty\) to

\[
1-(1-w)F(d)>1-(1-w)h=\tfrac12,
\]

because \(d<z\). The second has the uniform strict lower bound

\[
P_{CA}\ge(1-w)F(2d)>(1-w)F(z)=\tfrac12,
\]

because \(2d>z\). Consequently any sufficiently large *finite* \(K\) produces three strict pairwise majorities \(A\succ B\), \(B\succ C\), and \(C\succ A\), violating transitivity. Interchange the two classes for \(\tfrac12<w<1\). This also establishes minimality in alternative count: a strict directed cycle cannot occur on fewer than three alternatives; one class alone induces a score order.

**3. A rational Bradley–Terry–Luce witness and uniform parameter construction.** For positive component worths \(a_i,b_i\), set

\[
P_{ij}=w\frac{a_i}{a_i+a_j}+(1-w)\frac{b_i}{b_i+b_j}.
\]

For every \(0<w<\tfrac12\), define \(q=1-2w\), \(t=(1-w)/q\) and choose any positive \(k>(3-4w)/q\). Use

\[
(a_A,a_B,a_C)=(k^2,k,1),\qquad
(b_A,b_B,b_C)=(1,t,t^2).
\]

Here \(tq=1-w<1\), while \(t^2q=(1-w)^2/q>1\) since \((1-w)^2-q=w^2>0\). Thus

\[
P_{AB}=P_{BC}=w\frac{k}{k+1}+(1-w)\frac1{1+t}>\tfrac12,
\]

where rearrangement of the first inequality gives exactly \(k>(3-4w)/q\), and

\[
P_{CA}=w\frac1{1+k^2}+(1-w)\frac{t^2}{1+t^2}>\tfrac12
\]

by \(t^2q>1\). At \(w=1/3\), take \(k=10\), \(t=2\). The component worths are \((100,10,1)\) and \((1,2,4)\), and the strict cycle probabilities are exactly

\[
\boxed{P_{AB}=P_{BC}=\frac{52}{99},\qquad P_{CA}=\frac{271}{505}.}
\]

At equal shares the logistic formula moreover yields the exact margin identity

\[
P_{ij}(1/2)-\frac12
=\frac{a_ib_i-a_jb_j}{2(a_i+a_j)(b_i+b_j)},
\]

so its majority ordering is the ordering by products of worths. This is equivalent to ordering by the sums of log-worths; it is **not** a claim that every complete mixed choice probability has a single-component logistic representation. The theorem follows.

## Verification

The standalone `checker.py` uses only Python's standard-library exact rational arithmetic. It checks the displayed rational cycle, both cycle directions for \(127\) unequal rational weights, the explicit parameter inequalities, and every three-alternative pair among all \(4^6\) ordered pairs of worth arrays with worths in \(\{1,2,3,5\}\) at equal shares, including ties. It reports **25,215 exact rational assertions passed**. The infinite statements over every weight and every admissible link are supported by the analytic proof above, not by this finite computation. Execute: `python3 checker.py` in the extracted directory.

## Relationship to prior work

Regenwetter, Dana and Davis-Stober (2010) formalize weak stochastic transitivity and convex mixtures of transitive latent preference orders, showing that population-level majority consistency is distinct from a model of individually transitive responses. That larger mixture class permits majority cycles, but its general polytope and test results do not imply an exact two-class, common-link, half-share characterization. Zhao, Piech and Xia (2016) study the identifiability and estimation of mixtures of Plackett–Luce rankings, a different logical property from the weak-order phase boundary proved here. Makhijani and Ugander (2019) construct intransitivity using a majority vote *within each pair* of three independent random-utility coordinates; that nonlinear three-coordinate voting rule is not the convex, two-latent-class probability mixture studied here. The foundational single-class stochastic transitivity of common-noise Thurstone and BTL models is known and not claimed as new.

## Limitations

The theorem requires a shared strictly increasing symmetric pairwise link, and describes population-majority **signs** rather than precise probability ordering, strong stochastic transitivity or inference from finite observations. At unequal class shares cycles are *possible* for some scores, not necessary for every pair of score vectors. The explicit construction may use extreme utilities when shares approach one-half; it gives no uniform lower bound on the three cycle margins as \(w\to\tfrac12\). Prior literature on general mixture and social-choice majority paradoxes makes exact historical priority provisional. The model does not validate an empirical description of any particular voting or consumer population.

## References

1. M. Regenwetter, J. Dana and C. P. Davis-Stober (2010), *Testing Transitivity of Preferences on Two-Alternative Forced Choice Data*, Frontiers in Psychology 1:148; first publicly published 2010-12-13. https://doi.org/10.3389/fpsyg.2010.00148
2. Z. Zhao, S. Piech and L. Xia (2016), *Learning Mixtures of Plackett-Luce Models*, first arXiv submission 2016-03-23. https://arxiv.org/abs/1603.07323 ; conference full text https://proceedings.mlr.press/v48/zhaob16.pdf
3. A. Makhijani and J. Ugander (2019), *Parametric Models for Intransitivity in Pairwise Rankings*, Proceedings of The Web Conference. https://doi.org/10.1145/3308558.3313717 ; open full text https://www.researchgate.net/publication/333060254_Parametric_Models_for_Intransitivity_in_Pairwise_Rankings
4. X. Zhang, X. Zhang, P.-L. Loh and Y. Liang (2022), *On the Identifiability of Mixtures of Ranking Models*. https://arxiv.org/abs/2201.13132 (identifiability comparator; abstract inspected).
