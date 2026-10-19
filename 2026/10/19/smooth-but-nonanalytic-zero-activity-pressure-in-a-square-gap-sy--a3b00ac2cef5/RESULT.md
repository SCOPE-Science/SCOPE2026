# Smooth but nonanalytic zero-activity pressure in a square-gap symbolic system

## Finding

Let \(X\subset\{0,1\}^{\mathbb Z}\) be the two-sided \(S\)-gap shift for \(S=\{1,4,9,16,\ldots\}\): between successive symbols 1 there are exactly \(m^2\) zeros for some integer \(m\ge1\). Its closure includes the all-zero sequence. Let \(\sigma\) be the left shift. For each activity \(z>0\) put
\[
P(z)=\sup_{\mu\in\mathcal M_\sigma(X)}\left(h_\mu(\sigma)+(\log z)\mu([1])\right),
\]
where entropy and pressure use natural logarithms. Then \(X\) is topologically mixing, and the equilibrium measure is unique at every \(z>0\). The pressure is the unique positive solution of
\[
\boxed{z\sum_{m=1}^{\infty}\exp\bigl(-(m^2+1)P(z)\bigr)=1.}\tag{1}
\]

Put \(A(p)=(\sqrt{\pi/p}-1)/2\). For sufficiently small \(z>0\), let \(P_{\rm an}(z)>0\) be the unique solution of
\[
\boxed{z e^{-P_{\rm an}(z)}A(P_{\rm an}(z))=1.}\tag{2}
\]
Although (2) contains a square root, \(P_{\rm an}\) extends real-analytically through \(z=0\). The actual pressure extends to a \(C^\infty\) function at \(z=0\), with precisely the same complete Taylor series as \(P_{\rm an}\), **but it is not real analytic there**. The first terms of this shared expansion are
\[
\boxed{P(z)=\frac\pi4 z^2-\frac\pi4 z^3+\left(\frac{3\pi}{16}-\frac{\pi^2}{8}\right)z^4+O(z^5).}\tag{3}
\]
Their difference is positive and **beyond every algebraic order**, with an exact leading term:
\[
\boxed{\lim_{z\downarrow0}\frac{P(z)-P_{\rm an}(z)}{4P_{\rm an}(z)\exp[-\pi^2/P_{\rm an}(z)]}=1.}\tag{4}
\]
Thus the complete perturbative expansion misses a nonzero, exponentially small arithmetic contribution. In particular, writing \(\rho(z)\) for the equilibrium frequency of the symbol 1,
\[
\boxed{\rho(z)\sim\frac\pi2z^2,\qquad h_{\mu_z}(\sigma)\sim\frac\pi2 z^2\log(1/z).}\tag{5}
\]
The asymptotic statements concern \(z\downarrow0\); no continuation of the statistical interpretation to negative activity is claimed.

## Assumptions and scope

The shift is the closure of all bi-infinite concatenations of \(10^{m^2}\), for integers \(m\ge1\). A return from one marker to the next has length \(L_m=m^2+1\); the shortest two allowed lengths are \(2\) and \(5\). Consequently \(\gcd\{L_m:m\ge1\}=1\), which implies topological mixing for this irreducible renewal shift. The potential is the locally constant function \((\log z)\mathbf1_{[1]}\) and \(z\) is its positive fugacity. The pressure is the ordinary variational topological pressure on the compact two-sided shift. Both (1) and uniqueness hold for all \(z>0\); (2)--(5) describe the boundary \(z\downarrow0\). They do not cover arbitrary return schedules, arbitrary potentials, or complex analytic continuation of pressure.

## Proof

**1. Pressure and equilibrium by return words.** For fixed \(z>0\) define
\[
R_z(p)=z\sum_{m\ge1}e^{-pL_m},\qquad L_m=m^2+1.
\]
It is finite, continuous, and strictly decreasing for \(p>0\), with limits \(+\infty\) at \(p\downarrow0\) and zero at \(p\uparrow\infty\). Hence it has a unique root \(P=P(z)>0\) satisfying \(R_z(P)=1\). Define \(q_m=z e^{-PL_m}\); these probabilities sum to one and have finite mean \(\bar L=\sum_m L_mq_m\).

Take an ergodic invariant probability \(\mu\) assigning positive mass \(\rho\) to the marker cylinder \([1]\). Poincaré recurrence and the definition of \(X\) identify its first-return process with a stationary process on the countable alphabet of lengths \(L_m\). If \(r=(r_m)\) is the one-return marginal, then Kac's formula gives \(\mathbb E_rL=1/\rho\). Abramov's entropy formula and the one-symbol entropy bound yield
\[
h_\mu(\sigma)\le\rho H(r),\qquad H(r)=-\sum_mr_m\log r_m.
\]
(The entropy is finite because \(\mathbb E_rL<\infty\) and there is only one return word of each specified length.) The Kullback--Leibler identity for \(q_m=z e^{-PL_m}\) gives
\[
H(r)+\log z-P\mathbb E_rL=-D(r\Vert q)\le0.
\]
Combining the inequalities proves \(h_\mu+(\log z)\rho\le P\). Equality requires \(r=q\) and an independent return-length process. Conversely, the independent return words with law \(q\), suspended by the finite mean \(\bar L\), determine a stationary invariant probability attaining \(P\). This is the unique ergodic maximizer. The only ergodic invariant measure of marker mass zero is the all-zero point mass, whose pressure contribution is zero, strictly less than \(P\). Ergodic decomposition extends the uniqueness conclusion to all invariant probabilities. The standard return-length gcd criterion, or concatenation of lengths 2 and 5, gives mixing.

For \(z>0\), termwise differentiability of \(R_z\) and \(\partial_pR_z<0\) show that \(P\) is real analytic in \(z\). Differentiating (1) with respect to \(\log z\) and using uniqueness of the equilibrium gives
\[
\rho(z)=zP'(z)=\left(\sum_m L_mq_m\right)^{-1}.\tag{6}
\]

**2. The exact modular decomposition.** Write
\[
\Theta(p)=\sum_{m\ge1}e^{-m^2p}.
\]
Apply the classical Poisson summation identity to the Gaussian, whose Fourier transform is \(\sqrt{\pi/p}\,e^{-\pi^2j^2/p}\). Separating the zero and positive summation indices yields, for every \(p>0\),
\[
\Theta(p)=A(p)+B(p),\qquad
A(p)=\frac12\left(\sqrt{\frac\pi p}-1\right),\quad
B(p)=\sqrt{\frac\pi p}\sum_{j\ge1}e^{-\pi^2j^2/p}.\tag{7}
\]
Thus (1) is exactly \(z e^{-P}(A(P)+B(P))=1\). In particular, \(P\sim\pi z^2/4\) as \(z\downarrow0\), since \(B(p)\) is exponentially small relative to \(A(p)\). For all sufficiently small positive \(z\), (2) has a unique solution near zero, as \(A(p)>0\) for \(0<p<\pi\) and \(e^{-p}A(p)\) decreases strictly from infinity to zero on this interval. Because \(B(p)>0\), the exact root satisfies \(P(z)>P_{\rm an}(z)\).

**3. Smoothness and nonanalyticity.** Set \(w=\sqrt p\). Equation (2) becomes
\[
2w=z e^{-w^2}(\sqrt\pi-w).\tag{8}
\]
At \((w,z)=(0,0)\) its left-minus-right side is analytic and has \(w\)-derivative 2. The analytic implicit-function theorem produces a unique analytic root \(w_0(z)\) with \(w_0(0)=0\), positive for small positive \(z\), and \(P_{\rm an}(z)=w_0(z)^2\). Expansion of (8) gives
\[
w_0(z)=\frac{\sqrt\pi}{2}z-\frac{\sqrt\pi}{4}z^2+
\left(\frac{\sqrt\pi}{8}-\frac{\pi^{3/2}}8\right)z^3+O(z^4),
\]
from which (3) follows upon squaring.

For the true root the exact modular equation, with \(w=\sqrt{P(z)}\), becomes
\[
2w=z e^{-w^2}\left(\sqrt\pi-w+E(w)\right),\qquad
E(w)=2\sqrt\pi\sum_{j\ge1}e^{-\pi^2j^2/w^2}.\tag{9}
\]
Define \(E(0)=0\), using the displayed formula for nonzero real \(w\). The sum and every derivative converge locally uniformly away from zero, and all derivatives vanish as \(w\to0\) because of Gaussian exponential bounds. Thus \(E\) is \(C^\infty\) and flat at zero. The smooth implicit-function theorem applies to (9) near \((0,0)\), again with derivative 2, and constructs a \(C^\infty\) branch \(w(z)\). For positive small \(z\) this is the positive root of (1); consequently \(w(z)^2\) gives a smooth extension of \(P\) through zero. Formal differentiation of (9) and flatness of \(E\) show that the Taylor series of \(w\) coincides term by term with that of \(w_0\). The Taylor series of \(P\) and \(P_{\rm an}\) therefore coincide to all orders. However \(P(z)>P_{\rm an}(z)\) for every sufficiently small positive \(z\). An analytic function cannot differ from an analytic function while having all Taylor coefficients equal at the same point. Hence \(P\) is not real analytic at zero.

**4. Sharp size of the flat correction.** Denote \(p_0=P_{\rm an}(z)\), \(s=\sqrt{\pi/p_0}\), and \(F_0(p)=ze^{-p}A(p)\). Then \(F_0(p_0)=1\) and direct differentiation gives
\[
-F_0'(p_0)=\frac{s-1+s/(2p_0)}{s-1}.\tag{10}
\]
From (7), uniformly as \(p_0\downarrow0\),
\[
B(p_0)=s e^{-\pi^2/p_0}\bigl(1+O(e^{-3\pi^2/p_0})\bigr).\tag{11}
\]
Write \(\delta=P-p_0\). A monotonicity comparison of the exact root equation at \(p_0\) and at \(p_0+C p_0e^{-\pi^2/p_0}\), with any fixed \(C>4\), first gives \(0<\delta=O(p_0e^{-\pi^2/p_0})\). This bound and termwise differentiation of (7) show that the derivatives of \(ze^{-p}B(p)\) are exponentially negligible compared with \(-F_0'(p_0)\) throughout this interval. The mean-value theorem therefore yields
\[
\delta=\frac{ze^{-p_0}B(p_0)}{-F_0'(p_0)}\,(1+o(1)).
\]
Using \(ze^{-p_0}=2/(s-1)\) and (10)--(11), we obtain the more precise form
\[
\delta=\frac{4p_0}{1+2p_0-2p_0^{3/2}/\sqrt\pi}\,
 e^{-\pi^2/p_0}(1+o(1)).\tag{12}
\]
Since \(p_0\downarrow0\), this proves (4), including its positive sign. The exponentially small term is nonzero for every positive activity; no finite Taylor truncation in \(z\) can recover it.

**5. Marker density and entropy.** By (6) and (7),
\[
\sum_m m^2q_m=\frac{-\Theta'(P)}{\Theta(P)}\sim\frac1{2P},
\]
so \(\rho(z)\sim2P(z)\sim\pi z^2/2\). The equilibrium variational identity \(P=h_{\mu_z}+(\log z)\rho(z)\) then gives \(h_{\mu_z}\sim(\pi/2)z^2\log(1/z)\), establishing (5).

## Verification

The standalone `verify.py` evaluates (1) using direct finite Gaussian sums at 155 decimal digits, independently checks the Jacobi-dual expression (7), differentiates the pressure numerically to confirm (6), and checks the approach to the ratio in (4). Its observed output is

`VERIFY_OK: 4 renewal normalizations; 4 Jacobi-dual checks; 4 pressure-density checks; 4 beyond-all-orders ratios; mixing gcd`

At activities \(z=1,0.75,0.5,0.35\), the ratios on the left side of (4) were approximately \(0.73735610,0.78582762,0.85258563,0.90289804\). The direct summation truncation has exponentially bounded tails; the code is a finite numerical diagnostic. None of the infinite assertions, exact root existence, smoothness, or historical originality rests on these finite checks. Reproduction: run `python3 verify.py` with the freely available Python package `mpmath`.

## Relationship to prior work

Baker and Ghenciu, arXiv:1411.7167v1 (first public November 26, 2014), define \(S\)-gap shifts and record the general topological-entropy renewal equation (Proposition 2.1), as well as the unbounded-gap obstruction to the uniform Gibbs property (Corollary 3.16). Dastjerdi and Jangjoo, arXiv:1108.3242v1, establish structural and mixing/soficity criteria for \(S\)-gap shifts. Those results supply standard background and do not state (4) or the smooth-but-nonanalytic activity boundary. The present proof uses the established inducing principle, not a newly claimed general pressure equation.

A published mathematical research result entitled *Log-periodic second-order entropy law for geometric gap shifts* (2026, record ending `166969f68799`) treats allowed **geometrically spaced return distances** and fixed marker density; its oscillatory small-density term is not an instance of the square-gap pressure law (4). The separate published *Nonconstant discrete-scale pressure profile for dyadic interspersion shifts* (2026, record ending `818c7b0279b9`) studies a dyadic-lacunary schedule with free filler symbols and a doubly exponential rare-marker scale. Its hypotheses do not include square-gap return lengths or imply a Jacobi flat correction. These full result statements were compared by object, observable, regime, and conclusion, not by title alone.

Poisson summation and the Jacobi transformation of the Gaussian are classical analytic identities. Their use in (7) is explicitly credited; the proposed new mathematical fact is the combined **pressure smoothness/nonanalyticity classification and the exact positive beyond-all-orders coefficient (4)** for this natural symbolic system, with (5) as a statistical consequence. An older or not indexed treatment of theta-series renewal pressure could still subsume the result; independent historical-priority assessment is not claimed.

## Limitations

The arithmetic identity and asymptotic (4) are specific to the return schedule \(L_m=m^2+1\); no analogue is asserted for arbitrary \(S\)-gap shifts. The pressure is analytic for every strictly positive activity; the nonanalyticity concerns its smooth extension at the zero-activity boundary only. The smooth extension to negative real \(z\) used in the proof is formal and is not a thermodynamic equilibrium construction there. The usual \(S\)-gap uniform Gibbs property fails for this unbounded-gap set, notwithstanding existence and uniqueness of the equilibrium measure for this particular locally constant potential. Published-priority comparisons cannot exclude unindexed or inaccessible equivalent calculations. No independent audit has been performed.

## References

1. S. Baker and A. E. Ghenciu, *Dynamical properties of S-gap shifts and other shift spaces*, arXiv:1411.7167v1 (November 26, 2014); J. Math. Anal. Appl. 430 (2015), 633–647. https://arxiv.org/abs/1411.7167
2. D. Ahmadi Dastjerdi and S. Jangjoo, *Dynamics and topology of S-gap shifts*, arXiv:1108.3242v1 (August 2011). https://arxiv.org/abs/1108.3242
3. *Log-periodic second-order entropy law for geometric gap shifts*, published result record, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-log-periodic-second-order-entropy-law-for-geometric-gap-shifts--166969f68799
4. *Nonconstant discrete-scale pressure profile for dyadic interspersion shifts*, published result record, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-nonconstant-discrete-scale-pressure-profile-for-dyadic-intersper--818c7b0279b9
5. Classical Poisson summation theorem and Jacobi Gaussian theta transformation (standard identity, proved by applying Poisson summation to the Gaussian as recalled above).
