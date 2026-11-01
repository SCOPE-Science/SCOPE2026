# An exact linear-to-quadratic near-diameter tail transition on Johnson metric networks

## Finding

Let \(k\ge3\) and \(n\ge2k+1\) be integers. Give every edge of the Johnson graph \(J(n,k)\) length one and equip the resulting **continuous metric graph** with intrinsic shortest-path distance. Let \(X,Y\) be independent points sampled uniformly from its total edge arclength, and put \(D=d(X,Y)\). Define the exact edge count
\[
M_{n,k}=\frac{k(n-k)}2\binom nk.
\]
For **every** \(0<\varepsilon<1/2\), the following two identities hold.

* At the critical one-element-overlap size \(n=2k+1\), the continuous diameter is \(k+1/2\), and
\[
\boxed{\Pr\bigl(D>k+\tfrac12-\varepsilon\bigr)
=\frac{2k}{M_{2k+1,k}}\left[\varepsilon+(k-1)\varepsilon^2\right].}
\]
* Whenever \(n\ge2k+2\), the continuous diameter is \(k+1\), and
\[
\boxed{\Pr\bigl(D>k+1-\varepsilon\bigr)
=2\frac{\binom{n-k-1}{k+1}}{\binom n{k+1}}\varepsilon^2.}
\]

Thus, at fixed \(k\ge3\), increasing the ground-set size from \(2k+1\) to \(2k+2\) changes the exponent of the upper-distance tail from one to two. These are *exact identities on a nonzero interval*, not just asymptotic statements. The continuum diameters themselves were already established in the cited Johnson-graph hyperbolicity literature; the assertion here concerns the arclength-pair distribution near those diameters.

## Assumptions and scope

The vertices of \(J(n,k)\) are the \(k\)-subsets of \([n]=\{1,\dots,n\}\). Two vertices are adjacent exactly when their symmetric difference has size two. The distance between two vertices \(A,B\) is \(k-|A\cap B|\), but \(D\) uses all points of the **unit-interval edges**, not only vertices or Euclidean chord distances between hypersimplex vertices. The graph is simple, connected and finite; every edge carries arclength one. Independent normalized arclength sampling means each ordered pair of edges has probability \(1/M_{n,k}^2\), followed by independent uniform coordinates on those edges. The strict event sign is immaterial to probability because the distribution has no atoms on the stated upper-tail interval.

The restriction \(k\ge3\) is substantive: at vertex diameter at most two, earlier general tail formulas cover some of the lower-rank special cases. The question here is the higher-diameter family with a nontrivial, parameter-dependent support-intersection transition.

## Proof

**1. Edge supports and distances.** Every edge \(e=\{A_0,A_1\}\) has a uniquely determined \((k-1)\)-element core \(S_e=A_0\cap A_1\), two exceptional elements \(a,b\), and a support \(E=A_0\cup A_1=S_e\cup\{a,b\}\) of size \(k+1\). Conversely, each support \(E\) carries precisely \(\binom{k+1}{2}\) edges, indexed by the unordered exceptional pair. Hence edge supports are uniform among the \(\binom n{k+1}\) possible supports.

For two **different** edges \(e,f\) with ordered endpoints \(A_0,A_1\) and \(B_0,B_1\), parametrize interior points by \(x,y\in[0,1]\) measured from endpoint zero. Every connecting path must first leave the source edge through an endpoint and enter the target edge through an endpoint. Thus, exactly,
\[
d(x,y)=\min_{i,j\in\{0,1\}}
\bigl[k-|A_i\cap B_j|+|x-i|+|y-j|\bigr]. \tag{1}
\]
For the same edge, direct travel gives \(d(x,y)=|x-y|\le1\), which cannot enter either stated upper tail for \(k\ge3\). Formula (1) is used only for distinct edges.

**2. The two diameter values.** For \(n=2k+1\), two supports of size \(k+1\) must intersect. Therefore some vertex endpoint pair has distance at most \(k-1\). Relabel it as \((A_0,B_0)\). Using that pair and the opposite pair of endpoints in (1) gives
\[
d(x,y)\le\min\{k-1+x+y,\,k+2-x-y\}\le k+\tfrac12.
\]
Choose the supports to intersect in precisely one element, exceptional on both edges. Then the four endpoint distances are \(k-1,k,k,k\); the bound is attained on a line segment with \(x+y=3/2\). Hence the diameter is \(k+1/2\).

For \(n\ge2k+2\), each vertex-to-vertex distance is at most \(k\); traveling from an interior point to its nearer endpoint on each of the two edges gives diameter at most \(k+1\). Two disjoint \((k+1)\)-element supports exist; for any edges with these supports, all four endpoint distances are \(k\), and their two midpoints have distance \(k+1\). This gives the second diameter.

**3. Exact areas of upper-tail regions.** Write \(h(u)=\min\{u,1-u\}\). If two edge supports are disjoint, every endpoint-pair distance equals \(k\), so (1) reduces to \(k+h(x)+h(y)\). For \(0<\varepsilon<1/2\), the area of the region where this exceeds \(k+1-\varepsilon\) is the area of the diamond
\[
|x-\tfrac12|+|y-\tfrac12|<\varepsilon,
\]
namely \(2\varepsilon^2\). If the supports intersect, some endpoint distance is at most \(k-1\); the preceding two-corner bound then shows the distance is at most \(k+1/2\). Consequently **only disjoint supports contribute** to the unbalanced upper tail.

For \(n=2k+1\), denote the supports by \(E,F\). If they share at least two distinct elements, the four cross-endpoint intersection cells form a nonempty pattern covering both endpoint rows and both endpoint columns: no two distinct elements of a \((k+1)\)-support can be exclusive to the same endpoint of its edge. Every such two-by-two pattern contains a diagonal matching of two cells with intersection at least one. Applying (1) using those opposite cells gives \(d\le k\), hence no upper-tail contribution when \(\varepsilon<1/2\).

It remains to assume \(E\cap F=\{z\}\). There are four possible placements of \(z\) relative to the cores and exceptions of \(e,f\). If \(z\) lies in both cores, all four endpoint distances are \(k-1\), giving maximum at most \(k\). If \(z\) is exceptional in **both** edges, exactly one endpoint pair has distance \(k-1\); the other three have distance \(k\). After endpoint relabeling, (1) becomes
\[
d(x,y)=k+\min\{-1+x+y,\,1+x-y,\,1-x+y,\,2-x-y\}.
\]
For \(0<\varepsilon<1/2\), the event \(d>k+1/2-\varepsilon\) is exactly the strip
\[
\tfrac32-\varepsilon<x+y<\tfrac32+\varepsilon
\]
inside the unit square. Indeed, the two cross inequalities are automatic in this strip because \(|x-y|\le2-(x+y)\) there. Its area is precisely \(\varepsilon\).

If \(z\) is exceptional in exactly one edge and in the core of the other, exactly two endpoint distances equal \(k-1\), lying in one row or one column; the remaining two equal \(k\). After interchanging edges if needed, (1) simplifies to \(d(x,y)=k-1+x+h(y)\). Thus the near-diameter condition is
\[
(1-x)+|y-\tfrac12|<\varepsilon,
\]
a boundary triangle region of area \(\varepsilon^2\). These are all possible contributions.

**4. Exact counts.** Fix an edge \(e\) with support \(E\). At \(n=2k+1\), the complement of \(E\) has size \(k\). To have \(E\cap F=\{z\}\), the other support is uniquely \(F=([n]\setminus E)\cup\{z\}\). There are \(2k\) choices of a partner edge \(f\) with \(z\) exceptional in both: two choices of the exceptional point of \(e\), followed by \(k\) choices of its partner exception in \(f\). There are \(2\binom{k}{2}=k(k-1)\) choices with \(z\) exceptional in \(e\) and core in \(f\), and \((k-1)k\) with \(z\) core in \(e\) and exceptional in \(f\). The other placements have no contribution. Since \(e\) was arbitrary and sampled ordered edges have equal weight, division by \(M_{2k+1,k}\) gives the first boxed formula.

For \(n\ge2k+2\), the partner support \(F\) is disjoint from a fixed \(E\) with exact probability
\[
\frac{\binom{n-k-1}{k+1}}{\binom n{k+1}},
\]
as every support contains the same number of edges. Multiplying by the exact conditional diamond area \(2\varepsilon^2\) gives the second boxed formula. This completes the proof. \(\square\)

## Verification

The accompanying standalone Python script `verify_johnson_tail.py` uses only the standard library. It enumerates a complete orbit of edges relative to a fixed edge, evaluates all four endpoint-route inequalities on the unit square, clips rational polygons by exact arithmetic, and sums the areas. Independently of the proof's combinatorial counts, it confirms the two boxed formulas at three rational radii for \((n,k)=(7,3),(8,3),(9,3),(9,4),(10,4)\), plus lower-rank consistency examples. In all cases it also verifies the exact one-cell/two-cell neighbor counts where applicable. The finite checks are supporting evidence; they are not substituted for the quantified proof.

Reproduction: run `python3 verify_johnson_tail.py` from a directory containing the supplied file. The script prints its exact rational comparisons and ends with `ALL EXACT RATIONAL CASES PASSED` on success.

## Relationship to prior work

The 2012 study of geometric (island) Johnson graphs treats connectivity and **vertex** diameter of induced subset graphs, not arclength-pair distances. The 2024 Johnson–Kneser graph paper explicitly establishes the relevant *continuous diameter values* and Gromov-hyperbolicity constants; those diameter values are therefore not asserted as new here. The 2023 continuous mean-distance paper develops general edge-pair integration algorithms, but does not give this near-diameter probability law or support-intersection transition. Previously reported special-case upper tails for unit-edge graphs of vertex diameter at most two do not cover \(k\ge3\), where the Johnson graph's vertex diameter is \(k\). The new conclusion is the exact **probability distribution in a full neighborhood of the diameter**, including its distinct linear and quadratic regimes.

## Limitations

No formula is claimed for \(n=2k\), for \(k\le2\), for \(\varepsilon\ge1/2\), for unequal edge lengths, or for the whole distance distribution away from its upper endpoint. The result concerns the unit-interval intrinsic metric graph; the Euclidean geometry of an ambient hypersimplex is different. The originality comparison uses accessible literature and research records and does not establish absolute historical priority. Independent external validation has not been performed.

## References

1. C. Bautista-Santiago et al., *On the Connectedness and Diameter of a Geometric Johnson Graph*, arXiv:1202.3455, first public version 2012-02-15. The geometric island-graph setting is distinct from the continuous metric graph here.
2. J. Méndez, R. Reyes, J. M. Rodríguez and J. M. Sigarreta, *Gromov hyperbolicity of Johnson and Kneser graphs*, Aequationes Mathematicae 98 (2024), 661–686, DOI 10.1007/s00010-024-01076-y. In particular, Section 3 gives the continuous Johnson-graph diameters.
3. D. Garijo, A. Márquez and R. I. Silveira, *Continuous Mean Distance of a Weighted Graph*, Results in Mathematics 78 (2023), article 139, DOI 10.1007/s00025-023-01902-w. This establishes general continuous mean-distance methods, not the upper-tail identities.
