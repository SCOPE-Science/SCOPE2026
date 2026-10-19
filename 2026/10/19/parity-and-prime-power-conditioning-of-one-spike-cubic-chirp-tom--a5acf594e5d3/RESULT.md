# Parity and prime-power conditioning of one-spike cubic chirp tomography

## Finding

Let \(p\) be prime, \(a\ge1\), \(N=p^a\), and \(\zeta=\exp(2\pi i/N)\). On \(\mathbb Z/N\mathbb Z\) define
\[
 g(j)=\zeta^{j^3}+\mathbf1_{\{0\}}(j),\qquad h=g/\sqrt{N+3}.
\]
Use translations \((T_k f)(j)=f(j-k)\), modulations \((M_\ell f)(j)=\zeta^{\ell j}f(j)\), and the self-ambiguity function
\[
 A(k,\ell)=\sum_{j=0}^{N-1}\overline{g(j)}g(j-k)\zeta^{-\ell j}.
\]
For the full Weyl-orbit intensity lifting associated with the normalized window \(h\), all \(N^2\) singular values, including zeros and multiplicities, are
\[
 \left\{\frac{\sqrt N}{N+3}|A(k,\ell)|:(k,\ell)\in(\mathbb Z/N\mathbb Z)^2\right\}.
\]
The largest singular value is always \(\sqrt N\), occurring once.

**Odd prime powers.** If \(p\ge5\), every ambiguity coefficient is nonzero. For \(a\ge2\), the *exact* least ambiguity modulus and its multiplicity are
\[
 m_{p,a}=2\sin\!\left(\frac{\pi}{2p^{a-1}}\right),\qquad
 \#\{|A|=m_{p,a}\}=2p^{a-1}(p-1).
\]
The minimizing indices are exactly those with \(v_p(k)=1\) and
\[
 (k/p)\ell\equiv\frac{p^{a-1}+1}{2}
 \quad\text{or}\quad\frac{p^{a-1}-1}{2}\pmod{p^{a-1}}.
\]
For \(p\ge5\), \(a=1\), all ambiguity coefficients are nonzero; **no exact least-modulus formula is claimed in that case**. If \(p=3\), for *every* \(a\ge1\),
\[
 m_{3,a}=2\sin\!\left(\frac{\pi}{2\cdot3^a}\right),\qquad
 \#\{|A|=m_{3,a}\}=4\cdot3^{a-1},
\]
attained exactly when \(3\nmid k\) and
\[
 k\ell\equiv\frac{3^a+1}{2}
 \quad\text{or}\quad\frac{3^a-1}{2}\pmod{3^a}.
\]
Thus in all odd prime-power dimensions, the Weyl orbit of \(h\) gives informationally complete linear operator tomography and determines every complex signal up to global phase. For \(p\ge5\), \(a\ge2\), its **exact Hilbert--Schmidt lifting condition number** is
\[
 \kappa_{p,a}=\frac{N+3}{2\sin(\pi/(2p^{a-1}))};
\]
for \(p=3\) the denominator is \(2\sin(\pi/(2\cdot3^a))\). These condition numbers refer to the complete \(N^2\)-outcome linear-lifting map, not optimal nonlinear reconstruction or arbitrary-window design.

**Dyadic prime powers.** For \(N=2^a\), \(a\ge2\), the exact zero set is
\[
 \{(k,\ell): k\ell\equiv N/2\pmod N,\quad
 [k\text{ odd}\ \text{or}\ (2\mid k,\ 2v_2(k)\ge a-1)]\}.
\]
Here \(k\ne0\) is understood wherever \(v_2(k)\) is used. In particular the lifted rank is
\[
 \boxed{\operatorname{rank}\mathcal L_h
 =N^2-2^{a-1}\!\left(1+\left\lfloor\frac{a+1}{2}\right\rfloor\right).}
\]
At \(N=2\), precisely \((k,\ell)=(1,1)\) is an ambiguity zero, giving rank \(3\). The dyadic conclusion is **failure of linear informational completeness**; it does not assert failure of nonlinear pure-state phase retrieval.

## Assumptions and scope

Indices are residues modulo \(N\), and the matrix-space norm is Hilbert--Schmidt while the measurement-space norm is Euclidean. More precisely, write \(\pi(k,\ell)=M_\ell T_k\), \(P_{k,\ell}=\pi(k,\ell)hh^*\pi(k,\ell)^*\), and
\[
 \mathcal L_h(X)=(\operatorname{tr}(XP_{k,\ell}))_{k,\ell},\qquad X\in\mathbb C^{N\times N}.
\]
This is the complex-linear extension of the physical intensity map from Hermitian matrices. The prime-power hypothesis is part of the classification. No conclusions about arbitrary composite moduli, full-spark frames, or optimality over all windows are asserted. The center coefficient of \(g\) is exactly \(2\); all other coefficients have modulus \(1\), so \(\|g\|_2^2=N+3\).

## Proof

**1. Complete correlation reduction.** For \(k=0\), orthogonality of characters gives \(A(0,0)=N+3\) and \(A(0,\ell)=3\) if \(\ell\ne0\). For \(k\ne0\), expanding the two shifted cubic factors and the two single-impulse cross terms gives the exact identity
\[
 A(k,\ell)=\zeta^{-k^3}\left[
 Q_N(-3k,3k^2-\ell)+1+\zeta^{-k\ell}\right],
 \qquad Q_N(c,b)=\sum_{j\bmod N}\zeta^{cj^2+bj}.
\tag{1}
\]
There is no double-impulse contribution for nonzero \(k\). All phases in the formula arise from a single choice of modulation sign.

**2. Gauss-sum facts, including degeneracies.** Let \(d=\gcd(c,N)\). By grouping residues modulo \(N/d\), \(Q_N(c,b)=0\) unless \(d\mid b\); if \(d\mid b\),
\[
 Q_N(c,b)=d\,Q_{N/d}(c/d,b/d).
\]
If \(N/d\) is odd and \(c/d\) is a unit, completing the square and applying orthogonality to the difference of two squares gives
\[
 |Q_{N/d}(c/d,b/d)|=\sqrt{N/d}.
\]
For a power of two \(2^r\) with \(r\ge2\), primitive quadratic Gauss sums with odd leading coefficient vanish when \(b\) is odd, and have modulus \(\sqrt{2^{r+1}}\) when \(b\) is even. Indeed, for odd \(c\), a direct squared-modulus expansion with \(h=x-y\) shows \( |Q_{2^r}(c,b)|^2=2^r[1+(-1)^b]\): the inner character sum over \(y\) survives only for \(h=0\) and \(h=2^{r-1}\), and the quadratic phase of the second survivor is one for \(r\ge2\). This proves both the vanishing and the magnitude without evaluating any Gauss phase. At reduced modulus \(2\), the sum is zero for even \(b\) and has modulus \(2\) for odd \(b\). These statements include every zero/nonzero Gauss branch used below.

**3. Odd primes at least five.** For \(k\ne0\), write \(t=v_p(k)<a\), so \(d=p^t\). Whenever the Gauss term in (1) is nonzero its modulus is \(\sqrt{Np^t}\ge\sqrt N\), hence by the reverse triangle inequality \(|A(k,\ell)|\ge\sqrt N-2>0\). When it vanishes, \(|A|=|1+\zeta^{-k\ell}|\), which is strictly positive because \(N\) is odd. The indices \(k=0\) are also nonzero, establishing informational completeness for all \(a\ge1\).

For \(a\ge2\), \(\sqrt N-2\ge p-2\ge3\), whereas the candidate minimum in the Finding is at most \(2\sin(\pi/(2p))<1\). Thus a global minimum must lie on the zero-Gauss branch. The latter requires \(t\ge1\) (because the primitive odd Gauss sum with \(p\nmid k\) never vanishes) and \(\ell\not\equiv0\pmod{p^t}\). The order of \(\zeta^{k\ell}\) divides \(p^{a-t}\); among roots of odd order \(p^{a-t}\), the nearest roots to \(-1\) have modulus \(2\sin(\pi/(2p^{a-t}))\) for \(1+z\). This lower bound is smallest precisely when \(t=1\). At the two nearest roots the displayed modular conditions make \(\ell\) a unit, so the Gauss term does vanish. Each of the \((p-1)p^{a-2}\) choices of \(k\) having valuation one admits exactly \(p\) lifts of each of the two frequencies, giving \(2p^{a-1}(p-1)\) minimizers.

**4. Characteristic three.** When \(3\nmid k\), the quadratic coefficient \(-3k\) has gcd \(3\) with \(N\) for \(a\ge2\); taking \(3\nmid\ell\) makes the Gauss term vanish. Now \(k\) is a unit and \(\zeta^{k\ell}\) ranges over all primitive \(3^a\)-th roots, so the minimum and the stated two congruences follow. For \(3\mid k\), the impulse phase has order at most \(3^{a-1}\), forcing a strictly larger zero-Gauss modulus. Every *nonzero* Gauss term for \(a\ge2\) has modulus at least \(\sqrt{3N}\), except a fully constant phase, which has modulus \(N\). Its possible cancellation by a term of magnitude at most \(2\) cannot reach the proposed minimum. At \(N=3\) one checks directly that \(A(0,0)=6\), \(|A(0,\ell)|=3\) for \(\ell\ne0\), and at nonzero \(k\) the moduli are \(5\) for \(\ell=0\) and \(1\) for \(\ell\ne0\). The number of minimizing pairs is twice the number \(\varphi(3^a)=2\cdot3^{a-1}\) of unit shifts, namely \(4\cdot3^{a-1}\).

**5. Powers of two.** Suppose \(a\ge2\) and \(k\ne0\). If the Gauss term in (1) is nonzero, its magnitude is at least \(\sqrt{2N}>2\) when the reduced modulus is at least four; when the reduced modulus is two it has magnitude at least \(2^{a}>2\). Consequently it cannot cancel the impulse term, whose magnitude is at most \(2\). Hence \(A(k,\ell)=0\) exactly when *both* the Gauss term vanishes and \(\zeta^{k\ell}=-1\), the latter equivalent to \(k\ell\equiv N/2\pmod N\). If \(k\) is odd, this congruence forces even \(\ell\) and makes \(3k^2-\ell\) odd, so the primitive dyadic Gauss sum vanishes. If \(t=v_2(k)\ge1\), the product congruence forces \(v_2(\ell)=a-t-1\). When \(a-t-1<t\), the gcd \(2^t\) of the quadratic coefficient and \(N\) does not divide the linear coefficient, forcing zero. At equality \(a-t-1=t\), the divided linear coefficient is odd, again forcing zero for the reduced modulus \(2^{t+1}\). When \(a-t-1>t\), the reduced linear coefficient is even and its Gauss sum is nonzero. These alternatives are precisely \(2t\ge a-1\).

Each odd \(k\) admits one frequency solving the product congruence, yielding \(2^{a-1}\) zeros. For any fixed permitted valuation \(t\in\{\lceil(a-1)/2\rceil,\ldots,a-1\}\), there are \(2^{a-t-1}\) such shifts, each with \(2^t\) frequencies, contributing another \(2^{a-1}\) zeros. There are \(\lfloor(a+1)/2\rfloor\) such valuations. This proves the rank formula. A direct two-element calculation gives the stated \(N=2\) exception.

**6. Singular values and extremal multiplicities.** The orthonormal Weyl basis \(\{\pi(k,\ell)/\sqrt N\}\) diagonalizes the operator-frame Gram form because conjugation by a Weyl shift multiplies any fixed Weyl element by a character. Consequently the lifting singular value indexed by \((k,\ell)\) is \(\sqrt N\,|\langle h,\pi(k,\ell)h\rangle|=\sqrt N|A(k,\ell)|/(N+3)\). Cauchy--Schwarz gives \(|A(k,\ell)|\le\|g\|_2^2=N+3\), with equality only when the shifted-modulated window is a scalar multiple of itself. A nontrivial translation moves the unique magnitude-two coordinate, and a nontrivial modulation cannot preserve all nonzero coordinates up to one scalar. Therefore only \((k,\ell)=(0,0)\) attains equality. The stated minimum singular values and exact condition numbers follow, including their multiplicities.

## Verification

Run `python3 verify.py` alongside `verification_output.txt` using Python 3.10+ and NumPy. It independently forms each ambiguity row by FFT from the defining window, compares a second direct quadratic-sum evaluation in ten moduli, checks all dyadic zero coordinates for powers from \(2\) to \(512\), and checks the exact odd-prime-power minima and minimizing multiplicities in fourteen cases through \(625\). In dimensions \(3,4,5,8\), a direct singular-value decomposition of the entire lifted operator is compared with the Weyl prediction. All checks passed; finite calculations are corroboration, not the proof of the unrestricted statement.

## Relationship to prior work

Salanevich's 2023 paper [1] develops explicit *multi-window* Gabor phase retrieval with fewer measurements. Its theorem has different hypotheses and does not compute one fixed cubic chirp's complete Weyl-orbit ambiguity, arithmetic rank or singular-value conditioning. Bojarovska--Flinth [2] supplies the nonvanishing-ambiguity implication used here. The published quadratic-chirp one-impulse classification [3] gives a least-modulus factor \(2\sin(\pi/(2N))\) in every odd order, whereas this cubic variant has \(2\sin(\pi/(2p^{a-1}))\) in odd prime-power dimension \(p^a\) for \(p\ge5\), \(a\ge2\); its even dyadic nullity also differs. The nearby published one-coordinate *constant* window [4] is not a cubic phase, and its complex-parameter rank discriminant does not imply these Gauss-sum branches. Li [5] studies quantitatively phase-retrievable windows and the **unperturbed** cubic chirp; its prime-power ambiguity obstruction motivates, but does not state, this exact unit-impulse remedy and sharp rank/margin classification. No priority claim is made beyond the sources actually inspected.

## Limitations

For prime \(p\ge5\) at exponent \(a=1\), the nonvanishing theorem is proved but an exact least singular value is not supplied. The theorem is restricted to a fixed cubic-phase sequence and a fixed unit impulse on prime-power cyclic groups. The odd-order phase-retrieval statement uses the *sufficient* stronger property of full linear operator tomography. The dyadic failure of linear informational completeness does not by itself settle nonlinear pure-state injectivity. Sharpness is *within this fixed window*, not a minimax optimum over all windows. Related cyclic cubic Gauss-sum observations and not-fully-indexed radar/sequence literature remain possible originality risks; independent auditing has not been performed.

## References

1. P. Salanevich, *Injectivity of Multi-window Gabor Phase Retrieval*, arXiv:2307.00834v1, first public 2023-07-03; full HTML preprint, Sections I--III.
2. I. Bojarovska and A. Flinth, *Phase Retrieval from Gabor Measurements*, arXiv:1503.05800, Sections 2--3; full preprint.
3. *Single-impulse quadratic chirps: exact cyclic Gabor tomography spectrum and arithmetic rank obstruction*, published mathematical result 2026-10-11, RESULT.md full text, identifier `03361b3cff9c`.
4. *Exact rank discriminant for one-coordinate cyclic Gabor measurements*, published mathematical result 2026-10-11, RESULT.md full text, identifier `4ad1eba7465a`.
5. D. Li, *Explicit Full-Spark and Quantitatively Phase-Retrievable Gabor Windows via Algebraic Perturbations*, arXiv:2609.09614, Section 5 concerning unperturbed cubic chirps; full preprint material inspected.
6. *A parity dichotomy for Malikiosis's quadratic-exponent Gabor window*, published mathematical result 2026-10-04, RESULT.md full text, identifier `8ac7d311b287`.
