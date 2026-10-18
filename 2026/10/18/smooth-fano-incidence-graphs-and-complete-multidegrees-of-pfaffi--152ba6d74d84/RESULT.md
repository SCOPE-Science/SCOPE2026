# Smooth Fano incidence graphs and complete multidegrees of Pfaffian parametrizations

## Finding

Let \(n=2k+1\ge5\) be odd. Let \(V\) be a complex vector space of dimension \(n+1\), and choose a general projective \(n\)-plane \(L=\mathbb P(W_0)\subset\mathbb P(\bigwedge^2V^*)\), where \(\dim W_0=n+1\). Let \(\pi\cong\mathbb P^{n-1}\subset\mathbb P(V)\) be a general hyperplane. Write \(A(u)\) for the alternating form parametrized by \(u\in L\), and let \(\mathcal C\subset L\) be the Pfaffian hypersurface \(\operatorname{Pf}(A(u))=0\), of degree \((n+1)/2\).

The Bolognesi–Ciliberto–Verra rational parametrization \(\varphi:\pi\dashrightarrow\mathcal C\) has graph closure
\[
\Gamma=\{(p,u)\in\pi\times L:A(u)p=0\}.
\]
For general \(L\) and \(\pi\), this graph is a **smooth irreducible Fano variety of dimension \(n-1\)** with
\[
K_\Gamma\cong\mathcal O_\Gamma(-1,-1).
\]
Writing \(h\) and \(q\) for the hyperplane classes from \(\pi\) and \(L\), its entire Chow class is
\[
[\Gamma]=\sum_{j=0}^{n-1}a_jh^jq^{n-j},\qquad
 a_j=\sum_{i=0}^{j}(-2)^{j-i}\binom{n+1}{i}.
\]
Consequently, its complete projective multidegree sequence, defined by
\[
\delta_j=\int_\Gamma h^{n-1-j}q^j\quad(0\le j\le n-1),
\]
is \(\delta_j=a_j\). Equivalently, the sequence is the truncation through degree \(n-1\) of the power series \((1+t)^{n+1}/(1+2t)\). In particular, for \(n=5\) it is \((1,4,7,6,3)\), and for \(n=7\) it is \((1,6,16,24,22,12,4)\).

## Assumptions and scope

All varieties are over \(\mathbb C\). The integer \(n\) is odd and at least five. Generality means membership in a nonempty Zariski-open subset of the parameter space of \((n+1)\)-dimensional subspaces \(W_0\subset\bigwedge^2V^*\) and hyperplanes \(\pi\subset\mathbb P(V)\). The parametrization is the one that maps a general point \(p\in\pi\) to the unique \(u\in L\) satisfying \(A(u)p=0\); equivalently it is the complete linear system of hypersurfaces of degree \(n-1\) through the prescribed focal base locus, as in the originating theorem. The bidegree convention puts \(\delta_0\) at the source and \(\delta_{n-1}\) at the target; it is not the reversed convention sometimes used for inverse maps.

## Proof

**1. The incidence is a regular zero scheme.** Set \(N=\binom{n+1}{2}\) and let \(\mathcal U\subset\pi\times\mathbb P(\bigwedge^2V^*)\) be the universal incidence of pairs \((p,[\omega])\) with \(\omega(p,-)=0\). For each \(p\), contraction is a surjection from \(\bigwedge^2V^*\) to the \(n\)-dimensional annihilator of the line \(p\) in \(V^*\). Consequently \(\mathcal U\) is the projectivization of a vector bundle of rank \(N-n\) over \(\pi\): it is smooth and irreducible of dimension \(N-2\). The locus \(\Gamma=\mathcal U\cap(\pi\times L)\) is obtained by intersecting \(\mathcal U\) with \(N-n-1\) general hyperplanes pulled back from the second factor, hence has dimension \(n-1\). These hyperplane systems are base-point-free; successive Bertini smoothness applies.

For irreducibility, the projection of \(\mathcal U\) to the full space of forms has image the irreducible Pfaffian hypersurface and is generically one-to-one: a general singular alternating form has a two-dimensional kernel, whose projective line meets the fixed hyperplane \(\pi\) at one point. Thus the successive general hyperplane sections are also irreducible by the irreducible Bertini theorem, since their images have dimension greater than one throughout. Therefore \(\Gamma\) is smooth, irreducible, and of expected codimension \(n\) in \(\pi\times L\).

More intrinsically, contraction of the universal alternating form with the universal point defines a section of
\[
E=\operatorname{pr}_1^*(\Omega^1_{\mathbb P(V)}(2)|_\pi)\otimes\operatorname{pr}_2^*\mathcal O_L(1),
\]
a rank-\(n\) bundle. Its zero scheme is exactly \(\Gamma\), so it is a regular section. Over a dense open set of \(\pi\), the \(n\) independent linear conditions \(A(u)p=0\) determine one point \(u\in L\). The corresponding projection \(\Gamma\to\pi\) is birational; by irreducibility, \(\Gamma\) is the closure of the graph of \(\varphi\). The image is the Pfaffian hypersurface because any matrix with a nonzero kernel has zero Pfaffian, and the resulting image has the expected dimension. This also recovers the cited birational parametrization without assuming that its graph is nonsingular.

**2. Chow class and multidegrees.** The twisted Euler sequence on \(\mathbb P(V)\) is
\[
0\longrightarrow\Omega^1_{\mathbb P(V)}(2)\longrightarrow\mathcal O(1)^{n+1}\longrightarrow\mathcal O(2)\longrightarrow0.
\]
Thus, on \(\pi\),
\[
c(\Omega^1_{\mathbb P(V)}(2)|_\pi)=\frac{(1+h)^{n+1}}{1+2h}.
\]
Since \(\Gamma\) is the regular zero of \(E\), its fundamental class is \(c_n(E)\). The tensor-product Chern-root rule gives
\[
c_n(E)=\sum_{j=0}^{n}c_j(\Omega^1_{\mathbb P(V)}(2)|_\pi)q^{n-j}
=\sum_{j=0}^{n-1}a_jh^jq^{n-j},
\]
where \(h^n=0\) in \(A^*(\pi\times L)\). Multiplying by \(h^{n-1-i}q^i\) and integrating over \(\pi\times L\) picks out precisely the coefficient \(a_i\); hence \(\delta_i=a_i\) for every allowed \(i\). Integer polynomial division gives the equivalent recurrence
\[
a_0=1,\qquad a_j=\binom{n+1}{j}-2a_{j-1}\quad(1\le j\le n-1).
\]
In particular \(a_1=n-1\), \(a_2=(n^2-3n+4)/2\). For odd \(n\), the next formal coefficient \(a_n\) vanishes because the degree-\(n\) coefficient of \((1+t)^{n+1}/(1+2t)\) is zero, and the recurrence yields \(a_{n-1}=(n+1)/2\). These recover the degrees of the map and the Pfaffian image. The further intermediate coefficients are not fixed by those two degrees.

**3. Canonical class.** Since \(\det(\Omega^1_{\mathbb P(V)}(2)|_\pi)=\mathcal O_\pi(n-1)\), we have \(\det E=\mathcal O_{\pi\times L}(n-1,n)\). Adjunction for a smooth regular zero scheme yields
\[
K_\Gamma=\bigl(K_{\pi\times L}\otimes\det E\bigr)|_\Gamma
=\mathcal O_\Gamma(-n,-n-1)\otimes\mathcal O_\Gamma(n-1,n)
=\mathcal O_\Gamma(-1,-1).
\]
The restriction of \(\mathcal O(1,1)\) from a product of projective spaces is ample. Therefore \(-K_\Gamma\) is ample and \(\Gamma\) is Fano. This completes the proof.

## Verification

The standalone script `verification/check_multidegrees.py` recomputes each coefficient two ways: recursive exact division and the independent binomial-sum formula from the twisted Euler sequence. It checks the birationality, map-degree, base-degree, and Pfaffian-degree endpoints for every odd \(n\) from 5 through 101, and compares the first four sequences with explicit integer certificates. The accompanying `verification/check_output.txt` records its actual deterministic execution. These are finite arithmetic corroborations only; the universal smoothness, graph identification, Chow-class calculation, and Fano assertion follow from the geometric proof above. The anticanonical volume is additionally computable as \(\sum_{j=0}^{n-1}\binom{n-1}{j}a_j\); it equals 86 at \(n=5\).

## Relationship to prior work

Bolognesi–Ciliberto–Verra, *On Calabi–Yau varieties that are linear sections of Grassmannians of lines*, arXiv:2610.11925v1 (October 8, 2026), especially Sections 2.1 and 3.3, constructs the Pfaffian birational parametrization, identifies the focal base locus, and states the degrees of the map, image, and base locus. Its arguments are used as the geometric motivation and independent comparison. The additional result here is the **smooth Fano geometry of the closed graph** together with its **complete, uniformly indexed Chow/multidegree class**, beyond those endpoint degree statements. The second projective degree is also recoverable from the source's base-locus degree; the remaining interior sequence and Fano assertion are the distinguishing new claims.

Bolognesi–Ciliberto–Verra, *On Fano varieties of index one that are linear sections of Grassmannians of lines*, arXiv:2609.21503v1, concerns a different Grassmannian linear-section problem and distinct Pfaffian birational correspondence. Han's *Geometry of the genus 9 Fano 4-folds* (2010), Section 4, concerns a different order-one line congruence and its incidence geometry. Neither inspected material states the Fano-graph and full multidegree result above. Conventional Grassmannian and determinantal intersection methods underpin the proof, but are not asserted to be new.

## Limitations

The theorem is for a Zariski-general linear subsystem and general hyperplane over \(\mathbb C\), not arbitrary degenerate alternating matrices or positive characteristic. It computes the bidegree Chow class of this particular parametrization, not a classification of all birational parametrizations of Pfaffian hypersurfaces. Smoothness concerns the incidence **graph**, not the (possibly singular) target hypersurface. Explicit generators of the graph ideal beyond the contraction equations, its derived category, and the singularities of the target are not classified. No assertion of prior-literature uniqueness or independent mathematical verification is made; an unindexed equivalent computation remains a literature risk.

## References

1. M. Bolognesi, C. Ciliberto, A. Verra, *On Calabi–Yau varieties that are linear sections of Grassmannians of lines*, arXiv:2610.11925v1, 8 October 2026, https://arxiv.org/html/2610.11925v1.
2. M. Bolognesi, C. Ciliberto, A. Verra, *On Fano varieties of index one that are linear sections of Grassmannians of lines*, arXiv:2609.21503v1, 18 September 2026, https://arxiv.org/abs/2609.21503.
3. F. Han, *Geometry of the genus 9 Fano 4-folds*, Annales de l'Institut Fourier **60** (2010), 1401–1434, https://doi.org/10.5802/aif.2559.
4. W. Fulton, *Intersection Theory*, 2nd ed., Springer (1998), for regular-section Chern classes and Chow intersections.
