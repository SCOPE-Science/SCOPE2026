# Exact signed double Italian domination of once-subdivided stars
## Finding
For every integer \(q\ge4\), let \(T_q\) be the tree obtained from the star \(K_{1,q}\) by subdividing every edge once. Then its signed double Italian domination number is \[\gamma_{sdI}(T_q)=q+\left\lceil\frac q4\right\rceil+1.\] If \(q\not\equiv1\pmod4\), every minimum signed double Italian dominating function assigns the center value \(1\), assigns value \(3\) to exactly \(\lceil q/4\rceil\) support vertices and value \(-1\) to their leaves, and assigns value \(-1\) to every remaining support with value \(2\) on its leaf. Hence there are \(\binom{q}{\lceil q/4\rceil}\) minimum functions. If \(q=4k+1\) with \(k\ge1\), there are two minimum-function types: the preceding center-\(1\) type with \(k+1\) support vertices of value \(3\), and a center-\(2\) type with exactly \(k\) support vertices of value \(3\); therefore the number of minimum functions is \(\binom{q}{k+1}+\binom{q}{k}=\binom{q+1}{k+1}\). In particular, for the family \(T_{4k}\) used in the foundational paper, \(\gamma_{sdI}(T_{4k})=5k+1\), so its displayed upper bound is exact.

## Assumptions and scope
All graphs are finite, simple, and undirected. For an integer \(q\ge4\), let \(T_q\) be obtained from the star \(K_{1,q}\) by subdividing every edge once. Write \(c\) for the center, and on arm \(i\) write \(v_i\) for the degree-two support vertex and \(u_i\) for its leaf.

A signed double Italian dominating function is a map
\[
f:V(T_q)\to\{-1,1,2,3\}
\]
such that \(f(N[x])\ge1\) for every vertex \(x\); if \(f(x)=-1\), then some subset of \(N(x)\) has total label at least \(3\); and if \(f(x)=1\), then some subset of \(N(x)\) has total label at least \(2\).

## Proof
Fix the center value \(z=f(c)\). The leaf and support constraints leave the following cheapest possibilities on one arm.

When \(z\in\{1,2,3\}\), the unique arm type of weight \(1\) is
\[
(f(v_i),f(u_i))=(-1,2),
\]
and every arm with \(f(v_i)\ne-1\) has weight at least \(2\). Equality at weight \(2\) with \(f(v_i)\ne-1\) occurs only for
\[
(f(v_i),f(u_i))=(3,-1).
\]
If \(r\) arms have support value different from \(-1\), then
\[
\sum_i f(v_i)\le 3r-(q-r)=4r-q.
\]

For \(z=1\), the center closed-neighborhood inequality requires
\[
\sum_i f(v_i)\ge0,
\]
so \(r\ge\lceil q/4\rceil\). Therefore
\[
w(f)\ge 1+q+\left\lceil\frac q4\right\rceil.
\]
Equality forces every exceptional arm to be \((3,-1)\) and every other arm to be \((-1,2)\). Such a labeling is valid because the center sees positive support sum at least \(3\), so it also satisfies the extra condition for a center labeled \(1\).

For \(z=2\), the center inequality gives
\[
\sum_i f(v_i)\ge-1,
\]
hence
\[
w(f)\ge 2+q+\left\lceil\frac{q-1}{4}\right\rceil.
\]
Equality has the same two arm types. For \(z=3\), similarly,
\[
w(f)\ge 3+q+\left\lceil\frac{q-2}{4}\right\rceil.
\]

If \(z=-1\), the arm \((-1,2)\) is no longer feasible because the support closed-neighborhood sum would be \(0\). Every arm has weight at least \(2\), so
\[
w(f)\ge 2q-1.
\]

For every \(q\ge4\), comparison of these four bounds shows
\[
q+\left\lceil\frac q4\right\rceil+1
\]
is the minimum. The center-\(2\) bound ties it exactly when \(q\equiv1\pmod4\); the center-\(-1\) and center-\(3\) bounds are strictly larger.

The equality conditions already classify every optimum. If \(q\not\equiv1\pmod4\), the center is \(1\) and exactly \(\lceil q/4\rceil\) arms are of type \((3,-1)\), giving
\[
\binom{q}{\lceil q/4\rceil}
\]
minimum functions.

If \(q=4k+1\), the center-\(1\) family chooses \(k+1\) arms of type \((3,-1)\), while the center-\(2\) family chooses \(k\) such arms. Thus the number of minimum functions is
\[
\binom{q}{k+1}+\binom{q}{k}
=
\binom{q+1}{k+1}.
\]

For \(q=4k\), the value becomes
\[
4k+k+1=5k+1.
\]

## Verification
The included checker tests the defining signed double Italian conditions directly on every one of the \(4^9\) labelings of \(T_4\) and every one of the \(4^{11}\) labelings of \(T_5\).

Independently, it derives all locally feasible arm states from the defining inequalities and runs an exact dynamic program for every \(4\le q\le60\). The optimum value and the complete optimum count agree with the theorem for every tested \(q\).

## Relationship to prior work
The 2023 paper introducing signed double Italian domination uses exactly the once-subdivided star \(T_{4k}\) in Proposition 2. It constructs a signed double Italian dominating function of weight \(5k+1\) in order to separate signed double Italian domination from signed double Roman domination, but it states only
\[
\gamma_{sdI}(T_{4k})\le5k+1.
\]
The present theorem proves that this bound is exact, extends it from multiples of four to every \(q\ge4\), and classifies and counts all minimum functions.

The same paper gives exact values for paths, stars, and cycles, a lower bound for double stars, and sharp global bounds for trees. Those statements do not imply the once-subdivided-star formula: its general tree lower bound is much smaller on this family. A later survey summarizes the parameter by listing paths, stars, and cycles as the exact named families and does not report the subdivided-star equality.

## Limitations
The theorem concerns the uniform once-subdivision of a star and does not cover unequal spider arm lengths or repeated subdivisions. Small values \(q\le3\) have additional center-label ties and are excluded to keep the structural statement uniform. The finite computations corroborate the proof but do not replace it.

## References
1. A. Almulhim, “Signed double Italian domination,” AIMS Mathematics 8(12) (2023), 30895–30909, DOI 10.3934/math.20231580. Published 17 November 2023.
2. “Varieties of Roman domination IV,” survey article, 2025, section on signed double Italian domination.
