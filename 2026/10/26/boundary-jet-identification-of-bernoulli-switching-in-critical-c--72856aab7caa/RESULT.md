# Boundary-jet identification of Bernoulli switching in critical-cusp dynamics

## Finding
Fix two distinct parameters \(1<\theta_0<\theta_1<2\). Let \(c=1/2\),
\[
 K_j=\frac{1-\theta_j/2}{\sqrt 2},\qquad
 f_{\theta_j}(c\pm t)=1-\theta_j t-2K_j\sqrt t
 \quad(0\le t\le1/2).
\]
At each step independently select \(f_{\theta_0}\) with probability \(1-p\) and \(f_{\theta_1}\) with probability \(p\). Let \(P_p=(1-p)P_{\theta_0}+pP_{\theta_1}\) be the annealed transfer operator. The existing critical-cusp spectral-gap theorem guarantees an \(\varepsilon_0\in(0,1)\) for which each \(0\le p<\varepsilon_0\) has a normalized stationary density \(h_p\in W^{2,1}(0,1)\).

**Theorem (two-jet exact identification and three-jet mixing test).** For every such \(p\), \(h_p(c)>0\) and there are unique Peano coefficients \(\alpha_1(p),\alpha_2(p),\alpha_3(p)\) satisfying
\[
 h_p(1-z)=\alpha_1z+\alpha_2z^2+\alpha_3z^3+o(z^3)
 \qquad(z\downarrow0).
\]
Define known positive quantities
\[
 a_j=K_j^{-2},\qquad r_j=\theta_j K_j^{-2}
 =\frac{8\theta_j}{(2-\theta_j)^2}\quad(j=0,1)
\]
and the observable boundary ratio \(t=-4\alpha_2/(3\alpha_1)\). Then \(r_0<r_1\), \(r_0\le t<r_1\), and the mixing probability is reconstructed **without knowing the stationary density at the cusp**:
\[
 \boxed{\displaystyle
 p=\frac{a_0(t-r_0)}{a_0(t-r_0)+a_1(r_1-t)}.}
\]
Moreover, the three coefficients obey the exact nonnegative identity
\[
 \boxed{\displaystyle
 9\alpha_1\alpha_3-10\alpha_2^2
 =\frac{45}{8}h_p(c)^2p(1-p)a_0a_1(r_1-r_0)^2.}
\]
Thus this third-order boundary-jet discriminant vanishes precisely for the unmixed law \(p=0\) within the stated interval, and is strictly positive for every nontrivial Bernoulli mixture \(0<p<\varepsilon_0\). **Its sign tests for genuine switching without knowing either of the two shape parameters**, provided they are distinct members of the stated family. The ratio \(t(p)\) is strictly increasing, with
\[
 \frac{dt}{dp}=\frac{a_0a_1(r_1-r_0)}{[(1-p)a_0+pa_1]^2}>0.
\]
The inverse is consequently locally and uniformly stable throughout the admissible compact subintervals of mixing probabilities.

## Assumptions and scope
The maps, their common cusp position and value, the two distinct shape parameters, and the independent Bernoulli sampling law are all specified above. The existence/regularity input is exactly the \(W^{2,1}\) stationary density supplied by Oltiboev--Vafoyev, arXiv:2610.23180v1, Theorem 6.1, for a possibly nonexplicit sufficiently small mixing interval. The conclusion does not assert existence for every \(0<p<1\), nor does it require or assume ordinary three-times differentiability of \(h_p\) at the boundary: the displayed expansion is a *third-order Peano jet*.

## Proof
**1. Exact inverse-branch weights.** Fix \(\theta\in(1,2)\) and abbreviate \(K=(1-\theta/2)/\sqrt2\). Put \(z=1-x\) and
\[
 u(z)=\frac{\sqrt{K^2+\theta z}-K}{\theta}.
\]
The two preimages of \(1-z\) are \(c\pm u(z)^2\). Formula (3.4) of the source, or direct inverse differentiation, gives for every \(g\in C^1[0,1]\)
\[
 (P_\theta g)(1-z)
 =w_\theta(z)\,[g(c-u(z)^2)+g(c+u(z)^2)],\qquad
 w_\theta(z)=\frac{u(z)}{K+\theta u(z)}
 =\frac{1}{\theta}\left(1-\frac K{\sqrt{K^2+\theta z}}\right).
\]
In particular \(u(z)^2=O(z^2)\) and \(w_\theta(z)=O(z)\).

**2. The weak regularity is sufficient.** The one-dimensional Sobolev embedding gives \(W^{2,1}(0,1)\subset C^1[0,1]\). For such a \(g\), continuity of \(g'\) and cancellation of the odd linear terms show
\[
 g(c-u^2)+g(c+u^2)=2g(c)+o(u^2)=2g(c)+o(z^2).
\]
The elementary binomial expansion of the *explicit* weight is
\[
 2w_\theta(z)=\frac{z}{K^2}
 -\frac{3\theta z^2}{4K^4}
 +\frac{5\theta^2z^3}{8K^6}+O(z^4).
\]
Multiplying yields the genuine Peano asymptotic, with a remainder \(o(z^3)\),
\[
 (P_\theta g)(1-z)=g(c)\left[
 \frac{z}{K^2}-\frac{3\theta z^2}{4K^4}
 +\frac{5\theta^2 z^3}{8K^6}\right]+o(z^3).
\]
This step does not silently assume that \(g''\) is continuous or that a third derivative exists.

**3. Strict positivity at the cusp.** The stationary density is nonnegative, continuous, and integrates to one. Suppose \(h_p(c)=0\). The identity \(h_p=P_ph_p\), valid pointwise because both sides have continuous representatives, expresses its zero at \(c\) as a sum of nonnegative inverse-branch values. Because \(1-p>0\), both preimages of \(c\) under \(f_{\theta_0}\) are zeros. Repeating at these preimages forces zeros on every iterated inverse image of \(c\) under \(f_{\theta_0}\). These preimages are dense: both monotone branches map onto \([0,1]\), and their inverse branches are contractions by at most \((1+\theta_0/2)^{-1}<1\); each nested branch cylinder contains a preimage of \(c\). Continuity would imply \(h_p\equiv0\), contradicting normalization. Hence \(h_p(c)>0\).

**4. Solve the inverse problem.** Set
\[
 A=(1-p)a_0+pa_1,\quad
 B=(1-p)a_0r_0+pa_1r_1,\quad
 C=(1-p)a_0r_0^2+pa_1r_1^2.
\]
Combining Step 2 for the two maps with \(h_p=P_ph_p\) gives exactly
\[
 \alpha_1=h_p(c)A,\qquad
 \alpha_2=-\frac34h_p(c)B,\qquad
 \alpha_3=\frac58h_p(c)C.
\]
Thus \(t=B/A\), a strictly increasing weighted mean of \(r_0,r_1\): note that \(\theta/(K_\theta^2)=8\theta/(2-\theta)^2\) strictly increases with \(\theta\in(1,2)\). Rearranging \((1-p)a_0(t-r_0)=pa_1(r_1-t)\) gives the stated unique formula for \(p\). Differentiating the linear-fractional expression for \(t(p)\) gives the derivative in the theorem.

**5. Detect genuine switching.** Direct expansion of these two weighted moments gives
\[
 AC-B^2=p(1-p)a_0a_1(r_1-r_0)^2.
\]
Substituting the three coefficient formulas yields
\(9\alpha_1\alpha_3-10\alpha_2^2=(45/8)h_p(c)^2(AC-B^2)\). Strict positivity for \(0<p<\varepsilon_0\) and equality for \(p=0\) follow from Step 3 and \(r_1>r_0\). This completes the proof.

## Verification
The accompanying self-contained `verify.py` checks the inverse-branch Taylor coefficients symbolically, the moment discriminant and inverse map exactly, and a rational-parameter algebraic example. Running `python3 verify.py` with SymPy installed reproduces `verify_output.txt`. These computations are checks of the finite algebra only; the Sobolev argument, density positivity and all-parameter assertions above are proved analytically.

## Relationship to prior work
Oltiboev and Vafoyev, *Critical cusp cancellation and analytic response for a Bernoulli random interval map* (arXiv:2610.23180v1), introduce this critical square-root family, its explicit inverse branches, a \(W^{2,1}\) spectral gap and the existence of analytic stationary-density response for small Bernoulli mixing. Proposition 5.1 also gives a **leading-order** cusp-value boundary trace under its more general assumptions. None of those results states that the first two boundary coefficients uniquely recover the Bernoulli selection probability or that the third satisfies the strict variance discriminant above. The earlier Oltiboev--Rakhimov--Ruziboev work (arXiv:2608.26969v1) covers a different, strictly subcritical cusp-exponent range and treats linear response rather than this inverse problem. This theorem uses those existence results as premises, not as new claims.

## Limitations
The two shape parameters must be known and distinct; one cannot infer unknown map shapes simultaneously from this two-coefficient formula. Only the small-mixing range supported by the cited existence theorem is asserted. The boundary coefficients are theoretical asymptotic jets, not noisy finite-difference estimates, so statistical estimation error is not analyzed. The third-order statement is a Peano expansion; a classical third boundary derivative is not proved. More general finite mixtures have analogous weighted-moment identities if a \(W^{2,1}\) stationary density is known to exist, but the two-map inverse formula does not identify arbitrary many mixing weights.

## References
1. D. Oltiboev and F. Vafoyev, *Critical cusp cancellation and analytic response for a Bernoulli random interval map*, arXiv:2610.23180v1 (first submitted 16 October 2026), especially Sections 3--6.
2. D. Oltiboev, K. Rakhimov and M. Ruziboev, *Linear response for random systems with a cusp*, arXiv:2608.26969v1 (first submitted 27 August 2026), Sections 2--4.
3. W. Bahsoun, M. Ruziboev and B. Saussol, *Linear response for random dynamical systems*, Advances in Mathematics **364** (2020), 107011 (general background only).
