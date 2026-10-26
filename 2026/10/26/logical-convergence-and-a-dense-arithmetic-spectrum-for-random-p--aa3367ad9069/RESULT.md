# Logical convergence and a dense arithmetic spectrum for random partial injections

## Finding
Let \(J_n\) be uniform among all partial injections from an arbitrary subset of \([n]\) into \([n]\). Regard its graph as a structure in the fixed relational signature \(\{R,=\}\). For each fixed first-order sentence \(\varphi\), the limit \(L_\varphi=\lim_{n\to\infty}\Pr(J_n\models\varphi)\) exists. Moreover there is an effectively obtainable positive integer \(D_\varphi\) such that \(L_\varphi\in\mathbb Q[e^{-1/D_\varphi}]\), and the limit is effectively computable from \(\varphi\). The set of these limits, over all such sentences, is dense in \([0,1]\). In particular, the model obeys a first-order convergence law but not a zero-one law.

An explicit family witnessing density is indexed by finite sets \(H\subset\mathbb N_{\ge1}\): the first-order sentence asserting the existence of a directed cycle whose length lies in \(H\) has limit
\[
1-\exp\left(-\sum_{j\in H}\frac1j\right).
\]

## Assumptions and scope
The finite set \([n]\) is the entire vertex universe. A partial injection is a partial map \(f:D\to[n]\), \(D\subseteq[n]\), injective on its domain. Each such map receives equal probability. In the first-order language, \(R(a,b)\) means \(f(a)=b\). Thus \(R\) is a binary relation, **not** a total unary function symbol; undefined values are encoded by vertices with no outgoing edge. Loops are permitted. All formulas are fixed while \(n\to\infty\); all structures have nonempty universe for \(n\ge1\). This is a theorem about finite labelled partial injections, not about uniform permutations or fixed-domain/fixed-codomain injections.

The weak components of the directed graph of \(R\) are directed paths or directed cycles. Write \(P_j\) and \(C_j\) for the numbers of path and cycle components on exactly \(j\ge1\) vertices, respectively; an isolated vertex is a one-vertex path and a fixed point is a one-vertex cycle.

## Proof
**1. Labelled assembly and mixed moments.** A directed path on a specified \(j\)-vertex label set admits \(j!\) linear orientations; a directed cycle has \((j-1)!\) orientations (including \(j=1\)). The exponential generating function for all partial injections is therefore
\[
F(z)=\exp\left(\sum_{j\ge1}z^j+\sum_{j\ge1}\frac{z^j}{j}\right)
=\frac{1}{1-z}\exp\left(\frac{z}{1-z}\right).
\]
Set \(a_n=[z^n]F(z)\), with \(a_m=0\) for \(m<0\). For arbitrary finite nonnegative integer arrays \((u_j),(v_j)\), put \(s=\sum_j j(u_j+v_j)\). Exact differentiation with respect to path and cycle markers gives
\[
\mathbb E\left[\prod_j(P_j)_{u_j}(C_j)_{v_j}\right]
=\frac{a_{n-s}}{a_n}\prod_j j^{-v_j}.
\]
Here \((X)_t=X(X-1)\cdots(X-t+1)\), and the empty product is one. Bassino--Nicaud--Weil's singularity analysis supplies
\[
a_n\sim\frac{e^{-1/2}}{2\sqrt\pi}\,n^{-1/4}e^{2\sqrt n}.
\]
In particular \(a_{n-s}/a_n\to1\) for every fixed \(s\). The method of mixed factorial moments (with Poisson moment determinacy) now yields joint convergence, for each fixed finite set of indices, to mutually independent variables
\[
P_j\Rightarrow\operatorname{Poisson}(1),\qquad
C_j\Rightarrow\operatorname{Poisson}(1/j).
\]
This assertion concerns a finite set of \(j\)'s at a time; it does not claim an infinite-dimensional total-variation limit.

**2. Many long paths.** Let \(X_n=\sum_jP_j\), the total number of path components. The asymptotic \(X_n/\sqrt n\to1\) in probability follows from the component enumeration and its first two moments (Bassino--Nicaud--Weil, Lemma 2.11). For any fixed \(m\), \(\sum_{j\le m}P_j\) is tight by Step 1. Hence \(\sum_{j>m}P_j\to\infty\) in probability. Every sufficiently long directed path contains arbitrarily many copies of the radius-\(r\) interior type for any fixed \(r\), and at least one copy of each possible near-endpoint type that can occur on long paths; in fact the number of long paths diverges.

**3. Locality and arithmetic of limits.** Fix \(\varphi\). By the effective bounded-degree Hanf theorem (Gaifman degree at most two), there are computable \(r\) and \(t\) such that \(\varphi\)'s truth is determined by the counts of all radius-\(r\) rooted neighbourhood isomorphism types, with each count truncated at \(t\). A radius-\(r\) neighbourhood that detects an entire cycle must lie on a cycle of at most \(2r+1\) vertices; a neighbourhood that detects both ends of a path must lie on a path of at most \(2r+1\) vertices. All other realizable neighbourhood types already occur at least \(t\) times with probability tending to one, because sufficiently long path components are abundant. Consequently the limiting Hanf summary is a deterministic Boolean function of the finite vector
\[
\bigl(\min(P_j,t),\min(C_j,t)\bigr)_{1\le j\le 2r+1},
\]
with certain coordinates possibly immaterial. The joint Poisson limit in Step 1 proves convergence of the probability of each summary.

For a Poisson count with rational mean \(\lambda\), the probability of a specified count below \(t\) is \(e^{-\lambda}\lambda^i/i!\), and the probability of reaching the cap is \(1-e^{-\lambda}\sum_{i<t}\lambda^i/i!\). Finite sums and products of these probabilities lie in \(\mathbb Q[e^{-1/D}]\) for \(D=\operatorname{lcm}(1,2,\ldots,2r+1)\), since every mean is either \(1\) or \(1/j\) with \(j\le2r+1\). Enumeration of the finitely many capped count vectors and a canonical Hanf representative yields an effective computation of \(L_\varphi\). The effective Hanf radius may be chosen at least one, so \(D\) is well-defined.

**4. Density and failure of a zero-one law.** For any finite \(H\subset\mathbb N_{\ge1}\), a fixed first-order sentence can assert that at least one cycle has length in \(H\). Independence of the limiting \(C_j\)'s gives exactly the displayed probability. Given any positive real \(s\) and tolerance \(\varepsilon>0\), choose \(N\) with \(1/N<\varepsilon\); the partial sums \(\sum_{j=N}^M1/j\) eventually exceed \(s\), and the first such sum differs from \(s\) by less than \(\varepsilon\). Thus limits of the form \(1-e^{-\sum_{j=N}^M1/j}\) approximate any point of \((0,1)\); contradictory and valid sentences supply endpoints. The one-cycle sentence already has limiting probability \(1-e^{-1}\in(0,1)\), excluding a zero-one law.

## Verification
The companion `verify_partial_injection.py` runs using only the Python 3 standard library. It exactly enumerates 15,126 partial injections on domains of sizes \(0\) through \(6\), verifies the coefficient recurrence and twelve mixed factorial-moment identities at each size, and computes coefficient-ratio diagnostics at \(n=20,100,500\). The expected signal is `PARTIAL_INJECTION_EXACT_OK 15126 12` followed by three increasing ratios below one. The finite calculations check enumerative algebra, not Hanf locality or asymptotic convergence; those rest on the cited theorems and the argument above.

## Relationship to prior work
Bassino, Nicaud and Weil (arXiv:0707.3185, §§2.2--2.3) established the partial-injection component enumeration, coefficient asymptotic and path-count concentration used here. Stark (2021, DOI 10.37236/9496, §§2--4) studied cycle/path components and Poisson approximations for a distinct fixed-domain/fixed-codomain random injection model; his work establishes substantial prior component-probability machinery. Effective Hanf locality on degree-bounded structures is standard (Kuske--Schweikardt, arXiv:1703.01122). Compton's earlier logical approach to asymptotic combinatorics may subsume the bare convergence-law conclusion through general decomposable-class results; the explicit rational-exponential arithmetic spectrum and density for this precise uniform partial-injection model are the separately assessed conclusions. Kuželka (arXiv:2608.30580, first posted 2026-08-31) concerns exact enumeration/complexity with genuine total unary function symbols rather than this random binary-relation ensemble.

## Limitations
This is a specialization to one binary edge relation satisfying both indegree and outdegree at most one, without additional vertex colours, orders or function symbols. The integer \(D_\varphi\) need not be minimal, and no useful computational-complexity bound is asserted for the effective procedure. Neither an unrestricted number of simultaneously varying cycles nor a quantitative finite-\(n\) convergence rate is claimed. Classical enumeration and locality are not new. The historical-priority comparison cannot exclude an earlier specialized or more general theorem proving the complete arithmetic-and-density conclusion.

## References
1. O. Kuželka, *Unary Functions, Automorphisms, and Unlabeled First-Order Model Counting*, arXiv:2608.30580, first posted 2026-08-31, https://arxiv.org/abs/2608.30580.
2. F. Bassino, C. Nicaud and P. Weil, *Random generation of finitely generated subgroups of a free group*, arXiv:0707.3185, especially Section 2, https://arxiv.org/pdf/0707.3185.
3. D. Stark, *The Component Counts of Random Injections*, Electronic Journal of Combinatorics 28(1) (2021), P1.5, https://doi.org/10.37236/9496.
4. D. Kuske and N. Schweikardt, *First-Order Logic with Counting: At Least, Weak Hanf Normal Forms Always Exist and Can Be Computed!*, arXiv:1703.01122, https://arxiv.org/abs/1703.01122.
5. K. J. Compton, *A logical approach to asymptotic combinatorics. I. First order properties*, Advances in Mathematics 65 (1987), 65--96.
