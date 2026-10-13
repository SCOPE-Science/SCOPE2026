# Metric banana paths admit genus- and gonality-preserving algebraic lifts
## Finding
Let \(\Gamma\) be a metric banana path and put
\[
d=\operatorname{gon}(\Gamma),
\]
where the right-hand side is divisorial gonality, the least degree of a divisor of rank at least \(1\) on \(\Gamma\).

There exist an algebraically closed complete non-Archimedean field \(K\) and a smooth proper connected curve \(X/K\) having \(\Gamma\) as a skeleton such that
\[
g(X)=g(\Gamma)
\qquad\text{and}\qquad
\operatorname{gon}(X)=d.
\]
Mascuch--Teixidor i Bigas prove that divisorial and geometric gonality coincide for metric graphs of pseudocompact type, so this common value is also the geometric gonality of \(\Gamma\).

Thus every metric banana path has an algebraic lift that preserves both genus and gonality exactly.

## Assumptions and scope
A metric banana path is a metric graph whose canonical loopless model becomes a path after every nonempty family of parallel edges is replaced by a single edge. Such graphs are a special case of the metric graphs of pseudocompact type considered by Mascuch--Teixidor i Bigas.

Algebraic gonality of a smooth proper curve over the algebraically closed field \(K\) is the least degree of a divisor of rank at least \(1\), equivalently the least degree of a nonconstant map to \(\mathbf P^1_K\).

The statement asserts existence of at least one curve \(X\) with the specified skeleton, genus, and gonality. It does not claim that every curve having \(\Gamma\) as a skeleton has the same gonality.

## Proof
Choose a divisor \(D\) on \(\Gamma\) of degree \(d\) and rank at least \(1\). Such a divisor exists by the definition of \(d\).

Corollary 5.3 of Mascuch--Teixidor i Bigas states that every positive-rank divisor on a metric graph of pseudocompact type lifts, up to linear equivalence after tropicalization, to a positive-rank divisor on a smooth proper curve having the graph as a skeleton. In the metric-banana-path case, the curve can be chosen genus-preservingly. Hence there exist \(K\), \(X/K\), and a divisor \(B\) on \(X\) such that
\[
\deg(B)=d,\qquad \operatorname{rk}_X(B)\ge1,\qquad g(X)=g(\Gamma),
\]
and the tropicalization of \(B\) is linearly equivalent to \(D\). Therefore
\[
\operatorname{gon}(X)\le d.
\]

For the reverse inequality, let \(A\) be any divisor on \(X\) with \(\operatorname{rk}_X(A)\ge1\). The specialization inequality for divisors on a smooth non-Archimedean curve and its skeleton says that rank cannot decrease under specialization. Passing from the associated metrized-complex rank to the underlying metric-graph rank gives
\[
\operatorname{rk}_{\Gamma}(\operatorname{trop}(A))
\ge
\operatorname{rk}_X(A)
\ge1.
\]
Tropicalization preserves degree, so
\[
\deg(A)=\deg(\operatorname{trop}(A))\ge d
\]
by the minimality defining \(d=\operatorname{gon}(\Gamma)\). Taking \(A\) of minimal positive rank on \(X\) yields
\[
\operatorname{gon}(X)\ge d.
\]
Combining the two inequalities proves
\[
\operatorname{gon}(X)=\operatorname{gon}(\Gamma).
\]

Finally, Theorem 1.1 of Mascuch--Teixidor i Bigas identifies divisorial and geometric gonality on every metric graph of pseudocompact type, so the same number also equals the geometric gonality of \(\Gamma\).

## Verification
The lifting input was checked in the full text of Mascuch--Teixidor i Bigas. Proposition 4.2 gives a genus-preserving algebraic lift for path-induced divisors, Theorem 1.2 shows that every positive-rank divisor on a graph of pseudocompact type is tree-induced, and Corollary 5.3 specializes this to a genus-preserving lift for every positive-rank divisor on a metric banana path.

The lower-bound step was checked against the specialization inequality of Amini--Baker: divisor rank cannot go down under specialization from a smooth proper curve to its associated metrized complex, and the underlying metric-graph rank is at least the metrized-complex rank. The same inequality is explicitly invoked by Mascuch--Teixidor i Bigas in their Proposition 4.4.

The argument is exact and uses no finite experiment. A hypothetical pencil on \(X\) of degree smaller than \(d\) would specialize to a positive-rank divisor on \(\Gamma\) of the same smaller degree, contradicting the definition of \(d\).

## Relationship to prior work
Mascuch--Teixidor i Bigas prove the stronger divisor-level lifting statement needed for the upper bound and prove genus preservation for metric banana paths, but they state Corollary 5.3 only as existence of a positive-rank lifted divisor; they do not state that the resulting algebraic curve has gonality exactly equal to that of the skeleton. The missing reverse inequality comes from the specialization theorem.

Amini--Baker--Brugallé--Rabinoff study gonality lifting in much greater generality. Their general non-augmented lifting result permits increasing vertex genera, while their discussion of augmented tropical curves shows that gonality-preserving algebraic lifting can fail in general. The present conclusion is therefore sharper in a specific natural class: for every metric banana path the lift can retain the graph genus and still have exactly the graph gonality.

As a concrete consequence, the genus-\(2N\) banana paths of prescribed gonality constructed in Proposition 6.5 of Mascuch--Teixidor i Bigas admit smooth proper genus-\(2N\) lifts whose algebraic gonality is exactly the prescribed tropical value.

## Limitations
The theorem is existential and restricted to metric banana paths for the simultaneous genus-preserving conclusion. For general metric graphs of pseudocompact type, the same divisor-lifting argument gives an exact-gonality lift, but the available theorem does not guarantee that the lift has the same genus as the metric graph.

No claim is made about preserving higher-rank gonality sequences, uniqueness of the lift, the residue field, or moduli-theoretic dimensions of the resulting algebraic lifting locus.

## References
B. Mascuch and M. Teixidor i Bigas, “Divisors and harmonic morphisms on metric graphs of pseudocompact type,” arXiv:2609.38821v2, first public 2026-09-30; especially Theorems 1.1 and 1.2, Propositions 4.1 and 4.2, Corollary 5.3, and Proposition 6.5.

O. Amini and M. Baker, “Linear series on metrized complexes of algebraic curves,” Math. Ann. 362 (2015), 55--106, arXiv:1204.3508; especially the specialization inequality and Theorem 5.11.

O. Amini, M. Baker, E. Brugallé, and J. Rabinoff, “Lifting harmonic morphisms II: tropical curves and metrized complexes,” Algebra Number Theory 9 (2015), 267--315, arXiv:1404.3390; especially the discussion of gonality lifting in Section 5.
