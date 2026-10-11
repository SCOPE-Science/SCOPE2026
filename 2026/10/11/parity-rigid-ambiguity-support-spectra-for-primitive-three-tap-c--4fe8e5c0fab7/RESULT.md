# Parity-rigid ambiguity-support spectra for primitive three-tap cyclic signals

## Finding
For every integer \(N\geq5\), take a primitive three-term arithmetic progression \(\{u,u+d,u+2d\}\subset\mathbb Z_N\), where \(\gcd(d,N)=1\), and a function \(f:\mathbb Z_N\to\mathbb C\) supported **exactly** there. Write \(A=f(u)\), \(B=f(u+d)\), \(C=f(u+2d)\), all nonzero. For its self short-time Fourier transform (ambiguity function)
\[
V_ff(x,k)=N^{-1/2}\sum_{t\in\mathbb Z_N}f(t)\overline{f(t-x)}\exp(-2\pi i kt/N),
\]
put \(S(f)=|\operatorname{supp}V_ff|\). Define \(\mu_N=\{\exp(2\pi i j/N):0\le j<N\}\),
\[
R=-\frac{B\overline A}{C\overline B},\qquad
P(z)=|A|^2+|B|^2z+|C|^2z^2,
\]
and \(e={\bf1}_{\{R\in\mu_N\}}\), \(h=|\{z\in\mu_N:P(z)=0\}|\). The **exact support law** is
\[
\boxed{S(f)=5N-2e-h.}
\]
The root count \(h\) belongs to \(\{0,1,2\}\) and has the following exhaustive coefficient criterion:

* \(h=2\) precisely when \(|A|=|C|\) and there is an integer \(j\) with \(N/4<j<N/2\) such that
  \[\frac{|B|^2}{|A|^2}=-2\cos\left(\frac{2\pi j}{N}\right).\]
* \(h=1\) precisely when \(N\) is even and \(|B|^2=|A|^2+|C|^2\).
* Otherwise \(h=0\).

Thus the **complete attainable support-size spectrum**, as \(f\) ranges over these signals, is
\[
\boxed{\{5N,5N-2,5N-4\}\quad\text{if }N\text{ is odd},}
\]
\[
\boxed{\{5N,5N-1,5N-2,5N-3,5N-4\}\quad\text{if }N\text{ is even}.}
\]
In either parity the sharp minimum is \(5N-4\). **Every** minimizing function and only such a function satisfies both \(R\in\mu_N\) and the \(h=2\) coefficient criterion above. In particular, odd cyclic orders have two forbidden support levels immediately below the maximum: \(5N-1\) and \(5N-3\).

## Assumptions and scope
Only cyclic orders \(N\ge5\), exactly three nonzero taps, and progressions with step invertible modulo \(N\) are covered. The transform is normalized by \(N^{-1/2}\), which does not affect support cardinality. The theorem is uniform in the three nonzero complex coefficients, their phases, the translation \(u\), and the invertible step \(d\). Root counts mean distinct sampled roots, so a double root at \(-1\) counts once. No claim is made for nonprimitive progressions, arbitrary three-point configurations or independent signal/window pairs.

## Proof
Translation and replacement of the index \(t\) by \(u+ds\), with \(d\) a unit, multiply individual Fourier rows by unimodular factors and permute both time-delay and frequency indices. Hence it suffices to take the support \(\{0,1,2\}\), with coefficients \(A,B,C\). Since \(N\ge5\), the difference set is exactly \(\{-2,-1,0,1,2\}\subset\mathbb Z_N\), with five distinct elements. All other delay rows vanish identically.

For a fixed frequency \(k\), put \(z=\exp(-2\pi ik/N)\). Up to the same nonzero factor \(N^{-1/2}\), the five potentially nonzero rows are
\[
\begin{aligned}
V_ff(2,k)&=C\overline A z^2,\\
V_ff(1,k)&=z(B\overline A+C\overline Bz),\\
V_ff(0,k)&=|A|^2+|B|^2z+|C|^2z^2,\\
V_ff(-1,k)&=A\overline B+B\overline Cz,\\
V_ff(-2,k)&=A\overline C.
\end{aligned}
\]
The outer two rows are nonzero at every one of the \(N\) frequencies. The \(x=1\) row has exactly one frequency zero if and only if \(z=R\in\mu_N\), and no zeros otherwise. The root of the \(x=-1\) row is \(\overline R\); hence its zero count is identical. This gives a total of \(2e\) zeros from the two middle noncentral rows. The central row has \(h\) frequency zeros by definition. Subtracting from the five full rows proves \(S(f)=5N-2e-h\).

It remains to classify \(h\) without relying on numerical Fourier samples. Put \(r_0=|A|^2>0\), \(r_1=|B|^2>0\), \(r_2=|C|^2>0\). Then \(P(z)=r_0+r_1z+r_2z^2\) has positive real coefficients. In particular \(P(1)>0\). Any real root on the unit circle is therefore \(-1\), which belongs to \(\mu_N\) exactly when \(N\) is even. The condition \(P(-1)=0\) is exactly \(r_1=r_0+r_2\). It supplies one distinct sampled root even if the root has algebraic multiplicity two.

If a sampled unit-circle root is nonreal, the real coefficients force its conjugate to be the other root. Their product is one, so Vieta's formula gives \(r_0=r_2\). Writing the roots as \(\exp(\pm2\pi ij/N)\), with \(0<j<N/2\), the root sum gives \(r_1/r_0=-2\cos(2\pi j/N)>0\), equivalently \(N/4<j<N/2\). Conversely these conditions factor \(P\) with the indicated two sampled nonreal roots. This exhausts every possibility, and the two-root and one-root cases are disjoint.

For attainability, choose an integer \(j\) with \(N/4<j<N/2\), which exists for every \(N\ge5\), and set \(r=-2\cos(2\pi j/N)>0\). On the three consecutive sites take the coefficient triples
\[
(1,1,2),\quad(1,i\sqrt3,1),\quad(1,i\sqrt r,1).
\]
Their support sizes are respectively \(5N\), \(5N-2\), and \(5N-4\). If \(N\) is even, also use
\[
(1,\sqrt5,2),\quad(1,i\sqrt2,1),
\]
which produce \(5N-1\) and \(5N-3\), respectively. Indeed the first even-order extra example has \(e=0,h=1\), while the second has \(e=1,h=1\). The exact law proves both the listed spectra and the necessary and sufficient conditions for attaining the minimum. No computational assumption enters the argument.

## Verification
The accompanying standalone `verify.py` directly computes each sampled transform for all orders \(5\le N\le18\), evaluates independently the coefficient criteria, checks every predicted support value and a primitive-step change of variables, and tests 30 additional random complex triples at each order. It completed 560 direct comparisons (`VERIFY_OK`). Floating-point tests are finite corroboration, **not** the proof of the universal result, which is the five-row analysis above.

## Relationship to prior work
Fabio Nicola, *The uncertainty principle for the short-time Fourier transform on finite cyclic groups: cases of equality* (arXiv:2204.14176, first posted 29 April 2022), proves the general bound \(|\operatorname{supp}V_gf|\ge N\) and classifies its global equality cases. Neither statement determines the high-support spectrum under an exactly three-tap self-window constraint.

Krahmer, Pfander and Rashkov, *Uncertainty in time-frequency representations on finite Abelian groups and applications* (arXiv:math/0611493, first posted 16 November 2006), Proposition 4.4, already gives the lower bound \(5p-4\) for two support-three functions on \(\mathbb Z_p\), with \(p\ge5\) prime. Thus the **prime-order numerical lower bound alone is not asserted as new here**. That theorem does not distinguish self-ambiguity from arbitrary cross-STFT pairs, classify the coefficient-dependent zero patterns, exclude \(5p-1\) and \(5p-3\) for odd \(p\), or treat all composite cyclic orders. Its Figure 6 also tabulates broad support-triple feasibility at order five, not this self-window classification.

The published two-sparse prime-cyclic STFT support trichotomy concerns two-point windows and signals, not the present three-point self-transform. Fourier support laws for a single three-sparse vector likewise do not determine the five coupled delay rows here.

## Limitations
The result does not classify non-arithmetic three-point supports, non-unit-step progressions, or distinct signals and windows. Its exact lower bound for prime cyclic orders overlaps the earlier general theorem cited above; the added claims are the complete support-size spectrum, parity restrictions, all equality cases, and uniform composite-order extension for the specified natural support class. A search across the indexed literature and public result records cannot exclude an equivalent unindexed ambiguity-function computation. Numerical tests do not independently certify infinite-order statements.

## References
1. F. Nicola, "The uncertainty principle for the short-time Fourier transform on finite cyclic groups: cases of equality," arXiv:2204.14176v1, 29 April 2022; *Journal of Functional Analysis* 284 (2023), 109924. https://arxiv.org/abs/2204.14176
2. F. Krahmer, G. E. Pfander and P. Rashkov, "Uncertainty in time-frequency representations on finite Abelian groups and applications," arXiv:math/0611493v1, 16 November 2006; *Applied and Computational Harmonic Analysis* 25 (2008), 209–225. https://arxiv.org/abs/math/0611493
3. "Exact support trichotomy for two-sparse prime cyclic STFTs," public result, identifier `2026/10/4/SCOPE-exact-support-trichotomy-for-two-sparse-prime-cyclic-stfts--5b84852d543c`. https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-support-trichotomy-for-two-sparse-prime-cyclic-stfts--5b84852d543c
