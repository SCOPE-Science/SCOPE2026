# Dini roofs retain local product structure for full-shift suspensions
## Finding
Let \(\Sigma=\{0,1\}^{\mathbb Z}\) carry the full-shift metric used by Wen,
\[
d(a,b)=\frac{1}{3}\sum_{i\in\mathbb Z}\frac{|a_i-b_i|}{2^{|i|}},
\]
and let \(\sigma\) be the shift. Let \(\tau:\Sigma\to(0,\infty)\) be continuous. Write
\[
\omega(r)=\sup\{|\tau(x)-\tau(y)|:d(x,y)\le r\}
\]
for its modulus of continuity and suppose
\[
\int_0^1\frac{\omega(r)}{r}\,dr<\infty.
\]
Then the suspension flow over \((\Sigma,\sigma)\) with roof \(\tau\), equipped with the Bowen--Walters metric, has local product structure.

Define the dyadic tail
\[
\Omega(r)=\sum_{n=0}^{\infty}\omega(2^{-n}r).
\]
The Dini hypothesis implies \(\Omega(r)<\infty\) for every \(r>0\) and \(\Omega(r)\to0\) as \(r\downarrow0\). In Wen's Hölder proof, the quantity \(Lr^{\alpha}/(1-2^{-\alpha})\) can therefore be replaced by \(\Omega(r)\). The result strictly enlarges the Hölder class; for example, moduli comparable to \((\log(e/r))^{-1-\eta}\), with \(\eta>0\), are Dini but need not be Hölder.

Wen's explicit logarithmic counterexample sits outside this sufficient class. At the fixed point its roof variation is of order \(1/\log(1/r)\), so the corresponding dyadic tail is harmonic and diverges. This is the same divergence that destroys the stable and unstable time corrections in the source proof.

## Assumptions and scope
The statement concerns the full two-symbol shift and Wen's Bowen--Walters suspension model. The roof is positive and continuous on the compact base, so
\[
m=\min_{x\in\Sigma}\tau(x)>0,\qquad K=\max_{x\in\Sigma}\tau(x)<\infty.
\]
The conclusion is local product structure in the precise sense used in the source: sufficiently close suspension points have a unique small-time translate whose local stable set meets the local unstable set in exactly one point.

The Dini condition is only asserted as a sufficient condition. It is not claimed to be necessary; in particular, non-Dini roofs may have local product structure for other reasons, such as continuous cohomology to a regular roof.

## Proof
First, the Dini integral controls dyadic variation. Since \(\omega\) is nondecreasing, on every interval \([2^{-(n+1)}r,2^{-n}r]\),
\[
\omega(2^{-(n+1)}r)\log 2
\le
\int_{2^{-(n+1)}r}^{2^{-n}r}\frac{\omega(s)}{s}\,ds
\le
\omega(2^{-n}r)\log 2.
\]
Hence the Dini integral is finite only if \(\Omega(r)\) is finite. Applying the same comparison to the tail beginning at a large dyadic index, and then letting \(r\downarrow0\), gives \(\Omega(r)\to0\).

We now revisit the two estimates on which Wen's Hölder proof depends.

For the necessity direction for local stable sets, choose \(\varepsilon_0>0\) so small that
\[
\omega(2\varepsilon_0)+K\varepsilon_0<\frac{m}{2}.
\]
The induction in Wen's Lemma 3.1 uses Hölder regularity only through the estimate
\[
|\tau(a)-\tau(b)|\le Ld(a,b)^{\alpha}.
\]
Replacing it by \(|\tau(a)-\tau(b)|\le\omega(d(a,b))\) gives the same interior-return induction. Thus a point in a sufficiently small suspension stable set projects to a point in the corresponding local stable set of the shift, and its vertical coordinate must equal
\[
t=\frac{\tau(b)}{2}+
\sum_{n=0}^{\infty}\bigl(\tau(\sigma^n a)-\tau(\sigma^n b)\bigr).
\]
The analogous backward formula holds for local unstable sets.

For the converse direction, if \(a\) belongs to a sufficiently small local stable set of \(b\), then the full-shift geometry used in the source gives
\[
d(\sigma^n a,\sigma^n b)\le 2^{-n}d(a,b).
\]
Therefore the time correction converges absolutely and its tail satisfies
\[
\left|\sum_{k=n}^{\infty}\bigl(\tau(\sigma^k a)-\tau(\sigma^k b)\bigr)\right|
\le
\Omega(2^{-n}d(a,b)).
\]
The Bowen--Walters chain estimate from Wen's Lemma 3.2 becomes
\[
\rho\bigl(\psi_{t_n}(a,s),\psi_{t_n}(b,t)\bigr)
\le
d(\sigma^n a,\sigma^n b)+\frac{\Omega(2^{-n}d(a,b))}{m},
\]
which tends to zero. Uniform local closeness follows by choosing the base scale \(\epsilon\) so that
\[
\epsilon+\frac{\Omega(\epsilon)}{m}
\]
is smaller than the continuity scale required for flow times in \([-K,K]\). The unstable statement follows identically backward in time.

Finally, use the local product point \(c\) in the full shift exactly as in Wen's proof. The required suspension time displacement \(\theta\) is the sum of one midpoint error and one stable and one unstable roof tail. If \(d(a,b)\), \(d(a,c)\), and \(d(b,c)\) are bounded by \(\epsilon\), then
\[
|\theta|
\le
\frac{K}{2}\epsilon+rac{1}{2}\omega(\epsilon)+2\Omega(\epsilon).
\]
Because both \(\omega(\epsilon)\) and \(\Omega(\epsilon)\) tend to zero, this can be made smaller than any prescribed local-product time scale. Existence follows from the stable and unstable constructions above. Uniqueness is unchanged from Wen's argument: the generalized stable/unstable coordinate formulas project any two candidate intersections to the unique local product point of the full shift, and then the vertical coordinate is forced.

Thus the suspension has local product structure.

## Verification
The proof is a statement-level replacement of the only quantitative regularity estimates in Wen's Section 3. The source's Lemma 3.1 uses Hölder continuity to keep successive suspension representatives inside their roof intervals; continuity with modulus \(\omega\) supplies the same estimate once \(\omega(2\varepsilon)+K\varepsilon<m/2\). The source's Lemma 3.2 and final local-product construction use the geometric series
\[
\sum_{n\ge0}L(2^{-n}r)^{\alpha};
\]
Dini continuity supplies the finite vanishing replacement \(\Omega(r)\).

No finite experiment is used. The argument proves sufficiency for every positive Dini roof on this full-shift model. It does not establish necessity of the Dini condition.

For the source counterexample,
\[
\tau(a)=1+\frac{1}{-\log d(a,\underline 0)+1}
\]
away from \(\underline 0\), with \(\tau(\underline 0)=1\). Along dyadic approach to \(\underline 0\), the roof difference is comparable to \(1/n\); hence the stable-time series is harmonic. This agrees with the source's direct divergence calculation.

## Relationship to prior work
Xiao Wen proves that every Hölder positive roof over the full two-symbol shift gives a suspension flow with local product structure, while also constructing a continuous non-Hölder logarithmic roof whose suspension fails local product structure. Inspection of the full proof shows that the Hölder hypothesis is used quantitatively through geometric summability of stable and unstable roof differences. The present result replaces power-law summability by the strictly weaker Dini summability condition.

A published finding concerning the same counterexample proves a cohomological obstruction for Wen's logarithmic roof and notes that some non-Hölder roofs can nevertheless have local product structure. That statement does not supply a broad Dini sufficient class and does not imply the theorem here. Searches using Dini, summable-modulus, summable-variation, Walters, stable-holonomy, and suspension terminology located no implication-equivalent local-product theorem for Wen's model.

## Limitations
Dini continuity is not claimed to be necessary. The result is restricted to the full-shift suspension geometry used by Wen; extending the same criterion to more general symbolic bases or arbitrary expansive flows with shadowing would require separate control of the base contraction and product map. The novelty search cannot rule out an equivalent theorem under unindexed or different terminology.

## References
1. Xiao Wen, “Local Product Structure of Expansive Flows with Shadowing Property,” arXiv:2608.26561v1, first public 2026-08-27; especially Theorems 1.1 and 1.2, Lemmas 3.1 and 3.2, and the proof of Theorem 1.2.
2. R. Bowen and P. Walters, “Expansive one-parameter flows,” Journal of Differential Equations 12 (1972), 180–193, for the suspension metric used in the source.
