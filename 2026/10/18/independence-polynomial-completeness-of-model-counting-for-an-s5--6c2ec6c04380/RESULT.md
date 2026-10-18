# Independence-polynomial completeness of model counting for an S5 co-occurrence fragment

## Finding

**Theorem (exact spectrum, inverse classification, restricted counting complexity, and first collision).** Fix an integer \(k\geq1\), put \(q=2^k\), and label the \(q\) complete Boolean types in \(k\) propositional atoms by \(V_q=\{0,\ldots,q-1\}\). For each \(a\in V_q\), let \(\tau_a\) be the conjunction fixing every atom to its truth value in \(a\). Given any simple undirected graph \(G=(V_q,E)\), define the depth-one S5 formula

\[
\Phi_G=\bigvee_{\{a,b\}\in E}(\Diamond\tau_a\wedge\Diamond\tau_b),
\]

with the empty disjunction interpreted as false. On the *fixed complete* S5 frame with \(n\geq1\) **labelled** worlds, assign each propositional atom independently and uniformly at every world. Let \(M_G(n)\) be the number of the \(q^n\) valuations making \(\Phi_G\) true (equivalently, at every world), and let \(i_j(G)\) be the number of independent sets of cardinality \(j\) in \(G\).

1. **Exact transform.** With \(\left\{\begin{smallmatrix}n\\j\end{smallmatrix}\right\}\) the Stirling number of the second kind,

   \[
   M_G(n)=q^n-\sum_{j=1}^{\min(n,q)}i_j(G)\,j!\left\{\begin{matrix}n\\j\end{matrix}\right\}.
   \]

2. **Exact inverse.** The first \(q\) counts \(M_G(1),\ldots,M_G(q)\) determine the entire independence polynomial \(I_G(z)=\sum_{j=0}^q i_j(G)z^j\). Hence two formulas in this fragment have identical model counts for *every* positive world count exactly when their defining graphs have the same independence polynomial. This equivalence is about quantitative spectra, not equivalence of S5 formulas.

3. **Restricted complexity.** The function that inputs a formula in this co-occurrence fragment together with a positive world count written in unary and outputs \(M_G(n)\) is \(\#\mathrm P\)-complete under polynomial-time Turing reductions. No claim of parsimonious or many-one completeness is made.

4. **Noninjectivity already on two atoms.** For \(q=4\), take \(G_1\) to be the path with edges \(\{01,12,23\}\), and \(G_2\) to be a triangle on \(\{0,1,2\}\) plus isolated vertex \(3\), with edges \(\{01,02,12\}\). They are nonisomorphic, both have \(I(z)=1+4z+3z^2\), and for every \(n\geq1\)

   \[
   M_{G_1}(n)=M_{G_2}(n)=4^n-3\cdot2^n+2.
   \]

   The two formulas are *not* S5-equivalent: the model with two worlds of types \(0\) and \(2\) satisfies only the second formula. No distinct independence-polynomial-equivalent graphs exist on at most three vertices, so two propositional atoms are minimal for this graph-encoding obstruction.

As a sharp-rate consequence, for any graph \(G\) with at least one edge and independence number \(\alpha\), the failure probability has the asymptotic form
\[
1-\frac{M_G(n)}{q^n}\sim i_{\alpha}(G)\left(\frac{\alpha}{q}\right)^n.
\]
The coefficient counts maximum independent sets and \(\alpha<q\), so these formulas become almost surely true at an exact exponential rate.

## Assumptions and scope

There is exactly **one complete S5 accessibility class** with \(n\) distinguishable worlds and all worlds access all worlds. This is not a uniform distribution over all S5 equivalence frames or unlabelled isomorphism classes. Every assignment to \(k\) atoms at each world is counted once. The defining graph has all \(q\) Boolean types as vertices, including isolates. Formulae are constructed as displayed and use no nested modalities. The complexity input encodes \(n\) in unary and the displayed finite syntax explicitly. The output integer has polynomial bit length relative to that input. For asymptotics the graph and \(k\) are fixed as \(n\to\infty\).

## Proof

**Truth-support lemma.** For each valuation \(v:[n]\to V_q\), let \(S=v([n])\). In the universal accessibility relation, \(\Diamond\tau_a\) holds exactly when \(a\in S\); this truth value is the same at every world. Thus \(\Phi_G\) is false exactly when \(S\) is an independent vertex set of \(G\). This proves the exact semantic correspondence without identifying a graph-theoretic ``conflict graph'' constructed from a general formula.

**Exact counts.** There are \(i_j(G)\) possible independent image sets of size \(j\). The number of functions \([n]\to S\) *onto* one fixed \(j\)-set is \(j!\left\{\begin{smallmatrix}n\\j\end{smallmatrix}\right\}\). These categories are disjoint because every function has one image. Subtracting their sum from \(q^n\) gives (1). For \(n\ge1\), the empty image contributes zero. In particular \(i_0(G)=1\) but no \(j=0\) term is needed in the displayed formula.

**Inversion.** Put \(N_G(n)=q^n-M_G(n)\). Since \(j!\left\{\begin{smallmatrix}n\\j\end{smallmatrix}\right\}=0\) for \(j>n\), and its diagonal entry at \(j=n\) equals \(n!\), the integer recurrence
\[
i_0=1,\qquad i_n=\frac{N_G(n)-\sum_{j=1}^{n-1}i_j\,j!\left\{\begin{smallmatrix}n\\j\end{smallmatrix}\right\}}{n!}\quad(1\le n\le q)
\]
recovers every coefficient. The transform is injective on coefficient sequences. Thus equality for the first \(q\) counts is equivalent to equality of independence polynomials, and implies equality for all \(n\ge1\).

**Restricted counting complexity.** Membership in \(\#\mathrm P\) follows by guessing the \(nk\) truth bits and evaluating \(\Phi_G\) on the resulting labelled complete frame in polynomial time. For hardness, start from an arbitrary \(r\)-vertex graph \(H\), where the number of independent sets is \(\#\mathrm P\)-complete to compute. Pad it by \(q-r\) isolated vertices to obtain \(G\), where \(q=2^{\lceil\log_2r\rceil}\le2r\) for \(r\ge1\); take \(k=\log_2q\), using \(q=2\) when \(r=1\). Construct \(\Phi_G\) explicitly in polynomial time; its length is \(O(qk+|E|k)\). Query the exact counting oracle for \(n=1,\ldots,q\) (each \(n\) unary), use the displayed triangular inverse, and compute \(I_G(1)\). Since \(I_G(z)=(1+z)^{q-r}I_H(z)\), the answer is \(I_H(1)=I_G(1)/2^{q-r}\). This is a polynomial-time Turing reduction: integer sizes are polynomially bounded in bits. The case \(r=1\) is trivial and does not affect hardness. Consequently the restricted function is \(\#\mathrm P\)-complete under this explicitly stated reduction type. General S5 model counting is already trivially \(\#\mathrm P\)-hard via single-world propositional counting; **only the severe modal fragment restriction is at issue here**.

**First collision.** Both exhibited four-vertex graphs have exactly four independent singleton sets, three independent pairs, and no larger independent set. The path has degree multiset \(\{1,1,2,2\}\), whereas the triangle-plus-isolate has \(\{0,2,2,2\}\), so they are not isomorphic. The exact transform gives \(N_G(n)=4+3(2^n-2)=3\cdot2^n-2\). A two-world support equal to \(\{0,2\}\) contains an edge of the triangle but not of the path, proving logical inequivalence. For graphs of order one, two, or three, the graph classes are distinguished by the independent-set numbers (at order three: the four possibilities have coefficient vectors \((1,3,3,1)\), \((1,3,2,0)\), \((1,3,1,0)\), and \((1,3,0,0)\)); thus four vertices is the smallest graph order yielding this particular type of collision.

**Rate.** Write \(\alpha=\alpha(G)\). The count of onto maps to an \(\alpha\)-element set satisfies \(\alpha!\left\{\begin{smallmatrix}n\\\alpha\end{smallmatrix}\right\}=\alpha^n+O((\alpha-1)^n)\) for fixed \(\alpha\ge2\), by inclusion–exclusion; for \(\alpha=1\) it is exactly one. Contributions from smaller independent sets are \(O((\alpha-1)^n)\). Hence \(N_G(n)=i_\alpha\alpha^n+o(\alpha^n)\), giving the stated asymptotic. Since \(G\) has an edge, \(\alpha<q\).

## Verification

The companion `verify_modal.py` is a Python-3 standard-library program. Running `python verify_modal.py` independently builds graph independent-set coefficients, evaluates the displayed Stirling transform and its triangular inverse, and enumerates all labelled complete-frame assignments to test the original S5 co-occurrence truth condition. It covers all simple graphs on \(2\) and \(4\) labelled vertices, sixteen fixed-seed graphs on \(8\) vertices, and the explicit collision for world counts up to eight; it also checks absence of distinct polynomial-equivalent isomorphism types on one, two and three vertices. The successful run returned:

`VERIFY_OK graphs=82 complete_frame_valuations=162300 inversion=PASS min_collision=4 path_triangle_isolate=PASS`

The finite checks are not used as a proof of the infinite-family transform, the complexity reduction, or the asymptotic statement. Those statements are proved above.

## Relationship to prior work

The complete-accessibility semantics and modal S5 normal-form context are standard and directly described in Alviano–Batsakis–Baryannis (2021) and Huang et al. (2019). The graph in Huang et al. is a **diamond-conflict graph of clauses** used to bound model size for SAT solving; it is not the present graph on all Boolean valuations whose independent sets count *every* full-frame assignment. The established graph independence polynomial counts independent vertex subsets. Its failure to distinguish nonisomorphic graphs (including a four-vertex example) is known; neither the collision of graph polynomials nor the concept of \(\#\mathrm P\)-hardness of independent-set counting is claimed to be new. Verbrugge (2021), citing Halpern–Kapron, explains established modal zero–one laws, but the present result concerns an exact finite-size transform and an invertible classification of spectra on one fixed complete frame, not an original zero–one law. The assessed contribution is the precise restricted-fragment counting equivalence, the inverse spectrum classification, its specified Turing-hardness, and their logical implications. No claim about the first-ever publication of these consequences is made without independent bibliographic review.

## Limitations

The theorem does not describe model counts for arbitrary S5 formulas, all equivalence-frame distributions, nonuniform valuations, or unlabelled Kripke models. The model-count spectrum determines the independence polynomial, **not** the graph or logical equivalence class. The four-vertex graph-polynomial collision is an established graph-theoretic fact and is used as evidence rather than presented as a new graph theorem. The hardness classification uses polynomial-time **Turing** reductions, not a parsimonious many-one reduction. Full priority search across all possible prior modal model-counting terminology has not been independently completed.

## References

1. M. Alviano, S. Batsakis, G. Baryannis, *Modal Logic S5 Satisfiability in Answer Set Programming*, arXiv:2108.04194, first public 2021-08-09, https://arxiv.org/abs/2108.04194 . The accessible complete text, notably Sections 2–5, was inspected.
2. P. Huang, M. Liu, P. Wang, W. Zhang, F. Ma, J. Zhang, *Solving the Satisfiability Problem of Modal Logic S5 Guided by Graph Coloring*, IJCAI 2019, pp. 1093–1100, https://www.ijcai.org/proceedings/2019/0153.pdf . In particular, Section 5 defines a diamond-conflict graph with clauses as vertices.
3. R. Verbrugge, *Zero-one laws for provability logic: Axiomatizing validity in almost all models and almost all frames*, arXiv:2102.05947 (2021), https://arxiv.org/abs/2102.05947 . The introductory survey treats known S5 zero–one laws.
4. E. W. Weisstein, *Independence Polynomial*, MathWorld, https://mathworld.wolfram.com/IndependencePolynomial.html . Standard definition and catalogued four-vertex polynomial collisions.
5. J. S. Provan and M. O. Ball, *The Complexity of Counting Cuts and of Computing the Probability that a Graph is Connected*, SIAM J. Comput. 12 (1983), 777–788, DOI:10.1137/0212053. Counting vertex covers of bipartite graphs is established \(\#\mathrm P\)-complete; complementation identifies vertex covers with independent sets.
