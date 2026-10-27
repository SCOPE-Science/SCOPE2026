# Universal sharp midpoint extension on every regular Euclidean polygon

## Finding
For each integer \(n\ge3\), let \(v_j=(\cos(2\pi j/n),\sin(2\pi j/n))\), and let \(m_j=(v_j+v_{j+1})/2\), with indices modulo \(n\). Give \(V=\{v_j\}\) and \(Y=V\cup\{m_j\}\) their inherited **Euclidean chord distances**, not their cycle-graph distances. For any nonzero real Banach space \(Z\), consider bounded real-linear extension operators from \(\operatorname{Lip}(V;Z)\) to \(\operatorname{Lip}(Y;Z)\), reproducing all original values, with operator norm measured by Lipschitz seminorms (or equivalently after fixing one base point).

Put \(a=\pi/n\), \(r=\cos a\), and
\[
\Lambda_n=\frac{2\cot(a/2)}{\displaystyle\sum_{j=0}^{n-1}\sqrt{1+r^2-2r\cos((2j-1)a)}}.
\]
**The least extension-operator norm is exactly \(\Lambda_n\) for every \(n\ge3\) and every nonzero real Banach target space.** The infimum ranges over all real-linear extensions, including nonsymmetric, nonpositive or signed-coefficient operators. An explicit positive, dihedrally equivariant Markov extension attains it, and its restrictions to the added midpoint layer are even \(1\)-Lipschitz. Moreover \(\Lambda_n>1\) at every finite \(n\) and \(\Lambda_n\to1\) as \(n\to\infty\).

Write \(d_j=\|v_j-m_0\|_2\), \(S=2\cot(a/2)\), and \(c=\cos a\). The optimal probability weights for \(m_0\) are explicitly
\[
w_j=\frac{\Lambda_n}{4\sin a}\bigl(d_{j-1}+d_{j+1}-2c\,d_j\bigr)>0,
\qquad\sum_{j=0}^{n-1}w_j=1.
\]
At \(m_i\), use these weights rotated by \(i\): \((Ef)(m_i)=\sum_j w_{j-i}f(v_j)\), and set \((Ef)(v_j)=f(v_j)\). In addition to optimality, the weights satisfy \(w_0=w_1>w_2=w_{n-1}\ge w_3=w_{n-2}\ge\cdots\), interpreted in successive shells around the midpoint axis.

## Assumptions and scope
Only the ordinary Euclidean distance is used. The problem is *linear simultaneous extension* of arbitrary Banach-valued Lipschitz data, not Kirszbraun extension into Hilbert space or scalar nonlinear McShane extension. A finite-n upper bound is not inferred from numerical experiments; all identities and inequalities below hold for every integer \(n\ge3\). The theorem includes previously evaluated low-order regular polygons, but its new scope is the full unbounded family and a uniform constructive certificate.

## Proof
**1. Universal lower bound, including signed asymmetric extensions.** Every finite-norm linear extension preserves constant functions (their Lipschitz seminorm is zero), so its value at \(m_0\) is a linear combination \(\sum_j t_j f(v_j)\) with \(\sum_j t_j=1\), without any positivity hypothesis. For each \(k\), the real datum \(f_k(v_j)=\|v_j-v_k\|_2\) is \(1\)-Lipschitz, vanishes at \(v_k\), and therefore gives
\[
\sum_j t_j\|v_j-v_k\|_2\le \|E\|\,\|m_0-v_k\|_2.
\]
Summing over \(k\), each column of the vertex-distance matrix has the same total \(S=\sum_{k=0}^{n-1}2\sin(ka)=2\cot(a/2)\). Hence \(S\le\|E\|\sum_k d_k\), proving \(\|E\|\ge\Lambda_n\). For general \(Z\), restrict the operator to data \(f_kz\) for a fixed unit vector \(z\in Z\), and apply a norm-one functional taking value one on \(z\); the same argument applies.

**2. Inverse chord-distance identity.** Let \(D_{jk}=\|v_j-v_k\|_2=2\sin(a\,\operatorname{dist}_{\mathrm{cyc}}(j,k))\), and let \(T\) denote cyclic shift. The elementary sine recurrence, including the cusp at zero, gives
\[
(T+T^{-1}-2cI)D=4\sin a\,I.
\]
Consequently \(D\) is invertible and \(w=\frac{\Lambda_n}{4\sin a}(T+T^{-1}-2cI)d\) satisfies
\[
Dw=\Lambda_n d.
\]
Summing coordinates shows \(\sum_jw_j=\Lambda_n(2-2c)\sum_jd_j/(4\sin a)=1\), since \(S=2\sin a/(1-c)\).

**3. Positive, radially decreasing Ptolemy weights.** For any \(x\) strictly inside the circumcircle, Euclidean Ptolemy inequality applied to \((v_{j-1},v_j,v_{j+1},x)\) yields
\[
\|x-v_{j-1}\|_2+\|x-v_{j+1}\|_2>2c\,\|x-v_j\|_2,
\]
where the factor \(2c\) is the ratio of the outer chord to either adjacent chord. At \(x=m_0\), this proves \(w_j>0\).

The required *shell monotonicity* also has a direct analytic proof, rather than being guessed from plots. Set \(h=2a\), \(r=c<1\), and \(u(\theta)=\sqrt{1+r^2-2r\cos\theta}\). Direct differentiation gives the Pinney-type identity
\[
u''(\theta)+\tfrac14u(\theta)=\frac{(1-r^2)^2}{4u(\theta)^3}=:F(\theta).
\]
By variation of constants, the discrete Ptolemy defect is
\[
u(\theta+h)+u(\theta-h)-2\cos(h/2)u(\theta)
=\int_{-h}^{h}2\sin\bigl((h-|s|)/2\bigr)F(\theta+s)\,ds.
\]
The integrand kernel is nonnegative, even and nonincreasing in circular distance from zero. The function \(F\) is strictly positive, even and strictly decreasing in circular distance from zero. Their convolution on the circle is therefore even and nonincreasing in circular distance: by layer-cake representation this reduces to the elementary fact that the overlap of two centered circular arcs cannot increase when the centers separate through an angle from zero to \(\pi\). Evaluating at \(\theta=(2j-1)a\) proves the asserted shell monotonicity of \(w\) (strictness is unnecessary for the construction).

**4. A positive convolution factorization.** Write \(\eta_i=(\delta_{v_i}+\delta_{v_{i+1}})/2\). Since \(w\) is symmetric and nonincreasing in successive two-vertex shells about the axis through \(m_0\), there is a nonnegative probability vector \(\rho\) on the cyclic index group such that
\[
w=\rho*\eta_0.
\]
Here is a constructive verification. Put \(a_k=w_{k+1}=w_{-k}\) in the paired shells. For \(n=2q+1\), set \(\rho_q=a_q\) at the unique opposite vertex index class, and define \(\rho_k=2a_k-\rho_{k+1}\) for \(k=q-1,\ldots,0\), followed by \(\rho_{-k}=\rho_k\). For \(n=2q\), set \(\rho_q=0\), define \(\rho_k=2a_k-\rho_{k+1}\) for \(k=q-1,\ldots,0\), and again reflect. Each coefficient is an alternating sum of a nonnegative decreasing sequence and so is nonnegative (pair adjacent successive differences). These formulas give \(w_j=(\rho_j+\rho_{j-1})/2\) at every index; summing shows \(\sum_j\rho_j=\sum_jw_j=1\).

**5. All added-point pairs are contractive.** The two-point measures \(\eta_i\) have an explicit cross-coupling, sending half the mass from \(v_i\) to \(v_{k+1}\) and the other half from \(v_{i+1}\) to \(v_k\). For \(i\ne k\), its cost is
\[
\frac{\|v_i-v_{k+1}\|_2+\|v_{i+1}-v_k\|_2}{2}
=c\,\|v_i-v_k\|_2=\|m_i-m_k\|_2,
\]
by the same chord sine recurrence. Thus \(W_1(\eta_i,\eta_k)\le\|m_i-m_k\|_2\). Because \(\mu_i:=\rho*\eta_i\) is a common-mixture of rotated \(\eta\)'s, using the same rotation in both marginals yields
\[
W_1(\mu_i,\mu_k)\le\|m_i-m_k\|_2.
\]
For a midpoint and an original vertex, the only coupling to a Dirac mass gives
\[
W_1(\mu_i,\delta_{v_k})=\sum_jw_{j-i}\|v_j-v_k\|_2=\Lambda_n\|m_i-v_k\|_2
\]
by step 2. For vertex pairs, reproduction has constant one. Every probability-measure coupling yields the same Lipschitz estimate for arbitrary Banach-valued data by the triangle inequality. Hence \(\|E\|\le\Lambda_n\), and step 1 gives equality.

**6. Strict amplification and limiting value.** Convexity of Euclidean norm gives \(d_j\le(\|v_j-v_0\|_2+\|v_j-v_1\|_2)/2\), with strict inequality for at least one \(j\) since \(n\ge3\). Summing gives \(\sum_jd_j<S\), so \(\Lambda_n>1\). Riemann sums and \(r=\cos(\pi/n)\to1\) show that both normalized sums \(S/n\) and \((\sum_jd_j)/n\) tend to \(4/\pi\). Thus \(\Lambda_n\to1\).

## Verification
Run `python verify_polygon.py` with the dependencies in `requirements.txt`. It independently reconstructs Euclidean distance matrices, checks the inverse-distance identity, positivity, shell monotonicity, the nonnegative cyclic convolution, and, with linear programming, every distinct midpoint-pair transport class for \(3\le n\le30\). This finite corroboration does not certify the universal theorem; steps 1–6 above are the proof.

## Relationship to prior work
Bruè, Di Marino and Stra construct general random-measure linear Lipschitz extensions on doubling sets (2018), without sharp constants for this explicit finite midpoint configuration. Basso (2021) connects relative Lipschitz-free projection constants with extension questions and finite linear programming, but does not state this regular-polygon all-order formula; his 2023 exposition focuses on general explicit upper constants. Earlier special computations determine the square, regular pentagon, and regular hexagon separately. Those special cases are included here and are **not** claimed separately novel. The assessed extension is an unrestricted all-order classification with one Ptolemy-positive kernel and a uniform probabilistic contraction proof.

## Limitations
This concerns real-linear extensions for the chord metric, a regular Euclidean polygon, and its *edge* midpoints. It does not assert nonlinear or complex-linear optimality, general irregular polygons, facet centroids in higher dimensions, or prescribed interpolation support. The displayed \(\Lambda_n\) is an exact finite sum; no unproved higher-order asymptotic coefficient is asserted. Independent mathematical review has not been performed.

## References
- Elia Bruè, Simone Di Marino, Federico Stra, *Linear Lipschitz and \(C^1\) extension operators through random projection*, arXiv:1801.07533, first public 23 January 2018, especially Sections 3–4.
- Giuliano Basso, *Absolute Lipschitz extendability and linear projection constants*, arXiv:2104.14238, first public 29 April 2021, especially Sections 1 and 5.
- Giuliano Basso, *Lipschitz extension theorems with explicit constants*, arXiv:2310.13554, first public 20 October 2023, Sections 1–2.
