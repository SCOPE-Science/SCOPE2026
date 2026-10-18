# Scientific review

## Correctness: PASS
The central-section and orthogonal-projection formulas follow from standard linear Jacobians and a cofactor identity. Their quotient is the product of opposite quadratic forms. The sharp maximum is proved by a spectral endpoint inequality with an equality classification of four directions. A direct local chart gives the positive-definite deficit \(B s^2+D y^2\) with \(D=(B-A-C)/2>0\); the spherical area form is exactly \(d\theta\,dy\), so four elliptical caps prove the claimed coefficient with the correct Haar normalization. The inverse calculation gives exactly the roots \(t\) and \(k/t\); direct polar substitution proves this ambiguity cannot be removed. Symbolic/rational identities and independently integrated finite examples were checked by `checker.py`; these finite tests are not substitutes for the proof. The theorem excludes repeated eigenvalues and nonellipsoids.

## Originality: PASS, with residual priority risk
The closest inspected geometric-tomography papers treat full parallel section functions (Fish–Ryabogin–Sun–Yaskin), or the separate one-dimensional distributions of sections and projections (Kim–Yaskin–Zvavitch). Neither establishes a same-direction ratio upper-tail coefficient or its two-statistic shape inverse. Hillier's source was accessible only through the abstract and bibliographic information: it treats the density of a **single** spherical quadratic form; coverage by an unpublished equivalent or a broader joint-form theorem cannot be excluded. Two nearby published geometric findings reconstruct axes from negative section moments or describe one-spike random radii; those measurements do not imply this ratio's two-statistic recovery. Classical Kantorovich theory supplies the maximum, not the sharp random cap mass and its inverse. Complete historical uniqueness cannot be certified from literature searches.

## Mathematical value: PASS
This is a motivated, scale-invariant inverse problem for correlated section and projection measurements in the same direction. Instead of requiring entire direction-labeled functions or complete marginal laws, it shows how two precise features of **one scalar random quotient** recover a triaxial shape, and proves a necessary polarity obstruction. The explicit sharp near-extremal mass quantifies the geometric scarcity of almost-extremal viewing directions and is a natural benchmark for geometric tomography; it is not merely a restatement of the deterministic Kantorovich bound.

## Limitations
The inverse is at the ideal population level, requires three simple positive eigenvalues, and is not statistically conditioned near axis collisions. Only identified accessible primary material was inspected; Hillier's full text could not be accessed. The polar pair has the same complete quotient law pointwise, so a stronger inverse result without extra data would be false.

Self-review: passed. Independent audit: not yet performed.
