# An exact star-shaped full shadow with no transient zeros for regular root polygons

## Finding
For every integer \(d\ge3\) and every \(a\in\mathbb C\setminus\{0\}\), let \(P(z)=z^d-a\). Choose \(\lambda\ne0\) with \(\lambda^d=a\), and let \(\omega=e^{2\pi i/d}\). The *full shadow* \(S_P\) is the closure of the union of the complex zeros of \((P^n)^{(m)}\), over **every** integer \(n\ge1\) and every derivative order \(0\le m<dn\). The *limiting core* \(K_P\) is the limiting set defined by the pooled, normalized descendant-root measures of Hägg and Shapiro [1]; the *transient set* is \(T_P=S_P\setminus K_P\).

Then the full shadow and limiting core coincide with the regular \(d\)-spoke star, with no transient zeros:
\[
S_P=K_P=\bigcup_{j=0}^{d-1}\{\lambda\omega^j t:0\le t\le1\},\qquad T_P=\varnothing.
\]
In particular, these sets have Hausdorff dimension one and zero planar Lebesgue measure, although the convex hull of the roots has nonempty interior.

The stronger *all finite levels* statement is as follows. For integers \(n\ge1\), \(0\le m<dn\), let \(r_m\in\{0,\ldots,d-1\}\) be the least nonnegative residue of \(-m\) modulo \(d\), and set
\[
q_m=\frac{dn-m-r_m}{d},\qquad e_m=\max(n-m,0),\qquad k_m=q_m-e_m.
\]
There is a real polynomial \(Q_{d,n,m}\), of degree \(q_m\), with \(Q_{d,n,m}(0)\ne0\), such that
\[
(P^n)^{(m)}(\lambda w)=c_{d,n,m}\,w^{r_m}Q_{d,n,m}(w^d),\qquad c_{d,n,m}\ne0.
\]
Its zero at \(u=1\) has multiplicity exactly \(e_m\); its remaining \(k_m\) zeros are **distinct and strictly inside** \((0,1)\). There are no other zeros of \(Q_{d,n,m}\). Thus the descendant has a zero at the star center of multiplicity \(r_m\) when \(r_m>0\), \(d\) simple zeros of equal radius for each interior zero of \(Q_{d,n,m}\), and original vertices of multiplicity \(e_m\) when \(e_m>0\). This accounts for every zero, with multiplicity. The same elementary finite-level statement holds at \(d=2\), where the star is the familiar real segment.

## Assumptions and scope
All statements are over \(\mathbb C\), with \(d\ge3\), \(a\ne0\), \(n\ge1\), and the full range of nonconstant descendants \(0\le m<dn\). The choice of \(\lambda\) only relabels the spokes. The conclusion concerns the complete union of **all** derivative orders and powers, and the core defined in [1], rather than a single fixed-ratio zero limit. The polynomial \(P\) has \(d\) distinct vertices and its only critical point is the center.

## Proof
**1. Normalization and exact derivative recurrence.** With \(z=\lambda w\), differentiation introduces only nonzero scalar factors, so it is enough to prove the assertions for \(p(w)=w^d-1\). Fix \(n\). Set \(Q_0(u)=(u-1)^n\), \(r_0=0\), and construct \(Q_m\) recursively, suppressing harmless nonzero scalar factors:
\[
Q_{m+1}(u)=\begin{cases}
Q_m'(u),&r_m=0,\\
r_m Q_m(u)+d uQ_m'(u),&1\le r_m\le d-1.
\end{cases}
\]
Indeed, the chain rule applied to \(w^{r_m}Q_m(w^d)\) gives a factor \(d w^{d-1}Q_m'(w^d)\) if \(r_m=0\), and a factor \(w^{r_m-1}[r_mQ_m(w^d)+d w^dQ_m'(w^d)]\) if \(r_m>0\). Thus \(r_{m+1}\equiv-(m+1)\pmod d\), and comparison of the leading degree gives \(\deg Q_m=q_m\). In the first case \(\deg Q_m\ge1\), since \(m<dn\) and \(r_m=0\) imply \(dn-m\ge d\).

**2. Root-localization lemma, including the endpoints.** We prove by induction that every \(Q_m\) has only positive roots in \((0,1]\), that roots in \((0,1)\) are simple, and that \(Q_m(0)\ne0\). This is true for \(Q_0\), whose only root is \(1\), of multiplicity \(n\). Suppose a polynomial \(Q\) of degree \(q\) has \(k\) distinct roots in \((0,1)\) and a root at \(1\) of multiplicity \(e\), where \(q=k+e\), with \(Q(0)\ne0\).

If \(r=0\), Rolle's theorem places one simple root of \(Q'\) between each consecutive distinct positive roots. If \(e>0\), the endpoint contributes multiplicity \(e-1\) at \(1\); the exact total is \(q-1\), the degree of \(Q'\). If \(e=0\), Rolle gives the \(q-1\) simple interior roots of \(Q'\). No further roots exist, and \(Q'(0)\ne0\) because \(Q'(0)/Q(0)=-\sum_j\mu_j/t_j\), summing over all positive roots with multiplicities \(\mu_j\).

If \(1\le r<d\), set \(f(u)=u^{r/d}Q(u)\) on \([0,1]\). It vanishes at \(u=0\) and at all positive roots of \(Q\). Since
\[
d u^{1-r/d}f'(u)=rQ(u)+d uQ'(u),
\]
Rolle's theorem supplies one simple interior root between \(0\) and the first positive root and between every pair of successive positive roots. A root at \(1\) of multiplicity \(e>0\) leaves multiplicity \(e-1\) there after differentiation. Consequently we find all \(q\) roots, counted with multiplicity, of \(rQ+d uQ'\), since its leading coefficient is \((r+dq)\) times that of \(Q\). These interior roots are simple, and its constant term \(rQ(0)\) is nonzero. The case \(q=0\) is immediate. This closes the induction.

The endpoint multiplicity also follows from the induction, **including orders beyond \(m=n\)**. The starting polynomial \(Q_0=(u-1)^n\) has endpoint multiplicity \(n\). In either recurrence case the root-counting argument shows that a positive endpoint multiplicity decreases by exactly one, while if the endpoint multiplicity is zero, *all* roots of the next reduced polynomial lie strictly below \(1\), so a vertex zero cannot reappear. Therefore \(Q_m\) has endpoint multiplicity exactly \(e_m=\max(n-m,0)\) for every \(m\); its other \(q_m-e_m\) roots are simple in \((0,1)\). This stronger induction argument is needed for \(m>n\), because local differentiation of a general multiple-root polynomial alone does not rule out later accidental zeros. The factorization gives the claimed complete finite-level classification.

**3. From radial localization to the exact shadow.** Let \(\mathcal T\) be the closed star of the theorem. The finite-level root classification shows every descendant zero lies in \(\mathcal T\), so \(S_P\subseteq\mathcal T\). By Theorem 1.4(i) of Hägg and Shapiro [1], \(K_P\subseteq S_P\) is compact and connected and contains all \(d\) vertices of \(P\). A connected subset of the tree \(\mathcal T\) containing all its leaves must contain every intervening point: deleting an interior point on a spoke disconnects that leaf from every other leaf. Therefore \(\mathcal T\subseteq K_P\subseteq S_P\subseteq\mathcal T\), giving equality and \(T_P=\varnothing\). The general scaling \(\lambda\) follows from the chain rule and the affine covariance of the shadow and core in [1, Proposition 5.2].

## Verification
The separate `check_star.py` uses exact integer polynomial differentiation and symbolic real-root counting to independently test the congruence factorization, endpoint multiplicities, and simple interior root census for every \(d=2,3,\ldots,7\), every \(n=1,2,\ldots,6\), and every \(0\le m<dn\) (567 derivatives). It also checks the explicit recurrence against direct differentiation. Run with `python check_star.py` with SymPy installed. Finite checks do not prove the infinite-parameter theorem; the Rolle root count and the cited connectedness theorem establish the universal statements.

For example, \(( (w^3-1)^2 )''=6w(5w^3-2)\), so its noncentral roots lie on the three spokes at radius \((2/5)^{1/3}\). The full shadow needs **all** derivative orders and powers, not just this example.

## Relationship to prior work
Hägg and Shapiro [1, Theorems 1.3 and 1.4] introduce the full shadow and establish, in general, a connected limiting core and potentially nonempty transient set. Their Theorem 1.6 exhibits quartics with infinitely many transients. The present argument uses their connectedness theorem but supplies an exact finite-level radial zero-confinement and multiplicity lemma to determine **both** sets for every regular root polygon, proving absence of transients. The general connectedness theorem alone does not give that radial confinement.

Bøgvad, Hägg, and Shapiro [2] study fixed-ratio asymptotic descendants, including the classical quadratic case (Section 6); their Section 7 discusses regular polygons as exceptional to a generic configuration conjecture. It does not state the full-shadow classification for degrees at least three. Symmetric multi-orthogonal families supported on three-stars [3] and orthogonal polynomials on radial rays [4] share aspects of the geometry, but address different polynomial sequences and do not directly determine the double-indexed derivatives and their full-shadow/transient decomposition. This comparison establishes a distinction among the inspected statements, not a claim that all unindexed literature has been exhausted.

## Limitations
The exact geometric equality applies only to affine-normalized regular root polygons \(z^d-a\) with \(a\ne0\), not arbitrary polynomials with roots in convex position. The core equality relies on the connectedness result [1]. Neither an explicit limiting radial density for a fixed derivative-to-power ratio nor a stability theorem for perturbed vertices is proved here. The literature comparison is bounded; an earlier equivalent special-case analysis not found in the inspected sources remains possible. No independent review has been performed.

## References
[1] Christian Hägg and Boris Shapiro, *The full shadow of a polynomial I. The limiting core and the transient set*, arXiv:2610.09602v1 (first publicly posted 2026-10-07), especially Theorem 1.4 and Proposition 5.2. https://arxiv.org/abs/2610.09602

[2] Rikard Bøgvad, Christian Hägg, and Boris Shapiro, *Rodrigues' Descendants of a Polynomial and Boutroux Curves*, *Constructive Approximation* 59 (2024), 737–798; arXiv:2107.05710; doi:10.1007/s00365-023-09657-x.

[3] Ana F. Loureiro and Walter Van Assche, *Three-fold symmetric Hahn-classical multiple orthogonal polynomials*, *Analysis and Applications* 18 (2020), 271–332; doi:10.1142/S0219530519500106.

[4] Gradimir V. Milovanović, *Orthogonal Polynomials on Radial Rays in the Complex Plane: Construction, Properties and Applications*, *Axioms* 14 (2025), article 65; doi:10.3390/axioms14010065. Earlier open preprint: https://www.preprints.org/manuscript/202412.1898.
