# Single-impulse quadratic chirps: exact cyclic Gabor tomography spectrum and arithmetic rank obstruction
## Finding
Fix any integer \(N\ge3\), any integer \(a\), and any real \(t>0\). On \(\mathbb Z_N\), put \(\omega=\exp(2\pi i/N)\) and
\[
g(j)=\omega^{aj^2}+t\mathbf1_{\{0\}}(j),\qquad j\in\mathbb Z_N.
\]
Let \(T_u h(j)=h(j-u)\), \(M_vh(j)=\omega^{vj}h(j)\), and \(\pi_{u,v}=M_vT_u\). For the complex-linear lifted Gabor intensity operator
\[
\mathcal L_g(H)=\big(\langle H,\pi_{u,v}gg^*\pi_{u,v}^*\rangle_{\mathrm{HS}}\big)_{u,v\in\mathbb Z_N},
\quad H\in\mathbb C^{N\times N},
\]
all \(N^2\) singular values, counted with multiplicity, are exactly
\[
\big\{\sqrt N\,|A_g(u,v)|:(u,v)\in\mathbb Z_N^2\big\},
\]
where the following is an *explicit*, nonrecursive formula:
\[
A_g(u,v)=
\begin{cases}
N+t(t+2),&u=v=0,\\
t(t+2),&u=0,\ v\ne0,\\
(N+2t)\omega^{au^2},&u\ne0,\ v=2au,\\
t\omega^{au^2}(1+\omega^{u(v-2au)}),&u\ne0,\ v\ne2au.
\end{cases}
\]
All equalities between frequency indices are modulo \(N\). Thus the degree of the chirp affects the *placement*, but not the multiset, of singular values.

For **odd** \(N\), all singular values are positive. The smallest is
\[
\sigma_{\min}(\mathcal L_g)=2\sqrt N\,t\sin\left(\frac\pi{2N}\right),
\]
while \(\sigma_{\max}(\mathcal L_g)=\sqrt N\,(N+2t+t^2)\). In particular, full cyclic Gabor intensities of this explicitly specified window recover any complex signal, up to one global phase. The exact linear-lifting condition number is
\[
\kappa(t)=\frac{N+2t+t^2}{2t\sin(\pi/(2N))}.
\]
Within the whole positive single-impulse family the **unique** optimal strength is \(t=\sqrt N\), and the optimal condition number is
\[
\boxed{\kappa_* =\frac{1+\sqrt N}{\sin(\pi/(2N))}}.
\]
Equivalently, normalizing \(g\) to unit squared norm, its largest possible minimum ambiguity modulus is \(\sin(\pi/(2N))/(1+\sqrt N)\).

For **even** \(N\), the lifted map has an arithmetically determined nonzero kernel, independent of \(a\) and \(t>0\):
\[
\boxed{\dim\ker\mathcal L_g=Z_N
=\sum_{d\mid N/2}d\,\varphi(N/d)},
\]
where \(\varphi\) denotes Euler's totient function. More explicitly, if \(N=2^s m\) with \(s\ge1\) and odd \(m=\prod_{p^e\parallel m}p^e\), then
\[
Z_N=s2^{s-1}\prod_{p^e\parallel m}p^{e-1}\big((e+1)p-e\big).
\]
The least *positive* singular value for even \(N\ge4\) is \(2\sqrt N\,t\sin(\pi/N)\). This is a statement about linear completeness of all lifted intensity measurements, **not** a claim that nonlinear phase retrieval is impossible in even dimension.

## Assumptions and scope
The cyclic group \(\mathbb Z_N\) is represented by residues \(0,\ldots,N-1\); the inner product on \(\mathbb C^N\) is the unnormalized Euclidean inner product. The matrix space uses the Hilbert--Schmidt inner product and the data space the unnormalized Euclidean norm. The window is not normalized unless explicitly stated. The nonnegative parameter \(t\) is taken **strictly positive** throughout; neither negative nor complex perturbations are optimized. Multiplying the window by a scalar changes the lifting singular values by its squared modulus and leaves the condition number unchanged.

For phase retrieval, the data are the full set of \(N^2\) numbers \(|\langle f,\pi_{u,v}g\rangle|^2\). A sufficiently strong criterion for recovery up to global phase is that every self-ambiguity coefficient is nonzero [2]. The theorem gives this for odd \(N\); the even case asserts only the exact rank defect of \(\mathcal L_g\).

## Proof
**1. Exact ambiguity calculation.** Adopt the sign convention
\[
A_g(u,v)=\sum_{j\in\mathbb Z_N}g(j+u)\overline{g(j)}\omega^{-vj}.
\]
Expanding the two factors gives the pure-chirp sum
\[
\sum_j\omega^{a((j+u)^2-j^2)-vj}
=N\omega^{au^2}\mathbf1_{\{v=2au\}},
\]
together with the two linear impulse terms
\[
t\omega^{au^2}+t\omega^{-au^2+uv}
=t\omega^{au^2}(1+\omega^{u(v-2au)})
\]
and the quadratic impulse term \(t^2\mathbf1_{\{u=0\}}\). This yields all four branches of the displayed formula, with no primality assumption.

**2. Exact singular-value diagonalization.** The \(N^2\) Weyl matrices \(\pi_{u,v}/\sqrt N\) form an orthonormal basis of \(\mathbb C^{N\times N}\). Conjugation of a fixed Weyl matrix by \(\pi_{r,s}\) multiplies it by a character of \(\mathbb Z_N^2\). Consequently the columns of \(\mathcal L_g\) on the Weyl basis are orthogonal character vectors, with squared norms \(N|A_g(u,v)|^2\). Thus the complete singular-value multiset is \(\sqrt N|A_g(u,v)|\). This also shows that the number of zero singular values equals the number of zero ambiguity coefficients, including algebraic multiplicity.

**3. Odd and even zero patterns.** For \(t>0\), the zero-lag entries \(N+t(t+2)\) and \(t(t+2)\), and the on-line entries \(N+2t\), are all nonzero. Off the line \(v=2au\), a zero can occur precisely when \(\omega^{u(v-2au)}=-1\). An odd cyclic root group has no root \(-1\), proving all ambiguity coefficients nonzero for odd \(N\). For even \(N\), the exact condition is
\[
u(v-2au)\equiv N/2\pmod N.
\]
For each nonzero \(u\), let \(d=\gcd(u,N)\). This congruence has exactly \(d\) solutions \(v\) if \(d\mid N/2\), and none otherwise; every such solution is off the line. There are \(\varphi(N/d)\) choices of \(u\) with that gcd. Summing proves \(Z_N\). If \(N=2^sm\), multiplicativity of the odd divisor sum gives
\[
Z_N=s2^{s-1}\sum_{d\mid m}d\varphi(m/d)
=s2^{s-1}\prod_{p^e\parallel m}p^{e-1}((e+1)p-e).
\]

**4. Sharp endpoints and optimizing the impulse.** For positive \(t\), the largest ambiguity modulus is always \(N+2t+t^2\), attained at \((u,v)=(0,0)\). Every nonzero off-line modulus has the form
\[
2t\left|\cos\left(\frac{\pi k}{N}\right)\right|,
\quad k=u(v-2au)\pmod N.
\]
For odd \(N\), its minimum over nonzero residues is \(2t\sin(\pi/(2N))\); for even \(N\ge4\), its minimum over nonzero residues distinct from \(N/2\) is \(2t\sin(\pi/N)\). Both are attained by taking \(u=1\) and an appropriate \(v\). They are strictly below the other positive branch magnitudes, since \(t(t+2)>2t\) and \(N+2t>2t\). This proves both minimum formulas. Finally
\[
\frac{N+2t+t^2}{t}=\frac Nt+2+t
\ge 2\sqrt N+2,
\]
with equality if and only if \(t=\sqrt N\). This is the asserted unique optimal linear-lifting condition number. For odd \(N\), the nonvanishing-ambiguity phase-retrieval implication follows from [2, Theorem 2.2].

## Verification
The accompanying `verify.py` uses only the Python standard library. Running `python verify.py` recomputes self-ambiguity independently from the defining finite sum and compares it with the four-branch expression for every index in cyclic orders \(3\) through \(28\), three chirp parameters and three impulse values. It checks the totient nullity, endpoints, and unique positive optimizer over the tested values. An additional direct numerical singular-value decomposition of the lifted measurement matrices in orders \(3\) through \(8\) gave the same complete singular-value multisets. These finite computations corroborate, but do not replace, the exact all-order proof above.

## Relationship to prior work
Casazza and Fickus [1] analyze finite cyclic chirps, their Fourier transforms, and tight-frame correlations, including modulus-dependent effects. Their results treat unperturbed chirps; no single-impulse lifted-intensity rank census or exact optimizing impulse appears in the inspected paper. Bojarovska and Flinth [2] diagonalize finite Gabor intensity lifting and give a nonvanishing-ambiguity sufficient condition for phase retrieval. Their theorem supplies the general lifting framework and the last implication of the odd-order case, but does not itself calculate the ambiguity, singular spectrum, arithmetic nullity, or optimal impulse for this window family.

Related published results study a nonperiodic quadratic-exponent window \(j\mapsto e^{-j^2}\) and its odd/even ambiguity behavior [3]. That seed differs from the periodic unit-modulus quadratic chirp with a single additive impulse here; neither its exponential lower bound nor its half-period cancellation statement implies the explicit all-order rank census and sharp conditioning above. More recent constructions of quantitatively phase-retrievable Gabor windows [4] have better asymptotic margins for different seeds and establish a broader existence result. No global optimality among arbitrary windows is asserted here.

## Limitations
The condition-number optimum is solely within the one-positive-real-impulse chirp family. The margin for odd \(N\) scales like \(N^{-3/2}\) and is weaker than known margins for other window constructions. The even-order kernel of the lifted operator does not establish nonlinear phase-retrieval failure; full spark is not claimed. Formula-equivalent versions in older cyclic frame or radar-sequence literature remain a priority risk, and the most recent perturbation paper [4] was accessible here only at abstract level.

## References
1. P. G. Casazza and M. Fickus, *Fourier Transforms of Finite Chirps*, EURASIP Journal on Applied Signal Processing (2006), article 70204, DOI:10.1155/ASP/2006/70204; full open-access text.
2. I. Bojarovska and A. Flinth, *Phase Retrieval from Gabor Measurements*, arXiv:1503.05800, Theorem 2.2 and the lifted-operator bounds; full preprint.
3. *A parity dichotomy for Malikiosis's quadratic-exponent Gabor window*, published-finding corpus identifier `2026/10/4/SCOPE-a-parity-dichotomy-for-malikiosis-s-quadratic-exponent-gabor-win--8ac7d311b287`; RESULT.md read in full.
4. D. Li, *Explicit Full-Spark and Quantitatively Phase-Retrievable Gabor Windows via Algebraic Perturbations*, arXiv:2609.09614; abstract-level comparison only.
