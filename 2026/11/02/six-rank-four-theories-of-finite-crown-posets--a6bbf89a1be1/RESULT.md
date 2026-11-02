# Six rank-four theories of finite crown posets

## Finding
For every integer \(n\ge 2\), form the height-two crown poset \(X_n\) with elements \(a_i,b_i\), indexed by \(i\in\mathbb Z/n\mathbb Z\), and strict comparisons \(a_i<b_i\) and \(a_i<b_{i-1}\), with no others. In first-order logic with equality and this one binary strict-order predicate, the complete quantifier-rank-four equivalence classification is
\[
X_m\equiv_4X_n\quad\Longleftrightarrow\quad
\bigl(m=n\in\{2,3,4,5,6\}\bigr)\ \lor\ \bigl(m,n\ge7\bigr).
\]
Thus precisely six rank-four theories occur; their smallest representatives have \(4,6,8,10,12,14\) vertices. The sharp smallest representative of the eventual theory is the fourteen-point crown \(X_7\). In particular \(X_6\not\equiv_4 X_7\), although their undirected Hasse graphs, the 12- and 14-cycles, are rank-four equivalent as pure graphs by Brown--Hoshino [1, Theorem 4.1].

## Assumptions and scope
Every \(X_n\) is finite, with \(n\ge2\). The signature has only equality and a binary strict comparison \(<\); neither a cycle orientation nor a lower/upper-level unary color is in the signature. \(X_2\) is the four-point crown. The notation \(X_m\equiv_rX_n\) means agreement on all first-order sentences whose nested quantifier depth is at most \(r\). The nonstrict specialization order is quantifier-free interdefinable with this strict order by adjoining equality.

## Proof
**1. Uniform infinite tail from a stronger cyclic expansion.** Arrange the \(2n\) elements around the directed cycle
\[
a_0,b_0,a_1,b_1,\ldots,a_{n-1},b_{n-1},a_0.
\]
Give the directed cycle its successor relation \(S\) and a unary predicate \(A\) selecting the \(a_i\)'s. The crown order is quantifier-free definable by
\[
x<y\iff A(x)\wedge\neg A(y)\wedge\bigl(S(x,y)\lor S(y,x)\bigr).
\]
We prove the stronger statement that any two alternatingly colored directed cycles of even lengths at least 24 are equivalent for four Ehrenfeucht--Fraisse rounds.

Take \(L_0=2\) and \(L_{r+1}=2L_r+1\), so \(L_1=5\), \(L_2=11\), and \(L_3=23\). After pebbles have been placed, preserve their cyclic ordering, their colors, and the following invariant for each corresponding clockwise gap of edge-lengths \(d,e\), with \(r\) moves still available: either \(d=e<L_r\), or \(d,e\ge L_r\) and \(d\equiv e\pmod2\). Equal colors of the corresponding gap endpoints imply the parity condition.

For an old selected vertex, answer with its partner. When a new vertex splits a short corresponding gap, use the identical clockwise offset. When it splits a long gap \(d\) as \(d=u+v\), put \(T=L_{r-1}\). If \(u<T\), choose the same first segment \(u\); then the other segments on both cycles are at least \(T\). If \(v<T\), use the same last segment. These cases cannot overlap because \(d\ge2T+1\). Otherwise \(u,v\ge T\); since the target gap has length at least \(2T+1\), choose its first new subgap to have length \(T\) or \(T+1\), whichever has the parity of \(u\). Its remaining length is also at least \(T\). In all cases both new gaps satisfy the next invariant and the new vertex has the required alternating color. The strategy is symmetric between the two cycles.

On the first move choose any vertex of the same color. Thereafter a single gap spans the whole cycle. For every \(n\ge12\), its length \(2n\ge24>L_3\), and the two lengths have matching even parity. Apply the invariant for three further moves. With no moves left, \(L_0=2\) exactly preserves clockwise successor edges between pebbled vertices (gaps of length one), as well as equality and unary colors. Hence the directed colored cycles, and therefore the crown posets, agree at rank four for all \(n\ge12\).

**2. Exact finite boundary.** For a finite structure \(M\) and a tuple \(\bar x\), let \(T_0^M(\bar x)\) be its complete atomic equality-and-comparison diagram. Recursively set
\[
T_{j+1}^M(\bar x)=\{T_j^M(\bar x,y):y\in M\}.
\]
The types are literal nested finite sets, with a common canonical interning scheme across every structure; multiplicity is intentionally discarded. Standard backward induction in the Ehrenfeucht--Fraisse game proves that two tuples have equal \(T_j\) exactly when Duplicator wins the remaining \(j\) moves from those tuples. Thus comparing \(T_4^{X_n}(())\) is an exact decision procedure, not a heuristic or an approximation.

Both attached implementations compute every required atomic extension, one by using cyclic rotations to fix the first selected vertex and one by unrestricted enumeration of all ordered triples. For \(n=2,3,4,5,6,7,8,9,10,11,12\) their globally interned root-type indices are respectively \(0,1,2,3,4,5,5,5,5,5,5\). The independent programs additionally agree through \(n=15\). Therefore all sizes below seven have distinct rank-four types from one another and from size seven, while sizes seven through twelve have the same type. Combining this finite boundary with the infinite-tail argument proves the claimed classification.

## Verification
Run `sh reproduce.sh` beside `verify_types.cpp` and `verify_types.py`. The script compiles C++17, executes both independent recursions for every \(n\) from 2 to 15, compares their complete root-type partitions, and checks the six-class pattern. Recorded output is in `verification_output.txt`. The C++ verifier exploits only the automorphism \(a_i\mapsto a_{i+k}, b_i\mapsto b_{i+k}\); the Python verifier explicitly generates all ordered triples without quotienting by automorphisms. Each verifier derives types from actual adjacency/equality rather than relying on previously recorded counts.

The finite census alone would not prove the infinite tail; that implication comes solely from the gap strategy above. Conversely, the gap strategy begins at \(n=12\) and does not prove the sharp cutoff seven without the exact finite calculation.

## Relationship to prior work
Brown and Hoshino [1, Theorem 4.1] prove that pure undirected cycles of lengths at least eleven have the same rank-four theory. They do not treat the strict comparison relation of crown posets or the alternating bipartition as logical data. Indeed their result says that the Hasse graphs of \(X_6\) and \(X_7\) are rank-four equivalent, whereas this classification separates the posets at rank four. The cyclic comparison poset is a classical finite model of the topological circle; Stong [2] is an early general reference for finite topological spaces. The new statement is a sharp bounded-quantifier classification, not a homotopy or mapping-space result. Accessible contemporary records on crown configuration spaces concern different invariants and do not give the present six-class theorem.

## Limitations
The theorem concerns only single crown posets and first-order quantifier rank four. It does not classify arbitrary height-two posets, disconnected unions of crowns, formulas with extra named colors or successor symbols, or higher quantifier ranks. The originality search is necessarily nonexhaustive; an equivalent older classification under different terminology could remain undiscovered. Numerical type indices depend on traversal order and have no invariant meaning except equality of indices within one execution; the mathematical invariant is the recursively defined type itself. Independent mathematical audit has not been carried out.

## References
[1] Jason Brown and Richard Hoshino, "The Ehrenfeucht--Fraisse Game for Paths and Cycles," *Ars Combinatoria* **83** (2007), 193--212, especially Theorems 4.1 and 4.8. Public date recorded as 2007-04-30. https://combinatorialpress.com/article/ars/Volume%20083/volume-83-paper-13.pdf

[2] R. E. Stong, "Finite topological spaces," *Transactions of the American Mathematical Society* **123** (1966), 325--340. https://doi.org/10.1090/S0002-9947-1966-0195042-2
