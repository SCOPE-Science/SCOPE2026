# Quadratic onset and harmonic resonance of nonuniform random-circle Rips loops

## Finding

Let \(n\ge4\) independent points be drawn on the circle of circumference one from a strictly positive normalized \(C^3\) density \(f\). In the first possible nontrivial loop window, write
\[
r=(1+h)/n,\qquad 0<h<1/(n-1).
\]
For the **inclusive geodesic** Vietoris--Rips complex, the circle-homotopy event \(E_{n,h}\) has the exact nonuniform probability
\[
\boxed{\mathbb P_f(E_{n,h})=h^{n-1}\,\mathbb E_V\int_0^1\prod_{j=0}^{n-1} f\bigl(t+j/n+h b_j(V)\bigr)\,dt,}
\]
where \(V=(V_1,\ldots,V_n)\) is uniform on the probability simplex, i.e. \(\operatorname{Dirichlet}(1,\ldots,1)\), and
\[
b_0=0,\qquad b_j(V)=j/n-\sum_{i=1}^jV_i\quad (1\le j\le n-1).
\]
The first two nonzero orders are
\[
\boxed{\mathbb P_f(E_{n,h})=h^{n-1}\bigl(C_n(f)+h^2D_n(f)+O_{n,f}(h^3)\bigr)}
\]
with no relative order-\(h\) term. Explicitly,
\[
C_n(f)=\int_0^1\prod_{j=0}^{n-1}f(t+j/n)\,dt
\]
and, writing \(F(t,a)=\prod_{j=0}^{n-1} f(t+a_j)\) with \(a_0=0\),
\[
D_n(f)=\frac12\sum_{j,k=1}^{n-1}\frac{\min(j,k)(n-\max(j,k))}{n^2(n+1)}\int_0^1\left.\partial_{a_j}\partial_{a_k}F(t,a)\right|_{a_j=j/n}\,dt.
\]
A second conclusion identifies the **conditional geometry**. Start the clockwise gaps at the labeled first sample point \(T=X_1\), and normalize their deficits by \(V_i=(r-g_i)/h\). Conditioned on the circle-homotopy event, \((T,V)\) converges in total variation as \(h\downarrow0\) to independent factors: \(V\) has \(\operatorname{Dirichlet}(1^n)\) distribution and \(T\) has density
\[
w_{n,f}(t)=C_n(f)^{-1}\prod_{j=0}^{n-1}f(t+j/n).
\]

There is a sharp **harmonic resonance** in the leading coefficient. For every integer \(k\ge1\) and \(0<|\epsilon|<1\), put \(f_{\epsilon,k}(t)=1+\epsilon\cos(2\pi kt)\). Then
\[
\boxed{C_n(f_{\epsilon,k})<1\text{ if }n\nmid k,\qquad C_n(f_{\epsilon,k})>1\text{ if }n\mid k.}
\]
If \(\gcd(k,n)=1\), the coefficient is exactly
\[
C_n(f_{\epsilon,k})=2^{1-n}\epsilon^n T_n(1/\epsilon),
\]
where \(T_n\) denotes the ordinary Chebyshev polynomial of the first kind. For example, for \(n=4\), the first harmonic has coefficient \(1-\epsilon^2+\epsilon^4/8\), whereas the fourth harmonic has coefficient \(1+3\epsilon^2+3\epsilon^4/8\). For \(f\equiv1\) the entire exact probability equals \(h^{n-1}\), as already known in the uniform circle-coverage law.

## Assumptions and scope

The circle is \(\mathbb R/\mathbb Z\) with its geodesic distance, and the Vietoris--Rips complex contains each finite subset of diameter at most \(r\). The sample size \(n\ge4\) is fixed. Samples are independent with the same strictly positive periodic density \(f\in C^3\) satisfying \(\int_0^1 f=1\). All asymptotics are as \(h\downarrow0\) at fixed \(n\) and fixed \(f\). Almost surely the sample points and gaps are distinct and nonzero. The open window \(0<h<1/(n-1)\) is equivalent to \(1/n<r<1/(n-1)\). The full integral formula and the deterministic gap criterion hold throughout that window; the expansion and conditional limit concern its lower endpoint.

## Proof

**1. Exact topological event.** Order the distinct points clockwise, and write their consecutive circular gaps as \(g_1,\ldots,g_n\), all positive and summing to one. If every \(g_i\le r\), every consecutive pair is connected by an edge. For any nonconsecutive pair, each circular arc joining them consists of at least two gaps; its length is at least \(1-(n-2)r>r\). Thus **the entire Rips graph is exactly the cycle graph** \(C_n\). Because \(n\ge4\), its clique complex is a circle. Conversely, if a gap exceeds \(r\), cut the circle inside that gap and unwrap the sample onto an interval of the real line. Any shortest circular arc crossing the removed gap has length exceeding \(r\), so adjacency is exactly unit-interval adjacency for the unwrapped coordinates. Its clique complex is the nerve of real intervals of equal length \(r\) and is homotopy equivalent to a disjoint union of real intervals, hence is never a circle. This proves \(E_{n,h}\iff\max g_i\le r\).

**2. Density and simplex change of variables.** Fix the first labeled point \(X_1=t\). As the remaining \(n-1\) labeled points are placed in clockwise order, the joint density of \((t,g_1,\ldots,g_{n-1})\), relative to circle length and the first \(n-1\) gap coordinates, is
\[
(n-1)!\prod_{j=0}^{n-1}f\bigl(t+s_j\bigr),\qquad s_0=0,\quad s_j=\sum_{i=1}^jg_i.
\]
The factorial counts the possible orderings of the remaining labels. On \(E_{n,h}\), define \(u_i=r-g_i\ge0\). Then \(\sum_i u_i=nr-1=h\), so \(u_i=hV_i\) with \(V\) in the standard simplex. The substitution has Jacobian \(h^{n-1}\). The uniform Dirichlet measure on that simplex has density \((n-1)!\) in its first \(n-1\) coordinates. Finally,
\[
s_j=jr-h\sum_{i=1}^jV_i=j/n+h\bigl(j/n-\sum_{i=1}^jV_i\bigr).
\]
Integration gives the claimed **exact** probability without approximation.

**3. Vanishing linear correction and the quadratic coefficient.** For \(V\sim\operatorname{Dirichlet}(1^n)\),
\[
\mathbb E b_j=0,\qquad
\mathbb E(b_jb_k)=\frac{\min(j,k)(n-\max(j,k))}{n^2(n+1)}
\quad(1\le j,k<n).
\]
These identities follow either from the standard Dirichlet covariances or by the beta distribution of partial sums. Taylor-expand the product \(F(t,a+h b(V))\) at \(a_j=j/n\) to order two. The expected first derivative vanishes because every \(\mathbb E b_j=0\). The expected quadratic term is precisely the covariance-weighted Hessian integral stated above. Since \(f\in C^3\), all third derivatives are bounded uniformly on the compact circle/simplex, and the expectation of the remainder is \(O_{n,f}(h^3)\). Multiplication by \(h^{n-1}\) proves the expansion.

**4. Conditional geometric limit.** The change of variables in step 2 gives, conditioned on \(E_{n,h}\), the joint Radon--Nikodym density of \((T,V)\) relative to \(dt\otimes\operatorname{Dirichlet}(1^n)\):
\[
\frac{\prod_{j=0}^{n-1} f(t+j/n+h b_j(V))}{\mathbb P_f(E_{n,h})/h^{n-1}}.
\]
The numerator converges uniformly to \(\prod_j f(t+j/n)\), and the denominator converges to its strictly positive integral \(C_n(f)\). Uniform convergence of the joint densities implies convergence in total variation and factorization of the stated limit.

**5. The Fourier-resonance dichotomy.** The shifts of the trigonometric density have arithmetic mean exactly one if \(n\nmid k\), since \(\sum_{j=0}^{n-1}\exp(2\pi i k j/n)=0\). Pointwise arithmetic--geometric mean gives \(\prod_j f_{\epsilon,k}(t+j/n)\le1\), with strict inequality except on a null set when \(\epsilon\ne0\). If \(n\mid k\), all shifts are equal and \(C_n=\int_0^1 f_{\epsilon,k}(t)^n dt>1\) by strict Jensen inequality. For \(\gcd(k,n)=1\), take the product of the \(n\) cosine shifts in the standard Chebyshev product identity, then integrate to remove the nonconstant \(n\)-fold cosine term. This gives the claimed exact coefficient. All steps apply for any fixed integer \(n\ge4\).

## Verification

Run `python verify.py` with Python 3 and NumPy available. The checker constructs random circular samples and verifies the exact graph dichotomy in 800 cases for five graph sizes. It checks 24 Fourier-density configurations (including resonance and the coprime Chebyshev identity). For \(n=4,5\), it independently integrates the Dirichlet simplex and circle coordinates numerically, comparing the exact probability integrand with the theoretical Hessian coefficient as \(h\) decreases. Its final status is `VERIFY_OK`. These checks are finite corroboration, not a replacement for the preceding unrestricted argument.

## Relationship to prior work

Park (arXiv:2610.26366, first posted 2026-10-19) calculates the full distribution of homotopy types for **uniform** random circle samples; in the present initial window its known probability is exactly \(h^{n-1}\), as also follows from classical Stevens circle-coverage formulas. Adamaszek and Adams (arXiv:1503.03669) give deterministic homotopy classification for all circular subsets, but do not state nonuniform fixed-\(n\) probability laws or conditional deficit distributions. Lim (arXiv:2305.16270) studies uniform random circular Čech topology and expectations rather than the density-dependent Vietoris--Rips onset expansion. General circle-covering work by Jewell and Romano (1982) allows nonuniform random arc placements and exact probabilities; it is important related literature but is not credited here with the conditional Dirichlet-shape limit, the vanishing relative linear term, or the harmonic-resonance theorem. The full text of that paper was not accessible for comparison, so possible implicit coverage remains a stated risk. Hüsler (1988) studies large-sample nonuniform maximal spacings under densities vanishing at a minimum; the present assumptions are fixed \(n\) and positive density. Its full text was also inaccessible. The exact integral identity is a change-of-variables formula for circular coverage, not claimed as independently novel absent the accompanying topological, conditional, and harmonic structure.

## Limitations

The theorem concerns fixed sample size, smooth strictly positive common sampling density, and only the first circle-homotopy window \(1/n<r<1/(n-1)\). It does not determine the full nonuniform homotopy distribution at larger scales, an asymptotic uniform in growing sample size, or distributions with atoms/zeros. The near-threshold expansion has a fixed-\(n\), fixed-density remainder. Prior circle-coverage literature may contain implicit specializations; independent mathematical review of originality has not been performed.

## References

1. Jaemin Park, *Homotopy distributions for Vietoris--Rips complexes of random circle samples*, arXiv:2610.26366, first posted 2026-10-19, https://arxiv.org/abs/2610.26366.
2. Michal Adamaszek and Henry Adams, *The Vietoris--Rips complexes of a circle*, arXiv:1503.03669; Pacific Journal of Mathematics **290** (2017), 1--40, https://arxiv.org/abs/1503.03669.
3. Uzu Lim, *Strange Random Topology of the Circle*, arXiv:2305.16270, https://arxiv.org/abs/2305.16270.
4. Nicholas P. Jewell and Joseph P. Romano, *Coverage problems and random convex hulls*, Journal of Applied Probability **19** (1982), 546--561, https://doi.org/10.2307/3213513.
5. Jürg Hüsler, *Maximal, non-uniform spacings and the coverage problem*, Journal of Applied Probability **25** (1988), 519--528, https://doi.org/10.2307/3213981.
6. W. L. Stevens, *Solution to a geometrical problem in probability*, Annals of Eugenics **9** (1939), 315--320; classical uniform circle-coverage law.
