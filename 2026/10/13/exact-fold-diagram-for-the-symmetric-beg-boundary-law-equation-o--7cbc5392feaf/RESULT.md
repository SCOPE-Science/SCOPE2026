# Exact fold diagram for the symmetric BEG boundary-law equation on Cayley trees
## Finding
For the zero-field Blume--Emery--Griffiths model considered by Botirov, Haydarov and Qayumov, restrict the translation-invariant boundary-law system to the symmetric branch \(z=t\) on a Cayley tree of integer order \(k\ge 2\). With \(s=z^{1/k}>0\), \(\xi=e^\beta>1\),
\[
c_1=2\xi^b>0,\qquad c_2=\xi^{a+b-1}(1+\xi^2)>0,
\]
the source equation is exactly
\[
P(s)=c_1s^{k+1}-c_2s^k+s-1=0.
\]
Set
\[
\rho=\frac{k-1}{k+1},\qquad c_1^*=\rho^{k+1},\qquad c_2^*=\rho^{k-1},\qquad s^*=\frac{k+1}{k-1}.
\]
If \(c_1\ge c_1^*\), then for every \(c_2>0\) there is exactly one positive root. At \((c_1,c_2)=(c_1^*,c_2^*)\), that unique root is \(s=s^*\) and has multiplicity exactly three.

If \(0<c_1<c_1^*\), let \(s_-<s_+\) be the two positive roots of
\[
c_1s^{k+1}-(k-1)s+k=0.
\]
Then \(k/(k-1)<s_-<s^*<s_+\). Define
\[
c_2^{\rm hi}=\frac{ks_--(k+1)}{s_-^k},\qquad
c_2^{\rm lo}=\frac{ks_+-(k+1)}{s_+^k}.
\]
These satisfy \(0<c_2^{\rm lo}<c_2^{\rm hi}\). The equation \(P(s)=0\) has exactly three distinct positive roots when \(c_2^{\rm lo}<c_2<c_2^{\rm hi}\), exactly two distinct positive roots with one double root when \(c_2\) equals either fold value, and exactly one positive root otherwise.

Equivalently, the two fold branches admit the exact parameterization
\[
c_1(s)=\frac{(k-1)s-k}{s^{k+1}},\qquad
c_2(s)=\frac{ks-(k+1)}{s^k},\qquad s>\frac{k}{k-1},
\]
and meet at the triple-root cusp \((c_1^*,c_2^*)\). Thus the source's positive-coefficient symmetric branch has a complete sharp one-versus-three phase diagram for every \(k\ge2\).

## Assumptions and scope
The statement concerns only the symmetric translation-invariant branch \(z=t\) of the source's zero-field boundary-law system. The coefficients \(c_1,c_2\) are positive and every positive pair is realizable by real model parameters for any fixed \(\xi>1\): one may take
\[
b=\log_\xi(c_1/2),\qquad a=1-b+\log_\xi\!\left(\frac{c_2}{1+\xi^2}\right).
\]
Each positive root corresponds to a positive symmetric boundary law \(z=t=s^k\), hence to a translation-invariant splitting Gibbs measure through the source's compatibility theorem. No assertion is made about nonsymmetric translation-invariant boundary laws, periodic boundary laws, extremality, free energies, or thermodynamic dominance.

## Proof
Solve the polynomial equation for \(c_2\):
\[
c_2=q(s):=c_1s+\frac{s-1}{s^k},\qquad s>0.
\]
Its derivative is
\[
q'(s)=\frac{H(s)}{s^{k+1}},\qquad H(s)=c_1s^{k+1}-(k-1)s+k.
\]
The function \(H\) is strictly convex and has one critical point
\[
s_0=\left(\frac{k-1}{(k+1)c_1}\right)^{1/k}.
\]
At this point,
\[
H(s_0)=k\left(1-\frac{k-1}{k+1}s_0\right).
\]
Hence \(H\ge0\) on \((0,\infty)\) exactly when \(c_1\ge\rho^{k+1}\). In that regime \(q\) is increasing, with at most one stationary point in the equality case, while \(q(s)\to-\infty\) as \(s\downarrow0\) and \(q(s)\to+\infty\) as \(s\to\infty\). Therefore every horizontal level \(c_2>0\) is met exactly once.

At \(c_1=c_1^*\), the stationary point is \(s^*=(k+1)/(k-1)\), and direct substitution gives \(q(s^*)=c_2^*\). At this parameter pair,
\[
P(s^*)=P'(s^*)=P''(s^*)=0,
\qquad
P^3(s^*)=k(k-1)\rho^2>0,
\]
so the root has multiplicity exactly three.

Now suppose \(0<c_1<c_1^*\). Since
\[
H\!\left(\frac{k}{k-1}\right)>0,\qquad H(s^*)=c_1(s^*)^{k+1}-1<0,
\]
strict convexity shows that \(H\) has exactly two roots \(s_-<s_+\), ordered as stated. Thus \(q\) increases on \((0,s_-)\), decreases on \((s_-,s_+)\), and increases on \((s_+,\infty)\). At any stationary point, eliminating \(c_1\) via \(H(s)=0\) gives
\[
c_1=\frac{(k-1)s-k}{s^{k+1}},\qquad q(s)=\frac{ks-(k+1)}{s^k}.
\]
Both fold heights are positive, and the maximum at \(s_-\) is strictly above the minimum at \(s_+\). Intersections of a horizontal level \(c_2\) with this monotonicity pattern give exactly the stated counts, including one double root at a fold.

## Verification
The proof is analytic and does not infer an infinite statement from finite computation. The bundled `verify.py` checks the cusp identities exactly with rational arithmetic for \(2\le k\le20\), checks representative fold ordering and root counts for several orders, and checks reconstruction of physical parameters. These checks are corroborative only.

## Relationship to prior work
Botirov--Haydarov--Qayumov derive the same symmetric scalar equation for arbitrary tree order. For order two they prove a sufficient uniqueness condition and otherwise only an upper bound of three symmetric translation-invariant splitting Gibbs measures; for arbitrary order their positive-coefficient case likewise gives an upper bound of three positive solutions by Descartes' rule. The exact fold values, the triple-root cusp, and the all-order exact one-versus-three partition above are not stated there.

Ganikhodjaev--Idris studied a simple BEG model on a Cayley tree of order two and reported an exact critical temperature and phase-transition regions for a physical subfamily. Only its abstract was available in the present comparison, so no whole-document noncoverage claim is made for that paper. Lima's uniqueness result concerns the \(d\)-dimensional lattice and a Dobrushin-type disordered region, not this Cayley-tree boundary-law root geometry.

## Limitations
This is a branch-local classification. It does not count nonsymmetric solutions of the full two-variable translation-invariant system and therefore does not by itself give the total number of translation-invariant Gibbs measures. The fold diagram concerns splitting Gibbs measures represented by positive boundary laws; it does not address extremality or stability. A residual literature risk is that an equivalent order-two specialization may be hidden in older Bethe-lattice literature under different thermodynamic coordinates.

## References
1. G. Botirov, F. Haydarov, U. Qayumov, *Gibbs Measures of the Blume--Emery--Griffiths Model on the Cayley Tree*, Mathematical Physics, Analysis and Geometry **26** (2023), article 7. DOI: 10.1007/s11040-023-09448-7.
2. N. Ganikhodjaev, A. B. Idris, *The Blume-Emery-Griffiths model on Cayley tree and its phase transitions*, Middle-East Journal of Scientific Research **13** (2013), 83--89. DOI: 10.5829/idosi.mejsr.2013.13.mae.99932.
3. P. C. Lima, *Uniqueness of the Gibbs state of the BEG model in the disordered region of parameters*, arXiv:2004.11484; Letters in Mathematical Physics **111** (2021).
