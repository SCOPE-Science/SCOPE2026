# Exact variable-width alphabet spectrum of two-letter de Bruijn digraphs

## Finding

For each integer \(q\ge1\), take a \(q\)-element alphabet \(A_q\) and the directed graph \(\mathcal B_q\) with vertex set \(A_q^2\) and a single binary relation
\[
E((a,b),(c,d))\quad\Longleftrightarrow\quad b=c.
\]
Loops are retained. The language contains only \(E\) and equality: the coordinate projections, the alphabet, and all constants are *not* named. Write \(\equiv_{\mathrm{FO}^{k}}\) for equivalence with respect to all first-order sentences using at most \(k\) reusable variable symbols, without counting quantifiers, with no quantifier-depth bound.

**Theorem.** For every pair of positive integers \(q,q'\) and every \(k\ge1\),
\[
\mathcal B_q\equiv_{\mathrm{FO}^{k}}\mathcal B_{q'}
\quad\Longleftrightarrow\quad
\begin{cases}
\min(q,2)=\min(q',2),&k=1,\\
\min(q,3)=\min(q',3),&k=2,\\
\min(q,2k)=\min(q',2k),&k\ge3.
\end{cases}
\]
For each fixed \(k\), the number of distinct theories realized by this family is therefore \(2\) for \(k=1\), \(3\) for \(k=2\), and exactly \(2k\) for \(k\ge3\). Each theory has a unique smallest member *within this family*: the representative with alphabet size truncated at the displayed cutoff, containing the square of that truncated size as its number of vertices.

In particular, if \(1\le q<q'\), their minimum distinguishing variable width is
\[
w(q,q')=\begin{cases}
1,&q=1,\\
2,&q=2,\\
\max\{3,\lfloor q/2\rfloor+1\},&q\ge3.
\end{cases}
\]

## Assumptions and scope

A vertex is an ordered *two-letter word*, and adjacency is the one-step shift overlap. This is the standard length-two de Bruijn digraph, equivalently the line digraph of the complete reflexive digraph on \(q\) vertices. The theorem is about the **directed** relation and includes the loops. It concerns positive alphabet sizes only. No order, coloring, individual alphabet symbol, coordinate projection, successor function, or counting operator is present in the logical language. The full range of quantifier depths is included.

## Proof

**One variable.** The only nontrivial atomic information about a single vertex \(x\) is whether \(E(x,x)\) holds, which says that the two letters of its word agree. For \(q=1\), every vertex is looped. For every \(q\ge2\), looped and nonlooped vertices both occur. A one-variable sentence can combine existential and universal conditions on these unary types but cannot tell apart two structures with identical realized types. The formula \(\exists x\,\neg E(x,x)\) separates \(q=1\) from \(q\ge2\).

**Two variables: separating the three phases.** The same one-variable formula separates the first phase. The following formula uses only \(x,y\):
\[
\psi:=\exists x\,\exists y\bigl(E(x,x)\wedge\neg E(y,y)
\wedge\neg E(x,y)\wedge\neg E(y,x)\bigr).
\]
If \(x=(a,a)\) and \(y=(b,c)\) is nonlooped, the last two conditions demand \(a\notin\{b,c\}\). Thus \(\psi\) holds exactly when \(q\ge3\). It separates \(q=2\) from all larger alphabets.

**Two variables: permanent equivalence for \(q,q'\ge3\).** In the two-pebble game, Duplicator maintains whether each occupied vertex is looped and, if two pebbles are present, their equality and both directed edge bits. The possible local replacement patterns depend only on whether the unmoved vertex is looped, not on \(q\ge3\). Here is a complete witness table. Fix three distinct alphabet symbols \(a,b,c\). If the anchor is the looped vertex \((a,a)\), the response vertices \((a,a),(b,b),(a,b),(b,a),(b,c)\) respectively realize: equality; another loop with no directed edges; nonlooped forward-only; nonlooped backward-only; and nonlooped with neither edge. If the anchor is the nonlooped vertex \((a,b)\), the looped responses \((b,b),(a,a),(c,c)\) realize forward-only, backward-only, and neither, while the nonlooped responses \((a,b),(b,a),(b,c),(c,a),(a,c)\) realize equality, reciprocal edges, forward-only, backward-only, and neither. There are no further atomic patterns: this follows immediately from \(E((a,b),(c,d))\iff b=c\). Each table works for every alphabet size at least three.

At every round, Spoiler may change either pebble in either structure. Duplicator fixes the unmoved counterpart and chooses the response indicated by its anchor type and the requested atomic pattern. The displayed table guarantees availability in both structures, forever. This is a winning infinite two-pebble strategy. The standard pebble-game characterization therefore proves full \(\mathrm{FO}^{2}\)-equivalence for every pair \(q,q'\ge3\).

**Three or more variables: interpretation of coordinates.** Using three reusable variable symbols, define the following formulas with two free variables:
\[
F(x,y):=\exists z\,(E(z,x)\wedge E(z,y)),\qquad
S(x,y):=\exists z\,(E(x,z)\wedge E(y,z)).
\]
Writing \(x=(a,b)\) and \(y=(c,d)\), these express respectively \(a=c\) and \(b=d\). Moreover, the primitive atom \(E(x,y)\) expresses \(b=c\), and \(E(y,x)\) expresses \(d=a\); \(E(x,x)\) tests equality of the two coordinates of one word. Consequently, for any finite tuple of word-vertices, all equality and inequality conditions among *all* its coordinate positions can be expressed using at most the tuple variables plus a locally bound third variable.

A scope detail matters: in an existential formula using word variables \(x_1,\ldots,x_r\) for \(r\ge3\), the witness variable for a subformula \(F(x_i,x_j)\) or \(S(x_i,x_j)\) can be chosen from the other \(r-2\) variable names and shadowed **only in that conjunct**. This does not erase its binding in neighboring conjuncts. When \(r=2\) and \(k\ge3\), use the spare third name. Thus the complete equality diagram of all coordinate positions of \(r\le k\) selected vertices uses at most \(k\) variable names for every \(k\ge3\).

For each integer \(2\le t\le2k\), define a sentence \(\Theta_t\) demanding a tuple of \(r=\lceil t/2\rceil\) word-vertices whose \(t\) active coordinate positions are pairwise distinct: when \(t\) is even, all \(r\) words have unequal internal coordinates; when \(t\) is odd, the last word is looped and contributes one active coordinate, and the preceding words contribute two each. Conjoin the negations of the above four comparisons as appropriate for distinct positions. The preceding paragraph proves that \(\Theta_t\) is an \(\mathrm{FO}^{k}\) sentence. By its exact equality diagram, it is true in \(\mathcal B_q\) precisely when \(q\ge t\). Consequently, all distinct alphabet sizes below the cutoff \(2k\) can be separated using \(k\) variables, and a smaller size is separated from every size at least \(2k\).

**Three or more variables: permanent equivalence above the cutoff.** Let \(q,q'\ge2k\). Duplicator maintains the entire equality pattern among the \(2r\) alphabet positions appearing in the currently pebbled \(r\le k\) vertices. If Spoiler replaces one pebbled word, there remain at most \(2(k-1)\) alphabet symbols in the fixed words. The new word has at most two additional symbols, with any possible identifications to the fixed ones or to each other. Since the response alphabet has at least \(2k\) symbols, at least two unused symbols are available to realize the requested equality pattern. This invariant preserves vertex equality, loops, and each directed edge relation \(E(x,y)\), all of which depend only on coordinate equalities. It can be maintained for arbitrarily many rounds, proving \(\mathrm{FO}^{k}\)-equivalence above the cutoff. The lower and upper directions finish the theorem.

The theory counts, minimal representatives, and distinguishing-width formula follow by taking the smallest width whose cutoff exceeds the smaller of two unequal alphabet sizes, with the separately established widths one and two.

## Verification

Two standalone Python 3 scripts accompany this proof. `verify_pair_extensions.py` exhaustively checks the two-pebble response-pattern table for alphabet sizes \(3\) through \(12\), both low-width distinguishing predicates for sizes \(1\) through \(12\), and the coordinate-equality abbreviations for sizes \(1\) through \(8\). It also constructs the canonical distinct-symbol diagrams for selected widths and thresholds. `verify_three_pebble.py` independently runs exact noncounting three-pebble fixed-point refinement of every length-two de Bruijn digraph of alphabet sizes \(1\) through \(7\); it verifies that the resulting full three-variable theory classes are exactly those given by truncation at six. It uses only the Python standard library.

Run both scripts from the directory containing them with `python3 verify_pair_extensions.py` and `python3 verify_three_pebble.py`. The accompanying `verification_pair.txt` and `verification_three.txt` record the actual expected outputs. These finite checks are corroboration, not a substitute for the unrestricted mathematical argument above.

## Relationship to prior work

De Bruijn digraphs and their iterated-line-digraph representation are classical; Du, Lyuu, and Hsu (1993) study connectivity, and Hasunuma and Nagamochi (2001) study independent spanning trees. The latter paper explicitly identifies the de Bruijn family as iterated line digraphs of complete reflexive digraphs. Grohe and Otto (arXiv 1204.1990, Section 2) give the general characterization of finite-variable equivalence by pebble games, including its counting-free form. Etessami, Vardi, and Wilke (BRICS RS-97-5) study the two-variable fragment over words and linear temporal logic, a different class and signature. These sources supply objects and general methods, not the exact \(k\)-variable alphabet cutoff established here.

Fàbrega, Martí-Farré, and Muñoz (2023) analyze alphabet-permutation orbit classes and distance layers of de Bruijn and Kautz digraphs. Orbit enumeration does not itself imply that all \(\mathrm{FO}^{k}\) sentences collapse at the threshold, nor the sharp two-variable exception. A published result on simplified undirected de Bruijn graphs concerns a different adjacency signature and word-representability. Searches of related record titles and primary literature did not identify the present theorem. A more general, unidentified definable-incidence or line-digraph theorem might entail it; exhaustive historical-priority certification has not been established.

## Limitations

The proof is restricted to the *length-two* directed de Bruijn digraphs with loops retained, in pure adjacency language. The formula for \(F\) and \(S\) uses the complete reflexive alphabet digraph and need not work for de Bruijn digraphs of other word lengths, Kautz digraphs, loop-deleted versions, or undirected simplifications. Counting quantifiers, extra coordinate functions, and named alphabet symbols change the logical power. The finding does not assert a result for these altered languages or families. The priority comparison leaves a residual risk from general first-order interpretations and unidentified prior theorems. Independent mathematical review has not been performed.

## References

1. D. Z. Du, Y.-D. Lyuu, D. F. Hsu, *Line Digraph Iterations and Connectivity Analysis of de Bruijn and Kautz Graphs*, IEEE Transactions on Computers 42(5) (1993), 612–616, doi:10.1109/12.223681. The publisher records first publication on 1993-05-31. The connection with this finding is the graph family, not any claimed logical classification.
2. T. Hasunuma and H. Nagamochi, *Independent Spanning Trees with Small Depths in Iterated Line Digraphs*, Discrete Applied Mathematics 110 (2001), 189–211, doi:10.1016/S0166-218X(00)00269-9. Sections 1 and 4 give the iterated-line-digraph model and spanning-tree results.
3. M. Grohe and M. Otto, *Pebble Games and Linear Equations*, arXiv:1204.1990, first posted 2012-04-09. Section 2, Theorem 2.1, records the pebble-game characterization; the work's general counting-free algebraic framework does not state this de Bruijn classification.
4. K. Etessami, M. Y. Vardi, and T. Wilke, *First-Order Logic with Two Variables and Unary Temporal Logic*, BRICS RS-97-5 (March 1997), doi:10.7146/brics.v4i5.18784.
5. J. Fàbrega, J. Martí-Farré, and X. Muñoz, *Distance-Layer Structure of the De Bruijn and Kautz Digraphs*, Networks (2023), doi:10.1002/net.22177. Its alphabet-permutation orbit data are not a finite-variable logical equivalence classification.
