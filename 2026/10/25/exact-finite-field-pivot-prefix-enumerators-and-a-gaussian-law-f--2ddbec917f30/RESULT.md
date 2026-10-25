# Exact finite-field pivot-prefix enumerators and a Gaussian law for nonsingular matrix corners

## Finding
Fix any prime power \(q\ge 2\). For \(n\ge1\) and \(G\in\operatorname{GL}_n(\mathbb F_q)\), write
\[
B_n(G)=\#\big\{1\le k\le n:\det G[1\!:\!k,1\!:\!k]\ne0\big\}.
\]
Set \(a_{q,0}=1\), \(a_{q,k}=\prod_{j=1}^{k}(1-q^{-j})\) for \(k\ge1\), and use the formal series
\[
U_q(z)=\sum_{k\ge0}a_{q,k}z^k,\qquad F_q(z)=1-U_q(z)^{-1}.
\]
Then the exact finite-field counting identity, valid for every \(n\ge1\) and every integer \(b\), is
\[
\boxed{\#\{G\in\operatorname{GL}_n(\mathbb F_q):B_n(G)=b\}
=q^{n^2}[z^n]F_q(z)^b}\tag{1}
\]
for \(1\le b\le n\), and the count is zero otherwise. Equivalently, the normalized bivariate generating series is \(uF_q(z)/(1-uF_q(z))\).

Define convergent constants
\[
c_q=\prod_{j\ge1}(1-q^{-j}),\quad A_q=\sum_{k\ge0}(a_{q,k}-c_q),\quad
\sigma_q^2=2c_qA_q-c_q(1-c_q).
\]
The variance constant is strictly positive. If \(G_n\) is uniform in \(\operatorname{GL}_n(\mathbb F_q)\), then
\[
\boxed{\frac{B_n(G_n)-c_q n}{\sigma_q\sqrt n}\ \Longrightarrow\ \mathcal N(0,1)}.\tag{2}
\]
For example \(c_2=0.28878809508660\ldots\) and \(\sigma_2^2=0.42134159814045\ldots\). Thus nonsingularity of different leading corners has persistent but explicitly quantifiable dependence.

## Assumptions and scope
The field is any finite field of cardinality \(q\), with \(q\) a prime power. Matrices are sampled uniformly from all invertible \(n\)-by-\(n\) matrices; the index order of their rows and columns is fixed. A zero-size corner is treated as invertible for the renewal derivation but is not counted in \(B_n\). The coefficient symbol \([z^n]\) means formal coefficient extraction. Constants depend on fixed \(q\), and \(n\to\infty\) with \(q\) fixed. The large-deviation regime and simultaneous growth of \(q\) are not claimed.

## Proof
**1. Corner-nullity chain.** Take an infinite array of independent uniform \(\mathbb F_q\)-valued entries. Let \(M_k\) be the upper-left \(k\)-square corner and set \(D_k=k-\operatorname{rank}(M_k)\) (with \(D_0=0\)). Given any matrix of nullity \(d\), appending an independent column and row produces the following transition probabilities, depending only on \(d\):
\[
\begin{aligned}
\Pr(D_{k+1}=d+1\mid D_k=d)&=q^{-2d-1},\\
\Pr(D_{k+1}=d-1\mid D_k=d)&=(1-q^{-d})^2\quad(d\ge1),\\
\Pr(D_{k+1}=d\mid D_k=d)&=1-q^{-2d-1}-(1-q^{-d})^2.
\end{aligned}\tag{3}
\]
Here the downward transition is impossible from \(d=0\). To see (3), change bases to put the old matrix into rank-normal form, with an invertible block of size \(k-d\) and a trailing zero block of size \(d\). The new column lies inside the old column span with probability \(q^{-d}\), and independently the new row lies in the old row span with probability \(q^{-d}\). When both do, the rank rises by zero if the remaining scalar Schur complement vanishes, with conditional probability \(q^{-1}\); thus the nullity rises by one with probability \(q^{-2d-1}\). When both lie outside, the rank rises by two, decreasing nullity by one with probability \((1-q^{-d})^2\). The remaining cases increase rank by one. This argument works in every finite characteristic.

For each \(k\), \(M_k\) is a uniform square matrix, so
\[
\Pr(D_k=0)=\Pr(M_k\text{ invertible})=a_{q,k}.\tag{4}
\]

**2. Returns and exact enumeration.** Starting at \(D_0=0\), let \(\tau=\inf\{k\ge1:D_k=0\}\) be the first strictly positive return. The chain is homogeneous, hence its successive return times to zero are independent and identically distributed. Let \(f_{q,k}=\Pr(\tau=k)\) and \(f_q(z)=\sum_{k\ge1} f_{q,k}z^k\). The first-return decomposition and (4) give \(U_q(z)=1/(1-f_q(z))\) as formal power series, whence \(f_q=F_q\). If exactly \(b\) positive returns occur by time \(n\) and the chain is at zero at time \(n\), then their successive return lengths sum to \(n\); thus
\[
\Pr(D_n=0,\ \#\{1\le k\le n:D_k=0\}=b)=[z^n]F_q(z)^b.\tag{5}
\]
All \(q^{n^2}\) square matrices are equally likely, and \(D_n=0\) is precisely their invertibility. Multiplying (5) by \(q^{n^2}\) proves (1) and its bivariate form. In particular the identity is an exact integer-valued enumeration, not an asymptotic approximation.

**3. Exponential return tail.** For \(d\ge1\), the upward probability in (3) is at most \(1/8\) and the downward probability at least \(1/4\) (uniformly for \(q\ge2\)). Consequently, for any sufficiently small fixed \(h>0\), uniformly for \(d\ge1\),
\[
\mathbb E[e^{h(D_{k+1}-d)}\mid D_k=d]
\le 1+\tfrac18(e^h-1)+\tfrac14(e^{-h}-1)=:\theta<1.
\]
Before the first hitting of zero from state one, iteration yields \(\Pr_1(T_0>k)\le e^h\theta^k\). A return from zero is either immediate or starts at state one, so \(\tau\) has an exponential tail, in particular an exponential moment, and the chain returns to zero almost surely. Both \(f_{q,1}=1-q^{-1}\) and \(f_{q,2}=q^{-1}(1-q^{-1})^2\) are positive. Its return-time distribution is therefore nonconstant and aperiodic.

**4. Exact mean and variance.** Since \(a_{q,k}\) decreases to \(c_q>0\), and
\(0\le a_{q,k}-c_q\le\sum_{j>k}q^{-j}=O(q^{-k})\), the constant \(A_q\) converges absolutely and \(U_q\) has the analytic Laurent expansion
\[
U_q(z)=\frac{c_q}{1-z}+A_q+O(1-z),\qquad z\to1.
\]
It follows that
\[
F_q(z)=1-\frac{1-z}{c_q}+\frac{A_q(1-z)^2}{c_q^2}+O((1-z)^3).
\]
Thus \(\mu_q=\mathbb E\tau=1/c_q\) and
\(\operatorname{Var}(\tau)=(2A_q+c_q-1)/c_q^2\). Hence
\[
\mu_q^{-3}\operatorname{Var}(\tau)
=2c_qA_q-c_q(1-c_q)=\sigma_q^2>0,
\]
where positivity also follows directly from the two positive distinct return-time masses above.

**5. Conditional central limit theorem.** Exponential tails make \(F_q\) analytic on a disk of radius strictly greater than one. Because the coefficients of \(F_q\) are nonnegative, sum to one, and include strictly positive terms in degrees one and two, \(1-F_q(z)\) has exactly one zero on the closed unit disk, a simple zero at \(z=1\). For \(t\) in a sufficiently small complex neighborhood of zero, the equation \(e^tF_q(\rho(t))=1\) has a unique simple root near one, analytic in \(t\), with \(\rho(0)=1\). The same compactness/aperiodicity argument provides a fixed larger disk containing no other poles. Extracting the simple pole gives, uniformly for small complex \(t\),
\[
[z^n]\frac1{1-e^tF_q(z)}=
\frac{\rho(t)^{-n}}{e^t\rho(t)F_q'(\rho(t))}+O(R^{-n})
\]
for some \(R>1\) smaller than the analytic continuation radius (and the finite polynomial term at \(n=0\) is irrelevant). Conditioning on \(D_n=0\), formula (5) yields
\[
\mathbb E[e^{tB_n}\mid D_n=0]
=\frac{[z^n](1-e^tF_q(z))^{-1}}{a_{q,n}}.
\]
The analytic cumulant function \(K(t)=-\log\rho(t)\) satisfies
\(K'(0)=1/\mu_q=c_q\) and
\(K''(0)=\operatorname{Var}(\tau)/\mu_q^3=\sigma_q^2\), by differentiating \(e^tF_q(\rho(t))=1\). Substituting \(t=is/(\sigma_q\sqrt n)\) and expanding to second order proves convergence of characteristic functions to \(e^{-s^2/2}\). The matrices conditional on \(D_n=0\) are exactly uniform on \(\operatorname{GL}_n(\mathbb F_q)\), establishing (2).

## Verification
The independent exact-arithmetic check in `CHECK.py` directly enumerates all invertible matrices over \(\mathbb F_2\) in dimensions one through four and over \(\mathbb F_3\) in dimensions one through three; it compares the complete histogram of \(B_n\) with the coefficient counts in (1). It also exhaustively checks the conditional nullity transitions for three small field/size cases and numerically evaluates the absolutely convergent variance series for four field orders. The expected terminal line is `VERIFY_OK matrix_distributions=7 rank_transitions=3 exact_renewal_identity=PASS positive_variances=4`. These finite checks do not prove the central limit theorem, for which the analytic argument above is required.

## Relationship to prior work
Lvov's *A dynamic point of view on universality for random matrices over finite local rings* (first public September 9, 2026, arXiv:2609.10894) studies Markov and ergodic behavior of nested cokernel corners and motivates a finer count of zero-cokernel visits. Its publicly accessible abstract describes the almost-sure ergodic theorem and universality, not an exact size-by-size enumerator and conditioned Gaussian fluctuations with a field-dependent, explicit Euler-product variance. The complete paper could not be inspected, so this comparison has a bibliographic limitation, not a claim of exhaustive exclusion. Fulman and Goldstein analyze the one-time rank distribution of a random finite-field matrix, a weaker marginal statistic. The direct relation between the present joint-count result and the prior general Markov-chain theorem is the first-return decomposition; the explicit finite-field coefficient identity and field-dependent variance are the specific additional conclusions.

## Limitations
No independence or priority certification is claimed. The complete text of the highly relevant Lvov preprint was inaccessible during this comparison; it could contain a statement or implication stronger than its abstract. The proof treats uniform matrices over fixed finite fields, not general nonuniform entry distributions, random symmetric matrices, or growing field size. The variance series is exact but not simplified to an elementary closed form. The numerical verification covers only finite prime fields and small dimensions; the proof covers all prime powers and all dimensions.

## References
1. N. Lvov, *A dynamic point of view on universality for random matrices over finite local rings*, arXiv:2609.10894, first public 2026-09-09, https://arxiv.org/abs/2609.10894.
2. J. Fulman and L. Goldstein, *Stein's method and the rank distribution of random matrices over finite fields*, Annals of Probability 43 (2015), 1274–1314, https://doi.org/10.1214/13-AOP889.
3. C. Cooper, *On the distribution of rank of a random matrix over a finite field*, Random Structures & Algorithms 17 (2000), 197–212, https://doi.org/10.1002/1098-2418(200010/12)17:3/4%3C197::AID-RSA2%3E3.0.CO;2-K.
