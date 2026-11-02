# Every higher critical valuation occurs in the fifteenth-column Stirling difference

## Finding
Let \(S(n,k)\) be the Stirling number of the second kind, let \(\nu_2\) be the exponent of \(2\) in a nonzero integer, and fix integers \(N\ge10\), \(b\ge1\). Set
\[
H=b2^N-5,\qquad e=b2^N-N-6=H-N-1.
\]
For positive odd integers \(u\), put
\[
D(u)=S\bigl((b+2^eu)2^N,15\bigr)-S(b2^N,15).
\]
**Critical valuation-spectrum theorem:** The set of exact valuations \(\nu_2(D(u))\), as \(u\) ranges over positive odd integers, is precisely
\[
\{H+t:t\in\mathbb Z,\ t\ge1\}.
\]
There is a unique odd \(2\)-adic number \(\rho\) defined below, such that for every \(t\ge1\), every sufficiently large positive odd \(u\) satisfying \(u\equiv\rho+2^t\pmod{2^{t+1}}\) obeys \(\nu_2(D(u))=H+t\). Thus at the critical exponent the cancellation can be arbitrarily deep, and *every* possible depth occurs. Neither \(N=10\) nor the restriction to this column is asserted sharp.

## Assumptions and scope
The ring of two-adic integers is \(\mathbb Z_2\), and \(z^u\) for \(z\in1+4\mathbb Z_2\), \(u\in\mathbb Z_2\), denotes the unique continuous extension from integer powers. All Stirling indices in the theorem are positive integers. The main statement concerns the precisely defined critical slice \(a=b+2^eu\) with \(u\) odd; no claim is made about noncritical slices.

## Proof
**1. Odd/even decomposition.** Since the second index is odd, inclusion-exclusion gives for positive integers \(n\)
\[
15!S(n,15)=\sum_{j=1}^{15}(-1)^{15-j}\binom{15}{j}j^n.
\]
Write \(S(n,15)=O(n)+E(n)\), where \(O\) sums odd \(j\) with positive signs and \(E\) sums even \(j\) with negative signs, both divided by \(15!\). Each summand is in \(\mathbb Q_2\); their sum is the integer \(S(n,15)\). Since \(\nu_2(15!)=11\), it suffices to determine the numerator valuations.

**2. Uniform even-base valuation.** For every positive \(n\) divisible by \(16\), collect even bases \(j=2,6,10,14\):
\[
-15!E(n)=2^n\bigl(T(n)+2^nU(n)\bigr),
\quad T(n)=105+5005\cdot3^n+3003\cdot5^n+15\cdot7^n,
\]
where \(U(n)\in\mathbb Z\) represents the remaining bases \(4,8,12\). Modulo \(128\), for \(16\mid n\), the powers satisfy \(3^n\equiv5^n\equiv1+64(n/16)\), \(7^n\equiv1\). Since \(105+5005+3003+15=8128\equiv64\pmod{128}\) and \(5005+3003\) is even, we get \(T(n)\equiv64\pmod{128}\). The term \(2^nU(n)\) vanishes modulo \(128\). Consequently
\[
\nu_2(E(n))=n+6-11=n-5.
\]
This includes \(n=b2^N\), where \(E(n)/2^H\) is an odd \(2\)-adic integer.

**3. An isometric odd-base map.** For odd \(j\) and \(r\ge10\), define the integers
\[
Q_j(r)=(j^{2^r}-1)/2^{r+2}.
\]
The recurrence \(Q_j(r+1)=Q_j(r)+2^{r+1}Q_j(r)^2\) shows \(Q_j(r)\equiv Q_j(10)\pmod{2048}\). Direct repeated squaring modulo \(2^{23}\) gives the following exact residues (in order \(j=3,5,7,9,11,13,15\)):
\[
(Q_j(10)\bmod2048)=(573,415,374,1146,1355,1137,988).
\]
Multiplying by \(\binom{15}{j}\) and summing gives precisely \(1024\pmod{2048}\). Also \(j^{b2^N}\equiv1\pmod{2048}\), and for every odd integer \(w\), binomial expansion yields
\[
\frac{j^{w2^r}-1}{2^{r+2}}\equiv wQ_j(r)\pmod{2048},\qquad r\ge10.
\]
The same holds for negative odd \(w\) by inversion in \(1+4\mathbb Z_2\). Therefore, for every nonzero integer \(h\), writing \(r=N+\nu_2(h)\ge10\),
\[
\nu_2\bigl(O((b+h)2^N)-O(b2^N)\bigr)=N+\nu_2(h)+1,
\]
provided the odd-base powers are interpreted \(2\)-adically if \(b+h\le0\). The computation is: odd-part numerator has valuation \(r+2+10=r+12\), followed by division by \(15!\) of valuation \(11\). By continuity this is a metric identity for all \(2\)-adic index shifts.

Define, for \(u\in\mathbb Z_2\),
\[
\Phi(u)=\frac{O((b+2^eu)2^N)-O(b2^N)}{2^H},
\]
using continuous odd-base interpolation. Since \(e=H-N-1\), the preceding identity gives
\[
\nu_2(\Phi(u)-\Phi(v))=\nu_2(u-v)
\quad(u\ne v\in\mathbb Z_2),\qquad\Phi(0)=0.
\]
Thus \(\Phi\) is an isometry from \(\mathbb Z_2\) to itself. For every \(t\), it maps distinct residues modulo \(2^t\) to distinct residues modulo \(2^t\); hence it is bijective modulo every \(2^t\) and, by compactness, onto \(\mathbb Z_2\). This establishes a bijective nonlinear Hensel lifting map, not merely an existence bound.

**4. The unique critical center and every valuation.** Put \(\eta=E(b2^N)/2^H\in\mathbb Z_2^\times\). Surjectivity and injectivity supply a unique \(\rho\in\mathbb Z_2\) satisfying \(\Phi(\rho)=\eta\). Since \(\Phi(u)\equiv u\pmod2\), it follows that \(\rho\) is odd. For an odd positive integer \(u\), put \(a=b+2^eu\). Then
\[
\frac{D(u)}{2^H}=\Phi(u)-\eta+\frac{E(a2^N)}{2^H},
\qquad\nu_2\bigl(E(a2^N)/2^H\bigr)=u2^{N+e}.
\]
The first term \(\Phi(u)-\eta\) is even because both values are odd, and the last term is even. Therefore \(\nu_2(D(u))\ge H+1\) for every positive odd \(u\). Conversely, for any \(t\ge1\), choose any positive odd \(u\equiv\rho+2^t\pmod{2^{t+1}}\) with \(u2^{N+e}>t\), possible by adding sufficiently large multiples of \(2^{t+1}\). Then the isometry gives \(\nu_2(\Phi(u)-\eta)=t\), while the even-base remainder has larger valuation, so \(\nu_2(D(u))=H+t\). This proves the exact infinite spectrum and its residue-class construction.

## Verification
The companion `verify.py` uses the exact finite Stirling inclusion-exclusion identity with modular exponentiation, never floating point, and checks the seven odd-base residues, the even-base congruence, and 28 exact critical valuation witnesses at \((N,b)=(10,1),(10,2),(11,1),(11,2)\). The script independently derives each \(S(n,15)\bmod2^h\) by dividing its numerator by the known \(2^{11}\) factor of \(15!\) and inverting the remaining odd factorial. Exhaustive finite checks are **not** presented as a proof for unbounded \(t\); Steps 2–4 establish the unrestricted claim.

## Relationship to prior work
Lengyel's 2009 treatment formulated the Stirling-difference valuation question; Zhao, Zhao and Hong (2014, Theorem 1.2) established a three-way valuation law for columns \(3\) and \(7\), leaving the general higher Mersenne case outside their theorem. The present assertion is **not** that an off-resonance valuation rule is new: it is an exact classification of *every attainable higher valuation* at the critical slice of the first higher Mersenne column, together with a canonical isometric \(2\)-adic center. Bennett and Mosteig (2013) classify valuation behavior of individual Stirling numbers on congruence classes, a different invariant; related methods deserve further comparison.

## Limitations
Only the critical \(k=15\) slice for \(N\ge10\) is classified, and the threshold is not claimed sharp. The center is uniquely specified by an explicit continuous map rather than given in a simple closed formula. The proof gives residue-class constructions of arbitrary depth, not a global pointwise formula in all noncritical parameters. Historical-priority completeness is not certified; independent verification remains outstanding.

## References
1. T. Lengyel, *On the 2-adic order of Stirling numbers of the second kind and their differences*, FPSAC 2009, https://dmtcs.episciences.org/en/articles/2694.
2. W. Zhao, J. Zhao, S. Hong, *The 2-adic valuations of differences of Stirling numbers of the second kind*, arXiv:1407.8443 (first posted 2014-07-31), https://arxiv.org/abs/1407.8443.
3. C. Bennett, E. Mosteig, *Congruence Classes of 2-adic Valuations of Stirling Numbers of the Second Kind*, Journal of Integer Sequences 16 (2013), Article 13.3.6, https://www.maths.tcd.ie/EMIS/journals/JIS/VOL16/Mosteig/mosteig4.pdf.
