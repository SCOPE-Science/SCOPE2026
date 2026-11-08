# A nondegenerate almost-sure primordial-degree limit in random recursive two-complexes

## Finding

In the RRSC(2) growth model described below, let \(D_n\) be the graph degree of the first vertex at size \(n\). Set \(\gamma=(3-\sqrt5)/2\). There is an almost surely finite, nonnegative, nondegenerate random variable \(W\) such that
\[
n^{-\gamma}(D_n+1)\longrightarrow W\quad\text{almost surely}.
\]
Moreover, with \(\mathcal J\) the entire sequence of vertex-versus-edge selection types, the limit has finite conditional second moment almost surely, and \(\operatorname{Var}(W\mid\mathcal J)>0\) on an event of probability at least \(2/3\). Thus the predicted exponent admits an almost-sure stochastic limit, not merely a mean-field interpretation. No explicit density or strictly positive almost-sure lower bound for \(W\) is asserted.

## Assumptions and scope

Start with one vertex; the second vertex joins it deterministically. At each later step, choose uniformly among all vertices and all edges (each counted once) in the existing simplicial complex. If a vertex is chosen, join the new vertex to it by an edge; if an edge is chosen, join the new vertex to both endpoints and add the filled triangular face. All prior faces persist. Let \(T_n\) count triangular faces and \(E_n\) count edges at size \(n\). Then \(E_n=n-1+T_n\) for \(n\ge2\). Let \(J_n\in\{0,1\}\) indicate whether an edge is selected at step \(n\to n+1\); write \(\mathcal J=\sigma(J_n:n\ge2)\). This is the actual RRSC(2) model, not a fixed-dimensional facet-only attachment model.

## Proof

**1. Control the random environment.** Given the past, \(J_n\) is Bernoulli with parameter
\[
q_n=\frac{n-1+T_n}{2n-1+T_n},\qquad T_{n+1}=T_n+J_n.
\]
Put \(r=(\sqrt5-1)/2\), \(h=2+r\), \(\varphi=1+r\), and \(U_n=T_n-rn\). The identities \(\varphi=rh\) and \(1-r=1/h=\gamma\) give
\[
q_n-r=a_nU_n+c_n,\quad a_n=\frac{n}{(hn-1+U_n)(hn-1)},\quad c_n=-\frac{1}{h(hn-1)}.
\]
Because \(0\le T_n\le n-2\), direct bounds give \(0\le a_n\le 1/(3n)\) and \(|c_n|\le C/n\) for every \(n\ge2\). Expanding \(U_{n+1}=U_n+J_n-r\), using \(\mathbb E[(J_n-r)^2\mid\mathcal F_n]\le1\), and applying \(2|c_nU_n|\le U_n^2/(6n)+C_1/n\), yields
\[
\mathbb E U_{n+1}^2\le \left(1+\frac5{6n}\right)\mathbb E U_n^2+C_2.
\]
Induction gives \(\mathbb E U_n^2\le C_3\, n\). Hence Cauchy–Schwarz and Tonelli give \(\sum_{n\ge2}(1+|U_n|)/n^2<\infty\) almost surely. As \(E_n=\varphi n-1+U_n\ge n-1\), it follows that
\[
\sum_{n\ge2}\left|E_n^{-1}-(\varphi n)^{-1}\right|<\infty,
\qquad \sum_{n\ge2}\frac{|q_n-r|}{n}<\infty
\]
almost surely. The series \(\sum_{n\ge2}(J_n-q_n)/n\) converges almost surely by the bounded-increment square-integrable martingale convergence theorem. Thus \(\sum_{k=2}^{n-1}J_k/k-r\log n\) has a finite almost-sure limit.

Define the environment-dependent positive product
\[
G_2=1,\qquad G_n=\prod_{k=2}^{n-1}\left(1+\frac{J_k}{E_k}\right).
\]
Since \(\log(1+J_k/E_k)=J_k/E_k+O(k^{-2})\), the preceding absolutely convergent and martingale series prove
\[
\frac{G_n}{n^{\gamma}}\longrightarrow g(\mathcal J)\in(0,\infty)\quad\text{almost surely},
\qquad \gamma=\frac r\varphi=\frac{3-\sqrt5}{2}.
\]

**2. Conditional martingale and convergence.** Put \(A_n=D_n+1\), so \(A_2=2\). Conditional on the entire type sequence \(\mathcal J\), selection identities remain uniform: the type sequence is generated from face counts alone and future types are independent of which vertices or edges previously received attachments. Consequently the increment \(B_n=D_{n+1}-D_n\) is Bernoulli with conditional probability \(D_n/E_n\) if \(J_n=1\), and \(1/n\) if \(J_n=0\). With
\[
\alpha_n=\frac{J_n}{E_n},\qquad
\beta_n=\frac{1-J_n}{n}-\frac{J_n}{E_n},\qquad
\xi_{n+1}=B_n-(\alpha_nA_n+\beta_n),
\]
we have the exact conditional recursion
\[
\frac{A_n}{G_n}=2+\sum_{k=2}^{n-1}\frac{\beta_k}{G_{k+1}}
 +\sum_{k=2}^{n-1}\frac{\xi_{k+1}}{G_{k+1}}.
\]
For almost every fixed environment, \(|\beta_k|\le C/k\) and \(G_k\sim g k^{\gamma}\); hence the deterministic drift series converges absolutely. Its conditional expectation formula implies \(\mathbb E[A_n\mid\mathcal J]\le C(\mathcal J)G_n\). Since \(A_n\ge2\), the conditional Bernoulli variance satisfies
\[
\mathbb E[\xi_{n+1}^2\mid\mathcal J]\le
\mathbb E[B_n\mid\mathcal J]\le \frac{\mathbb E[A_n\mid\mathcal J]}{n-1}.
\]
It follows that the conditional quadratic variation of the martingale sum is bounded by \(C(\mathcal J)\sum_{n\ge2}(nG_n)^{-1}<\infty\). Thus \(A_n/G_n\) converges almost surely and in conditional \(L^2\) to a finite nonnegative random variable \(Z\). The product convergence gives the asserted almost-sure limit \(W=g(\mathcal J)Z\), with finite conditional second moment.

**3. Nondegeneracy.** The event \(J_2=0\) has probability \(2/3\). On this event, independently of all later types, the third vertex chooses one of the two old vertices uniformly. Therefore \(A_3=2\) or \(3\) with conditional probability \(1/2\) each; moreover \(G_3=1\). For each fixed subsequent type sequence, the conditional expected difference between evolutions started with \(A_3=3\) and \(A_3=2\) is exactly \(G_n\): subtract the two linear expectation recursions, whose inhomogeneous \(\beta_k\) terms cancel. Conditional \(L^2\) convergence permits taking the limit, so the two conditional means of \(W\) differ by \(g(\mathcal J)>0\). By the total-variance identity,
\[
\operatorname{Var}(W\mid\mathcal J)\ge \tfrac14 g(\mathcal J)^2
\quad\text{on }\{J_2=0\}.
\]
In particular the limiting law is not a point mass, completing the proof.

## Verification

Run `python3 checker.py` using only the Python standard library. It enumerates complete small complexes through six vertices, compares exact transition probabilities after projecting to triangular-face count and primordial degree, and separately iterates the reduced Markov chain through nine vertices. The reproducible run yielded 3300 exact-rational assertions passed. The infinite theorem is proved by the estimates above, not by finite enumeration.

## Relationship to prior work

Krapivsky and Lucas, *Random Recursive Simplicial Complexes* (first released 2026-08-27), Section V.2, equations (73)–(81), predicts the same exponent for the primordial degree from a mean-field replacement and reports simulated non-self-averaging; it explicitly says a proof of non-self-averaging is lacking. The present statement instead proves almost-sure convergence after normalization and nondegeneracy, conditional on the entire simplex-type environment. Fountoulakis, Iyer, Mailler and Sulzbach (2019/2022), *Dynamical Models for Random Simplicial Complexes*, investigate evolving complexes by selection of faces of a fixed dimension and prove empirical-degree-distribution results, not this pooled vertex-or-edge primordial-degree limit. That paper's Remark 3 describes variable-dimension attachment as a possible generalization but does not state this theorem.

## Limitations

No formula for the law of \(W\), its unconditional moments, or positivity \(W>0\) almost surely is established. A nondegenerate conditional limit does not by itself establish an asymptotic coefficient for the unconditional degree variance. No result is asserted for general RRSC(\(m\)) with \(m\ge3\), maximal vertex degrees, or degree-profile tails. Priority conclusions are restricted to the sources materially examined.

## References

1. P. L. Krapivsky and M. Lucas, *Random Recursive Simplicial Complexes*, arXiv:2608.26547 (first public 2026-08-27), https://arxiv.org/abs/2608.26547, especially Section V.2.
2. N. Fountoulakis, T. Iyer, C. Mailler and H. Sulzbach, *Dynamical Models for Random Simplicial Complexes*, arXiv:1910.12715 (2019; 2022 revision), https://arxiv.org/html/1910.12715v3, Sections 1.1–1.4 and Remark 3.
