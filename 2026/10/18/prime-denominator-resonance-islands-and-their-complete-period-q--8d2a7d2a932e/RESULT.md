# Prime-denominator resonance islands and their complete period-\(q\) area law

## Finding
Consider the bijective planar piecewise rotation
\[
F_\lambda(z)=\lambda\bigl(z-H(z)\bigr),\qquad
H(z)=\begin{cases}1,&\operatorname{Im}z\ge0,\\-1,&\operatorname{Im}z<0,\end{cases}
\quad\lambda=e^{2\pi i p/q}.
\]
For **every odd prime** \(q\ge5\) and every integer \(1\le p<q\), put
\[
c_+=\frac{\lambda}{\lambda-1}=\frac12-\frac{i}{2}\cot\!\left(\frac{\pi p}{q}\right),
\qquad c_-=-c_+.
\]
Then all points whose period divides \(q\) admit a complete, exact classification:

* If \(1\le p<q/2\), there are **no** such points: \(\operatorname{Fix}(F_\lambda^q)=\varnothing\).
* If \(q/2<p<q\), define \(h=-\tfrac12\cot(\pi p/q)>0\). Let
\[
P_+=\left\{z:\operatorname{Im}\bigl(c_++\lambda^j(z-c_+)\bigr)\ge0\text{ for }0\le j<q\right\},
\]
\[
P_-=\left\{z:\operatorname{Im}\bigl(c_-+\lambda^j(z-c_-)\bigr)<0\text{ for }0\le j<q\right\}.
\]
These are respectively a **closed regular \(q\)-gon** centered at \(c_+\) and an **open regular \(q\)-gon** centered at \(c_-\), each with inradius \(h\). They are disjoint and exhaust the return-fixed set:
\[
\boxed{\operatorname{Fix}(F_\lambda^q)=P_+\sqcup P_-.}
\]
Precisely two points, the centers \(c_+\) and \(c_-\), are fixed by \(F_\lambda\); all other points in these polygons have **least period exactly \(q\)**. In particular, even points on the boundary of \(P_+\) have period \(q\), apart from the center; the switching convention at height zero matters here.

The total planar Lebesgue measure of this return-fixed set is exactly
\[
\boxed{\operatorname{Leb}_2\bigl(\operatorname{Fix}(F_\lambda^q)\bigr)
=\frac q2\cot^2\!\left(\frac{\pi p}{q}\right)\tan\!\left(\frac\pi q\right)}
\qquad(q/2<p<q),
\]
and is zero otherwise. Among the admissible \(p\) for each fixed prime \(q\), this area has a unique maximum at \(p=q-1\), with value
\[
\boxed{\frac q2\cot\!\left(\frac\pi q\right)};
\]
it grows as \(q^2/(2\pi)\) along odd primes. Thus reversing the rotational orientation creates a positive-area first-resonance region, and the choice of rotation numerator quantitatively controls that area.

## Assumptions and scope
The phase space is all \(\mathbb C\simeq\mathbb R^2\). The integer \(q\) is an odd prime at least five; \(p\) is an integer in \(\{1,\ldots,q-1\}\), hence coprime to \(q\). The branch convention is **inclusive at the real axis for the upper branch**. We study \(\operatorname{Fix}(F^q)\), meaning periods *dividing* \(q\), and distinguish fixed points from points of least period \(q\). The result does not classify any other period or the full critical/fractal set.

## Proof
**1. The cyclotomic elimination of mixed itineraries.** Suppose \(F_\lambda^q(z)=z\). For \(0\le j<q\), set \(s_j=H(F_\lambda^j(z))\in\{-1,1\}\). Direct iteration gives the exact identity
\[
F_\lambda^q(z)=\lambda^q z-\sum_{j=0}^{q-1}\lambda^{q-j}s_j
=z-\sum_{j=0}^{q-1}\lambda^{-j}s_j.
\]
Therefore the integer polynomial \(S(X)=\sum_{j=0}^{q-1}s_jX^j\) vanishes at the primitive \(q\)-th root \(\lambda^{-1}\). Because \(q\) is prime, its minimal polynomial over \(\mathbb Q\) is
\(\Phi_q(X)=1+X+\cdots+X^{q-1}\). Both polynomials have degree at most \(q-1\), so \(S(X)=c\Phi_q(X)\). Comparing coefficients yields \(s_0=\cdots=s_{q-1}=c\in\{-1,1\}\). **Every \(q\)-return-fixed point must use exactly one branch throughout its first \(q\) iterates**. This conclusion applies to all points, including discontinuity preimages, and does not presuppose a partition of the phase space into regular tiles.

**2. Branch centers and a sharp orientation obstruction.** For a constant branch sign \(s\), the affine map \(z\mapsto\lambda(z-s)\) is rotation by \(\lambda\) around \(c_s=s\lambda/(\lambda-1)\), and its \(j\)-th iterate is \(c_s+\lambda^j(z-c_s)\). Since \(\sum_{j=0}^{q-1}\lambda^j=0\), the arithmetic mean of those \(q\) imaginary coordinates is \(\operatorname{Im}c_s\). An all-upper itinerary requires this mean to be nonnegative; an all-lower itinerary requires it to be strictly negative. From
\[
\frac{\lambda}{\lambda-1}=\frac12-\frac i2\cot(\pi p/q),
\]
when \(p<q/2\) the upper center is strictly below the real axis and the lower center is strictly above it. Neither constant itinerary is possible. Conversely when \(p>q/2\), the upper and lower centers lie in their respective open half-planes at signed distances \(h\) from the real axis.

**3. Exact regions, boundary, and least periods.** For \(p>q/2\), the constant-upper itinerary condition for all \(q\) steps is exactly the defining inequality for \(P_+\); likewise for \(P_-\), with strict inequalities because \(H=1\) when the height is zero. The \(q\) linear functionals \(u\mapsto\operatorname{Im}(\lambda^j u)\) have evenly spaced normal directions because multiplication by \(p\) permutes residues modulo \(q\). Hence the inequalities intersect to give a regular \(q\)-gon of inradius \(h\) about each center, closed in the upper case and open in the lower. Every point in either region follows its corresponding affine rotation for \(q\) steps, and therefore returns to itself. Step 1 shows there are no further points. The rotation has prime order \(q\), so the only point of lesser period within each polygon is its center. The two regions are disjoint because their initial imaginary coordinates have opposite sign.

**4. Area and optimal orientation.** A regular \(q\)-gon with inradius \(h\) has perimeter \(2qh\tan(\pi/q)\) and area \(qh^2\tan(\pi/q)\). The open/closed distinction affects no planar area. Doubling and substituting \(h\) yields the claimed formula. Since \(\cot(\pi p/q)\) is strictly decreasing and negative for \(q/2<p<q\), its square strictly increases with \(p\). Therefore the maximum is uniquely at \(p=q-1\). The identity \(\cot(\pi-\pi/q)=-\cot(\pi/q)\) gives its closed value, and \(\cot t\sim t^{-1}\) proves the prime-sequence asymptotic.

## Verification
The companion `CHECK.py` runs with Python's standard library. It enumerates all \(2^q\) sign words for \(q\in\{5,7,11\}\), checking the coefficient rigidity modulo \(\Phi_q\) with integer arithmetic. For every numerator \(p\) it independently constructs both candidate polygons from supporting half-planes, checks vertex inequalities and shoelace area, and tests interior orbit returns. The program passed **4236 checks**, of which the finite cyclotomic coefficient tests use exact integers and the geometry/iteration tests are floating point with explicit tolerances. These tests are not substitutes for the universal algebraic and geometric proof.

## Relationship to prior work
Cima, Gasull, Mañosa and Mañosas [1] introduced and investigated exactly this rational piecewise-rotation family, proving periodicity on regular components (Theorem A) and bounds on the number of polygon sides (Theorem B). They also explicitly exhibit a fixed pentagon for the particular angle \(8\pi/5\), which is therefore **not** newly claimed here. The new statement gives an *exhaustive* prime-denominator period-\(q\) locus (including its absence in the opposite orientation), exact global area, and numerator optimization; those implications do not follow merely from the existence of regular periodic tiles or a bound on their sides.

Goetz and Quas [2] established important global boundedness and periodic-island constructions for the more general two-half-plane family. Their Lemma 11 describes islands associated with periodic center orbits **visiting both half-planes**; its height parameters require visits to both sides, whereas the resonance islands here are precisely constant-sign orbits. Their results thus provide the natural geometry comparison but do not themselves state the mixed-word exclusion or the complete \(q\)-fixed area. Cima and collaborators [3] obtained much stronger global classifications for specific low-denominator angles (notably denominator three); those special-case results are acknowledged, and the present theorem is restricted to odd prime denominators at least five. This is a best-knowledge comparison, not a proof of absolute historical priority.

## Limitations
For composite \(q\), the minimal cyclotomic polynomial generally has lower degree, and a root-of-unity cancellation need not force constant signs; no composite-denominator claim is made. The planar area counts only points with period dividing \(q\), not every periodic orbit. Boundary membership uses the exact sign convention and could change with a different convention, although the area is unaffected. Other published or unindexed proofs may contain equivalent special cases; historical priority remains subject to independent review.

## References
[1] A. Cima, A. Gasull, V. Mañosa, F. Mañosas, *On some rational piecewise linear rotations* (first online preprint 30 June 2023), arXiv:2306.17543; *Journal of Difference Equations and Applications* **30** (2024), 1577–1589, doi:10.1080/10236198.2023.2260898. Author postprint: https://ddd.uab.cat/pub/artpub/2024/307719/CimGasManMan2023a-Postprint.pdf.

[2] A. Goetz and A. Quas, *Global properties of a family of piecewise isometries*, *Ergodic Theory and Dynamical Systems* **29** (2009), 545–568, doi:10.1017/S0143385708080280. Author full text: https://web.uvic.ca/~aquas/papers/paper28.pdf.

[3] A. Cima, A. Gasull, V. Mañosa, F. Mañosas, *Pointwise periodic maps with quantized first integrals*, arXiv:2010.12901 (2020), *Communications in Nonlinear Science and Numerical Simulation* **108** (2022), 106150.
