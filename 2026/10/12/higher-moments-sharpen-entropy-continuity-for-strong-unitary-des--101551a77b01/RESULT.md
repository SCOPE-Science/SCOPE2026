# Higher moments sharpen entropy continuity for strong unitary designs
## Finding
Let \(N=2^n\). Let \(\mu\) be a strong \(\varepsilon\)-approximate unitary \((k,k)\)-design with \(0\le\varepsilon\le1\), fix an input computational-basis state \(y\), and write
\[
P_x(U)=|\langle x|U|y\rangle|^2,\qquad S(U)=-\sum_x P_x(U)\log_2 P_x(U).
\]
Assume that for every output \(x\), the marginal law of \(P_x\) under \(\mu\) has Kolmogorov distance at most \(\eta\le1/2\) from its Haar law \(\operatorname{Beta}(1,N-1)\). For every even integer \(q\) with \(2\le q\le2k\), define
\[
R_{N,q}=\frac{N^{q-1}}{(N+1)(N+2)\cdots(N+q-1)}.
\]
Then
\[
\left|\mathbb E_\mu S-\mathbb E_{\mathrm{Haar}}S\right|
\le
\frac{2q}{e(q-1)\ln2}\,\eta^{1-1/q}
\left(\frac{(2+\varepsilon)q!R_{N,q}}{2}\right)^{1/q}.
\]
For \(\eta=0\), the entropy gap is zero.

In particular, if \(0<\eta\le e^{-2}\) and \(k\ge\lceil\ln(1/\eta)/2\rceil\), choose the least even integer \(q\ge\ln(1/\eta)\). Then
\[
\left|\mathbb E_\mu S-\mathbb E_{\mathrm{Haar}}S\right|
\le 15\eta\ln(1/\eta).
\]
Combining this with the generic marginal estimate in Hung's arXiv:2610.02135v1 gives, in the regime \(k\ll2^n\), the sufficient scale \(k=\Theta(n^2(\ln n)^2)\) and \(\varepsilon=O(n^{-2})\) for an expected entropy gap \(O(1/n)\). The source states the sufficient generic scale \(O(n^4)\) when its square-root entropy-continuity estimate is used.

## Assumptions and scope
The result concerns the ensemble-averaged Shannon entropy of computational-basis outcomes for a fixed input basis state. The design notion is the strong relative-error \((k,k)\)-design used in arXiv:2610.02135v1. The only distributional hypothesis beyond that design condition is a uniform marginal Kolmogorov bound \(\eta\) for the individual output probabilities. The proof uses even moments up to order \(2k\); it makes no claim about entropy concentration around its mean, adversarially correlated repeated samples, certification, or ordinary additive-error designs.

## Proof
Hung's entropy decomposition introduces a cutoff \(B/N\) and functions \(\phi_B^+\) and \(\phi_B^-\) satisfying
\[
S(P)=\log_2(N/B)+\sum_x\phi_B^+(P_x)-\sum_x\phi_B^-(P_x).
\]
The positive truncated contribution has interval superlevel sets and \(\|\phi_B^+\|_\infty=B/(Ne\ln2)\). The marginal Kolmogorov hypothesis therefore gives
\[
\left|\mathbb E_\mu\sum_x\phi_B^+(P_x)-\mathbb E_{\mathrm{Haar}}\sum_x\phi_B^+(P_x)\right|
\le\frac{2\eta B}{e\ln2}.
\]

For the tail, write \(z=Np/B\ge1\). For every \(q>1\),
\[
\ln z\le\frac{z^{q-1}}{e(q-1)},
\]
because the maximum of \(\ln z/z^{q-1}\) over \(z\ge1\) is \(1/(e(q-1))\). Hence
\[
\phi_B^-(p)=p\log_2(Np/B)
\le\frac{N^{q-1}p^q}{e(q-1)B^{q-1}\ln2}.
\]
For the Haar marginal,
\[
\mathbb E_{\mathrm{Haar}}[P_x^q]
=\frac{q!}{N(N+1)\cdots(N+q-1)}.
\]
Now take \(q=2r\) even with \(r\le k\). The strong-design squared-polynomial estimate applied to the polynomial \(p(t)=t^r\) gives
\[
\mathbb E_\mu[P_x^q]\le(1+\varepsilon)\mathbb E_{\mathrm{Haar}}[P_x^q].
\]
Summing the tail bound over \(x\) under both measures yields
\[
\mathbb E_\mu\sum_x\phi_B^-(P_x)+\mathbb E_{\mathrm{Haar}}\sum_x\phi_B^-(P_x)
\le
\frac{(2+\varepsilon)q!R_{N,q}}{e(q-1)B^{q-1}\ln2}.
\]
Therefore, for every \(B>0\),
\[
\left|\mathbb E_\mu S-\mathbb E_{\mathrm{Haar}}S\right|
\le\frac1{e\ln2}
\left(2\eta B+\frac{(2+\varepsilon)q!R_{N,q}}{(q-1)B^{q-1}}\right).
\]
For \(\eta>0\), differentiation gives the minimizing cutoff
\[
B^q=\frac{(2+\varepsilon)q!R_{N,q}}{2\eta},
\]
which gives the displayed bound. If \(\eta=0\), the marginal laws agree exactly and the expected entropy, being a sum of marginal expectations, agrees exactly as well.

For the near-linear corollary, use \(R_{N,q}\le1\), \(\varepsilon\le1\), and \((q!)^{1/q}\le q\). This gives
\[
\left|\mathbb E_\mu S-\mathbb E_{\mathrm{Haar}}S\right|
\le\frac{4\sqrt{3/2}}{e\ln2}\,q\eta^{1-1/q}.
\]
Let \(L=\ln(1/\eta)\ge2\) and choose \(q=2\lceil L/2\rceil\). Then \(L\le q\le2L\) and \(\eta^{-1/q}\le e\), so the right-hand side is at most
\[
\frac{8\sqrt{3/2}}{\ln2}\,\eta L<15\eta L.
\]
Finally, Hung's generic marginal bound is \(\eta=O(\sqrt{N/(k(k+N))}+\varepsilon)\). For \(N=2^n\) and \(k=\Theta(n^2(\ln n)^2)\ll N\), with \(\varepsilon=O(n^{-2})\), this is \(\eta=O(1/(n\ln n))\). The near-linear entropy bound is therefore \(O(1/n)\).

## Verification
The proof is analytic. The accompanying script `artifacts/verify.py` checks the optimized-cutoff algebra, the \(q=2\) reduction, the exact Haar moment factor \(R_{N,q}\), and the numerical constant in the \(15\eta\ln(1/\eta)\) corollary over representative dimensions and even moments. These finite computations corroborate, but do not replace, the inequalities proved above.

## Relationship to prior work
Hung, arXiv:2610.02135v1, proves the marginal Kolmogorov estimate for strong approximate designs and then derives a dimension-free expected Shannon-entropy bound of order \(O(\sqrt\eta)\) by controlling the large-probability tail with the second moment. The paper explicitly states the resulting sufficient generic design-order scale \(O(n^4)\) for \(O(1/n)\) expected entropy error. Its strong-design polynomial estimate, however, controls higher even moments as well. The finding above uses those already available higher moments in the same cutoff argument, yielding a family of \(\eta^{1-1/q}\) bounds and the near-linear \(O(\eta\ln(1/\eta))\) consequence.

The source also proves exponentially better marginal approximation under local unitary invariance, leading to a much smaller design order, but that result has an additional structural hypothesis and therefore does not cover the generic-design statement here. General work on unitary designs and random circuits supplies design constructions and moment control, while the searched literature did not identify a prior statement combining the source's marginal Kolmogorov estimate with higher design moments to obtain this entropy bound or the resulting \(n^2(\ln n)^2\) sufficient generic order scale. A 2007 paper by Zhang concerns bounds on mutual information for finite discrete variables in terms of Kolmogorov/variation-type distances; its accessible description does not address output-probability marginals of unitary designs or matched high moments.

## Limitations
This is a sufficient bound, not a lower bound on the design order needed for high expected entropy. The asymptotic resource corollary uses the hidden constants in Hung's \(O(\cdot)\) marginal estimate and therefore asserts an asymptotic scale rather than a finite numerical threshold. The result does not improve the source's stronger locally invariant regime. Literature searches cannot exclude an equivalent statement hidden under different terminology; the closest unresolved risk is a general probability inequality that may imply a comparable interpolation bound when specialized to beta marginals and matched moments.

## References
1. Shih-Han Hung, “Random Quantum Circuits Beyond Moment Matching,” arXiv:2610.02135v1, first submitted 1 October 2026. See Definition 2.2, Theorem 3.2, Theorem 1.1, Theorem 1.4, and Theorem 7.2.
2. Fernando G. S. L. Brandão, Aram W. Harrow, and Michał Horodecki, “Local Random Quantum Circuits are Approximate Polynomial-Designs,” Communications in Mathematical Physics 346 (2016), 397–434, DOI:10.1007/s00220-016-2706-8.
3. Zhengmin Zhang, “Estimating Mutual Information via Kolmogorov Distance,” IEEE Transactions on Information Theory 53 (2007), 3280–3282, DOI:10.1109/TIT.2007.903122.
