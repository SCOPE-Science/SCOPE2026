# Exact halfspace-depth law for three symmetric convex slices and a sharp one-third bound

## Finding
Let \(d\ge2\), and let \(K_0,K_1,K_2\subset\mathbb R^d\) be full-dimensional compact convex bodies that are centrally symmetric about the origin. Write \(a_i=|K_i|>0\), and form the mixed-dimensional measure
\[
\mu(E)=\sum_{i=0}^{2}\bigl|\{x\in K_i:(i,x)\in E\}\bigr|,
\qquad S=\bigcup_{i=0}^{2}(\{i\}\times K_i).
\]
Define unnormalized halfspace depth \(h_S(q)=\inf_{H\ni q}\mu(H)\), with the infimum over closed halfspaces of \(\mathbb R^{d+1}\). For \(u\in\mathbb S^{d-1}\) and \(t\in\mathbb R\) set
\[
F_i(u,t)=\bigl|\{x\in K_i:\langle u,x\rangle\ge t\}\bigr|,
\qquad
D=\sup_{u,t}\bigl(F_0(u,t)-F_2(u,t)\bigr).
\]
Then **a center of one of the three slices is always globally depth-optimal**, and the exact depth is
\[
\boxed{\max_{q\in S}h_S(q)=
\max\left\{\frac{a_0}{2},\frac{a_2}{2},\frac{a_1}{2}+a_0-D\right\}.}
\]
The individual center depths are exactly \(h_S(0,0)=a_0/2\), \(h_S(2,0)=a_2/2\), and \(h_S(1,0)=a_1/2+a_0-D\). In particular, the center chosen by the maximum is an optimizer; uniqueness is not asserted.

Put \(m=\min(a_0,a_2)\), \(M=\max(a_0,a_2)\), and \(\eta=D-(a_0-a_2)_+\). Then \(\eta\ge0\), and
\[
\boxed{\eta=0\ \Longleftrightarrow\ K_0\subseteq K_2\ \text{or}\ K_2\subseteq K_0.}
\]
The equivalent depth formula is
\[
\max_{q\in S}h_S(q)=\max\left\{\frac M2,\frac{a_1}{2}+m-\eta\right\}.
\]
Thus \(\eta\) is the **exact depth penalty at the middle center** caused by outer-slice nonnesting. When the two outer bodies are nested, the depth depends only on the three volumes and exceeds strictly one quarter of their sum. The sharp infimum of normalized depth over this nested class is \(1/4\), unattained by positive-volume slices.

If all three slice volumes are equal, the exact law yields the **sharp all-dimensional bound**
\[
\boxed{\frac{\max_{q\in S}h_S(q)}{\mu(S)}>\frac13,\qquad d\ge2,}
\]
and \(1/3\) is the infimum over full-dimensional centrally symmetric triples. It is approached by mutually transverse thin rectangular outer slices. In dimension \(1\), equal-length centrally symmetric intervals centered together coincide, and the corresponding normalized maximum is instead exactly \(1/2\).

The result remains valid for bodies with centers \(c_i=c_0+i v\) in arithmetic progression, after the affine shear \((i,x)\mapsto(i,x-c_0-iv)\); in this formulation the cap discrepancy is computed from the recentered bodies.

## Assumptions and scope
All volumes and section cuts are taken with respect to \(d\)-dimensional Lebesgue measure on each slice. The ambient measure is supported only on the three slices, and depth is maximized over \(S\), not over all of \(\mathbb R^{d+1}\). All halfspaces are closed; this does not affect positive-dimensional section volumes when their transverse normal is nonzero. The sets \(K_i\) need not be homothetic, need not satisfy any midpoint inclusion, and need not be mutually nested. Their common symmetry center is essential for the reduction. The quantity \(D\) is a nonnegative one-sided difference between ordinary halfspace-cap volumes, not a symmetric-difference volume or a Hausdorff distance.

The sharp \(1/3\) bound concerns triples of **equal volumes**, without the midpoint-inclusion condition that arises when the three slices of a single convex body are sampled at consecutive integer heights. No inference about the unrestricted convex-body mixed-integer centerpoint conjecture is made.

## Proof
**1. A depth center exists on each slice.** Given a halfspace containing a point, translate its boundary parallel inward until it passes through that point; the smaller halfspace cannot carry more mass. It therefore suffices throughout to consider halfspaces with boundary through the tested point. Reflection \((z,x)\mapsto(z,-x)\) preserves \(\mu\); hence \(h_S(i,x)=h_S(i,-x)\). For any measure and any two points \(p,q\), its Tukey depth is quasiconcave. Indeed, for any halfspace through \((p+q)/2\), at least one of \(p,q\) lies in that halfspace, and the parallel boundary halfspace through that point is contained in the original one. Thus
\[
h_S((p+q)/2)\ge\min(h_S(p),h_S(q)).
\]
Applying this to \((i,x)\) and \((i,-x)\) shows \(h_S(i,0)\ge h_S(i,x)\) for every \(x\in K_i\). The global maximum therefore equals the maximum of three center depths.

**2. The two outer depths.** A halfspace containing \((0,0)\) whose normal has a nonzero spatial component contains at least half the centrally symmetric bottom slice, of volume \(a_0/2\). A purely horizontal halfspace through that point contains the entire bottom slice. Hence \(h_S(0,0)\ge a_0/2\). For any fixed nonzero \(u\), the ambient halfspaces \(\{(z,x):\langle u,x\rangle-Tz\ge0\}\), with \(T\) larger than the finite widths of the other slices, retain exactly one half of \(K_0\) and none of the upper slices. Thus \(h_S(0,0)=a_0/2\). Reversing the slice coordinate gives \(h_S(2,0)=a_2/2\).

**3. The middle depth and the cap discrepancy.** Every nonhorizontal halfspace with boundary through \((1,0)\) can, after positive rescaling, be written
\[
H_{u,t}=\{(z,x):\langle u,x\rangle+t(z-1)\ge0\}.
\]
Its cut on slice zero is \(F_0(u,t)\); on slice one it is \(a_1/2\); on slice two it is \(F_2(u,-t)\). By central symmetry and the zero volume of a hyperplane section,
\[
F_2(u,-t)=a_2-F_2(u,t).
\]
Consequently
\[
\mu(H_{u,t})=\frac{a_1}{2}+a_2+F_0(u,t)-F_2(u,t).
\]
Similarly the difference \(f(u,t)=F_0(u,t)-F_2(u,t)\) satisfies
\[
f(u,-t)=(a_0-a_2)-f(u,t).
\]
The collection of values of \(f\) is reflection invariant around \((a_0-a_2)/2\), so its infimum is \((a_0-a_2)-D\). The infimum of the displayed nonhorizontal halfspace masses is therefore \(a_1/2+a_0-D\). A horizontal halfspace through \((1,0)\) contains the full middle slice and at least one outer slice; its mass is \(a_1+a_0\) or \(a_1+a_2\). Both are at least \(a_1/2+a_0-D\), since \(D\ge0\) and \(D\ge a_0-a_2\) (take an empty or a full cap). This proves the claimed middle depth and the exact global formula.

**4. Nonnesting is exactly the discrepancy penalty.** Since the empty and full caps give respective differences \(0\) and \(a_0-a_2\), necessarily \(D\ge(a_0-a_2)_+\). If \(K_0\subseteq K_2\), every halfspace cap of \(K_0\) is included in the corresponding cap of \(K_2\), so \(D=0\). Conversely, if \(D=0\) and a point of \(K_0\) lay outside \(K_2\), a strict supporting separation from compact convex \(K_2\) would produce a halfspace that misses \(K_2\) but intersects \(K_0\) in positive volume, contradicting \(D=0\). Thus \(D=0\) precisely when \(K_0\subseteq K_2\). By complementing the halfspace caps, the identity \(D=a_0-a_2\) is equivalent to \(K_2\subseteq K_0\). It follows that \(\eta=0\) precisely when the outer bodies are nested. The expression \(a_0-D=m-\eta\) then gives the alternate depth formula.

**5. The nested sharp quarter law.** In the nested class the unnormalized optimum is \(\max\{M/2,a_1/2+m\}\). If it were at most \((M+a_1+m)/4\), the two branches would respectively force \(M\le a_1+m\) and \(a_1+3m\le M\), an impossibility since \(m>0\). Thus the normalized depth is strictly above \(1/4\). For \(K_0=\varepsilon K\), \(K_1=K_2=K\), the ratio tends to \(1/4\) as \(\varepsilon\downarrow0\), proving sharpness in every dimension.

**6. Sharp equal-volume one-third law.** Suppose \(a_0=a_1=a_2=v>0\). For \(t\ge0\), symmetry gives \(0\le F_i(u,t)\le v/2\), so \(|F_0(u,t)-F_2(u,t)|\le v/2\). The identity for negative \(t\) gives \(D\le v/2\). In fact \(D<v/2\): the two outer convex bodies each contain a neighborhood of the origin, so for every fixed \((u,t)\) the cap difference is strictly below \(v/2\); continuity in \(u,t\), together with compact support and reduction of large thresholds to full or empty caps, makes the inequality uniform. Therefore
\[
\max_{q\in S}h_S(q)=\frac{3v}{2}-D>v,
\]
and division by \(3v\) proves the strict bound.

For sharpness in dimension two, let \(L>1\) and set
\[
K_0=[-L,L]\times[-L^{-1},L^{-1}],\quad
K_2=[-L^{-1},L^{-1}]\times[-L,L],\quad
K_1=[-1,1]^2.
\]
Each area is \(4\). At direction \(u=(1,0)\) and threshold \(t=L^{-1/2}\), the first cap has area \(2-2L^{-3/2}\), while the second cap is empty. Hence \(D\ge 2-2L^{-3/2}\), and the exact global formula gives
\[
\frac13<\frac{\max_{q\in S}h_S(q)}{12}
\le\frac13+\frac{L^{-3/2}}6.
\]
The limit is \(1/3\). Taking products of all three bodies with the same full-dimensional centered cube gives the same normalized law in every \(d>2\), since the exhibited cap proportions are unchanged. In \(d=1\), equal-length symmetric intervals have identical endpoints and hence identical supports, so their three-slice measure is centrally symmetric about \((1,0)\), attaining normalized depth \(1/2\). This completes the proof.

## Verification
The independent finite checker `verify.py` uses exact rational polygon clipping to verify the central halfspace-cap identities for three families of centered convex polygons, including nested and nonnested outer pairs. It also constructs a positive nonnesting discrepancy witness and checks finite members of the quarter-law sharpness family. Run `python3 verify.py`; its observed output is `VERIFY_OK exact_rational_assertions=3952 cases=3`. These finite checks confirm algebra and normalizations, not the global supremum over all directions, the general convex-body proof, or historical novelty; those are addressed analytically and bibliographically above.

## Relationship to prior work
Cheng and Basu, *A centerpoint theorem for three planar convex bodies* (first public version 26 September 2026, arXiv:2609.32953v1), prove the sharp lower bound \(2/9\) under midpoint inclusion for three planar slices. They do not classify exact depth for arbitrary centrally symmetric slices, introduce the signed outer-cap discrepancy, or determine the sharp non-midpoint equal-volume bound \(1/3\). Their setting permits nonsymmetric bodies and is therefore not subsumed by the present theorem.

The published result *Exact three-slice halfspace depth by reflected-core pairing* proves exact depth for the more specialized configuration \((rK,K,K)\), with an appropriate reflection inclusion and a general, possibly nonsymmetric convex \(K\). The present nested symmetric specialization agrees with that known result when \(K\) is symmetric, but the new theorem treats arbitrary mutually different centered convex slices, gives a nonnested discrepancy formula, characterizes inclusion by cap imbalance, and proves an equal-volume transverse-rectangle extremal law. These are not implications of the specialized published theorem. The earlier *Equal-area three-slice centerpoints improve to \(8/27\)* assumes midpoint inclusion and uses equality in Brunn--Minkowski to force all three equal-area slices to be translates; its conclusion is a lower bound, not the present non-midpoint exact formula.

Basic quasiconcavity of halfspace depth is classical; it is used, not claimed as new. The elementary cap identities are proved explicitly to clarify the full scope. No directly equivalent full three-slice discrepancy classification was found in the inspected literature, but unindexed equivalents remain possible.

## Limitations
The reduction to three candidate centers requires each slice to be centrally symmetric and their centers to be affinely aligned. The equal-volume sharp \(1/3\) is an infimum, not an attained minimum; without midpoint inclusion the three slices need not arise as all integer slices of one convex set. The formula is an exact variational representation through a halfspace discrepancy \(D\), not a closed elementary expression for arbitrary nonnested convex bodies. It does not address asymmetric slices, four or more layers, or the general mixed-integer centerpoint conjecture. Independent mathematical review and complete historical-priority verification have not been performed.

## References
1. H. Cheng and A. Basu, *A centerpoint theorem for three planar convex bodies*, arXiv:2609.32953v1 (first submitted 26 September 2026), https://arxiv.org/html/2609.32953v1, particularly Sections 1, 3 and 4.
2. *Exact three-slice halfspace depth by reflected-core pairing*, published result (2026), available in the public published-finding corpus mathematics collection, original RESULT.md inspected in full.
3. *Equal-area three-slice centerpoints improve to \(8/27\)*, published result (2026), available in the public published-finding corpus mathematics collection, original RESULT.md inspected in full.
4. A. Basu and T. Oertel, *Centerpoints: a link between optimization and convex geometry*, SIAM Journal on Optimization **27** (2017), 866–889, for the general mixed-integer centerpoint framework.
