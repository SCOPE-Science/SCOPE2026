# Parity-split spectral multiplicities and sharp norm envelope for annular Hardy selfcommutators

## Finding
Fix \(0<q<1\) and \(\beta>0\). On the boundary-weighted analytic Hardy space of the annulus, consider the multiplier \(M f(z)=zf(z)\) and its positive selfcommutator \(C=M^*M-MM^*\). Put \(Q=q^2\). The entire spectrum is
\[
\sigma(C)=\{0\}\cup\{\lambda_n:n\in\mathbb Z\},\qquad
\lambda_n=\frac{(1-Q)^2\beta Q^{n-1}}{(1+\beta Q^{n-1})(1+\beta Q^n)}.
\]
Every \(\lambda_n\) is positive, zero is not an eigenvalue, and \(C\) belongs to every Schatten class \(\mathcal S_p\) with \(p>0\). Its trace is \(\operatorname{Tr}C=1-q^2\), independent of \(\beta\).

There is an exact multiplicity trichotomy. If \(\beta\notin\{q^k:k\in\mathbb Z\}\), all positive eigenvalues are simple. If \(\beta=q^{2j}\), all positive eigenvalues have multiplicity two. If \(\beta=q^{2j+1}\), precisely the largest positive eigenvalue is simple (carried by \(n=-j\)); all others have multiplicity two. No eigenvalue has multiplicity exceeding two.

The operator norm is log-periodic in the boundary-mass ratio, and its **sharp global range** is
\[
\boxed{\frac{(1-q^2)^2}{2(1+q^2)}\le\|C\|\le(1-q)^2.}
\]
The lower equality occurs exactly for \(\beta=q^{2j}\), and the upper exactly for \(\beta=q^{2j+1}\), where \(j\in\mathbb Z\). Within every multiplicative interval from \(\beta=q^{2j}\) to \(\beta=q^{2j+2}\), the norm increases strictly to its unique maximum at \(\beta=q^{2j+1}\) and then decreases strictly. Replacing \(\beta\) by \(q^2\beta\) preserves the entire spectrum with multiplicities.

**Bridge to weighted Szegő-kernel zeros.** Gafai–Murid–Wahid (arXiv:2202.09114, Theorem 3) proved that the weighted Szegő kernel of this same annulus and mass family has a zero precisely at \(\beta=q^{2j+1}\), \(j\in\mathbb Z\). Combining their *known* kernel-zero theorem with the new selfcommutator classification yields a sharp joint trichotomy: a kernel zero occurs precisely at the maximum selfcommutator norm and its unique unpaired top eigenvalue; the all-double spectral cases are exactly the norm minima and are kernel-zero-free; every remaining mass is kernel-zero-free with completely simple commutator point spectrum. The Szegő-kernel zero criterion itself is prior work, not a new assertion of priority.

## Assumptions and scope
The annulus is \(\mathbb A_q=\{z\in\mathbb C:q<|z|<1\}\). Define the Hilbert space \(H^2_\beta(\mathbb A_q)\) of analytic Laurent series \(f(z)=\sum_{n\in\mathbb Z}a_n z^n\) with
\[
\|f\|_\beta^2=\sum_{n\in\mathbb Z}|a_n|^2(1+\beta q^{2n}).
\]
This is the sum of normalized angular \(L^2\)-masses on the outer circle and \(\beta\) times that on the inner circle; \(\beta\) is arbitrary positive. The spectral claims use the convention \(C=M^*M-MM^*\) (the opposite commutator has opposite sign). All integer indices range over the *bilateral* Laurent basis; neither a disk Hardy shift nor a truncation is being used.

## Proof
**Step 1 (normalized shift and diagonal commutator).** The functions
\[e_n(z)=\frac{z^n}{\sqrt{1+\beta Q^n}},\qquad n\in\mathbb Z,\]
form an orthonormal basis. Therefore \(Me_n=w_ne_{n+1}\) with
\[
w_n^2=\frac{1+\beta Q^{n+1}}{1+\beta Q^n}
=Q+\frac{1-Q}{1+\beta Q^n}.
\]
Thus \(Ce_n=(w_n^2-w_{n-1}^2)e_n=\lambda_ne_n\) with the displayed formula. The eigenvalues are positive and tend geometrically to zero at both ends of the bilateral index. Hence \(C\) is compact, injective, and lies in every \(\mathcal S_p\) for \(p>0\); its spectrum is exactly the closure of its diagonal entries. The telescoping trace is
\[
\sum_{n=-N}^N\lambda_n=w_N^2-w_{-N-1}^2\longrightarrow1-Q.
\]
In particular, positivity and trace-class membership are established without relying on any finite truncation.

**Step 2 (all collisions).** Define
\[
F_Q(t)=\frac{(1-Q)^2t}{(1+t)(1+Qt)},\quad t>0,
\qquad \lambda_n=F_Q(\beta Q^{n-1}).
\]
For positive \(t,s\), clearing the positive denominators gives
\[
F_Q(t)=F_Q(s)\quad\Longleftrightarrow\quad
(t-s)(1-Qts)=0.
\]
For distinct integers \(n,m\) the equality therefore holds if and only if
\[
\beta^2 Q^{n+m-1}=1
\quad\Longleftrightarrow\quad
\beta=q^{1-n-m}.
\]
If \(\beta=q^k\), every index \(n\) is paired uniquely with \(m=1-k-n\). For even \(k=2j\), the index sum is odd, so no index is fixed and each value has exactly two representatives. For odd \(k=2j+1\), the only fixed point is \(n=-j\); it is the peak since its argument equals \(q^{-1}\). In the absence of these integral powers, no collisions occur. Because the equation for \(s\) has only the two solutions \(s=t\) and \(s=1/(Qt)\), no positive eigenvalue can have multiplicity above two.

**Step 3 (sharp norm envelope).** Differentiating gives
\[
F'_Q(t)=\frac{(1-Q)^2(1-Qt^2)}{(1+t)^2(1+Qt)^2}.
\]
Thus \(F_Q\) rises strictly to its unique continuous maximum at \(t=q^{-1}\) and falls strictly thereafter. In particular \(F_Q(q^{-1})=(1-q)^2\).

The bilateral index shift identifies the spectra for \(\beta\) and \(\beta Q\), so it suffices to let \(q^2\le\beta\le1\). Here \(t_0=\beta Q^{-1}\in[1,Q^{-1}]\). For all other indices, the lattice arguments are \(t_n=Q^nt_0\). The collision identity and the unimodality show \(F_Q(t_0)\ge F_Q(Qt_0)\) because \(t_0\le Q^{-1}\), and \(F_Q(t_0)\ge F_Q(Q^{-1}t_0)\) because \(t_0\ge1\); strict monotonicity of the tails then yields
\[
\|C\|=F_Q(\beta Q^{-1})\quad (q^2\le\beta\le1).
\]
The argument \(\beta Q^{-1}\) moves through \([1,q^{-2}]\) and crosses the unique maximizer \(q^{-1}\) at \(\beta=q\). Both endpoint values equal
\[
F_Q(1)=F_Q(Q^{-1})=\frac{(1-Q)^2}{2(1+Q)}.
\]
The strict one-peaked law, exact global range, and equality cases follow. Translating by powers of \(Q\) recovers every positive \(\beta\). These steps exhaust the spectrum, multiplicities, and norm for all allowed parameters.

**Step 4 (the known kernel-zero criterion).** The weighted reproducing kernel here is a harmless scalar multiple of the weighted Szegő kernel in Gafai–Murid–Wahid, Theorem 3, with their annulus radius and weight parameter equal to \(q\) and \(\beta\). That established theorem gives a kernel zero exactly at odd integer powers \(\beta=q^{2j+1}\). Combining it with Steps 2–3 proves the asserted cross-invariant coincidence. No novel proof or priority is asserted for the Szegő-kernel zero classification.

## Verification
The standalone supplementary script `check_annulus.py` uses exact rational arithmetic for four rational annulus radii, eleven consecutive integral-power mass ratios per radius, a finite bilateral spectral window, generic mass ratios, and tail traces. It verifies 67,264 exact comparisons and tail checks and prints `PASS`; the mathematical proof above, rather than the finite script, establishes the unlimited statements.

## Relationship to prior work
Gafai, Murid and Wahid (arXiv:2202.09114, first public 18 February 2022) establish a weighted annular Szegő-kernel product and the odd-power zero criterion in their Theorem 3. Their theorem is credited as an independent known ingredient in the joint zero/commutator corollary, and does not by itself compute the new commutator spectrum. Katori and Shirai (arXiv:2008.04177, first posted 10 August 2020), building on McCullough and Shen, study the same boundary-weighted annular Szegő spaces, their Laurent reproducing kernels, and Gaussian zero processes. In particular the monomial norm \(1+\beta q^{2n}\) is already known and is **not** asserted to be new. Douglas and Kim (arXiv:0902.1794) study powers of annular Hardy/Bergman bilateral multiplication shifts and classify reducing subspaces, not the present commutator eigenvalue collisions or sharp boundary-mass norm profile. Tattersall's 2015 thesis develops annular Toeplitz/Hankel spectral theory, primarily for real symbols; the compared sections and searchable text did not identify this selfcommutator classification. The result is a targeted quantitative spectral analysis built from known function-space and shift inputs, rather than a new construction of the annular Hardy space.

## Limitations
The result applies to a round annulus with constant positive weights on each boundary circle and the coordinate multiplier \(z\). It does not establish stability under nonconstant boundary weights, perturbed boundaries, or other multipliers. As the diagonal formula follows from established annular monomial norms, historical priority for the consolidated spectral/multiplicity and norm classification remains provisional; other treatments of weighted shifts or Toeplitz commutators may contain equivalent consequences. Finite computations cannot exclude such prior coverage and do not independently prove the theorem. No independent mathematical audit has been performed.

## References
1. N. S. Gafai, A. H. M. Murid and N. H. A. A. Wahid, *Infinite Product Representation for the Szegö Kernel for an Annulus*, arXiv:2202.09114, first posted 18 February 2022, https://arxiv.org/abs/2202.09114 (Section 5, Theorem 3).
2. M. Katori and T. Shirai, *Zeros of the i.i.d. Gaussian Laurent series on an annulus: weighted Szegő kernels and permanental-determinantal point processes*, first public arXiv version 10 August 2020, https://arxiv.org/abs/2008.04177 (especially Section 1.1 and equation (1.4)).
3. R. G. Douglas and Y.-S. Kim, *Reducing Subspaces on the Annulus*, arXiv:0902.1794, 11 February 2009, https://arxiv.org/abs/0902.1794 (Sections 3–4).
4. J. M. Tattersall, *Toeplitz and Hankel operators on Hardy spaces of complex domains*, University of Leeds thesis, 2015, https://etheses.whiterose.ac.uk/id/eprint/11498/ (abstract, introduction and Chapter 3 excerpts checked).
5. M. B. McCullough and L.-C. Shen, *On the Szegő kernel of an annulus*, Proceedings of the American Mathematical Society **121** (1994), DOI: 10.1090/S0002-9939-1994-1189748-9 (background source credited through Katori–Shirai).
