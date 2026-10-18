# Marked-leaf pruning controls terminal depth in uniform recursive trees

## Finding
Let \(T_n\) be a uniform recursive tree on birth labels \(1,\ldots,n\) and \(n\ge3\). Let \(H_n\) be the depth of the last-born vertex \(n\), and \(L_n\) the number of childless vertices. For any prescribed subset \(S\subseteq\{2,\ldots,n-1\}\) of size \(s\), conditional on **every vertex of \(S\) being a leaf**, the depth \(H_n\) has exactly the unconditional distribution of \(H_{n-s}\). This holds without averaging over the positions of \(S\).

Write \(A_m(u)=\sum_{j=0}^{m-1}\langle m,j\rangle u^j\) for the ordinary Eulerian polynomial and define
\[
h_k(z)=\frac{z(z+1)\cdots(z+k-2)}{(k-1)!}\quad (k\ge2).
\]
Then the complete bivariate probability-generating function is
\[
\boxed{\displaystyle
\mathbb E\bigl[z^{H_n}u^{L_n-1}\bigr]
=\frac1{(n-1)!}\sum_{s=0}^{n-2}
\frac{A_{n-1}^{(s)}(1)}{s!}(u-1)^s h_{n-s}(z).}
\]
In particular, for every real-valued function \(f\) on \(\{1,\ldots,n\}\),
\[
\boxed{\displaystyle
\operatorname{Cov}(f(H_n),L_n)
=-\frac{n-2}{2(n-1)}\mathbb E\bigl[f(H_{n-1}+1)-f(H_{n-1})\bigr].}
\]
Here the expectation on the right is over the unconditional \(H_{n-1}\) law; the shift is deterministic. Every strictly increasing \(f\) therefore has strictly negative covariance. Notably,
\[
\operatorname{Cov}(H_n,L_n)=-\frac{n-2}{2(n-1)}.
\]

## Assumptions and scope
For each \(j=2,\ldots,n\), independently choose the parent of \(j\) uniformly from \(\{1,\ldots,j-1\}\); root \(1\) has depth zero. A leaf has no children (rather than undirected degree one). When \(S=\varnothing\), the first identity is read without conditioning. The last-born vertex \(n\) is always a leaf; vertex \(1\) is never a leaf for \(n\ge2\). Eulerian coefficients are \(\langle m,j\rangle=\#\{\pi\in\mathfrak S_m:\operatorname{des}(\pi)=j\}\). The product defining \(h_2(z)\) is simply \(z\).

The joint generating-function identity applies to every integer \(n\ge3\). The transform-covariance identity applies to any \(f\) on the indicated finite support, and its strict sign applies only when \(f\) is strictly increasing. The degenerate tree \(n=2\) has constant depth and leaf count.

## Proof
**1. Exact multi-leaf pruning.** Fix \(S\subseteq\{2,\ldots,n-1\}\). The event \(E_S\) that every member of \(S\) is childless is equivalent to forbidding every parent choice \(P_j\) from belonging to \(S\cap\{1,\ldots,j-1\}\), simultaneously for all \(j\). Since the original parent choices are mutually independent, conditioning on \(E_S\) preserves independence. Every surviving vertex \(j\notin S\) consequently selects its parent uniformly from the earlier surviving labels. Hence deleting the members of \(S\), each of which was terminal, gives precisely a uniform recursive tree on \(n-s\) vertices after order-preserving relabeling. Because neither \(1\) nor \(n\) is deleted, the depth of \(n\) is unchanged by deletion. Thus \(H_n\mid E_S\stackrel d=H_{n-s}\), independently of the locations of \(S\).

For completeness, if the selected leaf labels are \(2\le i_1<\cdots<i_s<n\), their event probability is
\[
\Pr(E_S)=\prod_{j=1}^{s}\frac{i_j-j}{n-j}>0.
\]
This follows by multiplying all allowed-parent fractions and canceling, or inductively removing the marked leaves. Every conditional law above is therefore well-defined.

**2. Depth and leaf marginals.** The root-to-vertex depth \(H_k\) has probability generating function
\[
h_k(z)=\prod_{j=1}^{k-1}\Bigl(1+\frac{z-1}{j}\Bigr)
=\frac{z(z+1)\cdots(z+k-2)}{(k-1)!}.
\]
One proof conditions on whether the \(j\)-th earlier vertex is an ancestor, whose indicators are independent Bernoulli variables of success probabilities \(1/j\). Equivalently, the usual generating-function recursion from uniformly chosen parents gives the same product. In particular, \(H_k\stackrel d=H_{k-1}+B_{k-1}\), with \(B_{k-1}\sim\operatorname{Bernoulli}(1/(k-1))\) independent of \(H_{k-1}\).

The leaf count satisfies the Eulerian marginal law
\[
\Pr(L_n=\ell)=\frac{\langle n-1,\ell-1\rangle}{(n-1)!},\qquad 1\le\ell\le n-1.
\]
Indeed, a newly arriving vertex leaves the leaf total unchanged when it attaches to a leaf, and increases it by one when it attaches to a nonleaf. The resulting exact count recurrence is the Eulerian recurrence \(\langle m,k\rangle=(k+1)\langle m-1,k\rangle+(m-k)\langle m-1,k-1\rangle\).

**3. Complete joint distribution.** Put \(I_i=\mathbf1\{i\text{ is a leaf}\}\) for \(2\le i<n\), so \(L_n-1=\sum_{i=2}^{n-1}I_i\). Expand
\[
u^{L_n-1}=\prod_{i=2}^{n-1}\bigl(1+(u-1)I_i\bigr)
=\sum_{S\subseteq\{2,\ldots,n-1\}}(u-1)^{|S|}\mathbf1_{E_S}.
\]
By step 1, \(\mathbb E[z^{H_n}\mathbf1_{E_S}]=\Pr(E_S)h_{n-|S|}(z)\). The summed probability over all subsets of size \(s\) is
\[
\sum_{|S|=s}\Pr(E_S)=\mathbb E\binom{L_n-1}{s}
=\frac{A_{n-1}^{(s)}(1)}{s!(n-1)!},
\]
by step 2. Substitution proves the displayed joint generating-function identity coefficientwise.

**4. Covariance for arbitrary transforms.** For each \(2\le i<n\), step 1 with \(S=\{i\}\) implies \(\mathbb E[f(H_n)\mid I_i=1]=\mathbb E[f(H_{n-1})]\). Thus
\[
\operatorname{Cov}(f(H_n),I_i)=\Pr(I_i=1)
\bigl(\mathbb E f(H_{n-1})-\mathbb E f(H_n)\bigr).
\]
The singleton probability in step 1 is \(\Pr(I_i=1)=(i-1)/(n-1)\), and summing it from \(i=2\) to \(n-1\) gives \((n-2)/2\). The Bernoulli convolution of step 2 shows
\[
\mathbb E f(H_n)-\mathbb E f(H_{n-1})
=\frac1{n-1}\mathbb E\bigl[f(H_{n-1}+1)-f(H_{n-1})\bigr].
\]
Since \(I_n=1\) deterministically, summing yields the announced transform-covariance law. The increment is strictly positive for strictly increasing \(f\), proving the strict sign. Taking \(f(x)=x\) gives the linear covariance.

## Verification
Run the standalone standard-library script `verify_rrt_pruning.py` using `python3 verify_rrt_pruning.py`. It enumerates every choice of recursive-tree parents for \(3\le n\le8\), verifies the two-variable generating polynomial coefficient by coefficient against an independently computed Eulerian-derivative expression, checks the closed covariance formula, and tests each possible subset of intermediate marked leaves by exact conditional depth frequencies. It reports 695 exact rational assertions. This finite enumeration corroborates, but does not replace, the all-\(n\) argument above.

## Relationship to prior work
Janson's study of random recursive trees treats the degree-distribution process, including the outdegree-zero statistic underlying the Eulerian leaf marginal. Kuba and Wagner's full-text bijective paper establishes the marginal distribution of individual vertex depths in increasing-tree families and preserves the outdegree sequence under its bijection. The present statement concerns the *joint* terminal-depth/leaf-count law and the stronger identity under every prescribed subset of marked leaves; neither comparison explicitly evaluates this joint law. These classical marginal ingredients are not claimed as new. A priori, earlier joint generating functions or degree-preserving bijections might imply the result through further extraction; historical priority therefore merits independent verification.

## Limitations
Only uniform recursive trees are treated; the pruning law need not hold for preferential-attachment or other degree-weighted increasing-tree models. The formula does not assert statistical independence of depth and leaf count. The exact distribution is proved mathematically, whereas finite computations are checks. Exhaustive historical coverage cannot be guaranteed; one relevant older degree paper was available at abstract level but its lawful open manuscript could not be fully inspected.

## References
1. Svante Janson, "Asymptotic degree distribution in random recursive trees," *Random Structures & Algorithms* **26** (2005), 69–83, first available November 16, 2004, DOI: 10.1002/rsa.20046.
2. Markus Kuba and Stephan Wagner, "On the distribution of depths in increasing trees," *Electronic Journal of Combinatorics* **17** (2010), R137, published October 15, 2010, DOI: 10.37236/409. Full-text PDF: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v17i1r137/pdf.
