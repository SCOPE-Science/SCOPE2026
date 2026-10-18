# The full \(2^4\!:\!S_5\) homology character of the folded-five-cube independence complex

## Finding
Let \(F\) be the degree-five folded five-cube (also known as the degree-five Clebsch or Greenwood–Gleason graph) and let \(K=\operatorname{Ind}(F)\). Its automorphism group is \(G=T\rtimes S_5\), where \(T\cong(\mathbb Z/2)^4\) is the vertex-translation group and \(S_5\) permutes the five edge directions.

The only nonzero reduced rational homology is \(\widetilde H_3(K;\mathbb Q)\), of dimension nine. As a \(\mathbb Q[G]\)-module, it has the **complete** decomposition
\[
\widetilde H_3(K;\mathbb Q)\cong
\operatorname{sgn}_{S_5}\otimes
\bigl(\operatorname{Std}_{S_5}\oplus W\bigr),
\]
where the four-dimensional standard representation \(\operatorname{Std}_{S_5}\) is inflated from \(S_5\), and \(W\) is a five-dimensional monomial representation explicitly defined below. Both summands are absolutely irreducible, nonisomorphic, and occur with multiplicity one.

Write \(s_0,s_1,s_2,s_3\) for the standard basis of \(T=\mathbb F_2^4\), and \(s_4=s_0+s_1+s_2+s_3\). For each \(i\in\{0,1,2,3,4\}\), there is a unique linear form \(\alpha_i:T\to\mathbb F_2\) such that \(\alpha_i(s_i)=0\) and \(\alpha_i(s_j)=1\) for \(j\ne i\). Define \(W\) on basis \(e_0,\ldots,e_4\) by
\[
\rho_W(t)e_i=(-1)^{\alpha_i(t)}e_i,\qquad
\rho_W(p)e_i=e_{p(i)}
\quad(t\in T,\ p\in S_5).
\]
Here the outside tensor factor \(\operatorname{sgn}_{S_5}\) is trivial on \(T\).

Equivalently, for every automorphism \(g=(t,p)\), where \(x\mapsto t+p(x)\) on the vertex set,
\[
\boxed{\operatorname{tr}\bigl(g\mid\widetilde H_3(K;\mathbb Q)\bigr)
=\operatorname{sgn}(p)\left(
\#\operatorname{Fix}(p)-1
+\sum_{i:p(i)=i}(-1)^{\alpha_i(t)}
\right).}
\]
In particular,
\[
\dim\widetilde H_3(K;\mathbb Q)^T=4,\qquad
\dim\widetilde H_3(K;\mathbb Q)^G=0.
\]
The nonidentity translations have character value one or five: exactly five have value one and ten have value five. Thus the nine-dimensional module is not simply a sum of copies of a trivial translation module.

## Assumptions and scope
The graph is the finite simple Cayley graph on \(T=\mathbb F_2^4\) with symmetric connection set \(\{s_0,s_1,s_2,s_3,s_4\}\). It has sixteen vertices and forty edges. A face of \(K\) is a vertex subset containing no adjacent pair. The similarly named degree-ten graph is the complement of \(F\); its *clique* complex equals \(K\), but its independence complex is different. All representation statements use rational coefficients, not an integral \(\mathbb Z[G]\)-module classification.

Every permutation of the five connection vectors induces an invertible linear map on \(T\): the sole linear relation among them is \(s_0+\cdots+s_4=0\). Together with translations these give 1,920 distinct graph automorphisms. Conversely, an automorphism fixing zero permutes its five neighbors. Each of the ten other vertices has the unique form \(s_i+s_j\) with \(i<j\); it is the common neighbor, other than zero, of \(s_i\) and \(s_j\). This forces any automorphism fixing zero and all five neighbors to fix every vertex. Thus the point stabilizer injects into \(S_5\), so these 1,920 automorphisms form the full group.

## Proof
**1. Exact rational homology.** Enumerating all 65,536 vertex subsets and testing adjacency gives exactly 393 independent sets, including the empty set. The simplex numbers by face cardinality zero through five are
\[
(1,16,80,160,120,16).
\]
Form each oriented simplicial boundary matrix. Exact binary Gaussian elimination gives positive-degree boundary ranks
\[
\bigl(\operatorname{rank}_{\mathbb F_2}\partial_1,
\operatorname{rank}_{\mathbb F_2}\partial_2,
\operatorname{rank}_{\mathbb F_2}\partial_3,
\operatorname{rank}_{\mathbb F_2}\partial_4\bigr)
=(15,65,95,16).
\]
A nonzero minor modulo two is nonzero as an integer and hence over \(\mathbb Q\), so these are lower bounds on the rational ranks. The rational rank of \(\partial_1\) is at most fifteen because the 1-skeleton is connected, the rank of \(\partial_2\) is at most \(80-15=65\) because \(\partial_1\partial_2=0\), that of \(\partial_3\) is at most \(160-65=95\), and that of \(\partial_4\) is at most sixteen, the number of its columns. Therefore the four rational ranks are **exactly** the four displayed binary ranks. The resulting reduced rational Betti vector is zero except in degree three, with rank \(120-95-16=9\). This uses only exact finite boundary matrices and the chain-complex identity, not a finite sampling argument or an assumption about integral torsion.

**2. Signed Lefschetz character.** For any graph automorphism \(g\), its trace on the alternating augmented simplicial chain complex equals its trace on reduced homology. On a simplex fixed setwise by \(g\), the oriented-chain trace is the sign of the induced vertex permutation; on every other simplex it is zero. As rational reduced homology is supported in degree three, the sign of that homological trace is negative. Consequently,
\[
\operatorname{tr}(g\mid\widetilde H_3)
=\sum_{\substack{\sigma\subseteq T\\\sigma\text{ independent},\ g\sigma=\sigma}}
(-1)^{|\sigma|}\operatorname{sgn}(g\mid\sigma).
\]
This sum includes the empty set with value one. Alternatively, every invariant independent set is a union of vertex cycles of \(g\), and a selected cycle contributes a factor of negative one: \((-1)^{\text{cycle length}}\) from the alternating sum times \((-1)^{\text{cycle length}-1}\) from orientation. The character is therefore the independence polynomial of the compatible-orbit graph evaluated at negative one.

**3. All group elements, without character interpolation.** The accompanying verifier independently evaluates the displayed signed-fixed-simplex formula **and** the orbit-quotient independence recurrence for every one of the 1,920 transformations \((t,p)\). In each case it checks equality with
\[
\epsilon(p)\bigl(f(p)-1+\sum_{p(i)=i}(-1)^{\alpha_i(t)}\bigr),
\quad\epsilon(p)=\operatorname{sgn}(p),\quad f(p)=\#\{i:p(i)=i\}.
\]
This is an exhaustive finite proof of the formula: all five-letter permutations and all sixteen translations are visited, all fixed simplices come from the complete enumerated complex, and the recurrence enumerates all compatible vertex-cycle selections. The resulting complete character histogram is
\[
\begin{array}{c|rrrrrrr}
\text{trace}&-5&-3&-1&1&3&5&9\\\hline
\text{group elements}&20&60&884&865&80&10&1.
\end{array}
\]
The sum of the traces is zero; the sum of squared traces is 3,840, twice the group order.

**4. Representation identification.** The rational representation \(\operatorname{sgn}_{S_5}\otimes\operatorname{Std}_{S_5}\) has character \(\epsilon(p)(f(p)-1)\) and trivial translation action. On the five-dimensional module \(W\), the five forms \(\alpha_i\) are distinct; \(S_5\) permutes them transitively, and \(\operatorname{sgn}_{S_5}\otimes W\) has character \(\epsilon(p)\sum_{p(i)=i}(-1)^{\alpha_i(t)}\). Thus the direct sum has exactly the computed character. Character equality determines a rational representation of a finite group up to isomorphism because characteristic zero representations are semisimple and the two displayed rational representations realize those characters.

The standard \(S_5\)-representation is absolutely irreducible. The five basis lines of \(W\) are the **distinct** \(T\)-character spaces, so every \(T\)-invariant subspace over \(\mathbb C\) is a sum of some of these lines. Since \(S_5\) acts transitively on them, a nonzero \(G\)-invariant subspace must contain all five. Hence \(W\), and its sign twist, are absolutely irreducible. They are nonisomorphic to the four-dimensional inflated constituent because the latter is \(T\)-trivial whereas the former has no \(T\)-invariants. The latter's \(T\)-fixed space has dimension four and the whole \(G\)-fixed space is zero. This completes the proof.

## Verification
Run `python3 verify_clebsch_character.py` with standard Python 3; no external libraries, network, random inputs or historical artifacts are required. The script reconstructs the graph and all simplices, calculates every exact mod-two boundary rank by integer bit elimination, constructs 1,920 distinct graph automorphisms and verifies graph-edge preservation, computes both signed fixed-simplex and compatible-orbit traces, checks the closed character formula element by element, and verifies trace histograms, character inner products and fixed-space dimensions. The exact output and assertions are described in `VERIFICATION.md`. The source script is part of this self-contained package.

## Relationship to prior work
The known independent-set table for the five-folded cube already fixes the face vector and independence polynomial; neither contains an automorphism character. Barmak's 2010 triangle-free independence-complex suspension theorem applies to this graph, but does not determine the rank-nine homology representation. Exact public discrete-Morse computations also establish \(\operatorname{Ind}(F)\simeq\bigvee^9 S^3\); an unmarked homotopy equivalence does not determine the induced \(G\)-module. The present claim neither re-derives that homotopy classification as its novelty nor claims the independent-set counts.

A published translation-module theorem for the **open-neighborhood complex** of odd folded cubes gives rank thirty-one in degree two for this graph, and is about a different complex. The rank-nine degree-three independence complex cannot be its special case. Cioabă and Mim's 2026 abstract treats principally *first* clique homology of strongly regular graphs; that statement does not imply a full third-homology character for this example. The full document was not accessible in this review, so possible unquoted treatment of this particular example remains a bibliographic risk.

## Limitations
The result determines the rational full-group representation, not the integral equivariant lattice or a uniform theorem for folded cubes of all dimensions. The proof is a finite exhaustive computation coupled to standard algebraic-topology and finite-group representation identities. Although the checker evaluates all elements and includes an independent orbit-based computation, it is not an externally certified formal proof. Bibliographic priority over unpublished or inaccessible equivalent calculations cannot be proved by finite searches. Independent scientific audit has not been performed.

## References
1. J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418v1, first posted 2010-07-02, especially Theorem 3.4, https://arxiv.org/abs/1007.0418.
2. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics **134** (1998), 90–145, https://doi.org/10.1006/aima.1997.1650.
3. OEIS A355227, *Number of independent sets of size \(k\) in the \(n\)-folded cube graph*, row five, https://oeis.org/A355227.
4. E. W. Weisstein, *Clebsch Graph*, MathWorld, standard degree-five graph and automorphism conventions, https://mathworld.wolfram.com/ClebschGraph.html.
5. S. M. Cioabă and M. Mim, *On the homology groups of clique complexes of strongly regular graphs*, arXiv:2606.27328v1 (2026), https://arxiv.org/abs/2606.27328.
