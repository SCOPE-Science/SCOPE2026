# An age-resolved leaf susceptibility profile for random recursive-tree path length

## Finding

**Theorem (marked-leaf path-length susceptibility).** For each integer \(n\ge2\), construct a uniformly random recursive tree on \(\{1,\ldots,n\}\), with root \(1\), by independently attaching each vertex \(t\in\{2,\ldots,n\}\) to a uniformly chosen earlier vertex. Let \(T_n\) be the sum of the graph distances of all vertices to the root; let \(I_{n,j}\) indicate that nonroot vertex \(j\) has no children in the final tree. Put \(H_k=\sum_{r=1}^k 1/r\), with \(H_0=0\). Then for each \(2\le j\le n\),

\[
\Pr(I_{n,j}=1)=\frac{j-1}{n-1},\qquad
\mathbb E[T_n\mid I_{n,j}=1]
=n(H_n-1)-(H_{n-1}-H_{j-1}),
\]

\[
\boxed{\operatorname{Cov}(I_{n,j},T_n)
=-\frac{j-1}{n-1}(H_{n-1}-H_{j-1}).}
\]

Thus the covariance is negative for every \(2\le j<n\) and zero for \(j=n\). The absolute covariance profile is discretely concave in \(j\): successive differences decrease strictly. Every maximizing birth rank \(j_n\) satisfies \(j_n/n\to e^{-1}\), and

\[
\boxed{\max_{2\le j\le n}|\operatorname{Cov}(I_{n,j},T_n)|\longrightarrow e^{-1}.}
\]

More precisely, if \(j_n/n\to x\in[0,1]\), then
\[
\operatorname{Cov}(I_{n,j_n},T_n)\longrightarrow x\log x,
\]
where \(0\log0:=0\). As an aggregate consequence, the total leaf count \(L_n=\sum_{j=2}^n I_{n,j}\) obeys
\[
\operatorname{Cov}(L_n,T_n)=-\frac{n-2}{4}.
\]
The **birth-rank-specific** conditional/covariance profile, rather than the unmarked aggregate covariance, is the distinct claim of the theorem.

## Assumptions and scope

Every attachment choice is independent and uniformly distributed among all earlier vertices. Depth uses unit edges, the root has depth zero, and “leaf” means outdegree zero in this rooted tree. The result holds for every finite integer \(n\ge2\); the root is not included among leaf indicators. At \(n=2\), the vertex \(j=2\) is deterministically a leaf and all stated covariances are zero. The asymptotic statements require only the indicated limit of the integer birth ranks; no exchangeability of birth labels is assumed.

## Proof

**1. Unconditional means.** Write \(P_t\) for the parent of vertex \(t\), \(D_t\) for its depth, and \(T_t=\sum_{r=1}^t D_r\). The recursion \(D_t=1+D_{P_t}\) and the independence of \(P_t\) from the previous tree give \(\mathbb E D_t=1+\frac1{t-1}\sum_{r=1}^{t-1}\mathbb E D_r=H_{t-1}\) by induction. Hence \(\mathbb E T_n=\sum_{t=1}^nH_{t-1}=n(H_n-1)\).

**2. Marking a leaf.** Fix \(j\ge2\). The event \(I_{n,j}=1\) means precisely that \(P_t\ne j\) for every \(t=j+1,\ldots,n\). The independent choices before or at time \(j\) retain their laws, and the later choices remain independent, each uniform on \(\{1,\ldots,t-1\}\setminus\{j\}\). Multiplying their probabilities gives
\[\Pr(I_{n,j}=1)=\prod_{t=j+1}^n\frac{t-2}{t-1}=\frac{j-1}{n-1}.\]

Set \(M_t=\mathbb E[T_t\mid I_{n,j}=1]\). For \(t\ge j\), the marked vertex has unchanged expected depth \(d_j=H_{j-1}\). At \(t=j\), \(M_j=j(H_j-1)\). For \(t=j+1,\ldots,n\), excluding vertex \(j\) as a parent gives the exact recursion
\[
M_t=M_{t-1}+1+\frac{M_{t-1}-d_j}{t-2}
=\frac{t-1}{t-2}M_{t-1}+1-\frac{d_j}{t-2}.
\]
Divide by \(t-1\), telescope, and use \(\sum_{t=j+1}^n1/((t-1)(t-2))=1/(j-1)-1/(n-1)\):
\[
\frac{M_n}{n-1}=\frac{j(H_j-1)}{j-1}+H_{n-1}-H_{j-1}-H_{j-1}\left(\frac1{j-1}-\frac1{n-1}\right)
=H_{n-1}-1+\frac{H_{j-1}}{n-1}.
\]
Consequently \(M_n=(n-1)(H_{n-1}-1)+H_{j-1}=n(H_n-1)-(H_{n-1}-H_{j-1})\). Multiplying its difference from the unconditioned mean by \(\Pr(I_{n,j}=1)\) yields the claimed covariance.

**3. Discrete concavity.** Let \(N=n-1\), \(m=j-1\), and \(F_N(m)=m(H_N-H_m)\), for \(1\le m\le N\). Direct subtraction gives
\[
F_N(m+1)-F_N(m)=H_N-H_m-1\quad(1\le m<N).
\]
This is strictly decreasing in \(m\), proving discrete concavity and at most two adjacent maximizers. The covariance is \(-F_N(m)/N\). Uniformly in \(1\le m\le N\), integral comparison for harmonic sums gives \(H_N-H_m=\log(N/m)+O(1/m)\), hence
\[
\sup_{1\le m\le N}\left|\frac{F_N(m)}N-\frac mN\log\frac Nm\right|=O(1/N).
\]
The continuous function \(x\log(1/x)\), extended by zero at \(x=0\), is uniquely maximized at \(x=e^{-1}\) with value \(e^{-1}\). The covariance profile, maximizing ranks, and asymptotic assertions follow.

**4. Aggregate consequence.** Since \(L_n=\sum_{j=2}^n I_{n,j}\), linearity of covariance and exchange of finite sums yield
\[
-\operatorname{Cov}(L_n,T_n)
=\frac1N\sum_{m=1}^{N}m\sum_{t=m+1}^{N}\frac1t
=\frac1N\sum_{t=2}^{N}\frac1t\sum_{m=1}^{t-1}m
=\frac1N\sum_{t=2}^{N}\frac{t-1}{2}=\frac{n-2}{4}.
\]

## Verification

The accompanying `verify.py` independently enumerates all recursive trees on \(n=2,\ldots,9\) by their parent arrays (\(46{,}233\) trees in total) and checks, in exact rational arithmetic, the unconditioned mean, every leaf probability, every marked conditional mean, every local covariance, and the aggregate covariance. It also checks the discrete-concavity difference formula and aggregate harmonic identity for \(n=2,\ldots,60\). Finite enumeration checks the algebra at those orders only; the proof above establishes the full domain and asymptotics.

## Relationship to prior work

Janson's 2020 study places random recursive trees among logarithmic-height random-tree families and provides the age/scale context and a probability-first classification (arXiv:2005.13832v1, Sections 12–14). Dobrow and Fill study total path length in random recursive trees (1999); Zhang studies leaf-count fluctuations (2015); Altok and Işlak consider leaf-related statistics (2017). These establish background marginals, not the conditional total-path-length profile indexed by the exact birth rank of a fixed marked vertex.

Lundblad and Wagner (2026), *Path Length and External Path Length in Random Trees*, Section 5, equation (13), provide a joint exponential generating function for **unmarked** leaf number, total path length, and external path length. Their exact generating function implicitly covers the unmarked aggregate covariance displayed here; **that aggregate formula is not asserted as a new independent result**. Their generating function does not retain the nonexchangeable birth-rank label \(j\), which is essential to the present marked-event profile and sharp \(1/e\) maximizing-rank statement. An age marking could be added to established generating-function methods, but it is not part of their displayed theorem. Published claims on root-child attachment and root degree in recursive trees concern different mark events and do not imply the displayed conditional expectation.

## Limitations

This theorem concerns only a single **first conditional moment** of the total path length given one specified final leaf; it does not give the conditional distribution, conditional variance, or a stochastic-order comparison. It does not claim that the overall leaf-count versus total-path-length covariance is historically new: the unmarked joint generating function already implies it. The possible presence of a marked-vertex specialization in older recursive-tree enumeration and uninspected full papers remains an originality risk. The theorem has not undergone independent validation.

## References

- S. Janson, *Tree limits and limits of random trees*, arXiv:2005.13832v1 (first submitted 28 May 2020), https://arxiv.org/abs/2005.13832 .
- R. Dobrow and J. Fill, *Total Path Length for Random Recursive Trees*, Combinatorics, Probability and Computing 8 (1999), 317–333; DOI:10.1017/S0963548399003855.
- H. Zhang, *On the number of leaves in a random recursive tree*, Bernoulli/related journal study (2015); DOI:10.1214/14-BJPS252.
- S. Altok and U. Işlak, *On leaf related statistics in recursive tree models*, Statistics & Probability Letters (2017); DOI:10.1016/j.spl.2016.10.007.
- J. Lundblad and S. Wagner, *Path Length and External Path Length in Random Trees*, AofA 2026, DOI:10.4230/LIPIcs.AofA.2026.2, https://drops.dagstuhl.de/storage/00lipics/lipics-vol381-aofa2026/LIPIcs.AofA.2026.2/LIPIcs.AofA.2026.2.pdf .
