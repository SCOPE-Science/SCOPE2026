# Exact critical periodic content and sharp equidistribution for star-type subshifts

## Finding

Fix an integer \(q\ge2\), a contraction parameter \(0<r<1\), and the one-sided shift \((X_q,\sigma)\) over \(\{0,1,\ldots,q\}\) defined by forbidding consecutive nonzero symbols. Give it the prefix ultrametric \(d_r(x,y)=r^{\ell(x,y)}\) for distinct sequences, where \(\ell\) is their common-prefix length. Put
\[
\lambda=\frac{1+\sqrt{1+4q}}2,\qquad \tau=\frac{1-\sqrt{1+4q}}2,\qquad s=\frac{\log\lambda}{\log(1/r)}.
\]
For a finite periodic orbit \(\mathcal O\), denote its smallest pairwise distance by \(\eta(\mathcal O)\), and define its \(s\)-dimensional asymptotic periodic content by
\[
\mathfrak P^{s}(X_q,d_r,\sigma)=\lim_{M\to\infty}\sup\left\{|\mathcal O|\eta(\mathcal O)^s:\ \mathcal O\text{ is one periodic orbit},\ |\mathcal O|\ge M\right\}.
\]
**The critical periodic content is exactly \(\mathfrak P^s(X_q,d_r,\sigma)=\lambda\).** In particular, its periodic dimension is \(s\).

A finite extremal statement gives the mechanism. For every integer \(n\ge2\), the largest possible period of a cyclic admissible word whose cyclic length-\(n\) windows are all distinct is exactly
\[
P_n=\lambda^n+\tau^n.
\]
There is a primitive periodic orbit \(\mathcal O_n\) of period \(P_n\) and minimum gap \(r^{n-1}\); hence \(P_n\eta(\mathcal O_n)^s\to\lambda\).

Every choice of these maximizing orbits has the **same** empirical measure on each cylinder of length at most \(n\), independently of which Euler circuit constructs it. For an admissible word \(u=u_1\cdots u_k\), \(1\le k\le n\), the orbit measure \(\nu_n\) satisfies the exact formula
\[
\nu_n([u])=\frac{(A_q^{n-k+1})_{u_k,u_1}}{\lambda^n+\tau^n},
\]
where \(A_q\) is the adjacency matrix described below. Consequently, \(\nu_n\) converges to the maximum-entropy (Parry) measure \(\nu\), with cylinder error \(O_{q,k}((|\tau|/\lambda)^{n-k+1})\). The rate cannot be improved uniformly over cylinders: the one-symbol cylinder \([0]\) has the exact nonzero oscillating bias
\[
\nu_n([0])-\nu([0])=\frac{(\beta-\alpha)(\tau/\lambda)^n}{1+(\tau/\lambda)^n},\qquad
\alpha=\frac{\lambda^2}{\lambda^2+q},\quad \beta=\frac{\tau^2}{\tau^2+q}.
\]
Here \(\beta-\alpha<0\). For instance, for \(q=2\) the sharp content is \(2\), the extremal periods are \(2^n+(-1)^n\), and the one-symbol discrepancy is \(-(-1/2)^n/(3(1+(-1/2)^n))\).

## Assumptions and scope

The alphabet is \(\mathcal A_q=\{0,1,\ldots,q\}\). A finite or infinite word is **linearly admissible** when no two consecutive entries are both nonzero. A finite cyclic word is **cyclically admissible** when this also holds across its last-to-first boundary. The compact space \(X_q\) consists of one-sided infinite linearly admissible words; \(\sigma\) deletes the first coordinate. A primitive cyclic word \(w\) determines a periodic point \(w^\infty\) with orbit cardinality \(|w|\). The metric is zero on the diagonal, and otherwise is \(r^{\ell}\), with \(\ell\) the number of equal initial symbols before the first difference. Thus distinct first symbols have distance \(1\).

The \((q+1)\times(q+1)\) adjacency matrix has entries \((A_q)_{ij}=1\) if \(i=0\) or \(j=0\) and zero otherwise. Its eigenvalues are \(\lambda\), \(\tau\), and \(0\) with multiplicity \(q-1\). It is symmetric, irreducible and aperiodic. The theorem concerns this entire exact family, with fixed \(q\) and any \(r\in(0,1)\); it asserts no analogous numeric content for Euclidean metrics or arbitrary forbidden-word lists.

## Proof

**1. The exact finite upper bound requires cyclic admissibility.** Let \(n\ge2\). Form the usual overlap graph whose vertices are the linearly admissible words of length \(n-1\), and whose directed edges are the linearly admissible words \(w=w_1\cdots w_n\), from \(w_1\cdots w_{n-1}\) to \(w_2\cdots w_n\). Call an edge *good* when the extra closing transition \(w_n\to w_1\) is admissible, and *bad* otherwise. The good edges are precisely the cyclically admissible length-\(n\) words, so their number is the closed-path count
\[
|E_{\mathrm{good}}|=\operatorname{tr}(A_q^n)=P_n=\lambda^n+\tau^n.
\]
A bad edge starts and ends with a nonzero symbol. Since \(w_1\ne0\), linear admissibility forces \(w_2=0\). Partition vertices into \(U\), those whose first symbol is nonzero, and \(B\), those whose first symbol is zero. Every bad edge runs from \(U\) to \(B\). Every edge from \(B\) to \(U\) is good. Moreover, the map taking the cyclic word \(0au_3\cdots u_n\) to \(au_3\cdots u_n0\) is a bijection from edges \(B\to U\) to *good* edges \(U\to B\). Let \(R\) denote this common total number.

Consider any cyclically admissible orbit whose length-\(n\) windows are distinct. They trace a closed directed trail in the full overlap graph, using no edge twice. For every closed trail, the number of used \(U\to B\) edges equals the number of used \(B\to U\) edges and is at most \(R\). Thus its number of used bad edges is no greater than the number of **unused** good \(U\to B\) edges. Adding all its used good edges proves that its length is at most the total number \(P_n\) of good edges. This is the required finite **upper** bound; simply counting admissible linear blocks would give a larger, generally incorrect number.

**2. Sharp Eulerian construction and exact gap.** Restrict the overlap graph to its good edges. At any vertex \(v=v_1\cdots v_{n-1}\), its outgoing good edges correspond to symbols \(a\) satisfying \((v_{n-1},a)\) and \((a,v_1)\) admissible; its incoming good edges satisfy exactly the same two conditions. Hence indegree equals outdegree. Appending zeros repeatedly connects every vertex to \(0^{n-1}\) through good edges, while appending the letters of any vertex successively connects \(0^{n-1}\) to that vertex through good edges. All vertices have positive degree. The good-edge graph is therefore strongly connected and Eulerian.

An Euler circuit through all \(P_n\) edges yields a cyclic word whose length-\(n\) windows are exactly the cyclically admissible length-\(n\) words, each once. The word is necessarily primitive. Thus the associated orbit has \(P_n\) distinct points and no two points have a common prefix of length \(n\), giving \(\eta\ge r^{n-1}\).

To show equality, let \(W_m\) be the number of linearly admissible length-\(m\) words. Then \(W_0=1\), \(W_1=q+1\), and \(W_m=W_{m-1}+qW_{m-2}\). The trace counts satisfy the same recurrence, with \(P_1=1\) and \(P_2=1+2q\). Directly \(P_2-W_1=q\) and \(P_3-W_2=q\); their difference obeys the same positive recurrence thereafter. Therefore \(P_n>W_{n-1}\) for all \(n\ge2\). Among \(P_n\) orbit positions some length-\(n-1\) window repeats, so \(\eta=r^{n-1}\).

**3. Exact critical content.** Since \(r^s=\lambda^{-1}\), the constructed orbit gives
\[
P_n\eta(\mathcal O_n)^s=(\lambda^n+\tau^n)\lambda^{-(n-1)}\longrightarrow\lambda.
\]
Conversely, consider any periodic orbit of size at least \(q+2\), and let \(L\ge1\) be the largest common-prefix length among two distinct orbit points; thus \(\eta=r^L\). Its cyclic windows of length \(L+1\) must be distinct (otherwise two points agree for more than \(L\) symbols). By step 1 its size is at most \(P_{L+1}\). Consequently
\[
|\mathcal O|\eta(\mathcal O)^s\le (\lambda^{L+1}+\tau^{L+1})\lambda^{-L}=\lambda+\frac{\tau^{L+1}}{\lambda^L}.
\]
The prefix length \(L\) tends to infinity uniformly as orbit cardinality tends to infinity: an orbit with \(L<m\) has all length-\(m\) prefixes distinct, and there are only finitely many. As \(|\tau|<\lambda\), taking the tail supremum proves \(\mathfrak P^s\le\lambda\), hence equality. The same estimates at any exponent greater than \(s\) force zero content and, along the constructed orbit, any exponent smaller than \(s\) gives infinite content. This proves the critical dimension claim.

**4. Exact cylinder statistics.** In an Euler cycle each good length-\(n\) edge occurs once. A length-\(n\) cyclic word starting with an admissible prefix \(u_1\cdots u_k\) is a closed walk of length \(n\) in the adjacency graph; after fixing the first \(k-1\) transitions, precisely \((A_q^{n-k+1})_{u_k,u_1}\) choices remain. The stated cylinder formula follows upon division by \(P_n\).

Let \(v=(\lambda,1,\ldots,1)\) and \(w=(\tau,1,\ldots,1)\). They are mutually orthogonal eigenvectors of the real symmetric matrix \(A_q\). For each integer \(m\ge1\), its exact spectral decomposition is
\[
A_q^m=\lambda^m\frac{vv^{\mathsf T}}{\lambda^2+q}+\tau^m\frac{ww^{\mathsf T}}{\tau^2+q}.
\]
The Parry measure has cylinder masses \(\nu([u])=v_{u_1}v_{u_k}/((\lambda^2+q)\lambda^{k-1})\). Substituting the spectral decomposition into the exact cylinder formula proves convergence and the displayed exponential estimate. For \(k=1\), substitution yields the exact bias formula in the Finding section. Because \(|\tau|<\lambda\) and \(\alpha\ne\beta\), its first-order coefficient never vanishes; this proves sharpness of the spectral rate.

## Verification

The included standalone Python 3 file `verify.py` uses only the standard library. Run `python verify.py`. It reconstructs the good-edge overlap graph, checks degree balance, constructs Euler circuits and cyclic words, verifies that every good length-\(n\) word occurs exactly once, checks the exact period and gap, and matches cylinder frequencies to adjacency-matrix powers for \(q\in\{2,3,4\}\) and \(2\le n\le6\). A small exhaustive primitive-cycle census independently checks the finite upper bound for the binary-nonzero case, while rational arithmetic tests the alternating one-cylinder spectral discrepancy. The script has no external files or network dependencies. Its finite checks are diagnostics; the argument above is the proof for all allowed parameters.

## Relationship to prior work

Kong, Wang and Yu introduced periodic content and periodic dimension, and their homogeneous full-shift construction uses classical de Bruijn sequences. Their theorems do not give the exact critical content of this constrained star-type finite-state shift, nor the precise maximizing finite-window orbit bound or its sharp Parry-measure error. Restricted universal-cycle theory already covers the **existence** of a cyclic word containing every cyclically admissible length-\(n\) word once: after relabeling the distinguished zero as the largest alphabet symbol, the forbidden nonzero pairs can be handled by the substring-avoidance and intersection cases in Sawada–Williams–Wong (Sections 3.3.6 and 3.3.9). Thus that Eulerian existence is not claimed as new. The exact upper bound over **all** competing cycles additionally requires the good/bad cut balance, because linearly admissible windows that are not cyclically admissible may occur in a periodic word. The leading eigenvalue determines the content constant in the precise normalized prefix metric specified above; it is not asserted to be invariant under bi-Lipschitz changes of metric.

## Limitations

The theorem is for this symmetric star adjacency (one distinguished zero symbol and at least two nonzero symbols), exact prefix ultrametrics, and the one-sided shift. The result does not classify all maximizing orbit families, establish exact Euclidean critical content for a geometrically embedded attractor, or extend the constant unchanged to general mixing finite-type shifts. The exponential discrepancy estimate is for each fixed cylinder length. The proof uses no experimental inference to establish universal claims. Bibliographic novelty is based on inspected literature and is not an independent or exhaustive priority certification.

## References

1. D. Kong, Z. Wang, D. Yu, *Asymptotic separation of periodic orbits and fractal dimension*, arXiv:2609.16296v1, first posted 2026-09-14, Sections 1, 3, and 5. https://arxiv.org/abs/2609.16296
2. J. Sawada, A. Williams, D. Wong, *Generalizing the Classic Greedy and Necklace Constructions of de Bruijn Sequences and Universal Cycles*, Electronic Journal of Combinatorics 23(1), 2016, Paper P1.24. https://doi.org/10.37236/5517
3. K. B. Gardner, A. Godbole, *Universal Cycles of Restricted Words*, Journal of Combinatorial Mathematics and Combinatorial Computing 106 (2018), 153–173; arXiv:1711.07029. https://arxiv.org/abs/1711.07029
4. N. G. de Bruijn, *A combinatorial problem*, Proc. Koninklijke Nederlandse Akademie van Wetenschappen 49 (1946), 758–764.
