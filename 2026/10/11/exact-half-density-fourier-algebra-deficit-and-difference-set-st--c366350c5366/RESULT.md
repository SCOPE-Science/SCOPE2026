# Exact half-density Fourier-algebra deficit and difference-set stability
## Finding
Let \(G\) be a finite abelian group of odd order \(v\ge3\), and let \(A\subset G\) satisfy \(|A|=(v-1)/2\). With normalized Fourier transform
\[
\widehat{1_A}(\gamma)=\frac1v\sum_{x\in G}1_A(x)\overline{\gamma(x)}
\]
and Fourier-algebra norm
\[
\|1_A\|_{A(G)}=\sum_{\gamma\in\widehat G}|\widehat{1_A}(\gamma)|,
\]
define
\[
c_v=\frac{\sqrt{v+1}}{2v},\qquad U_v=\frac{v-1}{2v}\left(1+\sqrt{v+1}\right).
\]
Then the deficit from the universal half-density upper envelope is exactly
\[
\boxed{U_v-\|1_A\|_{A(G)}=
\frac{v}{\sqrt{v+1}}
\sum_{\gamma\ne1}\left(|\widehat{1_A}(\gamma)|-c_v\right)^2.}
\]
Hence \(\|1_A\|_{A(G)}\le U_v\), and equality holds if and only if \(v\equiv3\pmod4\) and \(A\) is a difference set with parameters
\[
\left(v,\frac{v-1}{2},\frac{v-3}{4}\right).
\]

There is also a direct quantitative bridge to additive autocorrelation. Put
\[
r_A(t)=|A\cap(A+t)|,\qquad \lambda_v=\frac{v-3}{4},\qquad
V(A)=\sum_{t\ne0}(r_A(t)-\lambda_v)^2.
\]
Then
\[
\boxed{
\frac{4V(A)}{\sqrt{v+1}(v-1+\sqrt{v+1})^2}
\le U_v-\|1_A\|_{A(G)}
\le \frac{4V(A)}{(v+1)^{3/2}}.}
\]
If \(v\equiv3\pmod4\) and \(A\) is not a difference set, the integer deviations \(r_A(t)-\lambda_v\) have sum zero and are not all zero, so \(V(A)\ge2\). Therefore
\[
U_v-\|1_A\|_{A(G)}\ge
\frac{8}{\sqrt{v+1}(v-1+\sqrt{v+1})^2}.
\]

For every prime \(p\equiv3\pmod4\), the nonzero quadratic residues \(Q\subset\mathbb Z_p\) have constant nonprincipal Fourier magnitude \(\sqrt{p+1}/(2p)\), so they attain the exact maximum \(U_p\). If \(Q\) is viewed as a frequency set, the associated Fourier projection has
\[
\|P_Q\|_{\ell^1\to\ell^1}=\|P_Q\|_{\ell^\infty\to\ell^\infty}=U_p.
\]

## Assumptions and scope
All finite groups are abelian and use normalized counting measure. The stability identity and two-sided variance estimate hold for every odd group order \(v\), whether or not a difference set with the displayed parameters exists. The exact maximum assertion for prime cyclic groups is made only for \(p\equiv3\pmod4\), where the quadratic-residue construction supplies an extremizer. No classification of all difference sets with those parameters is asserted.

The projection statement uses the standard identification of a frequency subset with an idempotent Fourier multiplier. It concerns endpoint \(\ell^1\) and \(\ell^\infty\) norms, not interior \(\ell^q\) norms.

## Proof
Write \(k=(v-1)/2\) and \(a_\gamma=|\widehat{1_A}(\gamma)|\) for nonprincipal characters. The principal coefficient is \(k/v\). Parseval gives
\[
\sum_{\gamma\ne1}a_\gamma^2
=\frac{k}{v}-\frac{k^2}{v^2}
=\frac{v^2-1}{4v^2}
=(v-1)c_v^2.
\]
Cauchy--Schwarz therefore gives
\[
\sum_{\gamma\ne1}a_\gamma\le(v-1)c_v,
\]
which yields \(\|1_A\|_{A(G)}\le U_v\). More is true. Since the squared norm is fixed,
\[
\sum_{\gamma\ne1}(a_\gamma-c_v)^2
=2c_v\left((v-1)c_v-\sum_{\gamma\ne1}a_\gamma\right).
\]
Because \(2c_v=\sqrt{v+1}/v\), this is exactly the displayed deficit identity.

Equality occurs exactly when every nonprincipal Fourier coefficient has magnitude \(c_v\). To translate that condition, let \(r_A(t)=\sum_x1_A(x)1_A(x-t)\). Fourier inversion for the correlation gives, for \(t\ne0\),
\[
\frac{r_A(t)}v=\frac{k^2}{v^2}+\sum_{\gamma\ne1}a_\gamma^2\gamma(t).
\]
If every \(a_\gamma=c_v\), then \(\sum_{\gamma\ne1}\gamma(t)=-1\), hence
\[
r_A(t)=\frac{v-3}{4}
\]
for every nonzero \(t\). Conversely, constant nonzero difference multiplicity gives constant nonprincipal Fourier magnitude by Fourier transforming the correlation. Thus equality is equivalent to the stated difference-set property; integrality forces \(v\equiv3\pmod4\).

For the quantitative comparison, let \(d(t)=r_A(t)-\lambda_v\) for \(t\ne0\) and \(d(0)=0\). Parseval for the correlation difference gives
\[
V(A)=v^3\sum_{\gamma\ne1}(a_\gamma^2-c_v^2)^2.
\]
Since
\[
(a_\gamma^2-c_v^2)^2=(a_\gamma-c_v)^2(a_\gamma+c_v)^2
\]
and \(c_v\le a_\gamma+c_v\le k/v+c_v=(v-1+\sqrt{v+1})/(2v)\), substitution of the exact deficit identity gives both displayed inequalities.

When \(v\equiv3\pmod4\), the deviations \(d(t)\) are integers and satisfy \(\sum_{t\ne0}d(t)=0\). If they are not all zero then at least one is positive and one negative, so \(V(A)\ge2\), proving the explicit gap.

Finally let \(p\equiv3\pmod4\) be prime and \(Q\) the nonzero squares. For a nonzero frequency \(r\), the quadratic Gauss sum gives
\[
\sum_{q\in Q}e^{2\pi i rq/p}=\frac{-1+\chi(r)\tau_p}{2},
\]
where \(|\tau_p|=\sqrt p\) and \(\tau_p\) is purely imaginary because \(\chi(-1)=-1\). Therefore this sum has modulus \(\sqrt{p+1}/2\), so the normalized nonprincipal Fourier magnitude is exactly \(c_p\). Thus \(Q\) attains \(U_p\).

For the endpoint projection statement, Fourier inversion writes the projection onto \(Q\) as normalized convolution by \(K(x)=\sum_{q\in Q}e^{2\pi iqx/p}\). Its \(\ell^\infty\) norm is the normalized absolute kernel mass, attained by the pointwise phase of the reflected kernel; the \(\ell^1\) norm is the same by column sums or duality. That normalized absolute kernel mass is \(\|1_Q\|_{A(\mathbb Z_p)}\).

## Verification
The accompanying `verify.py` checks the deficit identity and both stability inequalities on many cyclic half-sets, exhaustively checks all half-sets for \(p=7\) and \(p=11\), and verifies the quadratic-residue formula and constant difference multiplicity for every prime \(p\equiv3\pmod4\) below \(300\). These finite computations are corroborative only; the proof above establishes the statements for all allowed groups and primes.

## Relationship to prior work
Green and Konyagin introduced precisely this normalized Fourier-algebra norm for subsets of \(\mathbb Z/p\mathbb Z\) and asked for the **minimum** norm among sets of size \(\lfloor p/2\rfloor\). Their Question 1.1 and Theorem 1.2 concern lower bounds for that minimum; they do not state the maximum, a deficit identity, or a difference-set stability theorem. Their paper therefore supplies the natural half-density Littlewood context but not the result proved here.

Matolcsi and Ruzsa study difference-avoidance and positive exponential-sum extremal quantities in finite commutative groups. Their definitions and Theorem 1.4 concern Turán/Delsarte-type constants and intersectivity, not the Fourier-algebra \(\ell^1\) norm of an indicator or the exact half-density deficit derived here.

The equality condition is consistent with the classical character-theoretic description of difference sets: constant nonprincipal Fourier magnitude is the spectral form of constant nonzero difference multiplicity. The new statement uses that structure to identify the exact half-density Fourier-algebra upper envelope and, more importantly, gives an exact quadratic spectral deficit and explicit autocorrelation-stability bounds. No claim is made that the underlying difference-set character criterion itself is new.

## Limitations
The stability constants are explicit but are not claimed optimal as functions of \(V(A)\); only the spectral deficit identity is exact. For composite \(v\), the theorem does not decide existence or classify isomorphism classes of the relevant difference sets. For primes \(p\equiv1\pmod4\), the universal Cauchy--Schwarz envelope is strict and this result does not compute the exact maximum.

A residual originality risk is that the exact deficit identity or an equivalent stability estimate may be implicit in older difference-set, perfect-sequence, or frame-theoretic literature under a different norm convention. Targeted statement-level searches did not locate such a result.

## References
1. B. Green and S. Konyagin, “On the Littlewood problem modulo a prime,” arXiv:math/0601565v1, first public 2006-01-23; *Canadian Journal of Mathematics* 61 (2009), 141–164, DOI 10.4153/CJM-2009-007-4. Primary MSC 42A99.
2. M. Matolcsi and I. Z. Ruzsa, “Difference Sets and Positive Exponential Sums I. General Properties,” arXiv:1207.1781v2, public 2012-07-16; *Journal of Fourier Analysis and Applications* 20 (2014), 17–41.
