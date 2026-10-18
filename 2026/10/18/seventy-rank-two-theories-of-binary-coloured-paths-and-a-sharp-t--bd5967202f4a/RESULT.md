# Seventy rank-two theories of binary-coloured paths and a sharp ten-vertex model bound

## Finding
Let \(\mathcal P\) be the class of nonempty finite simple undirected paths, including the one-vertex path, whose vertices are partitioned by two **named** unary predicates \(P_0,P_1\). The relational language consists of equality, undirected adjacency \(E\), and those predicates; it contains **no** order, directed successor, endpoint constants, or counting quantifiers. Let \(A\equiv_2 B\) mean that \(A,B\) satisfy the same ordinary first-order sentences of quantifier rank at most \(2\).

**Theorem.** Exactly \(70\) distinct \(\equiv_2\)-classes occur in \(\mathcal P\), of which \(62\) use both colours. Every such class has a representative with at most \(10\) vertices, and this is the best possible uniform bound. Exactly two classes first have representatives of length \(10\), represented in linear path notation by `0011001100` and `1100110011`.

The numbers of classes whose **smallest** representative has \(n\) vertices, for \(1\le n\le10\), are
\[
(2,3,6,10,14,18,10,5,0,2).
\]
In particular, every rank-two first-order sentence satisfied by at least one binary-coloured path is satisfied by one with at most \(10\) vertices. A pair of coloured paths is rank-two equivalent precisely when the two paths realize the same set of local colour/adjacency/nonadjacency types defined below.

## Assumptions and scope
A word \(w=c_1\cdots c_n\in\{0,1\}^n\), with \(n\ge1\), encodes the vertex-labelled path with edges exactly between consecutive positions, and \(P_j(i)\) iff \(c_i=j\). Reversal gives an isomorphic coloured path; colour complementation is **not** an isomorphism because the predicates are named. A colour may have an empty class. Graph adjacency is symmetric, irreflexive, and is the only binary relation.

For a vertex \(v\) write \(c(v)\in\{0,1\}\) for its colour, and put
\[
N(v)=\{j:\exists u\;(E(v,u)\land P_j(u))\},\qquad
F(v)=\{j:\exists u\;(u\ne v\land\neg E(v,u)\land P_j(u))\}.
\]
Define the **rank-one pointed profile set**
\[
\Sigma(A)=\{(c(v),N(v),F(v)):v\in A\}.
\]
The sets record the *existence*, not multiplicity, of each neighbour and each distinct non-neighbour colour.

## Proof
**Step 1: the exact two-round logical invariant.** Over a vocabulary with these two unary colours and simple undirected adjacency, the quantifier-free two-point atomic diagram of \((v,u)\) is determined by their colours and whether \(u=v\), \(E(v,u)\), or neither. With \(v\) fixed, an arbitrary rank-one formula in the variable \(v\) is a Boolean combination of quantifier-free facts about \(v\) and assertions \(\exists u\,\theta(v,u)\) for quantifier-free \(\theta\). Consequently its truth depends exactly on \((c(v),N(v),F(v))\); conversely every possible such profile is defined by a conjunction of presence and absence assertions of this shape. Every closed rank-two formula is, up to Boolean combinations and logical duality, of the form \(\exists v\,\psi(v)\) with \(\psi\) of rank at most one. Hence
\[
A\equiv_2 B\quad\Longleftrightarrow\quad\Sigma(A)=\Sigma(B).
\]
This uses ordinary first-order logic with unlimited variables; rank two permits only two nested quantifiers along any syntactic branch.

**Step 2: finitely many exact append states.** Introduce an end marker \(\#\) not belonging to \(\{0,1\}\), and for a path word \(w\) write \(c_0=c_{n+1}=\#\). Its position-window at \(i\) is \((c_{i-1},c_i,c_{i+1})\). There are \(18\) formally possible windows because the centre has two choices and either neighbour has three choices. Encode a word by the finite state
\[
q(w)=(a_0,a_1,W,\ell,b),
\]
where \(a_j=\min(4,|\{i:c_i=j\}|)\); \(W\) contains exactly the completed windows at positions \(1,\ldots,n-1\); \(b=c_n\); and \(\ell=c_{n-1}\) if \(n>1\), otherwise \(\ell=\#\). A singleton of colour \(j\) starts at state \((\delta_{0j},\delta_{1j},\varnothing,\#,j)\). On appending a colour \(d\), use the deterministic update
\[
(a_0,a_1,W,\ell,b)\longmapsto
\bigl(\min(4,a_0+[d=0]),\min(4,a_1+[d=1]),
W\cup\{(\ell,b,d)\},b,d\bigr).
\]
Here \([\cdot]\) equals one when its proposition is true and zero otherwise. The complete set of position-windows of the current word is \(W\cup\{(\ell,b,\#)\}\).

For a window \((L,C,R)\), neighbour colours are precisely the nonmarker values among \(L,R\). The presence of a distinct *non-neighbour* of colour \(j\) is equivalent to
\[
a_j> [L=j]+[C=j]+[R=j].
\]
This remains exact under truncation at \(4\), since the window contains at most \(3\) actual positions. Thus \(\Sigma(A)\) is explicitly calculable from \(q(w)\) alone, without access to the full word.

**Step 3: complete finite closure and optimal representatives.** Start with the two singleton states and follow both append transitions from **every** newly reached state until the queue is empty. The accompanying standalone program `enumerate_profiles.py` implements precisely the displayed integer/set operations; it discovers \(760\) distinct reachable states, each with both outgoing transitions in the visited set. Therefore every binary word of every length has a visited state. Their evaluated signatures \(\Sigma\) comprise exactly \(70\) distinct values. Breadth-first exploration also records the shortest word reaching each state. Taking the shortest word over states with identical \(\Sigma\) gives the displayed minimum-length histogram and witnesses; this is a finite exhaustive proof of the all-length result, not a finite-length experiment. The machine-checkable `certificate_70_types.json` records all \(70\) distinct signatures and one shortest word for each, and `finite_state_output.txt` gives the counts produced by the complete closure.

**Step 4: a direct lower bound for the sharp case.** Consider the word `0011001100`. Its complete pointed profile set, writing colour sets as digit strings, is exactly
\[
\{(0,\{0\},\{0,1\}),\;(0,\{0,1\},\{0,1\}),\;(1,\{0,1\},\{0,1\})\}.
\]
Any word with this profile set has each 1-vertex adjacent to both colours; hence all 1-runs have exactly two vertices and lie strictly inside the path. Every 1-vertex has a nonadjacent 1-vertex, so there must be at least two different 1-runs. Every 0-vertex has a 0-neighbour, so each 0-run, including the two endpoint runs and the separating run, has at least two vertices. Thus at least two 1-runs and three 0-runs of size two are forced, giving at least \(2\cdot2+3\cdot2=10\) vertices. The exhibited ten-letter word attains this. Interchanging the named colours yields the other extremal profile. The complete closure establishes that there are no further length-ten-minimal profiles.

## Verification
Run `python3 enumerate_profiles.py --write-certificate certificate_70_types.json` and `python3 verify_direct.py` in the directory containing the supplied files. The first program performs all-state closure and verifies each numerical assertion by program assertions. The second, structurally separate implementation computes the complete set of realized quantifier-free two-point atomic diagrams at each vertex, then the set of these pointed profile sets, for all \(32{,}766\) binary words of lengths one through fourteen. It reproduces all \(70\) signatures and their minimum lengths without using window states. The second computation is finite corroboration; the all-length quantification is established by the transition closure and Step 1.

## Relationship to prior work
Brown and Hoshino (2007) solve the Ehrenfeucht–Fraïssé game for **uncoloured** undirected paths and cycles at every quantifier depth; in particular, their uncoloured path threshold at depth two is four vertices. The two named vertex colours introduce new pointed profiles and increase the optimal rank-two representative bound to ten. The older paper does not classify these colour profiles or compute this spectrum.

Weis and Immerman (2009) describe quantifier-depth-bounded two-variable logic on words with **linear order** and, separately, an oriented successor relation; neither relation is present in this undirected adjacency-only problem. Related published results on directed paths in the successor-only language and on one-red linearly ordered words, together with calculations on binary words with order and successor, have different signatures and do not give the present unordered-path quotient or its sharp minimum representative length. Mwesigye and Truss (2010) show that arbitrary two-coloured **linear orders** admit rank-two representatives of length at most \(8\), using left/right colour-set characters. Their result is not the present undirected-neighbourhood theory: neither adjacency nor an unoriented path is quantifier-free definable from the order in their signature, and their optimal length is different. The general two-round game/pointed-profile principle is standard and is not claimed as original; the contribution is this exact family-specific quotient and sharp all-size bound.

## Limitations
The classification is relative to vertex-coloured paths and **does not** identify all binary-coloured graphs, arbitrary unions of paths, cycles, or structures with order, directed successor, constants, or counting quantifiers. Code verifies a finite transition system derived by proof, rather than certifying the logical reduction independently. An unlocated specialized treatment of coloured paths could imply the exact figures, so publication priority is not guaranteed; independent review has not been performed.

## References
1. Jason Brown and Richard Hoshino, *The Ehrenfeucht-Fraïssé Game for Paths and Cycles*, Ars Combinatoria 83 (2007), 193–212, published 2007-04-30. https://combinatorialpress.com/article/ars/Volume%20083/volume-83-paper-13.pdf
2. Philipp Weis and Neil Immerman, *Structure Theorem and Strict Alternation Hierarchy for FO² on Words*, Logical Methods in Computer Science 5 (2009), 1–23. https://lmcs.episciences.org/1159/pdf
3. *Exact quantifier-rank threshold for finite directed paths*, published research result (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-quantifier-rank-threshold-for-finite-directed-paths--75a6b05e7112
4. *Exact quantifier-rank profiles for finite one-red linear orders*, published research result (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-quantifier-rank-profiles-for-finite-one-red-linear-orders--eec9053b6af5
5. Feresiano Mwesigye and John K. Truss, *Classification of Finite Coloured Linear Orderings*, *Order* 28 (2011), 387–397, published online 2010-09-07. https://ir.must.ac.ug/bitstreams/ce8f9fc1-8064-4e56-b7ae-a30dd6b401c0/download
