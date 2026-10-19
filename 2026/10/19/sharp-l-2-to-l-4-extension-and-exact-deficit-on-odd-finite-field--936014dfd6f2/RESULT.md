# Sharp \(L^2\)-to-\(L^4\) extension and exact deficit on odd finite-field hyperbolas

## Finding
For every odd prime power \(q\ge3\), put \(n=q-1\) and
\[
H_q=\{h(t)=(t,t^{-1}):t\in\mathbb F_q^\times\}\subset\mathbb F_q^2.
\]
For any nontrivial additive character \(\psi\) of \(\mathbb F_q\), define the finite-field extension operator
\[
\mathcal E_q f(\xi,\eta)=\frac1n\sum_{t\in\mathbb F_q^\times}f(t)\psi(\xi t+\eta t^{-1}).
\]
Here the input norm is normalized \(L^2(H_q)\), while the output norm uses *unnormalized counting measure* on \(\mathbb F_q^2\). The exact sharp estimate is
\[
\boxed{\|\mathcal E_q f\|_{\ell^4(\mathbb F_q^2)}^4\le\frac{3q^2(q-2)}{(q-1)^3}\|f\|_{L^2(H_q)}^4.}
\]
A nonzero \(f\) is an equality case if and only if every coefficient has the same positive modulus and its antipodal products agree:
\[
|f(t)|=\rho>0,\qquad f(t)f(-t)=\alpha\quad\text{for all }t\ne0,
\]
for some \(\alpha\in\mathbb C\) of modulus \(\rho^2\). These conditions allow an independent phase on each antipodal pair and are generally less restrictive than being the restriction of an additive character.

There is additionally an *exact three-term deficit decomposition*, not merely an optimal constant. Put \(k=n/2\), and choose one representative \(t\) from every pair \(\{t,-t\}\). Define
\[
A_t=|f(t)|^2+|f(-t)|^2,\quad B_t=2f(t)f(-t),\quad
M=\sum_{t\ne0}|f(t)|^2,\quad B=\sum_{\{t,-t\}}B_t.
\]
For the unnormalized additive-energy fourth moment
\[
\mathcal Q(f)=\sum_{z\in\mathbb F_q^2}\left|\sum_{\substack{u,v\in\mathbb F_q^\times\\h(u)+h(v)=z}}f(u)f(v)\right|^2,
\]
one has, for every complex-valued \(f\),
\[
\boxed{\begin{aligned}
(3-3/n)M^2-\mathcal Q(f)
={}&\sum_{\{t,-t\}}(A_t-M/k)^2\\
&+\frac12\sum_{\{t,-t\}}|B_t-B/k|^2\\
&+\left(1-\frac1{2k}\right)(M^2-|B|^2).
\end{aligned}}
\]
Every displayed term on the right is nonnegative. In particular, a small fourth-moment deficit forces both pairwise mass equidistribution and near-maximal antipodal-product coherence.

## Assumptions and scope
The ground field is \(\mathbb F_q\) for any odd prime power \(q\), including nonprime extension fields, and the additive character \(\psi\) is arbitrary but nontrivial. The subset \(H_q\) is the nonzero level of the *split* binary quadratic form \((x,y)\mapsto xy\). Since \(q\) is odd, \(n\) is even and there are exactly \(k=(q-1)/2\) disjoint antipodal pairs. No assumption of real-valuedness, positivity or nonvanishing is placed on \(f\) in the inequality or deficit identity.

The normalized input norm is \(\|f\|_{L^2(H_q)}^2=M/n\). There is no normalization on the dual output: \(\|F\|_{\ell^4(\mathbb F_q^2)}^4=\sum_{(\xi,\eta)\in\mathbb F_q^2}|F(\xi,\eta)|^4\).

## Proof
**Step 1: sum-fiber geometry.** Write \(h(t)=(t,t^{-1})\). If
\[
h(u)+h(v)=(x,y)\ne(0,0),
\]
then \(x=u+v\) and \(y=(u+v)/(uv)\), so \(x,y\) are both nonzero and \(uv=x/y\). Therefore \(\{u,v\}\) is the unique unordered pair of roots, when it exists, of
\[
Z^2-xZ+x/y=0.
\]
Thus every nonzero sum has a unique unordered representation, including diagonal pairs \(u=v\). At sum zero, the ordered pairs are precisely \((t,-t)\) for every \(t\in\mathbb F_q^\times\).

**Step 2: exact fourth moment.** Character orthogonality gives
\[
\|\mathcal E_q f\|_{\ell^4}^4=\frac{q^2}{n^4}\mathcal Q(f).
\]
Each non-antipodal unordered pair contributes \(4|f(u)f(v)|^2\), each diagonal contributes \(|f(t)|^4\), and the exceptional zero-sum fiber contributes \(|B|^2\). Consequently,
\[
\begin{aligned}
\mathcal Q(f)&=2M^2-\sum_{t\ne0}|f(t)|^4
-4\sum_{\{t,-t\}}|f(t)f(-t)|^2+|B|^2\\
&=2M^2-\sum_{\{t,-t\}}\left(A_t^2+\tfrac12|B_t|^2\right)+|B|^2.
\end{aligned}
\]
In the second identity use \(A_t^2=|f(t)|^4+|f(-t)|^4+2|f(t)f(-t)|^2\).

**Step 3: exact deficit and sharpness.** Subtract this expression from \((3-3/n)M^2\), and complete two squares using
\[
\sum(A_t-M/k)^2=\sum A_t^2-M^2/k,\qquad
\sum|B_t-B/k|^2=\sum|B_t|^2-|B|^2/k.
\]
The displayed three-term deficit identity follows. The last term is nonnegative because
\[
|B|\le\sum_{\{t,-t\}}2|f(t)f(-t)|\le\sum_{\{t,-t\}}A_t=M.
\]
All three terms therefore vanish exactly when \(A_t=M/k\), all \(B_t=B/k\), and \(|B|=M\). Equality throughout the triangle and arithmetic-geometric inequalities forces \(|f(t)|=|f(-t)|\) on every pair and all antipodal products to share a common phase. Since \(A_t\) is independent of the pair, every \(|f(t)|\) is equal; equality is equivalent to the stated modulus and product conditions. Conversely those conditions make each deficit term zero. A constant nonzero \(f\) exhibits sharpness. Finally substitute \(M=n\|f\|_{L^2(H_q)}^2\) into the orthogonality identity; the fourth-power sharp constant is \(3q^2(n-1)/n^3=3q^2(q-2)/(q-1)^3\).

## Verification
A self-contained Python 3 program, `verify_hyperbola.py`, independently constructs each field, computes every two-point sum fiber, evaluates convolution moments directly, compares them with the exact deficit formula, and evaluates the full two-dimensional finite Fourier sum without using an FFT. It checks fields \(\mathbb F_3\), \(\mathbb F_5\), \(\mathbb F_7\), \(\mathbb F_9\) and \(\mathbb F_{11}\); the extension field uses the irreducible polynomial \(T^2+1\) over \(\mathbb F_3\). The executed program reports `VERIFY_OK` for 225 coefficient tests, 12,825 direct Fourier frequencies, and five independently constructed equality examples. These are finite corroborations, not the proof for unrestricted \(q\).

## Relationship to prior work
Iosevich and Koh [1] proved uniform \(L^2\to L^4\) estimates for nondegenerate quadratic surfaces in odd finite fields, using pair-sum incidence bounds. Their Theorem 2 and Section 4 provide bounds up to an unspecified universal multiplicative constant; they do not supply the exact constant, antipodal equality manifold, or the above quantitative deficit for this split hyperbola.

González-Riquelme and Oliveira e Silva [2] developed sharp finite-field extension inequalities for a parabola in two ambient dimensions, paraboloids, and a hyperbolic paraboloid in three ambient dimensions. Their hyperbolic paraboloid is \(\{(x,y,z):z=x^2-y^2\}\), not the level-one binary hyperbola here. González-Riquelme and Ismoilov [3] classify sharp extension on homogeneous quadratic cones in four ambient dimensions; those domains and normalizations do not imply this level-one curve classification. These works motivate exact constants and equality analysis but do not state the present result.

## Limitations
The theorem only treats the split level-one hyperbola in *odd* finite characteristic. It makes no assertion about even characteristic, anisotropic conics, higher-dimensional quadrics, or sharp constants for other Fourier exponents. Finite tests do not prove the unrestricted theorem. A historical general theorem about antipodal pair-sum collisions might yield an equivalent abstract formulation; published-source comparisons cannot certify priority.

## References
[1] A. Iosevich and D. Koh, *Extension theorems for the Fourier transform associated with non-degenerate quadratic surfaces in vector spaces over finite fields*, arXiv:0804.4505v1, first public April 28, 2008, Theorem 2 and Section 4. https://arxiv.org/html/0804.4505v1

[2] C. González-Riquelme and D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647v2 (first public May 26, 2024), Theorems 1.1 and 1.4 and Section 1. https://arxiv.org/html/2405.16647v2

[3] C. González-Riquelme and T. Ismoilov, *Maximizers of the \(L^2\to L^4\) Fourier extension inequality for cones in finite fields*, arXiv:2509.05600v2 (first public September 6, 2025), Theorems 1–2 and Section 1. https://arxiv.org/html/2509.05600v2
