# First flux-sensitive Schatten moments of weighted directed cycles

## Finding
For every integer \(n\ge3\), let \(W\) be the complex weighted cyclic shift on \(\mathbb C^n\) given by \(We_j=w_je_{j+1\pmod n}\). Let \(0<t<1\), \(s=1-t\), and
\[
R_\theta=t e^{i\theta}W+s e^{-i\theta}W^*,\qquad F_j(\theta)=\|R_\theta\|_{2j}^{2j}\quad(j=1,2,\ldots).
\]
Set \(k=n/\gcd(n,2)\), \(r=2k/n\in\{1,2\}\), \(Q=\prod_{j=0}^{n-1}w_j\), and \(H=\|W\|_2^2=\sum_j|w_j|^2\). Then **all the even Schatten moments of orders strictly below \(2k\) are phase-independent**, while the first potentially phase-dependent moment has the exact profile
\[
\boxed{F_k(\theta)=C_{t,W}+2n(ts)^k\operatorname{Re}(e^{2ik\theta}Q^r),}
\]
where the phase-independent constant is explicitly
\[
C_{t,W}=F_k(0)-2n(ts)^k\operatorname{Re}(Q^r).
\]
Consequently, its exact maximum-minus-minimum oscillation is
\[
\boxed{\operatorname{osc}_{\theta}F_k=4n(ts)^k|Q|^r\le4n^{1-k}(ts)^k H^k.}
\]
For \(H>0\), equality in the inequality occurs if and only if the \(n\) edge magnitudes are equal. The moment actually depends on \(\theta\) if and only if every edge weight is nonzero. Hence the first phase-sensitive even Schatten exponent is \(n\) for even cycles and \(2n\) for odd cycles. For fixed \(n,t\), the phase oscillation recovers the magnitude of the cycle product exactly by \(|Q|=[\operatorname{osc}F_k/(4n(ts)^k)]^{1/r}\).

## Assumptions and scope
The Hilbert space is \(\mathbb C^n\) with its standard Hermitian inner product. The weights are arbitrary complex numbers, including zero; the result does not assume normality, unit-modulus weights, or equal magnitudes. The integer \(j\) in \(F_j\) is positive, and the proof concerns even Schatten exponents only. The endpoint choices \(t=0,1\) are excluded from the strict phase-sensitivity and equality conclusions (all their moments are phase-independent), although the displayed identities remain valid with zero oscillation.

## Proof
Write \(u=e^{2i\theta}\). Direct multiplication gives
\[
B_\theta:=R_\theta^*R_\theta=D+ts\,uW^2+ts\,u^{-1}(W^*)^2,\qquad D=t^2W^*W+s^2WW^*.
\]
Here \(D\) is diagonal. Multiplication by \(W^2\) moves a basis vector two steps forward along the cycle, whereas multiplication by \((W^*)^2\) moves it two steps backward. In a word contributing to the expansion of \(\operatorname{Tr}(B_\theta^j)\), let \(a\) and \(b\) count factors \(W^2\) and \((W^*)^2\), respectively. A nonzero diagonal contribution requires \(2(a-b)\equiv0\pmod n\). Its phase is \(u^{a-b}\), and \(|a-b|\le j\). The least positive integer \(h\) such that \(n\mid2h\) is \(k=n/\gcd(n,2)\). Thus, for \(1\le j<k\), every surviving term has \(a=b\), and \(F_j(\theta)=\operatorname{Tr}(B_\theta^j)\) is independent of \(\theta\).

For \(j=k\), the only surviving nonconstant-phase terms have \(a-b=k\) or \(-k\); since there are exactly \(k\) positions, these are respectively the pure words \((ts\,uW^2)^k\) and \((ts\,u^{-1}(W^*)^2)^k\). The shift satisfies \(W^n=QI\), so \(W^{2k}=Q^rI\). The traces of the two pure words are \(n(ts)^k u^kQ^r\) and its complex conjugate. All other surviving words have \(a=b\) and contribute a constant \(C_{t,W}\), proving the exact harmonic identity.

The cosine term ranges over the full interval with endpoints \(\pm2n(ts)^k|Q|^r\); its oscillation is therefore \(4n(ts)^k|Q|^r\). By arithmetic-geometric mean applied to \(|w_j|^2\),
\[
|Q|^2=\prod_j|w_j|^2\le(H/n)^n.
\]
Raising this inequality to \(r/2\) yields \(|Q|^r\le(H/n)^k\). If \(H>0\), the AM--GM equality condition is precisely \(|w_0|=\cdots=|w_{n-1}|>0\). When \(Q\ne0\) and \(0<t<1\), the harmonic is nonconstant, with maximal values exactly when \(e^{2ik\theta}Q^r=|Q|^r\) and minimal values exactly when the expression equals \(-|Q|^r\). If \(Q=0\), the moment is constant. These statements establish all assertions.

## Verification
A standalone deterministic checker in `CHECK.py` constructs complex weighted cycles in dimensions \(3\) through \(10\), directly computes the traces of \((R_\theta^*R_\theta)^j\), compares them with the harmonic formula, checks lower-order phase independence, and tests the sharp equal-modulus bound. The checker is diagnostic, not an infinite-dimensional or all-parameter proof: the proof above applies to all integer dimensions and all complex weights. As direct examples, a nonzero three-cycle first shows phase dependence in the sixth Schatten moment, a nonzero four-cycle in the fourth moment, and a nonzero five-cycle in the tenth moment.

## Relationship to prior work
Pal and Chandok (arXiv:2610.11336v1, 8 October 2026) define weighted Schatten numerical radii and prove generalized-Aluthge upper inequalities, rather than the present exact phase-onset and oscillation classification for every cyclic length. Existing exact three-cycle sixth-moment and four-cycle fourth-moment optimization records cover instances of the onset and must not be misrepresented as new. Their optimization claims do not assert the full parity-dependent hierarchy for arbitrary \(n\), complex edge products, and the sharp normalized amplitude. Other existing circle-covariance results cover nilpotent shifts and hence the zero-oscillation regime. General spectral-graph closed-walk methods explain the trace mechanism; the exact weighted Schatten phase profile and sharp normalization are the specific claims here.

## Limitations
Only even integer Schatten powers are classified; no statement about the first variation at a noninteger exponent or the full operator-norm numerical-radius profile is proved. The theorem concerns a single directed cycle, not an arbitrary graph or direct sum. The amplitude determines the modulus of the edge product, not individual edge magnitudes or their phases. Earlier graph-flux trace identities might imply parts of this calculation; independent publication-priority assessment is outstanding. Numerical checks are finite and not proof substitutes.

## References
1. K. Pal and S. Chandok, *On weighted Schatten p-numerical radii via generalized Aluthge transformation*, arXiv:2610.11336v1 (8 October 2026), https://arxiv.org/html/2610.11336v1.
2. C.-T. Chang and K.-Z. Wang, *Maximizing numerical radii of weighted shifts under weight permutations*, Journal of Mathematical Analysis and Applications 394 (2012), 592–602, doi:10.1016/j.jmaa.2012.04.039. The accessible abstract concerns ordinary numerical radii, not phase-sensitive Schatten moments.
3. Relevant earlier specialized results in the mathematical research record: *Exact weighted Schatten-sixth numerical-radius minimization on a three-cycle* and *Exact weighted Schatten-fourth numerical-radius minimization on a four-cycle*. Those special cases are acknowledged as prior results, not claimed here.
