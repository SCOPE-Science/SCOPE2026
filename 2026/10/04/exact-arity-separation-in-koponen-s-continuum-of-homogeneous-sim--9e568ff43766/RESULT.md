# Exact arity separation in Koponen's continuum of homogeneous simple structures

## Finding

Let \(H_n\) and \(M_T\) be the ternary structures from Koponen's continuum family: \(T\subseteq\{H_n:n\ge3\}\), and \(M_T\) is the Fraïssé limit of the finite structures omitting every member of \(T\). Let \(a_k(T)\) be the number of \(\operatorname{Aut}(M_T)\)-orbits on injective ordered \(k\)-tuples.

If \(T\ne T'\) and
\[
n=\min\{j\ge3:H_j\in T\triangle T'\},
\]
then
\[
a_k(T)=a_k(T')\quad\text{for every }k\le n,
\]
while at the first possible arity,
\[
\left|a_{n+1}(T)-a_{n+1}(T')\right|
 =\frac{(n+1)!}{n}
 =(n+1)(n-1)!.
\]
For orbits on unlabeled \((n+1)\)-element subsets, the corresponding gap is exactly \(1\).

The same first-difference arity and the same numerical gap hold for the full ordered-tuple orbit profile, where repeated coordinates are allowed. Consequently the complete finite orbit profile determines \(T\), although for every fixed finite \(r\) there are \(2^{\aleph_0}\) pairwise nonisomorphic members of Koponen's family whose orbit counts agree in every arity at most \(r\).

## Assumptions and scope

Koponen works in the vocabulary consisting of one ternary relation \(R\). For each \(n>2\), the finite constraint \(H_n\) has universe \(\{0,1,\ldots,n\}\). On distinct elements, \(R\) fails exactly on the triples \((0,b,b+1)\) for \(1\le b<n\) and \((0,n,1)\). Koponen proves that the structures \(H_n\) form an embedding antichain, that each corresponding forbidden-family class has free amalgamation, and that distinct choices of \(T\) yield nonisomorphic countable homogeneous supersimple structures of SU-rank \(1\) with degenerate algebraic closure.

The orbit counts considered here are for the full automorphism group of \(M_T\). Homogeneity identifies injective ordered-tuple orbits with labeled finite structures in the age. The statement does not claim a new construction of the family or new simplicity-theoretic properties; it quantifies exactly how soon two members of the existing family become distinguishable by finite orbit counts.

## Proof

Fix distinct \(T,T'\), and let
\[
n=\min\{j\ge3:H_j\in T\triangle T'\}.
\]
The constraint \(H_j\) has \(j+1\) elements. Therefore no constraint indexed by \(j\ge n\) can affect a finite structure with at most \(n\) elements. Since \(T\) and \(T'\) agree on every \(H_j\) with \(j<n\), their ages contain exactly the same finite structures of sizes at most \(n\). Homogeneity therefore gives
\[
a_k(T)=a_k(T')\qquad(k\le n).
\]

Now consider size \(n+1\). The families still agree on all smaller constraints, while every constraint \(H_j\) with \(j>n\) is too large to embed into an \((n+1)\)-element structure. Thus the only possible difference between the two ages at this size is whether \(H_n\) itself is forbidden.

Koponen's antichain lemma implies that \(H_n\) omits every \(H_j\) with \(j<n\). Hence, on the side where \(H_n\notin T\), every labeled copy of \(H_n\) occurs in the age; on the side where \(H_n\in T\), exactly those labeled structures are absent. Because an embedding between two structures of the same finite cardinality is onto, an \((n+1)\)-element structure contains \(H_n\) precisely when it is isomorphic to \(H_n\).

It remains to count labeled copies. In \(H_n\), the element \(0\) is definable inside the finite structure as the unique element occurring in the first coordinate of every failure of \(R\). Once \(0\) is fixed, define a directed relation on the positive elements by
\[
S(b,c)\iff \neg R(0,b,c).
\]
Then \(S\) is exactly the directed cycle
\[
1\to2\to\cdots\to n\to1.
\]
Consequently every automorphism of \(H_n\) fixes \(0\) and acts as a rotation of this directed \(n\)-cycle, while every rotation is indeed an automorphism. Hence
\[
|\operatorname{Aut}(H_n)|=n.
\]
By orbit-stabilizer for relabelings, the number of labeled copies of \(H_n\) on a fixed \((n+1)\)-element set is
\[
\frac{(n+1)!}{|\operatorname{Aut}(H_n)|}
=\frac{(n+1)!}{n}
=(n+1)(n-1)!.
\]
These are exactly the injective ordered-tuple orbits lost when \(H_n\) is added to the forbidden family. This proves the claimed first-difference formula.

For unlabeled \((n+1)\)-element substructures, all those labeled copies form one isomorphism type, so the gap is exactly \(1\).

Finally, let \(b_k(T)\) denote the number of orbits on all ordered \(k\)-tuples, allowing repetitions. Equality of coordinates partitions the coordinate set into \(j\) blocks, and after collapsing equal coordinates the remaining orbit is an injective \(j\)-tuple orbit. Thus
\[
b_k(T)=\sum_{j=1}^{k}{k\brace j}a_j(T),
\]
where \({k\brace j}\) is a Stirling number of the second kind. Since the injective profiles first differ at \(n+1\), so do the full profiles, and the coefficient of \(a_{n+1}\) there is \({n+1\brace n+1}=1\). The first gap is therefore unchanged.

To obtain the continuum-fiber consequence, fix finite \(r\) and vary \(T\) over arbitrary subsets of \(\{H_n:n\ge r\}\). There are \(2^{\aleph_0}\) such choices, Koponen's theorem makes the resulting limits pairwise nonisomorphic, and every forbidden constraint has size at least \(r+1\). Hence all those structures have identical orbit counts through arity \(r\).

## Verification

A separate finite checker reconstructs \(H_n\) directly from Koponen's definition. For \(3\le n\le7\), it enumerates all permutations and obtains
\[
|\operatorname{Aut}(H_n)|=3,4,5,6,7,
\]
respectively. It then verifies that the numbers of distinct labeled copies are
\[
8,30,144,840,5760,
\]
which equal \((n+1)!/n\) in each case. The same checker exhaustively tests the relevant finite embeddings among \(H_3,\ldots,H_7\) and finds none between different indices, agreeing with Koponen's antichain lemma. It ends with `VERIFY_OK`.

The computation is only a replay of finite instances. The general theorem rests on the structural proof above and Koponen's published antichain and Fraïssé-family results.

## Relationship to prior work

Koponen's 2017 preprint, later published in the *Journal of Symbolic Logic*, constructs the family \(M_T\), proves that the \(H_n\) form an embedding antichain, and derives continuum many nonisomorphic ternary homogeneous supersimple structures of SU-rank \(1\). The source does not state an orbit-profile theorem or count the labeled copies of \(H_n\).

The general correspondence between finite substructures of a homogeneous structure and automorphism orbits on injective tuples is classical. What is specific here is the exact recovery threshold for Koponen's coding family: the least differing forbidden index determines the first differing tuple arity, and the difference there is the explicit factorial quantity \((n+1)!/n\).

Targeted searches for the family together with “orbit profile,” “tuple orbit,” “first differing arity,” and automorphism-count terminology did not locate this statement. Broader searches surfaced orbit-profile calculations for unrelated homogeneous reducts, but not an implication covering Koponen's constraints. This supports, but cannot establish absolutely, the originality assessment.

## Limitations

The theorem is a quantitative consequence of an existing construction, not a new classification of homogeneous ternary structures. It uses the particular constraint family \(H_n\), and no analogous formula is asserted for arbitrary forbidden-antichain Fraïssé classes.

The result concerns orbit *counts*. It does not classify the topological automorphism groups up to isomorphism or reconstruct \(T\) from weaker dynamical invariants.

The literature search cannot exclude an unpublished observation, folklore, or a result indexed under terminology not captured by the searches performed.

## References

1. Vera Koponen, “On constraints and dividing in ternary homogeneous structures,” arXiv:1707.05954, first posted 19 July 2017; *Journal of Symbolic Logic* 83 (2018), 1691–1721. DOI: 10.1017/jsl.2018.61.
2. Peter J. Cameron, *Oligomorphic Permutation Groups*, London Mathematical Society Lecture Note Series 152, Cambridge University Press, 1990, for the standard orbit/age viewpoint for homogeneous structures.
