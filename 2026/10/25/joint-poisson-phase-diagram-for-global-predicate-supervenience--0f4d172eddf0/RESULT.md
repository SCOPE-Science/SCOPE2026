# Joint Poisson phase diagram for global predicate supervenience

## Finding

Fix integers \(r\ge2\) and \(1\le a<r\), and a real constant \(c>0\). Let \(D_n\) be an \(n\)-element set and \(W_n\) a set of \(m_n\) distinct worlds, where \(m_n2^{-na/2}\to c\). Each \(P_i\), for \(1\le i\le r\), is interpreted independently at each world as a uniformly random subset of \(D_n\). The worlds form one complete S5 cluster. For \(A\subseteq[r]\), let \(X_v(A)\) be the tuple of extensions of the predicates in \(A\) at world \(v\), and define

\[
C_A=\#\{\{u,v\}\subseteq W_n:u\ne v,\ X_u(A)=X_v(A)\}.
\]

Write \(A\rightsquigarrow B\) for global supervenience: for every \(u,v\in W_n\), equality \(X_u(A)=X_v(A)\) implies \(X_u(B)=X_v(B)\). Put \(\lambda=c^2/2\). The following hold as \(n\to\infty\):

1. The vector \((C_A: A\subseteq[r],\ |A|=a)\) converges jointly in distribution to \(\binom{r}{a}\) **independent** \(\mathrm{Poisson}(\lambda)\) variables.
2. With probability tending to one, **all** pairs \(A,B\subseteq[r]\) obey the classification
   \[
   A\rightsquigarrow B\quad\Longleftrightarrow\quad
   B\subseteq A\ \text{ or }\ |A|>a\ \text{ or }\ (|A|=a\ \text{ and }\ C_A=0).
   \]
3. Consequently the truth-indicators of the nontrivial statements with a given critical antecedent \(A\), \(|A|=a\), are perfectly synchronized, whereas indicators corresponding to distinct critical antecedents converge to **independent** \(\mathrm{Bernoulli}(e^{-\lambda})\) variables. The number of minimal determining predicate families of cardinality \(a\) converges to \(\mathrm{Binomial}(\binom{r}{a},e^{-\lambda})\). Here determining means \(A\rightsquigarrow[r]\), and minimal means no strict subset determines all predicates.

For example, with three predicates, at the threshold \(m_n\sim c2^{n/2}\), the three single-predicate determinant events converge to three independent coins of bias \(e^{-c^2/2}\), while every two-predicate family determines every predicate asymptotically surely.

## Assumptions and scope

The domain \(D_n\) is the same in every world; predicate extensions at different world–predicate positions are independent and uniform. Worlds are named distinct even if all their predicate extensions coincide. All asymptotics take \(n\to\infty\) while \(r,a,c\) are fixed, and all displayed probability statements concern this precise finite random-model distribution. All subset pairs \(A,B\) are included, including empty antecedents and consequents. The supervenience connective means equality of **entire predicate extensions across worlds**, not pointwise individual supervenience. The bound \(1\le a<r\) is essential to leave at least one predicate outside each critical family.

## Proof

**Step 1: collision moments.** Write \(q=2^n\) and \(m=m_n\); a predicate extension is one of \(q\) equiprobable values. Thus each world is an independent uniform vector in \([q]^r\). For any \(A\) with \(|A|=a\), the probability that two distinct worlds agree on \(A\) is \(q^{-a}\), and \(\mathbb E C_A=\binom{m}{2}q^{-a}\to\lambda\).

Fix any nonnegative integers \(k_A\) for the finitely many critical sets and put \(K=\sum_A k_A\). Expand the mixed factorial moment \(\mathbb E\prod_A(C_A)_{k_A}\), where \((x)_j=x(x-1)\cdots(x-j+1)\). Every term specifies \(K\) labelled unordered world-pairs, with distinct pairs **within** any one \(A\). Terms using \(2K\) distinct world indices contribute
\[
\frac{(m)_{2K}}{2^K}q^{-aK}\ \longrightarrow\ \lambda^K.
\]
For all other terms, form the graph whose vertices are the used world indices and whose edges are the prescribed pairs, marked by their \(A\)-labels. In any connected component with \(v\ge3\) vertices, a spanning tree forces at least \(a(v-1)\) coordinate equalities; its probability is at most \(q^{-a(v-1)}\). There are \(O(m^v)\) assignments, so its total weight is \(O(q^{a(1-v/2)})=o(1)\). A component consisting of two vertices with different \(A\)-labels imposes equality on at least \(a+1\) coordinates, with total weight \(O(m^2q^{-(a+1)})=O(q^{-1})\). All remaining two-vertex components are disjoint ordinary single edges. Since the number of edges is fixed, the complete contribution of non-disjoint or multiply marked terms tends to zero. Therefore every mixed factorial moment tends to \(\prod_A\lambda^{k_A}\), which is the mixed factorial moment array of independent Poisson variables. This proves claim 1 (including tightness via the first moments).

**Step 2: above and at the threshold.** For every \(H\subseteq[r]\) with \(|H|>a\),
\[
\Pr(C_H>0)\le\mathbb EC_H=\binom{m}{2}q^{-|H|}=o(1).
\]
There are finitely many such \(H\), so all of their collision counts vanish simultaneously with high probability. Thus antecedents larger than \(a\) determine everything. Further, for any critical \(A\), a pair of worlds equal on \(A\) disagrees on **every** predicate outside \(A\): if it did not, it would be counted by some vanishing \(C_{A\cup\{j\}}\). Hence for any \(B\not\subseteq A\), \(A\rightsquigarrow B\) holds iff \(C_A=0\), on this same high-probability event.

**Step 3: below the threshold.** Fix \(H\) with \(|H|=h<a\) and \(j\notin H\). Let \(Y_{H,j}\) count unordered pairs of worlds agreeing on \(H\) but disagreeing on predicate \(j\). Each pair contributes a Bernoulli variable of mean \(p=q^{-h}(1-q^{-1})\), and \(\mathbb EY_{H,j}=\binom{m}{2}p\to\infty\), since \(m^2q^{-h}\asymp q^{a-h}\). Contributions from distinct unordered pairs are pairwise independent even if the pairs share a world: condition on the shared world's entire vector; for each independent other world the conditional success probability is the constant \(p\). Thus \(\mathrm{Var}(Y_{H,j})\le\mathbb EY_{H,j}\), and Chebyshev gives \(\Pr(Y_{H,j}=0)\le1/\mathbb EY_{H,j}\to0\). Finiteness of \(r\) gives the statement simultaneously for every such \(H,j\). Every nontrivial implication \(H\rightsquigarrow B\) fails, choosing any \(j\in B\setminus H\). Trivial implications \(B\subseteq H\) always hold. This proves claim 2.

**Step 4: the entire table and minimal families.** By claim 1 and the fact that the boundary of the coordinatewise zero event has no Poisson mass at half-integers, the vector \((\mathbf1\{C_A=0\}:|A|=a)\) converges to independent Bernoulli variables of parameter \(e^{-\lambda}\). Claim 2 identifies these with the complete critical truth table. Every strict subset of a critical \(A\) is asymptotically not a determinant, so a critical \(A\) is a minimal determinant exactly when \(C_A=0\). Summing the limiting Bernoulli variables gives claim 3.

## Verification

The accompanying `checker.py` uses exhaustive finite enumeration for \(q\in\{2,3\}\), \(r\in\{2,3\}\), and selected world counts \(m\in\{2,3,4\}\). On each enumerated table, it evaluates all global-supervenience implications directly, checks the exact finite deterministic classification whenever the high-probability conditions of Steps 2–3 hold, and independently checks first and cross second collision moments against closed formulas. Across nine parameter combinations it processes 49,391 tables and reports `ALL_CHECKS_OK`. These finite checks do not prove joint Poisson convergence; the factorial-moment argument above does.

## Relationship to prior work

Ciardelli (2025) introduces the exact constant-domain predicate-extension notion of global supervenience and proves its expressibility in inquisitive modal predicate logic, together with compactness and recursive enumerability. Ciardelli and Conti (2026) give labelled sequent proof theory for that logical system. Neither inspected work supplies a stochastic supervenience law. Crucially, Demetrovics, Katona, Miklós, Seleznjev and Thalheim (1998) already establish asymptotic **single** functional-dependency and key probabilities for random databases using Poisson approximation. Their marginal result encompasses the single-critical-family birthday-law component after an appropriate translation. The contribution claimed here is specifically the **joint asymptotic independence of all critical antecedents at once and the complete simultaneous supervenience-table/minimal-family limit**, not the familiar marginal collision approximation. The first two sources concern logic; the third is the closest mathematical precursor.

## Limitations

No universality is claimed for correlated predicates, nonuniform extensions, growing \(r\), or non-complete accessibility relations. The marginal Poisson approximation is old; independent priority assessment of the new joint profile is outstanding. The available indexed copy of the 1998 paper exposed its definitions, theorems, and proof passages but not a reliable complete contiguous transcription; an undiscovered multivariate extension in that work or related older database literature remains a priority risk. Independent audit has not been performed.

## References

- Ivano Ciardelli, *Global Supervenience in Inquisitive Modal Logic*, *Review of Symbolic Logic* **18** (2025), 589–615, DOI `10.1017/S175502032500005X`, public March 12, 2025. Open-access full text: https://www.research.unipd.it/retrieve/a76286b8-592a-484e-ad88-3f33f35caff3/global-supervenience-in-inquisitive-modal-logic.pdf
- Ivano Ciardelli and Simone Conti, *Labelled Sequents for Inquisitive First-Order Modal Logic*, *Electronic Proceedings in Theoretical Computer Science* **447** (2026), 242–261, arXiv `2606.31868`, public June 30, 2026. https://arxiv.org/abs/2606.31868
- J. Demetrovics, G. O. H. Katona, D. Miklós, O. Seleznjev and B. Thalheim, *Asymptotic Properties of Keys and Functional Dependencies in Random Databases*, *Theoretical Computer Science* **190** (1998), 151–166, DOI `10.1016/S0304-3975(97)00089-3`. https://doi.org/10.1016/S0304-3975(97)00089-3
