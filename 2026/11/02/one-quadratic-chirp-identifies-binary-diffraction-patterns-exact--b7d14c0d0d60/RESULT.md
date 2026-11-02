# One quadratic chirp identifies binary diffraction patterns exactly at prime lengths

## Finding

Let \(N\ge3\) be an integer, \(a,b\in\mathbb Z\), and \(\zeta_N=e^{2\pi i/N}\). For \(f:\mathbb Z_N\to\{0,1\}\), define one chirp-coded Fourier intensity vector by
\[
I_{N,a,b}(f;k)=\left|\sum_{j\in\mathbb Z_N}f(j)\zeta_N^{aj^2+bj+kj}\right|^2,
\qquad k\in\mathbb Z_N.
\]
All Fourier frequencies are labelled, not rearranged; no unmasked measurement is provided.

**Exact prime/composite criterion.** The mapping \(f\mapsto (I_{N,a,b}(f;k))_{k\in\mathbb Z_N}\) is injective on binary vectors of Hamming weight at least two if and only if \(N\) is prime and \(a\not\equiv0\pmod N\). In that case its complete collision structure on all binary vectors is as follows: the \(N\) distinct singletons have the same constant intensity vector, and every other vector (including the zero vector) has a unique intensity vector. Thus there are exactly \(2^N-N+1\) different intensity vectors. This is the maximum possible for any single diagonal **unit-modulus** mask followed by a full \(N\)-point Fourier intensity measurement, since all singleton inputs are indistinguishable under every such mask.

**Quantitative separation.** For prime \(p\ge3\) and \(a\not\equiv0\pmod p\), if distinct binary vectors \(f,g\) are not two singleton vectors, then
\[
\max_{k\in\mathbb Z_p}|I_{p,a,b}(f;k)-I_{p,a,b}(g;k)|\ \ge\ p^{-(p-2)}.
\]
The stated explicit separation bound is not asserted to be optimal.

## Assumptions and scope

The signal alphabet is exactly \(\{0,1\}\), the chirp mask has phase \(\zeta_N^{aj^2+bj}\), and the measurement uses the full, labelled discrete Fourier power spectrum. The result addresses exact noiseless identification as well as one conservative separation bound; no claim is made about arbitrary complex signals, arbitrary sub-sampled Fourier data, or computational efficiency under noise. The two-point composite witnesses use ordinary binary indicators without phase freedom.

## Proof

**1. Autocorrelation of the coded signal.** Write \(z_j=f(j)\zeta_N^{aj^2+bj}\) and \(\mathcal Fz(k)=\sum_jz_j\zeta_N^{kj}\). Fourier inversion of the power spectrum gives
\[
C_f(h)=\frac1N\sum_{k\in\mathbb Z_N} I_{N,a,b}(f;k)\zeta_N^{-kh}
=\zeta_N^{-ah^2+bh}\sum_{j\in\mathbb Z_N} f(j)f(j-h)\zeta_N^{2ahj}.
\]
In particular \(C_f(0)=|\operatorname{supp}f|\), so equal intensities imply equal Hamming weights. The identity uses the exact Fourier normalization above.

**2. Prime cyclotomic rigidity.** Suppose \(N=p\ge3\) is prime and \(p\nmid a\). If \(I_{p,a,b}(f;\cdot)=I_{p,a,b}(g;\cdot)\), then for each nonzero \(h\in\mathbb Z_p\),
\[
\sum_{j\in\mathbb Z_p} d_{j,h}\zeta_p^{2ahj}=0,
\qquad d_{j,h}=f(j)f(j-h)-g(j)g(j-h)\in\{-1,0,1\}.
\]
Since \(2ah\) is invertible modulo the odd prime \(p\), the coefficients are permuted into a polynomial of degree at most \(p-1\) vanishing at \(\zeta_p\). The irreducible minimal polynomial is \(\Phi_p(X)=1+X+\cdots+X^{p-1}\). Therefore every \(d_{j,h}\) has a common integer value \(c_h\in\{-1,0,1\}\). If \(c_h=1\), then \(f(j)f(j-h)=1\) for all \(j\), so \(f\) has weight \(p\), whereas \(g(j)g(j-h)=0\) for all \(j\), contradicting its equal weight \(p\). The case \(c_h=-1\) is symmetric. Hence \(c_h=0\) for every nonzero \(h\).

Thus every ordered pair of distinct active sites of \(f\) is also an ordered pair of distinct active sites of \(g\), and conversely. When the common support contains at least two sites, each active site is an endpoint of such a pair and the supports coincide. At weight zero the unique signal is zero, and at weight one every coordinate singleton gives \(I\equiv1\). There are no other collisions. The total count \(2^p-p+1\) follows by merging exactly the \(p\) singleton inputs into one class. No single unit-modulus mask can distinguish singletons because each masked singleton has a Fourier transform of constant modulus one.

**3. Composite-length two-point obstructions.** For two distinct indices \(u,u+d\), direct expansion gives
\[
I_{N,a,b}(\mathbf 1_{\{u,u+d\}};k)
=2+2\operatorname{Re}\zeta_N^{a(2ud+d^2)+bd+kd}.
\]
This intensity vector is unchanged when \(u\) is replaced by \(u+s\) whenever \(N\mid2ads\). If composite \(N\) is even, take \(d=N/2\) and \(s=1\); the supports \(\{0,N/2\}\) and \(\{1,1+N/2\}\) are distinct for \(N\ge4\) and produce identical intensities for every \(a,b\). If composite \(N\) is odd, choose any proper divisor \(d\) with \(1<d<N\) and put \(s=N/d\). Again \(N\mid2ads\). The supports \(\{0,d\}\) and \(\{s,s+d\}\) are distinct: equality would force \(2d\equiv0\pmod N\), impossible for odd \(N\). Thus no composite \(N\) qualifies. Finally, if \(N=p\ge3\) is prime and \(p\mid a\), the mask is a linear phase. Cyclically translating \(\{0,1\}\) to \(\{1,2\}\) leaves its Fourier intensities unchanged, proving noninjectivity.

**4. Quantitative separation.** Consider two distinct prime-length binary vectors outside the pair-of-singletons exception. If their weights differ, then \(|C_f(0)-C_g(0)|\ge1\), which implies the asserted stronger intensity separation \(\|I_f-I_g\|_\infty\ge1\). If the weights agree, Step 2 shows that some nonzero \(h\) has \(d_{j,h}\) not identically zero and not constant. Consequently
\[
\alpha=\sum_j d_{j,h}\zeta_p^{2ahj}\ne0
\]
is an algebraic integer. Its field norm from \(\mathbb Q(\zeta_p)\) to \(\mathbb Q\) is a nonzero integer, while every one of its other \(p-2\) Galois conjugates has absolute value at most \(p\). Therefore \(|\alpha|\ge p^{-(p-2)}\). The prefactor \(\zeta_p^{-ah^2+bh}\) has modulus one, so \(|C_f(h)-C_g(h)|=|\alpha|\). The inverse power-spectrum formula in Step 1 gives \(|C_f(h)-C_g(h)|\le\|I_f-I_g\|_\infty\). This completes the proof.

## Verification

Run `python3 check_chirp.py` with Python 3 and no third-party dependencies. The checker enumerates every binary signal at prime lengths \(3,5,7,11\) for the explicitly listed nonzero chirp slopes; it computes the power-spectrum autocorrelation keys **exactly** in the cyclotomic integer basis, not using floating-point rank tests. It finds precisely the singleton-collision family and independently verifies exact two-point composite witnesses at lengths \(4,6,8,9,10,15,21,25\), including nonzero linear chirp terms. These finite tests check definitions and boundary examples; Steps 1–4, not the finite enumeration, prove the unbounded-in-length theorem and separation estimate.

## Relationship to prior work

Bendory–Edidin–Gonzalez (arXiv:2301.10647v1, January 25, 2023) reduce *unmasked* finite-alphabet Fourier phase retrieval to homometric partitions under generic alphabet conditions; their full text discusses the difficult unmasked binary case. Here a **single fixed deterministic quadratic unit-modulus mask** breaks every non-singleton binary homometry in prime cyclic length, but provably cannot do so at composite length. The mechanism is the prime cyclotomic minimal polynomial rather than generic alphabet assumptions. Jaming–Rathmair (arXiv:2205.08753) construct three masks for unrestricted continuous phase retrieval and study different discretizations; that does not imply this one-mask binary theorem. The established literature on random coded diffraction masks and sparse binary Fourier phase retrieval also does not directly provide this exact arithmetic prime/composite criterion. This is a comparison of mathematical statements, not a claim that an unsuccessful search proves priority.

## Limitations

The exact signal model is binary; the proof does not extend automatically to arbitrary finite complex alphabets. Full labelled spectra are necessary for the displayed inversion argument, and unrestricted noisy optimization is not analyzed. The stability constant is intentionally conservative and not sharp. The special length \(N=2\) is excluded from the classification because the weight-at-least-two signal class then contains only one vector. Historical priority is provisional; a broader unpublished or differently indexed deterministic-mask theorem may imply the result indirectly. No independent mathematical validation has been performed.

## References

1. T. Bendory, D. Edidin, and I. Gonzalez, *Finite Alphabet Phase Retrieval*, arXiv:2301.10647v1, publicly posted 2023-01-25; full preprint https://arxiv.org/html/2301.10647v2.
2. P. Jaming and M. Rathmair, *Uniqueness of phase retrieval from three measurements*, arXiv:2205.08753v1, publicly posted 2022-05-18; full preprint https://arxiv.org/html/2205.08753v1.
3. *Phase retrieval for sparse binary signal: uniqueness and algorithm*, 2017, DOI:10.1080/17415977.2017.1336551; https://www.tandfonline.com/doi/full/10.1080/17415977.2017.1336551.
4. P. Chen and A. Fannjiang, *Fourier phase retrieval with a single mask by Douglas–Rachford algorithms*, Applied and Computational Harmonic Analysis, DOI:10.1016/j.acha.2016.07.003; https://pmc.ncbi.nlm.nih.gov/articles/PMC5869012/.
