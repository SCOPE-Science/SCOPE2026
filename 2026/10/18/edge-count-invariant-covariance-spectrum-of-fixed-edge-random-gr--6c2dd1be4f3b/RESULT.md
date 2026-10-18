# Edge-count invariant covariance spectrum of fixed-edge random-graph degree histograms

## Finding
Fix an integer \(n\ge4\), write \(s=n-1\), \(M=\binom n2\) and \(t=M-s\), and uniformly sample a graph \(G\) with vertex set \(\{1,\ldots,n\}\) and exactly \(m\) edges, where \(1\le m\le M-1\). Let \(H_k\) count vertices of degree \(k\), and let \(\pi_k=\Pr\{\deg_G(1)=k\}=\binom{s}{k}\binom{t}{m-k}/\binom{M}{m}\). The nonzero support is \(I=\{\ell,\ldots,u\}\), where \(\ell=\max(0,m-t)\), \(u=\min(s,m)\), and \(r=u-\ell\). Write \(P=\operatorname{diag}(\pi_k:k\in I)\) and \(\Sigma=\operatorname{Cov}((H_k)_{k\in I})\).

**Theorem.** The exact eigenvalue multiset of \(P^{-1/2}\Sigma P^{-1/2}\) is \(\{0,0\}\cup\{\lambda_j:2\le j\le r\}\) when \(r\ge1\). If \(r=0\), its sole eigenvalue is zero. For \(2\le j\le r\),
\[
\lambda_j=n\left[1+(n-1)\rho_j\right],\qquad
\rho_j=(-1)^j\frac{(s-1)_{\underline j}}{t_{\underline j}}+(-1)^{j-1}\frac{j(s-1)_{\underline{j-1}}}{s\,t_{\underline{j-1}}}.
\]
Here \((a)_{\underline j}=a(a-1)\cdots(a-j+1)\) and \((a)_{\underline 0}=1\). In particular **every nonzero eigenvalue is independent of the prescribed edge count \(m\)**, even though the hypergeometric degree weights \(\pi_k\) depend on \(m\). The spectrum simply truncates at the supported polynomial degree \(r\). The two displayed zero eigenvalues for \(r\ge1\) correspond to the deterministic constraints \(\sum_kH_k=n\) and \(\sum_kkH_k=2m\).

More precisely, let \(Q_0,\ldots,Q_r\) be any sequence of orthonormal polynomials on \(I\) with respect to \(\pi\), with \(\deg Q_j=j\). The vectors \((\sqrt{\pi_k}Q_j(k))_{k\in I}\) are an orthonormal eigenbasis, with eigenvalue zero for \(j=0,1\) and \(\lambda_j\) for \(j\ge2\). Thus for every real-valued score \(f\) on \(I\), writing its orthogonal expansion \(f=\sum_{j=0}^r c_jQ_j\), one has the sharp exact variance identity
\[
\operatorname{Var}\!\left(\sum_{v=1}^{n}f(\deg_G(v))\right)
=\sum_{j=2}^{r}\lambda_jc_j^2.
\]
An empty sum equals zero. These identities are finite-sample statements, not asymptotic approximations or chi-square distribution claims.

## Assumptions and scope
Graphs are simple, undirected, and labeled. The edge set is uniform among all \(m\)-subsets of the \(M\) possible edges; edges are **not** independent. For \(n\ge4\) we have \(t\ge s\), ensuring that all falling-factorial denominators occurring at \(j\le r\le s\) are positive. The cases \(m=0\) and \(m=M\) yield deterministic histograms and a zero covariance matrix after restriction to their singleton support. All assertions above refer to the supported degree histogram, so \(P^{-1/2}\) is well-defined.

## Proof
Fix distinct vertices \(v,w\), and put \(X=\deg_G(v)\) and \(Y=\deg_G(w)\). Their incident-edge sets each have size \(s\) and overlap in exactly one possible edge. Conditional on \(X=x\), the set of \(x\) selected edges incident with \(v\) is uniform; the remaining \(m-x\) edges form an independent uniform subset of the \(t=M-s\) edges not incident with \(v\). Consequently
\[
Y=Z+W,\qquad Z\sim\operatorname{Bernoulli}(x/s),\quad W\sim\operatorname{Hypergeom}(t,s-1,m-x),
\]
where \(Z,W\) are conditionally independent given \(X=x\). For any integer \(0\le j\le s\), the falling-factorial identity \((z+w)_{\underline j}=(w)_{\underline j}+jz(w)_{\underline{j-1}}\) for \(z\in\{0,1\}\) gives
\[
\mathbb E[(Y)_{\underline j}\mid X=x]
=\frac{(s-1)_{\underline j}(m-x)_{\underline j}}{t_{\underline j}}
+\frac{jx}{s}\frac{(s-1)_{\underline{j-1}}(m-x)_{\underline{j-1}}}{t_{\underline{j-1}}},
\]
with the second term omitted at \(j=0\). This polynomial in \(x\) has degree at most \(j\); its coefficient of \(x^j\) is exactly \(\rho_j\) given above (for \(j=0\), it is \(1\)).

Define \((Tf)(x)=\mathbb E[f(Y)\mid X=x]\) on \(L^2(I,\pi)\). Symmetry under swapping \(v,w\) makes \((X,Y)\) exchangeable, so \(T\) is self-adjoint with respect to \(\langle f,g\rangle_\pi=\sum_k\pi_kf(k)g(k)\). The factorial-moment calculation shows that \(T\) preserves polynomials of degree at most \(j\). If \(Q_j\) is orthogonal to all lower-degree polynomials, self-adjointness makes \(TQ_j\) orthogonal to all such polynomials. Since it also has degree at most \(j\), it must be a scalar multiple of \(Q_j\); comparing leading coefficients gives \(TQ_j=\rho_jQ_j\).

For any two degree scores \(f,g\), exchangeability of graph vertices implies
\[
\operatorname{Cov}\left(\sum_vf(\deg_G(v)),\sum_vg(\deg_G(v))\right)
=n\operatorname{Cov}(f(X),g(X))
+n(n-1)\operatorname{Cov}(f(X),g(Y)).
\]
Applying this to the orthonormal functions \(Q_j\), the constant \(Q_0\) has zero covariance, while each \(j\ge1\) produces variance \(n[1+(n-1)\rho_j]\). Directly \(\rho_1=1/s-(s-1)/t=-1/(n-1)\), so \(j=1\) is the second zero mode. Finally \(\sum_v f(\deg_G(v))=\sum_kf(k)H_k\), which identifies the weighted covariance matrix eigenvectors and proves the variance identity. No unproved asymptotic passage is needed.

## Verification
The included standalone Python program `verify.py` compares two independent exact-rational calculations for every allowed \(m\) and \(n\in\{4,5,6\}\): (i) direct enumeration of all labeled \(m\)-edge graphs, and (ii) an explicit triple-region hypergeometric joint law for two degrees. It constructs the polynomial eigenvectors by rational Gram–Schmidt and checks the full diagonalization including both null modes. The program returned `VERIFY_OK` in 56 independent test cases. These finite checks supplement but do not replace the proof above.

## Relationship to prior work
Liebenau and Wormald study the complete degree sequence of \(G(n,m)\) and establish an **asymptotic**, rather than exact finite-sample, approximation by conditioned binomial variables. Their degree-sequence result does not state the edge-count-invariant weighted covariance eigenvalues here. Lin and Reinert treat degree-count covariances for **independent-edge** random graphs, which do not directly provide the covariance matrix under a fixed total edge count. Van der Hofstad, Komjáthy and Vadon demonstrate the importance of empirical degree distributions for random-network models, but their model is a random intersection graph with community structure, not a uniform fixed-edge graph. Orthogonal-polynomial decompositions of hypergeometric laws are classical; novelty is claimed only for their stated exact fixed-edge graph histogram application and the explicit all-mode spectrum. Equivalence through a general older multivariate hypergeometric identity remains a priority risk.

## Limitations
Historical priority has not been independently established. The theorem addresses only the second moments of the supported degree histogram; it does not assert a Gaussian limit, chi-square calibration, or independence between individual degree bins. Its normalization differs from a covariance matrix of unconstrained independent binomial degrees. Degenerate edge counts require the explicitly stated singleton-support interpretation. The independent scientific audit remains unperformed.

## References
1. A. Liebenau and N. Wormald, *Asymptotic enumeration of graphs by degree sequence, and the degree sequence of a random graph*, arXiv:1702.08373 (first posted 2017-02-27), especially the introduction and Proposition 1.1 on \(G(n,m)\).
2. K. Lin and G. Reinert, *Joint vertex degrees in the inhomogeneous random graph model*, Advances in Applied Probability (2012), DOI: 10.1239/aap/1331216648, especially the explicit independent-edge covariance matrix near Theorem 3.1.
3. R. van der Hofstad, J. Komjáthy and V. Vadon, *Random intersection graphs with communities*, arXiv:1809.02514 (first posted 2018-09-07), especially the model definition and empirical degree distribution results.
