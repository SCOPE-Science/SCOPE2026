# A bivariate Touchard–Riordan law for simple chords and crossings

## Finding

For every integer \(n\ge2\), uniformly match \(2n\) labeled points on a circle in pairs. A *simple chord* joins cyclically consecutive points (including the pair joining the first and last points). Let \(S_n\) be the number of simple chords and \(X_n\) the number of unordered pairs of geometrically crossing chords. Set

\[
T_m(q)=\sum_{M\in\mathcal M_{2m}}q^{X(M)},\qquad T_0(q)=1,
\]

where \(\mathcal M_{2m}\) is the set of perfect matchings on \(2m\) cyclically ordered points; \(T_m\) is the classical Touchard–Riordan crossing polynomial. Define

\[
c_{n,k}=\frac{2n}{2n-k}\binom{2n-k}{k}\qquad(0\le k\le n).
\]

**The exact bivariate refinement** is

\[
\boxed{\sum_{M\in\mathcal M_{2n}}s^{S(M)}q^{X(M)}
=\sum_{k=0}^{n}c_{n,k}(s-1)^kT_{n-k}(q).}
\tag{1}
\]

Thus every joint probability is an explicitly determined polynomial coefficient divided by \((2n-1)!!\). For each choice of \(k\) pairwise endpoint-disjoint simple chords, conditioning on all those chords being present leaves the crossing count exactly distributed as \(X_{n-k}\); additional simple chords are not forbidden.

The joint law yields the exact negative dependence

\[
\begin{aligned}
\mathbb E S_n&=\frac{2n}{2n-1},
&\operatorname{Var}(S_n)&=\frac{4n(n-1)}{(2n-1)^2},\\
\mathbb E X_n&=\frac{n(n-1)}6,
&\operatorname{Var}(X_n)&=\frac{n(n-1)(n+3)}{45},\\
\operatorname{Cov}(S_n,X_n)&=-\frac{2n(n-1)}{3(2n-1)},
&\boxed{\operatorname{Corr}(S_n,X_n)&=-\sqrt{\frac5{n+3}}.}
\end{aligned}
\tag{2}
\]

The correlation is \(-1\) at \(n=2\), strictly between \(-1\) and zero at every \(n\ge3\), and asymptotic to \(-\sqrt{5/n}\).

## Assumptions and scope

Each endpoint is labeled by its cyclic position; each of the \((2n-1)!!\) perfect matchings has equal probability. Chords are straight line segments between distinct points in strictly convex position, so two chords cross precisely when their endpoints alternate around the circle. Simple means adjacency **modulo** \(2n\), not merely linear adjacency. A crossing is counted once for each unordered pair of distinct chords. No chord endpoints coincide. The theorem makes no claims about nonuniform matchings, collinear arrangements, or an open linear order instead of a circle.

## Proof

**Marked simple-chord deletion.** Write \(E\) for the \(2n\) potential simple chords, the edges of the cycle on the endpoints, and \(I_e(M)\) for the indicator that \(e\) belongs to matching \(M\). Then for each matching,

\[
s^{S(M)}=\prod_{e\in E}\left(1+(s-1)I_e(M)\right)
=\sum_{A\subseteq E}(s-1)^{|A|}\mathbf1\{A\subseteq M\}.
\]

If \(A\) contains two edges with a common endpoint, the corresponding term vanishes. If \(A\) is a matching in the cycle with \(k\) edges, all its chords lie along the boundary of the convex polygon, hence cross none of the other chords. Deleting these \(k\) prescribed pairs gives a bijection between perfect matchings that contain \(A\) and all perfect matchings on the other \(2(n-k)\) cyclically ordered endpoints. The bijection preserves *every* crossing between the remaining chords; crossing number is exactly \(X_{n-k}\), not just equal in expectation. Consequently the \(q\)-weighted sum over matchings containing \(A\) is \(T_{n-k}(q)\).

**Cycle matching multiplicity.** The number of \(k\)-subsets of cycle edges that are endpoint-disjoint is \(c_{n,k}\). Indeed, for \(1\le k\le n\), recording the positive gaps of unselected edges between successive chosen edges gives

\[
\frac{2n}{k}\binom{2n-k-1}{k-1}
=\frac{2n}{2n-k}\binom{2n-k}{k}.
\]

For \(k=0\) the count is one, agreeing with the formula. Summing the marked-deletion identity across these cycle matchings proves equation (1), including the \(k=n\) term with \(T_0=1\).

**Single- and double-marked moments.** A specified potential simple chord is present with probability \(1/(2n-1)\). Two disjoint specified simple chords are simultaneously present with probability \(1/((2n-1)(2n-3))\). There are \(2n\) potential simple chords and \(c_{n,2}=n(2n-3)\) unordered disjoint pairs. Hence

\[
\mathbb E S_n=\frac{2n}{2n-1},\qquad
\mathbb E[S_n(S_n-1)]=\frac{2c_{n,2}}{(2n-1)(2n-3)}=\frac{2n}{2n-1},
\]

which gives the stated variance. There are \(\binom{2n}4\) candidate crossings, each realized with probability \(1/((2n-1)(2n-3))\), so

\[
\mathbb E X_n=\frac{\binom{2n}{4}}{(2n-1)(2n-3)}=\frac{n(n-1)}6.
\]

The classical, exact Touchard–Riordan second moment (see Flajolet–Noy and Paguyo in References) is

\[
\mathbb E[X_n(X_n-1)]=
\frac{n^2(n-1)^2}{36}-\frac{n(n-1)}6+\frac{n(n-1)(n+3)}{45},
\]

which immediately gives \(\operatorname{Var}(X_n)\) in equation (2). This identity can also be obtained by extracting the first two derivatives at \(q=1\) from the classical polynomial formula

\[
T_m(q)=\frac{1}{(1-q)^m}\sum_{j=-m}^{m}(-1)^j\binom{2m}{m+j}q^{j(j-1)/2},
\]

where the right-hand side is interpreted through polynomial cancellation at \(q=1\).

**Mixed covariance and correlation.** Given any fixed simple chord, removing it leaves a uniform diagram with \(n-1\) chords, and no crossings were lost. Thus

\[
\mathbb E[X_n\mid I_e=1]=\frac{(n-1)(n-2)}6,
\]

independently of the position of \(e\). Since \(S_n=\sum_{e\in E}I_e\), linearity of covariance gives

\[
\operatorname{Cov}(S_n,X_n)=\sum_{e\in E}\Pr(I_e=1)
\bigl(\mathbb E[X_n\mid I_e=1]-\mathbb EX_n\bigr)
=\frac{2n}{2n-1}\left(-\frac{n-1}{3}\right).
\]

Both variances are positive for \(n\ge2\). Dividing by their positive square-root product and simplifying yields exactly \(-\sqrt{5/(n+3)}\). At \(n=2\) the circular diagram has three matchings, one crossing and two noncrossing, and the perfect negative correlation is genuine. This completes the proof.

## Verification

The standalone standard-library program `verify.py` independently generates each matching for \(2\le n\le7\), obtaining 3, 15, 105, 945, 10,395, and 135,135 diagrams respectively. It compares the full joint census to equation (1), computes exact rational moments through \(n=13\), separately enumerates cycle-edge matching coefficients, and checks the polynomial quotient in the Touchard–Riordan formula. Running `python3 verify.py` produces `ALL 372 EXACT ASSERTIONS PASSED`. None of these bounded enumerations is used to infer the unrestricted theorem; the deletion proof is all-size, and the classical crossing variance is supplied by the cited exact identity.

## Relationship to prior work

The crossing polynomial and marginal moments are classical Touchard–Riordan/Flajolet–Noy results. Acan studies simple chords and intersection graphs of uniformly random chord diagrams; Paguyo establishes separate limit theorems for crossings and simple chords, including exact marginal crossing variance. Pilaud–Rué analyze enumerations refined by crossing count. Young studies **linear** short chords, which exclude the cyclic boundary pair. The result here combines the two natural statistics in an exact bivariate polynomial via cycle-matching coefficients, giving a conditional-law identity and exact negative correlation rather than reproducing either marginal law. An earlier conditional crossing-variance statement for one prescribed arbitrary chord likewise does not imply the distribution jointly marked by all simple chords.

## Limitations

The result is specialized to uniform perfect matchings on labeled points in cyclic order. It does not describe the correlation of the number of crossings with short chords in an open linear diagram without adjusting the boundary-edge combinatorics. The crossing variance uses an established classical exact moment formula rather than an independently reproduced derivation of its binomial cancellation. Prior-work comparison covers the inspected literature and accessible mathematical records, but does not establish exhaustive historical priority. The exhaustive program stops at seven chords for full matchings and thirteen chords for polynomial moment checks; no independent validation or formal proof-system certification has been performed.

## References

1. P. Flajolet and M. Noy, *Analytic Combinatorics of Chord Diagrams*, INRIA Research Report RR-3914 (2000), https://algo.inria.fr/flajolet/Publications/FlNo00.pdf; crossing-polynomial and moment results.
2. V. Pilaud and J. Rué, *Analytic Combinatorics of Chord and Hyperchord Diagrams with k Crossings*, arXiv:1307.6440v1 (first posted 2013-07-24), https://arxiv.org/abs/1307.6440; crossing-refined chord enumerations.
3. H. Acan, *On a Uniformly Random Chord Diagram and its Intersection Graph*, arXiv:1501.01489v1 (first posted 2015-01-07), https://arxiv.org/abs/1501.01489; simple chords and crossing graph.
4. J. E. Paguyo, *Convergence Rates of Limit Theorems in Random Chord Diagrams*, arXiv:2104.01134v1 (first posted 2021-04-02), https://arxiv.org/abs/2104.01134; exact marginal moments and the separate limits.
5. D. Young, *Linear k-Chord Diagrams*, arXiv:2004.06921, https://arxiv.org/abs/2004.06921; related noncyclic short-chord model.
