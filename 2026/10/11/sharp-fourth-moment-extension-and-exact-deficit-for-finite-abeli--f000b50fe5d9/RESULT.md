# Sharp fourth-moment extension and exact deficit for finite abelian difference sets
## Finding
Let \(G\) be a finite abelian group of order \(v\), and let \(D\subset G\) be a \((v,k,\lambda)\)-difference set: \(|D|=k\) and each nonzero \(g\in G\) has exactly \(\lambda\) ordered representations \(g=a-b\) with \(a,b\in D\). Give the dual group \(\widehat G\) normalized Haar measure and define
\[
E_Df(\chi)=\sum_{d\in D} f(d)\chi(d).
\]
Then, for every \(f:D	o\mathbb C\),
\[
\|E_Df\|_{L^4(\widehat G)}\le C_D\|f\|_{\ell^2(D)},
\qquad
C_D^4=1+\lambda\left(1-\frac1k
ight)=1+\frac{(k-1)^2}{v-1}.
\]
The constant is sharp.

There is also an exact nonnegative deficit decomposition. Put
\[
S=\sum_{d\in D}|f(d)|^2,\qquad Q=\sum_{d\in D}|f(d)|^4,
\]
and for \(g\in G\) set
\[
A_g=\sum_{a-b=g}f(a)\overline{f(b)},\qquad
B_g=\sum_{a-b=g}|f(a)|^2|f(b)|^2.
\]
Then
\[
C_D^4S^2-\|E_Df\|_4^4
=\lambda\left(Q-\frac{S^2}k
ight)
+\sum_{g
e0}\left(\lambda B_g-|A_g|^2
ight).
\]
For nonzero \(f\), equality holds exactly when \(|f|\) is constant on \(D\) and, for every \(g
e0\), the numbers \(f(a)\overline{f(b)}\) are the same for all ordered representations \(a-b=g\) inside \(D\). In particular every scalar multiple of a character of \(G\), restricted to \(D\), is an extremizer.

## Assumptions and scope
The group is finite and abelian. The difference-set convention is ordered: every nonzero group element has exactly \(\lambda\) representations \(a-b\) from \(D	imes D\). The dual Haar measure has total mass one, while the \(\ell^2(D)\) norm is the unnormalized finite sum. The theorem is exact for every admissible \((v,k,\lambda)\), not asymptotic. It does not assert that the intrinsic phase-coherence criterion collapses to character restrictions for every difference set.

## Proof
Fourier orthogonality on \(\widehat G\) gives
\[
\|E_Df\|_4^4=\sum_{g\in G}|A_g|^2.
\]
For \(g=0\), one has \(A_0=S\). For every \(g
e0\), the difference-set hypothesis says that the sum defining \(A_g\) has exactly \(\lambda\) terms. Cauchy--Schwarz therefore gives
\[
|A_g|^2\le \lambda B_g.
\]
Summing the \(B_g\) over nonzero \(g\) counts every ordered pair of distinct points of \(D\) exactly once, so
\[
\sum_{g
e0}B_g=S^2-Q.
\]
Consequently
\[
\|E_Df\|_4^4\le S^2+\lambda(S^2-Q).
\]
The power-mean inequality gives \(Q\ge S^2/k\), hence
\[
\|E_Df\|_4^4\le\left(1+\lambda\left(1-\frac1k
ight)
ight)S^2.
\]
Since a difference set satisfies \(k(k-1)=\lambda(v-1)\), the fourth power of the constant is also \(1+(k-1)^2/(v-1)\).

Keeping both inequalities before discarding their nonnegative remainders gives exactly
\[
C_D^4S^2-\|E_Df\|_4^4
=\lambda\left(Q-\frac{S^2}k
ight)
+\sum_{g
e0}\left(\lambda B_g-|A_g|^2
ight).
\]
This proves the deficit identity and the upper bound. For \(f\equiv1\), \(A_0=k\) and \(A_g=\lambda\) for every \(g
e0\), so the bound is attained and is sharp. More generally, if \(f(d)=c\psi(d)\) for a character \(\psi\) of \(G\), every summand in a fixed difference fiber has the same phase \(|c|^2\psi(g)\), so equality holds.

For nonzero \(f\), equality in the deficit identity forces both nonnegative parts to vanish. The first vanishes exactly when all \(|f(d)|\) are equal. Equality in the Cauchy--Schwarz estimate for a fixed nonzero \(g\) holds exactly when the \(\lambda\) complex numbers \(f(a)\overline{f(b)}\), indexed by \(a-b=g\), are identical. These conditions are also sufficient, yielding the stated complete intrinsic equality criterion.

## Verification
The standalone verifier checks the difference-set multiplicities, the exact rational deficit identity, and sharpness for three representative cyclic examples: a \((7,4,2)\) difference set, the \((11,5,2)\) Paley difference set, and the \((19,9,4)\) Paley difference set. It uses exact rational arithmetic for the deficit identity. Its output is:

`VERIFY_OK cases=[(7, 4, 2, Fraction(5, 2)), (11, 5, 2, Fraction(13, 5)), (19, 9, 4, Fraction(41, 9))] exact_deficit=1 sharpness=1`

The finite replay corroborates the algebra but is not used as a substitute for the proof for arbitrary difference sets.

## Relationship to prior work
Mockenhaupt and Tao formulate the finite-field extension/restriction problem and its sharp-constant viewpoint for Fourier extension operators; their first public version is dated 18 April 2002 and lists primary MSC 42B05. Their paper treats algebraic varieties and general restriction estimates, not the exact difference-set constant or the displayed deficit identity.

Günther and Schmidt study \(L^4\) norms and merit factors of characteristic polynomials arising from Paley, Singer, and other difference sets. Their results concern structured \(\pm1\) coefficient polynomials and asymptotic merit factors. The statement here instead allows arbitrary complex coefficients on an arbitrary finite abelian difference set and identifies the exact operator norm, a sum-of-squares-type deficit, and the full intrinsic equality condition.

Targeted searches under the aliases “difference set”, “\(\Lambda(4)\) constant”, “finite abelian extension”, “fourth moment”, “representation fibers”, and “Paley/Singer arbitrary coefficients” found no published result in the checked sources that implies the complete statement. A residual risk remains that an older \(\Lambda(4)\)-set source records an equivalent inequality under a different normalization.

## Limitations
The theorem depends essentially on exact uniformity of all nonzero difference fibers. It does not directly give the optimal constant for partial or almost difference sets. The equality criterion is complete as stated but may have additional non-character phase solutions for particular difference sets, especially when \(\lambda=1\). No claim is made about higher moments.

## References
1. G. Mockenhaupt and T. Tao, *Restriction and Kakeya phenomena for finite fields*, arXiv:math/0204234, first public version 2002-04-18; primary MSC 42B05.
2. C. Günther and K.-U. Schmidt, *Merit factors of polynomials derived from difference sets*, arXiv:1503.05858, first public version 2015-03-19.
