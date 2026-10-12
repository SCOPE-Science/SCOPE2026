# Dilute-saturation XX-chain concurrence and a strict long-range onset discrepancy

## Finding

For the translation-invariant, infinite spin-\(1/2\) XX chain at zero temperature with positive exchange coupling \(J\), define the Hamiltonian formally by
\[
H=J\sum_{j\in\mathbb Z}(S^x_jS^x_{j+1}+S^y_jS^y_{j+1})-h\sum_{j\in\mathbb Z}S^z_j.
\]
Its saturation field is \(h_c=J\). For \(0<h<J\), write the density of minority spins as \(\nu=\arccos(h/J)/\pi\). For each positive integer separation \(r\), let \(C_r(h)\) be the Wootters concurrence of sites \(0\) and \(r\).

Set \(K(x,y)=\operatorname{sinc}(\pi(x-y))=\sin(\pi(x-y))/(\pi(x-y))\), with diagonal value one. For each \(s>0\), define the **first Fredholm minor**
\[
F(s)=\sum_{m=0}^{\infty}\frac{(-2)^m}{m!}\int_{[0,s]^m}
\det\left[K(x_a,y_b)\right]_{a,b=0}^{m}\,du_1\cdots du_m,
\quad x=(0,u_1,\dots,u_m),\ y=(s,u_1,\dots,u_m).
\]
For \(m=0\), the term is \(\sin(\pi s)/(\pi s)\). The series converges absolutely for every finite \(s\). The following formula holds for **every** sequence of positive densities tending to zero and integer separations tending to infinity such that \(\nu r\to s>0\):
\[
\boxed{\lim\frac{C_r(h)}{2\nu}
=\max\left\{0,\ |F(s)|-\sqrt{1-\operatorname{sinc}^{2}(\pi s)}\right\}.}
\]

The same limit at \(s_0=\sqrt2/\pi\) is strictly positive. Therefore, define the **proposed** long-range onset-field fraction from Fumani–Nemati–Mahdavifar–Darooneh by
\[
 h_r^{\mathrm{prop}}/J=\frac{(r-1)^2}{(r-1)^2+1}.
\]
For all sufficiently large integer \(r\), \(C_r(h_r^{\mathrm{prop}})>0\). By continuity in \(h\) below saturation, the pair remains entangled at some strictly lower field. Hence that empirical all-distance proposed fraction cannot equal the actual onset for all sufficiently large separations. This is not a claim that the source presented the fraction as an established theorem; the source explicitly calls it a proposed relation.

## Assumptions and scope

The state is the translation-invariant thermodynamic-limit ground state of the isotropic nearest-neighbor XX chain, obtained as the quasifree Fermi sea. The magnetic field approaches saturation **from below**, and both the separation and inverse excitation density diverge on the same scale. Concurrence has the standard normalization \(C\in[0,1]\). No finite chain, thermal state, anisotropic interaction, or nonuniform field is asserted to obey the scaling formula. A fermionic staggered gauge transformation may flip signs of off-diagonal correlations but not concurrence.

## Proof

**Step 1: exact finite-separation two-spin data.** Jordan–Wigner fermionization of the ground state yields a quasifree correlation matrix with entries
\[
 g_j=\nu\,\operatorname{sinc}(\pi\nu j),\qquad j\in\mathbb Z.
\]
Here \(g_0=\nu\). The spin-flip coherence is, up to an irrelevant gauge phase,
\[
 z_r=\left\langle c_0^\dagger\prod_{j=1}^{r-1}(1-2c_j^\dagger c_j)c_r\right\rangle.
\]
Wick's rule, valid for the quasifree ground state, gives the exact **finite sum**
\[
 z_r=\sum_{m=0}^{r-1}(-2)^m
 \sum_{1\le j_1<\cdots<j_m\le r-1}
 \det[g_{x_a-y_b}]_{a,b=0}^{m},
\quad x=(0,j_1,\ldots,j_m),\ y=(r,j_1,\ldots,j_m).
\]
The corner probabilities of the two-spin density matrix are
\[
 p_{11}=\nu^2-g_r^2,\qquad
 p_{00}=(1-\nu)^2-g_r^2.
\]
Conservation of total magnetization makes the two-spin density matrix an X state, so its concurrence is
\[
 C_r=2\max\{0,|z_r|-\sqrt{p_{00}p_{11}}\}.
\]
These identities can be checked independently by evaluating the fermionic two-point contractions and the Jordan–Wigner string.

**Step 2: double-scaling limit of the entire string.** Let \(\nu r\to s\). In each fixed-\(m\) Wick term, scale the sites by \(u_a=\nu j_a\), and factor one \(\nu\) from each of the \(m+1\) determinant rows. The sum over strictly ordered internal sites converges to the ordered \(m\)-fold integral of the continuous sine-kernel determinant. Symmetrizing the internal variables supplies the factor \(1/m!\). Uniform termwise domination follows from the Gram representation
\[
 K(x,y)=\int_{-1/2}^{1/2}e^{2\pi i t(x-y)}\,dt.
\]
By the Gram/Hadamard inequality, every mixed determinant of this kernel has absolute value at most one. Therefore the normalized absolute \(m\)-th term is bounded by \((2\nu r)^m/m!\), whose sum is uniformly finite on compact \(s\)-ranges. Dominated convergence proves \(z_r/\nu\to F(s)\). Furthermore,
\[
 \frac{\sqrt{p_{00}p_{11}}}{\nu}
 \longrightarrow\sqrt{1-\operatorname{sinc}^{2}(\pi s)}.
\]
Continuity of the modulus and positive-part map proves the stated universal concurrence limit. The argument requires no invertibility of a Fredholm operator.

**Step 3: a strict analytic lower bound at the proposed onset scale.** Put \(s_0=\sqrt2/\pi\) and \(k=\sin(\sqrt2)/\sqrt2\). The zeroth term in \(F(s_0)\) is \(k\). Its first integral correction is
\[
 I_1=2\int_0^{s_0}\big[K(0,u)K(u,s_0)-k\big]du.
\]
For \(0<t<1\), Euler's sine product yields
\[
 -\frac{d^2}{dt^2}\log\left(\frac{\sin(\pi t)}{\pi t}\right)
 \ge \frac{\pi^2}{3}+\frac{\pi^4t^2}{15}.
\]
Integrating this bound over the rectangle with sides \(u\) and \(s_0-u\), and using \(e^a\ge1+a\), gives
\[
 I_1\ge k\left(\frac{\pi^2s_0^3}{9}+\frac{\pi^4s_0^5}{150}\right)
 =\frac{56\sqrt2}{225\pi}k.
\]
For each \(m\ge2\), the mixed Gram determinant is bounded using successive divided differences of the vectors \(v_x(t)=e^{2\pi i t x}\) in \(L^2([-1/2,1/2])\). The \(j\)-th divided difference has norm at most \(\pi^j/(j!\sqrt{2j+1})\). Factoring the row and column Vandermonde products, each bounded by \(s_0^{m(m+1)/2}\), yields
\[
 \left|\det[K(x_a,y_b)]\right|
 \le\frac{(\pi s_0)^{m(m+1)}}{\prod_{j=0}^{m}(j!)^2(2j+1)}.
\]
Consequently the total absolute \(m\ge2\) tail is bounded by
\[
 T\le\sum_{m=2}^\infty\frac{(2s_0)^m}{m!}
 \frac{(\pi s_0)^{m(m+1)}}{\prod_{j=0}^m(j!)^2(2j+1)}
 <\frac{100}{99}\frac{8}{15\pi^2}.
\]
The ratio of successive summands is at most the ratio at \(m=2\), which is less than \(1/100\); the \(m=2\) term is exactly \(8/(15\pi^2)\).

For fully rational comparisons, use
\[
 \frac{314159}{100000}<\pi<\frac{314160}{100000},\qquad
 \sqrt2>\frac{14142}{10000},\qquad k>\frac{6984}{10000}.
\]
The last inequality follows from the alternating expansion \(k=\sum_{j=0}^\infty(-2)^j/(2j+1)!\). These rational bounds imply
\[
 F(s_0)>\frac{6984}{10000}
 +\frac{6984}{10000}\frac{56(14142/10000)}{225(314160/100000)}
 -\frac{800}{1485(314159/100000)^2}
 >\frac{716}{1000},
\]
whereas \(\sqrt{1-k^2}<716/1000\). Thus the limiting concurrence is strictly positive, with no numerical-integration assumption.

**Step 4: interpretation of the empirical onset formula.** For the stated proposed field, \(1-h_r^{\mathrm{prop}}/J=1/((r-1)^2+1)\). The elementary expansion of inverse cosine at one gives
\[
 r\nu_r=\frac r\pi\arccos\left(1-\frac1{(r-1)^2+1}\right)
 \longrightarrow\frac{\sqrt2}{\pi}=s_0.
\]
Step 2 and the positive strict bound in Step 3 imply \(C_r(h_r^{\mathrm{prop}})>0\) for every sufficiently large integer \(r\). Each fixed-distance two-site reduced state depends continuously on \(0<h<J\); strict positivity therefore persists at a slightly smaller field. Hence equality of the proposed field and the exact onset for all distances is false.

## Verification

The accompanying `verify.py` recomputes fifteen short Jordan–Wigner Wick expansions and their independent block-determinant values, validates the sign certificate using exact rational arithmetic (including the alternating sine-series lower bound), and checks three finite-distance instances of the proposed field. Its printed Fredholm value is an illustrative Nyström approximation and **not** used to certify the infinite-dimensional theorem. Execute `python verify.py` with Python 3 and NumPy installed. The decisive strict inequality is established by the displayed analytic and rational bounds, not finite sampling.

## Relationship to prior work

Fumani, Nemati, Mahdavifar and Darooneh, arXiv:1507.07384, derive finite-distance concurrence for separations two, three and four and **propose**, rather than prove, a simple formula extrapolating the magnetic-entanglement onset to arbitrary distance. Their explicit Jordan–Wigner correlators are the starting point; neither the general Wick string nor the spin-chain model is claimed here as new. The novel claim is the simultaneous dilute-density, long-separation concurrence limit **and** its certified strict implication against the extrapolated all-distance equality.

Yano and Nishimori (2005) analyze arbitrary-distance entanglement numerically and analytically, with entanglement length as a subject. Their complete article could not be materially inspected here, so possible equivalent asymptotics remain a priority risk. Its, Jin and Korepin (arXiv:quant-ph/0409027) derive integrable Fredholm representations for **block von Neumann entropy**, not two-site concurrence; standard sine-kernel Fredholm theory is used, not presented as original. Latorre, Rico and Vidal (arXiv:quant-ph/0304098) review and develop **block** entropy scaling. General high-field random-phase-approximation concurrence results concern a different approximation and do not establish this exact double-scaling equality.

## Limitations

The theorem gives the **pointwise** limit along every admissible scaled sequence. It does not identify all zeros of the limiting profile, the exact onset field at each finite distance, or the full finite-distance concurrence phase diagram. It does not assign independent priority or extend beyond the isotropic, zero-temperature infinite chain. A potentially covering formulation hidden in older arbitrary-distance entanglement or impenetrable-boson Fredholm-minor literature remains possible, particularly Yano–Nishimori (2005), whose complete text was not obtained.

## References

1. F. K. Fumani, S. Nemati, S. Mahdavifar, A. Darooneh, *Magnetic Entanglement in Spin-1/2 XX Chains* (original 2015 preprint; later revision titled *XY Chains*), arXiv:1507.07384, first posted 2015-07-27. https://arxiv.org/abs/1507.07384
2. H. Yano and H. Nishimori, *Ground State Entanglement in Spin Systems*, Progress of Theoretical Physics Supplement **157** (2005), 164–167. https://doi.org/10.1143/PTPS.157.164
3. A. R. Its, B.-Q. Jin, V. E. Korepin, *Entanglement in XY Spin Chain*, arXiv:quant-ph/0409027. https://arxiv.org/abs/quant-ph/0409027
4. J. I. Latorre, E. Rico, G. Vidal, *Ground state entanglement in quantum spin chains*, arXiv:quant-ph/0304098. https://arxiv.org/abs/quant-ph/0304098
5. J. M. Matera, R. Rossignoli, N. Canosa, *Evaluation of pairwise entanglement in translationally invariant systems with the random phase approximation*, Phys. Rev. A **78**, 042319 (2008). https://doi.org/10.1103/PhysRevA.78.042319
