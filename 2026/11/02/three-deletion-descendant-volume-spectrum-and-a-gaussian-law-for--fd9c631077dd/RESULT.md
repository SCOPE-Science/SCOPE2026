# Three-deletion descendant-volume spectrum and a Gaussian law for random multisets

## Finding

Fix integers \(q\ge2\), \(n\ge t\ge1\). A length-\(n\) multiset on \(q\) labeled symbols is identified with \(x=(x_1,\dots,x_q)\in\mathbb Z_{\ge0}^q\), \(\sum_i x_i=n\); the set is \(\mathcal S_{n,q}\). An exact \(t\)-deletion descendant is \(x-d\) for \(d\in\mathcal S_{t,q}\), coordinatewise \(d\le x\). Write \(Z_t(x)\) for the *number of distinct descendants*, and let \(X\) be uniform on \(\mathcal S_{n,q}\).

Set \(N_{n,q}=\binom{n+q-1}{q-1}\) and \(B(a,q)=\binom{a+q-1}{q-1}\) for integers \(a\ge0\), with \(B(a,q)=0\) for \(a<0\). For all parameters,
\[
\mathbb EZ_t=\binom{t+q-1}{q-1}\frac{B(n-t,q)}{N_{n,q}}.
\]
Put \(P_{q-1}(z)=\sum_{j=0}^{q-1}\binom{q-1}{j}^2z^j\), \(c_{q,m}=[z^m]P_{q-1}(z)(1-z)^{-(q-1)}\). Then
\[
\mathbb EZ_t^2=\frac1{N_{n,q}}\sum_{m=0}^t c_{q,m} B(t-m,q) B(n-t-m,q),\qquad
\operatorname{Var}Z_t=\mathbb EZ_t^2-(\mathbb EZ_t)^2.
\]
The coefficient identity defining \(c_{q,m}\) is previously published, not a new result; the two formulas above count *one-sided descendant volumes*, not ordinary same-level deletion-metric balls.

For \(t=3\), let \(K(x)=|\{i:x_i\ge1\}|\), \(H(x)=|\{i:x_i\ge2\}|\), and \(J(x)=|\{i:x_i\ge3\}|\). Exactly
\[
Z_3(x)=\binom{K(x)}3+(K(x)-1)H(x)+J(x).
\]
This also yields a **complete finite histogram**. Define, for integers \(0\le j\le h\le k\le q\),
\[
R_{n}(k,h,j)=\begin{cases}
  1,&j=0,\ n=k+h,\\
  \binom{n-k-h-1}{j-1},&j\ge1,\ n\ge k+h+j,\\
  0,&\text{otherwise}.
\end{cases}
\]
Then for every integer \(v\),
\[
\#\{x\in\mathcal S_{n,q}:Z_3(x)=v\}=
\sum_{\substack{1\le k\le\min(q,n)\\0\le j\le h\le k\\\binom k3+(k-1)h+j=v}}
\binom qk\binom kh\binom hj R_n(k,h,j).
\]
In particular the formula determines *all* possible volumes and their frequencies, including when \(n\) is comparable with \(q\).

For each fixed integer \(t\ge2\), if \(q\to\infty\) and \(n/q\to\lambda\in(0,\infty)\), let \(p=\lambda/(1+\lambda)\) and \(\mu_{n,q}=nq/(n+q-1)\). Writing \(\binom{s}{t}=s(s-1)\cdots(s-t+1)/t!\) also for real \(s\), one has
\[
\frac{Z_t(X)-\binom{\mu_{n,q}}{t}}{q^{t-1/2}}
\ \Longrightarrow\ \mathcal N\left(0,\frac{p^{2t}(1-p)}{((t-1)!)^2}\right),
\quad
\operatorname{Var}(Z_t)\sim \frac{p^{2t}(1-p)}{((t-1)!)^2}q^{2t-1}.
\]
For \(t=3\), the leading variance coefficient is \(\lambda^6/[4(1+\lambda)^7]\).

## Assumptions and scope

Each of the \(\binom{n+q-1}{q-1}\) multiplicity vectors is equally likely; this is *not* the multinomial law induced by independent uniformly sampled symbols. Deletions are exact, not up to \(t\), and their outputs have total size \(n-t\). All finite moment and histogram identities hold without divisibility assumptions. The normal law requires fixed \(t\ge2\) and a positive finite limit of \(n/q\).

## Proof

**One-sided counting.** For every \(d\in\mathcal S_{t,q}\), the indicator \(I_d(x)=\mathbf1\{x\ge d\}\) specifies one output; distinct deletion vectors yield distinct output vectors. Therefore \(Z_t=\sum_d I_d\). The number of inputs satisfying \(x\ge d\) is \(B(n-t,q)\), proving the first moment by double counting.

For two deletion vectors \(d,e\in\mathcal S_{t,q}\), both indicators are one precisely when \(x\ge\max(d,e)\) coordinatewise. With \(m=\tfrac12\sum_i|d_i-e_i|\), the sum of the coordinatewise maxima is \(t+m\), leaving exactly \(B(n-t-m,q)\) possible inputs. The known exact multiset pair-distance enumerator [1, Theorem 9] gives
\[
\#\{(d,e)\in\mathcal S_{t,q}^2:\tfrac12\|d-e\|_1=m\}
=c_{q,m}B(t-m,q).
\]
Grouping the double sum \(\sum_{d,e}I_dI_e\) by \(m\) establishes the second moment and hence the variance. The displayed pair-distance enumerator is explicitly cited prior coverage, not counted as original.

**Complete three-deletion histogram.** A feasible deletion vector with sum three has exactly one of the disjoint shapes \((1,1,1)\), \((2,1)\), \((3)\). Their respective counts are \(\binom K3\), \(H(K-1)\) and \(J\): the coordinate with a 2 has \(H\) choices and the distinct coordinate with a 1 has \(K-1\) choices. This proves the volume formula. For fixed \((k,h,j)\), choose the \(k\) occupied coordinates, the \(h\) coordinates having at least two, and the \(j\) having at least three: \(\binom qk\binom kh\binom hj\). Their minimal coordinate sum is \(k+h+j\). If \(j=0\), each coordinate is frozen at zero, one or two, and hence \(n=k+h\) is necessary and sufficient. If \(j>0\), all additional mass is arbitrarily distributed across precisely those \(j\) already-large coordinates, giving \(\binom{n-k-h-1}{j-1}\) possibilities when \(n\ge k+h+j\), and zero otherwise. Sum over triples matching the volume to obtain the exact histogram.

**Gaussian regime.** The number \(K\) of positive coordinates satisfies
\[
\Pr(K=k)=\frac{\binom qk\binom{n-1}{k-1}}{\binom{n+q-1}{q-1}},
\qquad
\mathbb EK=\mu_{n,q}=\frac{nq}{n+q-1},
\quad
\operatorname{Var}(K)=\frac{nq(n-1)(q-1)}{(n+q-1)^2(n+q-2)}.
\]
Thus \(K\) is hypergeometric, with population \(n+q-1\), marked count \(q\), and sample size \(n\). Classical hypergeometric central-limit asymptotics (also obtained directly by Stirling expansion of the displayed mass function) imply \((K-\mu_{n,q})/\sqrt q\Longrightarrow\mathcal N(0,p^2(1-p))\), and the variance is asymptotic to \(p^2(1-p)q\).

Among deletion vectors of weight \(t\), those with all coordinates distinct yield \(\binom Kt\) outcomes; the total number of remaining weight-\(t\) vectors, across *all* \(q\) coordinates, is bounded by \(C_t q^{t-1}\) for a constant depending only on fixed \(t\) (choose at most \(t-1\) support coordinates and allocate the \(t\) deletions). Hence uniformly in every \(x\),
\[
0\le Z_t(x)-\binom{K(x)}t\le C_tq^{t-1}.
\]
The polynomial delta method at \(\mu_{n,q}\sim pq\) gives the Gaussian limit, since the remainder is \(o(q^{t-1/2})\). For the variance asymptotic, a hypergeometric sampling-without-replacement concentration bound yields \(\mathbb E(K-\mu)^4=O(q^2)\). Taylor expansion of \(\binom Kt\), together with the uniform remainder bound, shows
\[
\operatorname{Var}Z_t=\left(\frac{(pq)^{t-1}}{(t-1)!}\right)^2\operatorname{Var}K+o(q^{2t-1}),
\]
which equals the coefficient stated above. The central limit and the variance claim concern \(q\to\infty\) jointly with \(n\); neither follows from finite enumeration.

## Verification

Two independent self-contained Python files, `verification/verify_descendants.py` and `verification/verify_moments.py`, accompany the theorem. The first checks each actual three-deletion descendant against its shape count and the full histogram, using 38,665 weak compositions across \(q=2,\dots,6\) and \(n=3,\dots,13\). The second checks the exact first and second moment formulas by rational arithmetic against actual descendant enumeration for 24,505 centers across \(q=2,\dots,5\), \(t=1,\dots,4\), \(n=t,\dots,11\). The programs contain no symbolic proof of the all-parameter identities or of the Gaussian limit; those follow from the arguments above.

For instance, \(q=3,n=6,t=3\) gives \(\mathbb EZ_3=25/7\) and \(\operatorname{Var}Z_3=297/98\). For \(q=4,n=10,t=3\), the exact values are \(1200/143\) and \(355222/20449\).

## Relationship to prior work

Kreindel, Barouch Essayag and Zabokritskiy [1] determine same-level multiset deletion-*distance* ball sizes and their mean, plus the exact pair-distance enumerator used explicitly in the second moment formula. A radius-\(r\) ball at fixed total size \(n\) is not the set of outputs left after deleting exactly \(t\) symbols; the present distribution and growing-alphabet law pertain to the latter directed channel. The earlier multiset code framework [2] concerns correction-code cardinalities and constructions. The previously known pair enumerator is not claimed as new. No complete three-deletion one-sided descendant-volume histogram or growing-alphabet Gaussian law was identified in the checked primary literature and research record searches; this does not establish absolute priority.

## Limitations

The exact histogram is specialized to three deletions, though first and second moments hold for every fixed or variable \(t\) with \(1\le t\le n\). The normal limit assumes a uniformly random *multiset* and \(n/q\) tending to a positive finite constant; it does not directly describe random ordered words, nonuniform compositions, or large deletion counts \(t\) growing with \(q\). Source availability and indexing mean earlier undiscovered equivalent results remain a priority risk.

## References

[1] A. Kreindel, I. Barouch Essayag, A. L. Zabokritskiy, *Polynomial Constructions and Deletion-Ball Geometry for Multiset Deletion Codes*, arXiv:2603.18322v1, publicly available 2026-03-18, https://arxiv.org/abs/2603.18322 (especially Theorem 9, pp. 28–30).

[2] A. Kreindel, I. Barouch Essayag, A. L. Zabokritskiy, *Multiset Deletion Codes: Cyclic Constructions, Bounds, and Exact Results*, arXiv:2601.05636v1, publicly available 2026-01-09, https://arxiv.org/abs/2601.05636.
