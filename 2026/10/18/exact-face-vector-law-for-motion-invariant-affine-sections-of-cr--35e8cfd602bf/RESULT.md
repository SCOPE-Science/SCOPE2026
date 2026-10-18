# Exact face-vector law for motion-invariant affine sections of cross-polytopes

## Finding
Fix an integer \(d\ge3\) and let \(C_d=\{x\in\mathbb R^d:\sum_{i=1}^d|x_i|\le1\}\). Sample an unoriented affine hyperplane with Euclidean-motion-invariant measure, conditional on meeting the interior of \(C_d\). Let \(f_j\) denote the number of \(j\)-faces of its \((d-1)\)-dimensional section, for \(0\le j\le d-2\). Define, for \(0\le k\le d-1\),
\[
F_{d,j}(k)=2^{j+2}\binom d{j+2}-\sum_{q=0}^{j+2}2^q\binom kq\binom{d-k}{j+2-q}-\binom{d-k}{j+2},
\]
with out-of-range binomial coefficients zero. The possible **face vectors** are exactly the \(d-1\) distinct vectors \(\mathbf F_d(k)=(F_{d,0}(k),\ldots,F_{d,d-2}(k))\), for \(1\le k\le d-1\). (The cases \(k=0\) and \(k=1\) have the same face vector, though not necessarily the same face lattice.)

For independent standard Gaussian variables \(G_1,\ldots,G_d\), set \(H_i=|G_i|\), let \(H_{(1)}<\cdots<H_{(d)}\) be their ascending order statistics and put \(H_{(0)}=0\). Then
\[
\Pr\{(f_0,\ldots,f_{d-2})=\mathbf F_d(1)\}=\frac{\mathbb EH_{(2)}}{\mathbb EH_{(d)}},
\]
\[
\Pr\{(f_0,\ldots,f_{d-2})=\mathbf F_d(k)\}=\frac{\mathbb E(H_{(k+1)}-H_{(k)})}{\mathbb EH_{(d)}},\quad 2\le k\le d-1.
\]
Each probability is strictly positive. Equivalently, with \(Q(t)=\operatorname{erf}(t/\sqrt2)\) and \(Z_d=\int_0^\infty(1-Q(t)^d)\,dt\), the numerator for \(k=1\) is \(\int_0^\infty((1-Q)^d+dQ(1-Q)^{d-1})\,dt\), and for \(2\le k\le d-1\) it is \(\binom dk\int_0^\infty Q^k(1-Q)^{d-k}\,dt\).

There is also an exact **joint high-dimensional law**. If \(j_1,\ldots,j_r\ge0\) are fixed and \(d\to\infty\), then
\[
\left(\frac{\log f_{j_1}}{\log d},\ldots,\frac{\log f_{j_r}}{\log d}\right)\ \Longrightarrow\ (j_1+2-U^2,\ldots,j_r+2-U^2),\qquad U\sim\operatorname{Uniform}[0,1].
\]
Thus the whole fixed-rank face-vector spectrum has one shared, nondegenerate random exponent. In particular, the vertex exponent lies in \([1,2]\) with distribution function \(1-\sqrt{2-x}\) for \(1\le x\le2\).

## Assumptions and scope
Use the invariant hyperplane measure \(d\sigma(u)\,ds\), with \(u\) uniform on the unit sphere and \(s\in\mathbb R\); normal sign reversal identifies \((u,s)\) and \((-u,-s)\). Conditioning on hitting \(C_d\) makes this a probability law. Almost every sampled section meets no vertex, its normal has nonzero coordinates with pairwise distinct absolute values, and its offset is not one of their absolute values. All face numbers and limiting statements concern such generic sections. The full law is for *face vectors*, not a claim that equal face vectors determine a unique face lattice.

## Proof
**Step 1: combinatorial enumeration.** Write the hyperplane as \(\langle u,x\rangle=s\). Central symmetry permits \(s>0\) and independent sign flips permit replacing the normal components by their magnitudes \(a_i=|u_i|>0\). Let \(k=\#\{i:a_i<s\}\). Every proper \((j+1)\)-face of \(C_d\) is a simplex whose \(m=j+2\) vertices choose \(m\) distinct coordinate axes and one sign on each. Generically its intersection with the hyperplane is a \(j\)-face of the section precisely if its vertex heights straddle \(s\); each section \(j\)-face arises uniquely in this way.

Fix a set \(S\) of \(m\) axes containing \(q\) axes with \(a_i<s\). Among its \(2^m\) sign patterns, exactly \(2^q\) fail to have any vertex above \(s\): every axis whose magnitude exceeds \(s\) must take the negative sign. If \(q>0\), at least one selected vertex lies below \(s\) automatically. If \(q=0\), the all-positive choice has no vertex below \(s\) and must additionally be removed. The number of straddling simplex faces is therefore \(2^m-2^q-\mathbf1_{\{q=0\}}\). Summing over choices of \(S\) with \(q\) small axes yields the stated \(F_{d,j}(k)\). In particular,
\[
F_{d,0}(k)=2\left(\binom d2-\binom k2\right).
\]
The identity \(F_{d,j}(0)=F_{d,j}(1)=(2^{j+2}-2)\binom d{j+2}\) follows by Pascal's identity. For \(k=1,\ldots,d-1\), the vertex counts are strictly decreasing from \(k=1\) onwards, proving exactly \(d-1\) distinct face-vector values.

**Step 2: invariant-plane probabilities.** Given a unit normal, its allowed offsets are \(-a_{(d)}<s<a_{(d)}\). For positive offsets, the event \(k=\#\{a_i<s\}\) occupies precisely the interval \((a_{(k)},a_{(k+1)})\), with \(a_{(0)}=0\). Integrating offsets before directions therefore gives probability \(\mathbb E_\sigma(a_{(k+1)}-a_{(k)})/\mathbb E_\sigma a_{(d)}\); combine \(k=0,1\). Represent the uniform spherical direction as \(G/\|G\|_2\), where \(G\) has independent standard normal coordinates. The common radial factor is independent of the direction and cancels in the ratio of expectations. This proves the half-normal order-statistic law. Using \(\mathbb EX=\int_0^\infty\Pr(X>t)\,dt\), the difference of consecutive order-statistic survival functions is \(\binom dk Q(t)^k(1-Q(t))^{d-k}\), proving the one-dimensional integral expressions and positivity.

**Step 3: joint logarithmic asymptotics.** Under the hitting-plane measure, a convenient equivalent sampling is: draw independent half-normal \(H_i\), tilt the joint density proportionally to \(M_d=\max_iH_i\), draw \(U\) independently uniform on \([0,1]\), and set \(k=\#\{i:H_i<UM_d\}\). To see the tilt, first represent a spherical direction by the radial Gaussian representation; since its radial part is independent of direction, weighting directions by their maximal coordinate is equivalent to weighting full Gaussian vectors by \(M_d\). Standard Gaussian tail bounds imply \(M_d/\sqrt{2\log d}\to1\) in probability and in first mean, and the tilted and untilted laws have vanishing total-variation distance because \(M_d/\mathbb EM_d\to1\) in \(L^1\). For fixed \(u\in(0,1)\), compare \(UM_d\) with \((u\pm\eta)\sqrt{2\log d}\). The counts exceeding those deterministic thresholds are binomial with expectations \(d^{1-(u\pm\eta)^2+o(1)}\) and concentrate relative to their means. Letting \(\eta\downarrow0\) gives, with \(\ell=d-k\),
\[
\frac{\log\ell}{\log d}\longrightarrow1-U^2\quad\text{in probability},\qquad \frac{\ell}{d}\longrightarrow0\quad\text{in probability}.
\]
For each fixed \(j\), the enumerated face count is dominated by faces with exactly one axis above threshold: their number is \(2^{j+1}\ell\binom{d-\ell}{j+1}\). Faces with at least two such axes contribute \(O_j(\ell^2d^j)\), uniformly whenever \(\ell=o(d)\). Hence
\[
f_j\sim \frac{2^{j+1}}{(j+1)!}\ell d^{j+1}
\]
in probability, simultaneously for any fixed finite collection of ranks. Taking logarithms proves the asserted joint weak convergence.

## Verification
A standalone Python checker, `verify_section_faces.py`, compares \(F_{d,j}(k)\) against direct enumeration of signed original faces for \(3\le d\le8\), with 945 exact integer comparisons. It separately computes the half-normal order-statistic integrals and performs 400,000 Gaussian importance-sampling trials for each of \(d=3,4,6\); the maximum probability discrepancy in those tests was below 0.0021. It outputs `CROSSPOLY_FACE_LAW_OK` when all assertions pass. Numerical experiments test finite cases but are not an infinite-dimensional proof.

For \(d=3\), the probabilities of a 6-vertex and a 4-vertex section are approximately \(0.5521496561\) and \(0.4478503439\). For \(d=4\), the possible vertex counts \(12,10,6\) have probabilities approximately \(0.3777936325,0.2444127350,0.3777936325\), respectively. The full face vector is given by the same formula at each rank.

## Relationship to prior work
Ambrus (arXiv:1208.5923, initially public 29 August 2012) develops Gaussian formulas for mean widths and extremal cross-polytope dimensions, but does not determine random affine-section face-vector laws. Liu and Tkocz (arXiv:1910.06993) study extrema of noncentral cross-polytope section volumes and line lengths; those extrema do not yield the invariant-plane face-vector distribution. Earlier face-enumeration theory supplies the ordinary cross-polytope face count \(2^{j+1}\binom d{j+1}\); conditioning those faces to straddle a *random offset* and integrating produces a different probability law. Some prior geometric-probability results for central cube and simplex sections are related in technique, but not equivalent: their sectioning models and face-incidence patterns differ. The vertex-exponent limit resembles a previously obtained affine-simplex limit, whereas the joint all-face-vector law and cross-polytope classification are the assessed content.

## Limitations
The result concerns regular coordinate cross-polytopes under invariant *affine* hyperplane sampling, not arbitrary cross-polytopes, hyperplanes forced through the center, or distributions weighted by section volume. The result classifies face vectors rather than all section face lattices. Historical priority is assessed against accessible literature and records, not independently certified. The proof's asymptotic convergence has no finite-dimensional rate, and no external independent audit has been performed.

## References
1. G. Ambrus, *Extremal cross-polytopes and Gaussian vectors*, arXiv:1208.5923 (first public 2012-08-29), https://arxiv.org/abs/1208.5923.
2. R. Liu and T. Tkocz, *A note on the extremal noncentral sections of the cross-polytope*, arXiv:1910.06993 (2019), https://arxiv.org/abs/1910.06993.
3. H. König, *Non-central sections of the simplex, the cross-polytope and the cube*, arXiv:2002.10743 (2020), https://arxiv.org/abs/2002.10743.
4. A. Padrol and J. Pfeifle, *Polygons as sections of higher-dimensional polytopes*, arXiv:1404.2443 (first public 2014-04-09), https://arxiv.org/abs/1404.2443 (different section-realization problem).
