# Cycle-index homology characters and the five-particle threshold on stars

## Finding
For every integer \(m\ge 3\), every integer \(n\ge 1\), and every permutation \(\sigma\in\mathfrak S_m\) of the arms of the \(m\)-armed star, the rational first-homology character of the unordered collision-free configuration space \(X_{m,n}=\operatorname{UConf}_n(S_m)\) is
\[
\operatorname{tr}\!\left(\sigma\mid H_1(X_{m,n};\mathbb Q)\right)
=1-[t^n]\left(1+(1-c_1(\sigma))t\right)
\prod_{\ell\ge1}(1-t^\ell)^{-c_\ell(\sigma)}.
\]
Here \(c_\ell(\sigma)\) counts arm-permutation cycles of length \(\ell\) and \([t^n]\) extracts a formal power-series coefficient. The product is finite in \(\ell\).

Writing \(p_r(k)\) for the number of partitions of \(k\) into at most \(r\) positive parts, with \(p_r(0)=1\) and \(p_r(k)=0\) for \(k<0\), the multiplicity of the trivial arm-permutation representation is exactly
\[
\dim_{\mathbb Q}H_1(X_{m,n};\mathbb Q)^{\mathfrak S_m}
=1-p_m(n)-p_m(n-1)+\sum_{j=0}^{n-1}p_{m-1}(j).
\]
In particular, **for every \(m\ge3\)** this dimension is zero for \(1\le n\le4\) and is exactly one for \(n=5\). Thus five is the first particle number for which an arm-invariant rational motion class occurs on any star with at least three arms.

## Assumptions and scope
The star \(S_m\) is a finite one-dimensional CW graph with one central vertex of degree \(m\), \(m\) distinct edges (arms), and one leaf on each arm. Each arm is homeomorphic to a closed interval and all arms meet only at the center. The space \(\operatorname{UConf}_n(S_m)\) consists of unordered \(n\)-element subsets of this topological graph with distinct points; no collisions are allowed even at the center. The arm-permutation action fixes the center and carries an arm to another arm by the matching radial coordinate. The theorem is over rational **ordinary** homology in degree one, and includes all \(m\ge3\), \(n\ge1\), and \(\sigma\in\mathfrak S_m\). It does not assert an integral decomposition into \(\mathfrak S_m\)-lattices.

## Proof
**1. First-homology reduction.** A radial tree has exactly one essential vertex. Farley and Sabalka's radial-tree Morse theorem [1, Corollary 4.2] gives a connected one-dimensional CW homotopy model for each nonempty unordered configuration space, and its braid group is free. Therefore \(H_0(X_{m,n};\mathbb Q)=\mathbb Q\) with trivial symmetry action, and \(H_i(X_{m,n};\mathbb Q)=0\) for every \(i\ge2\). From the number of critical one-cells in that corollary, with the usual binomial convention, one obtains
\[
\begin{split}
\operatorname{rank}H_1(X_{m,n};\mathbb Z)
&=\sum_{j=2}^{m-1}\left\{\binom{n+m-2}{m-1}-\binom{n+m-j-1}{n-1}\right\}\\
&=1-\binom{n+m-1}{m-1}+(m-1)\binom{n+m-2}{m-1}.
\end{split}
\]
The second equality follows by telescoping the hockey-stick identity for the sum of the second binomial terms. Hence, including \(n=0\) with \(\chi(\operatorname{UConf}_0(S_m))=1\),
\[
F_r(t):=\sum_{k\ge0}\chi(\operatorname{UConf}_k(S_r))t^k
=\frac{1+(1-r)t}{(1-t)^r}\qquad(r\ge3).
\]
The same identity holds for \(r=0,1,2\): respectively, the graph is a single point or an interval, so configurations are either empty or contractible where nonempty. The equality is checked directly, with \(F_0(t)=1+t\) and \(F_1(t)=F_2(t)=1/(1-t)\).

**2. Fixed unordered configurations.** Fix an arm permutation \(\sigma\), with \(c_\ell\) cycles of length \(\ell\). A configuration is invariant under \(\sigma\) precisely when, on each nontrivial arm cycle \(C\) of length \(\ell\ge2\), it contains \(k_C\ge0\) complete \(\ell\)-point orbits at distinct positive radial coordinates. Its remaining \(q=n-\sum_{|C|\ge2}|C|k_C\) particles lie on the \(c_1\) fixed arms and the center. Thus the fixed space has finitely many disjoint clopen pieces indexed by these integers, and each is homeomorphic to
\[
\operatorname{UConf}_{q}(S_{c_1})\times
\prod_{C:\,|C|\ge2}\operatorname{UConf}_{k_C}((0,1]).
\]
The radial configuration factor \(\operatorname{UConf}_{k}((0,1])\) is contractible for every \(k\ge0\). The pieces are clopen because changing \(k_C\) along an invariant collision-free path would require an orbit of at least two points to coalesce at the central vertex; this is forbidden. Consequently their ordinary Euler characteristics add. Summing their Euler characteristics over \(n\ge0\) gives
\[
\sum_{n\ge0}\chi(X_{m,n}^{\sigma})t^n
=F_{c_1}(t)\prod_{\ell\ge2}(1-t^\ell)^{-c_\ell}
=\left(1+(1-c_1)t\right)
 \prod_{\ell\ge1}(1-t^\ell)^{-c_\ell}.
\]

**3. Finite-order Lefschetz formula.** The configuration space is the complement of the collision diagonals in the compact semialgebraic symmetric power of \(S_m\). A finite-group-invariant triangulation followed by an invariant regular-neighborhood complement gives a finite equivariant CW homotopy model. For a finite-order cellular automorphism on such a model, the alternating trace on homology equals the Euler characteristic of its fixed subcomplex (equivalently, use barycentric subdivision and signed cell orbits). Taking the fixed part of the equivariant homotopy equivalence identifies its Euler characteristic with \(\chi(X_{m,n}^{\sigma})\). The only nonzero homology groups are \(H_0\) and \(H_1\), with trace one in degree zero. Therefore
\[
1-\operatorname{tr}(\sigma\mid H_1(X_{m,n};\mathbb Q))
=\chi(X_{m,n}^{\sigma}).
\]
Taking the coefficient of \(t^n\) in Step 2 proves the stated character for every triple \((m,n,\sigma)\).

**4. Invariants and the first threshold.** Averaging a rational character over the finite group \(\mathfrak S_m\) gives its trivial-representation multiplicity. Standard cycle-index enumeration of permutations yields
\[
\frac1{m!}\sum_{\sigma\in\mathfrak S_m}
\prod_{\ell\ge1}(1-t^\ell)^{-c_\ell(\sigma)}
=\prod_{i=1}^{m}(1-t^i)^{-1}=\sum_{k\ge0}p_m(k)t^k.
\]
Marking one fixed arm, then averaging the remaining \(m-1\) arms, gives
\[
\frac1{m!}\sum_{\sigma\in\mathfrak S_m}c_1(\sigma)
\prod_{\ell\ge1}(1-t^\ell)^{-c_\ell(\sigma)}
=\frac1{1-t}\prod_{i=1}^{m-1}(1-t^i)^{-1}.
\]
Combining these two identities with the character formula gives the exact partition expression in the Finding. Evaluating the ordinary partition recurrences \(p_r(k)=p_{r-1}(k)+p_r(k-r)\) for \(1\le k\le5\), separating \(m=3\), \(m=4\), and \(m\ge5\), yields the multiplicity vector \((0,0,0,0,1)\). This proves the sharp five-particle threshold.

## Verification
The included `verify_star_characters.py` independently builds the Abrams cubical model with each arm subdivided into \(n\) edges. Cells are subsets of \(n\) vertices or open edges whose closures are pairwise disjoint. For every arm permutation in the cases \((m,n)=(3,3),(3,4),(4,3),(4,4),(3,5)\), it computes the signed fixed-cell alternating sum, including the sign induced by permuting edge orientations. This agrees with the formula for each of the 66 tested permutations; the respective numbers of cells are 566, 5551, 1518, 21927 and 55785. Independent partition-recursion evaluations also verify the threshold for \(3\le m\le8\). Run `python3 verify_star_characters.py`; the recorded stdout appears in `verification_output.txt` and ends in `VERIFY_OK`. These finite computations independently corroborate but do not prove the all-parameter character; the proof is Steps 1–4 above.

## Relationship to prior work
Farley and Sabalka [1] establish the one-dimensional radial-tree model and nonequivariant ranks, not this arm-permutation character. Lütgehetmann [2] studies qualitative representation stability for ordered graph configurations. An and Maciążek [3] provide geometric star-braid presentations and relations. Wawrykow [4] studies ordered configurations on stars. Ramos and Yun [5, Section 3.1, Theorem 3.3] compute the arm-permutation representation for **two** unordered particles and give related representation-stability methods. Their two-particle result, together with earlier three-particle calculations, is compatible with the corresponding low-degree specializations of the formula but does not state the uniform all-particle cycle-index formula or its five-particle invariant threshold. The new content is the uniform \((m,n)\) character and its sharp symmetry-invariant onset; ordinary ranks and low-particle specializations are not asserted to be new. Generic cycle-index and finite-order Lefschetz tools are classical inputs rather than claimed innovations.

## Limitations
The theorem concerns one central branching vertex and unordered particles, not arbitrary trees, ordered configuration spaces, higher homology, or integral equivariant module splittings. It assumes collision-free configurations throughout. Originality has been compared against accessible full texts and indexed mathematical findings; an unindexed equivalent theorem remains possible. The included program verifies finite cases only.

## References
1. D. Farley and L. Sabalka, *Discrete Morse theory and graph braid groups*, arXiv:math/0410539, first publicly submitted 2004-10-25; *Algebraic & Geometric Topology* 5 (2005), 1075–1109, Corollary 4.2. https://arxiv.org/abs/math/0410539
2. D. Lütgehetmann, *Representation Stability for Configuration Spaces of Graphs*, arXiv:1701.03490 (2017). https://arxiv.org/abs/1701.03490
3. B. H. An and T. Maciążek, *Geometric Presentations of Braid Groups for Particles on a Graph*, arXiv:2006.15256 (2020), Sections 3–4. https://arxiv.org/abs/2006.15256
4. N. Wawrykow, *Homology Generators and Relations for the Ordered Configuration Space of a Star Graph*, arXiv:2401.13821 (2024). https://arxiv.org/abs/2401.13821
5. E. Ramos and C. H. Yun, *Computing stable homology representations of graph configuration spaces*, arXiv:2606.13813, first submitted 2026-06-11; Section 3.1. https://arxiv.org/abs/2606.13813
