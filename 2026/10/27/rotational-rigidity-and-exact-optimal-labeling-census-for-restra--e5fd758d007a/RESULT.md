# Rotational rigidity and exact optimal-labeling census for restrained double Roman domination on cycles

## Finding

Let \(C_n\) be the simple cycle with individually labeled vertices \(v_0,\ldots,v_{n-1}\), where \(n\ge3\) and indices are modulo \(n\). For a restrained double Roman dominating function \(f\) on \(C_n\), let its weight be \(w(f)=\sum_{i=0}^{n-1}f(v_i)\). Let \(M_n\) denote the number of functions attaining the minimum possible weight. Then

\[
M_n=\begin{cases}
3,&3\mid n,\\
10,&n\in\{4,5\},\\
n,&n\ge7\text{ and }3\nmid n.
\end{cases}
\]

All minimum functions are classified explicitly. For \(n=3k\), their cyclic label words are the three distinct rotations of \((003)^k\). For \(n=3k+1\), with \(k\ge1\), the functions containing a zero are exactly the rotations of \((0033)(003)^{k-1}\). For \(n=3k+2\), with \(k\ge1\), the functions containing a zero are exactly the rotations of \((00313)(003)^{k-1}\). For \(n\ge6\), these are **all** minimum functions, forming a single dihedral orbit. The only further minimum functions occur at \(n=4\) (choose any two vertices for value \(2\), all others value \(1\)) and at \(n=5\) (choose any two nonadjacent vertices for value \(2\), all others value \(1\)). Hence \(C_4\) has three dihedral orbits of minimizers and \(C_5\) has two.

The resulting ordinary generating function is the rational series

\[
\sum_{n\ge3}M_nt^n=\frac{t}{(1-t)^2}-t-2t^2-\frac{3t^6}{(1-t^3)^2}+6t^4+5t^5.
\]

The previously established minimum-weight identity, used only as context and also recovered below, is \(\gamma_{rdR}(C_n)=n\) when \(3\mid n\), and \(\gamma_{rdR}(C_n)=n+2\) otherwise. The claim here is the **exhaustive structure, exact count, and orbit census** of minimum functions, not this known scalar identity.

## Assumptions and scope

Graphs are finite and simple. An admissible labeling is a function \(f:V(C_n)\to\{0,1,2,3\}\) such that (i) a vertex carrying \(0\) has either a neighbor carrying \(3\) or two neighbors carrying \(2\); (ii) a vertex carrying \(1\) has a neighbor carrying \(2\) or \(3\); and (iii) the subgraph induced by the vertices carrying \(0\) has no isolated vertices. The empty zero set is allowed. The counted functions are assignments to the fixed labeled vertices; rotations and reflections are **not** identified when computing \(M_n\). The notation \((003)^k\) is a repeated word, not an algebraic power of a graph. Only cycles of order at least three are considered.

## Proof

**Zero-pair lemma.** Suppose an admissible labeling has at least one zero. Each maximal cyclic run of zeros consists of exactly two vertices, and the immediately preceding and following vertices each carry \(3\). Indeed, every zero needs a zero neighbor by the restraint condition. As the degree is two, the other neighbor must be a \(3\) to satisfy double Roman defense: two neighboring \(2\)'s are impossible in the presence of a zero neighbor. Thus a zero cannot have two zero neighbors, and each zero run is a pair flanked by \(3\)'s. Conversely, all zero vertices of such an arrangement satisfy both of their conditions; the remaining condition is that each \(1\) in a positive run see a \(2\) or \(3\).

Write the cyclic word, up to cyclic concatenation, as \(00P_1\,00P_2\,\cdots\,00P_k\) for \(k\ge1\). Every positive word \(P_i\) has length \(\ell_i\ge1\), starts and ends in \(3\), and any \(1\) inside it must have a neighboring \(2\) or \(3\). For \(\ell_i=1\), necessarily \(P_i=3\), with weight \(3=\ell_i+2\). For \(\ell_i\ge2\), the endpoints contribute \(6\) and every interior entry contributes at least \(1\), so

\[
\sum_{x\in P_i}x\ \ge\ \ell_i+4=(\ell_i+2)+2.
\]

Equality holds exactly when all interior entries are \(1\). Such a word is feasible precisely for \(\ell_i\in\{2,3,4\}\): the three possibilities are \(33\), \(313\), and \(3113\). When \(\ell_i\ge5\), the middle of three consecutive interior ones has no neighboring defender, so equality fails. Therefore the **excess**

\[
\delta_i=\Big(\sum_{x\in P_i}x\Big)-(\ell_i+2)
\]

is a nonnegative integer: it vanishes only for \(P_i=3\), is never \(1\), and is \(2\) precisely for those three defect words. Summing the lengths and weights of all zero-pair/positive-run blocks yields \(w(f)=n+\sum_i\delta_i\).

**No-zero lemma.** If no vertex has label \(0\), let \(H\) be the vertices labeled \(2\) or \(3\). The defining condition for label \(1\) makes \(H\) a dominating set of the cycle. Each member of \(H\) dominates at most three vertices (including itself), whence \(|H|\ge\lceil n/3\rceil\), and

\[
w(f)\ge n+\lceil n/3\rceil.
\]

In particular, this is strictly greater than \(n+2\) when \(n\ge7\). At \(n=4,5\), equality with \(n+2\) forces either two labels \(2\) with all remaining labels \(1\), or one label \(3\) with all remaining labels \(1\). The latter cannot dominate \(C_4\) or \(C_5\). Two labels \(2\) work in \(C_4\) at every choice of two vertices (six choices), and in \(C_5\) exactly when their vertices are nonadjacent (five choices).

**Minima and their exhaustive classification.** With zeros, the excess calculation proves \(w(f)\ge n\). Equality requires \(P_i=3\) for every \(i\), hence the cyclic word \((003)^k\) and \(n=3k\). If \(3\nmid n\), not every positive run can have length one; therefore \(w(f)\ge n+2\). These bounds also hold without zeros by the no-zero lemma. They are attained for \(n=3k\) by \((003)^k\); for \(n=3k+1\) by \((0033)(003)^{k-1}\); and for \(n=3k+2\) by \((00313)(003)^{k-1}\). Every displayed word is admissible (each zero pair is flanked by \(3\), while the only possible \(1\) is between two \(3\)'s). This also proves the cited minimum-weight formula without relying on it.

For an optimum of nonzero excess, the excess is exactly two, so precisely one \(P_i\) has excess two; all other \(P_j\)'s are \(3\). The distinguished positive run must be \(33\), \(313\), or \(3113\), producing respectively a length increment of one, two, or three over the basic three-vertex \(003\) block. Modulo three, the distinguished run is thus \(33\) when \(n\equiv1\pmod3\), or \(313\) when \(n\equiv2\pmod3\). The third possibility can occur only at weight \(n+2\) when \(3\mid n\), which is not optimal. The no-zero lemma excludes additional optima for \(n\ge7\), and its small cases give exactly the exceptions above.

For \(n\equiv0\pmod3\), the periodic word has exactly three distinct rotations. For \(n\equiv1\pmod3\), the unique adjacent \(33\) in the zero-containing optimum makes its cyclic period exactly \(n\); for \(n\equiv2\pmod3\), the unique vertex labeled \(1\) does the same. Hence these classes give \(n\) distinct functions each. At \(n=4,5\), add respectively six and five no-zero functions, obtaining ten each. The unique-defect words and the periodic word are invariant under a reflection up to rotation, so each is a single dihedral orbit. At \(n=4\), the six extra no-zero functions split into four adjacent-pair and two opposite-pair placements; at \(n=5\) all five extra placements form one orbit. This establishes the orbit statements.

Finally, sum the preceding casewise formula over \(n\ge3\). The series \(\sum_{n\ge3}nt^n=t/(1-t)^2-t-2t^2\) is corrected on multiples of three from \(3k\) to \(3\), adding \(-3t^6/(1-t^3)^2\), and corrected at \(n=4,5\) by \(6t^4+5t^5\). The displayed rational generating function follows.

## Verification

The accompanying standalone `verify_rdrd_cycles.py` independently evaluates the vertexwise conditions on every four-label assignment for \(3\le n\le9\). It also constructs the sixteen-state weighted cyclic automaton on adjacent label pairs and computes minimum-weight closed-walk counts for \(3\le n\le120\). Both methods agree with every predicted minimum and exact count. The initial pairs \((\gamma_{rdR}(C_n),M_n)\) for \(n=3,4,5,6,7,8,9\) are \((3,3),(6,10),(7,10),(6,3),(9,7),(10,8),(9,3)\). These finite checks are independent corroboration, not a substitute for the all-orders proof.

## Relationship to prior work

Mojdeh, Masoumi, and Volkmann introduced restrained double Roman domination and proved the scalar minimum formula for cycles in their June 16, 2021 preprint, Theorem 5, later published as Theorem 3.3. That article gives example optimum assignments but not an exhaustive minimum-function enumeration. Samadi and collaborators developed general bounds, algorithms, and structural results; Gao, Xi, and Yue studied products and corona operations. Their general theorems and cycle-related product results are compatible with the above classification but do not supply the complete labeled-cycle optimizer census or its dihedral-orbit distinctions. In particular, knowing \(\gamma_{rdR}(C_n)\) and exhibiting one optimum cannot determine how many other optima exist.

## Limitations

The result concerns ordinary labeled simple cycles only; it does not enumerate nonminimum restrained double Roman functions, optimize other domination variants, or address arbitrary graphs. Literature-priority uncertainty remains for unindexed or differently described optimum-labeling counts. The exhaustive finite checks do not certify originality or replace the combinatorial proof. Independent external verification has not been performed.

## References

1. D. A. Mojdeh, I. Masoumi, and L. Volkmann, *Restrained double Roman domination of a graph*, arXiv:2106.08501 (first submitted June 16, 2021), particularly Theorem 5; RAIRO Operations Research 56 (2022), 2293–2304, DOI:10.1051/ro/2022089.
2. B. Samadi, N. Soltankhah, H. Abdollahzadeh Ahangar, M. Chellali, D. A. Mojdeh, S. M. Sheikholeslami, and J. C. Valenzuela-Tripodoro, *Restrained condition on double Roman dominating functions*, arXiv:2109.06666 (2021), especially introduction and Sections 2–3.
3. Z. Gao, C. Xi, and J. Yue, *The restrained double Roman domination and graph operations*, arXiv:2111.04363 (2021), especially Sections 3–5.
