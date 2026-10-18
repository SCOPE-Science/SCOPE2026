# Resonance walls and two-point fibers in shifted Euler-derivative phase retrieval

## Finding
For an integer \(d\ge1\) and a complex number \(\alpha\), define the Euler-filtered polynomial
\[
\mathcal E_\alpha P(z)=zP'(z)-\alpha P(z),\qquad P\in\mathbb C[z]_{\le d}.
\]
Let \(W\) be **any** \(2d+1\) distinct unit-modulus points and let \(V\) be **any** \(2d-1\) distinct unit-modulus points. Points may coincide between the two sets. From the \(4d\) real intensities
\[
\bigl\{|P(w)|^2:w\in W\bigr\}\quad\text{and}\quad
\bigl\{|\mathcal E_\alpha P(v)|^2:v\in V\bigr\},
\]
where each datum is labeled by its sampling point, the entire phase-retrieval fiber is as follows.

If \(2\operatorname{Re}\alpha\notin\{1,\ldots,2d-1\}\), every nonzero \(P\) is determined up to multiplication by a unimodular constant. If \(2\operatorname{Re}\alpha=k\in\{1,\ldots,2d-1\}\), every fiber modulo global phase has at most two elements: \(P\) and, *when it is a polynomial of degree at most \(d\)*, its shifted reciprocal conjugate
\[
\mathcal R_kP(z)=z^k\overline{P(1/\overline z)}
=\sum_{j=0}^{d}\overline{a_{k-j}}z^j,
\qquad P(z)=\sum_{j=0}^{d}a_jz^j,
\]
where the coefficient summation is valid **only under the support condition below** (outside it, the preceding expression is a Laurent polynomial and is not an admissible polynomial alternative). The second member exists exactly when the support of \(P\) is contained in
\[
\max(0,k-d)\le j\le\min(d,k).
\]
On this support, the second member may equal the first modulo phase, but no other ambiguity occurs. Every resonant value \(k\) admits non-phase-equivalent monomials having identical data, so the nonresonance condition is also necessary for **universal** phase retrieval. The imaginary part of \(\alpha\) does not affect the resonance walls.

## Assumptions and scope
The polynomial space is the full complex vector space of degrees at most \(d\), including lower-degree polynomials, zero coefficients, boundary zeros, and the zero polynomial. Distinctness is required within each sampling set only. There are no assumptions on angular spacing, on nonvanishing of samples, or on a generic input. Global phase means \(P\sim cP\) with \(|c|=1\). The zero polynomial is uniquely detected by the first channel. The result is about exact noiseless measurements, not uniform numerical conditioning. The primary classification is complex analysis / holomorphic-polynomial phase retrieval (MSC \(30D05\)).

## Proof
**Step 1: finite data determine both complete intensity profiles.** On \(|z|=1\), let
\[
A(z)=|P(z)|^2,\qquad B(z)=|\mathcal E_\alpha P(z)|^2.
\]
These are real Laurent polynomials of degree at most \(d\) in each direction. The \(2d+1\) first-channel values determine \(A\): after multiplication by \(z^d\), a difference of two such Laurent polynomials becomes an ordinary polynomial of degree at most \(2d\) with \(2d+1\) distinct zeros.

Write \(P(z)=\sum_{j=0}^{d}a_jz^j\), allowing zero leading or constant coefficients. The top positive Fourier coefficients of the profiles satisfy
\[
[A]_d=a_d\overline{a_0},\qquad
[B]_d=-\overline\alpha(d-\alpha)[A]_d.
\]
Thus the known \(A\) fixes both extreme Fourier coefficients of \(B\), even when they vanish. Subtract these known harmonics from \(B\); the remainder is a real trigonometric polynomial of degree at most \(d-1\). Its \(2d-1\) values at the arbitrary distinct points of \(V\) recover it uniquely by the same zero-count argument. Hence the finite data determine \(A\) and \(B\) on the **entire** unit circle.

**Step 2: a global sign alternative.** Set \(z=e^{it}\), \(u=\operatorname{Re}\alpha\), and \(v=\operatorname{Im}\alpha\). Define
\[
C_P(t)=zP'(z)\overline{P(z)},\qquad
S_P(t)=\operatorname{Re}C_P(t)-uA(t).
\]
Differentiating the first intensity gives
\[
A'(t)=-2\operatorname{Im}C_P(t).
\]
Expanding \(A(t)B(t)=|zP'(z)\overline{P(z)}-\alpha A(t)|^2\) yields the **exact** Laurent-polynomial identity
\[
S_P(t)^2=A(t)B(t)-\left(\frac{A'(t)}2+vA(t)\right)^2.
\]
If \(Q\) has the same two profiles, then \(S_Q^2=S_P^2\). Since the real trigonometric polynomials are restrictions of Laurent polynomials and \(\mathbb C[z,z^{-1}]\) has no zero divisors, either \(S_Q=S_P\) at every point, or \(S_Q=-S_P\) at every point. No sign change on isolated arcs is possible.

**Step 3: the positive branch.** If \(S_Q=S_P\), the imaginary and real parts of \(C_P\) and \(C_Q\) coincide, because \(A\) and its derivative coincide. Away from their finitely many zeros, divide by the common intensity to obtain
\[
\frac{zP'(z)}{P(z)}=\frac{zQ'(z)}{Q(z)}\quad(|z|=1).
\]
As rational functions the equality is global; consequently \(P'Q-PQ'=0\) and \(Q=cP\), where \(|c|=1\) follows from \(A_Q=A_P\).

**Step 4: the negative branch and its integer obstruction.** Suppose \(S_Q=-S_P\), and neither polynomial is zero. Wherever neither vanishes on the circle,
\[
\operatorname{Re}\left(\frac{zQ'}Q+\frac{zP'}P\right)=2u.
\]
Introduce the Laurent-conjugate \(P^\#(z)=\overline{P(1/\overline z)}\) and the nonzero rational function \(F(z)=Q(z)/P^\#(z)\). Because \(|Q|=|P|\) on the circle, \(|F|=1\) there wherever defined. The logarithmic angular derivative \(zF'/F\) is real there. Further, \(z(P^\#)'/P^\#=-\overline{zP'/P}\) on that circle, so
\[
\frac{zF'}F=\frac{zQ'}Q+\overline{\frac{zP'}P}=2u
\quad\text{on the circle away from zeros}.
\]
Rational identity gives this equality throughout its domain. If \(k\) is the integral order of \(F\) at \(z=0\), then the constant term of \(zF'/F\) near zero is \(k\), whence \(2u=k\in\mathbb Z\). Integrating the rational logarithmic derivative shows \(F(z)=cz^k\), with \(|c|=1\). Thus
\[
Q(z)=c\mathcal R_kP(z).
\]
For this to be a polynomial of degree at most \(d\), every nonzero coefficient of \(P\) must have exponent \(j\) such that \(0\le k-j\le d\), giving the stated support interval. For nonzero \(P\), that interval is nonempty precisely when \(0\le k\le2d\). When \(k=0\) or \(k=2d\), it contains only a single endpoint exponent, so the reflected polynomial is phase-equivalent to the original. The only possible **nontrivial** resonances are \(1\le k\le2d-1\).

**Step 5: converse and sharp failures.** Whenever \(k=2\operatorname{Re}\alpha\) and the support condition holds, the polynomial \(Q=\mathcal R_kP\) satisfies on \(|z|=1\)
\[
Q(z)=z^k\overline{P(z)},\qquad
\mathcal E_\alpha Q(z)=-z^k\overline{\mathcal E_\alpha P(z)},
\]
because \(k-\alpha=\overline\alpha\). Therefore it gives exactly the same full intensity profiles. Applying \(\mathcal R_k\) twice returns \(P\), so each nonzero fiber has at most two phase classes. To show that **each** listed resonance is genuine, take \(j=\max(0,k-d)\) and \(\ell=k-j\), so \(0\le j<\ell\le d\). The monomials \(P(z)=z^j\), \(Q(z)=z^\ell\) are inequivalent, while both intensities are equal to \(1\) and \(|j-\alpha|^2=|\ell-\alpha|^2\) respectively. This completes the global classification and all boundary cases.

## Verification
The accompanying standalone Python/NumPy file `checks/verify.py` performs exact rational-complex Laurent-identity checks and reciprocal-conjugate symmetry tests for degrees \(1\) through \(8\), together with a detuned nonresonance witness and top-harmonic identities. It also reconstructs both intensity profiles from distinct nonuniform angular grids for \(48\) numerical cases. Running `python checks/verify.py` produces the included `checks/output.txt`: \(105\) exact identity/resonance checks, \(48\) finite-sampling reconstructions, maximum numerical Fourier-coefficient discrepancy approximately \(1.14\times10^{-13}\), and `PASS`. The proof above, rather than finite tests, establishes the universal theorem.

## Relationship to prior work
Friedrich Philipp, *Phase Retrieval from 4N–4 Measurements* (2014), Theorem 1.1, already proves that the full polynomial can be reconstructed from \(2d+1\) intensity evaluations of \(P\) and \(2d-1\) intensity evaluations of \(P'\) at arbitrary unit-circle points. Thus the unshifted derivative case \(\alpha=0\), the count \(4d\), Fourier interpolation, and the general real-part sign-alternative technique are prior art. The present result does **not** claim any of those ingredients as new. Its additional assertion is the full **complex-parameter** classification of shifted Euler-filtered measurements, including all half-integer real-part resonances, exact two-point fibers, support restrictions, and counterexamples at every resonance. This is not a direct consequence of the unshifted theorem, which contains no classification for the nonzero shift.

Rolando Perez III, *A Note on the Phase Retrieval of Holomorphic Functions* (first available 2020), treats continuous modulus data on pairs of intersecting segments or concentric circles in holomorphic/Nevanlinna spaces; it does not analyze an Euler-filtered second intensity channel. Related joint-channel spectral-factorization studies, including Flamant and collaborators' *Polarimetric Phase Retrieval* (2022), likewise do not give the stated parameter-wall theorem in their inspected main results. No stronger known coverage is asserted to be impossible; an older equivalent formulation in differential phase retrieval or reciprocal-polynomial literature remains a bibliographic risk.

## Limitations
The classification is exact and noiseless. Near a resonance wall, or for clustered sampling points, numerical conditioning can deteriorate; no quantitative stability uniform in \(\alpha\), \(d\), or angular separation is established. Nothing here proves that \(4d\) is the smallest possible number of measurements among all measurement designs. The imaginary part of the shift affects numerical values but not the uniqueness classification. The direct phase-retrieval extension is specific to the diagonal Euler filter, not to arbitrary differentiation-like operators. Novelty is assessed by comparison with accessible literature and indexed claims, not by exhaustive proof of historical priority. Independent validation has not been performed.

## References
- F. Philipp, *Phase Retrieval from 4N–4 Measurements*, arXiv:1403.4769v1 (19 March 2014), particularly Theorem 1.1 and Section 2. https://arxiv.org/pdf/1403.4769
- R. Perez III, *A Note on the Phase Retrieval of Holomorphic Functions*, arXiv:2009.02061v1 (4 September 2020), primary MSC 30D05, Theorems 2.1–2.2. https://arxiv.org/abs/2009.02061
- J. Flamant and collaborators, *Polarimetric Phase Retrieval: Uniqueness and Algorithms*, arXiv:2206.12868v1 (2022). https://arxiv.org/abs/2206.12868
