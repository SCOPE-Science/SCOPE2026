# A matching-polynomial identity for singleton two-rainbow domination on cycles

## Finding

For every integer \(n\geq3\), let \(C_n\) be the simple cycle on the *labelled* vertices \(0,1,\ldots,n-1\), with indices modulo \(n\). A **singleton two-rainbow dominating function** is a labeling \(f:V(C_n)\to\{0,1,2\}\) such that every vertex labeled \(0\) has neighbors labeled \(1\) and \(2\), one of each. Write \(w(f)=|\{v:f(v)\ne0\}|\), and define the all-weight enumerator
\[
R_n(t)=\sum_{f\text{ admissible}}t^{w(f)}.
\]
The colors \(1\) and \(2\) are distinguishable; color exchange and graph symmetries are **not** quotiented out.

**Theorem (complete cycle enumerator).** For every \(n\geq3\),
\[
\boxed{R_n(t)=\sum_{k=0}^{\lfloor(n-1)/2\rfloor}
 \frac{n}{n-k}\binom{n-k}{k}\,2^{n-2k}t^{n-k}
 +4\,\mathbf1_{4\mid n}\,t^{n/2}.}
\]
The apparent rational binomial factors are integers. Equivalently, if \(\alpha_\pm=t\pm\sqrt{t^2+t}\) are formal algebraic expressions, then
\[
\boxed{R_n(t)=\alpha_+^n+\alpha_-^n+
 2\,\mathbf1_{2\mid n}\,(-1)^{n/2}t^{n/2}.}
\]
The two conjugate powers sum to a polynomial in \(\mathbb Z[t]\). The second presentation identifies a *single parity correction* to the ordinary cycle matching polynomial.

As a direct consequence, the number \(N_n\) of minimum-weight singleton two-rainbow dominating functions, with labeled vertices and distinguished colors, is
\[
\boxed{N_n=\begin{cases}
4,&n\equiv0\pmod4,\\
2n,&n\equiv1,3\pmod4,\\
n^2,&n\equiv2\pmod4.
\end{cases}}
\]
Their minimum weight is \(n/2\) for \(n\equiv0\pmod4\), \((n+1)/2\) for odd \(n\), and \(n/2+1\) for \(n\equiv2\pmod4\).

For example,
\[
\begin{aligned}
R_3(t)&=8t^3+6t^2,\\
R_4(t)&=16t^4+16t^3+4t^2,\\
R_5(t)&=32t^5+40t^4+10t^3,\\
R_6(t)&=64t^6+96t^5+36t^4.
\end{aligned}
\]

## Assumptions and scope

The graph is an ordinary simple cycle with \(n\ge3\). Each vertex is either uncolored or receives **exactly one** of two colors; it may not receive both. The sole constraint is imposed on uncolored vertices. In particular, adjacent colored vertices may receive equal colors. Every vertex position and both color names are distinguishable, so the enumerator counts individual functions, not color-swap or dihedral equivalence classes. The variable \(t\) records the number of nonzero labels, not the number of empty vertices.

This is the singleton/dual-server model, not the classical set-valued two-rainbow domination model allowing the label \(\{1,2\}\) at a single vertex, nor the more restrictive two-rainbow *independent* domination model.

## Proof

**Step 1: Zero placements.** For an admissible labeling, every zero must have two nonzero neighbors with opposite colors. In particular, the zero set \(Z=f^{-1}(0)\) is an independent subset of the cycle. Suppose \(|Z|=k\). There are \(m=n-k\) colored vertices, and \(k\le\lfloor n/2\rfloor\).

For \(0\le k<n/2\), the number of independent \(k\)-subsets of the cycle is
\[
c_{n,k}=\frac{n}{n-k}\binom{n-k}{k}.
\]
For \(k=0\), this equals one. For \(k\ge1\), choose one of the \(k\) zeros as distinguished, then record the \(k\) positive numbers of colored vertices following successive zeros. These sum to \(n-k\), giving \(\binom{n-k-1}{k-1}\) compositions. There are \(n\) choices of the distinguished zero's absolute vertex position, and each unmarked zero set is counted \(k\) times. Hence the count is \(\tfrac nk\binom{n-k-1}{k-1}=c_{n,k}\).

**Step 2: Colorings for nonalternating zero sets.** Fix \(Z\) with \(k<n/2\), and cyclically order the \(m=n-k\) colored vertices. Every zero separates two *successive* colored vertices and demands that their colors differ. Thus the \(k\) zeros select \(k\) edges of the cyclic succession graph on those \(m\) vertices. Because \(k<m\), at least one succession edge remains unrestricted: the edges requiring a color flip form a disjoint union of paths, with \(m\) vertices and \(k\) edges (also valid when \(m=2\), treating the two cyclic succession edges distinctly). Every path component can choose its initial color freely; the remaining colors along the path then alternate. Therefore the exact number of consistent assignments to the colored vertices is
\[
2^{m-k}=2^{n-2k}.
\]
This count depends only on \(n\) and \(k\), not on the location of the independent zero set. Summing proves the stated nonalternating terms.

**Step 3: Alternating zero sets.** The remaining case \(k=n/2\) requires even \(n\) and means that colored and zero vertices alternate. There are exactly two choices of \(Z\), the two bipartition classes of the cycle. The \(m=n/2\) colored vertices must alternate colors around a *closed* cyclic succession, which is possible exactly when \(m\) is even. Then there are two color assignments for each of the two zero patterns, yielding four functions. If \(m\) is odd, there is no consistent coloring. Thus the endpoint coefficient is four for \(4\mid n\) and zero otherwise. This completes the all-weight formula.

**Step 4: Matching-polynomial form.** For \(0\le k<n/2\), the number \(c_{n,k}\) also equals the number of \(k\)-edge matchings in \(C_n\) (its line graph is again a cycle). For even \(n\), the number of perfect matchings is two. The weighted cyclic monomer-dimer enumerator
\[
M_n(a,b)=\sum_{\text{matchings }Q\subseteq E(C_n)}a^{n-2|Q|}b^{|Q|}
\]
equals \(\operatorname{tr}(T(a,b)^n)\) for
\[
T(a,b)=\begin{pmatrix}a&b\\1&0\end{pmatrix}.
\]
To verify this identity directly, expand the trace as closed length-\(n\) walks on the two transfer states: each transition staying in the first state is a monomer of weight \(a\), while a consecutive pair of transitions through the second state is a dimer of weight \(b\); each cyclic tiling occurs exactly once as a state sequence indexed by the cycle vertices. The eigenvalues of \(T(a,b)\) are \(\tfrac12(a\pm\sqrt{a^2+4b})\).

Specialize \(a=2t\), \(b=t\). For a nonperfect matching of size \(k\), its monomer-dimer weight is \(2^{n-2k}t^{n-k}\), exactly the previously derived coefficient. For even \(n\), this monomer-dimer enumerator counts the two perfect matchings with total weight \(2t^{n/2}\), whereas Step 3 showed that the admissible labeling count is four if \(n/2\) is even, and zero if \(n/2\) is odd. The difference is therefore \(2(-1)^{n/2}t^{n/2}\). The displayed algebraic form follows from the two eigenvalues \(t\pm\sqrt{t^2+t}\).

**Step 5: Minimum layer.** If \(n\) is a multiple of four, the alternating functions exist and are the four minimum-weight configurations. For odd \(n\), the largest admissible zero count is \(k=(n-1)/2\); then \(c_{n,k}=n\) and there are two color choices, giving \(N_n=2n\). For \(n\equiv2\pmod4\), the alternating zero set has an odd flip cycle and is impossible. The largest feasible zero count is \(k=n/2-1\), for which \(c_{n,k}=n^2/4\) and there are four color choices, giving \(N_n=n^2\). These constructions all exist by Steps 2 and 3, so the resulting weights really are minimum.

## Verification

The standalone Python 3 checker at `artifacts/verify.py` reconstructs the domain predicate on every one of the \(3^n\) vertex labelings for \(3\le n\le12\), independently computes the same all-weight polynomials using a nine-state closed-walk transfer matrix through \(n=60\), and compares the Lucas recurrence and minimum-count formulas through \(n=150\). Its output terminates in `VERIFY_OK` when every assertion succeeds. These are finite consistency tests; Steps 1–5 are the proof for all \(n\ge3\).

## Relationship to prior work

Lange, *Complexity, Bounds, and Exact Algorithms for Rainbow \(k\)-Domination in Regular Graphs*, arXiv:2610.06906v1 (first posted 2026-10-01), distinguishes singleton from set-valued rainbow domination and, in Proposition 12 and its cycle proof, gives the numerical minimum singleton two-rainbow domination weight of \(C_n\). The present theorem refines that numerical result to the complete weight enumerator, the exact number of minimum labelings and a matching-polynomial interpretation; these are not consequences of the numerical weight formula alone.

Rao, Udupa and Prathviraj, *The Dual-Server Domination Number of Some Graph Operations*, arXiv:2608.14690v1 (2026-08-07), studies dual-server domination under graph operations, including splitting graphs of cycles; its cycle discussion concerns splitting graphs and minimum sizes, not the all-weight enumeration of the base cycles here. Bonomo, Brešar, Grippo, Milanič and Safe, *Domination parameters involving the number 2: interrelations and algorithmic consequences*, Discrete Applied Mathematics 235 (2018), defines and relates the singleton two-rainbow parameter to other domination notions. General finite-state counting on bounded-width graphs can compute the coefficients algorithmically, but does not by itself state the closed binomial count or identify the alternating-cycle obstruction.

Chellali, Haynes and Hedetniemi, *Dual-server domination in graphs*, Discrete Applied Mathematics 387 (2026), is an important prior source for the underlying dual-server parameter. Only its accessible bibliographic description and summaries, not the entire paper, were available in the present comparison; this leaves a historical-priority risk. Claims of unconditional first discovery are **not** made.

## Limitations

The theorem applies to ordinary labelled cycles and the singleton two-color model. It is not a formula for classical set-valued two-rainbow domination or rainbow independent domination. The count keeps vertex labels and color names fixed; it does not quotient by cycle automorphisms or color swapping. The matching polynomial link concerns this particular specialization and parity correction, not a general equivalence of domination and matching polynomials on arbitrary graphs. Publication priority remains provisional, especially because the complete 2026 foundational dual-server paper was not accessible; independent mathematical validation has not been performed.

## References

1. P. Lange, *Complexity, Bounds, and Exact Algorithms for Rainbow \(k\)-Domination in Regular Graphs*, arXiv:2610.06906v1, posted 2026-10-01. https://arxiv.org/abs/2610.06906 ; full HTML https://arxiv.org/html/2610.06906 .
2. S. L. Rao, S. Udupa N. V., and Prathviraj N, *The Dual-Server Domination Number of Some Graph Operations*, arXiv:2608.14690v1, posted 2026-08-07. https://arxiv.org/abs/2608.14690 .
3. M. Chellali, T. W. Haynes, and S. T. Hedetniemi, *Dual-server domination in graphs*, Discrete Applied Mathematics 387 (2026), 251–259. DOI: 10.1016/j.dam.2026.03.017.
4. F. Bonomo, B. Brešar, L. N. Grippo, M. Milanič, and M. D. Safe, *Domination parameters involving the number 2: interrelations and algorithmic consequences*, Discrete Applied Mathematics 235 (2018), 23–50. DOI: 10.1016/j.dam.2017.08.017.
