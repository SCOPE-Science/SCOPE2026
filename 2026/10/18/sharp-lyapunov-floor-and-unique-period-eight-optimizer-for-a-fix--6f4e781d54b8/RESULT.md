# Sharp Lyapunov floor and unique period-eight optimizer for a fixed-point-free affine map

## Finding

For an open parameter region of the fixed-point-free four-branch affine map of García-Grimaldo and Campos, every boundary-avoiding orbit has a uniformly positive four-step derivative lower bound. The exact minimum Lyapunov exponent over invariant probability measures avoiding the branch boundaries is
\[
\inf_{\mu}\int\log|F'|\,d\mu=\frac14\log(ts^3)>0.
\]
The minimizer is unique: the uniform measure on a single primitive period-eight orbit. The same orbit attains the lower bound, so the result is sharp, rather than merely a positivity criterion.

More precisely, let \(a>0\), \(0<s<1\), \(t>1\), and set
\[
\rho=s^3t-s-s^2-s^3,\qquad \Lambda=ts^3.
\]
Assume \(0<\rho<1\) and \(\Lambda>1\). Define \(u_*=\rho/(1+\Lambda)\) and \(P(u)=s(u-1)\). The unique minimizing periodic orbit consists of the eight signed states
\[
\begin{aligned}
&a u_*,\quad -a t(1-u_*),\quad -aP(t(1-u_*)),\quad -aP^2(t(1-u_*)),\\
&-a u_*,\quad a t(1-u_*),\quad aP(t(1-u_*)),\quad aP^2(t(1-u_*)).
\end{aligned}
\]
Their multipliers satisfy \(|(F^8)'|=\Lambda^2\). Its least period is exactly eight.

## Assumptions and scope

The map \(F=F_{a,s,t}:[-ta,ta]\to[-ta,ta]\) is defined by
\[
F(x)=\begin{cases}
s(x+a),&-ta\le x\le-a,\\
t(x+a),&-a<x<0,\\
t(x-a),&0\le x<a,\\
s(x-a),&a\le x\le ta.
\end{cases}
\]
This is the published four-branch family with \(m_1=s\), \(m_2=t\), \(b_1=sa\), \(b_2=ta\). The singular set for the derivative is \(B=\{-a,0,a\}\). Every derivative statement assumes that all forward iterates avoid \(B\). Every measure statement ranges over Borel probability measures invariant under the displayed map and satisfying \(\mu(B)=0\). At the two endpoints of the closed state interval derivatives have their natural one-sided branch meaning. For invariant measures with \(\mu(B)=0\), the endpoints carry zero mass because their only possible predecessor among interval states is the excluded discontinuity or no predecessor at all. No assertion about differentiation at the discontinuity or the branch joins is included.

The parameter conditions \(0<\rho<1\) and \(\Lambda>1\) are strict; behavior at equality and outside this region is not classified. The open region includes \((s,t)=(4/5,5)\), the slope choice studied in the published FPGA example.

## Proof

**Step 1: exact absolute-value semiconjugacy.** Put \(u=|x|/a\). The induced map \(g:[0,t]\to[0,t]\) obeys
\[
g(u)=\begin{cases}t(1-u),&0\le u<1,\\s(u-1),&1\le u\le t.\end{cases}
\]
The two possible slopes in absolute value are therefore \(t\) for \(0<u<1\) (denote such a visit by `I`) and \(s\) for \(1<u\le t\) (denote by `O`). For \(u>1\), write the next iterate as \(P(u)=s(u-1)\).

**Step 2: the sharp four-visit restriction.** If an orbit could have four consecutive `O` visits, its first three moves would follow the increasing affine map \(P\) from some \(u\le t\). Yet
\[
P^3(u)\le P^3(t)=s^3t-s-s^2-s^3=\rho<1,
\]
contradicting the fourth `O`. Hence each block of four successive derivative-defined iterates contains at least one `I`. As \(t>s>0\), its derivative product is at least \(ts^3=\Lambda\). For every integer \(k\ge1\),
\[
\bigl|(F^{4k})'(x)\bigr|\ge\Lambda^k.
\]
For arbitrary \(n\), the remaining fewer than four factors have product bounded below by \(\min\{s,t\}^3=s^3\); dividing logarithms by \(n\) gives the lower Lyapunov exponent at least \(\frac14\log\Lambda\).

**Step 3: equality orbit.** Define \(u_*=\rho/(1+\Lambda)\). Since \(0<\rho<1\), we have \(0<u_*<1\). Direct affine substitution gives
\[
P^3(t(1-u_*))=\rho-\Lambda u_*=u_*.
\]
The intermediate three iterates are strictly larger than \(1\): the last `O` maps by \(P\) to the positive value \(u_*\), so its input exceeds \(1\), and positivity propagates backward through the increasing affine outer branch. Equivalently, all three intermediate values are the explicit states above and lie in \((1,t)\). Thus the absolute-value itinerary is the strictly admissible periodic word `IOOO`. On the signed map, outer steps preserve sign and the inner step reverses sign, giving the displayed primitive eight-cycle. Exactly two `I` and six `O` visits occur per eight steps, so \(|(F^8)'|=(ts^3)^2\) and its exponent equals \(\frac14\log\Lambda\).

**Step 4: equality implies unique invariant measure.** For any invariant probability \(\mu\) with \(\mu(B)=0\), let \(p=\mu(\{x:|x|<a\})\). Because \(\mu(B)=0\), the derivative exists along almost every complete orbit. Integrating the four-visit restriction and using invariance gives \(4p\ge1\). Hence
\[
\int\log|F'|\,d\mu=p\log t+(1-p)\log s\ge\frac14\log(ts^3).
\]
If equality holds, \(p=1/4\). The nonnegative integer count of `I` symbols in each four-window has mean exactly one, hence equals one almost surely. Intersecting the count-one events over all forward shifts, subtracting consecutive window counts yields that the inner/outer itinerary repeats with period four. Its only possible recurrent symbolic word is `IOOO`, up to cyclic shift.

On the `IOOO` cylinder the fourth iterate of \(g\) is the affine map \(u\mapsto\rho-\Lambda u\). Since \(\Lambda>1\), an orbit whose four-symbol word repeats forever must start at its unique fixed point \(u_*\): any different point would have its displacement multiplied by \(-\Lambda\) at each fourth step, eventually leaving the compact interval \([0,t]\). For other cyclic shifts apply the appropriate finite prefix. Thus the absolute orbit is the unique four-cycle from Step 3. Since the original map reverses sign once per four visits, its only lift is the displayed eight-cycle. An invariant measure supported on this single orbit must be its uniform orbit measure. Conversely that measure attains equality. This establishes uniqueness.

## Verification

A standalone Python 3 standard-library script, `verify_sharp_lyap.py`, checks the exact rational eight-cycle at \((a,s,t)=(5,4/5,5)\); verifies its return multiplier and all eight images; tests the four-visit restriction along more than one thousand exact rational initial states; and verifies the explicit orbit on four additional rational parameter triples. It prints `EXACT_PERIOD8_AND_FINITE_ITINERARY_CHECKS_OK` on success. The universal four-visit restriction and measure rigidity are analytical deductions in the proof above; finite testing cannot certify them independently.

For the source's reported slopes and amplitude, the minimizing orbit is
\[
\left(\frac{76}{89},-\frac{1845}{89},-\frac{1120}{89},-\frac{540}{89},-\frac{76}{89},\frac{1845}{89},\frac{1120}{89},\frac{540}{89}\right)
\]
with \(\rho=76/125\), \(\Lambda=64/25\), and exact exponent \(\frac14\log(64/25)\).

## Relationship to prior work

García-Grimaldo and Campos (2021) introduced the fixed-point-free piecewise-linear family and proved a fixed-point criterion and a Devaney-chaotic special case. García-Grimaldo and collaborators (2023) analyzed this same four-branch map and reported its Lyapunov-exponent diagrams, its exact values \(s=4/5\), \(t=5\), \(a=5\), and an implementation. Their full accessible article discusses those numerical exponents and the existing Devaney theorem, but does not provide the universal sharp lower Lyapunov bound, identify its unique invariant-measure minimizer, or exhibit the precise period-eight optimizer. Standard eventual-expansion theory and general ergodic optimization provide relevant context, but an explicit result for this exact four-branch family was not identified. The 2021 article was accessible only in bibliographic/abstract/preview form, so undiscovered overlapping results remain a priority risk.

## Limitations

The conclusion is not a claim about branch-boundary derivatives or invariant measures charging \(\{-a,0,a\}\), about invariant densities, entropy, cryptographic randomness, or numerical implementation precision. The parameter region is sufficient for the sharp formula, and no optimality of this parameter region is claimed. Unique minimization does not imply an isolated Lyapunov value or a quantitative spectral gap. Publication priority beyond inspected material requires independent literature verification.

## References

1. C. García-Grimaldo and E. Campos, *Chaotic Features of a Class of Discrete Maps without Fixed Points*, International Journal of Bifurcation and Chaos **31** (2021), 2150200, DOI: 10.1142/S021812742150200X.
2. C. García-Grimaldo, C. F. Bermúdez-Márquez, E. Tlelo-Cuautle, and E. Campos-Cantón, *FPGA Implementation of a Chaotic Map with No Fixed Point*, Electronics **12** (2023), 444, DOI: 10.3390/electronics12020444.
3. P. Góra and P. Eslami, *On Eventually Expanding Maps of the Interval* (2011), Concordia repository identifier 976827.
4. M. Pollicott and P. Vytnova, *Accurate Bounds on Lyapunov Exponents for Expanding Maps of the Interval* (2022), DOI: 10.1007/s00220-022-04495-7.
