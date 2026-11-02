# Arithmetic protection and exceptional moment modes in a biased harmonically trapped run-and-tumble process

## Finding

Consider a one-dimensional run-and-tumble particle driven by a linearly restoring trap and two unequal orientation-flip rates. Write \(Z=\kappa X/v\), with \(v,\kappa>0\), and let \(\sigma\in\{-1,+1\}\). The flow is \(\dot Z=\kappa(\sigma-Z)\). The flip \(+1\to-1\) has rate \(a>0\), and \(-1\to+1\) has rate \(b>0\). Set \(\delta=(a+b)/\kappa\).

For every nonnegative integer \(N\), the backward generator on the invariant polynomial observable space
\[
\mathscr P_N=\{P(Z)+\sigma Q(Z):\deg P,\deg Q\le N\}
\]
has eigenvalues, with algebraic multiplicity,
\[
\{-j\kappa:0\le j\le N\}\ \cup\ \{-(j\kappa+a+b):0\le j\le N\}.
\]
If \(\delta\notin\mathbb N\), the operator is diagonalizable on every \(\mathscr P_N\). If \(\delta=m\in\mathbb N\), then **every** coincident eigenvalue \(-j\kappa\), \(m\le j\le N\), is semisimple, for all \(N\), precisely when **both** \(a/\kappa\) and \(b/\kappa\) are positive integers. Otherwise each such coincident eigenvalue has exactly one nontrivial Jordan block of size two. All other eigenvalues are simple. Thus integer total switching-to-trap ratios produce moment exceptional points generically, but splitting that integer into two positive integer rates protects the entire moment hierarchy.

In particular, for symmetric flipping \(a=b\) the resonant integer \(m\) is protected exactly when \(m\) is even. Bias can reveal a Jordan block at an otherwise protected even resonance, or eliminate one at an odd resonance. These are statements about all finite-degree polynomial observables, **not** a determination of the entire spectrum on an infinite-dimensional Banach or Hilbert space.

## Assumptions and scope

All three parameters \(a,b,\kappa\) and the propulsion speed \(v\) are strictly positive and constant. Flip times are exponential and independent conditional on orientation. There is no translational Brownian noise, no resetting and no time spent in a zero-speed tumble state. Initial \(Z\) may be anywhere in the invariant interval \([-1,1]\) and either orientation may be used. Markov expectations preserve \(\mathscr P_N\) by the exact generator equation.

Normalize time by \(\kappa\): \(A=a/\kappa\), \(B=b/\kappa\), \(m=A+B\). For the proof at an integer resonance \(m\), use \(u=(Z+1)/2\) and write a polynomial observable as the pair \((f_+(u),f_-(u))\). Its dimensionless generator is
\[
\mathcal L f_+=(1-u)f_+'+A(f_- -f_+),\qquad
\mathcal L f_-=-u f_-'+B(f_+ -f_-).
\]
The distinction between *orientation flip rate* and *orientation redraw rate* is material: symmetric independent redraws at rate \(2a\) have the same generator as symmetric flips at rate \(a\).

## Proof

**Step 1 (triangular moment hierarchy).** Put \(h=(b-a)/(a+b)\), \(q=\sigma-h\), \(p_j=Z^j\), \(q_j=qZ^j\). Since \(\mathcal L\sigma=-(a+b)(\sigma-h)\) and \(q\sigma=1-h^2-hq\), direct differentiation gives
\[
\begin{split}
\mathcal Lp_j&=-j\kappa p_j+j\kappa h p_{j-1}+j\kappa q_{j-1},\\
\mathcal Lq_j&=-(j\kappa+a+b)q_j+j\kappa(1-h^2)p_{j-1}-j\kappa hq_{j-1}.
\end{split}
\]
Terms with coefficient \(j=0\) vanish. In the degree filtration these equations have diagonal blocks \(\operatorname{diag}(-j\kappa,-j\kappa-a-b)\), proving the displayed eigenvalue multiset. A noninteger \(\delta\) makes all diagonal eigenvalues distinct, hence gives diagonalizability.

**Step 2 (the first collision is exactly classified).** Suppose \(a+b=m\kappa\), \(m\ge1\) integer, and divide the generator by \(\kappa\). On \(\mathscr P_m\) the eigenvalue \(-m\) has algebraic multiplicity two. The obvious eigenvector is \(q=\sigma-h\), which is independent of position. A second independent eigenvector exists if and only if an eigenfunction with nonzero leading positional term of degree \(m\) exists.

For such an eigenfunction \((f_+,f_-)\), eliminate the minus component from \(\mathcal L f=-m f\). The plus component \(F=f_+\) must satisfy
\[
u(1-u)F''+[-A+(m-1)u]F'=0,\qquad
f_-=-\frac BA F-\frac{1-u}{A}F'.
\]
A first integral is
\[
F'(u)=C u^{A}(1-u)^{B-1}.
\]
For \(C\ne0\) this is a polynomial of degree \(m-1\) if and only if \(A\) and \(B\) are positive integers: analyticity at both endpoints forces integral nonnegative exponents, and their sum is \(m-1\). Conversely, when both are integers, integrate this monomial product and use the displayed formula for \(f_-\); it gives a second polynomial eigenfunction of degree \(m\). When they are not, only \(C=0\) gives a polynomial solution, which is the already identified degree-zero orientation eigenfunction. Thus the double eigenvalue is semisimple precisely at the positive-integer splits; otherwise it is one size-two Jordan block.

**Step 3 (every higher collision behaves identically).** The derivative \(D=\partial_Z\) satisfies the exact commutator \(D\mathcal L=\mathcal LD- D\) for the dimensionless generator. Therefore differentiating an eigenfunction at \(-j\) gives an eigenfunction at \(-(j-1)\). Conversely, if \(f\) is a polynomial eigenfunction at \(-j\), take any polynomial primitive \(F\) with \(DF=f\). Then \((\mathcal L+(j+1))F\) is position-independent. It can be canceled by a position-independent orientation function because \(\mathcal L+(j+1)\) is invertible on that two-dimensional space whenever \(j+1>m\). Consequently a degree-\(m\) second eigenfunction lifts recursively to a new, independent degree-\(j\) eigenfunction at every \(-j\), \(j>m\). Conversely a degree-\(j\) second eigenfunction, differentiated \(j-m\) times, would produce the forbidden degree-\(m\) second eigenfunction. At each collision there are exactly two algebraic copies and at least the low-degree orientation-sector eigenfunction, so failure of the second eigenfunction gives exactly one Jordan block of size two. This completes the classification.

**Step 4 (observable dynamical consequence).** A size-two Jordan block at \(-j\kappa\) yields a nonzero \(t e^{-j\kappa t}\) term in an appropriate conditional polynomial expectation or stationary polynomial correlation; away from the defective locus each finite-degree polynomial expectation is a finite linear combination of pure exponentials. For a directly observable lowest-degree witness, take \(a+b=2\kappa\) and \(h=(b-a)/(a+b)\). The coefficient multiplying \((\sigma_0-h)t e^{-2\kappa t}\) in \(\mathbb E[Z_t^2\mid Z_0=z,\sigma_0]\) is exactly \(-4\kappa h\). It is nonzero for unequal flip rates and vanishes at \(a=b=\kappa\), where the double eigenvalue is semisimple. For symmetric \(a=b=3\kappa/2\), the coefficient multiplying \(\sigma_0 t e^{-3\kappa t}\) in the conditional cubic moment is \(-3\kappa/2\). Both follow by exponentiating the four- or six-dimensional exact moment matrix; their expressions are reproduced and tested in the supplied standalone verifier.

## Verification

Run `python3 verify_moment_spectrum.py` with standard Python. It independently constructs the generator from the two physical orientation equations, checks rational characteristic polynomials, ranks and Jordan defects over multiple truncation degrees, tests integral-split protection and nonintegral splits, and verifies the quadratic and cubic defective-time coefficients using rational resolvent algebra. All calculations are finite exact-arithmetic checks, not substitutes for the parameter-uniform proof. This paper's theorem is specifically about polynomial moment subspaces; finite truncations are not used to infer any unproved full-function-space spectral completeness.

## Relationship to prior work

Sun, Ye and Chen (arXiv:2610.24961v1, first public 2026-10-18) construct conditional position/velocity moment distributions of a run-and-tumble particle in a harmonic field. Their Section III, equations (21)–(26), addresses the symmetric zero-tumble-time limit, and their broader analysis includes stationary distributions and general moment methods. In particular, their symmetric all-order moment denominators already expose coinciding poles at certain rate ratios: that symmetric-pole observation is not asserted to be novel here. Their asymmetric *run-versus-tumble* rates concern a different three-velocity-state process than the two unequal *orientation-flip* rates classified here.

Sun, Ye and Podgornik (arXiv:2409.00578, first public 2024-09-01) derive arbitrary-order harmonic-trap moments with finite tumble times. Mallmin, Blythe and Evans (arXiv:1810.00813, first public 2018-10-01) identify exceptional points and polynomially modified relaxation on a finite lattice ring, including a two-particle exclusion model. That work demonstrates the broader exceptional-point mechanism, but its lattice spectral branches and finite-size crossing condition do not determine the biased harmonic-trap polynomial hierarchy or the integer-split protection criterion here.

The new mathematical contribution is the exact if-and-only-if all-order classification at **unequal orientation-switching rates**, including the protection of a coincident moment spectrum only at positive-integer partitions of the total rate, and the associated observable biased even-resonance witness. A prior general formula for Markov-modulated harmonic filters could conceivably imply it after a nontrivial specialization; see the review for this residual priority risk.

## Limitations

This is a classification of the generator restricted to finite-degree polynomial observables and of their exact time evolution; it is not a claim that the full generator has only these eigenvalues or that non-polynomial observables lack other exceptional phenomena. No translational diffusion, stochastic resetting, nonexponential switching or finite-duration zero-speed tumble is included. The physical value of the exact resonance is structural and dynamical; robustness under small perturbations is not asserted. The novelty assessment is qualified best-knowledge, with no independent audit or external priority certification.

## References

1. A. Sun, F. Ye and J. Z. Y. Chen, *Run-and-tumble particles in a harmonic external field: constructing the solution of the Fokker–Planck equation from the equations of motion*, arXiv:2610.24961v1 (2026-10-18), https://arxiv.org/html/2610.24961v1.
2. A. Sun, F. Ye and R. Podgornik, *Exact moments for a run and tumble particle with a finite tumble time in a harmonic trap*, arXiv:2409.00578 (2024-09-01), https://arxiv.org/pdf/2409.00578.
3. E. Mallmin, R. A. Blythe and M. R. Evans, *Exact spectral solution of two interacting run-and-tumble particles on a ring lattice*, arXiv:1810.00813 (2018-10-01), https://arxiv.org/pdf/1810.00813.
