# Minimum discriminating codes and exchange components in biplanes of order four

## Finding

**Theorem.** Let \(\mathcal D=(P,\mathcal B)\) be **any** symmetric \(2\text{-}(16,6,2)\) design, with its point--block incidence graph. A *point-side discriminating code* is a set \(C\subseteq P\) such that the sixteen traces \(C\cap B\), for \(B\in\mathcal B\), are all **nonempty and pairwise distinct**. Then its smallest possible size is \(5\), and the complete family of minimum codes is
\[
\mathcal C_{\min}=\{B\setminus\{p\}:B\in\mathcal B,\ p\in B\}.
\]
There are exactly \(96\) different minimum codes. Joining two minimum codes precisely when one point can be replaced by another (that is, their intersection has size \(4\)) gives an exchange graph isomorphic to a disjoint union of \(16\) copies of \(K_6\). In particular it has \(96\) vertices, \(240\) edges, and \(16\) components. These conclusions depend only on the design parameters and hold for every isomorphism type of such a biplane.

## Assumptions and scope

A symmetric \(2\text{-}(v,k,\lambda)\) design has \(v\) points and \(v\) blocks, each of size \(k\), with each point in \(k\) blocks and each pair of distinct points in \(\lambda\) blocks. In a symmetric design any two distinct blocks also have exactly \(\lambda\) common points. Here \((v,k,\lambda)=(16,6,2)\). The code is restricted to the *point* part of the incidence graph and must identify the *block* part by its nonempty incidence traces. This is the standard bipartite *discriminating-code* requirement, not the weaker semi-resolving condition which allows one empty trace. Codes are labelled subsets of a fixed design; no equivalence under automorphisms is imposed. Exchange moves maintain optimum size and the discriminating property.

## Proof

**1. Minimum size.** For \(t\) chosen points there are at most \(2^t-1\) distinct nonempty traces. Distinguishing sixteen blocks therefore requires \(2^t-1\ge16\), so \(t\ge5\).

**2. Classification at size five.** Suppose \(|C|=5\) and all sixteen block traces are nonempty and pairwise distinct. Let \(r_j\) count blocks satisfying \(|C\cap B|=j\), for \(1\le j\le5\). Counting blocks, point--block incidences, and pairs of chosen points with a containing block, respectively, gives
\[
\sum_{j=1}^{5}r_j=16,\quad
\sum_{j=1}^{5}jr_j=30,\quad
\sum_{j=1}^{5}\binom j2 r_j=20.
\]
For distinct traces, each of the five singleton subsets can occur at most once, so \(r_1\le5\). Likewise \(r_5\le1\). Eliminating the first three variables from these equations yields
\[
 r_1=8-r_4-3r_5,\qquad
 r_2=2+3r_4+8r_5,\qquad
 r_3=6-3r_4-6r_5.
\]
If \(r_5=0\), the nonnegativity of \(r_3\) forces \(r_4\le2\), and then \(r_1=8-r_4\ge6\), impossible. Hence \(r_5=1\). Nonnegativity of \(r_3\) now forces \(r_4=r_3=0\), and thus \((r_1,r_2,r_3,r_4,r_5)=(5,10,0,0,1)\). In particular one block \(B\) contains every point of \(C\). Since \(|B|=6\), \(C=B\setminus\{p\}\) for its unique omitted point \(p\).

**3. Sufficiency.** Conversely fix \(B\in\mathcal B\), \(p\in B\), and \(C=B\setminus\{p\}\). The trace of \(B\) itself is \(C\). Every other block \(A\ne B\) intersects \(B\) in precisely two points. Each of the five pairs \(\{p,c\}\), \(c\in C\), occurs in exactly one block other than \(B\), and that block has singleton trace \(\{c\}\). Similarly each of the ten pairs \(\{c,d\}\subseteq C\) occurs in exactly one block other than \(B\), with doubleton trace \(\{c,d\}\). These account for all fifteen other blocks, so the sixteen traces are \(C\), all five singletons, and all ten doubletons: nonempty and distinct.

**4. Counting and reconfiguration.** A five-set cannot lie in two different blocks, since distinct blocks share only two points. Thus the \(16\) choices of \(B\), each with six choices of the omitted \(p\), give exactly \(16\cdot6=96\) distinct codes. Within one fixed block the six punctured blocks pairwise intersect in four points and hence form \(K_6\) in the exchange graph. Codes supported on distinct blocks intersect in at most two points, so there are no edges between different families. The exchange graph is therefore \(16K_6\), with \(16\binom{6}{2}=240\) edges.

## Verification

The proof above is universal and requires no computation or classification of individual biplanes. The accompanying standard-library Python script `verify.py` separately constructs one explicit \(2\text{-}(16,6,2)\) design on the binary four-space: for each vertex \(v\), its block is \(\{v,v\oplus1,v\oplus2,v\oplus4,v\oplus8,v\oplus15\}\). It checks all incidence axioms, all \(\binom{16}{5}=4368\) five-point subsets and their sixteen traces, and the entire exchange graph. Its reproducible results are \(96\) minimum codes, size-profile \((r_1,r_2,r_5)=(5,10,1)\), sixteen six-vertex components, and \(240\) exchange edges. The script illustrates the theorem for one design; it is not being used to extrapolate to all designs.

To replay: run `python3 verify.py` from a directory containing the bundled script (Python 3 standard library only); expect a final line `VERIFY_OK`.

## Relationship to prior work

Discriminating codes of bipartite graphs were studied by Charbit, Charon, Cohen, Hudry, and Lobstein and by subsequent authors; their requirement is exactly separation **plus** nonempty traces. Bailey, *On the metric dimension of imprimitive distance-regular graphs*, Proposition 14 (arXiv:1312.4971, §4.2), already proves that a block with one point deleted is **semi-resolving** for the opposite part of any biplane. Thus the punctured-block *construction itself is not new*. What the present theorem establishes beyond that construction is the **converse under the discriminating/nonempty condition**, the resulting exact \(96\)-code count, and the complete exchange graph, uniformly for every \(2\text{-}(16,6,2)\) biplane. Note that a semi-resolving set is only required to separate block traces, potentially allowing an empty trace; one must not identify all optimal semi-resolving sets with the \(96\) codes here. Work on ordinary metric resolving sets of incidence graphs studies a different, two-sided distance invariant and does not supply this classification in the material inspected.

## Limitations

The theorem is specific to the symmetric \(2\text{-}(16,6,2)\) parameter set, although it covers all its realizations. It is not a classification of arbitrary minimum **semi-resolving** sets, of ordinary metric bases of incidence graphs, of discriminating codes at larger sizes, or of the exchange graphs at higher cardinalities. Unindexed or inaccessible literature may still contain an equivalent statement.

## References

1. E. Charbit, I. Charon, G. Cohen, O. Hudry, “Discriminating codes in bipartite graphs,” *Electronic Notes in Discrete Mathematics* **26** (2006), 29–35, doi:10.1016/j.endm.2006.08.005.
2. I. Charon, G. Cohen, O. Hudry, A. Lobstein, “Discriminating codes in (bipartite) planar graphs,” *European Journal of Combinatorics* **29** (2008), 1353–1364, doi:10.1016/j.ejc.2007.05.006.
3. E. Charbit, I. Charon, G. Cohen, O. Hudry, A. Lobstein, “Discriminating codes in bipartite graphs: bounds, extremal cardinalities, complexity,” *Advances in Mathematics of Communications* **2** (2008), 403–420, doi:10.3934/amc.2008.2.403.
4. R. F. Bailey, “On the metric dimension of imprimitive distance-regular graphs,” arXiv:1312.4971, first submitted 2013-12-17, especially Proposition 14.
5. P. Kaski and P. R. J. Östergård, “There are exactly five biplanes with \(k=11\),” *Journal of Combinatorial Designs* **16** (2008), 117–127, first online 2007-02-22, doi:10.1002/jcd.20145.
6. L. Tang, S. Zhou, J. Chen, Z. Zhang, “Metric dimension and metric independence number of incidence graphs of symmetric designs,” *Discrete Applied Mathematics* (2021), doi:10.1016/j.dam.2020.12.001.
