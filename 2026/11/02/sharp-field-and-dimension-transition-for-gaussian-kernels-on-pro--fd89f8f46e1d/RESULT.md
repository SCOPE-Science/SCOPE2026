# Sharp field-and-dimension transition for Gaussian kernels on projective incidence metrics

## Finding
Let \(q\) be a prime power, let \(d\ge2\), and let \(X\) comprise all projective points and all hyperplanes of \(\operatorname{PG}(d,q)\). Give \(X\) the shortest-path metric \(\rho\) in the point–hyperplane incidence graph. Write
\[
 v=\frac{q^{d+1}-1}{q-1},\qquad
 k=\frac{q^d-1}{q-1},\qquad
 s=q^{(d-1)/2}.
\]
There is a unique \(\sigma_{d,q}>0\) satisfying
\[
 s(3^{\sigma_{d,q}}-1)=2^{\sigma_{d,q}}.
\]
The largest exponent \(p\ge0\) for which \(\exp(-t\rho(x,y)^p)\) is positive semidefinite on \(X\), **for every \(t>0\)**, is the following \(p_{d,q}\):

* If \(q\ge3\), or if \(q=2\) and \(2\le d\le4\), then \(p_{d,q}=\sigma_{d,q}\).
* If \(q=2\) and \(d\ge5\), then \(p_{d,2}\) is the unique root in \((0,\sigma_{d,2})\) of
\[
 (2^{d+1}-2)2^p=(2^d-1)+2^d3^p.
\]

Thus the extremizing zero-sum Fourier/singular mode changes **sharply at dimension five over the binary field**, while for every field of order at least three the transversal mode always controls the cutoff. In the binary high-dimensional regime,
\[
 p_{d,2}=\frac{1}{2^d\log(4/3)}+O(2^{-2d}),
 \qquad
 \sigma_{d,2}\sim\frac{2^{-(d-1)/2}}{\log3}.
\]
The two potential obstructions therefore occur at different exponential scales.

For every admissible exponent and every fixed \(t>0\), the Gaussian matrix is in fact **strictly** positive definite. The powered-distance matrix is strictly conditionally negative definite for \(0\le p<p_{d,q}\). At the sharp endpoint, its nullity on the zero-sum space is \(v-1\) in the transversal regime and exactly \(1\) in the binary high-dimensional regime. Hence the minimum Euclidean dimensions realizing \(\rho^p\) as squared distances at the respective endpoints are \(v\) and \(2v-2\).

## Assumptions and scope
The statement is for every existing prime-power field order \(q\) and every integer \(d\ge2\). A point is a one-dimensional subspace of \(\mathbb F_q^{d+1}\), and a hyperplane is a codimension-one subspace. Distinct points are at distance two, as are distinct hyperplanes; a point and a hyperplane are at distance one when incident and three otherwise. For \(p=0\), use \(\rho(x,x)^0=0\) and \(\rho(x,y)^0=1\) when \(x\ne y\). A zero-sum nullity is the dimension of the kernel of the quadratic form restricted to vectors whose coordinates sum to zero; it is **not** the nullity of the uncentered matrix.

## Proof
Let \(N\) be the \(v\times v\) point–hyperplane incidence matrix. Projective incidence counting yields
\[
 N\mathbf1=k\mathbf1,\quad N^T\mathbf1=k\mathbf1,\quad
 NN^T=(k-\lambda)I+\lambda J,\quad
 \lambda=\frac{q^{d-1}-1}{q-1},\quad k-\lambda=q^{d-1}=s^2.
\]
For \(a=2^p\) and \(b=3^p\), the powered-distance matrix is exactly
\[
 D_p=\begin{pmatrix}
 a(J-I)&bJ+(1-b)N\\
 bJ+(1-b)N^T&a(J-I)
 \end{pmatrix}.
\]
The orthogonal complement of the global constant decomposes as the point-versus-hyperplane contrast \((\mathbf1,-\mathbf1)\) and the space of two zero-sum half-vectors. The former has scalar quadratic eigenvalue
\[
 \gamma_{d,q}(p)=(v-1)2^p-k-(v-k)3^p.
\]
On the latter, the singular values of \(N\) are all \(s\), giving eigenvalues
\[
 -2^p+s(3^p-1),\qquad -2^p-s(3^p-1)
\]
with multiplicity \(v-1\) each. The second is strictly negative for all \(p\ge0\). The first vanishes only at \(\sigma_{d,q}\) because \((3^p-1)/2^p=(3/2)^p-(1/2)^p\) is strictly increasing from zero to infinity. Schoenberg's negative-type criterion equates \(D_p\) being nonpositive on zero-sum vectors to positive semidefiniteness of every \(\exp(-tD_p)\). The strict-lower-exponent principle of Li–Weston shows that, once an endpoint is of negative type, all smaller exponents are strictly of negative type; conversely any endpoint zero mode rules out every larger exponent by the same principle. Thus it remains to identify which of the two candidate zero modes occurs first.

For projective point–hyperplane incidence, \(v-k=q^d\) and
\[
 \gamma'_{d,q}(p)=(v-1)(\log2)2^p-q^d(\log3)3^p.
\]
When \(q\ge3\), one has
\[
 \frac{v-1}{q^d}=\frac{q}{q-1}(1-q^{-d})<\frac32<\frac{\log3}{\log2}.
\]
Therefore \(\gamma'_{d,q}(p)<0\) for all \(p\ge0\); since \(\gamma_{d,q}(0)=-1\), the contrast cannot obstruct, and the first eigenvalue reaches zero at \(\sigma_{d,q}\).

For \(q=2,d=2\), \(\gamma'_{2,2}(0)=6\log2-4\log3<0\), and the same monotonicity argument applies. For \(d=3,4\), exact rational root brackets give respectively
\[
 0.482<\sigma_{3,2}<0.483,\quad \gamma_{3,2}(\sigma_{3,2})<-1.018,
\]
\[
 0.335<\sigma_{4,2}<0.336,\quad \gamma_{4,2}(\sigma_{4,2})<-0.250.
\]
These are strict interval enclosures verified by raising rational bounds for \(2^p\), \(3^p\), and \(\sqrt{2^{d-1}}\) to integer powers; see `check.py`. Negative type at \(\sigma\), followed by the strict-lower-exponent principle, gives the small-dimensional claim without assuming monotonicity of \(\gamma\).

For binary \(d\ge5\), first exhibit a point \(p<\sigma_{d,2}\) where \(\gamma_{d,2}(p)>0\). Exact rational-power enclosures verify this with \(p=1/5\) for \(d=5\), \(p=1/16\) for \(d=6\), and \(p=1/32\) for \(d=7\); the corresponding certified lower bounds for \(\gamma\) are \(0.3559\), \(0.02966\), and \(0.09111\), and the transversal eigenvalue is strictly negative at each witness.

For all \(d\ge8\), set \(p=4/2^d\le1/64\) and \(f(x)=2^{x+1}-1-3^x\). Elementary inequalities \(\log2>0.69\), \(\log3<1.10\), \(2^{1/64}<1.011\), and \(3^{1/64}<1.02\) yield
\[
 f(0)=0,\qquad f'(0)>0.28,\qquad f''(x)>-1\quad(0\le x\le1/64).
\]
Since \(\gamma_{d,2}(p)=2^d f(p)-(2^{p+1}-1)\), Taylor's inequality gives
\[
 \gamma_{d,2}(p)>1.12-8/2^d-1.022>0.
\]
Meanwhile
\[
 2^{(d-1)/2}(3^p-1)
 <\frac{4(1.10)(1.02)}{2^{(d+1)/2}}<1<2^p,
\]
so this witness is strictly below \(\sigma_{d,2}\). Finally \(\gamma_{d,2}(0)=-1\), and \(\gamma\) is strictly increasing throughout \([0,\sigma_{d,2}]\). Indeed, \(\sigma_{d,2}\le\sigma_{5,2}<1/4\), as the left side of its defining equation divided by \(2^p\) increases in \(p\) and in \(d\). For \(0\le p\le1/4\), one has \((3/2)^p<1.11\), whereas \(\frac{2^{d+1}-2}{2^d}\frac{\log2}{\log3}\ge(31/16)(0.63)>1.22\); comparison with the displayed derivative shows \(\gamma'_{d,2}(p)>0\). Consequently its zero lies uniquely in \((0,\sigma_{d,2})\) and is the sharp cutoff. The endpoint multiplicities follow from the displayed spectral decomposition. Centering a squared-distance matrix identifies Euclidean embedding dimension with zero-sum rank, giving the stated dimensions.

To obtain the binary asymptotic, expand \(\gamma_{d,2}\) at zero: its initial value is \(-1\), derivative is \(2^d\log(4/3)-2\log2\), and its second derivative is \(O(2^d)\) uniformly for \(p=O(2^{-d})\). Thus its first root has the stated expansion. Similarly, expanding \(s(3^p-1)=2^p\) gives the stated \(\sigma\) asymptotic. Strict Gaussian positive definiteness at any fixed \(t>0\) follows because the zero-diagonal negative-type matrix represents squared distances between distinct Euclidean points, and the ordinary Gaussian is strictly positive definite on any finite set of distinct Euclidean points.

## Verification
Run `python check.py` with Python 3 and NumPy. The script certifies the decisive small-dimensional interval inequalities using **exact integers and rational brackets**; independently reconstructs the projective incidence matrices for prime fields of orders two and three; computes shortest paths; and checks the full centered spectrum against the formulas at seven exponents. Tested geometries are \(\operatorname{PG}(d,2)\) for \(2\le d\le5\) and \(\operatorname{PG}(d,3)\) for \(2\le d\le3\). The analytic argument, not these finite tests, proves the universal prime-power statement and the all-dimensional binary cutoff.

## Relationship to prior work
Schoenberg's Gaussian/negative-type equivalence and Li–Weston's strict-lower-exponent principle are used as known theorems. The projective-incidence parameter identities and their distance-regular interpretation are standard; Bailey's projective-incidence treatment supplies structural context but analyzes resolving sets, not kernel thresholds. Aalipour et al. determine ordinary distance spectra of several other distance-regular graph families rather than the powered-distance cutoff here. The new classification is the **field-versus-dimension switch at \(q=2,d=5\)**, including the competing endpoint nullities and two different binary asymptotic scales. The projective-plane special case \(d=2\) follows from earlier negative-type calculations; this is not claimed as new.

## Limitations
The theorem concerns all-bandwidth positivity of Gaussian distance-power kernels; it does not give a sharp cutoff at any prescribed single bandwidth. Numerical checks cover only specified small prime-field cases and do not verify arbitrary extension fields. The historical comparison is bounded: an older equivalent result stated using distance-regular association schemes or generalized roundness may exist. No independent mathematical audit has been performed.

## References
- H. Li and A. Weston, *Strict p-negative type of a metric space*, arXiv:0901.0695, first submitted 2009-01-06, especially Theorems 5.2 and 5.4. https://arxiv.org/html/0901.0695v3
- R. F. Bailey, *On the metric dimension of incidence graphs*, arXiv:1707.02899, first submitted 2017-07-10, Section 2 (incidence parameter and distance-regular framework). https://arxiv.org/html/1707.02899v2
- G. Aalipour et al., *On the distance spectra of graphs*, arXiv:1509.01196, first submitted 2015-09-03 (distance-spectral literature comparison). https://arxiv.org/html/1509.01196v2
- The standard symmetric-design identities are also described in *Combinatorics of Symmetric Designs* by Ionin and Shrikhande (2006); this is background rather than a source of the threshold claim.
