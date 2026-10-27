# Forcing-set spectrum and two matching orbits of the Tutte–Coxeter graph

## Finding
Let \(T\) be the Tutte–Coxeter graph, realized as the incidence graph between the fifteen duads (two-subsets) of \(\{0,1,2,3,4,5\}\) and the fifteen synthemes (partitions into three disjoint duads). For each perfect matching \(M\) of \(T\), a forcing set is a subset \(A\subseteq M\) contained in no other perfect matching. Define \(f_M(t)=\sum_{A\subseteq M\,:\,A\text{ forcing}}t^{|A|}\). Then the natural \(S_6\)-action on the \(288\) perfect matchings has two orbits of size \(144\), whose forcing-set polynomials are respectively
\[
\begin{aligned}
f_0(t)={}&240t^5+1380t^6+3360t^7+4745t^8+4420t^9\\
&+2887t^{10}+1355t^{11}+455t^{12}+105t^{13}+15t^{14}+t^{15},\\
f_1(t)={}&240t^5+1355t^6+3310t^7+4710t^8+4410t^9\\
&+2886t^{10}+1355t^{11}+455t^{12}+105t^{13}+15t^{14}+t^{15}.
\end{aligned}
\]
In particular, every perfect matching has forcing number exactly \(5\) and exactly \(240\) forcing five-subsets, but the two orbits have differing numbers \(1380\) and \(1355\) of forcing six-subsets. The total forcing-subset polynomial \(\sum_M f_M(t)=144(f_0(t)+f_1(t))\), with coefficients for degrees \(5,\ldots,15\), is
\[
(69120,393840,960480,1361520,1271520,831312,390240,131040,30240,4320,288).
\]

## Assumptions and scope
All graphs and matchings are finite and labelled. A duad \(d\) is incident with a syntheme \(s\) exactly when \(d\in s\). A perfect matching chooses one incident syntheme for every duad, with every syntheme chosen exactly once; its cardinality is \(15\). The natural \(S_6\)-action relabels the six underlying symbols. The polynomial enumerates **all** forcing subsets (not only inclusion-minimal forcing subsets). The ordinary forcing polynomial, which records only the minimum size for each matching, is \(288t^5\).

## Proof
Lexicographically order the fifteen duads and the fifteen synthemes, each syntheme internally sorted lexicographically. For each duad \(d_i\), let \(J_i\) be the three synthemes containing it. Enumerate vectors \(m=(m_0,\ldots,m_{14})\) by the recursion that chooses \(m_i\in J_i\) unused by earlier entries. An accepted full vector is exactly one perfect matching: no partial branch is omitted, and the distinctness condition enforces every syntheme once. The executable recurrence in `verify_forcing.py` enumerates exactly \(288\) vectors.

For every permutation \(p\in S_6\), compute the induced permutations \(p_D\) of the duad indices and \(p_S\) of syntheme indices. It sends \(m\) to \(m'\) with \(m'_{p_D(i)}=p_S(m_i)\). Exhaustive evaluation of the \(720\) permutations partitions all \(288\) vectors into two disjoint orbits of \(144\), represented respectively by the index vectors

`(0,3,7,9,13,12,10,4,11,14,8,2,5,1,6)` and

`(0,3,7,9,14,12,10,4,8,11,13,2,5,1,6)`.

Fix such a representative \(m\). For every matching \(n\), define the \(15\)-bit intersection mask \(I(m,n)=\{i:m_i=n_i\}\). Count the frequencies \(h(U)=\#\{n:I(m,n)=U\}\). For an index subset \(A\), the exact number of perfect matchings containing all its selected edges is
\[
c_m(A)=\sum_{U\supseteq A}h(U).
\]
A subset is forcing precisely when \(c_m(A)=1\). The standard superset-zeta recurrence \(h_{i+1}(A)=h_i(A)+h_i(A\cup\{i\})\) when \(i\notin A\), otherwise \(h_{i+1}(A)=h_i(A)\), computes all \(32768\) values. Counting masks by cardinality with value exactly one gives the two coefficient vectors displayed above. Relabelling preserves containment of matchings and subset size, so these two representative calculations cover **all** perfect matchings. The explicit, terminating enumeration and complete zeta-transform arithmetic are the finite proof; no extrapolation from sampled instances is used.

## Verification
Run `python3 verify_forcing.py` and `python3 verify_independent.py` using Python 3 and no external dependencies. `verify_forcing.py` independently constructs all matchings from duad-side assignments, computes full \(S_6\) orbit coverage and both complete forcing-subset coefficient vectors by superset zeta. `verify_independent.py` builds a 30-vertex incidence graph from six-bit duads, checks its \(45\) edges and girth eight, enumerates perfect matchings by exact cover of **all thirty vertices**, and directly tests every subset of sizes \(4,5,6\) of each orbit representative against all other matchings. Recorded outputs are provided in `verify_forcing.out` and `verify_independent.out`.

## Relationship to prior work
Afshani, Hatami and Mahmoodian develop the forcing-number framework and establish results for path/cycle grids, not the Tutte–Coxeter forcing-subset census. Baez gives the duad–syntheme realization and the \(S_6\) action; these are used as known inputs, not claimed as discoveries. Balasubramanian reports the \(288\) perfect matchings in an ordinary matching-polynomial computation; this does not determine which edge subsets uniquely identify one of those matchings. The new object is the **forcing-subset enumerator refined by matching orbit**, which even distinguishes the two orbits while their minimum forcing numbers coincide. Searches for alternate names (Tutte eight-cage, Cremona–Richmond, defining subsets) located no covering census, but this is not a mathematical proof of publication priority.

## Limitations
This is one exact finite-graph classification, not a statement for all cubic cages or generalized quadrangles. The natural \(S_6\) action is sufficient for the orbit partition; no claim is made that its two classes exhaust any broader classification of matchings under unrelated operations. An ordinary matching polynomial cannot by itself supply the forcing-set data. Unindexed literature, and uninspected full text of the 2025 ordinary-matching paper, leave residual originality uncertainty. Scientific review is not independent certification.

## References
1. P. Afshani, H. Hatami, E. S. Mahmoodian, *On the spectrum of the forced matching number of graphs*, arXiv:0903.2578, first arXiv version March 14, 2009. https://arxiv.org/abs/0903.2578
2. J. Baez, *Tutte–Coxeter Graph*, Visual Insight, August 15, 2015. https://math.ucr.edu/home/baez/visual_insight/20150815%20-%20Tutte-Coxeter%20Graph.html
3. K. Balasubramanian, *Matching Polynomials of Symmetric, Semisymmetric, Double Group Graphs, Polyacenes, Wheels, Fans, and Symmetric Solids in Third and Higher Dimensions*, Symmetry 17 (2025), 133. https://doi.org/10.3390/sym17010133
