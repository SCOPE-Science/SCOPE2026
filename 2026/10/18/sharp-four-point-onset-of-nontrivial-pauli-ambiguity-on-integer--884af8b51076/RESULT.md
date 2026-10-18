# Sharp four-point onset of nontrivial Pauli ambiguity on integer signals

## Finding

Let \(f:\mathbb Z\to\mathbb C\) be finitely supported and nonzero, with Fourier series \(\widehat f(\theta)=\sum_{n\in\mathbb Z}f(n)e^{in\theta}\) for every \(\theta\in\mathbb R\). Its Pauli data consist of all position magnitudes \(|f(n)|\) and all frequency magnitudes \(|\widehat f(\theta)|\). Two signals are called trivially associated when one is a global unit-modulus scalar and translate of the other, or a global unit-modulus scalar times a translated conjugate reflection.

**Theorem.** If \(|\operatorname{supp}f|\le3\), every finitely supported signal with the same Pauli data as \(f\) is trivially associated to \(f\). The threshold is exact: nontrivially associated signals with identical Pauli data and exactly four nonzero coordinates exist. Hence the minimum support cardinality for genuinely nontrivial one-dimensional finitely supported Pauli partners is \(4\).

Moreover, for **every** real pair \((s,t)\) such that \(s\ne0\), \(t\ne0\), and \(|t|\ne1\), the polynomials
\[
F_{s,t}(z)=(1-tz)(1+i s z+z^2),\qquad
G_{s,t}(z)=(1-tz)(1-i s z+z^2)
\]
are Fourier polynomials of such a four-point nontrivial pair. An explicit Gaussian-integer instance is
\[
f=(1,-2+i,1-2i,-2),\qquad g=(1,-2-i,1+2i,-2),
\]
with coordinates indexed by \(0,1,2,3\) and zero outside this range.

## Assumptions and scope

The frequency variable ranges over the **whole continuous torus** \(\mathbb R/(2\pi\mathbb Z)\), not merely finitely many sampled discrete Fourier frequencies. The data include individually specified time-coordinate magnitudes, so the supports of Pauli partners coincide. There are no restrictions on nonzero complex coefficients or on the locations of at most three support points. A shift or conjugate reflection is considered trivial only when it actually preserves the data under comparison.

For \(k\in\mathbb Z\), use the aperiodic autocorrelation
\[
R_f(k)=\sum_{n\in\mathbb Z}f(n+k)\overline{f(n)}.
\]
Fourier expansion gives
\[
|\widehat f(\theta)|^2=\sum_{k\in\mathbb Z}R_f(k)e^{ik\theta}.
\]
Uniqueness of finite Fourier series implies equality of frequency magnitudes for all \(\theta\) exactly when the autocorrelations agree for every integer \(k\). No discretization or limiting argument is used.

## Proof

**Rigidity for at most three points.** Equal position magnitudes force equal support. The one-point case is a global phase. For two points \(a<c\), multiply each candidate independently by a unit scalar so that both first coefficients equal a positive real number \(A\). The outermost autocorrelation \(R(c-a)=f(c)\overline{f(a)}\) fixes the other coefficient, yielding equality.

Now let the common support be \(a<b<c\), with initial coefficients \(A,B,C\) and partner coefficients \(A,D,E\), where \(A>0\). Equality of the outermost autocorrelation forces \(E=C\). Put \(u=b-a\) and \(v=c-b\). If \(u\ne v\), the autocorrelation at lag \(u\) has the single contribution \(B\overline A\). Thus \(D=B\).

If \(u=v\), the lag-\(u\) identity becomes
\[
A D+C\overline D=A B+C\overline B,
\qquad |D|=|B|.
\]
If \(|C|\ne A\), subtraction and absolute values show \(D=B\), because a nonzero difference \(\delta\) satisfying \(A\delta+C\overline\delta=0\) would force \(A=|C|\).

If \(|C|=A\), write \(C=A\eta\) with \(|\eta|=1\). The two conditions reduce to a fixed real part of \(\eta^{-1/2}D\) and a fixed modulus of \(D\). The intersection of a circle and a vertical line has at most two points, so
\[
D=B\quad\text{or}\quad D=\eta\overline B.
\]
In the second case the entire partner, after the preceding phase normalization, equals \(\eta\overline{f(a+c-n)}\) at every integer \(n\). It is precisely the allowed conjugate reflection, since the endpoints have equal magnitudes. This exhausts every three-point support configuration.

**Four-point construction.** For real nonzero \(s,t\), the coefficient lists of \(F_{s,t}\) and \(G_{s,t}\) are respectively
\[
(1,-t+i s,1-i s t,-t),\qquad
(1,-t-i s,1+i s t,-t).
\]
They are complex conjugates coordinatewise; all four entries are nonzero, and their position magnitudes agree. On \(z=e^{i\theta}\),
\[
1+i s z+z^2=z(2\cos\theta+i s),
\]
so both polynomials have the same **full-circle** squared modulus,
\[
|F_{s,t}(e^{i\theta})|^2
=|G_{s,t}(e^{i\theta})|^2
=(1+t^2-2t\cos\theta)(4\cos^2\theta+s^2).
\]
Since both supports are exactly \(\{0,1,2,3\}\), a translation preserving that support must be the identity. Their coefficients at \(0\) are both \(1\), forcing any global phase between them to be \(1\), but their coefficients at \(1\) differ because \(s\ne0\). A translated conjugate reflection preserving the support must map \(n\) to \(3-n\), and would exchange the endpoint magnitudes \(1\) and \(|t|\). This is impossible when \(|t|\ne1\). Hence these are nontrivial Pauli partners. The lower-bound proof and construction yield the exact threshold \(4\).

For the integer witness \(s=1,t=2\), the nonnegative-lag autocorrelations are precisely \(15,-8,5,-2\), all real. Therefore the Fourier intensity equals \(15-16\cos\theta+10\cos(2\theta)-4\cos(3\theta)\). These identities supply an independent exact-arithmetic form of the certificate.

## Verification

The included standalone program `verify.py` uses rational complex pairs and Python standard-library fractions. It checks the entire autocorrelation vector for sixteen rational pairs \((s,t)\) in the stated admissible region, the closed-form identities
\[
R(0)=(1+t^2)(2+s^2),\quad
R(1)=-t(3+s^2),\quad R(2)=1+t^2,\quad R(3)=-t,
\]
the explicit integer witness, and a three-point conjugate-reflection instance. Execution command: `python verify.py`. All equality claims in the proof are algebraic and established for the whole parameter range; the finite test grid is supplemental rather than the source of the general theorem.

## Relationship to prior work

Novikov and Xu (2026, arXiv:2604.25662v1) study both discrete Pauli data and nontrivial partners; their Theorems 1–2 construct examples through finite-difference operators and disjoint shifted supports. Their statements and proofs do not present the minimum one-dimensional support size or the present explicit four-coordinate family. The complete manuscript was compared at the level of its objects, conditions, examples, and proofs.

Friedman (1989, Section 3) explicitly formulated finite-dimensional Pauli data as coordinate magnitudes plus aperiodic autocorrelations and noted the low-dimensional case as elementary. The three-point rigidity argument above supplies the requisite arbitrary-support statement, but low-dimensional uniqueness by itself is not claimed to be historically new. Corbett and Hurst (1977/78) study continuous \(L^2\) wave functions, while Ranieri and collaborators (2013) principally investigate Fourier-only sparse phase retrieval; neither inspected result determines the exact four-point cutoff for simultaneous discrete position/Fourier magnitude data. Ramos and Sousa (2025) address sampled-data continuation for real-line Fourier uniqueness, not the present support-count threshold.

## Limitations

The result concerns finitely supported sequences on \(\mathbb Z\) observed at every frequency on the continuous torus. It does not establish the analogous threshold for a finite cyclic group using only the finite discrete Fourier transform, classify all four-point Pauli fibers, or quantify noise-stable recovery. The four-point family does not assert that all four-point supports permit ambiguity. Exhaustive bibliographic uniqueness is not certified; an older unindexed equivalent four-point construction may exist. Independent mathematical audit has not been performed.

## References

1. R. G. Novikov and T. Xu, *On Phase Retrieval for Continuous and Discrete Fourier Transforms*, arXiv:2604.25662v1 (first public version 28 April 2026), https://arxiv.org/abs/2604.25662.
2. C. N. Friedman, *Some remarks on Pauli data in quantum mechanics*, J. Austral. Math. Soc. Ser. B **30** (1989), 298–303, https://doi.org/10.1017/S033427000000624X.
3. J. V. Corbett and C. A. Hurst, *Are wave functions uniquely determined by their position and momentum distributions?*, J. Austral. Math. Soc. Ser. B **20** (1977/78), 182–201, https://doi.org/10.1017/S0334270000001569.
4. J. Ranieri, A. Chebira, Y. M. Lu and M. Vetterli, *Phase Retrieval for Sparse Signals: Uniqueness Conditions*, arXiv:1308.3058 (2013), https://arxiv.org/abs/1308.3058.
5. J. P. G. Ramos and M. Sousa, *On Pauli pairs and Fourier uniqueness problems*, J. London Math. Soc. **112** (2025), e70358, https://doi.org/10.1112/jlms.70358.
