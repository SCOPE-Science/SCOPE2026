# A sharp support gap above the odd-prime short-time Fourier uncertainty minimum

## Finding
For every odd prime \(p\ge5\), every pair of nonzero complex signals on \(\mathbb Z_p\) has either exactly \(p\) nonzero short-time Fourier transform (STFT) coefficients or at least \(2p\):
\[
\boxed{\left|\operatorname{supp}V_gf\right|=p\quad\text{or}\quad\left|\operatorname{supp}V_gf\right|\ge2p.}
\]
Both alternatives occur. Thus \(2p\) is the **exact second-smallest attainable STFT support cardinality**, uniformly over the signal and the window. This improves the bare minimum \(p\) by excluding every intermediate support size; it does not assert any lower bound on the magnitudes of nonzero coefficients.

The proof also applies at \(p=3\); that individual finite case is already represented in earlier support diagrams. The parity restriction matters: the dichotomy fails at \(p=2\).

## Assumptions and scope
Fix an odd prime \(p\ge5\) and write \(\mathbb Z_p=\mathbb Z/p\mathbb Z\) with counting measure. Let \(f,g:\mathbb Z_p\to\mathbb C\) be arbitrary, nonzero functions; neither is assumed sparse, generic, unimodular, or normalized. Define
\[
\omega=e^{2\pi i/p},\qquad
V_gf(j,k)=\frac1{\sqrt p}\sum_{n\in\mathbb Z_p}f(n)\overline{g(n-j)}\omega^{-kn}.
\]
The support is the set of ordered pairs \((j,k)\in\mathbb Z_p^2\) for which this complex number is nonzero. Multiplying the transform by the harmless nonzero factor \(\sqrt p\) does not change its support.

Two standard inputs are the Cauchy--Davenport inequality and the prime cyclic Fourier uncertainty principle: if a nonzero \(h:\mathbb Z_p\to\mathbb C\) has time support cardinality \(r\), then its discrete Fourier transform has at least \(p+1-r\) nonzero frequencies. The full argument using these inputs and an additional short character-product lemma follows.

## Proof
Let
\[
a=|\operatorname{supp}f|,\quad b=|\operatorname{supp}g|,\quad
h_j(n)=f(n)\overline{g(n-j)}.
\]
Set \(K=\{j:h_j\not\equiv0\}\). Its cardinality equals the difference-set size \(|\operatorname{supp}f-\operatorname{supp}g|\), so Cauchy--Davenport gives
\[
|K|\ge\min(p,a+b-1).
\]
Each nonzero row \(V_gf(j,\cdot)\) is the Fourier transform of \(h_j\), up to normalization. Prime-order Fourier uncertainty therefore gives
\[
\left|\operatorname{supp}V_gf(j,\cdot)\right|
\ge p+1-|\operatorname{supp}h_j|
\qquad(j\in K).
\]
Each ordered pair \((n,m)\) with \(f(n)\ne0\) and \(g(m)\ne0\) contributes to exactly one time-row \(j=n-m\); consequently
\[
\sum_{j\in\mathbb Z_p}|\operatorname{supp}h_j|=ab.
\]
Writing \(s=|\operatorname{supp}V_gf|\), we obtain the exact combinatorial lower estimate
\[
\tag{1}s\ge(p+1)|K|-ab.
\]

**Case 1: at least one input has a zero.** When \(a+b>p\) and \((a,b)\ne(p,p)\), the difference set has size \(p\) and \(ab\le p(p-1)\). Equation (1) yields
\[
s\ge p(p+1)-p(p-1)=2p.
\]
When \(a+b\le p\), define
\[
F(a,b)=(a+b-1)(p+1)-ab.
\]
For positive integers \(a,b\le p\), its increment upon raising \(a\) by one is \(p+1-b>0\), and symmetrically for \(b\). Apart from \((a,b)=(1,1)\), the smallest admissible value is thus
\[
F(1,2)=F(2,1)=2p.
\]
In the omitted singleton-pair case, exactly one \(h_j\) is nonzero at exactly one coordinate and its Fourier transform has all \(p\) frequencies nonzero, so \(s=p\). All non-full-support cases are settled.

**Case 2: both inputs have full support.** Suppose \(a=b=p\). Every row \(h_j\) is now nonzero everywhere. Write
\[
t_j=|\operatorname{supp}V_gf(j,\cdot)|,\qquad
s=\sum_{j\in\mathbb Z_p}t_j.
\]
If all \(t_j\ge2\), then \(s\ge2p\). Assume at least one row has \(t_j=1\) and relabel the time shifts so that it is \(j=0\). The corresponding coefficient field \(h_0\) must be a nonzero scalar multiple of a character:
\[
h_0(n)=c\omega^{qn}
\]
for some \(c\ne0\) and \(q\in\mathbb Z_p\).

Put \(G(n)=\overline{g(n)}\), which is nonvanishing, and
\[
r_j(n)=\frac{G(n-j)}{G(n)}.
\]
Then \(h_j=h_0r_j\). Multiplying by \(h_0\) merely translates Fourier frequencies, so \(t_j\) equals the Fourier support cardinality of \(r_j\). The ratios satisfy the cocycle identity
\[
\tag{2}r_{j+d}(n)=r_j(n)r_d(n-j).
\]
If a second row \(d\ne0\) has \(t_d=1\), its ratio \(r_d\) is also a scalar character. Equation (2) shows inductively that \(r_{md}\) is a scalar character for every integer \(m\). As \(d\) generates \(\mathbb Z_p\), every row has Fourier support one. Hence \(s=p\).

Suppose instead that \(j=0\) is the **unique** row with \(t_j=1\). All other rows have \(t_j\ge2\). If any one of them has \(t_j\ge3\), then
\[
s\ge1+3+2(p-2)=2p.
\]
We show that such a row necessarily exists. If \(t_1\ge3\), it is already present. Otherwise \(t_1=2\), and the discrete Fourier inversion formula supplies distinct \(u,v\in\mathbb Z_p\) and nonzero \(A,B\in\mathbb C\) such that
\[
r_1(n)=A\omega^{un}+B\omega^{vn}.
\]
From the definition, \(r_2(n)=r_1(n)r_1(n-1)\). Expanding gives
\[
\begin{aligned}
r_2(n)={}&A^2\omega^{-u}\omega^{2un}\\
&+AB(\omega^{-u}+\omega^{-v})\omega^{(u+v)n}\\
&+B^2\omega^{-v}\omega^{2vn}.
\end{aligned}
\]
For odd prime \(p\), the three frequency indices \(2u,u+v,2v\) are pairwise distinct. Moreover \(\omega^{-u}+\omega^{-v}\ne0\), since this would require the \(p\)-th root of unity \(\omega^{u-v}\) to equal \(-1\), impossible when \(p\) is odd. Thus all three Fourier coefficients displayed above are nonzero, and \(t_2=3\). Hence \(s\ge2p\), completing Case 2 and the proof.

**Sharpness.** With \(f=g=\delta_0\), only one time row is nonzero and all its \(p\) Fourier frequencies are nonzero, giving \(s=p\). With \(f=\delta_0\) and \(g=\delta_0+\delta_1\), exactly two time rows are nonzero; each comes from a one-point coefficient field, so each has all \(p\) frequencies nonzero, giving \(s=2p\).

## Verification
Every step above is an identity or a prime-order finite Fourier inequality; there is no asymptotic approximation, numerical optimization, or unproved conjecture. The Cauchy--Davenport and Fourier-support steps reproduce the argument behind Proposition 4.3 of Krahmer--Pfander--Rashkov. The additional part is the character-ratio cocycle and three-frequency expansion, which closes the full-support case that the earlier bound alone leaves at \(s\ge p\).

The odd-prime restriction is essential. On \(\mathbb Z_2\), take
\[
f=(1,1/2),\qquad g=(1,2).
\]
At time zero the coefficient row is \((1,1)\) and has exactly one nonzero Fourier coefficient; at time one it is \((2,1/2)\) and has two. Thus the STFT has three nonzero entries, strictly between \(2\) and \(4\).

As a non-proof numerical sanity test, exact Gaussian-integer coefficient calculations checked \(19{,}891\), \(19{,}999\), and \(20{,}000\) sampled nonzero signal-window pairs at primes \(3\), \(5\), and \(7\), respectively, with no value in the claimed forbidden interval. Infinite validity follows from the proof, not from this sampling.

## Relationship to prior work
Krahmer, Pfander, and Rashkov (2008), Proposition 4.3, bound STFT support in terms of the input support sizes. This already forces at least \(2p\) coefficients unless both inputs have full support or both are singletons. Their Figure 4 also records small-prime possibilities, including the case \(p=3\). That bound does not eliminate the intermediate \(p+1\) through \(2p-1\) possibilities when both inputs have full support.

Fernández, Galbis, and Martínez (2014), Theorem 3, and Nicola (2022/2023), Theorem 1.2, classify exact support-minimizing pairs. In particular Nicola identifies the coset geometry of the \(p\)-element support. Those results address equality at \(p\), not the sharp *second* attainable cardinality among arbitrary signal-window pairs.

Studies of generic windows or of pairs in which both inputs are two-sparse address different quantifiers and support strata. The gap proved here is uniform over **all** complex windows and signals, including exceptional non-generic full-support pairs. The exact sharp threshold \(2p\), rather than just the \(p\)-coefficient uncertainty minimum, is the new statement under review.

## Limitations
Only odd prime cyclic groups are claimed. The proof works for \(p=3\), but that finite case was already charted in earlier literature and is not claimed as a new isolated classification. The conclusion is **cardinality-based** and does not control small nonzero STFT amplitudes, approximate support, numerical thresholds, or noisy concentration. It does not classify the pairs attaining \(2p\), nor does it assert a full support spectrum above \(2p\). An unindexed equivalent statement in the broader time-frequency literature cannot be excluded.

## References
1. F. Nicola, *The uncertainty principle for the short-time Fourier transform on finite cyclic groups: cases of equality*, arXiv:2204.14176v1, first public 29 April 2022; Journal of Functional Analysis 284 (2023), 109924, DOI 10.1016/j.jfa.2023.109924.
2. F. Krahmer, G. E. Pfander, and P. Rashkov, *Uncertainty in time-frequency representations on finite Abelian groups and applications*, Applied and Computational Harmonic Analysis 25 (2008), 209--225, DOI 10.1016/j.acha.2007.09.008, especially Proposition 4.3 and Figure 4.
3. C. Fernández, A. Galbis, and J. Martínez, *Localization operators and an uncertainty principle for the discrete short time Fourier transform*, Abstract and Applied Analysis (2014), Article 131459, DOI 10.1155/2014/131459, especially Theorem 3.
4. T. Tao, *An uncertainty principle for cyclic groups of prime order*, Mathematical Research Letters 12 (2005), 121--127, DOI 10.4310/MRL.2005.v12.n1.a11.
