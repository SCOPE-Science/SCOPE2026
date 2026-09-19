# Schatten phase transitions for biased-sign resolvents

## Statement

Let
\[
G=\{-1,1\}^{\mathbb N}
\]
with Haar probability measure \(m\), and let \((\chi_F)_{F\Subset\mathbb N}\) be the Walsh orthonormal basis of \(L_2(G,m)\). For a sequence \(\lambda_j\ge0\), put
\[
\lambda_F=\sum_{j\in F}\lambda_j.
\]
Acuaviva's biased-sign semigroup has normalized resolvents \(R_t\) satisfying
\[
R_t\chi_F=(1+t\lambda_F)^{-1}\chi_F,\qquad t>0.
\]
The following consequences give a Schatten-class phase diagram that is not stated in the source paper.

### Theorem 1: exact Schatten formula and a representability obstruction

For every \(p>0\), with \(S_p\) interpreted as the Schatten quasi-ideal when \(0<p<1\),
\[
\boxed{
\|R_t\|_{S_p}^p
=
\sum_{F\Subset\mathbb N}(1+t\lambda_F)^{-p}.
}
\]
Equivalently, in the extended interval \([0,\infty]\),
\[
\boxed{
\operatorname{Tr}(R_t^p)
=
\frac1{\Gamma(p)}\int_0^\infty
x^{p-1}e^{-x}
\prod_{j=1}^\infty(1+e^{-tx\lambda_j})\,dx.
}
\]

Moreover, if \(R_t\in S_p\) for one finite \(p>0\), then every positive-time product measure \(\mu_u\) in Acuaviva's semigroup is absolutely continuous with respect to Haar measure, the resolvent measure \(\nu_t\) is absolutely continuous with respect to Haar measure, and the convolution operator \(R_t:L_1(G,m)\to L_1(G,m)\) is representable. Consequently,
\[
\boxed{
\nu_t\perp m\quad\Longrightarrow\quad
R_t\notin S_p\ \text{for every finite }p>0.
}
\]

For Acuaviva's Schur example
\[
\lambda_j=\sqrt{\log(j+1)},
\]
Proposition 4.2 gives compactness of \(R_t\) on \(L_2\), while Lemma 4.1 gives singularity of \(\nu_t\). Hence
\[
\boxed{
R_t\in S_\infty\setminus\bigcup_{0<p<\infty}S_p
\qquad(t>0).
}
\]
Thus the compact block used in that construction lies beyond every finite Schatten scale.

### Theorem 2: entropy-energy phase transition

Fix \(c,\gamma>0\) and take
\[
\lambda_j=e^{c j^\gamma}.
\]
Then \(R_t\) is compact on \(L_2(G,m)\) for every \(t>0\), and:

\[
\boxed{
\begin{array}{ll}
0<\gamma<1:& R_t\notin S_p\quad\text{for every finite }p>0,\\[1mm]
\gamma>1:& R_t\in S_p\quad\text{for every }p>0.
\end{array}}
\]

At the critical scale \(\gamma=1\), write \(a=e^c>1\) and
\[
d=\frac{\log2}{\log a}=\log_a2.
\]
Then
\[
\boxed{R_t\in S_p\iff p>d.}
\]
At the endpoint,
\[
\boxed{R_t\in S_{d,\infty}\setminus S_d,\qquad s_k(R_t)\asymp k^{-1/d}.}
\]
Here \(s_k\) are the singular values in decreasing order. In particular every prescribed critical exponent \(d>0\) occurs by choosing \(a=2^{1/d}\). For the geometric family, trace class occurs exactly when \(a>2\), and Hilbert--Schmidt membership occurs exactly when \(a>\sqrt2\).

### Theorem 3: spectral-zeta residue for geometric weights

For \(\lambda_j=a^j\), \(a>1\), let \(d=\log_a2\) and
\[
\zeta_t(s)=\operatorname{Tr}(R_t^s),\qquad s>d.
\]
If \((B_k)_{k\ge1}\) are independent Bernoulli variables with \(\mathbb P(B_k=1)=1/2\) and
\[
X_a=\sum_{k\ge1}B_k a^{-k},
\]
then
\[
\boxed{
\lim_{s\downarrow d}(s-d)\zeta_t(s)
=
\frac{t^{-d}}{2\log a}\,
\mathbb E(1+X_a)^{-d}.
}
\]
For the dyadic choice \(a=2\), finite subset sums of \(2^j\), \(j\ge1\), are exactly the even nonnegative integers. Hence
\[
R_t\simeq \operatorname{diag}_{n\ge0}(1+2tn)^{-1},
\]
and therefore
\[
\boxed{
\zeta_t(s)=(2t)^{-s}\zeta\!\left(s,(2t)^{-1}\right),
\qquad
\lim_{s\downarrow1}(s-1)\zeta_t(s)=\frac1{2t}.
}
\]

## Proof

### Diagonal Schatten formula

The Walsh characters form an orthonormal basis of \(L_2(G,m)\), and Acuaviva's Proposition 3.2 gives the positive eigenvalues
\[
r_F=(1+t\lambda_F)^{-1}.
\]
Therefore the Schatten \(p\)-sum is exactly \(\sum_F r_F^p\).

For the integral form, use
\[
(1+y)^{-p}=\frac1{\Gamma(p)}\int_0^\infty x^{p-1}e^{-x}e^{-xy}\,dx
\]
and Tonelli's theorem. Since finite subsets are selected independently coordinate by coordinate,
\[
\sum_{F\Subset\mathbb N}e^{-tx\lambda_F}
=\prod_{j=1}^\infty(1+e^{-tx\lambda_j}),
\]
with both sides allowed to be infinite.

### Finite Schatten membership forces absolute continuity

If \(R_t\in S_p\), the singleton Walsh characters already give
\[
\sum_{j=1}^\infty(1+t\lambda_j)^{-p}<\infty.
\]
For each fixed \(u>0\), exponential decay dominates polynomial decay, so there is a finite constant \(C_{u,t,p}\) with
\[
e^{-2u x}\le C_{u,t,p}(1+tx)^{-p}\qquad(x\ge0).
\]
Hence
\[
\sum_j e^{-2u\lambda_j}<\infty.
\]
Acuaviva's product measure \(\mu_u\) has coordinate bias
\[
2p_j(u)-1=e^{-u\lambda_j}.
\]
Kakutani's product-measure dichotomy, in the biased-sign form recorded by Schachermayer, therefore yields \(\mu_u\ll m\) for every \(u>0\). (If every \(\lambda_j>0\), the measures are in fact equivalent.) Since
\[
\nu_t(D)=\int_0^\infty \mu_u(D)t^{-1}e^{-u/t}\,du,
\]
we obtain \(\nu_t\ll m\). Costé's criterion, recalled as Lemma 2.2 and the preceding discussion in Acuaviva, then makes the scalar convolution operator representable.

For the Schur choice one can also see the failure of every finite Schatten sum directly. For the \(2^{N-1}\) subsets with \(\max F=N\),
\[
\lambda_F\le \sum_{j=1}^N\sqrt{\log(j+1)}
\le N\sqrt{\log(N+1)},
\]
so their contribution is at least
\[
2^{N-1}\bigl(1+tN\sqrt{\log(N+1)}\bigr)^{-p},
\]
which tends to infinity with \(N\).

### Exponential-scale weights

Let
\[
E_N=\{F\Subset\mathbb N:\max F=N\},\qquad |E_N|=2^{N-1},
\]
and set \(\Lambda_N=\sum_{j=1}^N\lambda_j\). Since
\[
\lambda_N\le\lambda_F\le\Lambda_N\qquad(F\in E_N),
\]
we have the level bounds
\[
2^{N-1}(1+t\Lambda_N)^{-p}
\le
\sum_{F\in E_N}(1+t\lambda_F)^{-p}
\le
2^{N-1}(1+t\lambda_N)^{-p}.
\]

For \(\lambda_j=e^{cj^\gamma}\), the upper bound is summable for every \(p>0\) when \(\gamma>1\), because it is bounded by a constant times
\[
\exp(N\log2-pcN^\gamma).
\]
When \(0<\gamma<1\), use \(\Lambda_N\le Ne^{cN^\gamma}\). The logarithm of the lower bound is
\[
N\log2-pcN^\gamma-p\log N+O(1),
\]
which tends to \(+\infty\). Thus no finite Schatten sum converges.

When \(\gamma=1\), \(\lambda_j=a^j\) and \(\Lambda_N\asymp a^N\). Consequently the entire \(N\)-th level has eigenvalues comparable to \(a^{-N}\), with \(2^{N-1}\) eigenvalues on that scale. Therefore the \(S_p\) series behaves like
\[
\sum_N2^Na^{-pN},
\]
which converges exactly when \(p>d=\log_a2\). At \(p=d\), each level contributes a quantity bounded above and below away from zero. The cumulative number of eigenvalues through level \(N\) is comparable to \(2^N\), while their size is comparable to \(a^{-N}=2^{-N/d}\); hence
\[
s_k(R_t)\asymp k^{-1/d},
\]
which is exactly \(S_{d,\infty}\setminus S_d\).

Compactness for all these choices follows already from \(\lambda_j\to\infty\): for each fixed spectral threshold, only finitely many finite sets \(F\) have \(\lambda_F\) below it. Acuaviva's compact-restriction lemma then also implies that the corresponding \(L_1\) convolution operator is Dunford--Pettis.

### Zeta residue

For geometric weights, group the trace by \(\max F=N\). If
\[
X_N=\sum_{k=1}^{N-1}B_ka^{-k},
\]
then uniform choice of the lower coordinates gives
\[
\sum_{\max F=N}(1+t\lambda_F)^{-s}
=\frac{t^{-s}}2(2a^{-s})^N
\mathbb E\left(1+X_N+(ta^N)^{-1}\right)^{-s}.
\]
As \(N\to\infty\), \(X_N\to X_a\) uniformly. Near \(s=d\), the expectation therefore converges uniformly to
\[
C_d=\mathbb E(1+X_a)^{-d}.
\]
Since
\[
2a^{-s}=e^{-(s-d)\log a},
\]
the elementary Abel limit
\[
\lim_{s\downarrow d}(s-d)\sum_{N\ge1}(2a^{-s})^N=\frac1{\log a}
\]
gives the stated residue. The empty-set eigenvalue contributes only a bounded term.

For \(a=2\), uniqueness of binary expansion of nonnegative integers in finite support identifies \(\lambda_F\) with \(2n\), \(n\ge0\). The Hurwitz-zeta formula and its residue at \(1\) follow immediately. As a consistency check, \(X_2\) is uniform on \([0,1]\), so \(\mathbb E(1+X_2)^{-1}=\log2\), and the general residue reduces to \(1/(2t)\).

## Relation to prior literature

Acuaviva develops the biased-sign semigroup and resolvent family for arbitrary nonnegative \((\lambda_j)\), and proves compactness and singularity for the specific Schur choice \(\lambda_j=\sqrt{\log(j+1)}\). The paper does not discuss Schatten membership.

Schachermayer's 1986 construction is an essential antecedent and must be distinguished from the present calculation. He chooses a single biased product measure whose convolution eigenvalues are multiplicative products of coordinate biases, and obtains a singular positive convolution operator that belongs to \(S_p\) for every \(p>2\). The resolvents here instead have reciprocal-additive eigenvalues \((1+t\sum_{j\in F}\lambda_j)^{-1}\). For this resolvent structure, finite Schatten membership forces absolute continuity of every positive-time product measure and hence representability of the averaged convolution measure. Thus singularity and finite Schatten membership, which coexist in Schachermayer's direct-convolution example, are incompatible for these resolvents.

The phase transition for \(e^{cj^\gamma}\), the exact critical weak-Schatten exponent, and the zeta residue are consequences of the additive subset-sum spectrum. To the best of our knowledge, targeted searches using the source paper, biased-sign resolvents, Walsh multipliers, Schatten ideals, subset-sum spectra, and equivalent spectral-zeta terminology did not locate these statements.

## Limitations

The implication
\[
R_t\in S_p\Longrightarrow \nu_t\ll m
\]
is one-way; no converse is claimed. The exponentially growing examples are used to classify Schatten behavior of the resolvent family and are not claimed to retain the singular-measure or Schur-space features of Acuaviva's particular choice. The result does not classify Schatten membership for arbitrary sequences \((\lambda_j)\). It also does not claim novelty for Walsh diagonalization, Kakutani's product-measure theorem, Costé's representability criterion, Schachermayer's singular \(S_p\) convolution example, or standard weak-Schatten and Mellin-transform facts.

## References

1. Antonio Acuaviva, *On complemented subspaces of \(L_1[0,1]\)*, arXiv:2609.17283v1, 2026. https://arxiv.org/abs/2609.17283
2. Walter Schachermayer, *Some remarks on integral operators and equimeasurable sets*, in *Probability and Analysis*, Lecture Notes in Mathematics 1206, Springer, 1986, pp. 242--258. DOI: 10.1007/BFb0076303.
3. Shizuo Kakutani, *On equivalence of infinite product measures*, Annals of Mathematics 49 (1948), 214--224. DOI: 10.2307/1969123.
