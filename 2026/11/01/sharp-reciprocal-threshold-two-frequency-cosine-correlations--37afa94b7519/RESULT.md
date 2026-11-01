# Sharp reciprocal-threshold two-frequency cosine correlations

## Finding

For an integer \(m\ge5\), put \(\alpha_m=\cos(2\pi/m)\), and let \(\mathbb T=\mathbb R/\mathbb Z\) have normalized Lebesgue measure \(\mu\). For distinct positive integers \(a,b\), define
\[
P_m(a,b)=\mu\{t\in\mathbb T:\ [\cos(2\pi at)>\alpha_m\text{ and }\cos(2\pi bt)>\alpha_m]\ \text{or}\ [\cos(2\pi at)<-\alpha_m\text{ and }\cos(2\pi bt)<-\alpha_m]\}.
\]
Let \(L_m\) be the largest odd integer strictly less than \(m\): \(L_m=m-1\) if \(m\) is even and \(L_m=m-2\) if \(m\) is odd. Then
\[
\boxed{\min_{a\ne b}P_m(a,b)=\frac{4}{mL_m}.}
\]
The minimizing unordered frequency sets are *exactly* the positive integer dilates of \(\{1,L_m\}\), together with the positive integer dilates of \(\{1,9\}\) when \(m=5\). There are no further equality cases.

The same proof also recovers the previously known zero-threshold endpoint \(m=4\), where the minimum is \(1/3\) and equality occurs only for dilates of \(\{1,3\}\); that endpoint is not claimed as a new contribution.

The theorem depends only on the two positive and negative level arcs. Consequently, for every continuous, even, \(1\)-periodic \(f\) that is strictly decreasing on \([0,1/2]\), normalized by \(f(0)=1\), and satisfies \(f(t+1/2)=-f(t)\), the same minimum and minimizers hold with \(f(1/m)\) in place of \(\alpha_m\) and \(f(at),f(bt)\) in place of the cosines.

## Assumptions and scope

Frequencies \(a,b\) range over all **distinct positive integers**, without a frequency cutoff; \(m\) ranges over all integers at least five. All endpoint inequalities defining the level sets are strict; their boundaries have measure zero. The monotonicity assumption on the optional waveform extension guarantees exactly two antipodal level arcs of half-width \(1/m\). No result is asserted for nonreciprocal half-widths, more than two frequencies, or an arbitrary non-antipodal waveform.

Since \(t\mapsto dt\) preserves normalized measure for every positive integer \(d\), we have \(P_m(da,db)=P_m(a,b)\). It therefore suffices to analyze coprime \(1\le a<b\).

## Proof

**1. Exact Fourier formula.** Set \(\rho=1/m\), \(U(t)=\mathbf1_{\{\|t\|_{\mathbb T}<\rho\}}\), and \(V(t)=U(t-1/2)\). The event probability is the sum of \(\int U(at)U(bt)\,dt\) and \(\int V(at)V(bt)\,dt\). For nonzero integer \(k\),
\[
\widehat U(k)=\frac{\sin(2\pi k/m)}{\pi k},\qquad
\widehat V(k)=(-1)^k\widehat U(k),\qquad \widehat U(0)=\widehat V(0)=\frac2m.
\]
For coprime \(a,b\), a nonzero Fourier frequency matches in the two factors only at indices \(jb\) and \(-ja\), with nonzero integer \(j\). Introduce the continuous periodic Bernoulli function
\[
B(x)=\{x\}^2-\{x\}+\frac16,\qquad
\sum_{j=1}^{\infty}\frac{\cos(2\pi jx)}{j^2}=\pi^2B(x).
\]
The Fourier series and product-to-sum formula yield two exact rational expressions:
\[
P_m(a,b)=\frac8{m^2}+\frac2{ab}
\left[B\left(\frac{b-a}{m}\right)-B\left(\frac{a+b}{m}\right)\right]
\quad\text{if }a,b\text{ are odd},\tag{1}
\]
\[
P_m(a,b)=\frac8{m^2}+\frac1{2ab}
\left[B\left(\frac{2(b-a)}m\right)-B\left(\frac{2(a+b)}m\right)\right]
\quad\text{if }a,b\text{ have opposite parity}.\tag{2}
\]
The mixed-parity formula follows because only even Fourier indices survive addition of the two antipodal correlations. It is legitimate to integrate the products by their Fourier coefficients, since the indicator Fourier coefficients are square summable and the resulting correlation series is absolutely convergent.

**2. Two elementary estimates.** Since the periodic Bernoulli function has minimum \(-1/12\) and maximum \(1/6\), for any \(x,y\) one has \(B(x)-B(y)\ge-1/4\). Moreover, for any real \(x\) and \(0\le\delta\le1\),
\[
B(x)-B(x+\delta)\ge-\delta(1-\delta).\tag{3}
\]
To prove (3), reduce \(x\) modulo one. On each of the intervals \([0,1-\delta]\) and \([1-\delta,1]\), the difference is affine in \(x\). On the first interval it decreases to \(-\delta(1-\delta)\); on the second it increases from that value. Thus (3) holds everywhere, with no approximation.

**3. Both frequencies odd, \(b\le L_m\).** Near \(t=0\), both frequencies are positive above threshold for \(|t|<1/(mb)\). Near \(t=1/2\), both are negative below the opposite threshold on the same half-width, since both frequencies are odd. Therefore \(P_m(a,b)\ge4/(mb)\ge4/(mL_m)\). If equality holds, necessarily \(b=L_m\). For odd \(a,b<m\), equation (1) simplifies to
\[
P_m(a,b)=\begin{cases}
\dfrac4{mb},& a+b\le m,\\[2mm]
\dfrac{4(2a+b-m)}{abm},& a+b>m.
\end{cases}\tag{4}
\]
When \(b=L_m\), the first branch is possible only for \(a=1\), and in the second branch the value is strictly greater than \(4/(mb)\). Hence equality is possible here precisely for \(\{a,b\}=\{1,L_m\}\).

**4. Both frequencies odd, \(b>L_m\).** Necessarily \(b\ge m\). If \(a>m/2\), equation (1), the range of \(B\), and \(ab>m^2/2\) give
\[
P_m(a,b)\ge\frac8{m^2}-\frac1{2ab}>\frac7{m^2}>\frac4{mL_m}
\]
for every \(m\ge5\).

Suppose next that \(a\le m/2\). Taking \(\delta=2a/m\) in (3), and exploiting periodicity of \(B\), equation (1) gives
\[
P_m(a,b)\ge\frac8{m^2}-\frac4{mb}\left(1-\frac{2a}{m}\right).
\tag{5}
\]
If \(m\) is even, then \(b\ge m+1\), so the right side of (5) is at least \(4(m+4)/(m^2(m+1))\), strictly exceeding \(4/[m(m-1)]\). If \(m\) is odd and \(b=m\), the two Bernoulli values in (1) are equal by reflection symmetry, and \(P_m(a,m)=8/m^2>4/[m(m-2)]\). If \(m\ge7\) is odd and \(b\ge m+2\), (5) gives \(P_m(a,b)\ge4(m+6)/(m^2(m+2))>4/[m(m-2)]\).

The remaining odd case is \(m=5\). Here \(a\le5/2\) and odd forces \(a=1\). For \(b=5\) or \(b=7\), direct substitution into (1) gives respectively \(8/25\) or \(12/35\), both strictly greater than \(4/15\). For \(b\ge9\), (5) reduces to \(P_5(1,b)\ge8/25-12/(25b)\ge4/15\), with equality possible only when \(b=9\). Formula (1) gives \(P_5(1,9)=4/15\). This is the exceptional second minimizing orbit.

**5. Opposite parities.** The common positive arc centered at \(0\) gives \(P_m(a,b)\ge2/(mb)\). If \(b\le L_m/2\), this is strictly greater than \(4/(mL_m)\), because \(L_m\) is odd. Hence assume \(b>L_m/2\), which for integer \(b\) implies \(b\ge(m-1)/2\).

If \(a\le m/4\), apply (3) with \(\delta=4a/m\) to (2). As \(a\ge1\), this yields
\[
P_m(a,b)\ge\frac8{m^2}-\frac2{mb}\left(1-\frac{4a}{m}\right)
\ge\frac{4(m+2)}{m^2(m-1)}>\frac4{mL_m}
\]
for every \(m\ge5\). If \(a>m/4\), then \(ab>m(m-1)/8\); from the range of \(B\) in (2),
\[
P_m(a,b)\ge\frac8{m^2}-\frac1{8ab}>
\frac{7m-8}{m^2(m-1)}>\frac4{mL_m}.
\]
For odd \(m\ge5\), the last inequality is equivalent to \(3m^2-18m+16>0\); for even \(m\), it is immediate. Thus no mixed-parity pair attains the minimum.

**6. Attainment and waveform independence.** Substituting \(a=1,b=L_m\) in (4) gives exactly \(4/(mL_m)\); at \(m=5\) the exceptional value was established above. Steps 3–5 exhaust all coprime positive pairs, and the initial gcd reduction supplies exactly their integer dilates. For the waveform extension, monotonicity, evenness, and antipodal symmetry identify the positive and negative threshold events *exactly* with the intervals used in Step 1. Their measures and equality cases therefore do not depend on the waveform profile. This proves the complete statement. \(\square\)

## Verification

The standalone, dependency-free `CHECK.py` computes the correlation in two independent ways: (i) exact rational Bernoulli/Fourier formulas and (ii) exact rational intersections of positive/negative threshold arcs. It compares all coprime pairs with \(a<b<28\) and all \(4\le m\le21\), and separately checks every coprime pair with \(b\le160\) for \(4\le m\le52\) against the theorem's value and complete equality list. Exact arithmetic, not floating-point tolerance, is used throughout. It also checks the periodic-Bernoulli difference bound at rational grid points. The script prints `CHECK_OK 386617`. These bounded computations do **not** constitute the proof for unbounded frequencies and threshold indices; the case analysis in Steps 1–6 does.

Run `python3 CHECK.py` with Python 3. No third-party packages or data files are required.

## Relationship to prior work

Clément and Steinerberger (first publicly posted December 23, 2024) study discrete sign-rounded Fourier matrices and quantify the parity/arithmetic dependence of pairwise cosine signs. Their theorem is a finite-field sampled, zero-threshold correlation estimate, not an exact *continuous positive-threshold* two-frequency minimization. The zero-threshold instance \(m=4\) is already known from Gonçalves, Oliveira e Silva, and Steinerberger (2019), and is explicitly recorded by Dou et al. (first posted in 2022) and Zang et al. (submitted October 23 and announced October 27, 2026). The last paper studies sharp sign correlations for four cosines and large-frequency-count asymptotics, but not the sharp two-frequency *positive-threshold* family proved here.

Giannitsi and Madrid (first posted October 28, 2026) introduce the general antipodal-wave threshold-correlation framework and prove, for half-width \(1/m\), the bound \(F_{\alpha}(n)\ge4/m^n\) and the large-\(n\) exponential decay rate. Their available full text does not give the exact finite-dimensional two-frequency constant, parity-dependent equality cases, or the \(m=5\) exceptional minimizer. The new value \(4/(mL_m)\) is strictly larger than their general lower bound \(4/m^2\). The comparison concerns theorem implications, rather than merely differing terminology.

## Limitations

The exact formula applies only to reciprocal half-widths and two frequencies. It does not resolve three-or-more-frequency sharp thresholds or arbitrary nonreciprocal thresholds. The second minimizing orbit at \(m=5\) has been established analytically rather than inferred from a finite search. While the closest full-text primary papers and relevant semantic research records were compared, an unindexed or differently phrased earlier exact two-frequency classification remains possible.

## References

1. F. Gonçalves, D. Oliveira e Silva, and S. Steinerberger, *A Universality Law for Sign Correlations of Eigenfunctions of Differential Operators*, arXiv:1903.06826, first posted 2019-03-15. https://arxiv.org/abs/1903.06826
2. S. Dou, A. Goh, K. Liu, M. Legate, and G. Pettigrew, *Cosine Sign Correlation*, arXiv:2212.02496, first posted 2022-12-05. https://arxiv.org/abs/2212.02496
3. F. Clément and S. Steinerberger, *Failure of Orthogonality of Rounded Fourier Bases*, arXiv:2412.17466, first posted 2024-12-23. https://arxiv.org/abs/2412.17466
4. S. Zang, Y. Zhao, Y. Zhao, and C. Zhou, *Extremal Cosine Sign Correlations*, arXiv:2610.33190, submitted 2026-10-23 and announced 2026-10-27. https://arxiv.org/abs/2610.33190
5. C. Giannitsi and J. Madrid, *Exponential Decay of Threshold Correlations for Symmetric Periodic Functions*, arXiv:2610.38135, first posted 2026-10-28. https://arxiv.org/abs/2610.38135
