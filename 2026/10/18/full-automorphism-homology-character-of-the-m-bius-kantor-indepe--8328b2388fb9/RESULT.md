# Full automorphism homology character of the Möbius–Kantor independence complex

## Finding
Let \(M=\operatorname{GP}(8,3)\) be the Möbius–Kantor graph, \(X=\operatorname{Ind}(M)\), and \(G=\operatorname{Aut}(M)\) (of order \(96\)). Put \(\beta(g)=1\) when \(g\) preserves the two graph bipartition classes and \(\beta(g)=-1\) when it exchanges them. Let \(\epsilon_E(g)\) be the sign of the permutation induced by \(g\) on the \(24\) edges of \(M\). Then the **complete rational equivariant homology classification** is
\[
\boxed{\begin{aligned}
\widetilde H_4(X;\mathbb Q)&\cong \mathbb Q_\beta,\\
\widetilde H_3(X;\mathbb Q)&\cong\mathbb Q_{\beta\epsilon_E}\oplus W_3,
\end{aligned}}
\]
where \(W_3\) is an absolutely irreducible three-dimensional rational representation. There is no other nonzero reduced rational homology. The two one-dimensional characters \(\beta\) and \(\beta\epsilon_E\) are distinct. Neither positive-degree homology group has a nonzero \(G\)-fixed class.

The table gives the *complete character values* for every element of \(G\), grouped by order and character pair. Rows may combine conjugacy classes on which both characters agree; the final column gives the exact number of elements:

| Element order | \(\chi_4\) | \(\chi_3\) | Number of elements |
|---:|---:|---:|---:|
|1|1|4|1|
|2|1|4|1|
|2|-1|0|6|
|2|-1|2|12|
|2|1|-2|12|
|3|1|1|8|
|4|-1|-4|2|
|4|1|0|6|
|6|1|1|8|
|8|-1|0|12|
|8|1|0|12|
|12|-1|-1|16|

In particular, the canonical order-eight rotation fixes a nonzero class in degree three, but **that class is not fixed by the full automorphism group**.

## Assumptions and scope
Use vertices \(u_i,v_i\), indexed by \(i\in\mathbb Z/8\mathbb Z\), and edges \(u_i u_{i+1}\), \(u_i v_i\), \(v_i v_{i+3}\). The independence complex consists of vertex subsets containing none of these edges. Its bipartition classes are
\[
A=\{u_i:i\text{ even}\}\cup\{v_i:i\text{ odd}\},\qquad
B=\{u_i:i\text{ odd}\}\cup\{v_i:i\text{ even}\}.
\]
A graph automorphism either preserves both classes or exchanges them; hence \(\beta\) is a one-dimensional character. The edge-permutation sign \(\epsilon_E\) is likewise a character. Chains use increasing vertex order, reduced chains include degree minus one, and all computations are exact integer or finite-field operations.

## Proof
**Integral homotopy and homology.** A complete face enumeration gives the nonempty face counts \((16,96,272,376,240,72,16,2)\) in dimensions zero through seven. The independently constructed, explicitly specified acyclic matching in `morse_integral.py` pairs \(542\) cover incidences, leaves one critical vertex, four critical three-faces and one critical four-face, and checks acyclicity against all \(4272\) Hasse covers. Integer cancellation of every matched unit boundary coefficient gives the zero Morse boundary \(\mathbb Z\to\mathbb Z^4\) in degrees four to three. With no critical one- or two-cells, the resulting CW complex has three-skeleton \(\bigvee^4 S^3\). Since the attaching map of its only four-cell is classified by its four degree coordinates in \(\pi_3(\bigvee^4 S^3)\cong\mathbb Z^4\), the zero boundary makes it nullhomotopic. Thus
\[
X\simeq \bigvee^4S^3\vee S^4,
\]
with \(H_4(X;\mathbb Z)\cong\mathbb Z\) and \(H_3(X;\mathbb Z)\cong\mathbb Z^4\); no torsion or further reduced homology occurs. This nonequivariant homotopy statement was already established by Bıyıkoğlu and Civan (2015, Example 3.9) and is **not claimed to be new**.

**Action on the rank-one group.** The standard simplicial boundary matrices in degrees four and five have ranks \(181\) and \(58\), respectively, over each of \(\mathbb F_{101}\) and \(\mathbb F_{103}\). Consequently the fourth mod-prime homology is one-dimensional. For each of the \(96\) graph automorphisms, `verify.py` explicitly forms the signed chain-permutation action, reduces it modulo the fifth boundary group, and computes its scalar on that line. At both primes the resulting sign equals \(\beta(g)\), for all \(g\). Since the integral fourth homology is free of rank one, every integral automorphism acts by \(+1\) or \(-1\); reduction at either prime distinguishes these signs. It follows that \(\chi_4=\beta\) over \(\mathbb Q\), not merely modulo a prime.

**Action on degree three.** For an automorphism \(g\), let \(\operatorname{sgn}(g|_S)\) be its orientation sign on an independent vertex subset \(S\) setwise fixed by \(g\). The reduced simplicial Lefschetz number is the finite exact sum
\[
L_{\mathrm{red}}(g)=-1+\sum_{\substack{\varnothing\ne S\in X\\gS=S}}
(-1)^{|S|-1}\operatorname{sgn}(g|_S).
\]
Only degrees three and four carry reduced homology, so \(L_{\mathrm{red}}(g)=\chi_4(g)-\chi_3(g)\). Evaluating this identity on every group element gives the table above and \(\sum_{g\in G}\chi_3(g)=0\), \(\sum_{g\in G}\chi_3(g)^2=192\), and \(\sum_{g\in G}\chi_3(g)\chi_4(g)=0\). The edge sign character \(\epsilon_E\) is computed by the induced permutation of the ordered edge set. Its product with \(\beta\) has inner product one with \(\chi_3\). Subtracting this character leaves a rational degree-three character \(\psi\) with \(\psi(1)=3\) and \(\langle\psi,\psi\rangle_G=1\). Therefore \(\psi\) is absolutely irreducible and defines \(W_3\). Moreover \(\langle\chi_3,\mathbf1\rangle_G=0\) and \(\langle\chi_4,\mathbf1\rangle_G=0\), proving the vanishing of full-group invariants.

## Verification
Run `python morse_integral.py` and `python verify.py` after installing the dependencies in `requirements.txt`. The first uses only the Python standard library and checks the exact acyclic matching and integer attaching degrees. The second uses NumPy and NetworkX; it enumerates the \(96\) automorphisms, verifies face and boundary ranks at both primes, computes signed action on fourth homology, evaluates all Lefschetz traces, obtains all table counts and irreducible character inner products, and checks the previously reported restriction to the canonical rotation subgroup. Both scripts were executed from the final local source content. The finite enumeration covers *all* independent faces and *all* graph automorphisms, not sampled cases.

## Relationship to prior work
Bıyıkoğlu and Civan, *Castelnuovo–Mumford regularity of graphs* (arXiv:1503.06018v1, 2015, Example 3.9), already proved the exact nonequivariant wedge \(\bigvee^4 S^3\vee S^4\). Its homotopy statement cannot specify the action of automorphisms on homology. The published computation *Cyclic symmetry on Möbius–Kantor independence homology* determines the restriction to the single rotation subgroup \(C_8\): its characters are \((4,0,0,0,4,0,0,0)\) and \((1,-1,1,-1,1,-1,1,-1)\). The new full \(96\)-element calculation restricts exactly to those values, but the subgroup calculation neither determines the action of the remaining \(88\) automorphisms nor implies the distinct global one-dimensional constituents, irreducibility of the remaining three-dimensional constituent, or absence of full-group invariants. A separate previously published homotopy computation concerns the same nonequivariant wedge, without the full-group character. The matroid, matching-complex and cut-complex calculations on this graph concern different complexes.

## Limitations
The new contribution is a *finite complete rational representation calculation* for the single canonical graph \(\operatorname{GP}(8,3)\). It does not classify generalized Petersen graphs in general or establish an integral equivariant direct-sum splitting. The argument identifying the fourth-homology sign uses exact modular reductions together with a separately established and independently rechecked free integral homology group; modular experiments alone would not prove a free-integral statement. Unindexed literature may contain related computations; no independent scientific audit is claimed.

## References
1. T. Bıyıkoğlu and Y. Civan, *Castelnuovo–Mumford regularity of graphs*, arXiv:1503.06018v1 (first public 2015-03-20), Example 3.9, https://arxiv.org/html/1503.06018v1.
2. *Cyclic symmetry on Möbius–Kantor independence homology*, public research record `2026/10/11/SCOPE-cyclic-symmetry-on-m-bius-kantor-independence-homology--1c198fd64c4e`, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-cyclic-symmetry-on-m-bius-kantor-independence-homology--1c198fd64c4e.
3. *Integral homotopy type of the Möbius–Kantor independence complex*, public research record `2026/10/11/SCOPE-integral-homotopy-type-of-the-m-bius-kantor-independence-complex--b0d62cfde5f3`, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-integral-homotopy-type-of-the-m-bius-kantor-independence-complex--b0d62cfde5f3.
4. E. W. Weisstein, *Möbius-Kantor Graph*, MathWorld, https://mathworld.wolfram.com/Moebius-KantorGraph.html.
