# Complete positive Fourier-support diagram on prime cyclic groups

## Finding

Let \(p\ge3\) be an odd prime. For a nonzero function \(f:\mathbb Z/p\mathbb Z\to[0,\infty)\), put \(k=|\operatorname{supp}f|\) and \(\ell=|\operatorname{supp}\widehat f|\), with the Fourier transform defined below. Then **the possible pairs \((k,\ell)\) are exactly**
\[
1\le k\le p,\qquad 1\le\ell\le p,\qquad \ell\text{ odd},\qquad k+\ell\ge p+1.
\]
Every admissible pair is realized by an explicit nonnegative sampled trigonometric polynomial. In particular, the exact minimum Fourier support for each time-support size is
\[
\min_{f\ge0,\,|\operatorname{supp}f|=k}|\operatorname{supp}\widehat f|
=\begin{cases}p+1-k,&k\text{ odd},\\ p+2-k,&k\text{ even}.\end{cases}
\]
The theorem classifies cardinalities, **not arbitrary prescribed support sets**.

## Assumptions and scope

All supports are exact supports, and \(f\) is pointwise nonnegative, real, and not identically zero. Identify the group with \(\{0,\ldots,p-1\}\) modulo \(p\); let \(\zeta=e^{2\pi i/p}\) and \(\widehat f(j)=\sum_{x=0}^{p-1}f(x)\zeta^{-jx}\). Normalizing the transform by \(1/p\) does not change supports. The prime assumption is used in the Chebotarev--Tao additive uncertainty inequality.

## Proof

**Necessity.** Tao's prime-cyclic uncertainty inequality gives \(k+\ell\ge p+1\). Because \(f\ge0\) and \(f\not\equiv0\), its zero-frequency Fourier coefficient \(\widehat f(0)=\sum_x f(x)\) is strictly positive. Since \(f\) is real, \(\widehat f(-j)=\overline{\widehat f(j)}\). For odd \(p\), every nonzero frequency belongs to a distinct opposite pair. Consequently \(\ell\) is odd. The trivial range bounds finish necessity.

**A nonnegative extremizer at every \(k\).** Put \(t=p-k\) and \(d=\lceil t/2\rceil\). For \(0\le r<\lfloor t/2\rfloor\), define on integer grid points
\[
B_r(x)=\cos(\pi/p)-\cos\bigl(2\pi(x-2r-\tfrac12)/p\bigr).
\]
The largest values of the second cosine on the sampled grid are exactly \(\cos(\pi/p)\), at the two adjacent residues \(2r\) and \(2r+1\); every other grid value is smaller. Hence \(B_r\ge0\) and its two grid zeros are exactly these residues. If \(t\) is odd, additionally set
\[
S_t(x)=1-\cos\bigl(2\pi(x-(t-1))/p\bigr),
\]
which is nonnegative and vanishes on the grid exactly at residue \(t-1\). Define
\[
F_t(x)=\prod_{0\le r<\lfloor t/2\rfloor}B_r(x)
\,\times\begin{cases}S_t(x),&t\text{ odd},\\1,&t\text{ even}.\end{cases}
\]
The empty product equals one. This function is zero exactly on residues \(0,1,\ldots,t-1\) and strictly positive on the other \(k\) residues. It is a trigonometric polynomial of degree at most \(d\), so its Fourier transform is supported within \(\{-d,\ldots,d\}\) modulo \(p\). Because \(2d+1\le p\), these frequencies are distinct. Their number is \(2d+1\). Necessity already proved gives \(\ell\ge t+1\) and \(\ell\) odd, hence \(\ell\ge2d+1\). Therefore \(F_t\) has **all** \(2d+1\) of those Fourier coefficients nonzero.

**Every larger odd Fourier-support size.** Choose an integer \(D\) with \(d\le D\le(p-1)/2\), and put \(e=D-d\). For sufficiently small \(\varepsilon>0\), consider
\[
F_{t,D,\varepsilon}(x)=F_t(x)\bigl(1+\varepsilon\cos(2\pi x/p)\bigr)^e.
\]
The second factor is strictly positive for \(0<\varepsilon<1\); the time support is unchanged. The resulting trigonometric polynomial has degree at most \(D\), so no Fourier coefficient outside \(\{-D,\ldots,D\}\) can occur. Write \(F_t(x)=\sum_{j=-d}^{d}c_j e^{2\pi ijx/p}\). The preceding paragraph shows \(c_j\ne0\) for all \(|j|\le d\). For each old frequency \(|j|\le d\), its new coefficient tends to \(c_j\ne0\) as \(\varepsilon\downarrow0\). For a new positive frequency \(j=d+s\), where \(1\le s\le e\), its coefficient has leading term
\[
c_d\binom es\left(\frac{\varepsilon}{2}\right)^s+O(\varepsilon^{s+1}),
\]
which is nonzero for sufficiently small positive \(\varepsilon\). The negative-frequency coefficients are their complex conjugates. Since there are finitely many coefficients, a single sufficiently small \(\varepsilon\) makes all \(2D+1\) coefficients nonzero. No modular aliasing occurs because \(D\le(p-1)/2\). Thus every odd \(\ell=2D+1\) between \(2d+1\) and \(p\) occurs. This is exactly the set of odd integers obeying \(\ell\ge p+1-k\), completing the classification.

## Verification

The companion standalone script `CHECK.py` evaluates the displayed constructions for each admissible pair at odd primes \(p\in\{3,5,7,11,13\}\), with relative numerical tolerances. These finite tests corroborate, but do not replace, the prime-uniform proof. The nonvanishing of all intermediate Fourier coefficients for sufficiently small \(\varepsilon\) follows from the displayed coefficient asymptotics, not from sampling a finite set of parameters.

## Relationship to prior work

Tao's prime-cyclic uncertainty theorem proves the lower support bound and realizes every admissible pair of prescribed supports over **complex** coefficients. That converse does not impose nonnegativity. Here nonnegativity forces nonzero DC and hence odd Fourier support; the cosine-pair construction proves that this parity obstruction is the **only additional restriction on cardinality pairs**. The classification does not extend Tao's stronger statement about *arbitrarily specified* support locations to the nonnegative setting. The 2023 discrete-Fourier uncertainty-diagram study concerns the unrestricted DFT support diagram and a different positivity notion arising in Kirkwood--Dirac distributions. Published investigations of small positive-atom supports on even prime-power groups likewise do not entail the prime-cyclic all-support cardinality classification.

## Limitations

The theorem concerns cardinality pairs on odd prime cycles, not the geometry of arbitrary prescribed time and frequency support sets; it does not assert positivity or support realizability with any fixed set of zero locations. It gives no condition-number or robust-noise guarantees. The continuous parameter \(\varepsilon\) is asserted to exist sufficiently small; no universal quantitative threshold is claimed. Searches and source comparison cannot exclude every unindexed antecedent; independent validation has not been performed.

## References

- T. Tao, *An uncertainty principle for cyclic groups of prime order*, arXiv:math/0308286, first posted 29 August 2003; see especially Theorem 1.1 and its converse, https://arxiv.org/abs/math/0308286.
- *Characterizing an Uncertainty Diagram and Kirkwood--Dirac Nonclassicality Based on Discrete Fourier Transform*, *Entropy* 25 (2023), article 1075, https://doi.org/10.3390/e25071075. Related complex-valued support-diagram context; not a positivity-constrained theorem for nonnegative functions.
