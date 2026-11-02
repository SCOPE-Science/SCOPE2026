# Reinforcement creates a strict arrival-time hierarchy of leaf covariances in growing recursive trees

## Finding

For every real reinforcement parameter \(\alpha\ge 0\), let \(T_n\) be the increasing rooted tree with vertex set \(\{1,\ldots,n\}\) in which, at step \(m+1\), a vertex \(v\in\{1,\ldots,m\}\) is chosen as parent with probability
\[
\frac{1+\alpha d_m^+(v)}{s_m},\qquad s_m=(1+\alpha)m-\alpha.
\]
Here \(d_m^+(v)\) is the current number of children. Write \(D_n=d_n^+(1)\), \(L_n=|\{v:d_n^+(v)=0\}|\), and \(I_j=\mathbf 1\{\operatorname{parent}(j)=1\}\). For \(n\ge j\ge3\), put \(w_{j,n}=\operatorname{Cov}(I_j,L_n)\).

Define positive deterministic sequences, for \(m\ge2\), by
\[
r_2=1+\alpha,\quad h_2=1,\qquad
r_{m+1}=r_m\left(1+\frac\alpha{s_m}\right),\quad
h_{m+1}=h_m\left(1+\frac{\alpha-1}{s_m}\right).
\]
Then the total root-degree/leaf covariance and its individual arrival contributions are exactly
\[
\operatorname{Cov}(D_n,L_n)=C_n=\frac{r_n-(1+\alpha)h_n}{\alpha+2},\qquad
w_{j,n}=q_{j,n}\frac{\alpha C_{j-1}+r_{j-1}/(\alpha+2)}{s_{j-1}},
\]
where \(q_{j,n}=\prod_{t=j}^{n-1}(1-1/s_t)\), with an empty product equal to one. In particular, \(C_2=0\), \(C_n>0\) for \(n\ge3\), and \(w_{j,n}>0\) for every \(3\le j\le n\).

**Sharp arrival-time hierarchy.** For every \(3\le j<n\),
\[
\boxed{w_{j+1,n}-w_{j,n}
=q_{j+1,n}\frac{\alpha(\alpha+1)h_{j-1}}{(\alpha+2)s_{j-1}s_j}.}
\]
Thus, at zero reinforcement the contributions are all equal, whereas for every strictly positive reinforcement they are strictly increasing with arrival time:
\[
\alpha=0:\quad w_{3,n}=\cdots=w_{n,n}=\frac1{2(n-1)},
\qquad
\alpha>0:\quad 0<w_{3,n}<\cdots<w_{n,n}.
\]
For each \(n\ge3\), these contributions sum to \(C_n\). The equality regime is consequently *exactly* the uniform-attachment boundary.

For fixed \(\alpha>0\), with \(\delta=\alpha/(\alpha+1)\),
\[
C_n\sim\frac{\alpha+1}{\alpha+2}\,\Gamma(2-\delta)\,n^\delta.
\]
In the uniform plane-oriented recursive-tree case \(\alpha=1\), the exact covariance simplifies to
\[
C_n=\frac13\left(\frac{4^{n-1}}{\binom{2n-2}{n-1}}-2\right)
\sim\frac{\sqrt{\pi n}}3.
\]

## Assumptions and scope

The process starts with a single root at time one. Every choice is sampled from the stated conditional distribution. All results are exact for finite \(n\ge2\) and every real \(\alpha\ge0\); the asymptotic statements hold at fixed positive \(\alpha\). A leaf means *zero children*; in particular, the root is not counted as a leaf for \(n\ge2\). The first root attachment \(I_2=1\) is deterministic and is deliberately excluded from the strict hierarchy. At \(\alpha=0\) the process is the classical uniform recursive tree; at \(\alpha=1\) its parent-history projection is the random plane-oriented recursive tree. No assertion of independence, causality, or stochastic-ordering between the indicators is made.

## Proof

**1. One-step conditional identities.** For any \(m\ge2\), abbreviate \(D=D_m\), \(L=L_m\), \(R=1+\alpha D\), \(s=s_m\), \(X=I_{m+1}\), and \(Y=L_{m+1}-L_m\). The new vertex is a leaf. It adds one to the leaf count exactly when its parent is *not* a leaf. Consequently, conditional on the current tree,
\[
\mathbb E[X\mid T_m]=R/s,\qquad
\mathbb E[Y\mid T_m]=1-L/s,\qquad XY=X.
\]
The third identity is valid because the root is already nonleaf. Taking conditional and then unconditional covariances gives
\[
\operatorname{Cov}(X,L)=\frac{\alpha}{s}\operatorname{Cov}(D,L),\qquad
\operatorname{Cov}(D,Y)=-\frac1s\operatorname{Cov}(D,L),
\]
\[
\operatorname{Cov}(X,Y)=\frac{\mathbb ER\,\mathbb EL}{s^2}.
\]
For the last equality, use \(\mathbb E[XY]=\mathbb EX\), then expand \(\mathbb E[X]\mathbb E[Y]\); there is no independence assumption.

**2. Exact means.** The weight normalization follows from \(\sum_v d_m^+(v)=m-1\), so \(\sum_v(1+\alpha d_m^+(v))=s_m\). Let \(r_m=\mathbb E(1+\alpha D_m)\). Since \(D_{m+1}=D_m+X\),
\[
r_{m+1}=r_m(1+\alpha/s_m).
\]
Also \(\mathbb E(L_{m+1}\mid T_m)=L_m+1-L_m/s_m\), which, with \(L_2=1\), solves to \(\mathbb EL_m=s_m/(\alpha+2)\).

**3. Global covariance.** Adding the four covariance terms arising from \(D_{m+1}=D_m+X\) and \(L_{m+1}=L_m+Y\) yields the exact recurrence
\[
C_{m+1}=\left(1+\frac{\alpha-1}{s_m}\right)C_m
+\frac{r_m}{(\alpha+2)s_m},\qquad C_2=0.
\]
The displayed recurrences for \(r_m,h_m\) give, by direct induction,
\(C_m=[r_m-(\alpha+1)h_m]/(\alpha+2)\). The factors defining \(h_m\) are positive because \(s_m\ge m\ge2\). Initially \(r_2=(\alpha+1)h_2\), while each subsequent multiplier of \(r_m\) exceeds that of \(h_m\) by \(1/s_m>0\). Thus \(C_m>0\) for \(m\ge3\).

**4. Individual arrivals.** At its birth, the indicator \(I_j\) has covariance
\[
\operatorname{Cov}(I_j,L_j)=\frac{\alpha C_{j-1}+r_{j-1}/(\alpha+2)}{s_{j-1}}.
\]
For every later step \(m\ge j\), conditioning the leaf increment on the entire tree gives
\[
\operatorname{Cov}(I_j,L_{m+1})=(1-1/s_m)\operatorname{Cov}(I_j,L_m).
\]
Iteration proves the stated formula for \(w_{j,n}\) and its positivity.

**5. Strict hierarchy.** Put \(F_m=\alpha C_m+r_m/(\alpha+2)=(\alpha+1)(r_m-\alpha h_m)/(\alpha+2)\). Since \(s_j-1=s_{j-1}+\alpha\), the step recurrences imply the exact algebraic identity
\[
s_{j-1}F_j-(s_j-1)F_{j-1}
=\frac{\alpha(\alpha+1)}{\alpha+2}h_{j-1}.
\]
Subtracting the consecutive arrival formulas and factoring out \(q_{j+1,n}\) gives precisely the boxed gap identity. All factors other than \(\alpha\) are positive, establishing both its equality and strictness cases. Finally \(D_n=1+\sum_{j=3}^n I_j\); bilinearity of covariance proves \(\sum_{j=3}^n w_{j,n}=C_n\).

**6. Asymptotics.** Set \(\delta=\alpha/(\alpha+1)\) and \(\beta=1/(\alpha+1)\). Product evaluation yields
\[
r_n=(\alpha+1)\frac{\Gamma(n)\Gamma(2-\delta)}{\Gamma(n-\delta)},\qquad
h_n=\frac{\Gamma(n-\beta)\Gamma(2-\delta)}{\Gamma(2-\beta)\Gamma(n-\delta)}.
\]
For fixed \(\alpha>0\), their ratio satisfies \(h_n/r_n=O(n^{-\beta})\), so the Gamma-ratio asymptotic proves the limit law. For \(\alpha=1\), the first product reduces to \(r_n=4^{n-1}/\binom{2n-2}{n-1}\) and \(h_n=1\).

## Verification

The standalone `verify.py` uses exact rational arithmetic. It independently enumerates every recursive parent history through eight vertices, assigning the specified *full-history probability* rather than sampling, for \(\alpha\in\{0,1/2,1,2\}\). It compares direct joint moments with the closed covariance, each arrival contribution, and the strict/equality boundary. Additional exact rational checks cover five parameter values and sizes through 59; the central-binomial formula is checked at the plane-tree parameter. The script reports 2,777 passing assertions. The all-size result is established by the proof above, not by this finite enumeration. Run with `python3 verify.py` from the directory containing this document and the verifier.

## Relationship to prior work

The increasing-tree, preferential-attachment, and leaf-count models are established. Mahmoud, Smythe and Szymański (1993) study root outdegree and marginal leaf statistics for plane-oriented recursive trees; Janson (2008) and Janson, Kuba and Panholzer (2008) study Stirling-permutation correspondences, the classical plane-tree root-degree/Stirling-block correspondence, generalized plane-tree models, and the respective marginal block and leaf statistics. Their accessible manuscript material does not state the cross-statistic arrival-time covariance identity and strict hierarchy proved here. The exact equal contribution at \(\alpha=0\) is previously available in the uniform recursive-tree setting; it is used here as a boundary case, not asserted to be new. The distinction is the strict, explicitly quantified reversal from equal shares to later-arrival dominance at \(\alpha>0\), uniformly across the affine family. The relevant joint distribution might admit an alternative derivation through the classical generating functions or a larger urn process; historical priority is not certified by unsuccessful searches.

## Limitations

The theorem is for affine attachment with nonnegative reinforcement, not arbitrary preferential-attachment kernels, random graph growth with multiple parents, or time-varying parameters. Only covariances are ordered; a stochastic order of the underlying conditional leaf-count distributions is not established. The \(\alpha\downarrow0\) and \(n\to\infty\) limits are not claimed to be uniform. The bibliographic comparison is a bounded originality review, not an independent historical-priority audit.

## References

1. H. M. Mahmoud, R. T. Smythe, and J. Szymański, *On the structure of random plane-oriented recursive trees and their branches*, Random Structures & Algorithms **4** (1993), 151–176. https://doi.org/10.1002/rsa.3240040204
2. S. Janson, *Plane recursive trees, Stirling permutations and an urn model*, arXiv:0803.1129, publicly submitted March 7, 2008. https://arxiv.org/abs/0803.1129
3. S. Janson, M. Kuba, and A. Panholzer, *Generalized Stirling permutations, families of increasing trees and urn models*, arXiv:0805.4084, publicly submitted May 27, 2008. https://arxiv.org/abs/0805.4084
4. S. Janson, *Asymptotic degree distribution in random recursive trees*, Random Structures & Algorithms **26** (2005), 69–83. https://doi.org/10.1002/rsa.20046
