# Intermittent mass dimension of the canonical spectrum of a deterministic Salem measure

## Finding
For every \(0<s<1\), let \(\mu_s\) be the deterministic Salem spectral measure constructed by Lai--Shi--Xie, and let \(\Lambda\subset\mathbb Z\) be the canonical exponential spectrum in their Theorem 4.2. Define
\[
C(R)=\#\bigl(\Lambda\cap[-R,R]\bigr),\qquad R\ge 1.
\]
Then
\[
\liminf_{R\to\infty}\frac{\log C(R)}{\log R}=0,
\qquad
\limsup_{R\to\infty}\frac{\log C(R)}{\log R}=s.
\]
Thus the canonical orthonormal exponential basis has lower centered mass dimension \(0\) and upper centered mass dimension \(s\). Replacing \(\log R\) by \(\log(2R)\), as in another common normalization of mass dimension, gives the same two values.

## Assumptions and scope
Fix \(0<s<1\). In the notation of Lai--Shi--Xie, put
\[
q_n=n+\lceil 2/s\rceil,\qquad r_n=\lfloor s q_n\rfloor,
\]
let \(p_n\) be the odd primes chosen in their construction, and set
\[
N_n=p_n^{q_n},\qquad M_n=p_n^{r_n},\qquad P_n=\prod_{j=1}^n N_j,
\qquad h_n=\frac{N_n}{M_n}=p_n^{q_n-r_n}.
\]
Their canonical spectrum is
\[
\Lambda=\bigcup_{n\ge 1}\Lambda_n,
\qquad
\Lambda_n=L_1+P_1L_2+\cdots+P_{n-1}L_n,
\]
with
\[
L_n=h_n\left\{-\frac{M_n-1}{2},\ldots,\frac{M_n-1}{2}\right\}.
\]
The construction also gives \(N_n>P_{n-1}^{\,n}\) and \(N_n\ge 27\). The present statement concerns only this particular canonical spectrum and only the centered counting function above.

## Proof
Write
\[
A_n=\prod_{j=1}^n M_j.
\]
First, the mixed-radix representation in \(\Lambda_n\) is unique. Indeed, the level-\(j\) digit difference is a multiple of \(h_j\) of absolute value at most
\[
h_j(M_j-1)=N_j-h_j<N_j.
\]
If two level-\(n\) expansions agree, reduction modulo \(N_1\) forces equality of their first digits; division by \(N_1\) and iteration forces equality at every level. Hence
\[
\#\Lambda_n=A_n.
\]

Let \(R_n=\max\{|\lambda|:\lambda\in\Lambda_n\}\). Directly from the digit ranges,
\[
R_n=\frac12\sum_{j=1}^nP_{j-1}(N_j-h_j)
=\frac12\sum_{j=1}^nP_j\left(1-\frac1{M_j}\right).
\]
Since \(p_j\ge3\) and \(r_j\ge2\), one has \(M_j\ge9\). Therefore
\[
\frac49P_n\le R_n.
\]
Also \(N_j\ge27\) implies
\[
\sum_{j<n}\frac{P_j}{P_n}<\frac1{26},
\]
so
\[
R_n<\frac12\left(1+\frac1{26}\right)P_n=\frac{27}{52}P_n.
\]

The centers introduced at level \(n+1\) are spaced by
\[
G_{n+1}=P_nh_{n+1}.
\]
Because \(h_{n+1}\ge3\),
\[
G_{n+1}>3P_n>2R_n.
\]
Consequently the nonzero level-\(n+1\) translates of \(\Lambda_n\) miss \([-R_n,R_n]\). The same holds for all later levels: if \(k\ge n+2\), the smallest possible absolute value from a nonzero level-\(k\) digit is at least \(G_k-R_{k-1}\), which exceeds \(2P_{k-1}\) and hence exceeds \(R_n\). Thus
\[
C(R_n)=A_n.
\]

The source construction has \(r_n/q_n\to s\), while \(N_n>P_{n-1}^{\,n}\) makes the last logarithmic scale dominate all previous ones. Hence
\[
\frac{\log A_n}{\log P_n}
=\frac{\sum_{j\le n}r_j\log p_j}{\sum_{j\le n}q_j\log p_j}
\longrightarrow s.
\]
Since \(R_n/P_n\) stays between positive constants,
\[
\frac{\log C(R_n)}{\log R_n}
=\frac{\log A_n}{\log P_n+O(1)}\longrightarrow s,
\]
which proves the lower bound \(\limsup\ge s\).

Now put
\[
S_n=G_{n+1}-R_n-\frac12.
\]
No new level enters the centered interval before this radius, so \(C(S_n)=A_n\). Because \(0<s<1\), there is a constant \(c_s>0\) such that eventually
\[
\frac{q_{n+1}-r_{n+1}}{q_{n+1}}\ge c_s.
\]
Therefore
\[
\log h_{n+1}\ge c_s\log N_{n+1}>c_s(n+1)\log P_n.
\]
Since \(A_n\le P_n\) and \(S_n\) is comparable to \(P_nh_{n+1}\), it follows that
\[
0\le\frac{\log C(S_n)}{\log S_n}
\le\frac{\log P_n}{\log h_{n+1}+\log P_n+O(1)}\longrightarrow0.
\]
Thus \(\liminf=0\).

It remains to rule out a larger limsup between completed stages. For \(R_n\le R<G_{n+1}-R_n\), one has \(C(R)=A_n\), so the logarithmic ratio decreases from its value at \(R_n\). Once \(R\ge G_{n+1}-R_n\), only level-\(n+1\) clusters can enter before \(R_{n+1}\); later levels remain outside by the preceding separation estimate. Their centers have spacing \(G_{n+1}\), and each cluster contains \(A_n\) points. Hence, for all sufficiently large \(n\),
\[
C(R)\le 6A_n\frac{R}{G_{n+1}},
\qquad G_{n+1}-R_n\le R\le R_{n+1}.
\]
Because \(6A_n/G_{n+1}<1\) eventually, the upper bound
\[
\frac{\log C(R)}{\log R}
\le 1+\frac{\log(6A_n/G_{n+1})}{\log R}
\]
is increasing in \(R\) throughout this interval. At \(R_{n+1}\), its numerator differs by only \(O(1)\) from \(\log A_{n+1}\), while \(\log R_{n+1}=\log P_{n+1}+O(1)\). The resulting endpoint bound tends to \(s\). Therefore \(\limsup\le s\), completing the proof.

## Verification
The proof uses only the explicit spectrum formula and growth conditions in arXiv:2609.22772v1. The critical checks are: uniqueness of mixed-radix digits; exact stage cardinality \(A_n\); two-sided comparison \(R_n\asymp P_n\); the gap \(G_{n+1}>2R_n\); logarithmic domination from \(N_{n+1}>P_n^{\,n+1}\); and a uniform cluster-count bound between successive completed stages. No finite computation is used as a substitute for an infinite argument.

The conclusion is not a statement about Beurling dimension. Centered mass dimension records growth of the number of frequencies in expanding intervals centered at the origin, whereas Beurling dimension permits translated intervals and is therefore a different invariant. The proof also does not identify lower discrete Hausdorff dimension.

## Relationship to prior work
Lai--Shi--Xie construct the first singular Salem spectral measures on the real line and give the explicit canonical spectrum used here, but their paper does not state the two centered mass dimensions of that spectrum. The present calculation extracts a strong frequency-intermittency invariant from their mixed-radix formula.

Li--Wu study Beurling dimensions of spectra for a class of Moran measures, and Wu--Yin--Zhang study Beurling dimensions of frame spectra. Those results concern translated-window density invariants and do not imply the centered liminf/limsup pair proved here. Li--Zeng--Wu study lower discrete Hausdorff dimension of spectra for Moran measures, again a different invariant. Glasscock's work supplies standard counting/mass-dimension terminology for subsets of the integers but does not concern this Salem spectral construction.

## Limitations
The proof requires \(0<s<1\). At \(s=1\), the argument producing arbitrarily large empty logarithmic scales from \(q_n-r_n\) no longer applies, so no endpoint statement is claimed. Nothing is asserted about noncanonical spectra of \(\mu_s\), about Beurling dimension, about lower discrete Hausdorff dimension, or about optimality among all spectra.

A literature search found no statement equivalent to the exact pair \((0,s)\) for this canonical spectrum. Some older Moran-spectrum dimension papers were available only through abstracts or publisher previews during the comparison, so an equivalent specialized observation in inaccessible full text remains a residual literature risk.

## References
1. C.-K. Lai, R. Shi, Y.-H. Xie, *A new type of deterministic Salem sets and its spectrality*, arXiv:2609.22772v1, 19 September 2026.
2. L. Li, M. Wu, *Beurling dimensions of spectra for a class of Moran measures*, Applied and Computational Harmonic Analysis 68 (2024), 101606. DOI: 10.1016/j.acha.2023.101606.
3. L. Li, X. Zeng, M. Wu, *Lower discrete Hausdorff dimension of spectra for Moran measure*, Nonlinearity 37 (2024). DOI: 10.1088/1361-6544/ad7808.
4. M. Wu, Z. Yin, H. Zhang, *Beurling dimension of frame spectra for Moran measures*, Studia Mathematica 280 (2025). DOI: 10.4064/sm240305-25-9.
5. D. Glasscock, *Marstrand-type theorems for the counting and mass dimensions in \(\mathbb Z\)*, 2016.
