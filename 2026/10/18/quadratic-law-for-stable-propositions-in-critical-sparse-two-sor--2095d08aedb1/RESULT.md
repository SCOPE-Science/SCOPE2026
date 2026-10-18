# Quadratic law for stable propositions in critical sparse two-sorted modal frames

## Finding

Fix \(c>0\). Let \(G_n\) and \(M_n\) be disjoint labelled sets with \(|G_n|=|M_n|=n\). Form a random two-sorted bidirectional frame with incidence relation \(I_n\subseteq G_n\times M_n\), independently inserting each pair with probability \(p_n=c/\sqrt n\), for integers \(n>c^2\). For \(A\subseteq G_n\) define
\[
A^+=\{m\in M_n:\text{every }g\in A\text{ satisfies }gI_nm\},\qquad
B^-=\{g\in G_n:\text{every }m\in B\text{ satisfies }gI_nm\}.
\]
The *stable object propositions* are exactly the subsets \(A\) fixed by \(A\mapsto (A^+)^-\); denote their number by \(S_n\). This is the extent semantics of the two-sorted window modalities studied in the logic \(\mathbf{KF}\), and each fixed point corresponds to one formal concept \((A,A^+)\).

Write \(\lambda=c^2\) and
\[
F(c)=1-e^{-\lambda}\left(1+\lambda+\frac{\lambda^2}{2}\right)
       +\frac{\lambda^2}{4}e^{-2\lambda}.
\]
Then there is a constant \(K_c<\infty\) such that for all sufficiently large \(n\),
\[
\boxed{\displaystyle \mathbb E\left|\frac{S_n}{n^2}-F(c)\right|\leq \frac{K_c}{\sqrt n}.}
\]
In particular \(S_n/n^2\to F(c)\) in \(L^1\) and in probability, and \(\mathbb E S_n=n^2F(c)+O_c(n^{3/2})\). The three terms in the limit have an exact structural explanation: concepts with two objects and at least three attributes, concepts with at least three objects and two attributes, and maximal \(2\)-by-\(2\) incidence rectangles.

## Assumptions and scope

The two sorts have exactly \(n\) labelled points each, incidence edges are independent with the same probability \(c/\sqrt n\), and \(c\) is fixed as \(n\to\infty\). Complements and incidence are not confused: a proposition is *stable* if it is fixed by the antitone Galois derivation composed twice. Empty and singleton extents and intents are included in \(S_n\). This result counts semantic fixed-point sets of the finite frame, not equivalence classes of syntactic formulas across models, nor all valuations, and does not assert almost-sure convergence under arbitrary cross-size couplings.

## Proof

**1. Concept partition.** A pair \((A,B)\) is a formal concept precisely when \(A^+=B\) and \(B^-=A\). Every stable extent gives exactly one concept. Partition concepts according to the two cardinalities \((|A|,|B|)\). Those with \(\min(|A|,|B|)\leq1\) number at most \(2n+2\), deterministically: for a specified extent or intent there can be only one concept. Denote by \(X_n\) the number with \(|A|=2,|B|\geq3\), by \(Y_n\) the number with \(|A|\geq3,|B|=2\), by \(Z_n\) those with \(|A|=|B|=2\), and by \(R_n\) those with \(|A|,|B|\geq3\). Thus
\[
S_n=X_n+Y_n+Z_n+R_n+L_n,\quad 0\leq L_n\leq2n+2.
\]

**2. Large rectangles contribute only lower order.** Every counted \((A,B)\) is a complete rectangle of its own dimensions. Hence, for \(p=p_n\),
\[
\mathbb E R_n\leq\sum_{a,b\geq3}\binom na\binom nb p^{ab}.
\]
If \(t_{a,b}=\binom na\binom nb p^{ab}\), then for \(a,b\geq3\) the ratios \(t_{a+1,b}/t_{a,b}\) and \(t_{a,b+1}/t_{a,b}\) are each at most \(np^3=c^3/\sqrt n\). Consequently the double sum is bounded by \(t_{3,3}(1-c^3/\sqrt n)^{-2}=O_c(n^{3/2})\) for large \(n\). Therefore \(\mathbb E(R_n+L_n)=O_c(n^{3/2})\).

**3. Rectangles with a side of two and the other side at least three.** Let \(U_n\) count pairs of objects with at least three common attributes. For one object pair its common-attribute count \(K\) has distribution \(\operatorname{Bin}(n,p^2)=\operatorname{Bin}(n,\lambda/n)\). If \(K\geq3\), it fails to give a concept whose extent is exactly that pair only if an additional object has all \(K\) shared attributes. Conditional on the pair's rows, that failure has probability at most \((n-2)p^K\leq np^3\). Thus \(X_n\leq U_n\), with
\[
\mathbb E(U_n-X_n)\leq \binom n2 np^3=O_c(n^{3/2}).
\]
Disjoint object pairs depend on disjoint independent rows, while pairs sharing an object have covariance bounded in absolute value by one. There are \(O(n^3)\) overlapping ordered pairs, so \(\operatorname{Var}(U_n)=O(n^3)\). Binomial-to-Poisson convergence with its standard \(O_c(1/n)\) total-variation error yields
\[
\mathbb E U_n=\frac{n^2}{2}\Pr\{\operatorname{Poi}(\lambda)\geq3\}+O_c(n).
\]
It follows by Cauchy--Schwarz that
\[
\mathbb E\left|X_n-\frac{n^2}{2}\Pr\{\operatorname{Poi}(\lambda)\geq3\}\right|=O_c(n^{3/2}).
\]
Interchanging objects and attributes proves the identical estimate for \(Y_n\).

**4. Exactly two-by-two concepts.** Choose two specified objects and two specified attributes. Their rectangle is a concept with exactly those extent and intent sets iff its four edges are present, no other attribute is shared by the two objects, and no other object has both specified attributes. The last two conditions involve disjoint sets of edge variables. Therefore
\[
\mathbb E Z_n=\binom n2^2p^4(1-p^2)^{2(n-2)}
=\frac{n^2\lambda^2}{4}e^{-2\lambda}+O_c(n).
\]
We show \(\operatorname{Var}(Z_n)=O_c(n^3)\), rather than infer concentration merely from the expectation. Expose the \(n\) independent object rows and apply the Efron--Stein resampling inequality. If row \(r\) is replaced, any changing two-by-two concept either uses row \(r\), or is a four-edge rectangle on other rows whose maximality changes because \(r\) joins their two columns. Hence the number of changes is at most the rooted counts \(H_{2,2}(r)+H_{3,2}(r)\) before and after replacement, where \(H_{a,2}(r)\) counts labelled copies of complete \(a\)-by-\(2\) incidence rectangles that include \(r\) among their \(a\) object vertices (only \(a=2,3\) is used).

For each fixed root \(r\), both \(\mathbb E H_{2,2}(r)^2\) and \(\mathbb E H_{3,2}(r)^2\) are \(O_c(n^2)\). Here is an explicit overlap check for the nontrivial case. Two rooted \(3\)-by-\(2\) copies may share \(t\in\{0,1,2\}\) further object vertices and \(s\in\{0,1,2\}\) attribute vertices. There are \(O(n^{8-t-s})\) ordered pairs of such copies and their combined edge event has probability \(p^{12-(1+t)s}\). Its power of \(n\) is \(2-t+(t-1)s/2\leq2\) in every case. For two rooted \(2\)-by-\(2\) copies the same exponent holds with \(t\in\{0,1\}\). Consequently a single row resampling has expected squared change \(O_c(n^2)\). Efron--Stein gives \(\operatorname{Var}(Z_n)=O_c(n^3)\). Thus
\[
\mathbb E\left|Z_n-\frac{n^2\lambda^2}{4}e^{-2\lambda}\right|=O_c(n^{3/2}).
\]

**5. Combine.** The exact partition in step 1 and the expectations and concentration estimates in steps 2--4 give
\[
\mathbb E|S_n-n^2F(c)|=O_c(n^{3/2}),
\]
where \(\Pr\{\operatorname{Poi}(\lambda)\geq3\}=1-e^{-\lambda}(1+\lambda+\lambda^2/2)\). Division by \(n^2\) proves the assertion.

## Verification

The accompanying standalone `verify.py` independently enumerates every binary incidence matrix of size at most \(4\)-by-\(4\). It constructs formal concepts by applying the Galois derivation operator to each candidate extent and compares the resulting five-way size partition with exact rational-probability formulas for \(p\in\{1/2,1/3,2/3\}\). All \(12\) matrix-size/probability comparisons pass; the largest case exhaustively examines \(65{,}536\) incidence matrices. In particular, it checks the nonobvious exact two-by-two maximality factor \((1-p^2)^{2(n-2)}\). These finite computations do not establish the asymptotic \(L^1\) estimate; that estimate follows from the proof above.

The exact expectation identity for any fixed \(n\) and \(p\) used as a cross-check is
\[
\mathbb E S_n=\sum_{a=0}^n\sum_{b=0}^n\binom na\binom nb p^{ab}(1-p^a)^{n-b}(1-p^b)^{n-a},
\]
with the usual convention for empty powers. This identity is prior literature and not claimed as new.

## Relationship to prior work

Felde--Hanika (2018), Sections 2--4, describe the independent coin-toss generation of formal contexts and emphasize the number of concepts as a null-model statistic; the model is prior work. Howlader--Liau (2023), Sections 2.2--3, introduce the two-sorted \(\mathbf{KF}\) window-modality semantics and its correspondence with formal concepts; these definitions and their correspondence are prior work. Kovács (2018), Section 2.1, gives a weighted expectation formula for concept counts in independent-incidence contexts. Sakurai (2021), Sections 3--5, gives an exact random-context expectation and a superpolynomial lower bound in a different, constant-density setting. Baudin--Magnien--Tabourier (2024) concerns enumeration algorithms and their complexity, not a probabilistic law for the fixed-point count. The 2009 MathOverflow discussion records the general exact expectation principle. The present claim is the critical scaling \(p=c/\sqrt n\), its explicit quadratic constant with a three-way maximal-rectangle decomposition, and a quantitative \(L^1\) law. The known expectation identities do not by themselves imply concentration. No claim of a novel concept-to-modal correspondence or of a novel exact general expectation identity is made.

## Limitations

This is a fixed-\(c\), balanced two-sort, independent-edge result; neither an almost-sure law nor a central limit theorem is claimed. Its finite checker supports exact finite identities but is not an infinite-size certificate. The possibility of an earlier equivalent law under maximal-biclique or random-closure terminology remains a literature risk. For \(p_n\) outside the critical square-root regime, a different asymptotic balance may apply.

## References

- M. Felde and T. Hanika, *Formal Context Generation using Dirichlet Distributions*, arXiv:1809.11160v1, first public 2018-09-28, Sections 2--4, precursor of Felde--Hanika--Stumme (2020). https://arxiv.org/abs/1809.11160
- M. Felde, T. Hanika, and G. Stumme, *Null Models for Formal Contexts*, *Information* **11** (2020), 135, DOI: 10.3390/info11030135 (MSC 03G10; 68T27). https://doi.org/10.3390/info11030135
- P. Howlader and C.-J. Liau, *Two-sorted Modal Logic for Formal and Rough Concepts*, arXiv:2309.04115v1, first public 2023-09-08, Sections 2.2--3. https://arxiv.org/html/2309.04115v1
- T. Sakurai, *On formal concepts of random formal contexts*, arXiv:2101.11023v1, first public 2021-01-26, Sections 3--5. https://arxiv.org/html/2101.11023v1
- L. Kovács, *Efficient approximation for counting of formal concepts generated from formal context*, Miskolc Mathematical Notes 19 (2018), 983--996, DOI: 10.18514/MMN.2018.2529, Section 2. https://real.mtak.hu/92004/1/2529.pdf
- A. Baudin, C. Magnien, and L. Tabourier, *BBK: a simpler, faster algorithm for enumerating maximal bicliques in large sparse bipartite graphs*, arXiv:2405.04428v1, 2024, Sections 1--6. https://arxiv.org/html/2405.04428v1
- M. Lugo et al., *What is the expected number of maximal bicliques in a random bipartite graph?*, MathOverflow discussion, 2009. https://mathoverflow.net/questions/473/what-is-the-expected-number-of-maximal-bicliques-in-a-random-bipartite-graph
