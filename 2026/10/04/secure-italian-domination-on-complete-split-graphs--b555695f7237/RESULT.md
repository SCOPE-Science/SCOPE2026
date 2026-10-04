# Secure Italian domination on complete split graphs
## Finding
Let \(S_{m,n}=K_m\vee\overline{K_n}\) be the complete split graph with clique \(C\) of size \(m\ge1\) and independent set \(I\) of size \(n\ge2\). For a labeling \(f:V(S_{m,n})\to\{0,1,2\}\), put \(q=|\{v\in I:f(v)=0\}|\) and \(c=\sum_{v\in C}f(v)\). Then \(f\) is a secure Italian dominating function if and only if exactly one of the following holds: (i) \(q=0\) and either \(c>0\) or some vertex of \(I\) has label \(2\); (ii) \(q=1\) and \(c\ge2\); (iii) \(q\ge2\) and \(c\ge3\). Consequently, defining \(C_k(z)=(1+z+z^2)^k\), \(P_k(z)=z^k(1+z)^k\), and \(E_n(z)=n z^{n-1}(1+z)^{n-1}\), the weight enumerator of all secure Italian dominating functions is \[\mathcal S_{m,n}(z)=P_n(z)C_m(z)-z^n+E_n(z)\big(C_m(z)-1-mz\big)+\big(C_n(z)-P_n(z)-E_n(z)\big)\big(C_m(z)-1-mz-\binom{m+1}{2}z^2\big).\] The minimum-weight corollary is \(\gamma_I^s(S_{1,n})=n+1\) and \(\gamma_I^s(S_{m,n})=3\) for \(m\ge2\); these minimum values are already implied by the published extremal and join theorems, while the all-function criterion and weight enumerator are the new content.

## Assumptions and scope
All graphs are finite and simple. The complete split graph \(S_{m,n}\) is the join \(K_m\vee\overline{K_n}\), where \(m\ge1\) and \(n\ge2\). Its vertex set is partitioned into a clique \(C\) of size \(m\) and an independent set \(I\) of size \(n\). A labeling \(f:V(S_{m,n})\to\{0,1,2\}\) is Italian dominating when every zero-labeled vertex has neighbor-label sum at least \(2\). It is secure Italian dominating when every zero-labeled vertex \(v\) has an adjacent positive-labeled vertex \(u\) such that transferring one unit from \(u\) to \(v\) leaves an Italian dominating function. The weight enumerator is \(\mathcal S_{m,n}(z)=\sum_f z^{\omega(f)}\), summed over all secure Italian dominating functions.

## Proof
Let \(q=|\{v\in I:f(v)=0\}|\) and \(c=\sum_{v\in C}f(v)\).

First suppose \(q>0\). Every zero in \(I\) is adjacent exactly to the clique, so Italian domination forces \(c\ge2\). To defend a zero \(v\in I\), its moving neighbor must lie in \(C\). After transferring one unit to \(v\), the clique weight becomes \(c-1\) and the number of zero vertices in \(I\) becomes \(q-1\). If \(q=1\), no zero remains in \(I\), so \(c\ge2\) is sufficient. If \(q\ge2\), at least one zero remains in \(I\), and the transferred labeling is Italian dominating exactly when \(c-1\ge2\), or \(c\ge3\). Clique zeros cause no extra obstruction: because \(c\ge2\), one can move a unit between clique vertices, which preserves the total clique weight seen by every zero in \(I\).

Now suppose \(q=0\). Every vertex of \(I\) is positive. If \(c>0\), then every zero in \(C\) can be defended by a positive clique vertex; a transfer inside \(C\) does not create a zero in \(I\), and all clique zeros continue to see total weight at least \(n\ge2\). If \(c=0\), then every clique vertex is zero. A moving neighbor must lie in \(I\). Moving from a vertex labeled \(2\) is valid because it remains positive, whereas moving from a vertex labeled \(1\) creates a zero in \(I\) that sees clique weight only \(1\). Thus the all-zero clique is secure exactly when at least one independent vertex has label \(2\). This proves the structural criterion.

For the enumerator, write \(C_k(z)=(1+z+z^2)^k\), \(P_k(z)=z^k(1+z)^k\), and \(E_n(z)=n z^{n-1}(1+z)^{n-1}\).

When \(q=0\), all independent vertices are labeled \(1\) or \(2\), contributing \(P_n(z)C_m(z)\), except for the unique invalid labeling in which every clique vertex is \(0\) and every independent vertex is \(1\). Hence this case contributes \(P_n(z)C_m(z)-z^n\).

When \(q=1\), the independent side contributes \(E_n(z)\), while the clique must have weight at least \(2\). The weight-zero and weight-one clique labelings contribute \(1\) and \(mz\), so this case contributes
\[
E_n(z)\big(C_m(z)-1-mz\big).
\]

When \(q\ge2\), the independent-side polynomial is \(C_n(z)-P_n(z)-E_n(z)\), while the clique must have weight at least \(3\). The number of clique labelings of weight \(2\) is \(m+\binom m2=\binom{m+1}{2}\). Thus this case contributes
\[
\big(C_n(z)-P_n(z)-E_n(z)\big)\big(C_m(z)-1-mz-\binom{m+1}{2}z^2\big).
\]
Adding the three disjoint cases proves the formula.

The minimum-weight formula is an immediate coefficient consequence. For \(m=1\), the third case is impossible and each of the first two cases has minimum weight \(n+1\). For \(m\ge2\), choose all independent vertices as \(0\) and give clique weight \(3\), so the minimum is at most \(3\); the published general lower bound for non-complete graphs gives equality.

## Verification
The included checker constructs \(S_{m,n}\) directly, examines every labeling into \(\{0,1,2\}\), tests Italian domination from neighbor sums, and for every zero vertex searches every adjacent positive vertex for a valid one-unit transfer. It does not use the structural criterion to decide validity. It then compares the accepted functions with the criterion, every weight-enumerator coefficient, and the minimum-weight corollary.

## Relationship to prior work
Dettlaff, Lemańska, and Rodríguez-Velázquez introduced secure Italian domination and proved general bounds, tree results, and join-graph results. Their Theorem 5 gives the star extremal value, and Theorem 19 gives \(\gamma_I^s(K_m+G)=3\) for \(m\ge2\) when \(G\) is non-complete. Therefore the minimum values for complete split graphs are prior coverage and are not claimed as new.

The same full article contains no occurrence of “polynomial,” “split,” or “enumerat” in the retrieved text, and its join section concerns minimum weight rather than all secure Italian functions. A 2024 survey uses the equivalent name secure Roman \(\{2\}\)-domination and summarizes the primary study and the secure \(w\)-domination generalization; its secure Roman \(\{2\}\) section likewise reports complexity, bounds, and particular graph classes rather than a complete-split weight census. Targeted literature and semantic-database searches under both names did not locate the criterion or the displayed enumerator.

## Limitations
The theorem is restricted to complete split graphs with \(n\ge2\); the case \(n=1\) is a complete graph and is not part of the stated family. The minimum-weight values are prior results in this specialization; the claimed contribution is the exact all-function classification and weight distribution. Exhaustive verification through order nine is corroborative only. A differently phrased or non-indexed enumeration may exist despite the searches recorded in the audit.

## References
1. M. Dettlaff, M. Lemańska, J. A. Rodríguez-Velázquez, “Secure Italian domination in graphs,” Journal of Combinatorial Optimization 41 (2021), 56–72, DOI 10.1007/s10878-020-00658-1; published online 28 October 2020.
2. A. Cabrera Martínez, A. Estrada-Moreno, J. A. Rodríguez-Velázquez, “Secure w-Domination in Graphs,” Symmetry 12 (2020), 1948, DOI 10.3390/sym12121948.
3. A. Almulhim, B. Al Subaiei, “Survey on Roman {2}-Domination,” Mathematics 12 (2024), 2771, DOI 10.3390/math12172771.
