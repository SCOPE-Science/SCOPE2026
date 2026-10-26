# Four-point Pareto frontier for single-redundancy, three-dimensional file retrieval

## Finding
For every finite field \(\mathbb F_q\), fix complementary information files \(F_1=\langle e_1\rangle\) and \(F_2=\langle e_2,e_3\rangle\) in \(\mathbb F_q^3\). For a rank-three generator matrix \(G\in\mathbb F_q^{3\times4}\), sample its four column indices independently, uniformly, and with replacement until the sampled columns span the requested file. Let \(E_i(G)\) be the expected number of samples for file \(F_i\).

**The complete set of Pareto-minimal pairs** \((E_1(G),E_2(G))\), with componentwise minimization, is
\[
\boxed{\big\{(2,6),\;(8/3,5),\;(3,4),\;(4,10/3)\big\}.}
\]
In particular, every admissible code is weakly dominated by a code achieving one of these pairs, and none of the four pairs dominates another. This holds for *all* finite fields and all rank-three matrices, without imposing systematicity or requiring nonzero columns.

Writing \(P=e_1\), \(U=e_2\), and \(V=e_3\), the four points are achieved in the displayed order by the column lists
\[
[P,P,U,V],\quad [P,U,P+U,V],\quad [P,U,V,P+U+V],\quad [P,U,V,U+V].
\]
These witnesses work unchanged over every finite field.

## Assumptions and scope
A rank-three matrix has four *indexed* columns, so repeated or zero columns are permitted initially. Sampling selects an index uniformly from the four, even when column values coincide. The stopping time for file \(F_i\) is the first time the sampled columns span that entire subspace. Comparison of expected-time pairs is componentwise: a point is dominated if another attainable point is no greater in either component and strictly smaller in at least one.

The file dimensions are exactly \((1,2)\), the length is exactly four, the rank is exactly three, and the field size is an arbitrary prime power. The result concerns retrieval from noiseless, uniformly sampled coded symbols, not error-correcting reliability, nonuniform sampling, or longer codes.

## Proof
**1. Exact four-column recovery accounting.** For each file, define \(\alpha_i(s)\) as the number of \(s\)-subsets of the four column indices whose column span contains \(F_i\). The standard coupon-collection stopping-time identity gives
\[
E_i=4H_4-\sum_{s=1}^3\frac{\alpha_i(s)}{\binom3s}
=\frac{25}{3}-\frac{\alpha_i(1)+\alpha_i(2)}3-\alpha_i(3).
\]
File \(F_2\) cannot be spanned by a single column. Put \(a_1=\alpha_1(1)\), \(a_2=\alpha_1(2)\), \(a_3=\alpha_1(3)\), \(b_2=\alpha_2(2)\), and \(b_3=\alpha_2(3)\), so
\[
E_1=\frac{25}{3}-\frac{a_1+a_2}{3}-a_3,\qquad
E_2=\frac{25}{3}-\frac{b_2}{3}-b_3.
\]
Only pairs of *independent pure-\(F_2\)* columns can span \(F_2\). At most three columns can belong to \(F_2\), since \(G\) has rank three. Thus \(b_2\le3\), \(b_3\le4\), and universally \(E_2\ge10/3\).

If a column is zero, replace it by \(P\) without changing the other columns. The matrix retains rank three; under the same drawn index sequence, every new sampled span contains the original span. The stopping times do not increase, while that of \(F_1\) decreases with positive probability (for instance, if the zero index is drawn first). Therefore no matrix containing a zero column is Pareto minimal. It suffices to analyze four nonzero columns.

**2. Unique dependence support.** Four nonzero vectors of rank three have a one-dimensional relation space. The unique relation, up to scaling, has support of size \(r\in\{2,3,4\}\). This trichotomy exhausts all fields and all matrices.

**Case \(r=4\).** Every triple is independent, so \(a_3=b_3=4\). Moreover at most two columns lie in \(F_2\), else an all-\(F_2\) triple would be dependent. Hence \(b_2\le1\), giving \(E_2\ge4\). If \(P\) is a column, it occurs only once, and exactly the three pairs containing it span \(P\); hence \(a_1=1,a_2=3\) and \(E_1=3\). Otherwise \(a_1=0\) and at most two pairs span \(P\): two such pairs sharing a column would create a dependent triple, forbidden in this case. Thus \(E_1\ge25/3-2/3-4=11/3\). Every such matrix therefore satisfies \(E_1\ge3,E_2\ge4\).

**Case \(r=3\).** The dependent triple consists of three distinct projective points \(T_1,T_2,T_3\) spanning one plane \(W\); the fourth column \(Q\) lies outside \(W\). The other three triples are independent.

If \(P\) is one of \(T_1,T_2,T_3\), then \(a_1=1,a_2=4,a_3=4\), giving \(E_1=8/3\). Since \(W\) contains \(P\) and differs from \(F_2\), only the other three triples can span \(F_2\). At most two columns can be pure-\(F_2\) (at most one from the projective line of the triple, and possibly \(Q\)), so \(b_2\le1,b_3=3\), whence \(E_2\ge5\).

If \(P=Q\), the three pairs containing \(Q\) and the three independent triples span \(P\), whereas the dependent triple does not: \(a_1=1,a_2=3,a_3=3\), giving \(E_1=4\). If \(P\) lies in \(W\) but is none of its three columns, exactly the three pairs within the dependent triple span \(P\), and all four triples span it, giving \(a_1=0,a_2=3,a_3=4\) and \(E_1=10/3\). Finally, if \(P\notin W\) and \(P\ne Q\), no pair within \(W\) spans \(P\); at most one of the three distinct lines through \(Q\) and \(T_j\) can contain \(P\). Therefore \(a_1=0,a_2\le1,a_3=3\), so \(E_1\ge5\). Apart from the explicitly bounded \(8/3\) case, this case always has \(E_1\ge3\).

**Case \(r=2\).** Exactly two columns are parallel, equal to a projective point \(Q\); the other two, call them \(C,D\), together with \(Q\) are independent. If \(Q=P\), both parallel copies are pure-\(F_1\), so \(a_1=2,a_2=5,a_3=4\), giving \(E_1=2\). The two dependent triples contain \(P\) and cannot span \(F_2\), while the other two are independent. At most one pure-\(F_2\) pair exists, hence \(b_2\le1,b_3=2\), giving \(E_2\ge6\).

If \(Q\ne P\) and \(P\) equals \(C\) or \(D\), then \(a_1=1,a_2=3,a_3\le4\), hence \(E_1\ge3\). If \(P\) is not a column, then the parallel pair does not span it; among the pairs \(QC,QD\), at most one projective line can contain \(P\) because \(Q,C,D\) are independent. Each such line contributes two indexed pairs, and \(CD\) contributes at most one, so \(a_1=0,a_2\le3,a_3\le4\) and \(E_1\ge10/3\). Thus \(E_1\ge3\) whenever \(Q\ne P\).

**3. Sharp small-\(E_2\) obstruction.** Suppose \(E_2<4\). The counting identity and \(b_3\le4\) force \(b_2\ge2\), which requires at least three pure-\(F_2\) columns. Exactly three are pure-\(F_2\), and the fourth, \(Q\), lies outside \(F_2\). Since the triple inside \(F_2\) cannot span \(P\), we have \(a_3\le3\). If \(Q=P\), then \(a_1=1,a_2=3,a_3=3\), giving \(E_1=4\). Otherwise \(a_1=0\); a pair spanning \(P\) must consist of \(Q\) and a pure-\(F_2\) column on the unique projective line \(\langle P,Q\rangle\cap F_2\). Among the three pure columns, at most two occupy that direction because rank three requires them to span \(F_2\). Hence \(a_2\le2\) and \(E_1\ge25/3-2/3-3=14/3>4\). Therefore
\[
\boxed{E_2<4\implies E_1\ge4.}
\]

**4. Dominance and sharpness.** The dependence trichotomy proves that either \(E_1=2,E_2\ge6\); or \(E_1=8/3,E_2\ge5\); or \(E_1\ge3\). Within the last case, \(E_2\ge4\) gives domination by \((3,4)\), whereas \(E_2<4\) implies \(E_1\ge4,E_2\ge10/3\) and domination by \((4,10/3)\). The four matrices in the Finding have exact expectations in the stated order by the displayed counting identity. Their coordinate pairs are pairwise incomparable. Consequently, all four and only four are Pareto minimal. \(\square\)

## Verification
The standalone `verify_retrieval_frontier.py` independently computes exact retrieval expectations by two methods: the subset-recovery formula above and a coupon-drawing Markov recurrence. For each subset \(S\subseteq\{1,2,3,4\}\), the Markov method sets the remaining expected draws to zero once \(S\) spans the target; otherwise it uses
\[
T(S)=\frac{4+\sum_{j\notin S}T(S\cup\{j\})}{4-|S|}.
\]
The check exhausts all full-rank multisets of four nonzero projective columns over \(\mathbb F_2\) and \(\mathbb F_3\), including all dependence patterns, and compares both rational methods. It finds exactly \(119\) and \(1404\) full-rank multisets, respectively, with exactly the four predicted Pareto points. It also evaluates all four explicit witnesses independently over prime fields of orders \(2,3,5,7\). The successful record prints `VERIFY_OK`. These computations check small cases; the field-uniform theorem follows from the rank-and-incidence proof above.

## Relationship to prior work
Bar-Lev (arXiv:2603.17154, first publicly available March 17, 2026) introduced the two-file block-retrieval tradeoff and the general subset-count formula. Her constructions cover file-dedicated MDS and systematic global MDS families but do not classify all length-four rank-three pairs. The endpoints \((2,6)\) and \((4,10/3)\) arise from dedicated MDS allocations and are **not** claimed here as previously unknown constructions.

Vlachos and Bar-Lev (arXiv:2609.36067, first publicly available September 28, 2026) establish a general sufficient condition for a hyperbolic bound involving the number of mixed columns. Their Section V explicitly asks whether dedicated MDS codes are Pareto optimal at finite lengths and identifies nonsystematic generalization as a further direction. It does not identify the four finite-length Pareto points.

The publicly available “Dimension-three one-mixed-column hyperbolic bound” establishes a hyperbolic inequality for systematic dimension-three codes with exactly one mixed column for any length. A scalar inequality does not imply the present *exact* four-point Pareto frontier: it neither enumerates all finite-length expectation pairs nor rules out unlisted Pareto points, and its hypotheses exclude some of the rank-three four-column matrices considered here. The new result handles all dependence types and arbitrary mixed-column configurations in the first-redundancy case.

## Limitations
The full classification is restricted to four stored symbols, three information symbols, two files of dimensions one and two, and the uniform noiseless sampling model. It does not establish a general finite-length Pareto frontier for greater redundancy or higher dimensions. It supplies no error correction, synthesis model, or nonuniform sampling theorem. Existing published literature was compared at the statement and implication level, but an equivalent classification in unindexed work cannot be excluded. The accompanying verification is finite and is not a substitute for the proof for all finite fields.

## References
1. D. Bar-Lev, “Coded Information Retrieval for Block-Structured DNA-Based Data Storage,” arXiv:2603.17154v1, public March 17, 2026; full text at https://arxiv.org/html/2603.17154v2 (July 19, 2026 revision).
2. C. V. A. Vlachos and D. Bar-Lev, “A Hyperbolic Bound for File Retrieval in DNA-Based Data Storage,” arXiv:2609.36067v1, public September 28, 2026; full text at https://arxiv.org/abs/2609.36067.
3. “Dimension-three one-mixed-column hyperbolic bound,” public RESULT.md at https://github.com/Resultary/2026/blob/main/2026/10/4/SCOPE-dimension-three-one-mixed-column-hyperbolic-bound--b0daab8aecae/RESULT.md.
