# Two timescales of transient amplification and positivity recovery on unbalanced bipartite graphs

## Finding

Let \(m,n\) be integers with \(m\ge2\) and \(n\ge32m\). On the unit-conductance complete bipartite graph \(K_{m,n}\), let \(L\) be the unnormalized graph Laplacian and \(T(t)=\exp(-tL^2)\) for \(t\ge0\). Write \(N=m+n\), and define
\[
 F_A(t)=N e^{-n^2t}-m-n e^{-N^2t},\qquad
 F_B(t)=N e^{-m^2t}-n-m e^{-N^2t},
\]
\[
 d_A(t)=\frac{m-1}{mN}[F_A(t)]_+,\qquad
 d_B(t)=\frac{n-1}{nN}[F_B(t)]_+,
 \quad [r]_+=\max\{r,0\}.
\]
For every \(t\ge0\) the **exact, attained endpoint norm** is
\[
 \|T(t)\|_{\ell^1\to\ell^1}
 =\|T(t)\|_{\ell^\infty\to\ell^\infty}
 =1+2\max\{d_A(t),d_B(t)\}.
\]
It reaches its unique maximum at
\[
 \theta_{m,n}=\frac{\log(N/m)}{n(n+2m)}.
\]
The exact maximal endpoint norm is
\[
 \boxed{\mathcal M_{m,n}=1+
 \frac{2(n-1)}N\left[
 \frac{n+2m}{N}
 \left(\frac mN\right)^{m^2/[n(n+2m)]}-1\right].}
\]
For a fixed vertex of the \(n\)-vertex part, an extremizing sign input is \(+1\) on that vertex and the entire \(m\)-vertex part, and \(-1\) at every other vertex of the \(n\)-vertex part.

There is a unique positive number \(\tau_{m,n}\) solving
\[
 N e^{-m^2\tau_{m,n}}-n-m e^{-N^2\tau_{m,n}}=0.
\]
The matrix \(T(t)\) is entrywise nonnegative **exactly** at \(t=0\) and at \(t\ge\tau_{m,n}\); it is strictly positive for \(t>\tau_{m,n}\). Its only negative entries for \(2/n^2\le t<\tau_{m,n}\) occur between distinct vertices in the \(n\)-vertex part.

For **every** sequence of integer pairs satisfying \(m\ge2\) and \(n/m\to\infty\), the amplification peak and the positivity recovery horizon obey the distinct scales
\[
 \mathcal M_{m,n}-1\sim\frac{2m}{n},\qquad
 \theta_{m,n}\sim\frac{\log(n/m)}{n^2},\qquad
 \tau_{m,n}\sim\frac1{mn},
\]
\[
 \boxed{\frac{\tau_{m,n}}{\theta_{m,n}}\sim
 \frac{n/m}{\log(n/m)}\longrightarrow\infty.}
\]
Thus a vanishingly small worst-case signed excursion can persist, through its last negative kernel entries, for a parametrically longer time than the time of greatest amplification.

## Assumptions and scope

The graph is finite, simple, undirected, and unweighted; the two vertex classes have cardinalities \(m\) and \(n\). The Laplacian convention is \((Lf)(v)=\deg(v)f(v)-\sum_{w\sim v}f(w)\). Counting measure is used for all sequence norms. No rescaling of time or Laplacian is implicit. The unbalanced condition \(n\ge32m\) is sufficient for the asserted unique winning peak; optimality of this numerical cutoff is not claimed. The asymptotic assertion allows \(m\) to vary and does not require it to be fixed.

## Proof

**Spectral kernel.** Decompose the vertex space orthogonally into constants (eigenvalue \(0\)), the one-dimensional contrast between the parts (eigenvalue \(N\)), mean-zero vectors supported on the \(m\)-vertex part (eigenvalue \(n\)), and mean-zero vectors supported on the \(n\)-vertex part (eigenvalue \(m\)). Their spectral projections are explicit. In the first part the contrast projector has each entry \(n/(mN)\); in the second it has each entry \(m/(nN)\); its cross-part entries are \(-1/N\). The mean-zero projectors on each part are the identity minus the all-ones matrix divided by that part's size. Consequently, distinct entries in the first part are
\[
 a(t)=\frac{m+n e^{-N^2t}-N e^{-n^2t}}{mN}
      =-\frac{F_A(t)}{mN},
\]
while distinct entries in the second part are
\[
 b(t)=\frac{n+m e^{-N^2t}-N e^{-m^2t}}{nN}
      =-\frac{F_B(t)}{nN}.
\]
All cross-part entries are \((1-e^{-N^2t})/N\), which are positive for \(t>0\). Diagonal entries are \(a(t)+e^{-n^2t}\) and \(b(t)+e^{-m^2t}\), strictly positive because the matrix exponential of a symmetric matrix is positive definite. Every row sums to one because \(L\mathbf1=0\). The sum of absolute values in a row is therefore one plus twice the mass of its negative entries. This gives the claimed exact operator norm for every time, and equality is attained by taking the signs of a maximizing row. Symmetry gives the identical \(\ell^1\) norm.

**The two candidate peaks.** Differentiation gives
\[
 F_A'(t)=nN e^{-n^2t}\big(N e^{-[N^2-n^2]t}-n\big),
\]
\[
 F_B'(t)=mN e^{-m^2t}\big(N e^{-[N^2-m^2]t}-m\big).
\]
Each is positive initially, changes sign exactly once, and is negative thereafter. Because both \(F_A\) and \(F_B\) equal zero at \(t=0\) and tend to negative constants, each has exactly one positive zero. The unique positive peak of \(F_A\) is at \(\log(N/n)/[m(m+2n)]\), and that of \(F_B\) is at the asserted \(\theta_{m,n}\).

To prove which peak wins, write \(q=m/n\le1/32\). From \(1-e^{-u}\le u\),
\[
 F_A(t)=m(e^{-n^2t}-1)+n(e^{-n^2t}-e^{-N^2t})
 \le nm(m+2n)t e^{-n^2t}.
\]
Since \(\sup_{t\ge0}t e^{-n^2t}=1/(en^2)\),
\[
 \sup_{t\ge0}d_A(t)\le\frac{(m-1)(m+2n)}{enN}
 <\frac{2m}{en}<\frac{3m}{4n}.
\]
At the peak of \(F_B\), the derivative equation implies \(e^{-N^2\theta_{m,n}}=(m/N)e^{-m^2\theta_{m,n}}\). The bound \(e^{-u}\ge1-u\) therefore yields
\[
 d_B(\theta_{m,n})\ge\frac mn
 \left(1-\frac1n\right)(1+q)^{-2}
 \left(1-q\log(1+1/q)\right).
\]
The four elementary inequalities \(n\ge64\), \(q\le1/32\), \((32/33)^2>93/100\), and \(q\log(1+1/q)<1/8\) make this strictly larger than
\[
 \frac mn\cdot\frac{49}{50}\cdot\frac{93}{100}\cdot\frac78
 >\frac{3m}{4n}.
\]
The last comparison uses \(e>8/3\). Hence no value of \(d_A\) can equal the single global maximum of \(d_B\); the overall peak is unique. Substitution of the derivative relation gives the displayed exact formula for \(\mathcal M_{m,n}\).

**Recovery horizon and negativity location.** At \(t_0=2/n^2\),
\[
 F_A(t_0)\le m\left[e^{-2}(1+2(2+q))-1\right]<0,
\]
whereas
\[
 F_B(t_0)\ge m\left[1-e^{-2}-2q(1+q)\right]>0.
\]
By the one-peak/one-positive-root property, the positive zero of \(F_A\) occurs before \(t_0\), and the positive zero \(\tau_{m,n}\) of \(F_B\) occurs afterward. The explicit sign pattern of the kernel now proves the complete positivity-time assertion and the claim about the location of negative entries.

**Separated scales.** Set \(q=m/n\to0\). The exact peak time is
\[
 \theta_{m,n}=\frac{\log(1+1/q)}{n^2(1+2q)}.
\]
At the peak, \(m^2\theta_{m,n}=q^2\log(1+1/q)/(1+2q)\to0\). The peak formula then gives \(\mathcal M_{m,n}-1\sim2q\). For any fixed \(c>0\), evaluate the defining sign function of the recovery horizon at \(t=c/(mn)\):
\[
 \frac{F_B(c/(mn))}{m}
 =\frac{(1+q)e^{-cq}-1}{q}
 -e^{-c(1+q)^2/q}\longrightarrow 1-c.
\]
Its unique positive root is consequently located at \(\tau_{m,n}\sim1/(mn)\), by bracketing with arbitrary \(c<1<c'\). Combining these expressions proves the divergent ratio of the two time scales.

## Verification

The accompanying `verify.py` constructs actual graph Laplacians and independently computes \(\exp(-tL^2)\) for many small bipartite graphs; it checks every kernel-entry type and the exact endpoint norm, and probes the large-imbalance inequalities, positivity roots, and scale limits. Run `python verify.py` after installing the packages in `requirements.txt`. A successful run prints `CHECKS_OK 3618`. This number counts explicit program assertions, not a proof of the infinite-parameter theorem. The analytic arguments above establish all quantified claims independently of finite numerical experiments.

## Relationship to prior work

Daners, Glück and Kennedy developed spectral and order-theoretic criteria for eventual positivity of semigroups, including examples with fourth-order generators; their results motivate the quantitative question here, but do not determine the two sharp time scales of this family. Yamagishi obtained exact discrete Sobolev constants, ordinary heat kernels, and Green matrices on balanced complete bipartite graphs; the operator in that work is \(e^{-tL}\), not the squared-generator evolution considered here. General three-spectral-level positivity structure does not settle the present genuinely four-level, unbalanced case. The contribution is the full explicit endpoint norm coupled to an **attained unique peak, sharp positivity horizon, and asymptotically divergent peak-to-recovery separation**.

## Limitations

The bound \(n\ge32m\) is a convenient provable regime, not the exact smallest imbalance for the global peak selection. No assertion is made for weighted graphs, alternate Laplacian normalization, or arbitrary spectral powers. The equations for the finite positivity horizon are implicit rather than elementary closed forms. Historical novelty has been checked against the identified related sources and searchable records, but global bibliographic completeness and independent validation are not claimed.

## References

1. D. Daners, J. Glück, J. B. Kennedy, *Eventually and asymptotically positive semigroups on Banach lattices*, arXiv:1511.05294, first public version 17 November 2015, https://arxiv.org/abs/1511.05294 .
2. H. Yamagishi, *The best constant of the discrete Sobolev inequalities on the complete bipartite graph*, Mathematical Journal of Okayama University 64 (2022), 31–45, https://www.math.okayama-u.ac.jp/mjou/mjou64/_03_yamagishi.pdf .
