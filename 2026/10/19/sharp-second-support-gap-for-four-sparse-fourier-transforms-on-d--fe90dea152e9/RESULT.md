# Sharp second-support gap for four-sparse Fourier transforms on dyadic cycles

## Finding
For every integer \(m\ge3\), put \(N=2^m\) and \(G=\mathbb Z/N\mathbb Z\). Let \(f:G\to\mathbb C\) have **exactly four** nonzero values, without any restriction on their phases or magnitudes. With the unnormalized discrete Fourier transform
\[
\widehat f(k)=\sum_{x\in G}f(x)e^{-2\pi i kx/N},
\]
there is a sharp gap:
\[
\boxed{\ |\operatorname{supp}\widehat f|=\frac N4\quad\text{or}\quad
|\operatorname{supp}\widehat f|\ge\frac{3N}{8}.\ }
\]
The first alternative holds exactly when the spatial support is a coset of the unique order-four subgroup \(H=\{0,N/4,N/2,3N/4\}\) and \(f\) is a nonzero scalar multiple of a character restricted to that coset. Both endpoints are attained for every \(m\ge3\). In particular, **among all nonextremal four-sparse complex signals, the optimal Fourier-support cardinality is exactly \(3N/8\)**; no value lies strictly between \(N/4\) and \(3N/8\).

One sharp nonextremal signal has polynomial
\[
P(z)=(1+z^{N/2})(1+z^{N/8});
\]
its four exponents are distinct modulo \(N\). The first factor vanishes at odd frequency indices, and the second at frequency indices congruent to \(4\pmod8\). These disjoint zero sets have respectively \(N/2\) and \(N/8\) elements, leaving exactly \(3N/8\) nonzero Fourier coefficients.

## Assumptions and scope
The ambient group is the cyclic two-power group \(\mathbb Z_{2^m}\) with \(m\ge3\). Fourier-support sizes count nonzero **complex** transform entries exactly; we make no small-noise or numerical threshold claim. Every point in the spatial support has a nonzero complex coefficient. The result does not apply unchanged to noncyclic two-groups or cyclic orders with odd factors. We use the elementary multiplicative uncertainty inequality, with an equality proof below, only in its four-point form.

## Proof
**Lemma 1 (two or three spatial atoms).** For a two-sparse or three-sparse nonzero function on \(\mathbb Z_{2^h}\), its Fourier transform is nonzero at least \(2^{h-1}\) frequencies, whenever such exact spatial support exists.

For two terms, after factoring out a monomial, the Fourier polynomial is \(a+bz^d\) with \(d\not\equiv0\pmod{2^h}\). It can vanish on at most \(\gcd(d,2^h)\le2^{h-1}\) of the \(2^h\)-th roots; this follows by solving a single power equation on the cyclic root group. For three terms, factor out a common monomial and repeatedly divide all three exponent differences by two as long as they are even. This reduces to a smaller cyclic two-power group, and the Fourier values for the original group repeat equally many times. In the reduced polynomial there are both odd and even exponent classes, and since there are three terms, one parity class consists of exactly one nonzero monomial. If both \(P(z)\) and \(P(-z)\) vanished, the even and odd parts would vanish separately; the singleton parity part cannot vanish at a root of unity. Thus at most one member of each antipodal pair \(\{z,-z\}\) is a root. Lifting back proves the bound.

**Lemma 2 (four-point equality).** For any finite cyclic group of size \(N\), a nonzero four-sparse \(f\) satisfies \(|\operatorname{supp}\widehat f|\ge N/4\). Equality forces the support to be a coset of a subgroup of order four, and the values of \(f\) there to be proportional to a character.

Indeed, with \(A=\operatorname{supp}f\) and \(B=\operatorname{supp}\widehat f\), Cauchy--Schwarz and Parseval give
\[
N\|f\|_2^2=\sum_{k\in B}|\widehat f(k)|^2
\le |B|\bigl(\sum_{x\in A}|f(x)|\bigr)^2
\le 4|B|\|f\|_2^2.
\]
At equality, all four \(|f(x)|\) are equal and, for every \(k\in B\), the four summands \(f(x)e^{-2\pi ikx/N}\) have a common argument. Comparing two frequencies in \(B\) shows that the annihilator of \(\langle A-A\rangle\) contains the entire difference set \(B-B\). As \(B\) has size \(N/4\) and \(\langle A-A\rangle\) has at least four elements, it follows that this subgroup has exactly four elements, \(A\) is one of its cosets, and coefficient phases match a character there. Conversely such a restricted character has a Fourier transform supported on one annihilator coset of size \(N/4\).

We prove the gap by induction on \(m\). At \(N=4\), every four-point support is the whole group; the inequality \(|\operatorname{supp}\widehat f|\ge1\) and the equality characterization suffice to start the induction (the expression \(3N/8\) is only required for \(N\ge8\)). Fix \(N=2^m\ge8\), write \(M=N/2\), and compare the points in \(\mathbb Z_N\) lying above the same residue \(r\in\mathbb Z_M\). Define
\[
F_0(r)=f(r)+f(r+M),\qquad
F_1(r)=e^{-2\pi ir/N}\bigl(f(r)-f(r+M)\bigr).
\]
The even-index Fourier values of \(f\) are the complete \(M\)-point Fourier transform of \(F_0\); the odd-index values are the complete \(M\)-point transform of \(F_1\), up to a harmless choice of Fourier-sign convention. Hence
\[
|\operatorname{supp}\widehat f|
=|\operatorname{supp}\widehat{F_0}|+|\operatorname{supp}\widehat{F_1}|.
\tag{1}
\]

**Case A: at least one antipodal spatial pair.** Call \(\{x,x+M\}\) an antipodal pair. If there is exactly one such pair, the two functions \(F_0,F_1\) have two or three nonzero values apiece (the other two distinct projected sites cannot cancel). Lemma 1 and (1) give at least \(M\) frequencies, more than \(3N/8\). If there are two antipodal pairs, each \(F_j\) has at most two nonzero entries. When both are nonzero, each has at least \(M/2\) Fourier-support entries (a one-point function has all \(M\)), and their total is at least \(M\). When one is identically zero, the other is exactly two-sparse on \(\mathbb Z_M\); write the projected support separation as \(d\not\equiv0\pmod M\). The Fourier transform of that two-term function can vanish at no more than \(\gcd(d,M)\) frequencies. If \(d\equiv M/2\pmod M\), the original four-point spatial support is a coset of the order-four subgroup; the remaining two-term quotient transform has either exactly \(M/2=N/4\) or exactly \(M=N/2\) nonzero frequencies, according as its two coefficient magnitudes agree or not. Lemma 2 identifies the former equality case as a restricted character. Otherwise \(\gcd(d,M)\le M/4\), so
\[
|\operatorname{supp}\widehat f|\ge M-M/4=3N/8.
\]

**Case B: no antipodal spatial pair.** The four spatial atoms project to four distinct residues in \(\mathbb Z_M\), and both \(F_0,F_1\) are exactly four-sparse with the same projected support \(A'\). If \(A'\) is not an order-four subgroup coset, the inductive gap gives each a Fourier support of size at least \(3M/8\) (when \(M=4\), this subcase is impossible), proving the desired bound after adding them.

If instead \(A'\) is a coset of the order-four subgroup of \(\mathbb Z_M\), each \(\widehat{F_j}\) has support cardinality a **positive integer multiple of \(M/4=N/8\)**: the transforms are periodic in nonvanishing status modulo four because the spatial coset has spacing \(M/4\). Lemma 2 says each cardinality is at least \(M/4\). Thus a combined support size strictly below \(3N/8=3M/4\) would force both supports to be exactly \(M/4\). By Lemma 2, \(F_0\) and \(F_1\) would then each be scalar characters on that same projected order-four coset.

Write its elements \(r_j=r_0+jM/4\) and let \(x_j=r_j+\varepsilon_jM\), where \(\varepsilon_j\in\{0,1\}\), be the four actual spatial positions. Since there are no antipodal pairs, each projected residue has one actual coefficient, so
\[
\frac{F_1(r_j)}{F_0(r_j)}=e^{-2\pi i x_j/N}.
\]
For two restricted characters their ratio, relative to its value at \(r_0\), must be a fourth root of unity at \(r_1\). But for this ratio,
\[
\left(\frac{F_1(r_1)/F_0(r_1)}{F_1(r_0)/F_0(r_0)}\right)^4
=e^{-2\pi i\,4(x_1-x_0)/N}=-1,
\]
because \(x_1-x_0\equiv M/4=N/8\pmod M\). This contradiction excludes the sub-threshold possibility. Hence the gap holds also in Case B.

Lemma 2 identifies every equality case at \(N/4\); the displayed four-term product supplies the upper witness \(3N/8\), completing the proof for all \(m\ge3\).

## Verification
Run `python verify.py` with NumPy installed. The checker tests every four-point spatial support on \(\mathbb Z_8\) and every four-tuple of coefficients in \(\{1,-1,i,-i\}^4\), as well as deterministic pseudorandom nonzero coefficient/support samples for sizes \(16,32,64,128\). It additionally checks the exact sharpness constructions for \(N=8,16,32,64,128,256\). A successful execution prints `VERIFY_OK 22732 finite sampled comparisons`.

This finite floating-point check is **not** an exhaustive test over all complex coefficients or all group orders; the infinite theorem depends on Lemmas 1 and 2 and the full induction above.

## Relationship to prior work
The classical multiplicative uncertainty principle, and its equality classification, give the \(N/4\) minimum but not the sharp next possible Fourier-support size. The 2010 work of Bonami and Ghobber treats equality families for certain groups, including cyclic prime-square groups, not this infinite family of cyclic two-power groups with arbitrary complex coefficients and a sharp second-support gap. The 2008 work of Krahmer, Pfander, and Rashkov gives broader time-frequency support principles and finite rank criteria, not the displayed gap.

Two closely relevant published mathematical notes cover different objects: *Dyadic shell classification of Fourier zeros for four-point indicators* treats **only coefficient-one indicators** and gives the full shell decomposition in that restriction; *Four-sparse Walsh spectra are controlled by affine dimension* treats elementary abelian \(2\)-groups rather than cyclic \(2\)-power groups. The indicator theorem already yields the same numerical gap for its coefficient-one subclass; the new assertion is that **no arbitrary complex four-spike coefficients can enter the intervening gap**, across every dyadic cyclic order. Neither comparison establishes that unrestricted assertion. *Exact three-point Fourier uncertainty on every cyclic group* provides a prior general three-atom minimum; a self-contained dyadic proof of the needed subsidiary lemma is included above.

A recent motivating paper, Iosevich, Li, and Yu (first submitted September 21, 2026), studies finite-scale spectral synthesis and Fourier concentration on cyclic product groups in a Fourier-ratio framework. Its accessible abstract does not state the exact four-spike dyadic next-support problem. The present result addresses sharp **support cardinality**, not those asymptotic synthesis or random-sampling estimates.

## Limitations
The claim does not characterize every coefficient tuple attaining the second value \(3N/8\), nor does it give a robust lower bound when coefficients are merely close to zero. It does not claim an arbitrary-prime-power extension. Full text of the recent motivating preprint and some older comparisons was unavailable; the comparisons that rely on their abstracts alone do not exclude historical priority. No independent audit has been performed.

## References
1. A. Iosevich, Z. Li, and K. Yu, *Spectral synthesis with the complexity parameter in \(\mathbb Z_N^d\)*, arXiv:2609.25404, first submitted 2026-09-21.
2. A. Bonami and S. Ghobber, *Equality cases for the uncertainty principle in finite Abelian groups*, arXiv:1003.5060 (first submitted 2010-03-26), Acta Sci. Math. 79 (2013), 507--528.
3. F. Krahmer, G. Pfander, and P. Rashkov, *Uncertainty in time-frequency representations on finite Abelian groups and applications*, arXiv:math/0611493 (first submitted 2006-11-16), Applied and Computational Harmonic Analysis 25 (2008), 209--225.
4. Published mathematical note, *Dyadic shell classification of Fourier zeros for four-point indicators* (2026), full public mathematical statement inspected.
5. Published mathematical note, *Four-sparse Walsh spectra are controlled by affine dimension on \((\mathbb Z/2\mathbb Z)^d\)* (2026), full public mathematical statement inspected.
6. Published mathematical note, *Exact three-point Fourier uncertainty on every cyclic group* (2026), full public mathematical statement inspected.
