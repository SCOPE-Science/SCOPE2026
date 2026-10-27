# Degree-one motif dependence and its leaf-number sign law in fixed-edge random graphs

## Finding
Let \(L_1\) count degree-one vertices in a uniform fixed-edge random graph and \(X_H\) count injective, not necessarily induced, embeddings of a graph \(H\). Their exact normalized mixed moment is
\[
\mathcal R=\frac{\mathbb E[L_1X_H]}{\mathbb E[L_1]\mathbb E[X_H]}
=\frac{(N)_{\underline h}}{(U)_{\underline h}}
\left[\frac{(n-k)(m-h)}{nm}+\frac{\ell(U-h+1)}{n(n-1)m}\right].
\]
Here \(N=\binom n2\), \(U=\binom{n-1}{2}\), \(k=|V(H)|\), \(h=|E(H)|\), and \(\ell\) is the number of vertices of degree one in \(H\). The covariance is \(\mathbb E[L_1]\mathbb E[X_H](\mathcal R-1)\). Consequently its sign is determined by these five integers, regardless of other details of the motif topology. For fixed \(n,k,h,\ell\), the ratio is affine in \(1/m\) and has at most one strict sign transition in the admissible integer edge range. Holding \(n,m,k,h\) fixed, it increases strictly with \(\ell\). In particular, on six vertices with five motif edges, the path and star have opposite signs in \(G(12,10)\):
\[
\mathcal R_{P_6}=\frac{41664}{49555}<1,
\qquad
\mathcal R_{K_{1,5}}=\frac{11284}{9911}>1.
\]

## Assumptions and scope
Take integers \(n\ge4\), \(2\le k\le n\), and \(h\ge1\). Let \(H\) be a fixed simple graph on \(k\) labeled vertices, with \(h\) edges, no isolated vertices, and exactly \(\ell\) degree-one vertices. Require \(h\le m\le U=\binom{n-1}{2}\). The random graph \(G(n,m)\) is uniform over all simple labeled graphs on \(n\) vertices having exactly \(m\) edges. Each injection of \(V(H)\) into \(V(G)\) preserving every edge is counted once in \(X_H\); nonedges of \(H\) are unrestricted. The falling factorial is \((a)_{\underline r}=\prod_{j=0}^{r-1}(a-j)\). All claims include equality and zero-covariance boundary cases within the specified range. This range ensures that the event that a chosen vertex has degree one has positive probability, so the normalized ratio is defined.

## Proof
Fix a graph vertex \(v\). Conditional on \(\deg_G(v)=1\), its unique neighbor is uniform over the other \(n-1\) vertices, and the \(m-1\) other edges form a uniformly selected subset of the \(U\) edges not incident to \(v\). For any injection of \(H\), there are three disjoint cases.

If \(v\) is outside the image, all \(h\) prescribed edges lie away from \(v\), and the conditional probability of their occurrence is
\[
\frac{(m-1)_{\underline h}}{(U)_{\underline h}}.
\]
There are \((n-1)_{\underline k}\) such injections. If \(v\) is the image of one of the \(\ell\) degree-one motif vertices, the motif edge incident at \(v\) must be the unique graph edge incident there; conditional on that event, the remaining \(h-1\) motif edges occur with probability
\[
\frac1{n-1}\frac{(m-1)_{\underline{h-1}}}{(U)_{\underline{h-1}}}.
\]
There are \(\ell(n-1)_{\underline{k-1}}\) such injections. If \(v\) is the image of a motif vertex of degree at least two, the conditional probability is zero. Summing,
\[
\mathbb E[X_H\mid \deg_G(v)=1]
=(n-1)_{\underline k}\frac{(m-1)_{\underline h}}{(U)_{\underline h}}
+\frac{\ell(n-1)_{\underline{k-1}}}{n-1}\frac{(m-1)_{\underline{h-1}}}{(U)_{\underline{h-1}}}.
\]
By exchangeability, \(\mathbb E[L_1X_H]=n\Pr(\deg_G(v)=1)\mathbb E[X_H\mid\deg_G(v)=1]\) and \(\mathbb E[L_1]=n\Pr(\deg_G(v)=1)\). Also
\[
\Pr(\deg_G(v)=1)=(n-1)\frac{\binom U{m-1}}{\binom N m},\qquad
\mathbb E[X_H]=(n)_{\underline k}\frac{(m)_{\underline h}}{(N)_{\underline h}}.
\]
Dividing the conditional expectation by \(\mathbb E[X_H]\), using \((n-1)_{\underline k}/(n)_{\underline k}=(n-k)/n\) and \((n-1)_{\underline{k-1}}/(n)_{\underline k}=1/n\), and canceling the falling factorials gives precisely \(\mathcal R\) above. The cancellation is valid also at \(m=h\); zero falling factorials are interpreted in their ordinary finite-product sense.

Set \(A=(N)_{\underline h}/(U)_{\underline h}>0\). The formula rewrites as
\[
\mathcal R=A\left[\frac{n-k}{n}+\frac{1}{nm}\left(\frac{\ell(U-h+1)}{n-1}-h(n-k)\right)\right].
\]
Therefore \(\mathcal R-1\) is affine in \(1/m\) and monotone as \(m\) varies, so its strict sign can change at most once. Moreover \(\partial\mathcal R/\partial\ell=A(U-h+1)/(n(n-1)m)>0\) as a comparison between attainable integer motif leaf numbers. The exact fractions for the path and star follow by substitution. No asymptotic or finite-enumeration inference is used in this proof.

## Verification
Run `python verify_degree_one_motifs.py` with Python's standard library from the directory containing this document and the verifier. It exhaustively enumerates fixed-edge graphs for selected small orders, compares exact rational covariances independently with the formula, and checks the single-crossing algebra on a rational parameter grid. The recorded run passed 72 exhaustive graph comparisons and 2,896 rational parameter-grid checks; the six-vertex path and star fractions were recomputed exactly. The exhaustive finite tests do not themselves prove the theorem for all orders; that follows from the conditioning argument above.

## Relationship to prior work
A principal reference is Janson's 2006 treatment of random-graph degree counts under the fixed-edge ensemble, including limit theorems and coupling arguments. That material studies degree statistics and subgraph-count asymptotics, but its inspected degree-count section does not provide this exact mixed moment between degree-one counts and arbitrary noninduced motif counts, or the motif leaf-number sign comparison. Earlier subgraph-count functional limits establish a broader asymptotic setting; a full-text priority comparison for one 1990 predecessor remains incomplete. The present exact finite formula is not an assertion that those classical general frameworks are new.

## Limitations
The statement applies to simple fixed-edge graphs, motifs without isolated vertices, and the stated domain \(h\le m\le\binom{n-1}{2}\). It does not cover induced embeddings, degree classes other than one, or all densities outside that range. The number of embeddings counts labeled injections; automorphism-normalized motif counts multiply by a positive constant and therefore preserve covariance signs. A potentially relevant 1990 functional-limit paper was available only in abstract and has not been excluded as an earlier equivalent source. Originality is a best-knowledge, non-independent assessment, not a historical priority guarantee.

## References
- Svante Janson, *Monotonicity, asymptotic normality and vertex degrees in random graphs*, arXiv:math/0605642 (first public version May 24, 2006), particularly the section on vertex degrees and fixed-edge random graphs.
- Svante Janson, *A functional limit theorem for random graphs with applications to subgraph count statistics*, Random Structures & Algorithms (1990), DOI:10.1002/rsa.3240010103 (only abstract examined for the present priority comparison).
