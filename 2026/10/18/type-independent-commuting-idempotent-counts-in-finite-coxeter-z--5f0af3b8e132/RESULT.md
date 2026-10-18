# Type-independent commuting-idempotent counts in finite Coxeter zero-Hecke monoids

## Finding
Let \((W,S)\) be a finite Coxeter system of rank \(n=|S|\), and let \(H_0(W)\) denote its **monoid** of Demazure products (not the set of idempotents in its semigroup algebra). For \(I\subseteq S\), write \(e_I\) for the zero-Hecke element indexed by the longest element of the finite parabolic subgroup \(W_I\), with \(e_\varnothing=1\). Let \(\Gamma\) be the unlabelled Coxeter diagram, placing an edge precisely when two distinct simple generators do not commute.

**Commutation criterion.** For all \(I,J\subseteq S\),
\[
e_Ie_J=e_Je_I\quad\Longleftrightarrow\quad
\text{each connected component }C\text{ of }\Gamma[I\cup J]\text{ satisfies }C\subseteq I\text{ or }C\subseteq J.
\tag{1}
\]
Consequently, the number of **ordered** commuting idempotent pairs in \(H_0(W)\) is
\[
F(\Gamma)=\sum_{K\subseteq S}\ \prod_{C\in\pi_0(\Gamma[K])}(2^{|C|+1}-1).
\tag{2}
\]
Here the empty product is \(1\). Edge labels \(m_{st}\ge3\) do not affect either (1) or (2).

**Coxeter-type invariance.** If \(W\) is irreducible and \(n\ge1\), then
\[
\boxed{F(\Gamma)=a_n,\quad a_0=1,\quad a_1=4,\quad a_n=4a_{n-1}-2a_{n-2}\ (n\ge2).}
\tag{3}
\]
Equivalently,
\[
\sum_{n\ge0}a_nz^n=\frac1{1-4z+2z^2},\qquad
 a_n=\frac{(2+\sqrt2)^{n+1}-(2-\sqrt2)^{n+1}}{2\sqrt2}.
\tag{4}
\]
Thus the ranks \(1,2,3,4,5,6\) give \(4,14,48,164,560,1912\), independently of whether the irreducible finite Coxeter type is \(A,B,C,D,E,F,G,H\), or \(I_2(m)\) when defined at that rank. For a reducible system with irreducible component ranks \(n_1,\dots,n_r\), the count is \(\prod_{j=1}^r a_{n_j}\).

More generally, the weighted graph partition function (2) equals \(a_n\) for **every tree on \(n\) vertices of maximum degree at most three**. The degree restriction is sharp for this graph statement: the five-vertex star has \(F(K_{1,4})=564\ne560=a_5\).

## Assumptions and scope
All Coxeter systems here are finite, including any finite crystallographic or noncrystallographic type. Rank is the number of canonical simple reflections, and disconnected diagrams are allowed. Every idempotent of \(H_0(W)\) is a unique \(e_I\), a standard parabolic-longest classification. An ordered pair \((e_I,e_J)\) and its reversal are counted separately unless identical. Formula (2) is defined combinatorially for all finite simple graphs, but its interpretation as an idempotent count is asserted only for finite Coxeter systems.

## Proof
**1. Necessity and sufficiency of (1).** The zero-Hecke multiplication is the Demazure product: scanning a word in simple generators from left to right, append the next reflection to the Coxeter-group element only if length increases. The resulting retained letters form a reduced expression. The support of a zero-Hecke product is the union of the supports of the factors. By the parabolic-longest classification, any commuting idempotents \(e_I,e_J\) have an idempotent product equal to \(e_K\), where \(K=I\cup J\).

Suppose a connected component \(C\) of \(\Gamma[K]\) contains both a vertex \(s\in J\setminus I\) and a vertex \(t\in I\setminus J\). Choose a simple path \(s=v_0,v_1,\ldots,v_d=t\) inside \(C\). Define a Coxeter element \(c\in W_K\) by listing these path vertices in the displayed order and then all remaining vertices of \(K\) in any order. Every reduced expression of this Coxeter element uses each simple generator exactly once, and all such expressions differ only by interchanging commuting adjacent generators (nontrivial braid moves need repeated letters). Hence \(s\) precedes \(t\) in **every** reduced expression for \(c\): the adjacent edges along the displayed path impose the precedence chain.

If \(e_Ie_J=e_K\), scan a concatenation of reduced expressions of the longest elements of \(W_I\) and \(W_J\). The retained letters give a reduced expression for the longest element of \(W_K\), consisting of a subword from the \(I\)-block followed by a subword from the \(J\)-block. Since every element of the finite parabolic \(W_K\), in particular \(c\), is Bruhat-below this longest element, the Bruhat subword property would give a reduced expression for \(c\) with every \(I\)-block letter preceding every \(J\)-block letter. But \(t\in I\setminus J\) would then precede \(s\in J\setminus I\), a contradiction. Therefore such a component cannot exist.

Conversely, suppose every connected component \(C\) of \(\Gamma[K]\) lies wholly in \(I\) or wholly in \(J\). Within a component contained in \(I\), \(e_{I\cap C}=e_C\) absorbs \(e_{J\cap C}\) on either side, since \(e_C\) absorbs every simple generator of \(C\); the same argument applies with \(I,J\) interchanged. Generators from distinct connected components commute. Therefore \(e_Ie_J=e_Je_I=e_K\), proving (1).

**2. Component partition formula.** Fix the union \(K=I\cup J\). For each component \(C\) of \(\Gamma[K]\), either all of \(C\) belongs to \(I\) and \(J\cap C\) is arbitrary, or all of \(C\) belongs to \(J\) and \(I\cap C\) is arbitrary. The intersection where both contain all of \(C\) is counted twice. Therefore there are exactly \(2^{|C|}+2^{|C|}-1=2^{|C|+1}-1\) assignments on \(C\). Components are independent, proving (2).

**3. Tree-shape invariance.** Interpret each vertex as carrying a state \(0\) (in neither subset), \(P\) (only in the first), \(Q\) (only in the second), or \(R\) (in both). Condition (1) says that no connected occupied component contains both a \(P\)-vertex and a \(Q\)-vertex. Root a tree. Let \(Z\) count admissible assignments with vacant root, \(R_0\) those where the occupied root component has only \(R\)-vertices, and \(P_0\) those where that component has at least one \(P\) and no \(Q\). By exchanging the first and second subsets, the analogous \(Q\)-count equals \(P_0\). Define
\[
t=Z+R_0+2P_0,\qquad u=Z+R_0,\qquad v=Z+R_0+P_0.
\]
Thus \(t=2v-u\). If the root has child subtrees with respective messages \((t_i,u_i,v_i)\), a direct disjoint-case count gives
\[
Z=\prod_i t_i,\quad R_0=\prod_i u_i,\quad
P_0=2\prod_i v_i-\prod_i u_i,
\]
and hence
\[
u=\prod_i t_i+\prod_i u_i,\quad
v=\prod_i t_i+2\prod_i v_i,\quad t=2v-u.
\tag{5}
\]
Empty products equal one; the single-vertex message is \((4,2,3)\). For the path message on \(n\) vertices write \((t_n,u_n,v_n)\), using the virtual empty message \((t_0,u_0,v_0)=(1,1,1)\). With one child, (5) becomes
\[
u_{n+1}=t_n+u_n=2v_n,\qquad
v_{n+1}=t_n+2v_n=4v_n-u_n.
\tag{6}
\]
The matrix of this recurrence has characteristic polynomial \(\lambda^2-4\lambda+2\). Therefore each of the three sequences obeys the second-order recurrence in (3), with \(t_0=1\) and \(t_1=4\).

For all \(a,b\ge0\), the following **branch-addition identities** hold:
\[
\begin{split}
u_{a+b+1}&=t_at_b+u_au_b,\\
v_{a+b+1}&=t_at_b+2v_av_b.
\end{split}
\tag{7}
\]
For fixed \(a\), both right sides satisfy the same second-order recurrence in \(b\), since each of \(t_b,u_b,v_b\) does. The cases \(b=0,1\) follow by substitution in (6) and \(t=2v-u\); this proves (7) for every \(b\) by induction.

Now root any nonempty tree of maximum degree at most three at a leaf. Every node has at most two children. A node with zero or one child obeys the path recurrence (6); a node with two child subtrees of sizes \(a,b\) has exactly the path message of size \(a+b+1\) by (5) and (7). Structural induction shows the root message depends only on total vertex number and equals \((t_n,u_n,v_n)\). Thus (2) equals \(t_n=a_n\) for every such tree. Formula (4) follows by solving the recurrence. If the tree is the star \(K_{1,4}\), conditioning on its center yields \(4^4+\sum_{j=0}^4\binom4j(2^{j+2}-1)=564\), whereas \(a_5=560\).

**4. Coxeter application.** By the classification of irreducible finite Coxeter diagrams, the underlying unlabelled diagram of each irreducible finite Coxeter system is a tree of maximum degree at most three. (All type \(A,B,C,F,G,H,I_2\) diagrams are paths; types \(D,E\) are subcubic branching trees.) The tree identity proves (3) for every irreducible system, independently of edge labels. A disconnected Coxeter diagram gives a direct product of the corresponding zero-Hecke monoids, and ordered commuting idempotent-pair counts multiply, proving the reducible assertion.

## Verification
The standalone `verify.py` enumerates all pairs of parabolic-longest idempotents in the ordinary permutation model for type \(A\), and in the signed-permutation root model for types \(B\) and \(D\). It compares direct Demazure multiplication with (1) and (3). It separately enumerates induced-component weights on every labelled tree of size at most six with maximum degree three, plus selected larger branchings, and performs direct four-state assignment checks. No probabilistic or infinite extrapolation is used in the proof. Run `python3 verify.py` from the same directory as this file.

## Relationship to prior work
Ganyushkin and Mazorchuk (2010, arXiv:1006.0316), Section 2, explicitly establish the \(\mathcal J\)-triviality and parabolic-longest idempotent classification of the simply-laced zero-Hecke monoids. Hivert, Schilling and Thiéry (2010, arXiv:1012.1361), Sections 1.1–1.2, give the general finite-Coxeter zero-Hecke/Demazure formalism and parabolic longest elements; their separate focus is the biHecke monoid and its representations. Those structural foundations are used, not claimed as new.

The type-\(A\) commuting-idempotent count and a quotient explanation through the Catalan monoid were already available, so neither the numerical sequence for type \(A\) nor its ordinary generating function alone constitutes the new claim. The same numerical sequence is OEIS A007070. The contribution assessed here is the **general Coxeter-diagram commutation criterion and the non-obvious tree-shape independence**, giving the same count for all finite irreducible Coxeter types—including the branching and exceptional types, not just type \(A\). Nearby connected-component partition functions, such as ordinary two-species Widom–Rowlinson counts, have different local component weights; they do not themselves yield the identity (2)–(3).

## Limitations
The result concerns **monoid** idempotents under Demazure multiplication, not arbitrary idempotents of the zero-Hecke algebra, and counts ordered pairs rather than commuting triples or centralizers of arbitrary elements. The tree universality requires maximum degree at most three and is not asserted for cyclic or degree-four graphs. The recurrence sequence is previously known numerically; novelty here concerns its mathematical interpretation and its independence of finite Coxeter type. Exhaustive bibliographic uniqueness is not established; an unlocated equivalent Coxeter-monoid or tree-partition-function identity could change the originality assessment. No independent mathematical audit has been performed.

## References
1. O. Ganyushkin and V. Mazorchuk, *On Kiselman quotients of 0-Hecke monoids*, arXiv:1006.0316v1 (first posted 2010-06-02), Section 2; https://arxiv.org/abs/1006.0316.
2. F. Hivert, A. Schilling and N. M. Thiéry, *The biHecke monoid of a finite Coxeter group and its representations*, arXiv:1012.1361v1 (first posted 2010-12-06), Sections 1.1–1.2; https://arxiv.org/abs/1012.1361.
3. OEIS A007070, integer sequence \(a_n=4a_{n-1}-2a_{n-2}\), https://oeis.org/A007070 (numerical sequence and preexisting interpretations; not a source of the present Coxeter-type theorem).
