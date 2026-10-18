# Two sharp locating-total prism counterexamples in distinct residue classes

## Finding

For the circular prism \(P_n=C_n\square K_2\), the locating-total domination number satisfies
\[
\gamma_t^{L}(P_8)=7,\qquad \gamma_t^{L}(P_{11})=9.
\]
These are simultaneous sharp counterexamples to the two exceptional congruence branches of Conjecture 2 in Raza, Iqbal, Khan, and Botmart (2021): that conjecture predicts \(8\) when \(n=8\equiv3\pmod5\) and \(10\) when \(n=11\equiv1\pmod5\). Both actual values attain the universal cubic-regular lower bound \(\lceil4n/5\rceil\).

## Assumptions and scope

All graphs are finite, simple, and undirected. For an integer \(n\ge3\), write \(V(P_n)=\{v_i,w_i: i\in\mathbb Z/n\mathbb Z\}\), with edges \(v_iv_{i+1}\), \(w_iw_{i+1}\), and \(v_iw_i\), indices modulo \(n\). A locating-total dominating set \(D\subseteq V(P_n)\) satisfies (i) \(N(u)\cap D\ne\varnothing\) for every vertex \(u\), including those in \(D\), and (ii) the open-neighborhood signatures \(N(u)\cap D\) of distinct vertices \(u\notin D\) are pairwise different. Only these two exact graph orders are asserted. In particular, no infinite-family formula or eventual periodicity is claimed.

## Proof

**General sharp lower bound.** Let \(G\) be any \(d\)-regular graph on \(N\) vertices with a locating-total dominating set \(D\) of cardinality \(k\), and put \(U=V(G)\setminus D\), \(|U|=N-k\). Distinct nonempty signatures on \(U\) imply at most \(k\) vertices in \(U\) have singleton signatures. Therefore the number \(e(D,U)\) of crossing edges obeys
\[
e(D,U)=\sum_{u\in U}|N(u)\cap D|\ge2(N-k)-k=2N-3k.
\]
Total domination means every selected vertex has at least one selected neighbor, so each selected vertex has at most \(d-1\) neighbors in \(U\); hence \(e(D,U)\le(d-1)k\). Combining gives \((d+2)k\ge2N\). For \(P_n\), \(d=3\), \(N=2n\), so
\[\gamma_t^{L}(P_n)\ge\left\lceil\frac{4n}{5}\right\rceil.\]

**Seven-vertex witness at order \(8\).** Choose
\[
D_8=\{v_0,v_1,v_2,v_4,v_6,w_4,w_6\}.
\]
Every vertex of \(D_8\) has a selected neighbor: the selected consecutive cycle triple \(v_0,v_1,v_2\) is internally totally dominated, and \(v_4w_4\) and \(v_6w_6\) are selected rungs. For the nine unselected vertices, the full signature list is
\[
\begin{array}{c|ccccccccc}
u&v_3&v_5&v_7&w_0&w_1&w_2&w_3&w_5&w_7\\ \hline
N(u)\cap D_8&\{v_2,v_4\}&\{v_4,v_6\}&\{v_0,v_6\}&\{v_0\}&\{v_1\}&\{v_2\}&\{w_4\}&\{w_4,w_6\}&\{w_6\}
\end{array}
\]
Every displayed signature is nonempty, and all nine are different. Consequently \(D_8\) is locating-total with \(|D_8|=7\), while the lower bound gives \(\gamma_t^{L}(P_8)\ge\lceil32/5\rceil=7\).

**Nine-vertex witness at order \(11\).** Choose
\[
D_{11}=\{v_0,v_1,v_2,v_4,v_9,w_4,w_6,w_7,w_9\}.
\]
Every selected vertex has a selected neighbor: the triple \(v_0,v_1,v_2\), rungs \(v_4w_4\) and \(v_9w_9\), and bottom-layer edge \(w_6w_7\) together cover the selected vertices. For the thirteen unselected vertices, the signatures are
\[
\begin{array}{c|cccccc}
u&v_3&v_5&v_6&v_7&v_8&v_{10}\\ \hline
N(u)\cap D_{11}&\{v_2,v_4\}&\{v_4\}&\{w_6\}&\{w_7\}&\{v_9\}&\{v_0,v_9\}
\end{array}
\]
and
\[
\begin{array}{c|ccccccc}
u&w_0&w_1&w_2&w_3&w_5&w_8&w_{10}\\ \hline
N(u)\cap D_{11}&\{v_0\}&\{v_1\}&\{v_2\}&\{w_4\}&\{w_4,w_6\}&\{w_7,w_9\}&\{w_9\}
\end{array}
\]
These thirteen signatures are nonempty and pairwise distinct, proving feasibility with \(|D_{11}|=9\). The lower bound gives \(\gamma_t^{L}(P_{11})\ge\lceil44/5\rceil=9\).

**Conjecture comparison.** Conjecture 2 in the cited 2021 paper proposes the upper-bound expression \(\lceil4n/5\rceil+1\) as the exact locating-total domination number for \(n\equiv1,3\pmod5\). At \(n=8\) and \(n=11\), the two values above are exactly one smaller. This contradicts both of those predicted congruence branches; it does not challenge the paper's proved upper bounds or its other congruence cases.

## Verification

The accompanying standalone `verify.py` reconstructs both circular prisms from modular adjacency, independently checks every vertex for total domination, compares every outside signature, confirms sizes and congruence-class conjectural predictions, and checks the cubic-regular lower bound. It additionally examines all \(14{,}893\) sets of size at most six in \(P_8\), finding none feasible; this finite exhaustive check is supplementary to the general lower-bound proof. Run `python verify.py` (standard Python 3 only); `verification_output.txt` records the actual execution output. The proof of the lower bound is mathematical and does not rely on the finite search.

## Relationship to prior work

Raza, Iqbal, Khan, and Botmart (2021), *Computing locating-total domination number in some rotationally symmetric graphs*, Theorem 5 and Conjecture 2, explicitly study precisely \(C_n\square K_2\). Theorem 5 already supplies the relevant general lower bound and an upper bound one larger for \(n\equiv1,3\pmod5\); these are not claimed as new. The present two small sharp constructions settle the predicted equalities negatively at both residue classes. The distinct invariant of total identifying codes and results on \(K_n\square K_2\) concern different questions and do not imply these two locating-total minima. A 2024 comparative study of domination parameters in antiprisms addresses ordinary total domination and other variants, not these exact locating-total prism cases.

## Limitations

Only \(n=8\) and \(n=11\) are settled here; no formula for all lengths is asserted. An absence of matching indexed records does not prove priority: a published correction, exhaustive table, or independent earlier derivation outside inspected sources could exist. No independent scientific audit has been performed.

## References

1. H. Raza, N. Iqbal, H. Khan, T. Botmart, *Computing locating-total domination number in some rotationally symmetric graphs*, Science Progress 104(4) (first published online 2021-11-17). DOI: 10.1177/00368504211053417. https://journals.sagepub.com/doi/10.1177/00368504211053417
2. *Dominance Parameters in Prism Graphs: A Comparative Study of Minimum Dominating Sets*, Mathematical Modelling of Engineering Problems (2024), DOI: 10.18280/mmep.110112; related variants, not a covering locating-total prism classification.
