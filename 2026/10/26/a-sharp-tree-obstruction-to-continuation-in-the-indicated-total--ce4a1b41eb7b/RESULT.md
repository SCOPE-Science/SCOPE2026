# A sharp tree obstruction to continuation in the indicated total domination game

## Finding

**Theorem.** For every integer \(r\geq 0\), let \(T_r\) be the tree with vertices \(a,b,c,d,e,f,h_1,\ldots,h_r\) and edges \(ab,bc,cd,de,cf,bh_1,\ldots,bh_r\). Thus \(T_r\) is a five-vertex path with a leaf at its central vertex and \(r\) additional leaves at the neighboring vertex \(b\). Put \(P=\{f\}\). In the indicated total domination game,
\[
\gamma_t^{\mathrm i}(T_r)=3,\qquad
\gamma_t^{\mathrm i}(T_r\mid P)=4.
\]
Consequently, for every integer \(n\geq6\), there is a tree on \(n\) vertices for which declaring just **one** vertex already totally dominated increases the optimal duration by one move.

The order six is sharp even if arbitrary nested declared sets are allowed: for every tree \(H\) on at most five vertices with no isolated vertices and all \(B\subseteq A\subseteq V(H)\),
\[
\gamma_t^{\mathrm i}(H\mid A)\leq\gamma_t^{\mathrm i}(H\mid B).
\]
Up to isomorphism, \(T_0\) is the **only** tree of order six that admits any strict reverse inequality for some \(B\subseteq A\). The sharp-order assertion and uniqueness are exact finite-enumeration results, with exhaustive checker supplied; the infinite-family formulas have a direct proof.

## Assumptions and scope

All graphs are finite and simple. The indicated total domination game is played on an isolate-free graph \(G\) with a declared set \(P\) of vertices already totally dominated. On each turn Dominator indicates a vertex that has **not** yet been totally dominated, and Staller selects an as-yet-unselected neighbor of that vertex. A selected vertex totally dominates all its open neighbors. The game ends once every vertex is either declared dominated or has a selected neighbor. Dominator minimizes the number of Staller selections; Staller maximizes it. Write \(\gamma_t^{\mathrm i}(G\mid P)\) for the optimal number of selections, and \(\gamma_t^{\mathrm i}(G)\) when \(P=\varnothing\). The declaration does not select a vertex and does not alter any edges.

The family has \(6+r\) vertices and one distinguished declared leaf \(f\). The sharp-order statement covers all nontrivial trees with at most six vertices and **all** initial declared-set pairs, not merely the family \(T_r\).

## Proof

**1. A unique three-vertex total dominating set.** Every total dominating set of \(T_r\) contains \(b\), because \(a\) is a leaf, and contains \(d\), because \(e\) is a leaf. The vertices \(b,d\) are not adjacent, so to dominate both using just one further selected vertex requires a common neighbor. Their only common neighbor is \(c\). The set \(\{b,c,d\}\) indeed totally dominates all vertices, including \(f\) and the \(h_j\). Hence the total domination number is three and \(\{b,c,d\}\) is its unique three-element total dominating set.

**2. Ordinary game length.** Dominator can indicate \(f\), forcing Staller to select \(c\); then indicate \(a\), forcing \(b\); then indicate \(e\), forcing \(d\). These indications are legal when made: after selecting \(c\), the vertices \(a,c,e\) are not yet totally dominated, and after selecting \(b\), \(e\) is not dominated. The resulting three selections totally dominate \(T_r\). No ordinary play can finish in fewer than three moves because it ends in a total dominating set. Thus \(\gamma_t^{\mathrm i}(T_r)=3\).

**3. Four-move upper bound after declaring \(f\).** Declare only \(f\) dominated initially. Dominator indicates \(a\), forcing \(b\), and indicates \(e\), forcing \(d\). At this point all vertices except possibly \(b,d\) are dominated (the leaves \(h_j\) are dominated by \(b\), and \(f\) was declared). For each remaining undominated vertex, Dominator indicates it; each resulting Staller choice newly dominates that vertex. At most two further selections are required. Hence \(\gamma_t^{\mathrm i}(T_r\mid\{f\})\leq4\).

**4. Four-move lower bound after declaring \(f\).** Staller prevents the unique three-vertex total dominating set \(\{b,c,d\}\) from being the set of the first three selections, independently of Dominator's first indication.

If Dominator first indicates \(b\), Staller selects leaf \(a\); if Dominator first indicates \(d\), Staller selects leaf \(e\); if Dominator first indicates \(c\), Staller selects leaf \(f\). In each case the first selected vertex lies outside the unique three-element total dominating set, so completion in three moves is impossible.

If Dominator first indicates \(a\) or any \(h_j\), Staller is forced to select \(b\); if he first indicates \(e\), she is forced to select \(d\). In either case \(c\) is immediately totally dominated, so Dominator cannot subsequently indicate \(c\). Nor can he indicate \(f\), since it was declared dominated. On any later legal indication of \(b\), Staller can choose a leaf adjacent to \(b\) (the leaf \(a\) is initially unselected); on a legal indication of \(d\), she can choose leaf \(e\). These choices are available whenever the respective indication first occurs, and afterwards that vertex is dominated and cannot be indicated again. All other legal indications can be answered without choosing \(c\) (indications of leaves force their support vertex). Thus Staller can avoid ever selecting \(c\). Since \(c\) belongs to the unique three-vertex total dominating set, at least four selections are needed. Therefore \(\gamma_t^{\mathrm i}(T_r\mid\{f\})\geq4\), proving the family formulas for **every** \(r\geq0\).

**5. Sharp minimum order and uniqueness.** The standalone exact checker `checker.py` exhaustively generates all labeled trees on \(n\in\{2,3,4,5,6\}\) vertices from their Prüfer sequences, partitions the resulting trees into isomorphism classes using their canonical recursively sorted rooted-parenthesis encodings, and for each class evaluates the complete minimax game on every declared set and every nested pair. Its recurrence, for the selected set \(S\) and initially declared set \(P\), is
\[
 g(S,P)=\begin{cases}
 0,&P\cup N(S)=V,\\
 1+\displaystyle\min_{v\notin P\cup N(S)}\max_{u\in N(v)}g(S\cup\{u\},P),&\text{otherwise}.
 \end{cases}
\]
Here \(N(S)=\bigcup_{u\in S}N(u)\). An undominated indicated vertex has no selected neighbor, so all \(u\in N(v)\) in the recurrence are unselected and legal. Recursion terminates because the selected set strictly increases. Enumerating all Prüfer sequences is exhaustive for labeled trees, and rooted-tree canonical coding is a complete isomorphism invariant; the checker examines **all** nested declared-set pairs of each representative. The five class counts are \(1,1,2,3,6\) respectively, with no strict continuation violations for orders two through five, and exactly one violating isomorphism class at order six. Its canonical code matches \(T_0\). This is a finite exhaustive certificate of the sharp boundary, not an extrapolation from a sample.

## Verification

Run `python3 checker.py` in a directory containing the supplied standalone file. No third-party Python modules are required. The checker returns `CHECKS_PASSED`, enumerates \(1,3,16,125,1296\) labeled trees of orders \(2,3,4,5,6\), checks every declared-set pair in each of \(1,1,2,3,6\) isomorphism classes, and reports exactly one offending class of order six. It independently evaluates both game lengths for \(T_r\) with \(0\leq r\leq7\). These additional finite family checks are consistency tests, not the proof of the theorem for unbounded \(r\). The exact output of an actual execution is included as `checker_output.txt`.

## Relationship to prior work

Henning and Rall introduced the indicated total domination game and documented the failure of the continuation principle by an eight-vertex graph built from a six-cycle, a chord and two added leaves, declaring **two** vertices dominated; their example has cycles. Their article also asks about ordinary-game values on trees. The present theorem proves a sharper continuation boundary: failure already occurs in a six-vertex **tree** with one declared vertex, it is the only offending tree of that smallest order, and such one-vertex failures occur at **every** larger tree order. It does **not** assert a counterexample to their distinct question on equality between the ordinary indicated total domination number and upper total domination on trees; indeed ordinary values here remain three.

Brešar, Bujtás, Iršič, Rall and Tuza study the related *indicated domination game*, where Staller may select from a **closed**, not open, neighborhood. The present result concerns the total (open-neighborhood) game; results for the closed-neighborhood version cannot be substituted. The published and arXiv references below were inspected for their definitions and relevant stated results, and an equivalent tree-specific continuation boundary was not identified. Bibliographic priority beyond those accessible sources and the queried research records is not certified.

## Limitations

The theorem does not give a universal upper bound on how much predomination can alter the game in arbitrary trees, does not claim that the displayed family exhausts all larger-order counterexamples, and does not resolve the ordinary-game tree equality question. Its sharp minimum-order classification depends on an exhaustive **finite** computation with the complete checker included; the unbounded family has a separate theoretical strategy proof. Independent validation has not been performed.

## References

1. M. A. Henning and D. F. Rall, *Indicated total domination game*, arXiv:2310.03506, initially public 5 October 2023; revised version 3, 1 February 2024, Section 2 and the tree question in Section 3. https://arxiv.org/pdf/2310.03506
2. B. Brešar, Cs. Bujtás, V. Iršič, D. F. Rall and Zs. Tuza, *Indicated domination game*, arXiv:2310.14647, 2023, particularly the closed-neighborhood game definition. https://arxiv.org/pdf/2310.14647
