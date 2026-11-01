# Dyadic boundary layers and a complete endpoint phase law for flat-spot-map fluctuations

## Finding

Consider the limiting fluctuation density \(\rho\) of the truncated flat-spot doubling family, defined below. Let \(u>10\), put \(z=u^{-1}\), and set
\[
a_k=\frac{1-2^{1-k}}{k},\qquad
K(u)=\min\{k\geq 4:a_k\leq u^{-1}\}.
\]
For the canonical interval-indicator representative of the density,
\[
\boxed{\rho\left(-\frac12+\frac1u\right)
 = (K(u)+1)2^{1-K(u)}+O\!\left(u^2 2^{-3u/2}\right)}
\qquad(u\to\infty),
\]
with an absolute implied constant. For every integer \(q\geq 10\) and \(q\leq u<q+1\), the integer \(K(u)\) is explicitly
\[
K(u)=\begin{cases}
q,&q\leq u\leq q+\delta_q,\\
q+1,&q+\delta_q<u<q+1,
\end{cases}\qquad
\delta_q=\frac{q\,2^{1-q}}{1-2^{1-q}}.
\]
Consequently the normalized endpoint density
\[
R(u)=\frac{\rho(-1/2+1/u)}{2u\,2^{-u}}
\]
obeys, uniformly for \(u\to\infty\),
\[
R(u)=2^{u-K(u)}\left(1+O\!\left(u^{-1}+u2^{-u/2}\right)\right).
\]
Its set of subsequential limits is **exactly** \([1/2,1]\). In particular, the normalized density does not converge at the endpoint: it has an exponentially thin layer of width \(\delta_q\sim q2^{1-q}\) adjacent to each integer in the reciprocal-distance variable, followed by a factor-two phase reset. The result does not assert that the unnormalized density is continuous at component boundaries.

## Assumptions and scope

For \(0<t<1\), define the weakly monotone circle map on \([0,1)\)
\[
f_t(x)=\begin{cases}
t,&0\leq x\leq t/2,\\
2x\pmod1,&t/2<x<(1+t)/2,\\
t,&(1+t)/2\leq x<1.
\end{cases}
\]
For independently uniform \(t,x_0\in[0,1)\), let
\[
S_n(t,x_0)=\sum_{j=0}^{n-1}\left(f_t^j(x_0)-\frac12\right).
\]
The cited primary source proves that \(Y=\lim_{n\to\infty}S_n/n\) exists for almost every \((t,x_0)\) and has an explicitly specified density. We take \(\rho\) to be the *canonical nonnegative representative* of its interval-indicator expansion: indicator intervals are closed at both ends. Values at the countable family of component endpoints are version-dependent; all asymptotic bounds concern this specified representative. This is a statement about the distribution obtained by drawing the map parameter \(t\) uniformly once, not about random switching of maps along a trajectory.

For relatively prime integers \(1\leq p<k\), define
\[
 s_i(p,k)=\left\lfloor\frac{(i+1)p}{k}\right\rfloor-
 \left\lfloor\frac{ip}{k}\right\rfloor,
 \quad
 \tau_{p,k}=\sum_{i=1}^{k}s_i(p,k)2^{-i},
\]
and
\[
J_{p,k}=\left[\frac{p-\tau_{p,k}}{k}-\frac12,
\frac{p-\tau_{p,k}+1}{k}-\frac12\right].
\]
The prior density formula (Veerman–Oberly–Fox, Theorem 3.3) is
\[
\rho(w)=\sum_{k=2}^{\infty}
\sum_{\substack{1\leq p<k\\\gcd(p,k)=1}}
\frac{k}{2^k-1}\,\mathbf1_{J_{p,k}}(w).
\]
This exact expansion is a **prior result**, not a finding claimed here. The new assertion is its *uniform all-distance asymptotic*, exact microscopic boundary layer, and full normalized limit set.

## Proof

**1. Denominator-one supports.** For \(p=1\), the mechanical word has its unique nonzero digit at index \(k-1\). Therefore \(\tau_{1,k}=2^{1-k}\), and the contribution at \(w=-1/2+z\) is nonzero precisely when
\[
a_k=\frac{1-2^{1-k}}{k}\leq z\leq
b_k=\frac{2-2^{1-k}}{k}.
\]
The sequence \(a_k\) decreases strictly for \(k\geq4\): cross-multiplication reduces \(a_{k+1}<a_k\) to \(2^k>k+2\). Thus all indices \(k\geq K(u)\) meet the lower support bound. Because \(u>10\) implies \(K(u)\geq5\), the upper bound also holds whenever \(K(u)\leq k\leq3u/2\): indeed \(k/u\leq3/2<2-2^{1-k}\). Hence every denominator-one term with \(K(u)\leq k\leq3u/2\) contributes.

**2. Suppression of all other numerators.** Suppose \(p\geq2\) and \(-1/2+1/u\in J_{p,k}\). Then \(p-\tau_{p,k}\leq k/u\). If \(k<3u/2\), the right side is less than \(3/2\). Since \(0<\tau_{p,k}<1\), this forces \(p=2\) and \(\tau_{2,k}>1/2\). But \(p-\tau_{p,k}>1\) also forces \(k>u>10\), and for \(k>4\) the first digit \(s_1(2,k)\) is zero. Therefore \(\tau_{2,k}<1/2\), a contradiction. Every contribution with numerator \(p\geq2\) hence has \(k\geq3u/2\).

**3. Uniform remainder.** Write \(c_k=k/(2^k-1)\). Step 1 shows that replacing the denominator-one terms by the entire tail \(\sum_{k\geq K(u)}c_k\) changes the result by at most \(\sum_{k\geq3u/2}c_k\). Step 2 bounds all other numerator terms by \(\sum_{k\geq3u/2}(k-1)c_k\). Both bounds are nonnegative and converge. In total,
\[
\rho(-1/2+1/u)=\sum_{k\geq K(u)}\frac{k}{2^k-1}
+O\!\left(\sum_{k\geq3u/2}k^2 2^{-k}\right).
\]
The last sum is \(O(u^2 2^{-3u/2})\) by the geometric-tail identities. Finally,
\[
\sum_{k\geq K}\frac{k}{2^k-1}
=\sum_{k\geq K}k2^{-k}+O\!\left(\sum_{k\geq K}k4^{-k}\right)
=(K+1)2^{1-K}+O(K4^{-K}).
\]
Since \(K(u)\in\{\lfloor u\rfloor,\lceil u\rceil\}\) for \(u>10\), the latter error is absorbed in \(O(u^2 2^{-3u/2})\). This proves the uniform expansion.

**4. Exact layer and phase.** For \(q=\lfloor u\rfloor\geq10\), one has \(a_{q-1}>1/q\) (equivalent to \(q2^{2-q}<1\)) and \(a_{q+1}<1/(q+1)\). Hence \(K(u)\in\{q,q+1\}\). The condition \(K(u)=q\) is exactly
\[
\frac1u\geq\frac{1-2^{1-q}}q
\quad\Longleftrightarrow\quad
u\leq\frac q{1-2^{1-q}}=q+\delta_q.
\]
This proves the two cases, including their stated boundary conventions.

**5. Complete limit set.** Divide the uniform expansion by \(2u2^{-u}\). The error is \(O(u2^{-u/2})\), while \((K(u)+1)/u=1+O(1/u)\). Thus \(R(u)=2^{u-K(u)}(1+o(1))\) uniformly. The phase satisfies \(-1\leq u-K(u)\leq O(u2^{-u})\), giving \(\liminf R\geq1/2\) and \(\limsup R\leq1\). Along \(u=q\) the limit is \(1\); along \(u=q+q^{-1/2}\), eventually outside the exponentially thin layer, it is \(1/2\). For any fixed \(0<\theta<1\), along \(u=q+\theta\) the limit is \(2^{\theta-1}\). These sequences realize every number in \([1/2,1]\). \(\square\)

## Verification

The accompanying standalone Python 3 script `verify_flat_spot.py` uses exact `fractions.Fraction` arithmetic. It verifies the mechanical-word specialization for \(3\leq k\leq50\), the exact two-phase threshold at four rational probes for each \(10\leq q\leq27\), and nine finite-denominator density decompositions including reciprocal-integer and boundary-layer probes. Its executed output was `PASS: 165 exact-rational finite checks`. The script does **not** certify the infinite expansion or the asymptotic theorem; those follow from Steps 1–5 and the cited exact density formula.

## Relationship to prior work

Veerman, Oberly and Fox established the limit law and the complete exact series representation of its density (Theorem 3.3). They also examined the endpoint specifically at reciprocal integers \(z=1/q\) (Proposition 5.2). Their exact series **contains the data** needed for this refinement, but neither its stated pointwise representation nor its reciprocal-integer tail statement gives the uniform phase classification without the separation of all higher numerator terms in Step 2. The present result is therefore an asymptotic refinement of a known exact density, not a new invariant law, a new map, or an independent proof of the original distribution theorem. Related analyses of flat-spot circle dynamics address rotation plateaux and symbolic orbits rather than this distributional all-distance endpoint phase.

## Limitations

Only the parameter-ensemble endpoint \(w\downarrow-1/2\) is analyzed, and only for the slope-two truncated flat-spot family. The density is specified by a canonical pointwise version; modifying a density on a null set can change its values at chosen endpoints. No rates of convergence of \(S_n/n\) are proved, nor an analogous phase law for other integer slopes. The prior exact density formula logically determines all values, so the claimed contribution is limited to extracting and proving the explicit **uniform phase theorem**. Possible unindexed equivalent endpoint asymptotics remain a publication-priority risk. The stated asymptotic and phase characterization have not received independent scientific validation.

## References

1. J. J. P. Veerman, P. J. Oberly, L. S. Fox, *Statistics of a Family of Piecewise Linear Maps*, arXiv:2010.00155 (first public version, 2020-10-01); Physica D **427** (2021), 133019, doi:10.1016/j.physd.2021.133019. Primary exact density: Theorem 3.3; reciprocal-integer endpoint study: Proposition 5.2.
2. J. J. P. Veerman, *Symbolic Dynamics and Rotation Numbers*, Physica D **22** (1986). Background for rational rotation plateaux and the mechanical-word parameterization (as credited by Reference 1).
3. J. J. P. Veerman, *Symbolic Dynamics of Order-Preserving Orbits*, Physica D **29** (1987). Background for the plateau geometry, as credited by Reference 1.
