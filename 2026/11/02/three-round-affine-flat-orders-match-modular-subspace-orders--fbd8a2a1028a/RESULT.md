# Three-round affine-flat orders match modular subspace orders

## Finding

Let \(F,K\) be arbitrary fields. For every integer \(d\ge1\), let \(\mathcal A_d(F)\) denote the inclusion poset of all affine subspaces of \(F^d\), **including the empty set**. Let \(\mathcal L_n(K)\) denote the inclusion poset of all linear subspaces of \(K^n\), including zero and the whole space. The language consists solely of equality and inclusion, with no constants, rank predicates, field symbols, or counting quantifiers. Write \(\equiv_3\) for agreement on every first-order sentence of quantifier rank at most three.

**Theorem.** For all fields \(F,K\) and every integer \(d\ge2\),
\[
\mathcal A_d(F)\equiv_3\mathcal L_{d+1}(K).
\]
The same equivalence holds when \(d=1\) and \(|F|\ge3\). Among all affine-flat inclusion posets \(\mathcal A_d(F)\), exactly **six** rank-three theories occur: \(d=1\) with \(|F|=2\); \(d=1\) with \(|F|\ge3\); dimensions \(d=2,3,4\) separately; and the single class consisting of **every \(d\ge5\)** over every field. The least finite member of the stable class has \(2452\) elements, namely \(\mathcal A_5(\mathbb F_2)\), and this bound is sharp within the class.

The cross-family equivalence is structurally meaningful: for \(d\ge2\), the affine-flat poset fails modularity whereas every linear-subspace lattice is modular. Thus even rank-three order logic cannot recognize this lattice-theoretic distinction.

## Assumptions and scope

The fields may be finite or infinite and need not have equal characteristic. The affine space has **positive finite dimension**. Empty affine subspace has rank zero, a nonempty affine \(k\)-flat has rank \(k+1\), and the full affine space has rank \(R=d+1\). For \(\mathcal L_R(K)\), rank means linear dimension; both kinds of structures have ranks \(0,\ldots,R\). The two-point affine line over \(\mathbb F_2\) is the sole exception to the common rank-only extension rule.

A first-order formula may reuse variables. Quantifier rank counts nesting, not the number of different variable names.

## Proof

**1. Atomic relationships and a complete pair-extension lemma.** For elements \(X,Y\), abbreviate \(E,L,G,I\) for equality, strict inclusion \(X\subsetneq Y\), strict reverse inclusion \(X\supsetneq Y\), and incomparability. Suppose \(r=\operatorname{rk}X\), \(s=\operatorname{rk}Y\), and \(c\) denotes the relation of \(X\) to \(Y\). Possible pair types are precisely: \(c=E\) if \(r=s\), \(c=L\) if \(r<s\), \(c=G\) if \(r>s\), and \(c=I\) if \(0<r,s<R\). (For \(E\), choose \(X=Y\); the other choices are available whenever their conditions hold.)

For each ordered pair, record which relation pairs \((\operatorname{rel}(Z,X),\operatorname{rel}(Z,Y))\) are realized as a third element \(Z\) varies. The following is the **entire** extension table, with a condition meaning that the displayed pair exists:

| Relations of \(Z\) to \((X,Y)\) | Necessary and sufficient condition |
| --- | --- |
| \((E,c)\), \((c^{\mathrm{op}},E)\) | Always; choose \(Z=X\) or \(Z=Y\). |
| \((L,L)\) | \(r,s>0\). |
| \((G,G)\) | \(r,s<R\). |
| \((G,L)\) | \(c=L\) and \(s-r\ge2\). |
| \((L,G)\) | \(c=G\) and \(r-s\ge2\). |
| \((L,I)\) | \(r\ge2\), \(s>0\), and \(c\in\{G,I\}\). |
| \((I,L)\) | \(s\ge2\), \(r>0\), and \(c\in\{L,I\}\). |
| \((G,I)\) | \(R-r\ge2\), \(s<R\), and \(c\in\{L,I\}\). |
| \((I,G)\) | \(R-s\ge2\), \(r<R\), and \(c\in\{G,I\}\). |
| \((I,I)\) | \(0<r,s<R\), except when the structure is \(\mathcal A_1(\mathbb F_2)\), \(r=s=1\), and \(c=I\). |

The displayed pairs not covered by these rows are impossible. For example, a third flat below both is the common bottom element whenever both are nonbottom; one above both is the common top whenever both are nontop. The strict-between row is exactly the existence of an intermediate rank. A proper flat below \(X\), incomparable with \(Y\), exists precisely in the \((L,I)\) case listed: choose a point of \(X\) not in \(Y\) when \(X\not\subseteq Y\); the rank condition excludes atoms, and \(s>0\) excludes the common bottom. For \((G,I)\), extend \(X\) one rank while avoiding containment of \(Y\); at codimension at least two, at least three distinct covers are available through an affine or linear point/line, so one avoids \(Y\). The remaining mixed cases are the symmetric arguments.

For \((I,I)\), whenever \(X,Y\) are proper nonbottom flats, a point outside \(X\cup Y\) is incomparable with both (and may be regarded as its rank-one flat). The only situation where two proper affine flats can cover the entire affine space is two parallel hyperplanes over \(\mathbb F_2\); when \(d\ge2\), a transverse affine line is incomparable with both. Two proper linear subspaces never cover their whole vector space. On a one-dimensional affine line with at least three points, a third point works; for the two-point affine line, it does not. This proves the exceptional clause. These constructions verify sufficiency, and the order constraints prove necessity.

**2. From extensions to three-round game types.** Let \(P_R(r,s,c)\) be the pair's atomic relation \(c\) together with its complete set of realized third-element patterns from the table. The two-round pointed type at an element of rank \(r\) is the finite set
\[
S_R(r)=\{P_R(r,s,c):0\le s\le R,\ c\text{ possible for ranks }r,s\}.
\]
The three-round type of the whole structure is the set of pointed types \(\{S_R(r):0\le r\le R\}\). This is the usual finite-round back-and-forth recursion: after one move, possible second moves are indexed by the pair types, and the third move tests precisely the realized atomic patterns. Repeated choices and equality are explicitly included in the table. Consequently equality of these finite type sets is **equivalent** to three-round Ehrenfeucht–Fraïssé equivalence.

For all \(R\ge3\), direct substitution of the ten table cases shows that \(S_R(r)\) depends **exactly** on the truncated rank/corank pair
\[
\bigl(\min(r,3),\min(R-r,3)\bigr).
\]
There are ten possible distinct pointed profiles, with their sizes as an independent compact check:

| Truncated rank/corank | Number of pair-extension types |
| --- | ---: |
| \((0,3)\), \((3,0)\) | 4 each |
| \((1,2)\), \((2,1)\) | 6 each |
| \((1,3)\), \((3,1)\) | 8 each |
| \((2,2)\) | 8 |
| \((2,3)\), \((3,2)\) | 9 each |
| \((3,3)\) | 10 |

Equal table sizes do not by themselves establish equality or distinction: the **actual sets of pair masks** are recorded in `symbolic_certificate.json`, and the formulas above determine them without reference to dimension bounds. All ten masks sets are pairwise distinct. For \(R\ge6\), the possible truncated rank/corank pairs are exactly seven of these ten entries: \((0,3),(1,3),(2,3),(3,3),(3,2),(3,1),(3,0)\), independent of \(R\). This proves all same-rank affine/linear equivalences for \(d\ge2\), and all stable-dimension equivalences. At \(R=2\), the third-point pattern alone separates the two-point affine line from every other affine line and from \(\mathcal L_2(K)\).

**3. Explicit rank-three separators and sharpness.** Define \(a<b\) to abbreviate \(a\subsetneq b\), and \(a\parallel b\) to abbreviate incomparability. For a free variable \(x\), define
\[
\begin{aligned}
L_2(x)&:=\exists y\exists z\,(z<y<x),\\
U_1(x)&:=\exists y\,(x<y),\\
U_2(x)&:=\exists y\exists z\,(x<y<z),\\
L_3(x)&:=\exists y\bigl(y<x\land\exists z(y<z<x)\land\exists z(z<x\land z\parallel y)\bigr),\\
U_3(x)&:=\exists y\bigl(x<y\land\exists z(x<z<y)\land\exists z(x<z\land z\parallel y)\bigr).
\end{aligned}
\]
Each formula has quantifier rank at most two with \(x\) free. The formulas respectively assert rank at least two, corank at least one, corank at least two, rank at least three, and corank at least three. For example, when rank is at least three, choose a rank-one \(y<x\), an intermediate rank-two \(z\), and a different rank-one \(z\) incomparable with \(y\); at smaller rank, one of the two branches necessarily fails. The dual reasoning establishes \(U_3\).

It follows that the rank-three sentences
\[
\begin{array}{c|c}
\exists x(L_2(x)\land U_1(x))&R\ge3\\
\exists x(L_2(x)\land U_2(x))&R\ge4\\
\exists x(L_3(x)\land U_2(x))&R\ge5\\
\exists x(L_3(x)\land U_3(x))&R\ge6
\end{array}
\]
have exactly the truth conditions indicated. Thus the rank classes \(R=2,3,4,5,\ge6\) are distinct. Within rank \(R=2\), the rank-three sentence asserting three pairwise incomparable elements distinguishes the two-point affine line from lines with at least three points. These give precisely six theories and prove that \(d=5\) is the first stable affine dimension.

For a finite field of order \(q\), the number of flats of affine \(d\)-space is
\[
1+\sum_{k=0}^{d}q^{d-k}{d\brack k}_q,
\]
where \({d\brack k}_q\) is the Gaussian binomial coefficient. For \(d=5,q=2\) this is \(2452\); larger dimensions or fields cannot yield fewer flats, proving the representative bound.

Finally, in an affine plane choose distinct parallel lines \(X,Y\). Their lattice ranks satisfy \(\operatorname{rk}X+\operatorname{rk}Y=4\), while their meet is empty of rank zero and their join is the full plane of rank three, violating modular rank equality. This nonmodularity embeds as an interval for every \(d\ge2\), while linear-subspace lattices are modular.

## Verification

Two standalone Python 3 programs provide corroboration. Execute `python3 symbolic_profiles.py` in the extracted directory to regenerate `symbolic_certificate.json` and print the rank profiles, then `python3 geometric_enumeration.py` to enumerate actual affine and linear subspace families over small prime fields and compute third-move patterns directly. `geometric_enumeration.out` records the observed results. The direct program does not call the symbolic-extension formulas; its computations include affine dimensions through six over the binary field and cross-family comparisons at dimensions two through five. The symbolic script checks the finite ten-case catalog and ranks through sixty; **the infinite theorem relies on the geometric extension lemma and the unbounded arithmetic case analysis, not on those finite tests**.

## Relationship to prior work

Izhakian and Rhodes [1] study Boolean representations of matroids and lattices of flats, including the relation between matroids and lattices; their inspected full text does not establish bounded first-order equivalence of affine and vector-subspace orders. Margolis, Rhodes, and Silva [2] characterize flat lattices in Boolean-representable complexes, but do not supply this affine-versus-modular logical comparison. Kuusisto, Meyers, and Virtema [3] study first-order theories of affine geometries in relational signatures involving betweenness; these are different from pure inclusion of flats. Bey [4] studies incidence matrices of finite affine flats; only the publisher abstract was accessible, and an exact logical comparison is not indicated there.

A prior classification of linear-subspace lattices at rank three establishes the *linear* six-dimensional cutoff, but it does **not** imply the new affine-to-linear transfer: affine-flat lattices are nonmodular and have different element counts and meet/join behaviour. A classification of uniform-matroid flat lattices likewise does not imply this result. An undiscovered general theorem about three-round types in semimodular lattices could subsume the present comparison; historical priority is therefore qualified rather than certified.

## Limitations

The theorem concerns finite **dimension** over arbitrary fields, but not infinite-dimensional affine spaces, richer signatures with joins/meets or named point predicates, counting logic, or quantifier rank four and higher. Its finite-field computations are checks, not independent formal verification. Full historical priority and independent mathematical review remain open.

## References

[1] Z. Izhakian and J. Rhodes, *Boolean Representations of Matroids and Lattices*, arXiv:1108.1473, first public August 6, 2011, https://arxiv.org/abs/1108.1473.

[2] S. Margolis, J. Rhodes, and P. V. Silva, *On the lattice of flats of a boolean representable simplicial complex*, arXiv:1510.05485, first public October 19, 2015, https://arxiv.org/abs/1510.05485.

[3] A. Kuusisto, M. Meyers, and J. Virtema, *Undecidable First-Order Theories of Affine Geometries*, arXiv:1208.4930, first public August 24, 2012, https://arxiv.org/abs/1208.4930.

[4] C. Bey, *On Incidence Matrices of Finite Affine Geometries*, *Ars Combinatoria* 47 (1997), publisher abstract accessed; full text not inspected.
