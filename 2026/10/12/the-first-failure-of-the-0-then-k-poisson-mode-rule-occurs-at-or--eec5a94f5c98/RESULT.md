# The first failure of the \(0\)-then-\(k\) Poisson mode rule occurs at order fifteen
## Finding
For each integer \(k\ge2\) and real \(\lambda>0\), let \(N_1,\ldots,N_k\) be independent \(\operatorname{Poisson}(\lambda)\) random variables and define the order-\(k\) Poisson variable
\[
X_{k,\lambda}=\sum_{j=1}^{k}jN_j.
\]
The *first modal departure* is the smallest positive intensity at which \(0\) is no longer the unique global maximizer of \(\Pr(X_{k,\lambda}=n)\), with equality at the boundary allowed. For each \(2\le k\le15\), this transition exists and has exactly two global modes at its transition intensity \(\tau_k\):
\[
\operatorname*{arg\,max}_{n\ge0}\Pr(X_{k,\tau_k}=n)=
\begin{cases}\{0,k\},&2\le k\le14,\\
\{0,25\},&k=15.
\end{cases}
\]
There are no other global modes at \(\tau_k\). Immediately below \(\tau_k\) the unique mode is \(0\), and on a nonempty interval immediately above it the unique mode is \(k\) for \(2\le k\le14\) and \(25\) for \(k=15\). Thus fifteen is the **least order** where the first modal departure does not select the index equal to the order. In particular,
\[
\frac{250227}{10^6}<\tau_{15}<\frac{250228}{10^6}.
\]

More precisely, define the polynomial-in-\(\lambda\) coefficient
\[
a_{k,n}(\lambda)=[z^n]\exp\!\left(\lambda\sum_{j=1}^{k}z^j\right).
\]
For \(2\le k\le14\), \(\tau_k\) is the unique positive root of \(a_{k,k}(\lambda)=1\), whereas \(\tau_{15}\) is the unique positive root of \(a_{15,25}(\lambda)=1\). All fourteen transitions admit the following rigorously certified rational brackets \((q_k-1)/10^6<\tau_k<q_k/10^6\):

| \(k\) | \(q_k\) | First nonzero modal index |
|---:|---:|---:|
| 2 | 732051 | 2 |
| 3 | 601680 | 3 |
| 4 | 520352 | 4 |
| 5 | 463330 | 5 |
| 6 | 420487 | 6 |
| 7 | 386782 | 7 |
| 8 | 359378 | 8 |
| 9 | 336537 | 9 |
| 10 | 317127 | 10 |
| 11 | 300374 | 11 |
| 12 | 285728 | 12 |
| 13 | 272786 | 13 |
| 14 | 261245 | 14 |
| 15 | 250228 | 25 |

## Assumptions and scope
The index \(k\) is an integer from \(2\) through \(15\), all Poisson components are mutually independent with a common **real** intensity \(\lambda>0\), and global modes range over **all** integers \(n\ge0\). No truncation of the probability distribution is assumed. The theorem classifies only the *initial* modal departure; it makes no assertion about subsequent transitions or orders at least sixteen. Ties at the first boundary are included.

## Proof
**1. Normalize and obtain a rational recurrence.** The probability-generating function is
\[
\mathbb E z^{X_{k,\lambda}}=\exp\!\left(\lambda\sum_{j=1}^{k}z^j-k\lambda\right).
\]
Consequently \(\Pr(X_{k,\lambda}=n)=e^{-k\lambda}a_{k,n}(\lambda)\), with \(a_{k,0}=1\) and the exact recurrence
\[
na_{k,n}(\lambda)=\lambda\sum_{j=1}^{\min(k,n)}j\,a_{k,n-j}(\lambda),\qquad n\ge1.
\]
Every \(a_{k,n}\) for \(n\ge1\) is a polynomial with strictly positive coefficients for its nonzero powers and zero constant term. It is therefore continuous and strictly increasing for \(\lambda>0\), starts at zero, and diverges as \(\lambda\to\infty\). Each equation \(a_{k,n}(\lambda)=1\) has exactly one positive solution.

**2. A finite certificate controls the complete infinite support.** For each displayed \(q_k\), set \(B_k=q_k/10^6\), \(L_k=(q_k-1)/10^6\), and \(j_k=k\) except \(j_{15}=25\). The accompanying standalone program `verify.py` computes the recurrence using exact rational arithmetic, with no floating-point comparisons, and establishes simultaneously for every \(k=2,\ldots,15\)
\[
a_{k,j_k}(L_k)<1<a_{k,j_k}(B_k),\quad
\max_{1\le n\le40k,\ n\ne j_k}a_{k,n}(B_k)<1,\quad kB_k<4.
\]
These finitely many **strict rational inequalities** constitute an inspectable certificate, not a probabilistic simulation.

To control all remaining indices, let \(M\sim\operatorname{Poisson}(k\lambda)\). Conditional on \(M=m\), \(X_{k,\lambda}\) is a sum of \(m\) independent uniforms on \(\{1,\ldots,k\}\). Thus \(X_{k,\lambda}=n>40k\) implies \(M\ge41\), and, at \(\lambda=B_k\),
\[
a_{k,n}(B_k)
=\sum_{m\ge0}\frac{(kB_k)^m}{m!}\Pr(U_1+\cdots+U_m=n)
\le\sum_{m\ge41}\frac{(kB_k)^m}{m!}
<\sum_{m\ge41}\frac{4^m}{m!}
\le\frac{2\cdot4^{41}}{41!}<1.
\]
The penultimate inequality follows because the ratio of successive terms is at most \(4/42\) for \(m\ge41\); the final inequality is an elementary exact integer comparison. Hence the finite comparisons control *every* possible competitor, including the infinite tail.

**3. Recover the global transitions.** By strict monotonicity and the first certificate inequalities, the unique root \(\tau_k\) of \(a_{k,j_k}(\lambda)=1\) lies strictly between \(L_k\) and \(B_k\). For \(0<\lambda\le B_k\), each alternative \(a_{k,n}(\lambda)\), \(n\ge1\), \(n\ne j_k\), is strictly less than one, while \(a_{k,0}=1\). Therefore for \(\lambda<\tau_k\) the unique maximizer is \(0\), at \(\tau_k\) precisely \(0\) and \(j_k\) are tied, and for \(\tau_k<\lambda\le B_k\) the unique maximizer is \(j_k\). The table gives \(j_k=k\) through fourteen and \(j_{15}=25\). This proves the stated *least-order* assertion, including all real intensities in the transition intervals and all possible modal indices.

## Verification
Run `python3 verify.py` from the directory containing the extracted files. This uses only Python's standard library (`fractions.Fraction`, `math.factorial`), checks fourteen root brackets, verifies all competitor inequalities through \(40k\), and verifies the exact infinite-tail constant. It prints `VERIFY_OK` on success. The analytic arguments above explain why those finite exact comparisons establish statements over **all real** intensities in the indicated intervals and over **all** integer modal indices. An ordinary floating-point scan or a finite simulation alone would not suffice.

## Relationship to prior work
Kwon and Philippou (2023) determine the early modes for orders three and four and explicitly ask whether the first two global-mode regimes are always \(0\) then \(k\). Their Lemma 2 considers the root of \(a_{k,k}(\lambda)=1\), which need not equal the *first global* transition in general. The present finding determines the **least** order where those roots diverge, and identifies the exact competing index \(25\).

Georghiou, Philippou, and Saghafi (2012/2013) prove broad mode-location bounds and integer-intensity results for orders through five, but those inequalities neither classify first transitions for orders six through fifteen nor imply the sharp finite cutoff. Philippou's 2013/2014 note gives a general small-intensity sufficient condition for mode zero and an exact result for order two. A large-order asymptotic estimate, even when available, cannot by itself identify the smallest finite exception or the first competing index.

## Limitations
The result is a finite-order exact classification, not a theorem for all \(k\). It does not describe later modal switches, all possible double modes, or the number of global modes at arbitrary intensities. Computational assertions are exact rational arithmetic supplemented by the displayed analytic infinite-tail bound; replay requires the included `verify.py`. A publication-priority search cannot guarantee the absence of an equivalent unindexed result, and independent review has not been performed.

## References
1. Y. Kwon and A. N. Philippou, *The Modes of the Poisson Distribution of Order 3 and 4*, Entropy **25** (2023), 699. DOI: 10.3390/e25040699. First verified public appearance: 2023-04-21. Public full text: https://pdfs.semanticscholar.org/9990/682c005b4b17d3a625e2d31ed941ff440142.pdf.
2. C. Georghiou, A. N. Philippou, and A. Saghafi, *On the modes of the Poisson distribution of order k*, Fibonacci Quarterly **51** (2013), 44–48. Preprint: arXiv:1204.3186 (first posted 2012-04-14).
3. A. N. Philippou, *A note on the modes of the Poisson distribution of order k*, Fibonacci Quarterly **52** (2014), 203–205. Preprint: arXiv:1312.7139 (first posted 2013-12-26).
