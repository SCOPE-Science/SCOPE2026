# Global periodic decomposition and exact entrance tails at a reciprocal-slope resonance

## Finding

For every real \(k>1\), the normalized García-Grimaldo–Campos-Cantón four-branch map \(g_k:[-k,k]\to[-k,k]\), defined precisely below, has the following **complete global decomposition**. Put
\[
 t=1-\frac1k,\qquad p=\frac{k}{k+1},\qquad
 J_0=[0,t),\quad J_1=[-k,-1),\quad J_2=[-t,0),\quad J_3=[1,k),\quad
 P=\bigcup_{j=0}^3J_j.
\]
Every point of \(P\) has *least* period four, and its orbit visits \(J_0,J_1,J_2,J_3\) cyclically. The only other periodic orbit is the repelling least-period-two orbit \(\{-p,p\}\). Every other initial condition enters \(P\) after finitely many iterates. In particular there are no fixed points or periodic orbits of any other least period.

For normalized Lebesgue measure, with \(\tau(u)=\min\{n\ge0:g_k^n(u)\in P\}\), the exact nonentrance measure and uniform-initialization law are
\[
 \operatorname{Leb}\{u:g_k^j(u)\notin P\text{ for }0\le j\le n\}=\frac{2}{k^{n+1}},\qquad
 \mathbb P(\tau>n)=k^{-n-2}\quad(n\ge0),\qquad
 \mathbb E\tau=\frac1{k(k-1)}.
\]
The two-cycle has derivative multiplier \(k^2\) under its second return. The four-cycles have identity fourth return, not merely unit derivative, including one-sided branch endpoints.

Finally, every invariant Borel probability is uniquely of the form
\[
 \alpha\,\frac{\delta_{-p}+\delta_p}{2}+
 (1-\alpha)\int_{J_0}\left(\frac14\sum_{j=0}^3\delta_{g_k^j(u)}\right)\,d\rho(u),
 \qquad 0\le\alpha\le1,
\]
where \(\rho\) is an arbitrary Borel probability on \(J_0\), except that \(\rho\) is immaterial when \(\alpha=1\). In particular these orbit probabilities are exactly the ergodic invariant probabilities.

## Assumptions and scope

The previously introduced four-branch map has positive constants \(m_1,m_2,b_1\), with \(a=b_1/m_1\), \(b_2=m_2b_1/m_1\), and equations
\[
 f(x)=\begin{cases}
 m_1x+b_1,&-b_2\le x\le-a,\\
 m_2x+b_2,&-a<x<0,\\
 m_2x-b_2,&0\le x<a,\\
 m_1x-b_1,&a\le x\le b_2.
 \end{cases}
\]
Restrict to the **reciprocal-slope resonance** \(m_1=1/k\), \(m_2=k\), \(k>1\), with arbitrary \(b_1>0\). The change \(u=x/a\), \(a=kb_1\), gives the exactly conjugate self-map
\[
 g_k(u)=\begin{cases}
 (u+1)/k,&-k\le u\le-1,\\
 k(u+1),&-1<u<0,\\
 k(u-1),&0\le u<1,\\
 (u-1)/k,&1\le u\le k.
 \end{cases}
\]
All statements concern exact real arithmetic, including the specified half-open endpoint conventions. Lebesgue measure above refers to length in the normalized coordinate \(u\); the probability uses the uniform distribution on \([-k,k]\). Conjugacy transfers the orbit classification to the original coordinate \(x\).

## Proof

**(1) A four-interval identity.** Since \(0<t<1\), the four half-open intervals are disjoint. Directly evaluating their endpoint images gives
\[
 g_k(J_0)=J_1,\quad g_k(J_1)=J_2,\quad
 g_k(J_2)=J_3,\quad g_k(J_3)=J_0.
\]
For an arbitrary \(u\in J_0\), successive exact branch formulas are
\[
 u\longmapsto k(u-1)\longmapsto u-t
 \longmapsto ku+1\longmapsto u.
\]
Thus \(g_k^4\) is the identity on \(J_0\), hence on all of \(P\) by the cyclic permutation. All four intervals are disjoint, so every point in \(P\) has least period four. The endpoint \(u=0\) is included in \(J_0\) and follows the same identities.

**(2) Every remaining orbit either enters \(P\) or is one repelling two-cycle.** The complement of \(P\) in \([-k,k]\) consists of the two open strips
\[
 E_-=(-1,-t),\qquad E_+=(t,1)
\]
and the three points \(-1,t,k\). The latter points enter \(P\) in at most three iterations because
\[
 k\longmapsto t\longmapsto-1\longmapsto0\in P.
\]
On \(E_-\), the map is the increasing affine function \(k(u+1)\) with image \((0,1)\); on \(E_+\) it is \(k(u-1)\) with image \((-1,0)\). Therefore an orbit avoiding \(P\) indefinitely must avoid the three exceptional points and alternate strictly between \(E_+\) and \(E_-\). On any such alternating orbit, two iterates starting in \(E_+\) satisfy
\[
 g_k^2(u)=k^2u-k^2+k,
 \qquad g_k^2(u)-p=k^2(u-p),\qquad p=\frac{k}{k+1}.
\]
As \(k^2>1\), boundedness of all the even iterates in the fixed strip \(E_+\) forces \(u=p\). Its alternating partner is \(-p\), and \(p-t=1/[k(k+1)]>0\) places the pair strictly inside the strips. This proves the periodic census, finite entrance for every other point, and the repelling two-step multiplier. This argument also excludes any orbit that could have a different period.

**(3) Exact tail of the entrance time.** At time zero the complement of \(P\) has Lebesgue length \(2/k\). To remain out of \(P\) at consecutive steps (apart from finitely many negligible boundary preimages), the orbit must alternate between the two strips. Each entire target strip has a unique inverse image under the relevant affine branch of slope \(k\), and that inverse image lies strictly within the preceding strip. Thus each additional avoidance step multiplies total surviving length by exactly \(1/k\). Induction yields \(2/k^{n+1}\) for simultaneous avoidance at times \(0,1,\ldots,n\). Dividing by the domain length \(2k\) proves \(\mathbb P(\tau>n)=k^{-n-2}\). The repelling pair has zero Lebesgue measure. The standard tail-sum identity gives
\[
 \mathbb E\tau=\sum_{n=0}^\infty\mathbb P(\tau>n)
 =\sum_{n=0}^\infty k^{-n-2}=\frac1{k(k-1)}.
\]

**(4) Complete invariant probability simplex.** Every point outside \(P\cup\{-p,p\}\) eventually enters the strictly forward-invariant set \(P\), and hence cannot return to any neighborhood confined to its initial complement after sufficiently many iterates. No such point is recurrent. By Poincaré recurrence, each invariant Borel probability gives zero mass to this transient set. Its restriction to the two-cycle is a multiple of the equal two-point probability. Every four-cycle has exactly one point in the Borel selector \(J_0\), so disintegration by the selector gives an arbitrary probability \(\rho\) on \(J_0\) and equal mass at the four points in each selected cycle. This proves the stated form and exhausts the ergodic components.

## Verification

The associated standalone `verify.py` checks the universal branch-composition identities symbolically with SymPy and checks **1,907 further exact rational assertions** for seven rational values of \(k\): cyclic interval images, fourth-return identities, the repelling two-cycle, exceptional endpoints, finite transient entrance, and exact lengths of finite-time survivor intervals. Execute `python verify.py` with Python and SymPy available. These finite checks are corroborative only; the quantified global assertions follow from the proof above.

## Relationship to prior work

García-Grimaldo and Campos-Cantón (2021) introduced the fixed-point-free class and discussed chaotic parameter values. García-Grimaldo and collaborators (2023) displayed the exact four-branch equation and numerically examined bifurcations and Lyapunov exponents, but did not state a global all-point classification at the reciprocal-slope resonance. A related **restricted-itinerary** calculation already gives a family of neutral least-period-four cycles at this resonance. That established family is not claimed as independently new here: the new contribution is the *exhaustive* periodic spectrum, proof of finite-time absorption outside one repelling pair, exact geometric entrance-tail law, and classification of **all** invariant probabilities. Existing periodic-orbit results for different interval maps cannot imply this global conclusion without identifying the particular map's complementary branches and preimages.

## Limitations

This is a codimension-one parameter family, not a classification for arbitrary independent inner and outer slopes. No claim is made about hardware finite-precision behavior or cryptographic security. The 2021 defining article could be inspected only via its accessible first-page and abstract: lawful full-text access was not obtained, so possible stronger results in its uninspected sections remain a publication-priority risk. A later comparative chapter was likewise accessible only at the abstract level. Other unpublished or unindexed equivalent results may exist. Independent mathematical audit has not been performed.

## References

1. C. García-Grimaldo and E. Campos-Cantón, *Chaotic Features of a Class of Discrete Maps without Fixed Points*, International Journal of Bifurcation and Chaos 31 (2021), 2150200. DOI: 10.1142/S021812742150200X. Public date: 2021-10-26.
2. C. García-Grimaldo, C. F. Bermudez-Marquez, E. Tlelo-Cuautle, and E. Campos-Cantón, *FPGA Implementation of a Chaotic Map with No Fixed Point*, Electronics 12 (2023), 444. DOI: 10.3390/electronics12020444. Public date: 2023-01-14. The openly available article was inspected throughout its dynamics discussion.
3. C. García-Grimaldo and E. Campos-Cantón, *Comparative Analysis of Chaotic Features of Maps Without Fixed Points*, in *Complex Systems and Their Applications* (2022), pp. 151–176. DOI: 10.1007/978-3-031-02472-6_8 (abstract consulted).
