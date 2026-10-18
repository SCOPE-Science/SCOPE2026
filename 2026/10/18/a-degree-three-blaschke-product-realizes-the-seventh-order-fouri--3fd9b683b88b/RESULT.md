# A degree-three Blaschke product realizes the seventh-order Fourier exponent optimally

## Finding

Define the finite Blaschke product
\[
B(z)=\frac{6z^{3}-9z^{2}+5z-1}{6-9z+5z^{2}-z^{3}}
=\prod_{a\in A}\frac{z-a}{1-\overline a z},
\quad A=\left\{\frac12,\frac12+\frac{i\sqrt3}{6},\frac12-\frac{i\sqrt3}{6}\right\}.
\]
For every integer \(n\ge1\), let \(c_n(k)=\widehat{B^n}(k)\) be its Taylor/Fourier coefficients. Then
\[
\lim_{n\to\infty}n^{1/7}c_n(7n)
=\frac{\Gamma(1/7)\cos(\pi/14)}{7\pi\,6^{1/7}}>0,
\qquad
\sup_{k\ge0}|c_n(k)|\asymp n^{-1/7}.
\]
Moreover, **three is the minimum degree** among all finite Blaschke products whose Fourier coefficient supremum decays comparably to \(n^{-1/7}\). The displayed rational function is a degree-three witness attaining the minimum.

## Assumptions and scope

The disk is \(\mathbb D=\{z\in\mathbb C:|z|<1\}\). A degree-\(m\) finite Blaschke product is \(e^{i\alpha}\prod_{j=1}^{m}(z-a_j)/(1-\overline{a_j}z)\), with all zeros \(a_j\in\mathbb D\) counted with multiplicity. Coefficients use normalized boundary Haar measure:
\[
\widehat{B^n}(k)=\frac1{2\pi}\int_{-\pi}^{\pi}B(e^{i\theta})^n e^{-ik\theta}\,d\theta,
\qquad k\ge0.
\]
The notation \(X_n\asymp Y_n\) means two-sided bounds with positive constants independent of \(n\) for all sufficiently large \(n\). The minimality statement ranges over all finite degrees, including unimodular rotations and monomials.

## Proof

**Factorization and the phase identity.** The three indicated zeros belong to \(\mathbb D\), since their absolute values are \(1/2\) and \(1/\sqrt3\). Expanding their product gives the rational formula; thus \(|B(e^{i\theta})|=1\) and \(B(1)=1\). Choose a continuous phase \(\psi\) with \(B(e^{i\theta})=e^{i\psi(\theta)}\) and \(\psi(0)=0\). Standard differentiation of the Blaschke factors gives
\[
\psi'(\theta)=\sum_{a\in A}\frac{1-|a|^2}{|e^{i\theta}-a|^2}.
\]
Set \(t=\tan(\theta/2)\). Under the Cayley coordinate \(w=(1+\overline a)/(1-\overline a)=u+iv\), an individual summand is
\[
\frac{u(1+t^2)}{1+2vt+(u^2+v^2)t^2}.
\]
For our three zeros the \(w\)-values are \(3\) and \(2\pm i\sqrt3\). With \(x=t^2\), direct addition yields
\[
\psi'(\theta)=\frac{7(1+x)(1+10x+57x^2)}{(1+9x)(1+2x+49x^2)}
=7-\frac{2688x^3}{(1+9x)(1+2x+49x^2)}. \tag{1}
\]
The denominator is positive for \(x\ge0\), so \(\psi'(\theta)=7\) only when \(\theta\equiv0\pmod{2\pi}\). Differentiating with respect to \(x\),
\[
\frac{d\psi'}{dx}=-\frac{2688x^2(3+22x+67x^2)}{(1+9x)^2(1+2x+49x^2)^2}<0\quad(x>0). \tag{2}
\]
Hence \(\psi''\) vanishes only at \(\theta\equiv0,\pi\pmod{2\pi}\). At the origin, \(t=\theta/2+O(\theta^3)\), and (1) implies
\[
\psi'(\theta)=7-42\theta^6+O(\theta^8),\qquad
\psi(\theta)=7\theta-6\theta^7+O(\theta^9). \tag{3}
\]
Thus \(\psi''\) has a zero of order five at the origin. At \(\theta=\pi\), (1) gives the nonzero quadratic term
\[
\psi'(\pi+h)=\frac{19}{21}+\frac{2144}{9261}h^2+O(h^4), \tag{4}
\]
so \(\psi''\) has a simple zero there. All phase normalizations and endpoint orders have therefore been fixed explicitly.

**Uniform upper bound.** Consider the oscillatory integral with phase \(\phi_{n,k}(\theta)=n\psi(\theta)-k\theta\). Its second derivative is \(n\psi''(\theta)\), independent of \(k\). On a fixed small punctured neighborhood of zero, \(|\psi''(\theta)|\asymp|\theta|^5\); near \(\pi\), \(|\psi''(\theta)|\asymp|\theta-\pi|\); elsewhere it is bounded away from zero. The inner interval of radius \(n^{-1/7}\) about zero contributes at most \(O(n^{-1/7})\) by length. The adjacent dyadic annulus of distance \(r\) from zero contributes at most \(O((nr^5)^{-1/2})\), uniformly in \(k\), by the standard second-derivative van der Corput bound. Summing annuli with \(r=2^j n^{-1/7}\) gives \(O(n^{-1/7}\sum_{j\ge0}2^{-5j/2})=O(n^{-1/7})\). The analogous argument at \(\pi\), starting at radius \(n^{-1/3}\), gives \(O(n^{-1/3})\); the remaining finitely many intervals give \(O(n^{-1/2})\). Consequently \(\sup_{k\ge0}|c_n(k)|=O(n^{-1/7})\).

**Matching coefficient and its constant.** Take precisely \(k=7n\). The derivative of the phase \(\psi(\theta)-7\theta\) is strictly negative away from \(\theta=0\), so a fixed complementary arc contributes \(O(n^{-1})\) by integration by parts. On a small arc about zero, (3) and the substitution \(s=(6n)^{1/7}\theta\) give the order-seven stationary-phase limit. Truncating first at bounded \(|s|\), then controlling the tails by one integration by parts using \(|(\psi-7\theta)'|\asymp |\theta|^6\), yields
\[
\lim_{n\to\infty}n^{1/7}c_n(7n)
=\frac{6^{-1/7}}{2\pi}\int_{-\infty}^{\infty}e^{-is^7}\,ds
=\frac{\Gamma(1/7)\cos(\pi/14)}{7\pi\,6^{1/7}}.
\]
The last equality follows by substituting \(u=s^7\) and using the Euler gamma integral in its oscillatory form for exponent \(1/7\). The constant is strictly positive. Combined with the upper estimate, this proves the claimed \(n^{-1/7}\) norm law.

**Sharp lower bound on degree.** Let \(C\) be an arbitrary degree-\(m\) finite Blaschke product whose boundary phase \(\eta\) has nonconstant derivative. Center the angular coordinate at any \(\theta_0\) and set \(t=\tan((\theta-\theta_0)/2)\). Applying the same Cayley calculation to the rotated zeros yields
\[
\eta'(\theta)=(1+t^2)\sum_{j=1}^{m}
\frac{u_j}{1+2v_jt+(u_j^2+v_j^2)t^2},\qquad u_j>0.
\]
After taking a common denominator, the numerator and denominator have degree at most \(2m\), and the denominator is nonzero at \(t=0\). Since \(\eta'\) is nonconstant, the difference \(\eta'(\theta)-\eta'(\theta_0)\) cannot vanish to order greater than \(2m\). Thus every zero of \(\eta''\) has multiplicity at most \(2m-1\). There are finitely many such zeros on the circle. The same local dyadic second-derivative argument gives the uniform estimate
\[
\sup_{k\ge0}|\widehat{C^n}(k)|=O\bigl(n^{-1/(2m+1)}\bigr).
\]
In particular, for \(m=1\) or \(m=2\) this is \(O(n^{-1/5})=o(n^{-1/7})\), incompatible with two-sided \(n^{-1/7}\) decay. If \(\eta'\) is constant, \(C\) is a unimodular multiple of a monomial and its Fourier coefficient supremum is exactly one. Degree zero likewise cannot realize the stated decay. No degree below three can therefore work, and the exhibited degree-three product is optimal.

## Verification

The reproducible standard-library script `verify.py` checks the exact polynomial identity behind (1), the positive derivative polynomial in (2), the product factorization, and pointwise phase slopes. Its output is in `verification_output.txt`. For \(n=100,500,2000\), numerical boundary quadrature gives respective values approximately \(0.232147247\), \(0.229289573\), \(0.227752040\) for \(n^{1/7}c_n(7n)\), approaching the proved constant \(0.224736169\). The exact identities and the analytic proof, not these finite calculations, establish the infinite assertion.

## Relationship to prior work

Borichev, Fouchet, and Zarouf (arXiv:2401.17520v1, Theorems 1–2, Section 5.3) gave a general phase-degeneracy law and an explicit **degree-four** product with \(n^{-1/7}\) coefficient-supremum decay; their text asks for the minimum possible degree for specified decay exponents. The present theorem answers that degree question at exponent \(1/7\) by a different, degree-three construction, proves the matching degree lower bound, and gives the explicit leading constant for one Fourier coefficient. Their general theorem supplies contextual support but does not itself supply this cubic witness. Their earlier arXiv:2107.00405 treats powers of a **single** Blaschke factor and Airy-type, rather than seventh-order, transitions. Searches of named-result archives and literature found no stronger covering result; this is a best-knowledge originality assessment, not a universal uniqueness certificate.

## Limitations

The theorem does not determine minimum degrees for other exponents (notably \(1/6\) or exponents \(1/N\) with \(N\ge8\)); it does not classify all degree-three witnesses, quantify convergence rates, or compute the exact leading asymptotic constant for the **supremum** over all coefficients. The coefficient limit is proved only at \(k=7n\), while the supremum is proved comparable up to constants. No numerical extrapolation is used as a proof.

## References

1. A. Borichev, K. Fouchet, R. Zarouf, *On the Fourier coefficients of powers of a finite Blaschke product*, arXiv:2401.17520v1, first posted 2024-01-31; subsequently *International Mathematics Research Notices*, DOI 10.1093/imrn/rnae199. Especially Theorems 1–2 and Section 5.3. https://arxiv.org/html/2401.17520v1
2. A. Borichev, K. Fouchet, R. Zarouf, *On the Fourier coefficients of powers of a Blaschke factor and strongly annular functions*, arXiv:2107.00405v1, first posted 2021-07-01. https://arxiv.org/html/2107.00405v1
3. Standard van der Corput second-derivative lemma and Euler oscillatory gamma integral; both are used with their hypotheses verified above.
