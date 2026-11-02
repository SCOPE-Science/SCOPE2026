# Three-branch-value collision geometry and full symmetric monodromy for sparse Euler critical points

## Finding

For all integers \(q\ge3\), consider the first nontrivial primitive sparse one-variable support \(A=\{0,1,q\}\) and the normalized polynomial \(f_\epsilon(t)=1+t+\epsilon t^q\). Put \(\epsilon_q=(-1)^q(q-1)^{q-1}/q^q\). When \(\epsilon\notin\{0,\epsilon_q\}\), the logarithmic Euler critical-point cover, with exponent ratio \(r=\nu/s\), is a degree-\(q\) map with full geometric monodromy \(S_q\). Its finite collision polynomial is
\[
D_q(r,\epsilon)=(-1)^q(q-1)^{q-1}(r+1)^q-q^q\epsilon r^{q-1}(r+q).
\]
For each allowed \(\epsilon\), this polynomial has \(q\) simple zeros, all corresponding to ordinary double collisions at nonzero points outside \(f_\epsilon=0\). The cover also branches at infinity over \(r=-q\) with index \(q-1\); this is **not** a finite critical-point collision.

On normalizing the algebraic collision-parameter correspondence \(D_q=0\), its projection to the coefficient coordinate \(\epsilon\) becomes the degree-\(q\) rational map
\[
E_q:\mathbb P^1_r\longrightarrow\mathbb P^1_\epsilon,\qquad
E_q(r)=\epsilon_q\frac{(r+1)^q}{r^{q-1}(r+q)}.
\]
The only branch values are \(0\), \(\infty\), and \(\epsilon_q\), with ramification partitions \((q)\), \((q-1,1)\), and \((2,1^{q-2})\), respectively. Thus \(E_q\) is a Belyi map and has geometric monodromy \(S_q\).

## Assumptions and scope

All curves and covers are over \(\mathbb C\). We require integer \(q\ge3\), coefficient \(\epsilon\in\mathbb C^*\setminus\{\epsilon_q\}\), and \(s\in\mathbb C^*\). The very affine critical-point domain is \(U_\epsilon=\{t\in\mathbb C^*:f_\epsilon(t)\ne0\}\). The Euler integrand is \(f_\epsilon(t)^s t^\nu\), understood through its logarithmic derivative, and \(r=\nu/s\). Geometric monodromy refers to the finite branched cover of projective parameter lines, whose generic fibers are the critical solutions; special resonant fibers must not be read as regular very-affine fibers.

## Proof

**1. The critical-point cover.** Its critical equation is \(r f_\epsilon(t)+t f_\epsilon'(t)=0\), equivalently
\[
P_{\epsilon,r}(t)=\epsilon(r+q)t^q+(r+1)t+r=0.
\]
Solving for \(r\) defines the rational map
\[
R_\epsilon(t)=-\frac{t f_\epsilon'(t)}{f_\epsilon(t)}.
\]
The numerator and denominator are coprime: at a common nonzero zero, both \(f_\epsilon\) and \(f_\epsilon'\) would vanish, forcing \(\epsilon=\epsilon_q\), while the numerator has no root at \(t=0\) in common with \(f_\epsilon(0)=1\). Hence \(R_\epsilon\) has degree \(q\). Moreover \(f_\epsilon\) is squarefree under the stated assumptions.

**2. Ramification and collision.** Direct differentiation gives
\[
R_\epsilon'(t)=-\frac{N_\epsilon(t)}{f_\epsilon(t)^2},\qquad
N_\epsilon(t)=1+q^2\epsilon t^{q-1}+(q-1)^2\epsilon t^q.
\]
Its derivative is
\[
N_\epsilon'(t)=q(q-1)\epsilon t^{q-2}\bigl(q+(q-1)t\bigr).
\]
Since \(N_\epsilon(0)=1\) and \(N_\epsilon(-q/(q-1))=1-\epsilon/\epsilon_q\), all \(q\) roots of \(N_\epsilon\) are simple under the hypotheses. None is a zero of \(f_\epsilon\): if a root of \(f_\epsilon\) were a ramification point, the displayed derivative formula together with \(f_\epsilon=0\) would force a multiple root of \(f_\epsilon\). They therefore yield \(q\) simple finite ramification points of the map, with transposition local monodromies.

At infinity, put \(u=1/t\). The identity
\[
R_\epsilon(t)+q=\frac{q+(q-1)t}{f_\epsilon(t)}
\]
yields \(R_\epsilon+q\sim(q-1)u^{q-1}/\epsilon\). Thus \(t=\infty\) has ramification index \(q-1\) over \(r=-q\), with one further unramified finite point of that fiber. Together the contributions \(q\) and \(q-2\) total \(2q-2\), exactly the Riemann–Hurwitz ramification degree of a degree-\(q\) rational map.

For a finite multiple root of \(P_{\epsilon,r}\), one has \(P=\partial_t P=0\), and elimination gives precisely
\[
D_q(r,\epsilon)=(-1)^q(q-1)^{q-1}(r+1)^q-q^q\epsilon r^{q-1}(r+q)=0.
\]
In particular the usual degree-\(q\) polynomial discriminant is, up to an overall sign, \([\epsilon(r+q)]^{q-2}D_q\). The factor at \(r=-q\) is caused by the drop in polynomial degree and captures ramification at \(t=\infty\), not an actual collision of two points of \(U_\epsilon\).

**3. Distinct finite branch values.** Solving \(D_q(r,\epsilon)=0\) for the coefficient yields \(\epsilon=E_q(r)\). Its logarithmic derivative is the exact identity
\[
\frac{E_q'(r)}{E_q(r)}=-\frac{q(q-1)}{r(r+1)(r+q)}.
\]
The map \(E_q\) has degree \(q\). Its critical points are \(r=-1\), \(r=0\) for \(q>2\), and \(r=\infty\), as analyzed below. Hence every finite, nonzero target value distinct from \(\epsilon_q\) has \(q\) distinct preimages. These are all finite and avoid \(r=-q,0,-1\), so the corresponding collisions occur at simple ramification points of \(R_\epsilon\) in \(U_\epsilon\).

**4. Full symmetric critical monodromy.** Let \(G\le S_q\) be the monodromy of the connected rational cover \(R_\epsilon:\mathbb P^1\to\mathbb P^1\). The local permutation \(\rho\) about \(r=-q\) is a cycle of length \(q-1\) fixing one label. Other branch permutations are transpositions because their ramification is simple. The monodromy group is generated by these local permutations. If every transposition preserved the fixed label of \(\rho\), the full group would preserve it, contradicting connectedness. Therefore some transposition \(\tau\) joins the fixed label to a label in the \((q-1)\)-cycle. The conjugates \(\rho^j\tau\rho^{-j}\) are the \(q-1\) star transpositions connecting that label to all others; they generate \(S_q\). Hence \(G=S_q\).

**5. Rational Belyi collision correspondence.** Because \(D_q(r,\epsilon)\) is linear in \(\epsilon\) and has no nontrivial common factor between its two coefficient polynomials, its irreducible projective correspondence has rational function field \(\mathbb C(r)\), with normalization \(\mathbb P^1_r\) and \(\epsilon=E_q(r)\). At \(r=-1\), the numerator has multiplicity \(q\), giving ramification partition \((q)\) over \(\epsilon=0\). At \(r=0\), the denominator has pole order \(q-1\), and at \(r=-q\) it has a simple pole, giving partition \((q-1,1)\) over \(\infty\). The expansion at \(r=\infty\) has \(E_q(r)=\epsilon_q+O(r^{-2})\) with a nonzero quadratic coefficient (by the logarithmic derivative identity); hence it has ramification index two over \(\epsilon_q\), and the other \(q-2\) points of that fiber are simple. Riemann–Hurwitz, with \((q-1)+(q-2)+1=2q-2\), excludes further ramification. The branch values are exactly the stated three. The monodromy of this connected degree-\(q\) map contains a \((q-1)\)-cycle and a transposition, whose supports must connect the fixed label by transitivity; the same star-transposition argument proves full \(S_q\).

## Verification

A standalone exact-symbolic script `verify.py` checks the critical equation, derivative, collision resultant factorization, logarithmic derivative identity, and exceptional-coefficient identity for each integer \(q\) from \(3\) through \(8\). The script prints `VERIFY_OK` only if every assertion succeeds. These finite tests are consistency checks; the all-\(q\) result is proved by the preceding symbolic identities, elementary divisor theory on \(\mathbb P^1\), and monodromy arguments, not inferred from the finite tests.

## Relationship to prior work

Goertz, Sturmfels, and Telen introduce logarithmic \(A\)-discriminants, establish their general geometry, and in Example 6.4 state the bidegree and leading-coefficient data for primitive supports \(\{0,p,q\}\). The present statement concerns the **normalized primitive trinomial subfamily \(p=1\)** and identifies the complete *projective branch profiles of two natural one-parameter covers*, together with full symmetric geometric monodromy uniformly in every smooth coefficient specialization. The discriminant polynomial by itself is elementary sparse-resultant algebra and is not treated as a separate new theorem. Classical theory of trinomials and Belyi coverings supplies conceptual background, but neither general existence of Belyi maps nor arithmetic Galois groups of fixed trinomials directly determines these exponent-ratio critical-point and collision covers.

## Limitations

The result does not cover \(q=2\), singular or degree-dropping coefficients \(\epsilon=\epsilon_q\) and \(\epsilon=0\), general sparse support \(\{0,p,q\}\) with \(p>1\), or higher-dimensional supports. The compactified rational covers contain resonance and infinity fibers that need not represent valid very-affine critical points. Literature priority remains subject to fuller comparison with classical explicitly parametrized three-point covers; an equivalent passport formula may already be known independently of logarithmic Euler critical points.

## References

- M. Goertz, B. Sturmfels, S. Telen, *The Logarithmic A-Discriminant*, arXiv:2610.29204v1 (first public version 2026-10-21), particularly §§2–3 and Example 6.4. https://arxiv.org/html/2610.29204v1
- H. Garmi, *Galois Groups of Trinomials with Small Coefficients*, arXiv:2610.22764 (2026). https://arxiv.org/abs/2610.22764
- Z. Scherr and M. E. Zieve, *Separated Belyi Maps*, Mathematical Research Letters 21 (2014), 1389–1406. https://websites.umich.edu/~zieve/papers/mochizuki.html
