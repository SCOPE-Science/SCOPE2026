# Opposite global and local leaf regressions under subtree-size conditioning in random recursive trees

## Finding
Let \(T_n\) be the uniform random recursive tree on labels \(1,\ldots,n\), where vertex \(j\ge2\) chooses an independent uniformly random parent in \(\{1,\ldots,j-1\}\). Fix \(n\ge3\) and \(2\le k\le n\). Write \(S=S_{k,n}\) for the size, including vertex \(k\), of the descendant subtree rooted at \(k\); \(U=U_{k,n}\) for the number of leaves within that descendant subtree; and \(L=L_n\) for the number of leaves in the *whole* tree. A leaf has no children.

For every \(1\le s\le n-k+1\),
\[
\mathbb E[U\mid S=s]=\frac{s}{2}+\frac12\mathbf1_{\{s=1\}}.
\]
For \(k\ge3\), the **global** leaf regression is
\[
\boxed{\mathbb E[L\mid S=s]=\frac n2+\frac12\mathbf1_{\{s=1\}}-\frac{k-2}{2(n-s-1)}.}
\]
It is strictly decreasing in \(s\) whenever at least two subtree sizes are possible. At \(k=2\), the exact regression is \(n/2+\mathbf1_{\{s=1\}}/2-\mathbf1_{\{s=n-1\}}/2\); it is nonincreasing, with possible interior plateaus.

For every \(2\le k\le n\), the exact covariances are
\[
\boxed{\operatorname{Cov}(S,L)=-\frac{n-k}{2(n-1)},\qquad
\operatorname{Cov}(S,U)=\frac{(n-k)(k-1)[n(n-1)-k(k+1)]}{2k^2(k+1)(n-1)}.}
\]
Consequently, for \(k<n\), \(\operatorname{Cov}(g(S),L)<0\) for every nonconstant nondecreasing real function \(g\) on the support of \(S\). Conversely, \(\operatorname{Cov}(g(S),U)>0\) for every such function if \(n\ge k+2\). At \(n=k+1\), \(U=1\) almost surely; at \(n=k\), \(S=1\) almost surely. This is an opposite-sign **regression** result, not a claim of stochastic ordering for the complete conditional leaf distributions.

## Assumptions and scope
All parent choices are independent and uniform, and the outdegree-zero convention for leaves includes a singleton tree. The claim concerns integer \(n\ge3\), integer \(k\in\{2,\ldots,n\}\), and \(s\in\{1,\ldots,n-k+1\}\). The whole-tree leaves include subtree leaves. The ancestor-to-subtree edge from the parent of \(k\) must be retained when counting global leaves. The primary classification is MSC2020 \(60\mathrm C05\).

## Proof
**1. The conditioned two-tree decomposition.** At the birth of vertex \(k\), mark it and all of its future descendants. At every later birth, a vertex joins the marked group precisely if its chosen parent is marked. Thus the marked count evolves by the classical two-color Pólya rule, starting at \(1\) marked and \(k-1\) unmarked vertices. The final support is \(1\le S\le n-k+1\), and for \(r=s-1\),
\[
\mathbb P(S=s)=\binom{n-k}{r}\frac{(1)_r(k-1)_{n-k-r}}{(k)_{n-k}},
\]
where \((a)_r=a(a+1)\cdots(a+r-1)\), with \((a)_0=1\). Conditioned on the entire marked/unmarked arrival sequence, each new marked vertex independently chooses a uniformly random earlier marked parent, and each new unmarked vertex chooses a uniformly random earlier unmarked parent. Thus, conditional on \(S=s\), the induced marked and unmarked trees are independent uniform recursive trees of sizes \(s\) and \(N=n-s\). The original parent of \(k\) is uniformly selected among the first \(k-1\) vertices of the unmarked tree and is independent of these two induced trees.

**2. The leaf regressions.** In a uniform recursive tree on \(a\ge2\) vertices, the mean number of leaves is \(a/2\). Indeed, vertex \(i\ge2\) remains a leaf with probability \((i-1)/(a-1)\), while the root is not a leaf. For a singleton tree the leaf count is \(1\). It follows that \(\mathbb E[U\mid S=s]=s/2+\mathbf1_{\{s=1\}}/2\).

Let \(J\) indicate that the parent of vertex \(k\) is a leaf *within the unmarked induced tree*. The entire tree has \(L=U+L_{\mathrm{out}}-J\): adding the parent-to-\(k\) edge removes precisely that one unmarked leaf if it existed. For \(k\ge3\), necessarily \(N\ge k-1\ge2\), and
\[
\mathbb E[J\mid S=s]=\frac1{k-1}\sum_{i=1}^{k-1}\frac{i-1}{N-1}=\frac{k-2}{2(N-1)}.
\]
Since \(\mathbb E[L_{\mathrm{out}}\mid S=s]=N/2\), this proves the displayed global regression. It is strictly decreasing from \(s=1\) onward for \(k\ge3\) when the support is nontrivial: the singleton correction decreases at the first step, and the reciprocal term decreases for subsequent steps. When \(k=2\), the unmarked tree has \(N\ge1\) vertices and its sole earliest vertex is the root; it is not a leaf for \(N\ge2\), while for \(N=1\) it is a leaf. This gives the exceptional two-endpoint formula, including \(n=3\).

**3. Local covariance.** The Pólya count has
\[
\mathbb ES=\frac nk,\quad \operatorname{Var}(S)=\frac{(n-k)(k-1)n}{k^2(k+1)},\quad \mathbb P(S=1)=\frac{k-1}{n-1}.
\]
From the local regression, \(\operatorname{Cov}(S,U)=\tfrac12\operatorname{Var}(S)+\tfrac12\mathbb P(S=1)(1-\mathbb ES)\). Substitution yields the stated exact expression. Its sign is positive for \(n\ge k+2\), and zero for \(n\in\{k,k+1\}\).

**4. Global covariance by a direct growth identity.** For times \(t\ge k\), let \(S_t,U_t,L_t\) be the corresponding counts. If the new vertex attaches inside the marked subtree, \(S_t\) grows by one. The whole-tree leaf count grows by one unless the chosen parent was a leaf. A one-step conditional multiplication gives
\[
\mathbb E[S_{t+1}L_{t+1}\mid T_t]=S_tL_t+(1+1/t)S_t-U_t/t.
\]
For \(t\ge k\ge2\), the one-vertex leaf probabilities and descendant probability \(1/k\) yield
\[
\mathbb ES_t=t/k,\qquad \mathbb EL_t=t/2,\qquad
\mathbb EU_t=t/(2k)+(k-1)/(2(t-1)).
\]
Also \(\mathbb ES_{t+1}=(1+1/t)\mathbb ES_t\) and \(\mathbb EL_{t+1}=1+(1-1/t)\mathbb EL_t\). Writing \(C_t=\operatorname{Cov}(S_t,L_t)\), subtraction therefore gives
\[
C_{t+1}-C_t=\frac{\mathbb ES_t\,\mathbb EL_t}{t^2}-\frac{\mathbb EU_t}{t}
=-\frac{k-1}{2t(t-1)}.
\]
Since \(C_k=0\), summing from \(t=k\) through \(n-1\) proves \(C_n=-(n-k)/(2(n-1))\).

**5. All increasing transforms.** For any nondecreasing function \(g\), the covariance \(\operatorname{Cov}(g(S),L)\) equals \(\operatorname{Cov}(g(S),h(S))\) with \(h(s)=\mathbb E[L\mid S=s]\), which is nonincreasing. For two iid copies \(S,S'\), twice this covariance equals \(\mathbb E[(g(S)-g(S'))(h(S)-h(S'))]\), hence is nonpositive. It is strictly negative whenever \(k<n\) and \(g\) is nonconstant, because the endpoint values of \(h\) are distinct and have positive probabilities. The same identity applied to the nondecreasing local regression gives strict positivity whenever the support includes \(s\ge3\), i.e. \(n\ge k+2\), and \(g\) is nonconstant. In the remaining two cases the local count is deterministic on the support.

## Verification
The standalone \`verify_recursive_subtree.py\` enumerates all \((n-1)!\) parent-choice trees for each \(3\le n\le9\), totaling \(46{,}232\) trees. It compares the complete exact conditional means, support probabilities, and both covariances using rational arithmetic. A separate exact-rational sum over all \(19{,}899\) parameter pairs \(3\le n\le200\), \(2\le k\le n\), verifies the beta-binomial probabilities and algebraic covariance identities. Both suites passed. These finite checks are corroborative, not an infinite proof.

Run \`python3 verify_recursive_subtree.py\` with Python 3; no nonstandard libraries are required.

## Relationship to prior work
Mahmoud and Smythe (1991) study the size and number of leaves *inside* a rooted recursive subtree, so the local ingredients and their mixed moments are classical. Leckey and Neininger (2012), in a stronger Hoppe-tree setting, give the independent subtree decomposition at the second inserted vertex and marginal global leaf estimates; the \(k=2\) boundary is already implicit in that decomposition. The contribution assessed here is the global leaf regression for every vertex label \(k\ge3\), its monotone anti-association for arbitrary nondecreasing scores, and the exact opposite-sign local/global covariance comparison. These are implication comparisons, not assertions that the underlying Pólya urn or leaf means are new. The full substantive text of the 1991 work could not be completely inspected, leaving a risk of implicit earlier coverage.

## Limitations
No stochastic order for the *full* conditional distribution of \(L\) is proved. The conclusions concern uniform recursive attachment, not arbitrary preferential attachment, plane-oriented recursive trees, or the complete Hoppe family. The local mixed moment is not claimed as separately novel. The 1991 precursor was accessible only in bibliographic/abstract form and incomplete machine-readable page material, so residual duplication risk persists. No independent scientific audit has been performed.

## References
1. H. M. Mahmoud and R. T. Smythe (1991), *On the Distribution of Leaves in Rooted Subtrees of Recursive Trees*, Annals of Applied Probability 1(3), 406–418, DOI: 10.1214/aoap/1177005874.
2. K. Leckey and R. Neininger (2012), *Asymptotic analysis of Hoppe trees*, arXiv:1202.2439 (first posted 2012-02-11), especially Theorem 2.5 and the two-tree decomposition in Section 3. https://arxiv.org/html/1202.2439v3
3. S. Janson (2005), *Asymptotic degree distribution in random recursive trees*, Random Structures & Algorithms 26, 69–83, DOI: 10.1002/rsa.20046 (preprint dated 2003-02-21).
