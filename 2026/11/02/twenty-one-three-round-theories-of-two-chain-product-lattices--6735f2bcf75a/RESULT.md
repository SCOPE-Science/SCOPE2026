# Twenty-one three-round theories of two-chain product lattices

## Finding
Let \(C_s=\{0,1,\ldots,s-1\}\) be the chain of size \(s\), for each positive integer \(s\). Define the **rectangular grid poset** \(P_{m,n}=C_m\times C_n\), with its sole nonlogical relation
\[
(i,j)\preceq (i',j')\quad\Longleftrightarrow\quad i\le i'\ \text{and}\ j\le j'.
\]
Only the order relation and equality are named; neither coordinate projection is named. For a parameter pair write \(a=\min(m,n)\), \(b=\max(m,n)\), and define the following canonical representative \(\kappa(a,b)\):
\[
\kappa(a,b)=
\begin{cases}
(1,\min(b,7)),&a=1;\\
(a,\min(b,6)),&a\in\{2,3,4\};\\
(5,5),&a=b=5;\\
(5,6),&\text{otherwise}.
\end{cases}
\]
For all positive integers \(m,n,p,q\), the following equivalence is exact:
\[
\boxed{P_{m,n}\equiv_3 P_{p,q}\quad\Longleftrightarrow\quad
\kappa(\min(m,n),\max(m,n))=\kappa(\min(p,q),\max(p,q)).}
\]
Here \(\equiv_3\) denotes agreement on all ordinary first-order sentences of quantifier rank at most three in the **pure order language**, without counting. There are exactly **21 distinct theories**. Every class has a representative with at most \(30\) elements, and \(30\) is the smallest possible uniform bound, attained by the class of \(P_{5,6}\).

## Assumptions and scope
The two chain lengths are positive and finite. Each \(P_{m,n}\) is a finite distributive lattice, equivalently the lattice of order ideals of a disjoint union of two finite chains (with the harmless adjustment that the chain of join-irreducibles has one fewer element in each factor). Its elements are ordered coordinatewise. The result concerns a **single binary reflexive order predicate**, not two named coordinate orders, not a strict-simultaneous-dominance relation, and not graph adjacency.

## Proof
**Step 1: a uniform finite reduction.** For any integer \(t\ge7\), the finite linear orders \(C_t\) and \(C_7\) agree through quantifier rank three. The standard three-move strategy preserves, after each move with \(r\) moves remaining, each gap between consecutive selected elements and the two outside gaps either exactly when its size is below \(2^r-1\), or jointly at least \(2^r-1\). Initially both chains have size at least \(2^3-1=7\). On the next move, if a new element leaves a small gap on one side, choose an element leaving an equal gap on that side; otherwise choose one leaving both resulting gaps large enough. The elementary inequality \(2^{r+1}-1=2(2^r-1)+1\) makes this possible. Selected equality and relative order are maintained through all three moves.

The product of two pairs of structures that each admit a three-move back-and-forth strategy also admits one for the coordinatewise product of linear orders: apply the two strategies independently to the two coordinates of every selected point. At the end, coordinatewise comparisons and equality of selected ordered pairs are preserved. Consequently,
\[
P_{m,n}\equiv_3 P_{\min(m,7),\min(n,7)}.
\]
Interchanging the two coordinates is an isomorphism. Thus the entire infinite problem reduces to the \(28\) finite rectangles \(P_{a,b}\) with \(1\le a\le b\le7\).

**Step 2: an exact finite logical-type recurrence.** Given any nonempty finite poset \(P\), let \(\rho(x,y)\) be exactly one of the four relations \(=\), \(<\), \(>\), or \(\parallel\), where the last denotes incomparability. Define
\[
\begin{aligned}
T_0(x,y,z)&=(\rho(x,y),\rho(x,z),\rho(y,z)),\\
T_1(x,y)&=\{T_0(x,y,z):z\in P\},\\
T_2(x)&=\{T_1(x,y):y\in P\},\\
T_3(P)&=\{T_2(x):x\in P\}.
\end{aligned}
\]
These are finite nested sets, compared by exact equality. Two nonempty posets have the same \(T_3\) if and only if Duplicator wins the three-move Ehrenfeucht–Fraïssé game. Indeed, after two moves equality of the \(T_1\) sets exactly says that every possible third-move atomic triple in either poset can be matched in the other. Inducting backward, equality of the \(T_2\) sets is exactly the condition for both directions of the second move, and equality of the \(T_3\) sets is exactly the first-move condition. Every comparison also records equality, so repeating a selection is handled without exceptions. Standard game semantics therefore equates this condition with \(\equiv_3\).

**Step 3: exhaustive finite classification.** The standalone programs `verify_grids.py` and `verify_game.py` construct all \(28\) reduced posets, evaluate the preceding recurrence using independent encodings (six order bits and four-valued comparisons), and compare their exact finite nested sets. Both return **21** classes and the identical grouping:

- One row of seven singleton classes represented by \(P_{1,1},P_{1,2},\ldots,P_{1,7}\).
- Five classes represented by \(P_{2,2},P_{2,3},P_{2,4},P_{2,5},P_{2,6}\), with \(P_{2,7}\) in the last.
- Four classes represented by \(P_{3,3},P_{3,4},P_{3,5},P_{3,6}\), with \(P_{3,7}\) in the last.
- Three classes represented by \(P_{4,4},P_{4,5},P_{4,6}\), with \(P_{4,7}\) in the last.
- The singleton class of \(P_{5,5}\), and the class represented by \(P_{5,6}\), which additionally contains \(P_{5,7},P_{6,6},P_{6,7},P_{7,7}\) within the reduced domain.

This is a **complete finite certificate**, not a sample: every normalized parameter pair occurs. Step 1 therefore extends the result to all positive parameters. Since all \(21\) signatures differ, no two representative classes can be merged. The largest smallest representative is \(P_{5,6}\), on \(5\cdot6=30\) points, proving sharpness.

## Verification
Use an ordinary Python 3 interpreter from the directory containing these files:

```sh
python3 verify_grids.py
python3 verify_game.py
```

The full outputs are embedded as `verify_grids.out` and `verify_game.out`. Both programs are deterministic, have no external dependencies, and compare finite logical types by exact set equality rather than hashes or probabilistic tests. The first checks all \(28\) rectangles through side length seven, including the \(21\) pairwise-distinct representatives, and also performs larger direct checks. The second independently reconstructs the complete exact three-round game signatures. The infinite reduction in Step 1 is essential: these finite runs alone do not prove the unbounded statement.

## Relationship to prior work
Mwesigye and Truss (2010/2011) analyze Ehrenfeucht–Fraïssé equivalence of finite coloured linear orders, including the sharp monochromatic chain cutoff \(2^r-1\). This supplies the one-dimensional antecedent to Step 1, not the sharp classification of unlabelled two-coordinate products. Sankaran, Adsul and Chakraborty (2014) prove preservation properties for product constructions and state that bounded-rank equivalence passes to tensor products. Sankaran (2016) explicitly treats finite-dimensional grid posets via equivalent bounded substructure properties. These results imply qualitative bounded-representative phenomena and a direct \(7\times7\) upper bound at rank three, but they do not give the **21** rank-three classes or the sharp **30**-element representative bound in the inspected relevant sections.

A related strict-simultaneous-dominance relation requires both coordinates to grow strictly. It is not the reflexive product order considered here: for example, pairs sharing one coordinate can be comparable in this lattice but never under strict simultaneous dominance. Its previously reported rank-three classification therefore does not imply the present one. The present statement gives a complete exact classification for a distinct canonical lattice signature.

## Limitations
No claim is made about quantifier rank four or greater, about fixed-point counting logic, or about formulas that name the two coordinate projections. The finite computation is exhaustive only after the proven reduction to side lengths at most seven. The priority comparison is evidence-based but not an exhaustive search of every historical paper, and independent mathematical validation has not been performed.

## References
1. F. Mwesigye and J. K. Truss, *Classification of Finite Coloured Linear Orderings*, **Order** 28 (2011), 387–397; first online 2010-09-07. DOI: 10.1007/s11083-010-9178-9. Full text: https://ir.must.ac.ug/bitstreams/ce8f9fc1-8064-4e56-b7ae-a30dd6b401c0/download.
2. A. Sankaran, B. Adsul and S. Chakraborty, *A Generalization of the Łoś–Tarski Preservation Theorem over Classes of Finite Structures* (2014), arXiv:1401.5953. https://arxiv.org/abs/1401.5953.
3. A. Sankaran, *A Generalization of the Łoś–Tarski Preservation Theorem* (2016), arXiv:1609.06297, especially Chapters 10–11. https://arxiv.org/abs/1609.06297.
