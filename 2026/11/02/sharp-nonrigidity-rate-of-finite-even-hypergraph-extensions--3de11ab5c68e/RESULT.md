# Sharp nonrigidity rate of finite even hypergraph extensions

## Finding

Fix integers \(k\geq2\) and \(s\geq1\), let \(A=(\mathbf F_2)^s\), and put \(q=|A|=2^s\). A finite **even \(A\)-coloured \((k+1)\)-hypergraph** on \([n]\) is a map \(F:\binom{[n]}{k+1}\to A\) with
\[
\sum_{T\in\binom{U}{k+1}}F(T)=0\qquad\text{for every }U\in\binom{[n]}{k+2}.
\]
All colours are named: a vertex automorphism preserves each element of \(A\), not just the underlying partition of faces. Sample \(F\) uniformly from the finite set of such maps. Define \(a_{n,k}=\binom{n-3}{k-1}\) and \(M_{n,k}=\binom{n-1}{k}\).

**Theorem.** As \(n\to\infty\), with \(k,s\) fixed,
\[
\Pr\bigl(\operatorname{Aut}(F)\ne\{1\}\bigr)
=\binom n2 q^{-a_{n,k}}(1+o(1)).
\]
Each transposition fixes exactly the fraction \(q^{-a_{n,k}}\) of all structures; the combined contributions of other nonidentity permutations and of intersections of distinct transposition events are both \(o\bigl(\binom n2q^{-a_{n,k}}\bigr)\). The exact number of labelled structures is \(q^{M_{n,k}}\). Consequently, the number \(u_{n,k,q}\) of vertex-isomorphism classes obeys the sharp Burnside correction
\[
u_{n,k,q}=\frac{q^{M_{n,k}}}{n!}
\left(1+\binom n2q^{-a_{n,k}}+o\left(\binom n2q^{-a_{n,k}}\right)\right).
\]
The statement is for fixed arity and fixed colour rank; it is not a uniform estimate when these parameters grow with \(n\).

## Assumptions and scope

The probability space contains all labelled even maps \(F\), each equally likely. The parameter \(q\) is a power of two because the parity equation is imposed separately in each of the \(s\) binary coordinates. The smallest cases of \(k\) and \(q\) specialize to ordinary two-graphs (equivalently, Seidel switching classes), whose exact isomorphism enumeration substantially predates this statement. The theorem concerns their common higher-arity and multicolour extension, not an assertion of priority for the two-graph enumeration.

## Proof

**1. Root coordinates and exact sample size.** Choose a distinguished vertex \(r\). Arbitrarily prescribe the \(A\)-values \(h(S)=F(\{r\}\cup S)\) for all \(k\)-subsets \(S\) of \([n]\setminus\{r\}\). Every remaining face is uniquely forced:
\[
F(T)=\sum_{v\in T}h(T\setminus\{v\})
\quad(r\notin T,\ |T|=k+1).
\]
Indeed, the parity equation on \(T\cup\{r\}\) forces this equality, and parity on any \((k+2)\)-set not containing \(r\) holds because every \(k\)-subset is counted exactly twice. Therefore the \(M_{n,k}\) root coordinates are free and independent uniform \(A\)-values, giving precisely \(q^{M_{n,k}}\) structures.

**2. Transposition events.** If a permutation \(\sigma\) fixes \(r\), its action on the root coordinates permutes the \(k\)-subsets of \([n]\setminus\{r\}\). An invariant structure is exactly a root assignment constant on every orbit of this action. Thus, writing \(d(\sigma)\) for the number of coordinates minus the number of these orbits,
\[
\Pr(\sigma\in\operatorname{Aut}(F))=q^{-d(\sigma)}.
\]
If \(\sigma\) swaps exactly two vertices, choose \(r\) outside the swap. Precisely \(2\binom{n-3}{k-1}\) root coordinates, those containing exactly one swapped vertex, form two-element orbits. All other root coordinates are fixed. Hence \(d(\sigma)=a_{n,k}\) **exactly**, for every \(n\ge k+2\).

**3. All other permutations with a fixed point are negligible.** Let \(t\) be the support size of \(\sigma\), and choose a fixed root. Write \(f=n-1-t\) for the number of other fixed vertices, and let \(c\) be the number of nontrivial cycles on the support. For each \((k-1)\)-subset \(S\) of the \(f\) other fixed vertices, the \(t\) coordinates \(S\cup\{v\}\), one for each moved vertex \(v\), have precisely \(c\) orbits. The coordinate families for different \(S\) are disjoint, so
\[
d(\sigma)\ge (t-c)\binom f{k-1}.
\]
For any nontransposition, \(t\ge3\); if \(t\in\{3,4\}\), then \(t-c\ge2\), and if \(t\ge5\), then \(t-c\ge t/2\).

Fix a sufficiently small constant \(\varepsilon>0\), depending on \(k\), such that, for all large \(n\), \(t\le\varepsilon n\) implies \(\binom{n-1-t}{k-1}\ge\frac34a_{n,k}\). Consequently every nontransposition with \(t\le\varepsilon n\) has \(d(\sigma)\ge\frac32a_{n,k}\) when \(t=3,4\), or \(d(\sigma)\ge\frac{3t}{8}a_{n,k}\) when \(t\ge5\). There are at most \(n^t\) permutations of support \(t\). Since \(a_{n,k}=\Theta(n^{k-1})\) and \(k\ge2\), summing these bounds for \(3\le t\le\varepsilon n\) gives \(o(n^2q^{-a_{n,k}})\).

For \(t\ge\varepsilon n\), the number of fixed \(k\)-subsets of the other \(n-1\) vertices is at most \(\binom{n-1-t}{k}+O_k(n^{k-1})\): any fixed subset containing a moved point must contain a whole nontrivial cycle, and there are only \(O_k(n^{k-1})\) such fixed subsets. Every nonfixed coordinate orbit has size at least two, so
\[
d(\sigma)\ge\tfrac12\left[\binom{n-1}{k}-\binom{n-1-t}{k}-O_k(n^{k-1})\right]=\Omega_{k,\varepsilon}(n^k).
\]
Summation over at most \(n!\) permutations is \(o(n^2q^{-a_{n,k}})\), since \(n\log n=o(n^k)\).

**4. Permutations with no fixed point are negligible.** Regard the parity structures over one binary coordinate as the image \(Z\) of the ordinary simplicial coboundary map \(\delta:W\to Z\), where \(W\) is the binary vector space of \(k\)-subset labels. The root argument shows \(\dim Z=M_{n,k}\) and \(\dim\ker\delta=\binom{n-1}{k-1}\). For any vertex permutation \(\sigma\), let \(Y=\{w\in W:(\sigma-1)w\in\ker\delta\}\). Then \(Y/\ker\delta\cong Z^\sigma\). The linear map \(Y\to\ker\delta\), \(w\mapsto(\sigma-1)w\), has kernel \(W^\sigma\); therefore
\[
\dim Z^\sigma\le\dim W^\sigma
=\#\{\text{orbits of }\sigma\text{ on }k\text{-subsets}\}.
\]
For a derangement, any fixed \(k\)-subset is a union of cycles of length at least two. There are \(O_k(n^{\lfloor k/2\rfloor})\) such subsets. Hence the number of subset orbits is at most \(\frac12\binom nk+O_k(n^{\lfloor k/2\rfloor})\). The invariant-subspace codimension is therefore at least
\[
\binom{n-1}{k}-\frac12\binom nk-O_k(n^{\lfloor k/2\rfloor})=\Omega_k(n^k).
\]
The same linear equations apply independently to each of the \(s\) binary coordinates, so the fixed probability is \(q^{-d(\sigma)}\). Summing over all derangements is again negligible.

**5. Transposition-event overlaps.** Let \(\tau\ne\nu\) be two transpositions. For large \(n\), select a common fixed root outside the at most four moved vertices. The group they generate acts on their union in two possibilities: it is transitive on three vertices if the swaps overlap, or has two orbits on four vertices if disjoint. In either case its invariant root assignments satisfy at least two independent equalities for each \((k-1)\)-subset of the other fixed vertices. Therefore
\[
\Pr(\tau,\nu\in\operatorname{Aut}(F))\le q^{-2\binom{n-5}{k-1}}.
\]
Summing over fewer than \(n^4\) ordered pairs yields \(o(n^2q^{-a_{n,k}})\), since \(2\binom{n-5}{k-1}-a_{n,k}\to+\infty\). The union bound and the first two Bonferroni terms now give the nonrigidity asymptotic.

**6. Isomorphism count.** Burnside's lemma gives the exact identity
\[
u_{n,k,q}=\frac{q^{M_{n,k}}}{n!}\sum_{\sigma\in S_n}\Pr(\sigma\in\operatorname{Aut}(F)).\]
The identity permutation contributes one; the \(\binom n2\) transpositions each contribute exactly \(q^{-a_{n,k}}\); Steps 3–4 show that all other contributions are lower order. This proves the stated correction. \(\square\)

## Verification

The attached standalone `checker.py` constructs the root-coordinate parity code, forms every permutation's invariant linear equations independently from face labels, and computes their exact binary ranks by row reduction. It separately checks the fixed-root orbit formula, the transposition codimension, conjugacy-class consistency, and Burnside integrality. With ordinary Python 3, run `python3 checker.py`. Successful output ends in `ALL_CHECKS_OK`. Checked configurations include arities three and four on up to seven vertices, with exact isomorphism counts \(3,7,16\) for the first arity at the displayed tested sizes, and \(3,16,423\) for the second. These finite verifications are not substitutes for the all-parameter proof.

## Relationship to prior work

Estrada (2026), Section 3, constructs the infinite homogeneous even hypergraph and its merges for numbers of colours that are powers of two; that is the structural motivation and background, not a result claimed here. The present theorem concerns the sharp finite-size automorphism probability and second-order class-count asymptotic. The case \(k=2,q=2\) is the classical two-graph/switching-class setting. Mallows and Sloane (1975) already give exact enumeration in that case; this specialization is not claimed as an independently new enumerative theorem. Cameron and Spiga (2015) investigate primitive automorphism groups of switching classes and existence of representatives with trivial *graph* automorphism group, not this probability of *class* automorphisms. Standard permutation-orbit and Burnside arguments are used here as tools. Earlier work of Chung and Graham on cohomological aspects of hypergraphs is a plausible source of related parity formalism; an equivalent older asymmetry estimate under that language has not been excluded.

## Limitations

The asymptotics require fixed \(k\) and fixed \(q\), with independent, named colours in an elementary abelian two-group. They do not apply to arbitrary coloured hypergraphs, to structural automorphisms that are allowed to permute the colour names, or to growing parameters. Earlier two-graph enumeration and generic parity-extension constructions are credited. Historical priority beyond the inspected references is not established; independent review has not been performed.

## References

- Felipe Estrada, *Transitive Extensions of Automorphism Groups of Generic Structures* (2026), arXiv:2604.12146, submitted 2026-04-13, especially Section 3. https://arxiv.org/abs/2604.12146
- C. L. Mallows and N. J. A. Sloane, *Two-Graphs, Switching Classes and Euler Graphs are Equal in Number*, SIAM J. Appl. Math. 28 (1975), 876–880. https://doi.org/10.1137/0128070
- Peter J. Cameron and Pablo Spiga, *Most switching classes with primitive automorphism groups contain graphs with trivial groups* (2015), arXiv:1407.5288, especially Sections 1 and 3. https://arxiv.org/abs/1407.5288
- F. R. K. Chung and R. L. Graham, *Cohomological Aspects of Hypergraphs*, Trans. Amer. Math. Soc. 334 (1992), 365–388. https://doi.org/10.2307/2153987
