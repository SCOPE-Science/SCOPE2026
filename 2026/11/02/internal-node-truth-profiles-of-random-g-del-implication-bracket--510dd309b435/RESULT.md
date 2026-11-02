# Internal-node truth profiles of random Gödel-implication bracketings

## Finding
For each integer \(m\ge2\), choose uniformly one plane full binary bracketing on \(n\) ordered distinct variables, and give its leaves independent uniform values in the Gödel chain \(V_m=\{0,1,\ldots,m-1\}\). Interpret each internal node by \(a\Rightarrow b=m-1\) for \(a\le b\), and \(a\Rightarrow b=b\) otherwise. Let \(L_{n,m}(a,b)\) count internal nodes whose left and right children evaluate to \(a,b\), and let \(N_{n,m}(j)\) count internal nodes evaluating to \(j\).

Write \(G_j(z)\) for the generating function counting root value \(j\) across all bracketings and leaf assignments, and put \(G(z)=\sum_jG_j(z)=(1-\sqrt{1-4mz})/2\). Then the exact all-size internal-pair enumerator is
\[
\sum_{n\ge1} m^n C_{n-1}\,\mathbb E[L_{n,m}(a,b)]z^n
=\frac{G_a(z)G_b(z)}{1-2G(z)}
=\frac{G_a(z)G_b(z)}{\sqrt{1-4mz}}.
\]
Set \(r_m=1/(4m)\) and \(\pi_{m,j}=2G_j(r_m)\). For each fixed \(m\) and all child values \(a,b\), simultaneously,
\[
\frac{L_{n,m}(a,b)}{n-1}\ \xrightarrow[n\to\infty]{\mathbb P}\ \pi_{m,a}\pi_{m,b}.
\]
Accordingly, for each truth value \(j\),
\[
\frac{N_{n,m}(j)}{n-1}\ \xrightarrow[n\to\infty]{\mathbb P}\
\tau_{m,j}=\sum_{a,b:\ a\Rightarrow b=j}\pi_{m,a}\pi_{m,b}.
\]
The vector \(\pi_m\) is the output law of a finite almost-surely terminating critical binary branching tree with probability \(1/2\) of a leaf (uniform Gödel label) and \(1/2\) of two ordered children. In particular, for the Boolean chain,
\[
\pi_{2,0}=\frac{\sqrt3-1}{2},\qquad
\tau_{2,0}=\sqrt3-\frac32,
\]
so the limiting proportion of **false internal subformulas** is \(0.232050807568877\ldots\), not the root-output false probability.

A second, distinct continuum law arises by first taking \(n\to\infty\) and then \(m\to\infty\). Scale levels by \(j/(m-1)\). The empirical child-value distributions converge to a measure \(\nu\) with
\[
\nu(dt)=\frac{\mathbf 1_{[0,1)}(t)}{\sqrt{1+2t}}\,dt+(2-\sqrt3)\,\delta_1(dt).
\]
The two child values have limiting joint law \(\nu\otimes\nu\). The empirical *internal-output* law converges to \(\eta\), with
\[
\eta(dt)=\left(\frac{2}{\sqrt{1+2t}}-1\right)\mathbf 1_{[0,1)}(t)\,dt
 +(4-2\sqrt3)\,\delta_1(dt).
\]
The order of limits is essential: the theorem asserts the iterated limit, not a uniform joint-rate statement with \(m\) growing arbitrarily with \(n\).

## Assumptions and scope
The full binary trees are plane, have exactly \(n\ge2\) leaves, have Catalan-uniform shape, and have independent uniform leaf labels. The finite truth chain has \(m\ge2\) levels. All quantities count **every internal implication occurrence in a single randomly evaluated formula**; they are not counts restricted to the root. Convergence in probability for the empirical matrix is for fixed \(m\) as \(n\to\infty\). The continuum law is obtained only subsequently by \(m\to\infty\). Catalan numbers satisfy \(C_k=\binom{2k}k/(k+1)\).

## Proof
**Exact marked-node generating functions.** By the Catalan decomposition, an unmarked term has ordinary generating function \(G=mz+G^2\), hence the stated explicit \(G\). Every internal node with child values \(a,b\) contributes the product \(G_aG_b\) when marked as the root. If the distinguished internal node lies below the root, the root has an arbitrary sibling term on either side. Therefore the marked enumerator \(M_{a,b}\) satisfies \(M_{a,b}=G_aG_b+2GM_{a,b}\), proving the exact identity. The coefficient of \(z^n\) counts all marked internal nodes over all \(m^n C_{n-1}\) equally likely labelled terms, and hence equals their total expectation numerator. The root functions \(G_j\) obey \(G_j=z+G_j\sum_{a>j}G_a\) for \(j<m-1\), with the top component determined by subtraction.

**A fixed marked-fringe strong concentration lemma.** Fix any ordered plane full binary fringe pattern \(t\) with \(\ell\ge2\) leaves, with prescribed labels on all leaves. Let \(X_t\) be the number of occurrences in the sampled tree. Contract one occurrence to a leaf. This produces a tree on \(n-\ell+1\) leaves with one marked leaf. Thus, exactly,
\[
\mathbb E X_t=\frac{(n-\ell+1)C_{n-\ell}}{C_{n-1}}\,m^{-\ell}.
\]
Two distinct occurrences of the same finite fringe pattern cannot be nested. Contracting both gives \(k=n-2(\ell-1)\) leaves and two ordered marked leaves, hence for \(n\ge2\ell\),
\[
\mathbb E[X_t(X_t-1)]=\frac{k(k-1)C_{k-1}}{C_{n-1}}\,m^{-2\ell}.
\]
For fixed \(\ell\), the Catalan ratio \(C_{n-d}/C_{n-1}\to4^{1-d}\) proves
\[
\frac{\mathbb E X_t}{n}\to 4^{1-\ell}m^{-\ell},\qquad
\frac{\mathbb E[X_t(X_t-1)]}{n^2}\to 4^{2-2\ell}m^{-2\ell}.
\]
Consequently \(X_t/n\to4^{1-\ell}m^{-\ell}\) in \(L^2\). Here \(4^{1-\ell}m^{-\ell}\) is the probability of the specified labelled pattern conditional on an internal root in the critical offspring-\(0/2\) Galton--Watson tree: every shape with \(\ell\) leaves has unconditional probability \(2^{-(2\ell-1)}\), and conditioning on the root being internal multiplies this by \(2\). Independent leaf labels multiply by \(m^{-\ell}\).

**Removing the finite-fringe restriction.** The critical \(0/2\) branching tree terminates almost surely, because its offspring generating function has only the extinction solution \(s=1\) in \([0,1]\). For any fixed size bound \(K\), finitely many labelled fringe patterns with at most \(K\) leaves occur, and their frequencies converge jointly by the preceding second-moment argument. The limiting mass of patterns with more than \(K\) leaves is the corresponding conditional Galton--Watson tail, which tends to zero as \(K\to\infty\). Markov's inequality transfers this to the frequency of omitted internal nodes. Since the ordered pair of child truth values is a measurable function of a complete labelled fringe, summing pattern frequencies establishes the empirical pair law \(\pi_{m,a}\pi_{m,b}\), because the branching process's two child subtrees are independent and have law \(\pi_m\). Applying the deterministic implication table gives the internal-output law.

**Critical equations and binary exact value.** The root distribution \(\pi_m\) is a probability distribution because it is the law of the terminating branching tree. Equivalently \(\pi_{m,j}=2G_j(r_m)\): a labelled tree with \(\ell\) leaves has branching probability \(2^{-(2\ell-1)}m^{-\ell}=2r_m^\ell\). Defining tails \(S_{m,j}=\sum_{a\ge j}\pi_{m,a}\), the equations for non-top levels are
\[
\pi_{m,j}=\frac{1}{m(2-S_{m,j+1})}\quad(0\le j<m-1),\qquad S_{m,0}=1.
\]
They also follow by conditioning on the branching root: \(\pi_{m,j}=1/(2m)+\pi_{m,j}S_{m,j+1}/2\). For \(m=2\), solve \(\pi_{2,0}=1/4+(1/2)\pi_{2,0}(1-\pi_{2,0})\) for its root in \((0,1)\). Only left truth \(1\), right truth \(0\) yields internal output \(0\), giving the stated constant.

**Second limit.** The tail recursion rewrites as
\[
S_{m,j}-S_{m,j+1}=\frac{1}{m(2-S_{m,j+1})} \quad(0\le j<m-1).
\]
Because the denominator is in \([1,2]\), the piecewise-linear interpolants of \(S_{m,j}\), for \(j/m\in[0,1)\), are equi-Lipschitz. Any subsequential limit solves \(S'(t)=-1/(2-S(t))\), \(S(0)=1\), uniquely giving \(S(t)=2-\sqrt{1+2t}\). Its left limit at \(t=1\) is the positive top-level atom \(2-\sqrt3\). Consequently scaled child laws converge weakly to \(\nu\), whose continuous density is \(-S'(t)=1/\sqrt{1+2t}\). By independent subtrees, pair limits are \(\nu\otimes\nu\). The implication map \(g(a,b)=1\) for \(a\le b\), otherwise \(b\), is continuous except along the diagonal below the top point; this diagonal has zero \(\nu\otimes\nu\) mass. The continuous mapping theorem applies. Its non-top output density is \(f(t)S(t)=2/\sqrt{1+2t}-1\); the remaining atom at the top is \(4-2\sqrt3\). This proves both continuum formulas and the stated order of limits.

## Verification
An independent exhaustive enumerator directly evaluates every Catalan bracketing and every assignment for all \(2\le m\le3\) and \(1\le n\le6\), and for \(m=4\), \(1\le n\le5\). It tests root counts against a separate dynamic program, all ordered internal-pair counts against an independent marked-node recurrence, and the total of internal occurrences against \((n-1)m^n C_{n-1}\). The included standalone Python program prints `ALL_CHECKS_OK 158`. A separate high-chain critical-value calculation checks the child and parent top atoms as \(m\) increases. Finite enumeration checks finite identities only; the infinite limiting theorems follow from the proofs above.

## Relationship to prior work
Yildiz, *Gödel Implication on Finite Chains: Catalan Enumeration and a Continuum Limit Law* (arXiv:2602.16135, first posted 18 February 2026; revised 10 October 2026) proves **root-output** asymptotics, their chain continuum law, and the root-pair factorisation \(G_aG_b\) (Part IV, Theorems 9--10). These are used explicitly. The present claim is about **all internal nodes within a sampled bracketing**, their empirical concentration, an exact marked-node enumerator, and a different continuum law. Its continuum internal-output atom \(4-2\sqrt3\) differs from the established root-output atom \(1/\sqrt3\).

Janson, *Asymptotic normality of fringe subtrees and additive functionals in conditioned Galton--Watson trees* (arXiv:1312.1211), establishes a broad framework for fringe-subtree counts, including strong distributional results. That general machinery can provide an alternative convergence proof, but the present specialized theorem supplies elementary exact second-moment counts, the complete Gödel child-pair/profile constants, and the second continuum law. Broutin, Devroye, and Fraiman, *Recursive functions on conditional Galton--Watson trees* (arXiv:1805.09425), treats recursive evaluations on conditioned trees, predominantly root values, and provides complementary perspective. The use of a critical branching-tree interpretation and classical Catalan identities is not claimed as novel in isolation.

## Limitations
The sampling model requires uniform Catalan bracketings and independent uniform leaf labels; it does not cover reused dependent propositional variables, nonuniform random trees, a growing chain in the same unqualified limit as growing formula size, or fluctuations/central limit theorems for these empirical frequencies. No absolute historical priority is claimed; the exact internal-node formulas might be obtainable as a specialization of general fringe-function results paired with the existing Gödel critical generating functions. Independent mathematical evaluation remains outstanding.

## References
1. V. Yildiz, *Gödel Implication on Finite Chains: Catalan Enumeration and a Continuum Limit Law*, arXiv:2602.16135v2, 2026; first public version 18 February 2026. https://arxiv.org/html/2602.16135v2
2. S. Janson, *Asymptotic normality of fringe subtrees and additive functionals in conditioned Galton--Watson trees*, arXiv:1312.1211, 2013. https://arxiv.org/abs/1312.1211
3. N. Broutin, L. Devroye and N. Fraiman, *Recursive functions on conditional Galton--Watson trees*, arXiv:1805.09425, 2018. https://arxiv.org/abs/1805.09425
