# Signed-burning reachable codes and sharp plurality phases on complete multipartite graphs

## Finding

Let \(G=K_{n_1,\ldots,n_r}\) be a connected complete multipartite graph with \(r\ge2\), all \(n_i\ge1\), and \(n=|V(G)|\). Let \(E\) be the set of vertices lying in parts of size at least two, let \(e=|E|\), let \(s=n-e\) be the number of singleton-part vertices, and put \(q=\lfloor n/2\rfloor\). Equip \(G\) with any **balanced** signing \(\sigma:E(G)\to\{\pm1\}\), i.e. every cycle has positive sign-product. Let \(Y(\Gamma)\) be the plurality number for the synchronous two-colour signed-burning process of Fallat–Gupta–Khodamoradi–Zilles [1].

**Theorem.** Choose vertex signs \(\phi(v)\in\{\pm1\}\) such that \(\sigma(uv)=\phi(u)\phi(v)\) on all edges, and put \(U=\{v:\phi(v)=-1\}\). Such a choice exists and is unique up to simultaneous negation. Then the complete set of reachable final signed colourings is
\[
\mathcal R(\Gamma)=\phi\cdot\left(\{\mathbf{1},-\mathbf{1}\}\ \cup\ \{\eta_v,-\eta_v:v\in E\}\right),
\]
where \(\eta_v\) is \(-1\) at \(v\) and \(+1\) everywhere else, and multiplication is coordinatewise. The reachable code has precisely \(2+2e\) words. In particular, **every** balanced signing on \(G\) has the exact plurality
\[
\boxed{\displaystyle
Y(\Gamma)=n-\min\left\{|U|-\mathbf{1}_{U\cap E\ne\varnothing},\quad
n-|U|-\mathbf{1}_{(V\setminus U)\cap E\ne\varnothing}\right\}.}
\]
This expression does not depend on choosing \(\phi\) or \(-\phi\).

Write \(Y_*(G)=\min_\sigma Y(G,\sigma)\), where the minimum is over all balanced signings. Then
\[
\boxed{\displaystyle Y_*(G)=
\begin{cases}
\lceil n/2\rceil,&e=0,\\
\lceil n/2\rceil,&e>0,\ n\text{ odd and }s\ge q,\\
\lceil n/2\rceil+1,&\text{otherwise}.
\end{cases}}
\]
Thus a strict, one-vertex plurality improvement over the general two-colour baseline occurs for every noncomplete even-order complete multipartite graph, and for odd order precisely when there are fewer than \(q\) singleton parts.

The number \(H(G)\) of **distinct balanced edge signings** attaining \(Y_*(G)\), not identifying graph automorphisms, is exactly
\[
\boxed{\displaystyle H(G)=
\begin{cases}
\tfrac{1}{2}\binom{n}{q},&e=0,\ n\text{ even},\\
\binom{n}{q},&e=0,\ n\text{ odd},\\
\tfrac{1}{2}\binom{n}{q}+\binom{s}{q-1},&e>0,\ n\text{ even},\\
\binom{s}{q},&e>0,\ n\text{ odd},\ s\ge q,\\
\binom{n}{q}+\binom{s}{q-1},&e>0,\ n\text{ odd},\ s<q.
\end{cases}}
\]
Use the convention \(\binom{a}{b}=0\) when \(b<0\) or \(b>a\).

Equivalently, the binary code of reachable colourings for the all-positive graph is the antipodal repetition code, augmented by precisely the one-coordinate flips at non-singleton vertices. Its Hamming covering radius is \(n-Y_*(G)\), and \(H(G)\) enumerates its antipodal pairs of deepest words.

## Assumptions and scope

Graphs are finite, simple and labelled, with at least two nonempty multipartite parts. All signs are \(\pm1\). The signing is balanced, meaning the sign-product around **every** cycle equals \(+1\); it is not assumed that all edges are positive. No assertion is made for arbitrary unbalanced signings or for an edgeless graph. Since \(r\ge2\), the graph is connected.

The burning process starts with every vertex unburned. In each round, every still-unburned vertex first receives the sign of the sum of signed colours of its previously burned neighbours when this sum is nonzero; ties remain unburned. Then, provided an unburned vertex remains, one of them is ignited in either colour. Burned vertices retain their colours. The process ends as soon as all vertices are burned. This is exactly the spread-before-ignition convention in Definition 2.1 of [1]. Identify the two colours with \(+1\) and \(-1\). The plurality \(Y\) maximizes the larger colour-class size over all completed ignition sequences.

## Proof

**1. Switching to the positive graph.** Fix a root \(w\). For every vertex \(v\), let \(\phi(v)\) be the product of edge signs along any path from \(w\) to \(v\), with \(\phi(w)=1\). Balance makes this path-independent: two paths give a closed walk, whose signed product is \(+1\) because every simple-cycle product is positive. Thus \(\sigma(uv)=\phi(u)\phi(v)\). Connectedness ensures uniqueness up to global negation.

For any state \(x:V\to\{0,\pm1\}\), put \((\phi x)(v)=\phi(v)x(v)\). If \(x\) is a state on the positive graph, the signed influence in the switched graph at \(v\) is
\[
\sum_{u\sim v}\sigma(uv)\phi(u)x(u)
=\phi(v)\sum_{u\sim v}x(u).
\]
The zero/nonzero status is unchanged and the sign of any nonzero influence is multiplied by \(\phi(v)\). Choosing each ignition colour multiplied by \(\phi(v)\) therefore gives, by induction on rounds, a bijection of burning sequences and the identity \(\mathcal R(\Gamma)=\phi\cdot\mathcal R(G_+)\). This also reconstructs the relevant switching relation in [1, Lemma 2.3] without assuming it.

**2. Complete reachable code.** On the all-positive graph, let the first ignition be at \(u\) in multipartite part \(V_i\), in colour \(c\in\{\pm1\}\). At the spread step of round two, every vertex outside \(V_i\) is adjacent to \(u\) and becomes colour \(c\). No other vertex inside \(V_i\) has a burned neighbour at that moment, so all remain unburned. If \(|V_i|=1\), the process ends with the constant colouring \(c\mathbf{1}\).

If \(|V_i|\ge2\), the round-two ignition may colour one different vertex \(v\in V_i\) either \(c\) or \(-c\). Every remaining vertex of \(V_i\) sees all outside-part vertices in colour \(c\), and so turns colour \(c\) at the round-three spread step. Therefore the terminal colouring is \(c\mathbf{1}\) or differs from it at exactly one vertex \(v\in E\). Conversely, for each \(v\in E\), first ignite another vertex of its part in colour \(c\) and ignite \(v\) in colour \(-c\) at round two; this reaches \(c\eta_v\). No other sequences are possible. There are \(2+2e\) distinct words (when \(e>0\), necessarily \(n\ge3\)).

**3. Exact plurality.** Let \(C=\mathcal R(G_+)\) and \(U=\{v:\phi(v)=-1\}\). The number of green vertices of \(\phi c\) is the Hamming distance \(d_H(\phi,c)\). Because \(C=-C\), maximizing the larger terminal colour class equals \(n-\min_{c\in C}d_H(\phi,c)\). The nearest codeword around \(+\mathbf{1}\) has distance \(|U|-1\) if a negative coordinate lies in \(E\), and distance \(|U|\) otherwise. Around \(-\mathbf{1}\), the analogous distance is \(n-|U|-1\) if a positive coordinate lies in \(E\), and \(n-|U|\) otherwise. Their minimum gives the displayed formula.

**4. Covering radius.** If \(E=\varnothing\), then \(C=\{\pm\mathbf{1}\}\), and the radius is \(q=\lfloor n/2\rfloor\). Suppose \(E\ne\varnothing\). Every \(U\) of size \(m\) has distance at most \(\min(m,n-m)\) to \(C\).

If \(n=2q\), every word with \(m=q\) has distance exactly \(q-1\): at least one of \(U\) and its complement intersects \(E\), and neither of the two distance terms falls below \(q-1\). If \(m\ne q\), then \(\min(m,n-m)\le q-1\). Thus the radius is \(q-1\).

If \(n=2q+1\), a word can have distance \(q\) only when \(m=q\) or \(m=q+1\). For \(m=q\), the formula gives distance \(q\) precisely when \(U\cap E=\varnothing\); the complementary case is symmetric. Such a word exists precisely when \(s\ge q\). If \(s<q\), all words of sizes \(q\) and \(q+1\) have distance exactly \(q-1\), and all other words have distance at most \(q-1\). Hence the radius is \(q\) when \(s\ge q\) and \(q-1\) otherwise. Since switching choices \(\phi\) exhaust all balanced signings up to global sign, \(Y_*(G)=n-\rho(C)\) as claimed.

**5. Counting the minimizing signings.** Exactly two vertex sign vectors, \(\phi\) and \(-\phi\), give any fixed balanced edge signing; there are \(2^{n-1}\) signings in all. Deepest vectors are the words at distance \(\rho(C)\) from \(C\).

If \(E=\varnothing\), they are all words of size \(q\), together with size \(q+1\) when \(n\) is odd. This gives the first two cases of \(H(G)\) after dividing by two.

For \(E\ne\varnothing\) and \(n=2q\), deepest words are every \(q\)-subset, all \((q-1)\)-subsets of the \(s\) singleton-part vertices, and complements of the latter. Their number is \(\binom{n}{q}+2\binom{s}{q-1}\).

For \(E\ne\varnothing\), \(n=2q+1\), and \(s\ge q\), deepest words are all \(q\)-subsets of the singleton-part vertices and their complements, giving \(2\binom{s}{q}\) words. When \(s<q\), deepest words instead consist of **all** \(q\)-subsets and their complements, plus all \((q-1)\)-subsets of singleton-part vertices and their complements. Their number is \(2\binom{n}{q}+2\binom{s}{q-1}\). Dividing by two completes the proof.

## Verification

The self-contained program `verify_burning_multipartite.py` directly simulates the original simultaneous signed spread and subsequent single-vertex ignition with memoized exhaustive branching; it does **not** assume the switching identity or predicted reachable-code description when generating outcomes. It checks every multipartite part-size partition with at least two parts through \(n=7\), and every balanced signing represented by fixing one vertex's switching sign. For each instance it compares the entire enumerated terminal-code set, exact plurality, covering radius and number of worst balanced signings with the theorem.

Run `python3 verify_burning_multipartite.py`. The expected output is `VERIFY_OK graph_types=37 signings=1354 terminal_states=14772 max_order=7`. These finite tests are checks, not substitutes for the preceding unrestricted proof.

## Relationship to prior work

Fallat, Gupta, Khodamoradi and Zilles [1] define the signed-burning dynamics, establish switching covariance (Lemma 2.3), interpret plurality through a binary reachable code and its covering radius (Proposition 2.9 and Remark 2.10), and study exact signed paths in Section 3. The general coding correspondence is **prior work**, not a new result here. What is determined here is the exact reachable code, every balanced-signature plurality value, its global minimum and the sharp deep-hole multiplicity for **all** connected complete multipartite graphs.

The switching characterization of balanced signed graphs goes back to Harary [2]. The proof of step 1 is included for self-containment; balance-to-switching equivalence is **not** presented as new. The method and conclusion concern plurality and signed propagation, not the ordinary burning number or signed domination.

For example, with five vertices, \(K_{2,2,1}\) has \(s=1<q=2\) and minimum plurality \(4\), while \(K_{2,1,1,1}\) has \(s=3\ge q\) and minimum plurality \(3\). This parity-sensitive threshold is invisible to a plain graph-degree or ordinary burning-number calculation.

## Limitations

The formulas hold only for balanced signatures (all cycle sign-products positive), not for arbitrary signs on a graph with cycles. In particular, a single negative edge of a complete bipartite graph containing a four-cycle is unbalanced and is outside the theorem. The output does not assign an independent proof-review status and makes no claim about unindexed parallel derivations. The brute-force checks cover only finitely many small graphs; all infinite assertions are justified in the proof.

## References

[1] Shaun Fallat, Himanshu Gupta, Kamyar Khodamoradi and Sandra Zilles, *Burning Signed Graphs*, arXiv:2610.02506v1, first publicly posted 2026-10-01. https://arxiv.org/abs/2610.02506

[2] Frank Harary, *On the notion of balance of a signed graph*, Michigan Mathematical Journal 2 (1953/54), 143–146. This classical reference is cited in [1] for the balance-switching criterion.
