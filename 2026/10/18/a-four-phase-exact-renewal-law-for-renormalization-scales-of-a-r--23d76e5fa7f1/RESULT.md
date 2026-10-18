# A four-phase exact renewal law for renormalization scales of a rhombus piecewise isometry

## Finding

Write \(q=\sqrt{2}-1\), and let \(s\) be selected uniformly from the parameter interval \([0,\sqrt{2}]\) of the Lowenstein–Vivaldi rhombus piecewise-isometry family. Follow the canonical nested base-triangle renormalization of its induced five-atom map, choosing at each stage the standard subtriangle associated with the interior of the relevant parameter branch. Let \(L_n(s)\) be its positive similarity-length scale after \(n\) *complete* renormalizations, with \(L_0>0\). Define the exact-scale event for integers \(m\geq0\) by

\[
 E_m=\{s:\text{there exists }n\geq0\text{ with }L_n(s)/L_0=q^m\}.
\]

For Lebesgue-almost every parameter the hierarchy continues indefinitely. Its exact-scale hit probability is

\[
 \boxed{u_m:=\frac{\operatorname{Leb}(E_m)}{\sqrt{2}}=\frac14+\frac{(-q^2)^m}{4}+\frac{q^m}{2}\left(\cos\frac{\pi m}{2}-\sin\frac{\pi m}{2}\right).}
\]

In particular, \(u_0=1\), \(u_1=0\), \(u_m\to1/4\), and the leading *finite-scale correction* is exactly four-periodic:

\[
\lim_{j\to\infty}q^{-(4j+r)}\left(u_{4j+r}-\frac14\right)
=\begin{cases}\frac12,&r=0,3,\\-\frac12,&r=1,2.\end{cases}
\quad r\in\{0,1,2,3\}.
\]

For every integer \(m\geq1\), let \(\tau_m=\min\{n\geq1:L_n/L_0\leq q^m\}\) and define the nonnegative lattice overshoot \(H_m\) through \(L_{\tau_m}/L_0=q^{m+H_m}\). Then \(H_m\) converges in distribution on \(\mathbb Z_{\geq0}\) to the explicit law

\[
\boxed{\lim_{m\to\infty}\Pr(H_m=k)=
\begin{cases}\frac14,&k=0,1,\\
q^k\left(\frac{k-1}{\sqrt{2}}+\frac12\right),&k\geq2.
\end{cases}}
\]

Write \(U(z)=\sum_{m\geq0}u_mz^m\). The overshoot law is also explicit at **every finite threshold**, not only in the limit. Writing \(F_k(z)=\sum_{m\geq1}\Pr(H_m=k)z^m\), one has

\[
F_0(z)=U(z)-1,\qquad F_1(z)=\frac{U(z)-1}{z},
\]

and for each integer \(k\geq2\),

\[
\boxed{F_k(z)=\frac{4q^{k+1}z[(k-1)-(k-2)qz]}{(1-z)(1+q^2z)(1+q^2z^2)}.}
\]

In particular, the exact finite-level identities \(\Pr(H_m=0)=u_m\) and \(\Pr(H_m=1)=u_{m+1}\) hold for all \(m\geq1\). These generating functions determine the entire threshold/overshoot distribution.

These are parameters sampled uniformly, not phase-space initial conditions sampled by planar area. This is one result about exact hits and first-passage overshoots in the same canonical nested geometric-scale hierarchy.

## Assumptions and scope

The source's notation is \(\alpha=\sqrt2\), \(\beta=q\), \(\omega=q^{-1}=1+\sqrt2\), the parameter interval \(I=[0,\alpha]\), and the Lüroth-type map \(f:I\to I\). Its intervals \(I_i\), indexed by integers \(i\), have length \(\alpha q^{|i|+1}\), and each interior branch maps affinely and bijectively onto \(I\), with absolute slope \(q^{-(|i|+1)}\) (Lowenstein–Vivaldi, equations (11)–(15), Section 5). The base-triangle renormalization parameter is \(r=f^2\); its similarity multiplier on a two-digit cylinder with digits \(i,j\) is

\[
\kappa=q^{|i|+|j|+2}=1/|r'|.
\]

This follows from Theorem 1(iii), the affine branch formula for \(r\), and the identity between the renormalization scale and reciprocal derivative. For the countable set of boundary/terminating exceptional parameters, branch choices may not be unique, but the events and probabilities are unchanged by any convention there. At every nonexceptional stage the relevant subtriangle is a geometrically similar copy of the preceding base-triangle prototype; \(L_n\) denotes the prototype length parameter \(l\), not its area, an individual periodic-tile diameter, or a physical return time.

Every claimed probability is with respect to normalized Lebesgue parameter measure \(ds/\sqrt2\). The result concerns the canonical subtriangle hierarchy, not every possible nested PWI domain or any arbitrary choice at a boundary bifurcation.

## Proof

**1. Independent Lüroth digits and geometric-scale increments.** The full-branch inverse of \(f\) maps a length-\(\alpha\) interval to a cylinder with relative length \(q^{|i|+1}\). Therefore for \(s\) uniform on \(I\) the digit sequence \((i_0,i_1,\ldots)\), read under iteration of \(f\), is independent, with

\[
\Pr(i_t=i)=q^{|i|+1},\qquad i\in\mathbb Z.
\]

Normalization follows from \(q+2q^2/(1-q)=1\), equivalent to \(q^2+2q=1\). Set \(X_t=|i_t|+1\), and pair the digits for one complete renormalization:

\[
Z_n=X_{2n}+X_{2n+1},\qquad S_n=\sum_{a=0}^{n-1} Z_a,\quad S_0=0.
\]

The variables \(Z_n\) are independent and identically distributed, \(Z_n\geq2\), and the source's scale identity gives \(L_n/L_0=q^{S_n}\). Since \(Z_n\geq2\), the sums strictly increase, \(S_n\to\infty\), and the hitting and crossing times are well defined with the stated convention.

The one-digit exponent law and probability generating function are

\[
\Pr(X=1)=q,\quad \Pr(X=j)=2q^j\ (j\geq2),\qquad
G(z)=\mathbb E[z^X]=\frac{qz(1+qz)}{1-qz}.
\]

Thus the full-step increment has generating function \(W(z)=G(z)^2\), with

\[
 w_2:=\Pr(Z=2)=q^2,\qquad
 w_j=4(j-2)q^j\quad(j\geq3),
\qquad \mathbb E Z=4.
\]

All series converge absolutely for \(|z|<q^{-1}\).

**2. Exact level-hitting probabilities.** Because each \(Z_n\geq2\), the positive sums cannot revisit an integer level. Conditioning on the first full renormalization yields the renewal recurrence

\[
 u_0=1,\qquad u_m=\sum_{j=2}^{m}w_j u_{m-j}\quad(m\geq1),
\]

where an empty sum is zero. With \(U(z)=\sum_{m\geq0}u_mz^m\), formal-power-series inversion gives

\[
 U(z)=\frac{1}{1-W(z)}
 =\frac{(1-qz)^2}{(1-z)(1+q^2z)(1+q^2z^2)}.
\]

Using only \(q^2+2q=1\), the *exact* partial fractions are

\[
 \boxed{U(z)=\frac{1}{4(1-z)}+\frac{1}{4(1+q^2z)}+\frac{1-qz}{2(1+q^2z^2)}.}
\]

The coefficients of the first two rational terms are \(1/4\) and \((-q^2)^m/4\). In the last term, the even coefficients are \((-q^2)^{m/2}/2\), and the odd coefficients are \(-q(-q^2)^{(m-1)/2}/2\). These two cases equal the claimed trigonometric expression. Dividing by \(q^m\), the remaining term \((-q)^m/4\) tends to zero, leaving the stated four-phase limits.

**3. Exact first-passage formula and limiting overshoot.** For \(m\geq1\) and \(k\geq0\), the last visited renewal level before crossing \(m\) is uniquely \(m-j\), with \(1\leq j\leq m\). Independence of the next increment gives the *finite-level exact identity*

\[
 \Pr(H_m=k)=\sum_{j=1}^{m}u_{m-j}\,w_{j+k}.
\]

Here \(w_0=w_1=0\) as above. Define \(F_k(z)=\sum_{m\geq1}\Pr(H_m=k)z^m\). The convolution gives

\[
F_k(z)=U(z)\sum_{j\geq1}w_{j+k}z^j.
\]

For \(k=0\), the inner series is \(W(z)\), so \(F_0=U-1\). For \(k=1\), it is \(W(z)/z\), so \(F_1=(U-1)/z\). For \(k\geq2\), one has

\[
\sum_{j\geq1}w_{j+k}z^j
=\frac{4q^{k+1}z[(k-1)-(k-2)qz]}{(1-qz)^2}.
\]

Substitute the earlier rational factorization of \(U\); the squared denominator cancels, proving the stated finite-threshold rational functions and the identities \(\Pr(H_m=0)=u_m\) and \(\Pr(H_m=1)=u_{m+1}\) for every integer \(m\geq1\).

The exact level formula implies \(u_n\to1/4\), and always \(0\leq u_n\leq1\). Since \(\sum_{j\geq1}w_{j+k}\leq1\), dominated convergence for series yields

\[
 \Pr(H_m=k)\longrightarrow
 \frac14\sum_{j\geq1}w_{j+k}
 =\frac14\Pr(Z\geq k+1).
\]

For \(k=0,1\), this is \(1/4\). For \(k\geq2\), summing the geometric-arithmetic tail gives

\[
\frac14\Pr(Z\geq k+1)
=\sum_{j=k+1}^{\infty}(j-2)q^j
=q^k\left(\frac{k-1}{\sqrt2}+\frac12\right),
\]

because \(q/(1-q)=1/\sqrt2\) and \(q^2/(1-q)^2=1/2\). These masses sum to one: \(\sum_{k\geq0}\Pr(Z\geq k+1)=\mathbb EZ=4\), so dividing by four gives total mass one. Therefore coordinatewise convergence gives convergence in distribution (indeed in total variation on the countable state space). The event \(H_m=0\) coincides with exact hit of \(m\), consistent with the earlier formula.

## Verification

An independent standard-library program `verify.py` checks paired-digit probabilities using exact operations in \(\mathbb Q(\sqrt2)\); constructs the renewal probabilities from the recurrence through level \(85\); checks the closed formula exactly at each level; and checks exact normalization of truncated overshoot distributions (including an analytically computed exact residual tail) at \(25\) thresholds. It also checks the exact normalization of the limiting overshoot distribution and 208 coefficients of the claimed finite-threshold rational functions. Execution result: `VERIFY_OK: 85 exact renewal levels; 84 exact paired-digit weights; 25 first-passage mass and k=0,1 checks; 208 exact rational overshoot coefficients`.

The finite checks are neither used nor asserted as a proof for all integer levels. The preceding rational generating-function identity and dominated-convergence argument are the infinite proofs. Reproduce with `python verify.py` from a directory containing the standalone file.

## Relationship to prior work

Lowenstein–Vivaldi (2014), especially Theorem 1 and Sections 4–5, supplies the planar PWI, the renormalization map \(f^2\), its geometric scale multiplier, and the full-branch symbolic coding. Those are prior results; the present contribution takes a *uniform parameter ensemble* and determines the exact probability of hitting every geometric lattice scale and the overshoot at the first threshold crossing.

Kesseböhmer–Munday–Stratmann (arXiv:1006.5693, Section 3, Lemma 3.1 and its proof) supplies a general renewal equation for generalized Lüroth sum-level sets and quotes the ordinary discrete renewal limit. Its general framework implies the existence of a reciprocal-mean hit limit after identifying the correct two-digit increment here. It does not state this particular rhombus geometric ensemble's rational generating-function factorization, exact all-level four-phase correction, or explicit first-crossing overshoot profile. The arithmetic/finite-scale content should not be confused with a new general renewal theorem.

Published mathematical-record searches and comparisons for piecewise-isometry renormalization scales, Lüroth renewal levels, and four-phase corrections did not identify an equivalent statement. This is not proof of absolute historical novelty; a hidden equivalent in related renormalization or symbolic-lattice literature remains possible.

## Limitations

The result concerns only the induced five-atom base-triangle hierarchy and one parameter family with normalized uniform parameter sampling. It does not establish distributions for planar initial conditions, physical return times, or exceptional-set Hausdorff dimensions. The scale uses *linear similarity ratio*, not area ratio. The endpoints and finite expansions form a Lebesgue-null exceptional set. The absence of an equivalent earlier theorem has not been independently certified; generic renewal theory accounts for the leading limit but not the displayed evaluated finite-scale formula. Computational verification is finite and supplementary.

## References

1. J. H. Lowenstein and F. Vivaldi, *Renormalization of a one-parameter family of piecewise isometries*, arXiv:1406.6910, first public 2014-06-26; full text, Theorem 1 and Sections 4–5. https://arxiv.org/abs/1406.6910
2. M. Kesseböhmer, S. Munday, and B. O. Stratmann, *Strong renewal theorems and Lyapunov spectra for \(\alpha\)-Farey and \(\alpha\)-Lüroth systems*, arXiv:1006.5693, first public 2010; particularly Section 3. https://arxiv.org/abs/1006.5693
