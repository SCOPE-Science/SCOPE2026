# Adjoint-rank and commutativity laws for cycle graphical Lie algebras

## Finding

For each prime power \(q\) and integer \(n\ge4\), let \(L_{n,q}\) be the \(2n\)-dimensional two-step nilpotent Lie algebra over \(\mathbb F_q\) with vertex basis \(v_0,\ldots,v_{n-1}\), central edge basis \(z_0,\ldots,z_{n-1}\), and brackets
\[
[v_i,v_{i+1}]=z_i\quad(i\bmod n),\qquad [v_i,z_j]=[z_i,z_j]=0,
\]
all other vertex basis brackets being zero, with alternating bilinear extension. Define its adjoint-rank enumerator
\[
R_{n,q}(t)=\sum_{x\in L_{n,q}}t^{\operatorname{rank}(\operatorname{ad}_x)}.
\]
Put \(w=q-1\) and set
\[
M_q(t)=\begin{pmatrix}
1&1&0&0\\
0&0&1&1\\
wt^2&wt&0&0\\
0&0&wt&wt
\end{pmatrix}.
\]
Then the entire rank distribution is given, for every \(n\ge4\), by
\[
\boxed{R_{n,q}(t)=q^n\left(\operatorname{tr}(M_q(t)^n)+w^n(t^{n-1}-t^n)\right).}
\]

Let \(X_n\) be uniform in \(L_{n,q}\), and write \(K_n=\operatorname{rank}(\operatorname{ad}_{X_n})\). With \(p=(q-1)/q\) and \(r=1/q\), define
\[
\mu_q=p(1+r^2),\qquad
\sigma_q^2=pr(5p^4-15p^3+21p^2-14p+4)
=\frac{(q-1)(q^4-3q^3+6q^2-5q+5)}{q^6}>0.
\]
For every \(n\ge5\), the exact mean and variance are
\[
\boxed{\mathbb E K_n=n\mu_q-p^n,}
\]
\[
\boxed{\operatorname{Var}(K_n)=n\sigma_q^2+p^n(1-p^n)-2n(1-\mu_q)p^n.}
\]
For each fixed prime power \(q\), these laws yield the central limit theorem
\[
\boxed{\frac{K_n-n\mu_q}{\sqrt{n\sigma_q^2}}\ \xrightarrow{\ d\ }\ N(0,1).}
\]

The *element commutativity degree* is the probability that two independent uniform elements commute:
\[
d(L_{n,q})=\Pr([X,Y]=0).
\]
Set \(\lambda_\pm=(1\pm\sqrt{1+4p})/2\). For every \(n\ge4\),
\[
\boxed{d(L_{n,q})=q^{-n}\left(\lambda_+^n+\lambda_-^n+qp^n\right).}
\]
In particular, since \(\lambda_+>1>p>0\) and \(|\lambda_-|<\lambda_+\),
\[
\boxed{d(L_{n,q})\sim(\lambda_+/q)^n\qquad(n\longrightarrow\infty,\ q\text{ fixed}).}
\]
For example, the element commutativity degrees are \(29/128\) for \(n=4,q=2\) and \(139/2187\) for \(n=4,q=3\).

## Assumptions and scope

All claims concern fields \(\mathbb F_q\) of arbitrary prime-power order, including characteristic two. The bracket is alternating by definition and is a Lie bracket because every bracket lies in the central edge space. Edge orientations do not change the isomorphism type when each edge has its own central basis vector. The cycle is simple and has \(n\ge4\) vertices; the length-three cycle is not needed. Both the rank and the element commutativity degree refer to **all elements** of the entire Lie algebra; the central component of an element does not affect its adjoint rank.

A general finite-graph identity underlies the cycle formula. For a finite simple undirected graph \(G=(V,E)\), form the corresponding edge-distinct graphical two-step Lie algebra. For a set \(S\subseteq V\), let \(N[S]\) be its closed neighborhood and \(c(G[S])\) the number of connected components of the induced subgraph, with \(c(G[\varnothing])=0\). Then
\[
\boxed{\sum_{x\in L_G}t^{\operatorname{rank}(\operatorname{ad}_x)}
=q^{|E|}\sum_{S\subseteq V}(q-1)^{|S|}t^{|N[S]|-c(G[S])}.}
\]
This support identity is proved here as the reduction, not independently asserted as a previously unknown graph-polynomial identity. The cycle-specific exact transfer, moment, Gaussian, and commutativity formulas constitute the assessed finding.

## Proof

**1. Kernel of a graphical adjoint.** Write \(x=\sum_{u\in V}x_uv_u+z\), with \(z\) central, and let \(S=\{u:x_u\ne0\}\). For any vertex vector \(y=\sum_uy_uv_u\), the coefficient of the central basis element corresponding to an oriented edge \(uv\) in \([x,y]\) equals \(x_uy_v-x_vy_u\). If \(u,v\in S\), the condition that this coefficient vanish says \(y_u/x_u=y_v/x_v\). Thus each connected component of \(G[S]\) has exactly one free scalar ratio. If exactly one endpoint is in \(S\), the coefficient equation forces the coordinate at the other endpoint to vanish. Every coordinate outside \(N[S]\) remains unconstrained. Therefore the kernel of the vertex-to-edge adjoint map has dimension
\[
c(G[S])+|V|-|N[S]|,
\]
and its rank is \(|N[S]|-c(G[S])\). There are \((q-1)^{|S|}\) vertex coefficient vectors of support \(S\), while the central coordinate \(z\) has \(q^{|E|}\) choices. This proves the finite-graph identity, including isolated vertices, disconnected graphs and the empty support.

**2. Cycle run statistic and transfer.** For \(G=C_n\), record a vertex support by a circular binary word \(a_0\ldots a_{n-1}\), with \(a_i=1\) for a nonzero vertex coefficient. If the support is nonempty and proper, its one-runs and zero-runs alternate in equal numbers. A zero-run of length \(\ell\) contributes \(\min(\ell,2)\) boundary vertices to the closed neighborhood, while each one-run contributes one connected component. Consequently
\[
|N[S]|-c(C_n[S])=|S|+\#\{\text{zero-runs of length at least two}\}.
\]
Each zero-run of length at least two has exactly one cyclic occurrence of the pattern \(100\). For the all-zero word the rank is zero. For the all-one word, the rank is \(n-1\), rather than \(n\). Hence, for **every** circular word,
\[
\operatorname{rank}(\operatorname{ad}_x)
=\sum_{i=0}^{n-1}\left(a_i+a_i(1-a_{i+1})(1-a_{i+2})\right)
-\mathbf1_{\{a_0=\cdots=a_{n-1}=1\}},
\]
with indices modulo \(n\).

Index the four matrix states by \((0,0),(0,1),(1,0),(1,1)\). A transition \((a,b)\to(b,c)\) carries weight \(w^a t^{a+\mathbf1_{\{(a,b,c)=(1,0,0)\}}}\). This is precisely the matrix \(M_q(t)\) above. A length-\(n\) closed walk uniquely encodes a circular binary word at the fixed indexed positions. The product of its transition weights is \(w^{|S|}t^{|S|+\#100}\). Thus \(\operatorname{tr}(M_q(t)^n)\) enumerates all words with the uncorrected statistic. Replacing the all-one contribution \(w^nt^n\) by \(w^nt^{n-1}\), then multiplying by \(q^n\) for the central coordinates, proves the exact rank polynomial.

**3. Exact commutativity degree.** Rank-nullity gives \(\Pr([x,Y]=0\mid x)=q^{-\operatorname{rank}(\operatorname{ad}_x)}\). Averaging, and cancelling the free central coordinates, yields
\[
d(L_{n,q})=q^{-n}\left(\operatorname{tr}(M_q(1/q)^n)+w^n(q^{-(n-1)}-q^{-n})\right).
\]
A direct characteristic-polynomial calculation at \(t=1/q\) gives
\[
\det(\lambda I-M_q(1/q))=\lambda(\lambda-p)(\lambda^2-\lambda-p).
\]
Therefore \(\operatorname{tr}(M_q(1/q)^n)=\lambda_+^n+\lambda_-^n+p^n\). The correction equals \((q-1)p^n\). Substitution gives the exact closed formula and its exponential asymptotic.

**4. Moments and Gaussian limit.** For a uniform vertex vector, the binary indicators \(A_i=\mathbf1_{\{x_i\ne0\}}\) are independent Bernoulli variables of mean \(p\). Set
\[
Y_i=A_i+A_i(1-A_{i+1})(1-A_{i+2}).
\]
Then \(K_n=\sum_iY_i-I_n\), where \(I_n=\mathbf1_{\{A_0=\cdots=A_{n-1}=1\}}\). Direct independent-Bernoulli calculations give
\[
\mathbb EY_i=p(1+r^2)=\mu_q,
\qquad \mathbb EY_i^2=p(1+3r^2),
\]
\[
\operatorname{Cov}(Y_i,Y_{i+1})=
\operatorname{Cov}(Y_i,Y_{i+2})=-p^2r^2(1+r^2).
\]
All other covariances vanish when the supporting triples are disjoint. For the cyclic model with \(n\ge5\), counting pairs at cyclic distances one and two yields
\[
\operatorname{Var}\!\left(\sum_iY_i\right)
=n\left(p(1+3r^2)-\mu_q^2-4p^2r^2(1+r^2)\right)=n\sigma_q^2.
\]
Moreover \(\mathbb EI_n=p^n\) and \(\operatorname{Cov}(\sum_iY_i,I_n)=n(1-\mu_q)p^n\). This proves both exact moments. Positivity of the displayed rational formula for \(\sigma_q^2\) is immediate at \(q=2\); at \(q\ge3\), its numerator's factor \(q^4-3q^3\) is nonnegative and the remaining \(6q^2-5q+5\) is positive.

The sequence \((Y_i)\) obtained from a bi-infinite independent Bernoulli sequence is bounded, stationary and two-dependent. Its asymptotic variance is the strictly positive \(\sigma_q^2\), so the standard central limit theorem for bounded finite-dependent sequences applies. Replacing a linear length-\(n\) sum by the cyclic sum modifies at most two boundary terms, each bounded; subtracting \(I_n\) changes the sum by at most one. These bounded changes disappear after division by \(\sqrt n\), proving the stated Gaussian limit with the stated centering.

## Verification

The accompanying standalone `verify.py` constructs the bracket coefficient matrix **directly** from each graph edge, performs finite-field Gaussian elimination, and counts the adjoint ranks over \(\mathbb F_2\) and \(\mathbb F_3\). Independently it determines the rank from closed neighborhoods and support components, and checks cycle coefficients against an explicitly multiplied polynomial transfer matrix. It also verifies the exact moment formulas from rational arithmetic, and performs weighted binary-word tests for orders \(q=2,3,4,5,9\) through cycle lengths four to ten. The verifier prints `VERIFY_OK` on success.

Sample vertex-coordinate rank distributions, **before** multiplication by the \(q^n\) central choices, are: for \((n,q)=(4,2)\), multiplicities \((1,0,6,9)\); for \((n,q)=(5,2)\), \((1,0,5,15,11)\); for \((n,q)=(5,3)\), \((1,0,10,80,152)\). Their sums are \(q^n\). The cyclic-pattern and transfer checks were also performed at nonprime field orders, where multiplicities depend only on the number of nonzero field elements. Finite experiments are corroboration, not proof of any all-\(n\) result or of the Gaussian limit.

## Relationship to prior work

Godoy Molina and Lagos (arXiv:2308.00272v2) develop two-step Lie algebras from labeled directed graphs and explicitly study graph ideals and strata-preserving derivations of two differently labeled complete bipartite graphs. Their edge-distinct bracket construction (Section 2) is the algebraic setting used here. Their original text, including Sections 3–5, does not supply cycle element-adjoint rank distributions, cycle commutativity degrees, or growing-cycle limit laws.

Shamsaki, Erfanian and Parvizi (arXiv:2406.10064v1) define and study the commutativity degree of finite-dimensional Lie algebras. Their Lemma 3.2 relates the degree to adjoint images; that general identity is **prior work** used in Step 3. Their examples and bounds do not give the cycle-specific transfer, exact closed form or Gaussian spectrum.

A published cycle graphical-group character-degree calculation (published-finding corpus, `SCOPE-cycle-graphical-groups-have-an-explicit-character-degree-enumera--a874723da77e`) enumerates ranks of **vertex-by-vertex alternating adjacency matrices parametrized by edge weights**. That is mathematically different from the **edge-by-vertex adjoint maps parametrized by vertex coefficients** counted here. Neither matrix family is an elementary specialization of the other, and the former rank table does not imply the formulas here. Another published rank calculation, `SCOPE-adjoint-rank-spectra-of-two-maximal-class-filiform-lie-algebras--48cdbeaf7d86`, treats maximal-class filiform Lie algebras of nilpotency class growing with dimension. The present algebras all have nilpotency class two and different centralizers. The respective full research statements were compared.

The general support identity, finite-dependent central limit theorem, transfer-matrix method, and graph-Lie construction are not claimed as individually novel. The assessed result is their explicit nontrivial combination giving exact cycle adjoint-rank coefficients, moment corrections, the closed element commutativity degree, and its accompanying Gaussian rank law.

## Limitations

The closed transfer formula and Gaussian law are established only for edge-distinct graphical Lie algebras of cycles; identifying several central edge labels can cause cancellation and invalidates the support-kernel argument. The general-graph support formula does not by itself provide closed distributions for arbitrary graphs. The central limit theorem fixes \(q\) and lets \(n\to\infty\); it does not assert uniformity when \(q\) grows with \(n\), local limit estimates, or independence of ranks at different sample points.

An equivalent cycle adjoint-rank formula might be published under graphical Lie breadth, centralizer distributions, or binary-pattern enumerator terminology not retrieved by the targeted searches. The literature comparison supports originality against the inspected sources but does not certify absolute publication priority. No independent audit has been performed.

## References

1. M. Godoy Molina and D. Lagos, “Lie algebras associated with labeled directed graphs,” arXiv:2308.00272v1, first public 1 August 2023; v2, 6 August 2023. Sections 2–5. https://arxiv.org/abs/2308.00272.
2. A. Shamsaki, A. Erfanian and M. Parvizi, “On the commutativity degree of a finite-dimensional Lie algebra,” arXiv:2406.10064v1, first public 14 June 2024, especially Definition 3.1 and Lemma 3.2. https://arxiv.org/abs/2406.10064.
3. T. Rossmann, “Enumerating conjugacy classes of graphical groups over finite fields,” arXiv:2107.05564v1, first public 12 July 2021. Background for the different edge-weighted character-rank problem. https://arxiv.org/abs/2107.05564.
4. Published result, “Cycle graphical groups have an explicit character-degree enumerator,” https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-cycle-graphical-groups-have-an-explicit-character-degree-enumera--a874723da77e.
5. Published result, “Adjoint-rank spectra of two maximal-class filiform Lie algebras,” https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-adjoint-rank-spectra-of-two-maximal-class-filiform-lie-algebras--48cdbeaf7d86.
