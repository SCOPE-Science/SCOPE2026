# A single-pair versus multi-pair price threshold for spectral-gap design of complete graphs

## Finding

Let \(n\ge4\) and fix any matching \(M\) of \(k\) disjoint edges in the complete graph \(K_n\), with \(1\le k\le\lfloor n/2\rfloor\). Edges in \(M\) cost \(P>0\) per unit conductance and all other edges cost \(Q>0\). Choose every conductance \(w_e\ge0\) independently under \(\sum_{e\in M}Pw_e+\sum_{e\notin M}Qw_e\le B\), where \(B>0\). Write \(\lambda_2(L(w))\) for the second-smallest eigenvalue of the unnormalized weighted graph Laplacian.

Set \(r=P/Q\) and
\[
 r_c(n,k)=\begin{cases}2(n-1)/(n-2),&k=1,\\2,&k\ge2.\end{cases}
\]
Then, without restricting the individual conductances to symmetric allocations,
\[
 \boxed{\max_w\lambda_2(L(w))=\frac{B}{Q\left[\frac{n-1}{2}+\frac{k}{n}(\min\{r,r_c(n,k)\}-1)\right]}.}
\]
For \(r<r_c(n,k)\), the **unique** optimizer assigns equal positive conductance to every edge. For \(r>r_c(n,k)\), **every** optimizer deletes all \(k\) priced matching edges (sets their conductances to zero). At the boundary \(r=r_c(n,k)\), both the uniform and an explicit matching-deleted allocation are optimal, as are all their convex combinations. In particular, one priced pair has a larger threshold \(2(n-1)/(n-2)>2\), whereas every matching of size at least two has the dimension-independent sharp threshold \(2\).

## Assumptions and scope

The graph is undirected and complete before assigning weights, the designated costly edges form a matching, prices are constant on each of the two edge classes, conductances may be zero, and the objective is the unnormalized **continuous-time** Laplacian spectral gap. No discrete-time Markov-kernel row-stochasticity or upper conductance bounds are assumed. The budget is linear and exhausted at every optimum. Vertex labels are arbitrary, and the statement covers all integers \(n\ge4\), \(1\le k\le\lfloor n/2\rfloor\) and all real \(P,Q,B>0\).

For unit-gap normalization, let \(e_i\) be the coordinate vectors, \(b_{ij}=e_i-e_j\), \(L(w)=\sum_{i<j}w_{ij}b_{ij}b_{ij}^{\mathsf T}\), and \(\Pi=I-\mathbf1\mathbf1^{\mathsf T}/n\). The constraint \(\lambda_2(L(w))\ge1\) is exactly \(L(w)\succeq\Pi\). Since \(\lambda_2\) is positively homogeneous, minimizing the price of a unit-gap Laplacian gives the asserted optimum at budget \(B\).

## Proof

**1. An explicit feasible dual matrix.** Let \(A_M\) be the adjacency matrix of the matching, with zeros at unmatched vertices. For \(s>0\) define
\[
G_s=\frac12I+\frac{1-s}{2}A_M,\qquad X_s=\Pi G_s\Pi.
\]
For every edge \(e=\{i,j\}\), the vector \(b_e\) is orthogonal to \(\mathbf1\), so
\[
 b_e^{\mathsf T}X_sb_e=b_e^{\mathsf T}G_sb_e=
 \begin{cases}s,&e\in M,\\1,&e\notin M.\end{cases}
\]
Furthermore,
\[
\operatorname{tr}X_s=\operatorname{tr}G_s-\frac{\mathbf1^{\mathsf T}G_s\mathbf1}{n}
=\frac{n-1}{2}+\frac{k}{n}(s-1).
\]
We next determine precisely when \(X_s\succeq0\).

For \(k\ge2\), every marked pair supports a difference vector of eigenvalue \(s/2\) for \(G_s\) and a sum vector of eigenvalue \((2-s)/2\); unmatched coordinates have eigenvalue \(1/2\). Thus \(X_s\) is positive definite on \(\mathbf1^\perp\) for \(0<s<2\), and positive semidefinite at \(s=2\). If \(s>2\), the contrast between two disjoint pair-sum vectors is in \(\mathbf1^\perp\) and has negative quadratic form. The sharp endpoint is \(r_c=2\).

For \(k=1\), let the marked endpoints be the first two vertices and put \(\ell=n-2\). The space \(\mathbf1^\perp\) is the orthogonal sum of (i) the endpoint-difference line, where the quadratic form of \(G_s\) has eigenvalue \(s/2\); (ii) the \(\ell-1\)-dimensional contrast space of unmatched vertices, with eigenvalue \(1/2\); and (iii) the line of vectors with both endpoint entries \(a\) and all unmatched entries \(-2a/\ell\), on which the quadratic form equals \((2+2/\ell-s)a^2\). Consequently \(X_s\) is positive definite on \(\mathbf1^\perp\) precisely when \(0<s<2+2/\ell\), and positive semidefinite at the endpoint \(r_c=2(n-1)/(n-2)\). The last line makes the quadratic form negative for larger \(s\).

**2. The universal price bound.** Divide prices by \(Q\), let \(s=\min\{r,r_c(n,k)\}\), and take any admissible unit-gap weights. The edge lengths above satisfy \(b_e^{\mathsf T}X_sb_e\le r\) for marked edges and equal \(1\) otherwise. Thus, using positive semidefiniteness of \(X_s\),
\[
\sum_e\frac{c_e}{Q}w_e\ge\sum_e w_eb_e^{\mathsf T}X_sb_e
=\operatorname{tr}(X_sL(w))
\ge\operatorname{tr}(X_s\Pi)
=\frac{n-1}{2}+\frac{k}{n}(s-1).
\]
The inequality \(\operatorname{tr}(X_s(L(w)-\Pi))\ge0\) follows because both factors are positive semidefinite. This gives the lower bound on the minimum unit-gap cost.

**3. Uniform optimality below the threshold.** Give *every* edge conductance \(1/n\). The resulting Laplacian is \(\Pi\); its gap is exactly one, and its normalized cost is \((n-1)/2+(k/n)(r-1)\), matching the dual bound whenever \(r\le r_c\). When \(r<r_c\), the dual \(X_r\) is positive definite on \(\mathbf1^\perp\). Equality in the trace inequality forces \(L(w)=\Pi\): a positive semidefinite difference with zero pairing against a positive definite dual must vanish on that space, and both Laplacians annihilate \(\mathbf1\). Since \(K_n\) has distinct off-diagonal entries \(L_{ij}=-w_{ij}\), this forces all \(w_{ij}=1/n\). Therefore the optimizer is unique.

**4. Optimal complete deletion of the matching.** At and above the threshold, the following conductance assignments attain the dual lower bound while giving gap one.

For \(k\ge2\), set all \(k\) matching-edge weights to zero. Put \(\ell=n-2k\). Give an edge between vertices from **different marked pairs** weight \(k/((k-1)n)\), and give every other unmarked edge weight \(1/n\) (including all edges incident to unmatched vertices). Pair-difference eigenvectors have Laplacian eigenvalue \(1\) with multiplicity \(k\). Pair-mean contrasts have eigenvalue \(1+2k/((k-1)n)\) with multiplicity \(k-1\). If \(\ell\ge1\), the pair-versus-unmatched contrast has eigenvalue \(1\); if \(\ell\ge2\), unmatched-vertex contrasts give another \(\ell-1\) eigenvalues equal to \(1\). Together with the constant zero eigenvector these span \(\mathbb R^n\), proving \(\lambda_2=1\). Counting edge weights gives normalized price \((n-1)/2+k/n\), the dual bound at \(r_c=2\).

For \(k=1\), put \(\ell=n-2\), delete the marked edge, give each of the \(2\ell\) edges between its endpoints and the unmatched vertices conductance \(1/\ell\), and give each edge among unmatched vertices conductance \((\ell-2)/\ell^2\). These weights are nonnegative even when \(\ell=2\). The Laplacian has eigenvalues \(0\), \(1\) with multiplicity \(\ell\), and \(n/\ell\) with multiplicity one, hence gap one. The normalized price is \((n-1)/2+1/(n-2)\), exactly the dual bound at \(r_c=2+2/(n-2)\).

When \(r>r_c\), the first inequality of step 2 has *strict* slack \((r-r_c)\sum_{e\in M}w_e\). At optimality equality holds throughout, so every optimizer must satisfy \(w_e=0\) on all matching edges. At \(r=r_c\), both distinct allocations have the same minimum cost and satisfy \(L\succeq\Pi\). The feasible unit-gap set is convex, so every convex combination is also optimal. Scaling all unit-gap weights by \(B/C_*\), where \(C_*\) is the asserted unit-gap price, exhausts the budget and completes the proof.

## Verification

The bundled standalone script `verify.py` uses Python's exact rational arithmetic. For each \(4\le n\le18\) and each admissible matching size, it constructs the dual and the deletion-design Laplacian directly from the formulas, checks all edge-dual lengths and dual traces, verifies a complete explicit Laplacian eigenbasis and exact unit-gap costs, and compares uniform certificates at several rational prices. It executes 35,388 exact rational assertions. Run `python verify.py` from the extracted package directory. Finite checks confirm the calculations in the covered instances; the proof in the previous section establishes the general statement for every admissible \(n,k,r\).

## Relationship to prior work

Sun, Boyd, Xiao and Diaconis (2006) formulate the general fastest-mixing continuous-time Markov-process problem as an algebraic-connectivity semidefinite program and derive an embedding/dual interpretation. Their published treatment provides the dual framework but not the present closed all-parameter matching-price threshold, the dimension-independent multi-pair boundary or the assertion that all expensive matched edges disappear in every optimizer. Boyd, Diaconis, Parrilo and Xiao (2007) develop group symmetry reductions for a *discrete-time* second-largest-eigenvalue-modulus problem and treat uniform complete graphs, rather than two priced edge classes in the continuous-time budgeted problem. Ghosh and Boyd (2006) study upper bounds on unweighted graph algebraic connectivity via convex optimization of graph families; that graph-selection setting does not give the two-price conductance formula here. The novel content asserted here is the explicit matching-size-dependent pricing law and its sharp optimizer rigidity/screening classifications; the general SDP and duality tools are prior art.

## Limitations

The theorem applies only to complete graphs with a *matching* as the distinguished price class and two homogeneous linear edge prices. It neither classifies every possible optimizer at or above the threshold nor covers intersecting costly edges, arbitrary per-edge prices, discrete-time spectral modulus, or robustness/conditioning. Searching relevant literature cannot eliminate the residual possibility of an unlocated equivalent specialist theorem.

## References

1. J. Sun, S. Boyd, L. Xiao, and P. Diaconis, *The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem*, SIAM Review 48 (2006), 681–699. Published online 2006-11-02. DOI: 10.1137/S0036144504443821. Open full text: https://web.stanford.edu/~boyd/papers/pdf/fmmp.pdf.
2. S. Boyd, P. Diaconis, P. A. Parrilo, and L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, arXiv:0709.0955v1 (2007-09-06), https://arxiv.org/pdf/0709.0955.
3. A. Ghosh and S. Boyd, *Upper Bounds on Algebraic Connectivity via Convex Optimization*, Linear Algebra and its Applications 418 (2006), 693–707, https://web.stanford.edu/~boyd/papers/eigbounds_laplacian.html.
