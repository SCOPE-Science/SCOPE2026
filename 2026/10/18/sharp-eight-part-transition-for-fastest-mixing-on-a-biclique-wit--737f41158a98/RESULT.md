# Sharp eight-part transition for fastest mixing on a biclique with one deleted edge

## Finding

Let \(m\ge 2\) be an integer and let \(G_m\) be the graph obtained by deleting exactly one edge from \(K_{m,m}\). Consider **all** real, symmetric, entrywise-nonnegative stochastic matrices \(P\) with off-diagonal support contained in the edges of \(G_m\); nonnegative holding probabilities are allowed. Minimize the second-largest eigenvalue modulus
\[
\mu(P)=\left\|P-\frac{1}{2m}\mathbf 1\mathbf 1^{\mathsf T}\right\|_2.
\]
The global minimum is
\[
\boxed{\mu_m^*=\begin{cases}
1/\sqrt m,&2\le m\le7,\\
\dfrac{m-2}{2m-2+\sqrt{m^2-8m+8}},&m\ge8.
\end{cases}}
\]
A fastest-mixing matrix exists that assigns the same probability \(x_m\) to all \((m-1)^2\) edges joining vertices other than the deleted edge's two endpoints, and the same probability \(y_m\) to all \(2(m-1)\) remaining edges incident to an endpoint. These probabilities are
\[
\boxed{(x_m,y_m)=\begin{cases}
\left(\dfrac{1}{2(m-1)},\dfrac1m\right),&2\le m\le7,\\[5pt]
\left(\dfrac{m-2+s_m}{(m-1)(2m-2+s_m)},\dfrac2{2m-2+s_m}\right),&m\ge8,
\end{cases}\quad s_m=\sqrt{m^2-8m+8}.}
\]
This is the **unique fastest-mixing graph-automorphism-invariant matrix**. No uniqueness assertion is made about arbitrary nonsymmetric-in-the-graph-sense optimal edge allocations (all feasible matrices are symmetric as matrices). For \(m\ge8\), the deletion penalty relative to the complete biclique is exactly
\[
\mu_m^*-\frac13=\frac{8}{3(2m-2+s_m)(m-4+s_m)}>0,
\qquad\lim_{m\to\infty}m^2\left(\mu_m^*-\frac13\right)=\frac49.
\]
The \(m=2\) path instance is already covered by the classical fastest-mixing path theorem; the substantive classification and the sharp structural transition are for \(m\ge3\).

## Assumptions and scope

Fix two vertex parts \(U=\{u_0,\ldots,u_{m-1}\}\) and \(V=\{v_0,\ldots,v_{m-1}\}\). Only \(u_0v_0\) is absent. All other cross-part edges and all diagonal holding loops may carry independently chosen nonnegative probabilities. Within-part transitions between distinct vertices are forbidden. The chain has uniform stationary distribution because \(P=P^{\mathsf T}\) and \(P\mathbf1=\mathbf1\). The minimization is over the full, unrestricted convex feasible set, **not** only invariant transition matrices.

An invariant kernel has exactly two edge probabilities \(x,y\). Write \(r=m-1\). Its special-vertex holding probability is \(1-r y\), its other-vertex holding probability is \(1-rx-y\), and its feasibility region is
\[
x\ge0,\qquad y\ge0,\qquad r y\le1,\qquad r x+y\le1.
\]
When \(m=2\), the within-ordinary-class eigenspace below has dimension zero.

## Proof

**1. Reduction from all edge allocations.** The automorphism group contains independent permutations of the \(r\) ordinary vertices in each part, together with the exchange of the two parts and their marked endpoints. Averaging an arbitrary feasible matrix over this group gives an invariant feasible matrix. The function \(P\mapsto\|P-\mathbf1\mathbf1^{\mathsf T}/(2m)\|_2\) is convex and invariant under permutation conjugation. Thus some global optimizer has edge probabilities \(x,y\). This averages only feasible matrices; no unproved uniqueness of unrestricted optimizers is used.

**2. Exact spectral decomposition.** Differences within either ordinary \(r\)-vertex class have eigenvalue \(z=1-rx-y\), with total multiplicity \(2(r-1)\). The part-exchange-even quotient has eigenvalues \(1\) and \(g=1-my\). On the two-dimensional part-exchange-odd quotient, using normalized ordinary-vertex sums, the matrix is
\[
E(x,y)=\begin{pmatrix}
1-r y&-\sqrt r\,y\\
-\sqrt r\,y&1-2r x-y
\end{pmatrix}.
\]
Consequently, for \(m\ge3\),
\[
\mu(x,y)=\max\bigl\{|z|,\,|g|,\,\lambda_{\max}(E),\,-\lambda_{\min}(E)\bigr\};
\]
for \(m=2\), omit the absent \(|z|\) term. The two extreme-eigenvalue functions are convex in \((x,y)\).

**3. Sharp lower bound for \(2\le m\le7\).** The first-column norm of \(E\) implies
\[
\|E\|_2^2\ge (1-r y)^2+r y^2
=\frac1m+mr\left(y-\frac1m\right)^2\ge\frac1m.
\]
Choose \(y=1/m\) and \(x=1/(2r)\). Then \(\operatorname{tr}E=0\), \(E^2=I/m\), and \(g=0\). The remaining eigenvalue is \(z=(m-2)/(2m)\), which does not exceed \(1/\sqrt m\) for every integer \(2\le m\le7\). Both holding probabilities are nonnegative. This proves sharpness. If equality holds, the column-norm inequality forces \(y=1/m\); equality between the first-column norm and the operator norm, together with the nonzero off-diagonal entry, forces \(E^2\) to be diagonal, hence \(\operatorname{tr}E=0\) and \(x=1/(2r)\). Therefore the invariant optimizer is unique.

**4. Candidate for \(m\ge8\).** Set \(s=\sqrt{m^2-8m+8}\), \(D=2r+s\), and
\[
\quad x=\frac{m-2+s}{rD},\qquad y=\frac2D,\qquad t=\frac{m-2}{D}.
\]
Since \(s>2\) and \(s<m\), the probabilities are feasible. Substitution gives
\[
z=t,\qquad g=\frac{s-2}{D}\in[0,t),\qquad
E=\begin{pmatrix}s/D&-2\sqrt r/D\\-2\sqrt r/D&-s/D\end{pmatrix},
\]
so \(E^2=t^2I\), by \(s^2+4r=(m-2)^2\). The candidate therefore has \(\mu=t\).

**5. Global optimality and invariant uniqueness for \(m\ge8\).** Define three convex lower bounds on the objective:
\[
f_0(x,y)=1-rx-y,\qquad f_+(x,y)=\lambda_{\max}(E),\qquad f_-(x,y)=-\lambda_{\min}(E).
\]
At the candidate, all three equal \(t\). Define the positive coefficients
\[
\alpha=\frac{2r(s-2)}{sD},\qquad
\beta=\frac{m(m-s)}{2sD},\qquad
\gamma=\frac{m+s}{2D}.
\]
They sum to one. For complete reproducibility of the subgradient certificate, set \(q=s/(m-2)\) and \(K=2r/(m-2)-(m-2)q/2\). Direct differentiation of the two simple eigenvalues of \(E\) at the candidate gives
\[
\nabla f_0=(-r,-1),\quad
\nabla f_+=\left(-r(1-q),-\frac m2+K\right),\quad
\nabla f_-=\left(r(1+q),\frac m2+K\right).
\]
Substituting the displayed coefficients and the identity \(s^2=m^2-8m+8\) yields
\[
\alpha\nabla f_0+\beta\nabla f_++\gamma\nabla f_-=0.
\]
Therefore the convex function \(\alpha f_0+\beta f_++\gamma f_-\) has global minimum \(t\), and **every** invariant feasible pair has \(\mu\ge\alpha f_0+\beta f_++\gamma f_-\ge t\). Group averaging extends this lower bound to every unrestricted feasible matrix. All three coefficients are strictly positive. Any invariant optimizer must consequently satisfy \(f_0=f_+=f_-=t\). The last two equalities give \(\operatorname{tr}E=0\), or \(2rx+my=2\); together with \(f_0=t\), they imply \(y=2t/(m-2)\) and the uniquely specified \(x\). This proves invariant uniqueness.

**6. Sharp transition and deletion penalty.** The column-norm lower bound is attained with admissible remaining modes precisely through \(m=7\), since \((m-2)/(2m)\le1/\sqrt m\) there. From \(m=8\) onward, the displayed strictly positive three-way subgradient certificate proves the alternative branch. The complete biclique has known optimal SLEM \(1/3\), whereas rationalizing \(m-4-s=8/(m-4+s)\) gives the exact positive deletion penalty and the asymptotic coefficient in the finding.

## Verification

The accompanying `verify.py` independently constructs the full \(2m\)-vertex transition matrix (without employing the invariant quotient in its construction), diagonalizes it numerically, and compares its spectrum against the four-block formula. It additionally checks rational low-branch identities, exact symbolic high-branch identities and subgradient cancellations for integer dimensions, as well as thousands of independently sampled feasible edge-orbit allocations. Execute with `python verify.py` after installing the dependencies in `requirements.txt`. The finite checks do **not** constitute the proof for all \(m\); the displayed spectral and convexity arguments supply the infinite-family proof.

## Relationship to prior work

Boyd, Diaconis and Xiao (2004) established the general semidefinite formulation and solved the **unmodified** complete bipartite graph, including the balanced value \(1/3\). Boyd, Diaconis, Sun and Xiao (2006) solved paths, which covers the \(m=2\) case here. Boyd, Diaconis, Parrilo and Xiao (2007 preprint; 2009 journal) gave general automorphism-based reductions and solved several graph families, including complete bipartite graphs and two complete cliques joined by a bridge. The single-deleted-edge biclique has a different two-edge-orbit quotient: the exact seven/eight transition, formulas, and deletion penalty above are not among the statements in the inspected relevant sections. General geometric fastest-mixing bounds of Olesker-Taylor and Zanetti (2021) are of a different quantitative form and do not give these exact finite-graph optimizers. The general symmetry and convexity machinery is established prior work, not claimed as new.

## Limitations

The objective is specifically second-largest **absolute** eigenvalue for symmetric uniform-stationary chains, with independently assignable nonnegative edge/loop probabilities. It is not total-variation mixing time, nonreversible optimization, or a prescribed nonuniform stationary law. The theorem proves uniqueness **within graph-automorphism-invariant kernels**; it does not classify every non-invariant optimal matrix. A search of inspected sources cannot prove absolute novelty against all specialized or unindexed literature. The case \(m=2\) is a known path special case.

## References

1. S. Boyd, P. Diaconis, L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review **46** (2004), 667–689. DOI: `10.1137/S0036144503423264`. Public full text: https://www.stat.berkeley.edu/~aldous/206-RWG/RWGpapers/boyd.pdf .
2. S. Boyd, P. Diaconis, J. Sun, L. Xiao, *Fastest Mixing Markov Chain on a Path*, American Mathematical Monthly **113** (2006), 70–74. DOI: `10.1080/00029890.2006.11920281`. Public abstract: https://www.web.stanford.edu/~boyd/papers/fmmc_path.html .
3. S. Boyd, P. Diaconis, P. A. Parrilo, L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, arXiv:0709.0955v1, first posted 2007-09-06; SIAM J. Optim. **20** (2009), 792–819. https://arxiv.org/pdf/0709.0955 .
4. S. Olesker-Taylor, L. Zanetti, *Geometric Bounds on the Fastest Mixing Markov Chain*, arXiv:2111.05816v1 (2021). https://arxiv.org/pdf/2111.05816 .
