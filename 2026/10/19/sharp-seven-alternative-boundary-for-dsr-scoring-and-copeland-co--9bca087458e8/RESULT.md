# Sharp seven-alternative boundary for DSR-scoring and Copeland containment

## Finding
For every tournament on \(2\le n\le6\) alternatives, the winner set \(W_{\mathrm{DSR}}(T)\) of Hou's dominating-set-relaxed scoring rule is contained in the Copeland winner set \(W_{\mathrm{Cop}}(T)\). The first failure occurs at \(n=7\). Exactly \(5040\) of the \(2^{21}=2097152\) labeled seven-alternative tournaments violate containment, comprising **one asymmetric isomorphism class**. In all those tournaments \(W_{\mathrm{DSR}}\cap W_{\mathrm{Cop}}\ne\varnothing\), with one unique Copeland winner and two DSR co-winners. The incidence is \(5040/2^{21}=315/131072\).

## Assumptions and scope
A tournament \(T\) is a complete oriented graph on \(V=\{0,\ldots,n-1\}\), with no ties. Write \(x\to y\) when \(x\) beats \(y\); its Copeland score is \(c(x)=|\{y:x\to y\}|\). For any \(z\), define \(U_z=\{x:x\to z\}\) and \(D_z=\{y:z\to y\}\). For \(D_z\ne\varnothing\), define the eligibility predicate
\[
q_z=\mathbf1\left\{\left[\forall x\in U_z\ \exists y\in D_z:\ x\to y\right]\ \lor\ \left[\exists x\in U_z\ \forall y\in D_z:\ x\to y\right]\right\}.
\]
If \(D_z=\varnothing\), put \(q_z=1\). The score contribution of pivot \(z\) is, for \(D_z\ne\varnothing\),
\[
s_z(x)=q_z\mathbf1_{x\in U_z\cup\{z\}}
\left(\mathbf1_{x\to z}+\sum_{y\in D_z}\mathbf1_{x\to y}\right);
\]
for \(D_z=\varnothing\), put \(s_z(x)=\mathbf1_{x\in U_z}\). The Hou DSR score is \(\psi(x)=\sum_{z\in V}s_z(x)\); its **set-valued** winners are all maximizers, with ties retained. This is precisely the no-tie restriction of Algorithm 2 in Hou (2024): its domination clause implies the first displayed alternative, its \(\gamma\)-clause is the first, and its \(\beta\)-clause is the second. In the \(\gamma\)-clause, \(z\) itself beats every member of \(D_z\). The result concerns this specified rule, not other partition-based tournament solutions.

## Proof
**(1) Exact score reduction.** In a tournament, every comparison \(\mu(x,y)\) in the source's Algorithm 2 is the indicator \(\mathbf1_{x\to y}\). The top/middle block for pivot \(z\) is \(U_z\cup\{z\}\), and its bottom block is \(D_z\). When \(D_z\ne\varnothing\), eligibility is exactly the logical disjunction defining \(q_z\); the redundant case in which every top member beats every bottom member is already included in the \(\gamma\)-condition. The scoring line of Algorithm 2 therefore gives \(s_z(x)\) above, with precisely one chosen specific partition at each pivot. When \(D_z=\varnothing\), its separate fifth line gives exactly \(s_z(x)=\mathbf1_{x\in U_z}\). Thus the verifier uses the original DSR-scoring rule, not an alternative rule.

**(2) A seven-vertex witness.** Order the \(\binom72=21\) pairs \((i,j)\) lexicographically with \(i<j\); bit \(1\) indicates \(i\to j\), bit \(0\) indicates \(j\to i\). The integer mask \(1324\) specifies the complete tournament with out-neighborhoods
\[
\begin{aligned}
D_0&=\{3,4,6\},&D_1&=\{0,4,6\},&D_2&=\{0,1\},\\
D_3&=\{1,2\},&D_4&=\{2,3\},&D_5&=\{0,1,2,3,4\},\\
D_6&=\{2,3,4,5\}.&&
\end{aligned}
\]
For this tournament, the eligible pivots are exactly \(z\in\{2,3,4,5,6\}\). The pivot contributions, in ascending vertex order, are
\[
\begin{array}{c|rrrrrrr}
z&0&1&2&3&4&5&6\\\hline
2&0&0&2&2&1&3&1\\
3&1&0&0&2&2&3&2\\
4&2&1&0&0&2&3&3\\
5&0&0&0&0&0&5&4\\
6&3&2&0&0&0&0&4
\end{array}
\]
so \(c=(3,3,2,2,2,5,4)\) and \(\psi=(6,3,2,4,5,14,14)\). Therefore \(W_{\mathrm{Cop}}=\{5\}\) but \(W_{\mathrm{DSR}}=\{5,6\}\), violating containment.

**(3) Complete finite check and orbit argument.** `verify_dsr.c` is a complete exact-integer enumeration. For each \(n\in\{2,3,4,5,6,7\}\) it visits precisely each integer mask in \([0,2^{n(n-1)/2})\) once, builds the uniquely corresponding tournament, evaluates the pivotal rule derived in (1), and counts (a) any DSR maximizer that fails to maximize Copeland and (b) cases with no common maximizer. Its executable assertions establish the respective noncontainment counts \((0,0,0,0,0,5040)\) and disjointness counts \((0,0,0,0,0,0)\) for \(n=2,\ldots,7\), with \(2^{21}\) examined at \(n=7\). The loops and the finite integer ranges are printed completely in the accompanying self-contained source, making this an auditable exhaustive finite computation rather than partial sampling.

`verify_orbit.py` independently reconstructs the witness using Python Boolean adjacency, recomputes both score vectors, and enumerates all \(7!=5040\) relabelings. It verifies that these relabelings give \(5040\) **distinct** masks, hence that the witness has trivial automorphism group. DSR and Copeland are permutation-equivariant by their definitions, so every relabeling violates containment. Since the exhaustive check found exactly \(5040\) violating labeled tournaments, they are **all** relabelings of the witness. The witness establishes sharpness; the counting comparison proves the uniqueness of the violating isomorphism type and the asserted common-winner property.

## Verification
Use a C99 compiler and the Python 3 standard library; no external data, network, stochastic sampling, or external packages are required:
```
cc -std=c99 -O3 -Wall -Wextra verify_dsr.c -o verify_dsr
./verify_dsr
python3 verify_orbit.py
```
The exact outputs are provided in `VERIFICATION.md`. The C source contains the whole finite state space loop, the scoring clauses, winner tie-handling, and hard assertions on every count. Python independently constructs the relabeling orbit of the witness and rechecks every tournament with at most six vertices using a separately written Boolean score routine. The computation proves a finite theorem only through seven alternatives; it does not address universal properties at larger orders.

## Relationship to prior work
Fujun Hou, *A new social welfare function with a number of desirable properties* (arXiv:2403.16373v1, publicly posted March 25, 2024), defines the DSR-scoring rule in Section 4 and proves containment in Copeland for tournaments of size at most four (Proposition 7), while identifying larger sizes as an open question in Section 7. The precise seven-vertex threshold and unique violating isomorphism class are not given there. Hou's later 2025 journal treatment *A social welfare function based on dominating set relaxations* still states in its accessible abstract the restriction to four alternatives. A different-looking later tournament solution of Hou, *A tournament solution based on dominating-set-relaxed partitions* (first published December 2025), discusses noncoincidence with Copeland at the abstract level. Its full text was unavailable for theorem-level comparison; it is a material residual priority risk, especially for the bare existence of a counterexample. The present claim is about the **specific 2024 DSR-scoring rule** and adds a sharp first-order/exhaustive-classification theorem, not merely noncoincidence of some partition-based solution.

## Limitations
The enumeration makes no assertion for \(n\ge8\). The proof of the small-order boundary and exact frequency depends on an inspectable exhaustive program, not a purely hand-derived structural classification. Exhaustive finite verification is not independent certification. Closely related subsequent papers, particularly the inaccessible 2025/2026 tournament article, may contain unobserved stronger results; novelty is assessed against inspectable material only. No separate independent audit has been performed.

## References
1. F. Hou, *A new social welfare function with a number of desirable properties*, arXiv:2403.16373v1 (March 25, 2024), especially §§3–4, Proposition 7, and §7; https://arxiv.org/abs/2403.16373.
2. F. Hou, *A social welfare function based on dominating set relaxations*, International Journal of General Systems, published online April 21, 2025; https://doi.org/10.1080/03081079.2025.2493189.
3. F. Hou, *A tournament solution based on dominating-set-relaxed partitions*, Expert Systems with Applications 306:130835 (2026 volume; online December 2025); https://doi.org/10.1016/j.eswa.2025.130835.
