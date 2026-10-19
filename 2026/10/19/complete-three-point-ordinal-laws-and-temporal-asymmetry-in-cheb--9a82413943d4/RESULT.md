# Complete three-point ordinal laws and temporal asymmetry in Chebyshev dynamics

## Finding
For every integer \(b\ge 2\) and lag \(m\ge 1\), set \(q=b^m\), and let \(F_b(x)=(1-T_b(1-2x))/2\) on \([0,1]\), where \(T_b\) is the first-kind Chebyshev polynomial. Initialize \(X\) under the invariant arcsine probability \(d\mu(x)=dx/(\pi\sqrt{x(1-x)})\). Write \(Z_0=X\), \(Z_1=F_b^m(X)\), and \(Z_2=F_b^{2m}(X)\). For a permutation \(ijk\) of \(012\), define \(p_{ijk}=\Pr(Z_i<Z_j<Z_k)\). Ties have probability zero.

When \(q\) is even, all six probabilities are
\[
\begin{aligned}
p_{012}&=\frac{q^2+2}{6(q^2-1)},&
p_{021}&=\frac{q^4-2q^2-2}{6(q^4-1)},\\
p_{102}&=\frac{q^2}{6(q^2+1)},&
p_{120}&=\frac{q^2+2}{6(q^2+1)},\\
p_{201}&=\frac{q^2(q^2+2)}{6(q^4-1)},&
p_{210}&=\frac{q^2-4}{6(q^2-1)}.
\end{aligned}
\]
When \(q\) is odd, they are
\[
p_{012}=p_{210}=\frac16,\qquad
p_{021}=p_{120}=\frac{q^2+2}{6(q^2+1)},\qquad
p_{102}=p_{201}=\frac{q^2}{6(q^2+1)}.
\]

True time reversal acts on the index-order permutations by \(i\mapsto 2-i\), pairing \(012\leftrightarrow210\), \(021\leftrightarrow201\), and \(102\leftrightarrow120\). The total-variation distance between the three-point ordinal law and its time reversal is exactly
\[
\mathsf{TV}(q)=
\begin{cases}
\dfrac{2q^2+1}{q^4-1},&q\ \text{even},\\[3pt]
\dfrac{2}{3(q^2+1)},&q\ \text{odd}.
\end{cases}
\]
In particular every finite-lag law is time-irreversible, but \(\mathsf{TV}(b^m)\sim 2b^{-2m}\) for even \(b\) and \(\mathsf{TV}(b^m)\sim (2/3)b^{-2m}\) for odd \(b\). The parity-dependent leading coefficients differ by a factor of three.

## Assumptions and scope
Only integer Chebyshev degrees \(b\ge2\), integer lags \(m\ge1\), stationary arcsine initialization, and strict comparisons of three equally spaced observations are considered. The ordinal word \(ijk\) denotes the **indices ordered by increasing observed value**, not the vector of ranks at chronological positions; this convention matters in formulating time reversal. The arcsine endpoints and intersections of compared trajectories form a measure-zero exceptional set.

## Proof
**1. Reduction to an expanding folding map.** Put \(h(y)=(1-\cos(\pi y))/2\) for \(y\in[0,1]\). The function \(h\) is strictly increasing in the interior and pushes normalized Lebesgue measure to \(\mu\). Define \(\tau_n\) on the \(j\)-th cell \([j/n,(j+1)/n]\), \(j=0,\ldots,n-1\), by \(\tau_n(y)=ny-j\) for even \(j\), and \(\tau_n(y)=j+1-ny\) for odd \(j\). The Chebyshev identity gives \(F_b\circ h=h\circ\tau_b\) and \(\tau_b^m=\tau_{b^m}=\tau_q\). Since each inverse branch of \(\tau_q\) contracts by \(q^{-1}\), Lebesgue measure is invariant. We may therefore compute ordinal probabilities from the uniform random triple \((Y,\tau_qY,\tau_{q^2}Y)\).

**2. Two-point comparison.** The crossing \(y=\tau_q(y)\) occurs on cell \(j\) at \(c_j=j/(q-1)\) for even \(j\) and \(c_j=(j+1)/(q+1)\) for odd \(j\). Summing the lengths on which \(y<\tau_q(y)\) gives
\[
U_q:=\Pr(Y<\tau_qY)=
\begin{cases}
\dfrac{q^2}{2(q^2-1)},&q\ \text{even},\\
\dfrac12,&q\ \text{odd}.
\end{cases}
\]
Likewise \(V_q:=\Pr(Y<\tau_{q^2}Y)=U_{q^2}\). All three two-point comparison probabilities in the stationary triple are thus determined (the remaining one is \(U_q\) by stationarity).

**3. The increasing triple.** Let \(a=p_{012}\). Set \(t=\tau_qy\). Conditional on \(t\), the \(q\) preimages are equally likely and are \(g_k(t)=(k+t)/q\) for even \(k\), \(g_k(t)=(k+1-t)/q\) for odd \(k\). On the rising portion of the \(j\)-th cell for \(t<\tau_qt\), precisely \(j+1\) preimages satisfy \(g_k(t)<t\) if \(j\) is even and precisely \(j\) do if \(j\) is odd. The rising lengths in these cells are respectively \((q-1-j)/(q(q-1))\) and \((q-j)/(q(q+1))\). Consequently
\[
a=\frac1{q^2}\left[
\sum_{\substack{0\le j<q\\j\text{ even}}}\frac{(j+1)(q-1-j)}{q-1}
+\sum_{\substack{0\le j<q\\j\text{ odd}}}\frac{j(q-j)}{q+1}
\right].
\]
Separately summing the even and odd arithmetic progressions yields \(a=(q^2+2)/(6(q^2-1))\) for even \(q\) and \(a=1/6\) for odd \(q\).

**4. The low-middle-high triple.** Put \(M=q^2\), \(Q_M(y)=\mathbf1_{\{y<\tau_My\}}\), and \(G_M(z)=\int_0^z Q_M(y)\,dy\). Pairing consecutive even and odd \(M\)-cells, whose combined rising length is \(2(M-1-2r)/(M^2-1)\), proves that for every even integer \(J\) between \(0\) and \(M\),
\[
G_M(J/M)=\frac{A(J)}{M^2-1},\qquad A(J)=J(M-J/2).
\]
The coarse falling region \(\tau_qy<y\) on an even \(j\)-cell is \([j/q,j/(q-1)]\), while on an odd \(j\)-cell it is \([(j+1)/(q+1),(j+1)/q]\). At each non-grid endpoint of these falling intervals, \(Q_M\) has remained zero since the start of the relevant even fine cell, so its cumulative integral equals its value at that even-cell boundary. Therefore \(c=p_{102}=\Pr(\tau_qY<Y<\tau_MY)\) is exactly
\[
\begin{aligned}
c=\frac1{M^2-1}\bigg(&
\sum_{\substack{0\le j<q\\j\text{ even}}}[A(j(q+1))-A(jq)]\\
&+\sum_{\substack{0\le j<q\\j\text{ odd}}}[A((j+1)q)-A((j+1)(q-1))]\bigg).
\end{aligned}
\]
Both sums are explicit quadratic power sums. For \(q=2\ell\), their respective evaluations are \(\ell(\ell-1)(4\ell^2+2\ell+1)/3\) and \(\ell(\ell+1)(4\ell^2-2\ell+1)/3\). For \(q=2\ell+1\), they are \(2\ell^2(\ell+1)(2\ell+1)/3\) and \(2\ell(\ell+1)^2(2\ell+1)/3\). In either case their sum divided by \(q^4-1\) is
\[
c=\frac{q^2}{6(q^2+1)}.
\]
The even-cell endpoint evaluation includes \(q=2\) and all larger \(q\); no asymptotic or finite-grid approximation is used.

**5. Completion of the six probabilities.** Write \(a=p_{012}\), \(c=p_{102}\), \(u=U_q\), and \(v=U_{q^2}\). The three pairwise-order marginals and the fact that the six probabilities sum to one imply
\[
\begin{aligned}
p_{012}&=a,&p_{102}&=c,&p_{021}&=v-a-c,\\
p_{120}&=u-a-c,&p_{201}&=c+u-v,&p_{210}&=1+a-2u.
\end{aligned}
\]
For example, \(\Pr(Z_0<Z_1)=p_{012}+p_{021}+p_{201}=u\), and \(\Pr(Z_0<Z_2)=p_{012}+p_{021}+p_{102}=v\). The further stationary identity \(\Pr(Z_1<Z_2)=p_{012}+p_{102}+p_{120}=u\) completes the linear system. Substitution and simplification produce the six formulas in the Finding section.

**6. Time reversal.** The total-variation distance is the sum of the absolute differences over the three reversal pairs. Substituting the six rational probabilities gives the displayed parity-specific expressions. They are strictly positive for every integer \(q\ge2\). Expansion at \(q=b^m\to\infty\) yields the two different coefficients.

## Verification
A standalone, standard-library Python checker is included as `verify.py`. Run `python3 verify.py`. It directly subdivides \([0,1]\) into the \(q^2\) cells on which \(y\), \(\tau_qy\), and \(\tau_{q^2}y\) are affine, inserts all pairwise intersection points as exact rational numbers, and integrates each of the six ranking events exactly. It independently checks the two key finite sums, two-point probabilities, time-reversal distance, and total mass. It reports `VERIFY_OK: 68 exactly integrated degrees; six ranks, lag-one/two pair laws, temporal reversal and both finite-sum identities`. Tests cover each integer \(2\le q\le64\) and \(72,81,96,125,128\). This finite verification is a reproducibility check; the universally quantified proof is the argument above.

## Relationship to prior work
Unakafov and Keller (2014, arXiv:1407.5390v1) develop conditional entropy and ordinal partitions, including numerical comparisons for the logistic family. Ordinal symbolic analyses of the fully chaotic logistic map already illustrate which patterns are forbidden at three observations. Soriano and Zunino (2021) emphasize lagged ordinal observables, and Acero, Lyons, Aragoneses and Pattanayak (2024) investigate word-symmetry quantifiers for logistic and related chaotic maps. The existence of these constructions and the basic Chebyshev--tent semiconjugacy are not claimed as new. The specific result here is the **simultaneous all-degree, all-lag six-pattern rational law and its evaluated temporal-reversal distance, with its parity-dependent sharp asymptotic coefficient**. The cited studies' examined statements and relevant sections do not state or imply that uniform family-wide formula. Other unindexed or earlier formulas could affect historical priority.

## Limitations
The theorem is restricted to three strictly ordered observations, equally spaced integer lags, Chebyshev degrees \(b\ge2\), and arcsine stationary initialization. It does not classify longer ordinal words, noninteger Chebyshev parameters, arbitrary invariant measures, or noise robustness. The computational sample is finite; it is not used to establish the infinite claim. No independent research audit has been conducted. Published ordinal pattern methodology and isolated logistic examples are prior art; universal historical uniqueness is not established.

## References
1. A. M. Unakafov and K. Keller, *Conditional entropy of ordinal patterns*, arXiv:1407.5390v1 (first publicly submitted 21 July 2014), https://arxiv.org/html/1407.5390v1.
2. L. Soriano and L. Zunino, *Time-Delay Identification Using Multiscale Ordinal Quantifiers*, *Entropy* 23 (2021), 969, https://doi.org/10.3390/e23080969.
3. M. Acero, S. Lyons, A. Aragoneses and A. K. Pattanayak, *Universality of Dynamical Symmetries in Chaotic Maps*, *Entropy* 26 (2024), 969, https://doi.org/10.3390/e26110969.
4. J. M. Amigó, K. Keller and V. A. Unakafova, *Ordinal symbolic analysis and its application to biomedical recordings*, *Philosophical Transactions of the Royal Society A* 373 (2015), 20140091, https://doi.org/10.1098/rsta.2014.0091.
