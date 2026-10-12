# Metric fibers of the universal-diversity orbit space have exponentially many higher-arity coordinates

## Finding
Let \(\mathbb U^{\delta}\) be the universal separable ultrahomogeneous diversity obtained from the class of finite diversities. For every \(n\ge 2\), an injective ordered tuple \(\bar a=(a_1,\ldots,a_n)\) is classified up to \(\operatorname{Aut}(\mathbb U^{\delta})\) by the labeled finite diversity it induces on \([n]\). Thus its complete finite orbit invariant consists of the numbers
\[
\delta(A),\qquad A\subseteq[n],\quad |A|\ge2.
\]
There are
\[
m_n=2^n-n-1
\]
such coordinates. The finite diversity cone is full-dimensional in these coordinates, a dimension also recorded in the diversity literature.

Passing to the induced metric keeps only the pair coordinates. Writing
\[
q_n=\binom n2,
\]
the forgetful map from diversity-orbit invariants to pairwise metric invariants is simply the coordinate projection onto those \(q_n\) entries. On a nonempty open set of strict labeled metric profiles, its fibers have exact dimension
\[
\boxed{h_n=2^n-n-1-\binom n2}.
\]
Equivalently, after the pairwise distances are fixed, there remain \(h_n\) locally independent higher-set parameters distinguishing automorphism orbits. Since \(h_2=0\) and \(h_3=1\), pairwise distances first lose orbit information already at arity three.

For three labels, write
\[
t=\delta(\{1,2,3\}).
\]
For a metric triple \((d_{12},d_{13},d_{23})\), the fiber is exactly the interval
\[
\boxed{
\max(d_{12},d_{13},d_{23})
\le t\le
\min(d_{12}+d_{13},d_{12}+d_{23},d_{13}+d_{23})
}.
\]
In particular, the equilateral metric \(d_{12}=d_{13}=d_{23}=1\) has the whole interval \(1\le t\le2\). Every different value of \(t\) is a different diversity-automorphism orbit of ordered triples, despite identical pairwise distances.

## Assumptions and scope
The statement concerns injective ordered tuples in the universal separable ultrahomogeneous diversity. Repeated-coordinate tuples reduce to the corresponding statement on their distinct support. The dimension assertion is local: it says that a nonempty open set of strict metric profiles has full-dimensional fibers of the displayed dimension. It does not assert that every boundary metric has a fiber of the same dimension.

The first-public source used for the model-theoretic structure is Bryant--Nies--Tupper's 2019 Fraïssé paper, whose primary MSC includes 03C30 and 03C52. The older universal-diversity construction is background only. The dimension of the finite diversity cone and the qualitative fact that an induced metric does not determine a diversity are treated as prior results, not as new claims here.

## Proof
Bryant, Nies, and Tupper prove that finite diversities form a Fraïssé class with a universal ultrahomogeneous limit. Universality realizes every labeled finite diversity, while ultrahomogeneity says that two finite labeled substructures with the same diversity values are carried to one another by an automorphism. Therefore injective ordered \(n\)-tuple orbits are in bijection with labeled \(n\)-point diversities.

A diversity is determined by one real coordinate \(\delta(A)\) for each subset \(A\subseteq[n]\) with \(|A|\ge2\), so the ambient coordinate count is \(m_n=2^n-n-1\). To see directly that there are no hidden equality constraints, fix a small \(\varepsilon>0\) and define
\[
\delta_0(A)=
\begin{cases}
0,&|A|\le1,\\
1+\varepsilon|A|,&|A|\ge2.
\end{cases}
\]
Use the standard equivalent form of the diversity axioms: monotonicity together with subadditivity on sets having nonempty intersection. Every nontrivial monotonicity inequality at \(\delta_0\) has positive slack. If \(|A|,|B|\ge2\) and \(A\cap B\ne\varnothing\), then
\[
\delta_0(A)+\delta_0(B)-\delta_0(A\cup B)
=1+\varepsilon|A\cap B|>0.
\]
If one of the overlapping sets is a singleton contained in the other, the corresponding inequality is a tautology rather than a genuine constraint. Hence all genuine linear inequalities have positive slack at \(\delta_0\), so a small box in all \(m_n\) free coordinates consists entirely of diversities. This proves full local dimension \(m_n\).

The induced metric is \(d(i,j)=\delta(\{i,j\})\), so forgetting higher-set values fixes exactly the \(q_n=\binom n2\) pair coordinates. Inside the small box above, vary the pair coordinates in a smaller open box and independently vary every coordinate belonging to a set of size at least three. Fixing a pair profile then leaves a box in exactly
\[
m_n-q_n=2^n-n-1-\binom n2
\]
coordinates. No fiber can have larger dimension because the pair coordinates are fixed. Thus these fibers have exact dimension \(h_n\) on a nonempty open metric stratum.

For \(n=3\), monotonicity gives \(t\ge\max(d_{12},d_{13},d_{23})\). Overlapping subadditivity applied to the two incident edges at each vertex gives
\[
t\le d_{12}+d_{13},\qquad
t\le d_{12}+d_{23},\qquad
t\le d_{13}+d_{23}.
\]
Conversely, the metric triangle inequalities together with these four bounds exhaust the three-point diversity axioms, yielding the stated interval.

## Verification
The bundled `verify.py` uses exact rational arithmetic. It checks the coordinate counts and hidden-dimension formula through \(n=12\); constructs the explicit interior diversity \(\delta_0\); enumerates all nontrivial monotonicity and overlapping-subadditivity inequalities through \(n=8\); derives a positive rational radius for a full coordinate box around \(\delta_0\); and verifies that the number of coordinates left after fixing all pairs is exactly \(h_n\).

Independently, it exhausts all integer metric triples with side lengths from 1 through 6 and all half-integer candidate triple values in the tested range, checking the original diversity axiom directly. In every case, direct validity agrees exactly with the displayed interval criterion. The verifier returns `VERIFY_OK 171758 exact assertions`.

## Relationship to prior work
Bryant--Nies--Tupper prove exact ultrahomogeneity and universality for the Fraïssé limit of finite diversities. Wu--Bryant--Tupper explicitly note that the cone of diversities on an \(n\)-point set has dimension \(2^n-(n+1)\). Poelstra already emphasizes that diversities are not characterized by their induced metrics and gives qualitatively different diversities with the same induced metric. Those ingredients are therefore prior art.

The contribution isolated here is the orbit-theoretic synthesis: exact ultrahomogeneity identifies those finite diversity parameters with automorphism orbits, and the metric-reduct map becomes a coordinate projection whose open fibers have the exact dimension \(2^n-n-1-\binom n2\). The explicit three-point interval identifies the first arity at which metric data cease to determine a diversity orbit. Targeted searches for the exact fiber formula, its automorphism-orbit formulation, and the triple threshold located the structural ingredients but no equivalent statement.

This also sharpens the contrast with the \(L_1\)-diversity subclass: there the cut-coordinate parameter count is smaller, and pairwise-invisible directions do not appear until arity four. No novelty is claimed for the cut-cone facts themselves.

## Limitations
The deduction is short once exact ultrahomogeneity and the finite diversity cone are placed side by side, so an unindexed folklore formulation remains possible. The full-dimensional fiber statement is proved on a nonempty open metric stratum; singular boundary metrics can have smaller fibers. The result concerns labeled injective tuples and does not classify quotient fibers under coordinate permutations. It also does not claim new results about the dimension of the diversity cone itself or the general qualitative failure of induced metrics to determine diversities.

## References
1. D. Bryant, A. Nies, and P. Tupper, *Fraïssé Limits for Relational Metric Structures*, arXiv:1901.02122; Journal of Symbolic Logic 86 (2021), 913--934, DOI:10.1017/jsl.2021.65.
2. P. Wu, D. Bryant, and P. Tupper, *Negative-Type Diversities, a Multi-dimensional Analogue of Negative-Type Metrics*, arXiv:1809.06523; Journal of Geometric Analysis 31 (2021), 1703--1720.
3. A. Poelstra, *On the Topological and Uniform Structure of Diversities*, Journal of Function Spaces and Applications (2013), Article 675057, DOI:10.1155/2013/675057.
4. D. Bryant, A. Nies, and P. Tupper, *A Universal Separable Diversity*, Analysis and Geometry in Metric Spaces 5 (2017), 138--151, DOI:10.1515/agms-2017-0008.
